from django.shortcuts import render

# Create your views here.


# session setup
def setsession(request):
    request.session['name'] = 'Sonam'
    request.session['lname'] = 'Jha'
    return render(request,'student/setsession.html')

def getsession(request):
    name = request.session['name']
    lname = request.session['lname']
    keys = request.session.keys()
    items = request.session.items()
    return render(request,'student/getsession.html',{'name':name,'lname':lname,'keys':keys,'items':items})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'student/delsession.html')

     