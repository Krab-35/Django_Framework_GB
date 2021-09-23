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
                # print('Сообщение подтверждения отправлено')
                messages.success(request, 'Сообщение подтверждения отправлено')
            else:
                # print('ошибка отправки сообщения')
                messages.success(request, 'ошибка отправки сообщения')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'title': 'GeekShop - Регистрация', 'form': form}
    return render(request, 'users/registration.html', context)
