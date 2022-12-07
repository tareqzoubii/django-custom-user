from django.urls import path
from .views import ClubsListView, ClubsDetailView, ClubsCreateView, ClubsUpdateView, ClubsDeleteView

urlpatterns = [
    path('clubs/', ClubsListView.as_view(), name='clubs-list'),
    path('clubs/<int:pk>/', ClubsDetailView.as_view(), name='clubs-detail'),
    path('clubs/create/', ClubsCreateView.as_view(), name='clubs-create'),
    path('clubs/<int:pk>/update/', ClubsUpdateView.as_view(), name='clubs-update'),
    path('clubs/<int:pk>/delete/', ClubsDeleteView.as_view(), name='clubs-delete'),
]