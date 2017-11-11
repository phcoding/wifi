from __future__ import absolute_import
import sys
import argparse
import wifi.wifilib as wifilib

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--action', help='action to login or logout.', default='login')
    parser.add_argument('-u', '--username', help='username to login wifi.', default='username', type=str)
    parser.add_argument('-p', '--password', help='password to login wifi.', default='password', type=str)
    args = parser.parse_args()
    if args.action == 'logout':
        # wifi logout
        try:
            print(wifilib.wifi_logout(args.username, args.password))
        except Exception as e:
            print("Wifi logout error !")
            print(e)
    else:
        # wifi login
        try:
            mess = wifilib.wifi_login(args.username, args.password)
            if mess.lower().find('ok') != -1:
                print("Wifi login succeed !")
            else:
                print("Wifi login error !")
                print(mess)
        except Exception as e:
            print("Wifi login error !")
            print(e)

if __name__ == '__main__':
    sys.exit(main())