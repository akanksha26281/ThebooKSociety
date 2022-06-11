from django.shortcuts import render, get_object_or_404
from .forms import UserForm, UserProfileForm

from django.contrib.auth import login, logout, views
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView, View)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import UserAccount

# Create your views here.

################################# SIGN UP VIEW ####################################
class SignUp(CreateView):
    form_class = UserForm
    success_url = reverse_lazy("home")
    template_name = "auth/signup.html"

###################################################################################





########################## Logged In User Profile VIEW #################################
class ProfileDetailView(LoginRequiredMixin, View):
    template_name = 'profile/profile_details.html'

    def get(self, request, *args, **kwargs):
        account = userAccount.objects.get(user=self.request.user)
        URL = account.profile_pic.url
        bio = account.bio
        name = request.user.get_full_name()
        books = book.objects.filter(auther = self.request.user)
        return render(request, self.template_name, {'name': name, 'URL': URL, 'bio': bio, 'books': books})

#########################################################################################





################################### GENERAL USER PROFILE VIEW ##############################
class ProfileView(DetailView):
    template_name = 'profile/view_profile.html'

    def get_object(self):
        username = self.kwargs.get("username")
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)

#############################################################################################





#################################### UPDATE PROFILE VIEW #####################################
class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'profile/profile_details.html'
    form_class = UserProfileForm, UserForm
    model = User, UserAccount

##############################################################################################
