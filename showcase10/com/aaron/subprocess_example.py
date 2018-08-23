# -*- codiing:utf-8 -*-
"""
subprocess use example
"""
__author__="aaron.qiu"

import subprocess

if __name__=='__main__':
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    # print(output.decode('utf-8'))
    # print(output.decode('latin-1'))
    print(output.decode('ISO-8859-1'))
    print('Exit code:', p.returncode)



