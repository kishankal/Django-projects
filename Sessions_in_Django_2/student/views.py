from django.shortcuts import render

# Create your views here.


# session setup
def setsession(request):
    request.session['name'] = 'ddskk'
    request.session.set_expiry(600)
    return render(request,'student/setsession.html')

#get created session
def getsession(request):
    name = request.session['name']
    return render(request,'student/getsession.html',{'name':name})

# delete created session
def delsession(request):
    if 'name' in request.session:
      request.session.flush()
      request.session.clear_expired() # to clear all expired session from database
    return render(request,'student/delsession.html')

     