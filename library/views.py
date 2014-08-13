from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
import json
from library.models import *
from django.views.decorators.csrf import csrf_exempt
from library.models import user,book
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User

def logout_view(request):
    logout(request)
    return render(request,'login.html')
    


# from library.models import *
def loginpage(request):
  return render(request,'login.html')
# def mlogin(request):
#   if request.method == 'POST':
#     post = request.POST
#     uname = post['uname'] 
#     mobile = post['mobile']
#     print uname,mobile
#     curr_user = User.objects.get(username=uname)
#     if curr_user.is_superuser:
#       user = authenticate(username=uname, password=mobile)
#       print user
#     # user1 = user.objects.get(uname =uname, mobile=mobile)
#     # if 
#     if user:

#       login(request, user)
#       print "login success"          
#       dump = "login success"
#       return HttpResponse(content=json.dumps(dump),content_type='Application/json')



#   return render(request,'mlogin.html')
@login_required
def mhome(request):
  return render(request,'mhome.html',{'uname':str(request.user.user.uname)})
@login_required
def meissue(request):
  print request.user.user

  return render(request,'meissue.html',{'uid':request.user.user.uid,'uname':request.user.user.uname,'mobile':request.user.user.mobile,'uaddr':request.user.user.uaddr})
@login_required
def muser(request):
  return render(request,'muser.html',{'uid':request.user.user.uid,'uname':request.user.user.uname})
@login_required
def mstock(request):
  return render(request,'mstock.html',{'uname':str(request.user.user.uname)})


def login_check(request):
  username = request.POST['username']
  password = request.POST['password']
  curr_user = User.objects.get(username=username)
  user = authenticate(username=username, password=password)
  if user is not None:
    if user.is_active:
        login(request, user)
        print "login success"
        if curr_user.is_superuser:
          dump = "superadmin"
          return HttpResponse(content=json.dumps(dump),content_type='Application/json')
        # returnsn HttpResponse(content=json.dumps(dump),content_type='Application/json')
        # return HttpResponseRedirect("/home/")
        # return render(request,'home.html')
        dump = "login success"
        return HttpResponse(content=json.dumps(dump),content_type='Application/json')

    else:
      return render(request,'login.html')
      # Return a 'disabled account' error message
  else:
      # Return an 'invalid login' error message.
    return render(request,'login.html')

@login_required
def home(request):
    c = {}
    c.update(csrf(request))
    # ... view code here
    return render_to_response('home.html', c)
    # return render(request,'home.html')
@login_required
def euser(request):
    if request.method == 'POST':
        post, data, req_field = request.POST, {}, ['uname','gender','uid','mobile','uaddr']
        for i in req_field:
            data[i] = post['all[%s]'%i]
        dump = "Registration Successfull !!!"

        if user.objects.filter(uid = data['uid']):
          dump = "Member ID Already Exist!"

        else:
          # .create_user('john', 'lennon@thebeatles.com', 'johnpassword')
          duser = User.objects.create_user(data['uname'],'',data['mobile'])
          user.objects.create(uname = data['uname'],
                            gender = data['gender'],
                            uid = data['uid'],
                            mobile = data['mobile'],
                            uaddr = data['uaddr'],
                            user =duser,  
                                            
                     )
          
        return HttpResponse(content=json.dumps(dump),content_type='Application/json')
    return render(request,'euser.html')


@login_required    
def ebook(request):
    if request.method == 'POST':
        post, data, req_field = request.POST, {}, ['btitle','category','publisher','author','bid']
        print data,'book'
        for i in req_field:
            data[i] = post['all[%s]'%i]
            # print '?????' 
        quantity = 1
        Book = book.objects.filter(btitle = data['btitle'],
                                   category = data['category'],
                                   publisher = data['publisher'],
                                   author = data['author'],
                                   )
        # if Book:
        #   # bookdetail = book.objects.get(bid = bid)
        #   # bookdetail.quantity = bookdetail.quantity +1
        #   # bookdetail.save()
        #   print '?????'
        #   # quantity = max([i.quantity for i in Book]) + 1
        #   # Book[0].quantity + 1
        
       
        if book.objects.filter(bid = data['bid']):
          dump = "Book ID Already Exist!"
        else:
          book.objects.create(btitle = data['btitle'],
                            category = data['category'],
                            publisher = data['publisher'],
                            author = data['author'],
                            bid = data['bid'], 
                            quantity = quantity                        
                            )
          dump = "New Book Recorded !!!"
       
        
        return HttpResponse(content=json.dumps(dump),content_type='Application/json')
    return render(request,'ebook.html')
