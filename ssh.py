# -*- coding: UTF-8 -*-

import paramiko
import sys


def test():
    'paramiko ssh test'

    if len(sys.argv) != 3:
        print 'input username and password'
        sys.exit(-1)

    args = sys.argv
    username, password = args[1], args[2]
    print username, password

    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        hostname = '115.156.163.234'
        port = 22

        client.connect(hostname=hostname, port=port, username=username, password=password)
        stdin, stdout, stderr = client.exec_command('ls -l')

        print stdout.read()
    except Exception,e:
        print e
    finally:
        client.close()


if __name__ == '__main__':
    test()