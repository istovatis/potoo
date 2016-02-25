from django.http import Http404
from django.views.generic import View

from app.pot_services import PotServices
from .forms import NewPot
from .models import Pot, User
from django.shortcuts import render


class PotsView(View):
    template_name = 'pots/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'latest_pots_list': PotServices.get_pots()})

    def post(self, request, *args, **kwargs):
        form = NewPot(request.POST)
        if form.is_valid():
            #TODO replace with loged in user
            PotServices.save(form.cleaned_data['pot_text'],  'd64400d3-dfa3-4331-a762-efdd547f21bc')
        return render(request, self.template_name, {'latest_pots_list': PotServices.get_pots()})

def pot_detail(request, id):
    try:
        pot = Pot.objects.get(pot_id=id)
        context = {
            'pot': pot,
            'user': User.objects.get(user_id=pot.creator)

        }
    except Pot.DoesNotExist:
        raise Http404("Oops... Not pot")
    return render(request, 'pots/detail.html', context)

def user_detail(request, id):
    try:
        latest_user_pots_list = sorted(Pot.objects.all().filter(creator=id), key=lambda n: n.time_created, reverse=True)
    except Pot.DoesNotExist:
        raise Http404("Oops... Not such user")
    return render(request, 'users/index.html', {'latest_pots_list': latest_user_pots_list})






