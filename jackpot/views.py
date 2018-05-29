from django.shortcuts import render

from django.contrib.auth.tokens import default_token_generator

from django.contrib.auth.forms import AuthenticationForm

from django.views.generic import TemplateView

from . models import JackpotGames, SingleBet

from django.utils import timezone

from . serializers import JackpotGamesSerializer, SingleBetSerializer

from rest_framework import viewsets



class SingleBetViewSet(viewsets.ModelViewSet):

    queryset = SingleBet.objects.all()

    serializer_class = SingleBetSerializer

class JackpotGamesViewSet(viewsets.ModelViewSet):

    queryset = JackpotGames.objects.all()

    serializer_class = JackpotGamesSerializer



def jackpotgames(request):

    model = JackpotGames

    template_name = 'jackpot.html'

    args = {}

    jackpotgames = JackpotGames.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('-published_date')[:17]


    args ['jackpotgames'] = jackpotgames

    return render(request, 'jackpot.html', args)



def singlebet(request):

    model = SingleBet

    template_name = 'single.html'

    args = {}

    singlebet = SingleBet.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('-published_date')[:2]


    args ['singlebet'] = singlebet

    return render(request, 'single.html', args)


def payment(request):

        template_name = 'payment.html'

        return render(request, 'payment.html')


def index(request):

        template_name = 'index.html'

        return render(request, 'index.html')



def guide(request):

        template_name = 'guide.html'

        return render(request, 'guide.html')


def vip_jp(request):

        template_name = 'vip_jp.html'

        return render(request, 'vip_jp.html')
