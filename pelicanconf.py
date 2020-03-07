#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel'
SITENAME = "Daniel Whittenbury"
SITEURL = 'https://dlwhittenbury.github.io'

PATH = 'content'

TIMEZONE = 'Australia/Adelaide'

DEFAULT_LANG = 'en'

TYPOGRIFY = True

THEME = 'voce-modified'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Home', '/index.html'),
         ('About me', '/pages/about-me.html'),
     	 ('Publications', '/pages/publications.html'),
         ('Resume', '/pages/resume.html'))


# Social Accounts
SOCIAL = (('Email', 'mailto:whittenburydaniel@gmail.com'),
          ('GitHub', 'https://github.com/dlwhittenbury'),
          ('GoogleScholar', 'https://scholar.google.com/citations?user=3m-Rd7oAAAAJ&hl=en'),
          ('ResearchGate','https://researchgate.net/profile/Daniel_Whittenbury'),
          ('Twitter', 'https://twitter.com/dlwhittenbury'),
          )

# ('LinkedIn', 'https://linkedin.com/in/daniel-whittenbury-44235a155'),
# ('Inspire','http://inspirehep.net/search?p=exactauthor%3AD.L.Whittenbury.1+'),
# ('ArXiv','https://arxiv.org/search/nucl-th?searchtype=author&query=Whittenbury%2C+D+L'),

PLUGINS = ["assets"]
PLUGIN_PATHS = ["voce-modified/plugins"]

DEFAULT_PAGINATION = 6
SUMMARY_MAX_LENGTH = 30

# Publish
DELETE_OUTPUT_DIRECTORY = False

USER_LOGO_URL =  "images/myAvatar-Circle.png"


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
