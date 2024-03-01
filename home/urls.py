from django.urls import path
from .views import home, contact, order, lang
from django.views.i18n import set_language

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('order/', order, name='order'),

]

