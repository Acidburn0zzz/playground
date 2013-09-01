#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.flags.add(" -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_GNU_SOURCE -fPIC")

    autotools.configure("--datadir=/usr/share/misc \
                         --disable-static \
                         --enable-fsect-man5")

    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", 'hardcode_libdir_flag_spec=""')
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("python")
    pythonmodules.install()

    shelltools.cd("..")
    pisitools.dodoc("ChangeLog", "MAINT", "README")
