from django.shortcuts import render,redirect
from first_app.forms import RegisterForm,ChangeUserData
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Account created successfully")
                return redirect('user_login')
        else:
            form = RegisterForm()
        return render(request,'register.html',{'form' : form})
    else:
        redirect('profile')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request = request , data = request.POST)
            
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name , password = userpass)
                    
                if user is not None:
                    login(request,user)
                    messages.success(request,'login successfully')
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request,'login.html',{'form': form})
    else:
        return redirect('profile')
@login_required
def profile(request):
    if request.method == 'POST':
        form = ChangeUserData(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile updated successfully')
            return redirect('profile')
        
    else:
        form = ChangeUserData(instance = request.user)
    return render(request,'profile.html',{'form':form})

def user_logout(request):
    logout(request)
    messages.success(request,"logout successfully")
    return redirect('homepage')

def passchange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user , data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,request.user)
            messages.success(request,"password changes successfully")
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'passchange.html',{'form' : form})


def passchange2(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user , data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,request.user)
            messages.success(request,"password changes successfully")
            return redirect('profile')
    else:
        form = SetPasswordForm(request.user)
    return render(request,'passchange.html',{'form' : form})