from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from resource_host.main_app.models import Host

from .forms import UserForm, AuthenticationForm


def sign_up(request):
    template = 'registration/sign_up.html'
    if request.method == 'POST':
        form = UserForm
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm
    context = {
        'form': form,
    }
    return render(request, template, context)


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/host/')
        else:
            return render(request, 'registration/login.html', {'form': form})


def host_page(request):
    template = 'host/index.html'
    hosts = Host.objects.all()
    context = {
        'hosts': hosts,
    }
    return render(request, template, context)
