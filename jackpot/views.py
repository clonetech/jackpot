from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.utils import timezone
from . models import Freetips, Singlebet
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_protect
from django.contrib.sites.shortcuts import get_current_site


def freetips(request):

    model = Freetips

    template_name = 'freetips.html'

    args = {}

    freetips = Freetips.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('-published_date')[:8]


    args ['freetips'] = freetips

    return render(request, 'freetips.html', args)


def results(request):

    template_name = 'results.html'

    args = {}

    results_teams = Freetips.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('-published_date')[8:24]


    args ['results_teams'] = grouped(results_teams, 6)

    return render(request, 'results.html', args)


def singlebet(request):

    template_name = 'singlebet.html'

    args = {}

    singlebet = Singlebet.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('-published_date')[:7]


    args ['singlebet'] = grouped(singlebet, 1)

    return render(request, 'singlebet.html', args)


def grouped(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]
