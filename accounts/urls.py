from django.urls import path
from accounts import views

urlpatterns = [
    path('accounts/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.ProfileDetailView.as_view(), name='profile-details'),
    path('profile/edit/', views.ProfileEditView.as_view(), name='profile-edit'),
    path('profile/delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
]