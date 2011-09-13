# vim: ft=python

import os
import sys
import site

wsgidir = os.path.dirname(__file__)
path = lambda *a: os.path.join(wsgidir, *a)
prev_sys_path = list(sys.path)

site.addsitedir(path('..'))
site.addsitedir(path('..', '..'))

# Reorder sys.path so that the new directories are at the front.
#
# The goal of the following reordering is to give the modules in the root 
# directory the highest priority, then virtualenv, then global python packages.  
# Since we're prepending to sys.path, we start with virtualenv, then project's 
# root.

# 1. Add virtualenv to sys.path
# =============================

# the path to the virtual env relative to wsgidir
ENV_PATH = '../env'

# the packages installed in the virtualenv
site.addsitedir(path(ENV_PATH, 'lib', 'python' + sys.version[:3],
                     'site-packages'))

# reorder sys.path so that the new directories are at the front
new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path

# 2. Add project's root to sys.path
# =================================

# manage prepends /apps, /lib, and /vendor to sys.path on its own
import manage


import django.core.handlers.wsgi
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = django.core.handlers.wsgi.WSGIHandler()
