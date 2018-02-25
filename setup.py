#!/usr/bin/env python
# -*- coding:utf8 -*-
###########################################################################
#    Copyright (C) 2005-2009 Håvard Gulldahl og Håvard Sjøvoll
#    <havard@lurtgjort.no>, <sjovoll@ntnu.no>
#
#    Lisens: GPL2
#
# $Id$
###########################################################################


from distutils.core import setup
#from setuptools import setup

import sys, os, os.path, glob

try:
  import py2exe
  extra = {'console':['faktura'],
           'options': { 'py2exe' : {
                                     'optimize': 2,
                                     'includes': ['sip', 'socket', 'xml.etree.ElementTree'], # list of modules to include
                                     'excludes':[], #list of module names to exclude
                                     'dll_excludes':[], #list of dlls to exclude
                                     'ignores':[],# list of modules to ignore if they are not found
                                    }
                       }
           }
except ImportError:
  PY2EXE=False
  extra = {}


import finfaktura # for versjonsnummer

setup(name="finfaktura",
      version=finfaktura.__version__,
      description="Fryktelig Fin Faktura - fakturaprogram for norske næringsdrivende",
      author="Johnny A. Solbu",
      author_email="johnny@solbu.net",
      url="https://sourceforge.net/projects/finfaktura/",
      packages=['finfaktura', 'finfaktura.ui'],
      package_data={'': ['ui/fakturanummer.ui']},
      include_package_data=True,
      data_files=[
            ('share/finfaktura/scripts', glob.glob('scripts/*')),
            ('share/finfaktura/translations', glob.glob('translations/*.qm')),
            ('share/applications', ['finfaktura.desktop']),
            ('share/pixmaps', ['finfaktura.png']),
            ('share/icons/hicolor/128x128/apps', ['finfaktura-icon.png']),
           ],
      scripts=["faktura"],
      Vendor="solbu.net",
      license="GPL2",
      long_description=file(os.path.split(os.path.realpath(sys.argv[0]))[0] + "/intro").read(),
      **extra
      #install_requires = ['docutils>=0.3', 'reportlab'],
      #zip_safe=True,
      #include_package_data = True,
          #entry_points = {
        #'console_scripts': [
            #'faktura_cli = faktura:cli_faktura',
        #],
     #}
     )
