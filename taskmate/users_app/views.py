from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomRegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ('User account created successfully, Login to Get Started'))
            return redirect('login')
    else:
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')
    
