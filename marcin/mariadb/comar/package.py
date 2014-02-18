#!/usr/bin/python

import os
import shutil

DATADIR = "/var/log/mysql"
DATADIRMODE = 0700

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if toRelease and toRelease in [str(r) for r in range(1,2)] and (not fromRelease or fromRelease == "1"):
        os.system("rm -rf %s" % DATADIR)
        if os.path.exists("/etc/mysql/my.cnf.newconfig"):
            if os.path.exists("/etc/mysql/my.cnf"): os.remove("/etc/mysql/my.cnf")
            shutil.copy2("/etc/mysql/my.cnf.newconfig", "/etc/mysql/my.cnf")
            os.remove("/etc/mysql/my.cnf.newconfig")

    os.system("/sbin/mudur_tmpfiles.py /usr/lib/tmpfiles.d/mariadb.conf")

    # On first install...
    if not os.path.exists(DATADIR):
        os.makedirs(DATADIR, DATADIRMODE)
        # Create the database
        os.system("/usr/bin/mysql_install_db --datadir=/var/lib/mysql --basedir=/usr --user=mysql --force")
        os.system("/bin/chown -R mysql:mysql %s" % DATADIR)
