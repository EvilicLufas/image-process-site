from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', FormView.as_view(), name='home'),
    path('url_rec/', ReceivedView.as_view(), name='url_rec'),
    path('howto/', HowToView.as_view(), name='howto')
]