@login_required
def issue(request):
  if request.method == 'POST':
      post = request.POST
      uid = post['uid']
      print '????'
     
      if post.has_key('post'):
          print 'check'
          try:
            obj = user.objects.get(uid=uid)
          except Exception as e:
            print e
         
          obj.uname = post['uname']
          obj.mobile = post['mobile']
          obj.uaddr = post['uaddr']
          obj.save()
          data = 'saved'
                
        
      
      else:
          if not user.objects.filter(uid=uid):
              data = 'none'
          else:
              user1 = user.objects.get(uid=uid)
              data = {'uid': user1.uid, 'uname': user1.uname, 'mobile':user1.mobile,'uaddr': user1.uaddr}
              print data   
 
      return HttpResponse(content=json.dumps(data),content_type='Application/json')

  
  return render(request,'issue.html')
@login_required
def bookdetails(request):
    if request.method == 'POST':
      post1 = request.POST
      bid = post1['bid']
      print '????'
     
      if post1.has_key('post'):
          print 'check'
          try:
            obj1 = book.objects.get(bid=bid)
          except Exception as e:
            print e
         
          obj1.btitle = post1['btitle']
          obj1.author = post1['author']
          
          obj1.save()
          data = 'saved'
     
 
      else:
        if not book.objects.filter(bid=bid):
            data = 'none'
        else:
            book1 = book.objects.get(bid=bid)
            data = {'bid': book1.bid, 'btitle': book1.btitle, 'author':book1.author}
            print data                
      return HttpResponse(content=json.dumps(data),content_type='Application/json')
    
    return render(request,'issue.html')    
@login_required
def stockdetails(request):
    if request.method == 'POST':
      post1 = request.POST
      bid = post1['bid']
      
      # if post1.has_key('post'):
      #     print 'check'
      #     try:
      #       obj1 = book.objects.get(bid=bid)
      #     except Exception as e:
      #       print e
         
      #     obj1.btitle = post1['btitle']
                    
      #     obj1.save()
      #     data = 'saved' 
      # else:   
      if not book.objects.filter(bid=bid):
            data = 'none'
      else:
            book1 = book.objects.get(bid=bid)
            data = {'bid': book1.bid, 'btitle': book1.btitle}
            print data                      
      return HttpResponse(content=json.dumps(data),content_type='Application/json')
    
    return render(request,'stock.html')    
@login_required
def stockdetails(request):
    if request.method == 'POST':
      post1 = request.POST
      bid = post1['bid']
           
      if post1.has_key('post'):
          print 'check'
          # try:
          #   obj1 = book.objects.get(bid=bid)
          # except Exception as e:
          #   print e
         
          # obj1.btitle = post1['btitle']
          # obj1.author = post['author']          
          # obj1.category = post['category']
          # obj1.publisher = post['publisher']
          # obj1.quantity = post['quantity']
          # obj1.save()
          # data = 'saved'
     
 
      else:
        if not book.objects.filter(bid=bid):
            data = 'none'
        else:
            book1 = book.objects.get(bid=bid)
            data = {'bid': book1.bid, 'btitle': book1.btitle,'author':book1.author,'category':book1.category,'publisher':book1.publisher,'quantity': book1.quantity}
            print data                
      return HttpResponse(content=json.dumps(data),content_type='Application/json')
    
    return render(request,'stock.html')    


@login_required
def bookreturn(request):
  data = []
  temp = {}
  if request.method == 'POST':
     post = request.POST
     bid = post['bid']

     book_d = book.objects.get(bid = bid)
     datadump = booklend.objects.filter(book = book_d)
     for i in datadump:
        print '?????'
        data.append({'bid':i.book.bid,'btitle':i.book.btitle,'uid':i.user.uid,'uname':i.user.uname,'doi':str(i.doi),'dor':str(i.dor)})
        print data
     return HttpResponse(content=json.dumps(({'data': data})),content_type='Application/json')
  return render(request, 'returns.html')

  # data = []
  # temp = {}
  # if request.method == 'POST':
  #    post = request.POST
  #    bid = post['bid']
  #    book_d = book.objects.get(bid = bid)
  #    datadump = booklend.objects.filter(book = book_d)
  #    if datadump.bid == bid :
  #      for i in datadump:
  #         print '?????'
  #         data.append({'bid':i.book.bid,'btitle':i.book.btitle,'uid':i.user.uid,'uname':i.user.uname,'doi':str(i.doi),'dor':str(i.dor)})
  #         print data
  #    else :
  #       dump = 'none'

  #   data = []
  # temp = {}
  # if request.method == 'POST':
  #    post1 = request.POST
  #    bid = post1['bid']
  #    if post1.has_key('post'):
  #     print '???'
      
  #    else:
  #     book_d = book.objects.get(bid = bid)
  #     if not booklend.objects.filter(bid=bid):
  #       data = 'none'
  #     else:
  #       book_d = book.objects.get(bid = bid)
  #       datadump = booklend.objects.filter(book = book_d)
  #       for i in datadump:
  #         print '?????'
  #         data.append({'bid':i.book.bid,'btitle':i.book.btitle,'uid':i.user.uid,'uname':i.user.uname,'doi':str(i.doi),'dor':str(i.dor)})
  #         print data
  #    return HttpResponse(content=json.dumps(({'data': data})),content_type='Application/json')
  # return render(request, 'returns.html')


