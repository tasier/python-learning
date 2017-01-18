# -*- coding: UTF-8 -*-

import sys
import paramiko
from VisitorDecorators import console_log


class Account(object):
    'account message'
    def __init__(self, username, password):
        if isinstance(username, str) and isinstance(password, str):
            self.username = username
            self.password = password
        else:
            self.username = ''
            self.password = ''


class ServerSite(object):
    'the hust1000 web site server'
    def __init__(self, ip, port):
        if isinstance(ip, str) and isinstance(port, int):
            self.ip = ip
            self.port = port
        else:
            self.ip = 'localhost'
            self.port = 22


class VisitorMonitor(object):
    'monitor hust1000 website visitor'
    def __init__(self, account, server):
        if isinstance(account, Account) and isinstance(server, ServerSite):
            self.account = account
            self.server = server
        else:
            self.account = None
            self.server = None

    @console_log
    def has_new_visitor(self):
        log_dir = '/var/lib/tomcat/webapps/hust1000/logs/'
        visit_log_file = 'visit.log'
        local_log_file = 'visit-has-new-visitor.log'

        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            hostname = self.server.ip
            port = self.server.port

            username = self.account.username
            password = self.account.password

            client.connect(hostname=hostname, port=port, username=username, password=password)

            # cd /var/lib/tomcat/webapps/hust1000/logs/
            # stat -c '%y,%Y' visit.log
            res = client.exec_command('cd '+log_dir+'; '+"stat -c '%y,%Y' "+visit_log_file)
            stdout = res[1]
            server_last_access_time = str(stdout.read()).strip()

            with open(local_log_file, 'r+') as local_file:
                last_access_time = local_file.readline().strip()

                if cmp(server_last_access_time, last_access_time) == 0:
                    print 'There is no new visitor'
                    return False
                else:
                    local_file.seek(0)
                    local_file.write(server_last_access_time)
                    access_date = str(server_last_access_time)[0:19]
                    print 'New visitors had come at ' + access_date
                    return True
        except Exception, e:
            print e
        finally:
            client.close()


    @console_log
    def ip_statistics(self):
        log_dir = '/var/lib/tomcat/webapps/hust1000/logs/'
        visit_log_file = 'visit.log'

        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            hostname = self.server.ip
            port = self.server.port

            username = self.account.username
            password = self.account.password

            client.connect(hostname=hostname, port=port, username=username, password=password)

            #cat /var/lib/tomcat/webapps/hust1000/logs/visit.log
            res = client.exec_command('cat '+log_dir+visit_log_file)
            stdout = res[1]
            #获取日志内容
            filecontent = str(stdout.read()).strip().split('\n')

            #截取 ip和时间 信息
            ip_accesstime = [line.strip().split(',')[-2::-1] for line in filecontent]


            #统计 ip-访问次数
            ips = [item[0] for item in ip_accesstime]
            ip_to_num = {}
            for ip in ips:
                if ip not in ip_to_num:
                    ip_to_num[ip] = 1
                else:
                    ip_to_num[ip] += 1

            print '------Ip-VisitTimes-------'
            for item in ip_to_num:
                print item, '-', ip_to_num[item]


            #统计 ip-最后访问时间
            ip_to_lastaccesstime = {}
            maxFunc = lambda x, y: x if cmp(x, y) else y
            for item in ip_accesstime:
                ip = item[0]
                time = item[1]
                if ip not in ip_to_lastaccesstime:
                    ip_to_lastaccesstime[ip] = time
                else:
                    ip_to_lastaccesstime[ip] = maxFunc(time, ip_to_lastaccesstime[ip])

            print '------Ip-LastAccessTime-------'
            for item in ip_to_lastaccesstime:
                print item, '-', ip_to_lastaccesstime[item]

        finally:
            client.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Please input username and password !'
        sys.exit(-1)

    username = sys.argv[1]
    password = sys.argv[2]
    account = Account(username, password)

    ip = '115.156.163.234'
    port = 22
    server = ServerSite(ip, port)

    visitor = VisitorMonitor(account, server)
    visitor.has_new_visitor()
    visitor.ip_statistics()

