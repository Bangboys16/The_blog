from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm() 
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            email = form.cleaned_data['email']

            messages.success(request, "Account created successfully!")

            
            send_mail(
                "Welcome Aboard",
                "Congrats on joining THE BLOG start creating that blog post and make a huge difference.",
                "edidiongeka54@gmail.com", #Your from email
                [form.cleaned_data['email']], # Recipient email
            )

            return redirect('login')
        