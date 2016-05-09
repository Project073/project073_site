#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Project073'
SITENAME = u'Project073'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'nl'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

#LINKS = (('Maillist', 'http://lists.project073.nl/cgi-bin/mailman/listinfo/project073_general'),
#         )
#use the 'lists.md'

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#CUSTOM_LICENSE = 'Copyright by Project073'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (
    ('Chat', '/chat.html'),
    ('Discussielijsten', '/lists.html'),
    ('Nieuws', '/category/news.html'),
)

#install via pelican-themes (automated via Ansible)
#THEME="hyde"
#THEME="gum" <-- ok-ish
#THEME="tuxlife_zf"
#THEME="nice-blog" <- is quite nice!

#very nice!

THEME="voidy-bootstrap"
#hide stuff to end-user
SKIP_COLOPHON = True
#csp issues with varnish. do local only for now
#SKIP_DEFAULT_CSS = True
#SKIP_DEFAULT_JS = True

