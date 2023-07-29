from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from account.models import JobSeekerUser, EmployerUser


class IndexView(View):

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('user_login')
        return render(request, 'base.html')
