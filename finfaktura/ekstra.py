#!/usr/bin/python -d
# -*- coding:utf8 -*-
###########################################################################
#    Copyright (C) 2005-2008- Håvard Gulldahl
#    <havard@lurtgjort.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################

PRODUKSJONSVERSJON=False

from qt import *
from cStringIO import StringIO

class QBuffer(QIODevice):

    def __init__(self):
        QIODevice.__init__(self)
        self.open( IO_ReadOnly)

    def open(self, mode):
        self.__io = StringIO()
        return True

    def close(self):
        self.__io.close()

    def flush(self):
        self.__io.flush()

    def readAll(self):
        return self.__io.read()

    def getch(self):
        return self.__io.read(1)

    def readBlock(self, size):
        result = self.__io.read(size)
        if result:
            return (result,)

        return None

    def writeBlock(self, data, length=None):
        if type(data) == QByteArray:
            data = data.data()

        self.__io.write(data)

        return len(data)

    def getData(self):
        return self.__io.getvalue()

class QFloatSpinBox(QSpinBox):
            #QString mapValueToText( int value )
            #{
                #if ( value == -1 ) // special case
                    #return QString( "Auto" );
                #return QString( "%1.%2" ) // 0.0 to 10.0
                    #.arg( value / 10 ).arg( value % 10 );
            #}

            #int mapTextToValue( bool *ok )
            #{
                #if ( text() == "Auto" ) // special case
                    #return -1;
                #return (int) ( 10 * text().toFloat() ); // 0 to 100
    def mapValueToText(verdi): # oversetter fra intern verdi til teksten som vises
        return QString("%i.%i" % (verdi / 10, verdi % 10))
    
    def mapTextToValue(boool):
        return int(10 * float(self.text()))

# Logoer inlines slik at vi slipper å laste dem fra fil
# Begge er i PNG-format

