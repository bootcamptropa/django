import os

from walladog.settings import BASE_DIR

STATIC_ROOT = os.path.join(BASE_DIR,'static/')

ALLOWED_HOST = ['*']
