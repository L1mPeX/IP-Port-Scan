import socket


def openports(ip):
    for port in [21, 22, 23, 25, 43, 45, 53, 68, 80, 110, 115, 119, 123, 135, 139, 143, 161, 179, 220, 389, 443, 445,
                 993, 1723, 2049, 3306, 3389, 5060, 8080, 9091, 9090, 1164]:
        try:
            sock = socket.socket()
            sock.settimeout(0.7)
            sock.connect((ip, port))
            print('port :: %s' % port, ':: open')
            sock.close()
        except:
            print('port :: %s' % port, ':: closed')


if __name__ == '__main__':
    openports(input('IP: '))
