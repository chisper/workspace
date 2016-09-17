#!/usr/bin/env python 

from ftplib import FTPcd
f = FTP('ftp.ibiblio.org')
print "Welcome:",f.getwelcome()
f.login()

print "CWD:",f.pwd()
f.quit()