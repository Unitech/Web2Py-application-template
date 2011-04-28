# -*- coding: utf-8 -*-

########################################################################
#
# Automatic files minification
#
########################################################################

# Clear cache
# cache.ram.clear()

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
        URL('static', 'css/base.css')
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
    compress = local_import('pack', reload=True)
    compress.process_css(css_files, request.folder, 'min.css')
    compress.process_js(js_files, request.folder, 'min.js')

#
#
#
if prod==True:
    minify_prod()
    css_files = [URL('static', 'min.css')]
    js_files = [URL('static', 'min.js')]

