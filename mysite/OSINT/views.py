from django.contrib import messages
from django.contrib.auth import (
                                  authenticate,
                                  logout,
                                  login
                              )

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import UsersForm
from .models import Requests, User


# Create your views here.
def login_view(request):
    return render(request, 'OSINT/Registration/login.html', {})


def registration(request):
    return render(request, 'OSINT/Registration/register.html', {})


def obj_requests(request):
    return render(request, 'OSINT/objects/obj_requests.html', {})


def obj_create(request):
    return render(request, 'OSINT/objects/create.html', {})


# def obj_list(request):
#     return render(request, 'OSINT/objects/list.html', {})


from django.views.generic.list import ListView


# импорт модели Artists

class ObjectsView(ListView):
    model = Requests
    template_name = 'OSINT/objects/list.html'
    context_object_name = 'objects'


def get_register(request):
    error = ''
    if request.method == 'POST':
        form = UsersForm(request.POST)
        print(request.POST.get('password'))
        if form.is_valid():
            user = form.save(commit=False)
            # Cleaned(normalized) data
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return render(request, 'OSINT/Registration/login.html', {})
        else:
            error = 'Неверное заполнение.'

    form = UsersForm()
    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'OSINT/Registration/register.html', data)


#added 20.06 by Romarado
from .forms import AuthUserForm
from django.contrib.auth.views import LoginView, LogoutView


def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect("main")


def email_authenticate_view(request):
    """
        Renders Login Form
      """
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("main")
    if request.POST:
        form = AuthUserForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged In")
            return redirect("main")
        else:
            messages.error(request, message="please Correct Below Errors")
    else:
        form = AuthUserForm()
    context['form'] = form
    return render(request, "OSINT/Registration/login.html", context)


