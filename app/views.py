from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Pot
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
        question = Pot.objects.get(pot_id=id)
    except Pot.DoesNotExist:
        raise Http404("Oops... Not pot")
    return render(request, 'pots/detail.html', {'pot': question})



