from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from accounts.forms import ProfileEditForm, CustomUserCreationForm
from accounts.models import Profile


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/profile-details.html'
    context_object_name = 'profile'

    def get_object(self, *args, **kwargs):
        # retrieving profile for current user
        return get_object_or_404(Profile, user=self.request.user)


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit.html'
    success_url = reverse_lazy('profile-details')

    def get_object(self, *args, **kwargs):
        return self.request.user.profile


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('homepage')

    def get_object(self, *args, **kwargs):
        return get_object_or_404(Profile, user=self.request.user)

    def delete(self, request, *args, **kwargs):

        profile = self.get_object()  # getting profile instance
        profile.delete()  # triggers signal to delete associated user

        logout(request)  # logs out the user after deletion

