from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm,EditUserProfileForm   
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,SetPasswordForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.

# Signup function
def sign_up(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Successfully!!!')
            fm.save()
            
    else:
        fm = SignupForm()
    return render(request, 'enroll/signup.html',{'form':fm})

# login view function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully !!')
                    return HttpResponseRedirect('/profile/')
                # fm = AuthenticationForm()
        else:
            fm = AuthenticationForm()
        return render(request,'enroll/userlogin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

# Profile Function
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = EditUserProfileForm(request.POST,instance=request.user)
            if fm.is_valid():
                messages.success(request,"Profile Updated!!")
                fm.save()
        else:
            fm = EditUserProfileForm(instance=request.user)
        return render(request,'enroll/profile.html',{'name':request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/')

# logout function
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')  

# change password with old password
def user_change_pass(request):
    if request.user.is_authenticated:

        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect('/profile/')

        fm = PasswordChangeForm(user=request.user)
        return render(request,'enroll/changepass.html',{'form':fm})
    else:
        messages.error(request,'First you have to Login')
        return HttpResponseRedirect('/login/')
    
