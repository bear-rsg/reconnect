#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys
sys.path.append('.')

from utils import filters

JINJA_FILTERS = {'sidebar': filters.sidebar}

AUTHOR = 'RE:Connect'
SITENAME = 'RE:Connect'
SITESUBTITLE = ''
SITEURL = '127.0.0.1'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%B %d, %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# PATH_METADATA = 'articles/(?P<path>.*)\..*'
# PAGINATED_DIRECT_TEMPLATES = ['blog']

# ARTICLE_SAVE_AS = '{slug}.html'
# ARTICLE_URL = '{path}/{slug}.html'
# ARTICLE_ORDER_BY = 'reversed-date'

DEFAULT_METADATA = { }

# Don't need the author pages
AUTHOR_SAVE_AS = ''
AUTHOR_URL = ''
# YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
YEAR_ARCHIVE_SAVE_AS = ''

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/Climate_and_RE'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
# Leave no orphans
DEFAULT_ORPHANS = 0

USE_PAGER = True

DELETE_OUTPUT_DIRECTORY = True

# URL settings
SLUGIFY_SOURCE = 'basename'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME_STATIC_DIR = 'theme'

THEME = './active-theme/twenty-pelican-html5up'
STATIC_PATHS = ['images']

# PLUGINS
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'pelican-page-hierarchy', 'category_order', 'w3c_validate', 'optimize_images', 'gzip_cache',
           'pelican_vimeo']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': .99,
        'pages': .75,
        'indexes': .5
    },
    'changefreqs': {
        'articles': 'daily',
        'pages': 'daily',
        'indexes': 'daily'
    },
}

FAVICON = 'favicon.png'
LOGO = 'st_peters.png'

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
SLUGIFY_SOURCE = 'basename'

DISPLAY_PAGES_ON_MENU = False

USE_FOLDER_AS_CATEGORY = True
ARCHIVES_URL = 'blog-index.html'

THEME_TEMPLATES_OVERRIDES = ['templates']

MENUITEMS = (
    ('About', 'about.html'),
    ('Projects Gallery', 'projects.html'),
    ('Reports', 'reports.html'),
    ('Resources for Teachers', 'resources.html'),
)
