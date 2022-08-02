#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys
sys.path.append('.')

from utils.filters import sidebar

JINJA_FILTERS = {'sidebar': sidebar}

AUTHOR = 'RE:Connect'
SITENAME = 'RE:Connect'
SITESUBTITLE = ''
# SITEURL = '127.0.0.1'
SITEURL = 'https://bear-rsg.github.io'

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
DIRECT_TEMPLATES = ['index', 'blog', 'projects_gallery']
PAGINATED_DIRECT_TEMPLATES = ['index', 'blog', 'projects_gallery']

ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
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
SOCIAL = (
    ('twitter', 'https://twitter.com/Climate_and_RE'),
          )

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
STATIC_PATHS = ['images', 'css', 'js']

# PLUGINS
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'pelican-page-hierarchy', 'category_order', 'optimize_images', 'gzip_cache',
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
ARCHIVES_URL = 'blog.html'

THEME_TEMPLATES_OVERRIDES = ['modified-templates']

MENUITEMS = (
    ('About', 'about.html'),
    ('Projects Gallery', 'projects_gallery.html'),
    ('Reports', 'reports.html'),
    ('Resources', 'resources.html'),
    ('Blog', 'blog.html'),
)
