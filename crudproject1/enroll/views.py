from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistrations
from .models import user


# this function will Add new item and show all items
def add_show(request):
    
    if request.method == 'POST':
        fm = StudentRegistrations(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = user(name=nm,email=em,password=pw)
            reg.save()
            fm = StudentRegistrations()

    else:
        fm = StudentRegistrations()
    
    stud = user.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})


# This function will delete the item which are present in database
def delete_data(request,id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

# this function will update and edit the data
def update_data(request,id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        fm = StudentRegistrations(request.POST,instance = pi)
        if fm.is_valid():
            fm.save()
        fm = StudentRegistrations()
    else:
        pi = user.objects.get(pk=id)
        fm = StudentRegistrations(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})