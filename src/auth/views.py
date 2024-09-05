from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model

User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if all([username, password]):
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            
    context = {}
    return render(request, 'auth/login.html', context)

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password') 
       
    #    username_exists = User.objects.filter(username__iexact=username).exists()
    #    email_exists = User.objects.filter(email__iexact=email).exists()
        try:
            User.objects.create_user(username, email=email, password=password)
        except:
            pass
    return render(request, 'auth/register.html')