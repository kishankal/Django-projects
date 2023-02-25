from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class SignupForm(UserCreationForm):
    
    password2 = forms.CharField(label='Confirm Password (again)',
    widget=forms.PasswordInput)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(error_messages={'required':'Last name is neccessary'})
    email = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        
        labels = {'email':'Email'}
#EditUserProfileForm     
class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model= User
        fields = ['username','first_name','last_name','email','date_joined','last_login']
        labels = {'email':'Email'}

# EditAdminProfileForm
# we have to show all information of user when 
# admin wants it that's we are using _all_
class EditAdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model= User
        fields = '__all__'
        labels = {'email':'Email'}