from django.shortcuts import render
from django.core.urlresolvers import reverse
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import redirect
from django.contrib.auth.models import User


# Create your views here.
@csrf_protect
def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
                )
                return HttpResponseRedirect('/accounts/register/success/')
        else:
            form = RegistrationForm()
        variables = RequestContext(request, {'form': form})

        return render_to_response('blog/accounts/register.html', variables)

def register_success(request):
    if request.user.is_authenticated():
        return render_to_response('home.html')
    else:
        return render_to_response('blog/accounts/success.html')

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')

#@login_required
#def home(request):
#    return render_to_response('home.html', {'user': request.user})
