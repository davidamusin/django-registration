
import simplejson as json

from django.http import HttpResponse

def json_login_required(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated():
            return view_func(request, *args, **kwargs)
        response_data = json.dumps({ 'not_authenticated': True })
        return HttpResponse(response_data, mimetype='application/json')
    wrap.__doc__ = view_func.__doc__
    wrap.__dict__ = view_func.__dict__
    return wrap

