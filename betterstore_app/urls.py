from django.urls import path
from .views import create_kye_value, show_value, delete_item


urlpatterns = [
    path('save/<str:KEY>/', create_kye_value),
    path('show/<str:KEY>/', show_value),
    path('del/<str:KEY>/', delete_item),
]