from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import SignUpForm
from users.models import MyUser


class RegisterView(CreateView):
    model = MyUser
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('main-view')

    def form_valid(self, form):
        valid = super(RegisterView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid
