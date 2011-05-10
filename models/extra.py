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

################## FILES TO INCLUDE #####################

if prod==True:
    ##############################
    # Dont touch at this files !
    ##############################
    css_files = [
        URL('static', 'min.css')
        ]
    js_files = [
        URL('static', 'min.js')
        ]
else:
    ########################################################################
    #
    # Here you put your CSS and JS file to include in layouts
    #
    # To include this files you have to add in your layouts :
    #    {{include 'layouts/js_css_include_from_extra.html'}}
    #
    ########################################################################
    js_files = [
        URL('static', 'js/jquery-1.5.2.js'),
        URL('static', 'js/main.js'),
        ]
    css_files = [
        URL('static', 'css/base.css')
        ]



