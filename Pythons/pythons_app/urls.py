from django.urls import path

from Pythons.pythons_app.views import index, create

urlpatterns = (
    path('', index, name='index'),
    path('create/', create, name='create'),
)
