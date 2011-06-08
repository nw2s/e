import os

from django.utils import simplejson



config = simplejson.load(open(os.path.join(os.path.dirname('.') + 'data/config.json')))

