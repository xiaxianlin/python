# -*- coding: utf-8 -*-
import sys
import commands
repos = sys.argv[1]
rev = sys.argv[2]


authorShell = "svnlook author -r %s %s" % (rev,repos)
changeFileShell = "svnlook changed -r %s %s" % (rev,repos)
changeDirShell = "svnlook dirs-changed -r %s %s" % (rev,repos)
messageShell = "svnlook log -r %s %s" % (rev,repos)
(status, author) = commands.getstatusoutput(authorShell)
(status, fileString) = commands.getstatusoutput(changeFileShell)
files = [i.split('   ') for i in fileString.split('\n')]
(status, dirs) = commands.getstatusoutput(changeDirShell)
(status, message) = commands.getstatusoutput(messageShell)
print author
print message
print dirs