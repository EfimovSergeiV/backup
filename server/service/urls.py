from django.urls import path
from service.views import list_files, get_file


urlpatterns = [
    path('bkps/', list_files),
    path('bkps/<uuid:uuid>/', get_file)
]
