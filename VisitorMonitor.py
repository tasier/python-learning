# -*- coding: UTF-8 -*-

import sys
import paramiko


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

    def has_new_visitr(self):
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
            serverLastAccessTime = str(stdout.read()).strip()


            local_file = open(local_log_file, 'r+')
            try:
                lastAccessTime = local_file.readline().strip()

                if cmp(serverLastAccessTime, lastAccessTime) == 0:
                    print 'There is no new visitor'
                    return False
                else:
                    local_file.seek(0)
                    local_file.write(serverLastAccessTime)
                    access_date = str(serverLastAccessTime)[0:19]
                    print 'New visitors had come at '+access_date
                    return True
            finally:
                local_file.close()

        finally:
            client.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Please input username and password !'
        sys.exit(-1)

    username = sys.argv[1]
    password = sys.argv[2]
    account = Account(username, password)

    server = ServerSite('115.156.163.234', 22)

    visitor = VisitorMonitor(account, server)
    visitor.has_new_visitr()

