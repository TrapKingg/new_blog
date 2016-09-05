from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
# Create your views here.

def landing_page(request):
    return render(request, 'landing_page.html')
