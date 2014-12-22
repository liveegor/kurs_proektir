#!/usr/bin/python
# -*- coding: utf-8 -*-

# Call if this is main module
# (not included)
if __name__ == '__main__':
    import os
    import subprocess
    PIPE = subprocess.PIPE
    lst = os.listdir('.')
    for name in lst:
        if name[-3:] == '.ui':
            cmd = 'pyuic4 -o {}.py {}.ui'.format('../Translated_UI_Forms/' + name[:-3], name[:-3])
            proc = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, \
                stderr=subprocess.STDOUT, close_fds=True)
    print proc.stdout.read()