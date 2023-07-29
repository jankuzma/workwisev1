from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from account.forms import EmployerRegisterForm, JobSeekerRegisterForm


class LoginUserView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        return render(request, 'login.html')


class UserProfileView(View):
    def get(self, request):
        return render(request, 'user_profile.html')


class LogoutUserView(View):

    def get(self, request):
        logout(request)
        return redirect('index')


class RegisterEmployerView(View):
    def get(self, request):
        return render(request, 'register_employer.html')

    def post(self, request):
        form = EmployerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('index')
        return render(request, 'register_employer.html')


class RegisterJobSeekerView(View):
    def get(self, request):
        return render(request, 'register_jobseeker.html')

    def post(self, request):
        form = JobSeekerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('index')
        return render(request, 'register_jobseeker.html')


