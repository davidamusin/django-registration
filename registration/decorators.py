
import simplejson as json

from django.contrib.sites.models import Site
from django.http import HttpResponse

class HttpResponseNotAuthorized(HttpResponse):
    status_code = 401

    def __init__(self, request, *args, **kwargs):
        HttpResponse.__init__(self, request, *args, **kwargs)
        self['WWW-Authenticate'] = 'Cookie realm="%s"' % Site.objects.get_current().name

def json_login_required(view_func):
    def wrap(instance, request, *args, **kwargs):
        if request.user.is_authenticated():
            return view_func(instance, request, *args, **kwargs)
        response_data = json.dumps({ 'not_authenticated': True })
        return HttpResponseNotAuthorized(response_data, mimetype='application/json')
    wrap.__doc__ = view_func.__doc__
    wrap.__dict__ = view_func.__dict__
    return wrap

