from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
import json
from library.models import *
from django.views.decorators.csrf import csrf_exempt
from library.models import user,book

# from library.models import *


def home(request):
    c = {}
    c.update(csrf(request))
    # ... view code here
    return render_to_response("home.html", c)
    # return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def euser(request):
    if request.method == 'POST':
        post, data, req_field = request.POST, {}, ['name','gender','uid','uaddr','mobile']
        for i in req_field:
            data[i] = post['all[%s]'%i]
            print data
        dump = 'saved'
      
        user.objects.create(uname = data['name'],
                        gender = data['gender'],
                        uid = data['uid'],
                        uaddr = data['uaddr'],
                        mobile = data['mobile'],
                         )
        
        # print e
        return HttpResponse(content=json.dumps(dump),content_type='Application/json')
    return render(request,'euser.html')


# def family(request):

#       if request.method == 'POST':
#         post, data, req_field  = request.POST, {}, ['rationcard' ,'street', 'city', 'code']
#         for i in req_field:
#             data[i] = post['all[%s]'%i]
#             print data
        
#         dump = 'notcomplete' if '' in data.values() else 'exists' if Family.objects.filter(ration_card=data['rationcard']) else None       
#         if dump:
#             print '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
#             return HttpResponse(content=json.dumps(dump),content_type='Application/json')
      
#         Family.objects.create( ration_card=data['rationcard'], 
#                                street=data['street'],
#                                city=data['city'],
#                                code=data['code'])

#         dump = 'saved'
#         return HttpResponse(content=json.dumps(dump),content_type='Application/json')

    
def ebook(request):
    return render(request,'ebook.html')

def booklend(request):
    return render(request,'booklend.html')

def stock(request):
    return render(request,'stock.html')

def userd(request):
    return render(request,'user.html')

def login(request):
    state = "Please log in below..."
    username = password = ''

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print username,password
        user = authenticate(username=username, password=password)
        print user
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('home.html',{'state':state, 'username': username})

    # Create your views here.