@login_required
def bookreturns(request):
  temp = {}
  if request.method == 'POST':
      post = request.POST
      bid = post['bid']
      status = post['status']
      bookdetail = book.objects.get(bid = bid)
      datadump = booklend.objects.get(book=bookdetail)
      if datadump.status == 'Issued' : 
        datadump.status = post['status'] 
        datadump.save()    
        bookdetail.quantity = bookdetail.quantity +1
        bookdetail.save()
        dump = 'Book has been Returned Successfully!'
      else : 
        dump = 'Nothing to Return...'
      return HttpResponse(content=json.dumps(dump),content_type='Application/json')
  return render(request,'returns.html')
  

@login_required     
def returns(request):
    return render(request,'returns.html')
@login_required
def stock(request):
    return render(request,'stock.html')
@login_required
def uhistory(request):
    data = []
    temp = {}
    if request.method == 'POST':
       post = request.POST
       uid = post['uid']
       user_poi = user.objects.get(uid = uid)
       datadump = booklend.objects.filter(user = user_poi)
       

       for i in datadump:
          print 
          data.append({'uid':i.user.uid,'uname':i.user.uname,'bid':i.book.bid,'btitle':i.book.btitle,'status':i.status,'doi':str(i.doi),'dor':str(i.dor)})
          print data
       return HttpResponse(content=json.dumps(({'data': data})),content_type='Application/json')
    return render(request, 'uhistory.html')
@login_required
def bhistory(request):
    data = []
    temp = {}
    if request.method == 'POST':
       post = request.POST
       bid = post['bid']
       book_stock = book.objects.get(bid = bid)
       datadump = booklend.objects.filter(book = book_stock)
       

       for i in datadump:
          print 
          data.append({'bid':i.book.bid,'btitle':i.book.btitle,'uid':i.user.uid,'uname':i.user.uname,'status':i.status,'doi':str(i.doi),'dor':str(i.dor)})
          print data
       return HttpResponse(content=json.dumps(({'data': data})),content_type='Application/json')
    return render(request, 'bhistory.html')
@login_required
def userd(request):
  if request.method == 'POST':
      post = request.POST
      uid = post['uid']
      print '????'
     
      if post.has_key('post'):
          print 'check'
          try:
            obj = user.objects.get(uid=uid)
          except Exception as e:
            print e
         
          obj.uname = post['uname']
          obj.mobile = post['mobile']
          obj.uaddr = post['uaddr']
          obj.save()
          data = 'saved'
                
        
      
      else:
          if not user.objects.filter(uid=uid):
              data = 'none'
          else:
              user1 = user.objects.get(uid=uid)
              data = {'uid': user1.uid, 'uname': user1.uname, 'mobile':user1.mobile,'uaddr': user1.uaddr}
              print data   
      
      return HttpResponse(content=json.dumps(data),content_type='Application/json')

  return render(request,'user.html')
@login_required
def userdetails(request):
    data = []
    temp = {}
    if request.method == 'POST':
       datadump = user.objects.all()
       

       for i in datadump:
          print 
          data.append({'uid':i.uid,'uname':i.uname,'gender':i.gender,'mobile':i.mobile,'uaddr':i.uaddr})
          # ,'doi':str(i.doi),'dor':str(i.dor)
          print data
       return HttpResponse(content=json.dumps(({'data': data})),content_type='Application/json')
    return render(request, 'user.html')

