from django.urls import path
from .views import SignUpView, ProfileDetailView, ProfileDeleteView, ProfileEditView

urlpatterns = [
    path('accounts/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileDetailView.as_view(), name='profile-details'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile-edit'),
    path('profile/delete/', ProfileDeleteView.as_view(), name='profile-delete'),
]