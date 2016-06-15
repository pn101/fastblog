from django.views.generic import View
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


class SignupView(View):

    def get(self, request, *args, **kwargs):
        return render(
                request,
                'auth/signup.html',
                {
                    'site_name': 'Signup to FastBlog',
                }
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
        )

        return redirect('auth:login')
