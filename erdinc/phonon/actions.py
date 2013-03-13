#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import qt4
from pisi.actionsapi import get

import os

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().partition("_")[0])

def setup():
    cmaketools.configure('-DCMAKE_SKIP_RPATH:BOOL=YES')

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    if get.buildTYPE() == "emul32": return

    #some applications like mediaplayer example of Qt needs this #11648
    pisitools.dosym("/usr/include/KDE/Phonon", "/usr/include/Phonon")
