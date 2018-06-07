from django.conf import settings
from django.urls import path, include
from jackpot import views
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from . views import jackpotgames, singlebet, payment, guide, vip_jp


app_name = 'jackpot'

urlpatterns = [

    path('single/', views.singlebet, name='singlebet'),
    path('jackpot/', views.jackpotgames, name='jackpotgames'),
    path('index/', views.index, name='index'),
    path('payment/', views.payment, name='payment'),
    path('guide/', views.guide, name='guide'),
    path('vip_jp/', views.vip_jp, name='vip_jp'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('accounts/', include('django.contrib.auth.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
