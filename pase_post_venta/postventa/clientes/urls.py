from django.urls import path
from .views import PartnersListView

urlpatterns = [
    path('clientes/', PartnersListView.as_view(), name='partners_list')
]