@login_required
def stocks(request):
    data = []
    temp = {}
    if request.method == 'POST':
       # book_stock = book.objects.all(bid = bid)
       datadump = book.objects.all()
       

       for i in datadump:
          print 
          data.append({'bid':i.bid,'btitle':i.btitle,'category':i.category,'author':i.author,'publisher':i.publisher,'quantity':i.quantity})
          print data
       return HttpResponse(content=json.dumps(({'data': data})),content_type='Application/json')
    return render(request, 'stock.html')



@login_required
def modify(request):
    temp = {}
    if request.method == 'POST':
      post = request.POST
      uid = post['uid']
      obj = user.objects.get(uid=uid)
      obj.uname = post['uname']
      obj.mobile = post['mobile']
      obj.uaddr = post['uaddr']
      obj.save()
      data = 'saved'

      
      return HttpResponse(content=json.dumps({'data': data}),content_type='Application/json')
    return render(request,'uedit.html')
@login_required
def delete(request):
    temp = {}
    if request.method == 'POST':
      post = request.POST
      uid = post['uid']
      obj = user.objects.get(uid=uid)
      obj.uname = post['uname']
      obj.mobile = post['mobile']
      obj.uaddr = post['uaddr']
      obj.delete()
      data = 'deleted'

      
      return HttpResponse(content=json.dumps({'data': data}),content_type='Application/json')
    return render(request,'udelete.html')
@login_required
def bdelete(request):
    temp = {}
    if request.method == 'POST':
      post = request.POST
      bid = post['bid']
      obj = book.objects.get(bid=bid)
      obj.btitle = post['btitle']
      obj.author = post['author']
      obj.publisher = post['publisher']
      obj.delete()
      data = 'deleted'

      
      return HttpResponse(content=json.dumps({'data': data}),content_type='Application/json')
    return render(request,'bdelete.html')

@login_required
def bedit(request):
    temp = {}
    if request.method == 'POST':
      post = request.POST
      bid = post['bid']    
      obj = book.objects.get(bid=bid)
      obj.btitle = post['btitle']
      obj.author = post['author']
      obj.category = post['category']
      obj.publisher = post['publisher']
      obj.quantity = post['quantity']
      obj.save()
      data = 'saved'      
      return HttpResponse(content=json.dumps({'data': data}),content_type='Application/json')
    return render(request,'bedit.html')
    
@login_required
def uedit(request):
  if request.method == 'POST':
      post = request.POST
      uid = post['uid']
     
      if post.has_key('post1'):
          try:
            obj = user.objects.get(uid=uid)
          except Exception as e:
            print e
         
          obj.uname = post['uname']
          obj.mobile = post['mobile']
          obj.uaddr = post['uaddr']
          obj.save()
          data = 'saved'
                
        
      
      else:
          if not user.objects.filter(uid=uid):
              data = 'none'
          else:
              user1 = user.objects.get(uid=uid)
              data = {'uid': user1.uid, 'uname': user1.uname, 'mobile':user1.mobile,'uaddr': user1.uaddr}
              print data    
      
      return HttpResponse(content=json.dumps(data),content_type='Application/json')

  return render(request,'uedit.html')
@login_required
def udelete(request):
    return render(request,'udelete.html')
@login_required
def issued(request):
    if request.method == 'POST':
      post= request.POST
      bid = post['bid']
      btitle = post['btitle']
      uid = post['uid']
      uname = post['uname']
      status = post['status']
      doi = post['doi']
      dor = post['dor']
      # obj = book.objects.all()
      # obj.btitle = post['btitle']
      # # obj.quantity = post['quantity']
      # obj.save()
      
      # for i in req_field: 
      #   data[i] = post['all[%s]'%i]
      #   print data
      curr_user = user.objects.get(uid=uid)
      curr_book = book.objects.get(bid=bid) 
      if curr_book.quantity > 0 :
        curr_book.quantity = curr_book.quantity -1      
        curr_book.save() 
        dump = 'Book Has Been Issued Successfully!!!'
        # try: 
        
        if booklend.objects.filter(user=curr_user,book=curr_book):
          get_book = booklend.objects.get(user=curr_user,book=curr_book)
          get_book.status = status
          get_book.doi=doi
          get_book.dor=dor
          get_book.save()
        else:       
          booklend.objects.create(user=curr_user,book=curr_book,status=status,doi=doi,dor=dor)
          print booklend.objects.get(bid=bid)
        # except Exception as e:
        #   print e 
      else :
        dump = 'No More Copies are Available!'
        
      return HttpResponse(content=json.dumps(dump),content_type='Application/json')
    return render(request,'issue.html')





