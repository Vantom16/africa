from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "index.html"

def has_add_permission(self, request):
    """Return True if the user has the permission to add a model."""
    try:
        user_is_authenticated = request.user.is_authenticated()
    except TypeError:
        user_is_authenticated = request.user.is_authenticated

    if not user_is_authenticated:
        return False
