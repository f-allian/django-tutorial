from django.shortcuts import render

from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}

class AuthorisedView(LoginRequiredMixin, TemplateView):

    template_name = 'home/authorised.html'
    login_url = '/admin'

def home(request):
    return render(request, 'home/welcome.html', {'today':datetime.today()}) #need empty brackets as a way of passing info from view to template.

@login_required(login_url='/admin') # this means django redirects the user to the login admin page.
def authorised(request):
    return render(request, 'home/authorised.html', {})