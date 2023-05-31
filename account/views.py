from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View

from account.forms import LoginForm, CreateUserForm


# Create your views here.


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            # user = authenticate(request, username=username, password=password)
            user = form.cleaned_data['user']

            if user is not None:
                login(request, user)
            return redirect('/')

        return render(request, 'account/form.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class CreateUserViews(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request, 'account/form.html', {'form': form})

    def post(self, request):
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('/')
        return render(request, 'account/form.html', {'form': form})