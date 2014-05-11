# -*- coding: utf-8 -*-

"""
This template tag is used to manage staticfiles.
"""

import os
import base64

from django.template import Library
from django.conf import settings

register = Library()


@register.simple_tag
def versioned_media(filename):
    url = settings.STATIC_URL + filename
    if settings.STATIC_ROOT:
        path = os.path.join(settings.STATIC_ROOT, filename)
        try:
            if os.path.exists:
                last_changed = os.path.getmtime(path)
                time_stamp = base64.b64encode(str(last_changed))
                url += "?ver=%s" % (time_stamp)
        except:
            pass

    return url
