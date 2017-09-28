from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.lista),
    url(r'^personas/', views.lista_personas),
    url(r'^register/', views.register_user, name='register_user'),
]