forfaltLogo_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x10\x00\x00\x00\x10" \
    "\x08\x06\x00\x00\x00\x1f\xf3\xff\x61\x00\x00\x02" \
    "\x74\x49\x44\x41\x54\x38\x8d\x95\x93\x4b\x48\x54" \
    "\x71\x14\xc6\x7f\xff\x7b\xef\x5c\xe7\x8e\x4e\x3a" \
    "\x73\x67\x54\x46\x74\xcc\x4a\x7c\x94\x61\x68\x60" \
    "\x0f\x53\x29\xf0\x41\x68\x91\x4a\x2d\x22\x11\x85" \
    "\x30\x5d\x14\x2d\xda\xd8\xa6\x82\x36\x41\x8b\x68" \
    "\xd5\xb6\xbd\x56\x3b\x25\x08\x02\x85\xa2\x85\x96" \
    "\x96\xa6\x96\x66\x2a\xa3\xe9\xcc\x38\x0f\x75\xe6" \
    "\xdf\x4a\xf0\x11\x92\x67\x75\x38\xe7\xfb\x7d\x8b" \
    "\xc3\xf9\x44\x57\x57\x17\x3b\x4b\x02\x69\x56\x6c" \
    "\xb5\x19\x64\xbe\xf9\xc5\xcc\x42\x84\x55\xb1\x4b" \
    "\xb5\x47\x59\x15\x78\x50\x4c\xc7\xc8\x0d\xa6\xee" \
    "\x16\x72\x5b\x13\x68\xfb\xe1\x29\x77\x53\xf8\xf9" \
    "\xa6\x3a\x12\x79\xed\x90\x1f\xdb\xd5\xf1\x12\x27" \
    "\x27\xff\x1b\x76\xe8\x58\x9e\x9f\xe1\x69\xb0\xb7" \
    "\x4a\xca\x68\xaf\x0c\xf4\x56\xc9\x27\x65\xbc\x48" \
    "\x54\xb1\xff\x4b\xaf\xee\x1c\x5c\x3f\x48\x65\x7b" \
    "\x83\x79\x3f\x76\xae\x33\xf1\xeb\xef\x4c\x8c\x74" \
    "\x17\x39\xab\x83\xde\x89\xf1\xf0\xf0\x88\x9f\xd1" \
    "\x3d\x0d\x32\x0c\x92\xef\x9d\xe6\x71\x5e\x4b\xe3" \
    "\x89\xe1\x40\x29\x83\x03\x63\xc4\x74\x17\xf9\x05" \
    "\x71\xc3\xf6\x7d\xc8\x7c\xfb\x83\xbe\x50\x8c\xe0" \
    "\x56\x46\xd9\x6c\x0c\x15\x3a\xf3\xb8\x7c\xfc\x82" \
    "\xf7\xbc\x51\x74\x11\x4d\x13\xc4\x62\x1b\x68\x9a" \
    "\x82\xad\xb8\x8e\xb2\x9a\xcc\xb3\x4d\xd9\x34\x2a" \
    "\x5b\x98\x6d\x06\x25\x0e\xbc\xb5\xa5\x6a\x87\xb3" \
    "\xa6\xda\xc0\x6a\x62\x9a\x1b\x48\x19\xc5\x34\xd7" \
    "\x11\x46\x0a\xee\xea\x8a\x84\xe6\x53\x4a\x5b\xfe" \
    "\x01\xf2\x77\x19\x18\x0a\x4a\x53\x2e\xad\x59\x75" \
    "\x39\xc5\x96\xcc\x22\x60\x01\xa7\x33\x48\x42\x42" \
    "\x08\xb7\x3b\x00\xcc\xa2\x65\x1d\xe6\x58\x7d\x46" \
    "\xc1\xb5\x5c\x5a\x75\x05\xeb\xb6\x1b\x54\xa5\x51" \
    "\xd2\x71\xc9\xf2\xc8\x73\xb5\x22\x45\xd8\x5c\xc0" \
    "\x0a\x9a\x16\x20\x29\x69\x15\x8f\x27\x8c\xc5\xe2" \
    "\x03\x25\x80\x9e\x1a\x15\x8e\xb9\x19\xef\xa7\x2f" \
    "\xf2\xc3\x74\x98\x49\x00\x35\xcb\x86\xed\x61\x39" \
    "\xdd\x45\xed\x9e\x0a\xfd\x50\x0e\x10\x00\x96\x98" \
    "\x99\x99\x67\x70\x70\x0e\xbb\xdd\x87\x69\x2e\x02" \
    "\x0b\x08\x23\x8a\x3d\xd9\x6f\xd7\x47\xc3\xc6\xbb" \
    "\x9f\xf4\x47\xe2\x44\xd4\xb6\x23\x5c\xa9\x6f\x56" \
    "\xef\x38\x6b\x53\x0d\xa1\xad\x01\x8b\x80\x8f\x9e" \
    "\x9e\x59\xba\xbb\xa7\x71\x38\x16\x29\x2b\x5b\x02" \
    "\x7c\xc0\x1f\x34\xd7\x1a\xae\x60\xc4\x3b\x35\xcc" \
    "\xd8\xf0\x32\x43\xea\xb3\x7a\x5e\x66\xb5\xe8\x5e" \
    "\x8b\x0b\x90\x7e\x90\xcb\xc0\x32\xf6\x44\x3f\x6e" \
    "\x57\x88\xca\x8a\x55\xd2\xd3\xfd\x20\x57\x40\x06" \
    "\x10\x5a\x14\xc3\x1d\xd3\xf5\x11\x5c\x7d\x63\xf4" \
    "\x6b\xd1\x08\xda\xec\xab\xd8\xb2\xd0\x83\x02\x04" \
    "\x02\x01\x48\x34\x21\x69\xb0\x4a\xe2\x03\x71\x26" \
    "\xdf\x4b\x40\x82\x8c\x03\x71\xd8\x90\x62\x7d\x0d" \
    "\x1d\x41\x8a\x38\x7a\x80\x3c\x4f\x02\xd9\x71\x89" \
    "\x85\xad\x91\x93\x3b\x7f\x6e\xdb\x4a\x4e\x84\x98" \
    "\x9f\x0c\xf1\x4d\xdc\xea\xec\xda\xd4\xee\x2b\xb1" \
    "\x42\x80\x02\xf2\x2f\x88\xc9\xd2\x31\x87\xf1\x2f" \
    "\x13\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60" \
    "\x82"
