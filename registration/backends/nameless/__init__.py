
from registration.backends.simple import SimpleBackend
from registration.forms import RegistrationFormUsernameEmailMatch


class NamelessBackend(SimpleBackend):

    def get_form_class(self, request):
        return RegistrationFormUsernameEmailMatch

