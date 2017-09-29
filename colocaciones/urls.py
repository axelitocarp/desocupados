from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.lista),
    url(r'^register/', views.register_user, name='register_user'),
    url(r'^personas/', views.lista_p),
    url(r'^ofertas/', views.lista_o),
    url(r'^empresas/', views.lista_e)


]
