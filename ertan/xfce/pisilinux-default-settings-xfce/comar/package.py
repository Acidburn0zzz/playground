#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi import api as pisiapi
import platform
import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    environments = open ("/usr/lib/python2.7/site-packages/pds/environments.py","r")
    environments_array = environments.readlines()
    x= 0
    for i in range(0,environments_array.__len__()):
        if environments_array[i].find("DefaultIconTheme     = 'hicolor'") != -1:
            environments_array[i] ="    DefaultIconTheme     = 'oxygen'\n"
            x = 42
            break
    environments.close()
    if x != 0:
        environments = open("/usr/lib/python2.7/site-packages/pds/environments.py","w")
        environments.writelines(environments_array)
        environments.close()

    fileassociations = open("/usr/share/applications/mimeapps.list","a")
    fileassociations.write("application/arj=xarchiver.desktop;\n")
    fileassociations.write("application/csv=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/excel=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/msexcel=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/mspowerpoint=ooo-presentation.desktop;\n")
    fileassociations.write("application/msword=ooo-textdoc.desktop;\n")
    fileassociations.write("application/ogg=parole.desktop;\n")
    fileassociations.write("application/pdf=epdfview.desktop;\n")
    fileassociations.write("application/ram=parole.desktop;\n")
    fileassociations.write("application/rtf=ooo-textdoc.desktop;\n")
    fileassociations.write("application/sdp=parole.desktop;\n")
    fileassociations.write("application/smil=parole.desktop;\n")
    fileassociations.write("application/smil+xml=parole.desktop;\n")
    fileassociations.write("application/tab-separated-values=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/vnd.lotus-1-2-3=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/vnd.ms-excel=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/vnd.ms-excel.sheet.binary.macroEnabled.12=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/vnd.ms-excel.sheet.macroEnabled.12=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/vnd.ms-excel.template.macroEnabled.12=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/vnd.ms-powerpoint=ooo-presentation.desktop;\n")
    fileassociations.write("application/vnd.ms-powerpoint.presentation.macroEnabled.12=ooo-presentation.desktop;\n")
    fileassociations.write("application/vnd.ms-powerpoint.slideshow.macroEnabled.12=ooo-presentation.desktop;\n")
    fileassociations.write("application/vnd.ms-powerpoint.template.macroEnabled.12=ooo-presentation.desktop;\n")
    fileassociations.write("application/vnd.ms-word.document.macroEnabled.12=ooo-textdoc.desktop;\n")
    fileassociations.write("application/vnd.ms-word.template.macroEnabled.12=ooo-textdoc.desktop;\n")
    fileassociations.write("application/vnd.ms-works=ooo-textdoc.desktop;\n")
    fileassociations.write("application/vnd.oasis.opendocument.chart=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/vnd.oasis.opendocument.chart-template=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/vnd.oasis.opendocument.database=ooo-database.desktop;\n")
    fileassociations.write("application/vnd.oasis.opendocument.formula=ooo-formula.desktop;\n")
    fileassociations.write("application/vnd.oasis.opendocument.formula-template=ooo-formula.desktop;\n")
    fileassociations.write("application/vnd.oasis.opendocument.graphics=ooo-drawing.desktop;\n")
    fileassociations.write("application/vnd.oasis.opendocument.graphics-template=ooo-drawing.desktop;\n")
    fileassociations.write("application/vnd.oasis.opendocument.presentation=ooo-presentation.desktop;\n")
    fileassociations.write("application/vnd.oasis.opendocument.presentation-template=ooo-presentation.desktop;\n")
    fileassociations.write("application/vnd.oasis.opendocument.spreadsheet=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/vnd.oasis.opendocument.spreadsheet-template=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/vnd.oasis.opendocument.text=ooo-textdoc.desktop;\n")
    fileassociations.write("application/vnd.oasis.opendocument.text-master=ooo-textdoc.desktop;\n")
    fileassociations.write("application/vnd.oasis.opendocument.text-template=ooo-textdoc.desktop;\n")
    fileassociations.write("application/vnd.oasis.opendocument.text-web=ooo-web.desktop;\n")
    fileassociations.write("application/vnd.openofficeorg.extension=ooo-extension-manager.desktop;\n")
    fileassociations.write("application/vnd.openxmlformats-officedocument.presentationml.presentation=ooo-presentation.desktop;\n")
    fileassociations.write("application/vnd.openxmlformats-officedocument.presentationml.slideshow=ooo-presentation.desktop;\n")
    fileassociations.write("application/vnd.openxmlformats-officedocument.presentationml.template=ooo-presentation.desktop;\n")
    fileassociations.write("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/vnd.openxmlformats-officedocument.spreadsheetml.template=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/vnd.openxmlformats-officedocument.wordprocessingml.document=ooo-textdoc.desktop;\n")
    fileassociations.write("application/vnd.openxmlformats-officedocument.wordprocessingml.template=ooo-textdoc.desktop;\n")
    fileassociations.write("application/vnd.rn-realmedia=parole.desktop;\n")
    fileassociations.write("application/vnd.stardivision.calc=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/vnd.stardivision.chart=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/vnd.stardivision.draw=ooo-drawing.desktop;\n")
    fileassociations.write("application/vnd.stardivision.impress=ooo-presentation.desktop;\n")
    fileassociations.write("application/vnd.stardivision.math=ooo-formula.desktop;\n")
    fileassociations.write("application/vnd.stardivision.writer=ooo-textdoc.desktop;\n")
    fileassociations.write("application/vnd.stardivision.writer-global=ooo-textdoc.desktop;\n")
    fileassociations.write("application/vnd.sun.xml.base=ooo-database.desktop;\n")
    fileassociations.write("application/vnd.sun.xml.calc=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/vnd.sun.xml.calc.template=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/vnd.sun.xml.draw=ooo-drawing.desktop;\n")
    fileassociations.write("application/vnd.sun.xml.draw.template=ooo-drawing.desktop;\n")
    fileassociations.write("application/vnd.sun.xml.impress=ooo-presentation.desktop;\n")
    fileassociations.write("application/vnd.sun.xml.impress.template=ooo-presentation.desktop;\n")
    fileassociations.write("application/vnd.sun.xml.math=ooo-formula.desktop;\n")
    fileassociations.write("application/vnd.sun.xml.writer=ooo-textdoc.desktop;\n")
    fileassociations.write("application/vnd.sun.xml.writer.global=ooo-textdoc.desktop;\n")
    fileassociations.write("application/vnd.sun.xml.writer.template=ooo-textdoc.desktop;\n")
    fileassociations.write("application/vnd.wordperfect=ooo-textdoc.desktop;\n")
    fileassociations.write("application/wordperfect=ooo-textdoc.desktop;\n")
    fileassociations.write("application/x-123=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/x-7z-compressed=xarchiver.desktop;\n")
    fileassociations.write("application/x-arj=xarchiver.desktop;\n")
    fileassociations.write("application/x-bzip=xarchiver.desktop;\n")
    fileassociations.write("application/x-bzip-compressed-tar=xarchiver.desktop;\n")
    fileassociations.write("application/x-bzip2=xarchiver.desktop;\n")
    fileassociations.write("application/x-bzip2-compressed-tar=xarchiver.desktop;\n")
    fileassociations.write("application/x-compressed-tar=xarchiver.desktop;\n")
    fileassociations.write("application/x-dbase=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/x-dbf=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/x-desktop=panel-desktop-handler.desktop;\n")
    fileassociations.write("application/x-dos_ms_excel=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/x-excel=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/x-extension-m4a=parole.desktop;\n")
    fileassociations.write("application/x-extension-mp4=parole.desktop;\n")
    fileassociations.write("application/x-extension-txt=ooo-textdoc.desktop;\n")
    fileassociations.write("application/x-flac=parole.desktop;\n")
    fileassociations.write("application/x-flash-video=parole.desktop;\n")
    fileassociations.write("application/x-glade=glade-3.desktop;\n")
    fileassociations.write("application/x-gzip=xarchiver.desktop;\n")
    fileassociations.write("application/x-java-jnlp-file=javaws.desktop;\n")
    fileassociations.write("application/x-matroska=parole.desktop;\n")
    fileassociations.write("application/x-ms-excel=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/x-msexcel=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/x-netshow-channel=parole.desktop;\n")
    fileassociations.write("application/x-ogg=parole.desktop;\n")
    fileassociations.write("application/x-quattropro=ooo-spreadsheet.desktop;\n")
    fileassociations.write("application/x-quicktime-media-link=parole.desktop;\n")
    fileassociations.write("application/x-quicktimeplayer=parole.desktop;\n")
    fileassociations.write("application/x-rar=xarchiver.desktop;\n")
    fileassociations.write("application/x-rar-compressed=xarchiver.desktop;\n")
    fileassociations.write("application/x-shorten=parole.desktop;\n")
    fileassociations.write("application/x-smil=parole.desktop;\n")
    fileassociations.write("application/x-t602=ooo-textdoc.desktop;\n")
    fileassociations.write("application/x-tar=xarchiver.desktop;\n")
    fileassociations.write("application/x-zip=xarchiver.desktop;\n")
    fileassociations.write("application/x-zip-compressed=xarchiver.desktop;\n")
    fileassociations.write("application/xhtml_xml=chromium-browser.desktop;\n")
    fileassociations.write("application/zip=xarchiver.desktop;\n")
    fileassociations.write("audio/3gpp=parole.desktop;\n")
    fileassociations.write("audio/AMR=parole.desktop;\n")
    fileassociations.write("audio/AMR-WB=parole.desktop;\n")
    fileassociations.write("audio/ac3=parole.desktop;\n")
    fileassociations.write("audio/basic=parole.desktop;\n")
    fileassociations.write("audio/midi=parole.desktop;\n")
    fileassociations.write("audio/mp4=parole.desktop;\n")
    fileassociations.write("audio/mpeg=parole.desktop;\n")
    fileassociations.write("audio/ogg=parole.desktop;\n")
    fileassociations.write("audio/vnd.rn-realaudio=parole.desktop;\n")
    fileassociations.write("audio/x-ape=parole.desktop;\n")
    fileassociations.write("audio/x-flac=parole.desktop;\n")
    fileassociations.write("audio/x-it=parole.desktop;\n")
    fileassociations.write("audio/x-m4a=parole.desktop;\n")
    fileassociations.write("audio/x-matroska=parole.desktop;\n")
    fileassociations.write("audio/x-mod=parole.desktop;\n")
    fileassociations.write("audio/x-mp3=parole.desktop;\n")
    fileassociations.write("audio/x-mpeg=parole.desktop;\n")
    fileassociations.write("audio/x-musepack=parole.desktop;\n")
    fileassociations.write("audio/x-pn-aiff=parole.desktop;\n")
    fileassociations.write("audio/x-pn-au=parole.desktop;\n")
    fileassociations.write("audio/x-pn-realaudio=parole.desktop;\n")
    fileassociations.write("audio/x-pn-realaudio-plugin=parole.desktop;\n")
    fileassociations.write("audio/x-pn-wav=parole.desktop;\n")
    fileassociations.write("audio/x-pn-windows-acm=parole.desktop;\n")
    fileassociations.write("audio/x-real-audio=parole.desktop;\n")
    fileassociations.write("audio/x-realaudio=parole.desktop;\n")
    fileassociations.write("audio/x-sbc=parole.desktop;\n")
    fileassociations.write("audio/x-speex=parole.desktop;\n")
    fileassociations.write("audio/x-tta=parole.desktop;\n")
    fileassociations.write("audio/x-vorbis=parole.desktop;\n")
    fileassociations.write("audio/x-vorbis+ogg=parole.desktop;\n")
    fileassociations.write("audio/x-wav=parole.desktop;\n")
    fileassociations.write("audio/x-wavpack=parole.desktop;\n")
    fileassociations.write("audio/x-xm=parole.desktop;\n")
    fileassociations.write("image/bmp=ristretto.desktop;\n")
    fileassociations.write("image/gif=ristretto.desktop;\n")
    fileassociations.write("image/jpeg=ristretto.desktop;\n")
    fileassociations.write("image/png=ristretto.desktop;\n")
    fileassociations.write("image/svg+xml=ristretto.desktop;\n")
    fileassociations.write("image/tiff=ristretto.desktop;\n")
    fileassociations.write("image/vnd.rn-realpix=parole.desktop;\n")
    fileassociations.write("image/x-pict=parole.desktop;\n")
    fileassociations.write("image/x-pixmap=ristretto.desktop;\n")
    fileassociations.write("image/x-xpixmap=ristretto.desktop;\n")
    fileassociations.write("inode/directory=Thunar-folder-handler.desktop;\n")
    fileassociations.write("misc/ultravox=parole.desktop;\n")
    fileassociations.write("multipart/x-zip=xarchiver.desktop;\n")
    fileassociations.write("text/comma-separated-values=ooo-spreadsheet.desktop;\n")
    fileassociations.write("text/csv=ooo-spreadsheet.desktop;\n")
    fileassociations.write("text/google-video-pointer=parole.desktop;\n")
    fileassociations.write("text/html=chromium-browser.desktop;\n")
    fileassociations.write("text/mathml=ooo-formula.desktop;\n")
    fileassociations.write("text/rtf=ooo-textdoc.desktop;\n")
    fileassociations.write("text/spreadsheet=ooo-spreadsheet.desktop;\n")
    fileassociations.write("text/tab-separated-values=ooo-spreadsheet.desktop;\n")
    fileassociations.write("text/x-comma-separated-values=ooo-spreadsheet.desktop;\n")
    fileassociations.write("text/x-csv=ooo-spreadsheet.desktop;\n")
    fileassociations.write("text/x-google-video-pointer=parole.desktop;\n")
    fileassociations.write("text/xml=chromium-browser.desktop;\n")
    fileassociations.write("video/3gpp=parole.desktop;\n")
    fileassociations.write("video/dv=parole.desktop;\n")
    fileassociations.write("video/fli=parole.desktop;\n")
    fileassociations.write("video/flv=parole.desktop;\n")
    fileassociations.write("video/mp4=parole.desktop;\n")
    fileassociations.write("video/mp4v-es=parole.desktop;\n")
    fileassociations.write("video/mpeg=parole.desktop;\n")
    fileassociations.write("video/msvideo=parole.desktop;\n")
    fileassociations.write("video/ogg=parole.desktop;\n")
    fileassociations.write("video/quicktime=parole.desktop;\n")
    fileassociations.write("video/vivo=parole.desktop;\n")
    fileassociations.write("video/vnd.divx=parole.desktop;\n")
    fileassociations.write("video/vnd.rn-realvideo=parole.desktop;\n")
    fileassociations.write("video/vnd.vivo=parole.desktop;\n")
    fileassociations.write("video/x-anim=parole.desktop;\n")
    fileassociations.write("video/x-avi=parole.desktop;\n")
    fileassociations.write("video/x-flc=parole.desktop;\n")
    fileassociations.write("video/x-fli=parole.desktop;\n")
    fileassociations.write("video/x-flic=parole.desktop;\n")
    fileassociations.write("video/x-flv=parole.desktop;\n")
    fileassociations.write("video/x-m4v=parole.desktop;\n")
    fileassociations.write("video/x-matroska=parole.desktop;\n")
    fileassociations.write("video/x-mpeg=parole.desktop;\n")
    fileassociations.write("video/x-ms-asf=parole.desktop;\n")
    fileassociations.write("video/x-ms-wm=parole.desktop;\n")
    fileassociations.write("video/x-ms-wmv=parole.desktop;\n")
    fileassociations.write("video/x-msvideo=parole.desktop;\n")
    fileassociations.write("video/x-nsv=parole.desktop;\n")
    fileassociations.write("video/x-ogm+ogg=parole.desktop;\n")
    fileassociations.write("video/x-theora+ogg=parole.desktop;\n")
    fileassociations.write("x-content/video-dvd=parole.desktop;\n")
    fileassociations.write("x-content/video-svcd=parole.desktop;\n")
    fileassociations.write("x-content/video-vcd=parole.desktop;\n")


    fileassociations.close()

