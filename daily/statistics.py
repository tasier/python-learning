# *-* coding: UTF-8 *-*


if __name__ == '__main__':
    with open('test.log', 'r') as test_log:
        ip_accesstime = [line.strip().split(',')[-2::-1] for line in test_log]
        # print ip_accesstime

        ips = [item[0] for item in ip_accesstime]
        ip_to_num = {}
        for ip in ips:
            if ip not in ip_to_num:
                ip_to_num[ip] = 1
            else:
                ip_to_num[ip] += 1

        # for item in ip_to_num:
        #     print item, ip_to_num[item]

        ip_to_lastaccesstime = {}
        maxFunc = lambda x, y: x if cmp(x, y) else y
        for item in ip_accesstime:
            ip = item[0]
            time = item[1]
            if ip not in ip_to_lastaccesstime:
                ip_to_lastaccesstime[ip] = time
            else:
                ip_to_lastaccesstime[ip] = maxFunc(time,ip_to_lastaccesstime[ip])

        for item in ip_to_lastaccesstime:
            print item, ip_to_lastaccesstime[item]