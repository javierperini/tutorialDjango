#!/home/javier/tutorial/bin/python
# EASY-INSTALL-DEV-SCRIPT: 'Django==1.9.dev20150714131322','django-admin.py'
__requires__ = 'Django==1.9.dev20150714131322'
import sys
from pkg_resources import require
require('Django==1.9.dev20150714131322')
del require
__file__ = '/home/javier/tutorial/django-trunk/django/bin/django-admin.py'
if sys.version_info < (3, 0):
    execfile(__file__)
else:
    exec(compile(open(__file__).read(), __file__, 'exec'))
