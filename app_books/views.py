from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import UserRegistrationForm


class UserRegistrationView(CreateView):
    template_name = "registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('index'))
        return super().dispatch(request, *args, **kwargs)


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    success_message = "Has iniciado sesión correctamente."

    def get_success_url(self):
        return reverse_lazy('index')


class UserLogoutView(LogoutView):

    next_page = reverse_lazy('index')


class HomeView(TemplateView):
    template_name = 'index.html'
