from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import receive_data

urlpatterns = [
    path('receive-data/<int:account_id>/', receive_data, name='receive_data'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
