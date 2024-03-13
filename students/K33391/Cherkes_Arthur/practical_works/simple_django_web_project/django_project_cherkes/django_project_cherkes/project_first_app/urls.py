from django.urls import path
from .views import *


urlpatterns = [
    path('owner/<int:owner_id>/', get_owner_info),
    path('owner/create/', create_owner),
    path('owners/', get_all_owners_info, name="owners"),
    path('car/<int:pk>/', CarView.as_view()),
    path('cars/', CarListView.as_view()),
    path('car/<int:pk>/update/', CarUpdateView.as_view()),
    path('car/create/', CarCreateView.as_view()),
    path('car/<int:pk>/delete/', CarDeleteView.as_view()),
]