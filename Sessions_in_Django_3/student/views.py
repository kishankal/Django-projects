from django.shortcuts import render

# Create your views here.


# session setup
def settestcookie(request):
    request.session.set_test_cookie()
    return render(request,'student/setsession.html')

#get created session
def checktestcookie(request):
    name = request.session.test_cookie_worked()#if cookie work=True notworking=False
    return render(request,'student/getsession.html',{'name':name})

# delete created session
def deltestcookie(request):
    request.session.delete_test_cookie()
    return render(request,'student/delsession.html')

     