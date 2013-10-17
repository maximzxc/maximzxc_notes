from django.forms import Textarea
from django.conf import settings


class BetterTextarea(Textarea):

    class Media:
        js = (settings.STATIC_URL+'js/jquery.js',
              settings.STATIC_URL+'js/counter.js',)

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'rows': 10, 'cols': 30,
                                               'class': 'read_symbols'})
        super(BetterTextarea, self).__init__(*args, **kwargs)
