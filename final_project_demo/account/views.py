from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View



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
