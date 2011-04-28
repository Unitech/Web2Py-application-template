#
# Table definition
#

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

import datetime
now=datetime.datetime.now()

db.define_table('articles',
                Field('title', type='string', length=128, requires=IS_NOT_EMPTY()),
                Field('content', type='text', requires=IS_NOT_EMPTY()),
                Field('image_src', type='upload', requires=IS_NOT_EMPTY()),
                Field('tags', type='text'),
                Field('like_nb', type='integer', default=0),
                Field('dislike_nb', type='integer', default=0),
                Field('date_created', type='datetime', default=now),
                Field('approved', type='boolean', default=False),
                Field('categorie', type='string', length=64),
                Field('user_name', type='string', requires=IS_NOT_EMPTY()),
                fake_migrate=fake_migrate)

#db.articles.categorie.requires = IS_NOT_EMPTY()
#db.articles.categorie.requires = IS_IN_SET(categories)

db.define_table('comments',
                Field('title', type='string', length=128),
                Field('content', type='text', requires=IS_NOT_EMPTY()),
                Field('like_nb', type='integer', default=0),
                Field('dislike_nb', type='integer', default=0),
                Field('date_created', type='datetime', default=now),
                Field('article', db.articles, requires=IS_IN_DB(db, db.articles.id)),
                Field('user_name', type='string'),
                fake_migrate=fake_migrate)

#
# Populating (fill table with random data)
#

# from gluon.contrib.populate import populate
# if db(db.articles.id>0).count() < 20:
#     populate(db.articles,70)


