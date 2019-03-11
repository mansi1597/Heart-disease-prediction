from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm, UpdateProfileForm
from django.views.generic import DetailView,UpdateView,TemplateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import UserProfileInfo, User
from django.shortcuts import get_object_or_404
# Create your views here.

@login_required
def user_logout(request):
    #del request.session['user_id']
    request.session.flush()
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

class Aboutpageview(TemplateView):
    template_name='accounts/about.html';


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

        if registered:
            return HttpResponseRedirect(reverse('user_login'))

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'accounts/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                request.session['user_id'] = user.profile.pk

                return HttpResponseRedirect(reverse('predict:predict', kwargs={'pk': user.profile.pk}))
            else:
                return HttpResponse("Account not active")
        else:
            print("Tried login and failed")
            print("username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")

    else:
        return render(request, 'accounts/login.html', {})

class ProfileDetailView(LoginRequiredMixin, DetailView):
    login_url = '/'
    redirect_field_name = '/'
    model = UserProfileInfo
    template_name = 'accounts/profileview.html'

    def get_context_data(self, **kwargs):
        if self.request.session.has_key('user_id'):
            u_id = self.request.session['user_id']
            context = super(ProfileDetailView, self).get_context_data(**kwargs)
            context['user_id'] = u_id

        return context
