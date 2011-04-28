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
# Automatic files minification
#
########################################################################

@cache(request.env.path_info, time_expire=999999, cache_model=cache.ram)
def get_urls():
    logger.info("+----------- URL update")
    #
    # Here we include files that will be included on
    # views/layouts/layout.html
    #
    # By adding them here, each files will be minimized
    # if the server is set on PRODUCTION environment
    #
    js_files = [
        URL('static', 'js/jquery-1.5.2.js'),
        URL('static', 'js/main.js')
        ]
    css_files = [
        URL('static', 'css/base.css'),
        URL('static', 'css/main.css')
        ]
    return js_files, css_files

(js_files, css_files) = get_urls()

@cache(request.env.path_info, time_expire=999999, cache_model=cache.ram)
def minify_prod():
    #
    # This function will be called for minimizing CSS and JS
    # on production environment
    #
    logger.info("+----------- File minification")
    global css_files
    global js_files
    compress = local_import('pack')
    OUTCSS = compress.process_css(css_files, app_name)
    OUTJS = compress.process_js(js_files, app_name)
    return OUTJS, OUTCSS

#
#
#
if prod==True:
    (OUTJS, OUTCSS) = minify_prod()
    css_files = [URL('static', OUTCSS)]
    js_files = [URL('static', OUTJS)]

