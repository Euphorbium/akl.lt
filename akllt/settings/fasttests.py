# pylint: disable=wildcard-import,unused-wildcard-import

from akllt.settings.testing import *  # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
