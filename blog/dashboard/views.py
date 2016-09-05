from django.shortcuts import render
from django.core.urlresolvers import reverse
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext


# Create your views here.

@login_required
def home(request):
    return render_to_response('dashboard/index.html', {'user': request.user})
@login_required
def buttons(request):
    return render_to_response('dashboard/buttons.html', {'user': request.user})
@login_required
def tables(request):
    return render_to_response('dashboard/tables.html', {'user': request.user})

@login_required
def profile(request):
    return render_to_response('dashboard/Profile.html', {'user': request.user})
