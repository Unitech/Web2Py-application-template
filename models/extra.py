# -*- coding: utf-8 -*-

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = 'Template app'

response.subtitle = T('customize me!')

########################################################################
# Data that will be append to the beginning
# of views/layouts/layout.html
#
# More infos about meta : http://dev.w3.org/html5/markup/meta.name.html
########################################################################

response.meta.author = 'Strzelewicz Alexandre'
response.meta.description = ''
response.meta.keywords = ''
response.meta.generator = ''
response.meta.copyright = 'Copyright 2010-2012'


########################################################################
#
# Here you put your CSS and JS file to include in layouts
#
########################################################################

if prod==True:
    css_files = [URL('static', 'min.css')]
    js_files = [URL('static', 'min.js')]
else:
    js_files = [
        URL('static', 'js/jquery-1.5.2.js'),
        URL('static', 'js/main.js'),
        URL('static', 'js/shit.js')
        ]
    css_files = [
        URL('static', 'css/base.css')
        ]



