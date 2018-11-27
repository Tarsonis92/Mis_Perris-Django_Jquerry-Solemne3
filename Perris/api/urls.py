from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.MascotaView.as_view()),
    url(r'^filtro/(?P<filtro>[a-zA-Z]+)$',views.MascotaFiltro.as_view()),
    url(r'^add/$',views.MascotaFiltro.as_view()),
    url(r'^$',views.PersonaView.as_view()),
    url(r'^filtro/(?P<filtro>[a-zA-Z]+)$',views.PersonaFiltro.as_view()),
    url(r'^add/$',views.PersonaFiltro.as_view()),
    url(r'^$',views.MascotaPersonaView.as_view()),
    url(r'^filtro/(?P<filtro>[a-zA-Z]+)$',views.MascotaPersonaFiltro.as_view()),
    url(r'^add/$',views.MascotaPersonaFiltro.as_view()),
]