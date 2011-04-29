# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

import logging, logging.handlers
import os

#
# Here we check the value of PRODUCTION environment variable
# On Ubuntu : export PRODUCTION='True'
#

prod = bool(os.environ.get('PRODUCTION')) #cache.ram('prod', lambda : bool(os.environ.get('PRODUCTION')), time_expire=500)

if prod==True:
    migrate=False
    log_level=logging.ERROR
    fake_migrate=True
#    db = DAL('postgres://postgres:123456@localhost:5432/TABLE_NAME', pool_size=20)
    db = DAL('sqlite://storage.sqlite')
else:
    migrate=True
    log_level=logging.DEBUG
    fake_migrate=False
    db = DAL('sqlite://storage.sqlite')

