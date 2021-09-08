from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import auth
from django.contrib import messages

from django.views.generic import FormView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LogoutView

from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from baskets.models import Basket


class LoginFormView(FormView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        auth.login(
            self.request, auth.authenticate(
                username=self.request.POST['username'],
                password=self.request.POST['password']
            )
        )
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class RegistrationCreateView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    extra_context = {'title': 'GeekShop - Регистрация'}

    def form_valid(self, form):
        messages.success(self.request, 'Вы успешно зарегистрировались!')
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class LogoutLogoutView(LogoutView):
    next_page = reverse_lazy('index')


class ProfileUpdateView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')
    extra_context = {'title': 'GeekShop - Личный кабинет'}

    def get_context_data(self, *, object_list=None, **kwargs):
        self.basket = Basket.objects.filter(user=self.request.user)
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        context['baskets'] = self.basket
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Вы успешно обновились!')
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('users:profile', kwargs={'pk': self.object.id})
