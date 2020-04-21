#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Momocode oy'
SITENAME = 'Emended'
SITEURL = ''
ABSOLUTE_SITEURL = ''

PLUGIN_PATHS = (
    'pelican-plugins',
)
PLUGINS = [
    'i18n_subsites',
    'sitemap',
]

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

PATH = 'content'
THEME = 'theme'

PAGE_PATHS = ['.']
ARTICLE_PATHS = []
STATIC_PATHS = ['extra', 'images', 'guides']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

DIRECT_TEMPLATES = []

I18N_UNTRANSLATED_PAGES = 'remove'

I18N_SUBSITES = {
    'fi': {
        'MENUITEMS': (
            ('Kirjaudu', 'https://app.emended.com/'),
            ('Rekisteröidy', 'https://app.emended.com/signup'),
        ),
        'SITEMAP': {
            'format': 'xml',
            'output_filename': 'sitemap_fi.xml'
        }
    },
}

SITEMAP = {
    'format': 'xml',
    'output_filename': 'sitemap_en.xml'
}

TIMEZONE = 'Europe/Helsinki'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (
    ('Sign in', 'https://app.emended.com/'),
    ('Sign up', 'https://app.emended.com/signup'),
)

LINKS = (
    ('info@emended.com', 'mailto:info@emended.com'),
)

SOCIAL = (
    ('facebook', 'https://www.facebook.com/emended'),
    ('twitter', 'https://twitter.com/emendedApp'),
)

DEFAULT_PAGINATION = False

RELATIVE_URLS = False

languages_lookup = {
    'en': 'In English',
    'fi': 'Suomeksi',
}

def lookup_lang_name(lang_code):
    return languages_lookup[lang_code]

JINJA_FILTERS = {
    'lang_name': lookup_lang_name,
}
