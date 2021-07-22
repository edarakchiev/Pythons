from django.urls import path

from Pythons.pythons_app.views import index, create, details, edit, delete

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('details/<int:pk>', details, name='details'),
    path('edit/<int:pk>', edit, name='edit'),
    path('delete/<int:pk>', delete, name='delete'),
]