slettetLogo_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x10\x00\x00\x00\x10" \
    "\x08\x06\x00\x00\x00\x1f\xf3\xff\x61\x00\x00\x02" \
    "\xf7\x49\x44\x41\x54\x38\x8d\x5d\x93\xcd\x6b\x54" \
    "\x67\x14\xc6\x7f\xe7\xcd\x9d\x9b\xf9\x40\x74\xd2" \
    "\xb1\xde\x44\x9b\xc9\x60\x4d\xc7\x60\x4a\x47\xc7" \
    "\x86\x5a\xc9\x84\x82\xd6\xc9\x1f\xd0\x9d\xba\x52" \
    "\x8c\x04\x09\x14\x71\x61\x56\x2e\xc4\x9d\x03\x09" \
    "\xd8\x65\x37\xba\x8b\x9b\x4a\x5c\x04\x24\x83\x64" \
    "\xd1\xa4\x03\x42\x2e\x64\x86\xf9\x30\x96\x01\xe3" \
    "\x30\xb6\x31\x24\x33\x73\x93\x9b\xfb\x76\x71\x53" \
    "\x0a\x7d\xe0\xc7\xd9\x1d\x9e\xf3\x70\x1e\x99\x9b" \
    "\x9b\x63\x71\x71\x11\x11\x41\x80\xcf\xa0\xfb\x1b" \
    "\xad\xbf\x1a\xd6\xfa\x5b\x4f\xeb\x01\x0f\xf0\x44" \
    "\xd6\x6d\x91\xe5\x55\x91\xd2\xdf\xe0\x68\x40\x6b" \
    "\xcd\xd8\xd8\x18\x46\x3e\x9f\x67\x66\x66\x06\x80" \
    "\x0c\x24\x6f\xc1\x64\x34\x1c\x1e\xdf\x3f\x79\xd2" \
    "\x0a\x1c\x3b\xd6\xad\x45\x68\x7f\xfc\xe8\x44\x2a" \
    "\x95\x8d\xcf\xb7\xb6\xe6\xe7\x61\x76\x19\x8a\x00" \
    "\x22\x82\xc1\x81\x7e\x80\xef\xef\x1b\x46\x6e\xe8" \
    "\xc2\x85\x73\xd1\x6b\xd7\xc4\x3c\x7b\x16\x09\x87" \
    "\x01\xd0\x8e\x13\x1a\x58\x5b\x4b\x0c\x3e\x7d\x7a" \
    "\x3b\xba\xb0\x30\x92\xeb\x74\xa6\x7e\x87\x25\x00" \
    "\x43\x80\x51\x48\xde\x57\x2a\x97\x1a\x1f\x4f\x1f" \
    "\xbe\x79\x13\xd5\xd7\x07\xad\x16\xec\xec\x00\x20" \
    "\x40\x70\x70\x90\x81\x3b\x77\x24\x18\x8b\xa5\xf7" \
    "\x9e\x3d\xcb\xed\x3a\xce\x55\x81\xa2\x3a\x0a\xe6" \
    "\x04\x4c\x0e\x25\x93\xe9\xc3\x57\xae\xa0\xe2\x71" \
    "\x88\xc7\xfd\x05\xd5\xaa\x4f\xbb\x0d\xf1\x38\x62" \
    "\x59\x58\xa3\xa3\x8c\xa4\xd3\xe9\x9f\x60\xf2\x08" \
    "\x98\xea\x6b\x48\x9e\x10\xc9\x46\x87\x86\x50\xed" \
    "\x36\x1c\x3a\x04\x3d\x3d\x90\x4a\x81\x88\x4f\x2a" \
    "\x05\x3d\x3d\xe8\x50\x08\x5d\x2a\xd1\xab\x14\xfd" \
    "\x90\xfd\x12\x92\xc6\xb0\xd6\xe7\xdd\x48\xc4\x0a" \
    "\x00\xbc\x79\x03\xdb\xdb\x70\xfd\xba\xef\x22\x9b" \
    "\xf5\x03\x8a\xc5\xd8\x5f\x5d\x65\xf7\xee\x5d\xf6" \
    "\x5f\xbf\x86\x4e\x87\x13\x60\x75\xc1\x79\xc3\x13" \
    "\x49\x98\x4a\x85\x55\xbd\x0e\x5d\x5d\x50\xa9\x40" \
    "\xbd\x0e\xd3\xd3\xd0\xdf\x0f\x80\x57\x2e\xe3\x4c" \
    "\x4c\xe0\x2e\x2d\x01\xa0\x80\x30\x84\x3b\x90\x30" \
    "\x3c\xc0\x6b\xb5\xa0\x56\xf3\xed\x7a\x1e\x58\x16" \
    "\x68\xcd\xff\xa5\x0e\xa6\x00\x1a\xf0\x00\xe5\xc1" \
    "\x5b\xc7\x75\x5b\x5e\xb3\x89\x6e\x34\xd0\xa7\x4f" \
    "\xa3\x1f\x3c\x80\x78\x1c\x5d\x2e\xa3\xcb\x65\xd4" \
    "\xa9\x53\x04\x9f\x3c\xc1\xbc\x78\x91\x00\x10\x00" \
    "\xb6\xa1\xe5\xc1\x5b\x65\xc3\xca\x3b\xd8\x70\x01" \
    "\xfa\xfa\xe0\xe1\x43\x38\x73\x06\x6c\x1b\x6e\xdc" \
    "\xf0\xb1\x6d\xd4\xf0\x30\x81\x47\x8f\x30\x8f\x1f" \
    "\xc7\x55\x8a\x1a\x6c\xd4\x60\x45\xd9\x50\xac\xc2" \
    "\xcb\xf7\xa1\x10\x28\x85\xe4\xf3\x48\xa1\x00\xd3" \
    "\xd3\x88\x6d\x23\xb6\xed\xe7\x51\x28\x20\xf9\x3c" \
    "\x28\x45\x25\x14\xa2\x04\x2f\xd7\xa1\x68\xfc\x05" \
    "\xbb\x2f\x60\x36\xea\x38\x23\x21\x48\x1f\x7d\xfe" \
    "\x1c\x79\xf5\x0a\x3e\x7c\x80\xde\x5e\xff\xe8\x6a" \
    "\x15\xee\xdd\x43\x6f\x6e\xf2\x27\xb0\xe0\x38\x7f" \
    "\xfc\x06\xb3\x3f\xc2\xae\xa1\x81\x15\x28\x3e\x76" \
    "\xdd\xa9\xbd\x46\x23\xf7\x9d\x69\x9e\xfb\x22\x18" \
    "\x14\xd3\xb2\x10\x11\xff\x95\xb5\xa6\xd3\x6e\x53" \
    "\xde\xdc\xd4\x0b\x8d\x46\xe1\x57\xd7\x9d\x2a\x42" \
    "\xf1\x32\xfc\xd7\x85\x65\x58\x7a\xec\x38\x57\xeb" \
    "\xb5\xda\x64\xa2\xd9\xcc\x26\x62\x31\x2b\x1c\x89" \
    "\x04\x3d\xe0\xd3\xce\x8e\x53\x6e\x36\x37\x4a\x5b" \
    "\x5b\xf3\x2f\xb4\x9e\x5d\x3b\x28\x13\x80\x91\xc9" \
    "\x64\xd0\x5a\xff\x5b\xe7\x62\x07\x7e\xde\xd3\xfa" \
    "\x17\x57\x64\xe4\x93\x52\x09\x0f\xd8\xf7\xbc\x75" \
    "\xd1\x7a\xb9\x5b\xa4\x74\x19\x9c\x4b\x07\xae\x32" \
    "\x99\x0c\xff\x00\x52\xc5\x38\x72\x53\x7f\x4a\xf3" \
    "\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"

def debug(*s):
    if not PRODUKSJONSVERSJON: print "[faktura]:", s

