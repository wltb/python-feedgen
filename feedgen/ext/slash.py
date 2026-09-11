# -*- coding: utf-8 -*-
#

'''
Extension for FeedGenerator to support slash comment count for RSS feeds.

See:
https://www.rssboard.org/rss-profile#namespace-elements-slash-comments
https://web.resource.org/rss/1.0/modules/slash/
'''

from feedgen.ext.base import BaseExtension
from feedgen.util import xml_elem

SLASH_NS = 'http://purl.org/rss/1.0/modules/slash/'

class SlashExtension(BaseExtension):
    def extend_ns(self):
        return {'slash': SLASH_NS}

class SlashEntryExtension(BaseExtension):
    def __init__(self):
        self._comments = None

    def extend_rss(self, entry):
        if self._comments:
            elem = xml_elem('{%s}' % SLASH_NS + 'comments', entry)
            elem.text = self._comments

        return entry

    def comments(self, value):
        if type(value) is not int or value < 0:
            raise ValueError('Slash Extension: Invalid comment count')
        self._comments = str(value)

        return self._comments
