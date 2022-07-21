#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import time

# Base configuration
AUTHOR = 'RE:Connect'
SITENAME = 'RE:Connect'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'

# Custom settings for copyright notice
CURRENT_YEAR = time.strftime("%Y")

# Appearance
THEME = './active-theme/brutalist'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

CUSTOM_CSS = 'css/custom.css'

PLUGINS = ['assets', 'sitemap', 'pelican-page-hierarchy', 'jinja2content']

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
PLUGIN_PATHS = ['./pelican-plugins/']
I18N_TEMPLATES_LANG = 'en'

USE_FOLDER_AS_CATEGORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

NEWEST_FIRST_ARCHIVES = True

DISPLAY_CATEGORIES_ON_MENU = False

PATH_METADATA = 'articles/(?P<path>.*)\..*'

DEFAULT_METADATA = { }

# Don't need the author pages
AUTHOR_SAVE_AS = ''
AUTHOR_URL = ''
# YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
YEAR_ARCHIVE_SAVE_AS = ''

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
SLUGIFY_SOURCE = 'basename'
PAGE_ORDER_BY = 'reversed-date'
# INDEX_SAVE_AS = 'index.html'

ARTICLE_SAVE_AS = '{path}/{slug}.html'
ARTICLE_URL = '{path}/{slug}.html'
ARTICLE_ORDER_BY = 'reversed-date'
ARTICLE_TRANSLATION_ID = None

# The URL to refer to an article draft
DRAFT_URL = '{path}/drafts/{slug}/'
DRAFT_SAVE_AS = '{path}/drafts/{slug}/index.html'

# Build only modified content instead of all content
LOAD_CONTENT_CACHE = False
CACHE_CONTENT = False

# Allow Markdown in the summary and title
FORMATTED_FIELDS = ['summary', 'title']

USE_PAGER = True  # Prev / Next vs Page no block
ARTICLE_EXCLUDES = ['templates']
TEMPLATE_PAGES = {
    'templates/homepage.html': 'index.html',
}
DIRECT_TEMPLATES = ['blog-index']
PAGINATED_DIRECT_TEMPLATES = ['blog-index']
BLOG_INDEX_SAVE_AS = 'blog/index.html'

THEME_TEMPLATES_OVERRIDES = ['content/templates']

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git', '.gitignore']
#
# SITEMAP PLUGIN
#
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = ('%d-%m-%Y')

SITEURL = 'https://bear-rsg.github.io/reconnect'

STATIC_PATHS = [
    'images',
    'assets',
    'files'
]

EXTRA_PATH_METADATA = {
    # 'extra/css/custom.css': {'path': 'custom.css'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    # 'extra/robots.txt': {'path': 'robots.txt'},
}
IGNORE_FILES = ['.#*', 'README.md']

DEFAULT_PAGINATION = 10

# Leave no orphans
DEFAULT_ORPHANS = 0

PAGINATED_TEMPLATES = {'index': 10 }

USE_PAGER = True

# URL settings
SLUGIFY_SOURCE = 'basename'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
# ARTICLE_SAVE_AS = '{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
# ARTICLE_URL = '{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
# Don't need the author pages
# AUTHOR_SAVE_AS = ''
# AUTHOR_URL = ''
# YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False


MENUITEMS = (
    ('Home', '/reconnect/index.html'),
    ('About', '/reconnect/about.html'),
    ('Projects', '/reconnect/projects.html'),
    ('Reports', '/reconnect/reports.html'),
    ('Resources', '/reconnect/resources.html'),
    ('Blog', '/reconnect/blog/index.html'),
)

LOCALE = ('en_GB', 'en')