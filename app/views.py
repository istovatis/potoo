import datetime
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .forms import NewPot


from .models import Pot, User
from django.shortcuts import get_object_or_404, render

# Create your views here.

def index(request):
    latest_pots_list = Pot.objects[:5]
    template = loader.get_template('pots/index.html')
    context = {
        'latest_pots_list': latest_pots_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, id):
    try:
        pot = Pot.objects.get(pot_id=id)
    except Pot.DoesNotExist:
        raise Http404("Oops... Not pot")
    return render(request, 'pots/detail.html', {'pot': pot})

def user_detail(request, id):
    try:
        latest_pots_list = Pot.objects.all().filter(creator=id)
        context = {
            'latest_pots_list': latest_pots_list,
        }
    except Pot.DoesNotExist:
        raise Http404("Oops... Not such user")
    return render(request, 'users/index.html', context)




