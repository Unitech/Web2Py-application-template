# -*- coding: utf-8 -*-

import logging, logging.handlers
import os
from gluon.tools import *

###############################################################
#
# Here we check the value of PRODUCTION environment variable
# You can set this variable directly, example:
#  On Ubuntu : export PRODUCTION='True'
#
###############################################################

prod = bool(os.environ.get('PRODUCTION'))

if prod==True:
    # If we are on production environment
    migrate=False
    log_level=logging.ERROR
    fake_migrate=True
    db = DAL('sqlite://storage.sqlite')
else:
    # On development environment
    migrate=True
    log_level=logging.DEBUG
    fake_migrate=False
    db = DAL('sqlite://storage.sqlite')


#
# You can force language with the next line
# T.force('fr-ca')
#

#
# Auth
#
mail = Mail()                                  # mailer
auth = Auth(globals(),db)                      # authentication/authorization
auth.settings.hmac_key = 'sha512:46b39fae-cd78-425d-803e-49c781eaf70e'   # before define_tables()

########
# Custom auth_user table
########
# db.define_table(auth.settings.table_user_name,
#                 Field('username', length=128, default=''),
#                 Field('email', length=128, default='', unique=True),
#                 Field('first_name', readable=False, writable=False),
#                 Field('last_name', readable=False, writable=False),
#                 Field('password', 'password', length=512, readable=False, label='Password'),
#                 Field('registration_key', length=512, writable=False, readable=False, default=''),
#                 Field('reset_password_key', length=512, writable=False, readable=False, default=''),
#                 Field('registration_id', length=512, writable=False, readable=False, default=''))

# custom_auth_table = db[auth.settings.table_user_name] #get the custom_auth_table
# custom_auth_table.password.requires = [CRYPT()]
# custom_auth_table.email.requires = [
#                     IS_EMAIL(error_message=auth.messages.invalid_email),
#                     IS_NOT_IN_DB(db, custom_auth_table.email)]

auth.define_tables(migrate=migrate,fake_migrate=fake_migrate)
auth.settings.mailer = mail                    # for user email verification
auth.settings.registration_requires_verification = True
auth.settings.registration_requires_approval = False

auth.messages.verify_email = 'Click on the link http://'+request.env.http_host+URL('default','user',args=['verify_email'])+'/%(key)s to verify your email'
auth.settings.reset_password_requires_verification = True
auth.messages.reset_password = 'Click on the link http://'+request.env.http_host+URL('default','user',args=['reset_password'])+'/%(key)s to reset your password'

#
# Other 
#
crud = Crud(globals(),db)                      # for CRUD helpers using auth
service = Service(globals())                   # for json, xml, jsonrpc, xmlrpc, amfrpc
plugins = PluginManager()

mail.settings.server = 'logging' or 'smtp.gmail.com:587'  # your SMTP server
mail.settings.sender = 'you@gmail.com'         # your email
mail.settings.login = 'username:password'      # your credentials or None

crud.settings.auth = None                      # =auth to enforce authorization on crud

#
#
# Logger (Example : logger.debug("TEST"))
#
#
def get_configured_logger(name):
    logger = logging.getLogger(name)
    if (len(logger.handlers) == 0):
        # Create RotatingFileHandler
        import os
        formatter="%(asctime)s %(levelname)s %(process)s %(thread)s %(funcName)s():%(lineno)d %(message)s"
        handler = logging.handlers.RotatingFileHandler(os.path.join(request.folder,'private/app.log'),maxBytes=1024,backupCount=2)
        handler.setFormatter(logging.Formatter(formatter))
        # setting level
        handler.setLevel(log_level)
        logger.addHandler(handler)
        logger.setLevel(log_level)
        logger.debug(name + ' logger created')
    return logger

logger = cache.ram('once',lambda:get_configured_logger(request.application),time_expire=99999999)

