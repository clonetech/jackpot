from django.conf import settings
from django.urls import path
from jackpot import views
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from . views import freetips, singlebet, results


app_name = 'jackpot'

urlpatterns = [

    path('singlebet/', views.singlebet, name='singlebet'),
    path('freetips/', views.freetips, name='freetips'),
    path('results/', views.results, name='results'),
    path('', TemplateView.as_view(template_name='freetips.html'), name='freetips'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
