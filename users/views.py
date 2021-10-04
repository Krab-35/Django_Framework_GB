from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse, reverse_lazy
from django.contrib import auth
from django.contrib import messages

from django.conf import settings
from django.core.mail import send_mail

from django.views.generic import FormView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LogoutView

from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, UserProfileEditForm
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

    def form_valid(self, form):
        messages.success(self.request, 'Вы успешно обновились!')
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('users:profile', kwargs={'pk': self.object.id})


@transaction.atomic
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        profile_form = UserProfileEditForm(data=request.POST, instance=request.user.userprofile)

        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
        profile_form = UserProfileEditForm(instance=request.user.userprofile)

    context = {
        'form': form,
        'profile_form': profile_form,
        'title': 'GeekShop - Личный кабинет',
    }
    return render(request, 'users/profile.html', context)


def send_verify_mail(user):
    verify_link = reverse('users:verify', args=[user.email, user.activation_key])

    title = f'Подтверждение учетной записи {user.username}'

    message = f'Для подтверждения учетной записи {user.username} на портале {settings.DOMAIN_NAME}' \
              f' пройдите по ссылке:\n{settings.DOMAIN_NAME}{verify_link}'

    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request, 'users/verification.html')
        else:
            print(f'error activation user: {user}')
            return render(request, 'users/verification.html')
    except Exception as err:
        print(f'error activation user: {err.args}')
        return HttpResponseRedirect(reverse('index'))


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if send_verify_mail(user):
                messages.success(request, 'Сообщение подтверждения отправлено')
            else:
                messages.success(request, 'ошибка отправки сообщения')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'title': 'GeekShop - Регистрация', 'form': form}
    return render(request, 'users/registration.html', context)
