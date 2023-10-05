#!/usr/bin/env python3
import os
import re
import sys

def main():
    for line in sys.stdin:
        match = re.match(r'^#', line)  

        fields = line.strip().split(':')

        if match or len(fields) != 5:
            continue

        username = fields[0]
        password = fields[1]

        gecos = "{} {} , , ,".format(fields[3], fields[2])

        groups = fields[4].split(',')

        print("==> Creating account for {}...".format(username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '{}' {}".format(gecos, username)
        os.system(cmd)

        print("==> Setting the password for {}...".format(username))
        cmd = "/bin/echo -ne '{}\\n{}' | /usr/bin/sudo /usr/bin/passwd {}".format(password, password, username)
        os.system(cmd)

        for group in groups:
            if group != '-':
                print("==> Assigning {} to the {} group...".format(username, group))
                cmd = "/usr/sbin/adduser {} {}".format(username, group)
                os.system(cmd)

if __name__ == '__main__':
    main()

