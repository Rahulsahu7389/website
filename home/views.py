from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from home.models import Logged,Templ,Template1
from django.contrib import messages

MESSAGE_TAGS = {
    'name':'Rohan'
    
}


# Create your views here.
def logged(request):
    global MESSAGE_TAGS
    if request.method == 'POST':
       name2 = request.POST.get('name')
       password2 = request.POST.get('password')
       for i in Logged.objects.all():
           if name2 == i.name and password2 == i.password:
               MESSAGE_TAGS['name'] = name2
            #    user = form.save()
               return redirect('/home')
       
    #    user1 = authenticate(request,name = name2,password = password2)
    #    print(user1)

    #    if user1 is not None:
    #    print(Logged.objects.all())
    #    for i in Logged.objects.all():
    #        print(i.name,i.password)
       
    return render(request,'logins.html')

def index(request):
    # if request.user.is_anonymous:
    #     return render(request,'logins.html')
    messages.success(request,f'Hello! {MESSAGE_TAGS['name']}')    
    return render(request,'index.html')

def logoutUser(request):
    logout(request)
    return redirect('/')

def signed(request):
    if request.method == "POST":
        name1 = request.POST.get("name")
        pass2 = request.POST.get("password")
        log = Logged(name = name1, password = pass2)
        print('got it')
        log.save()
        return redirect("/")
    return render(request,'sign.html')

def temple(request):
    # l1 = []
    # l2 = []
    if request.method == "POST":
        t1 = request.POST.get("name")
        t2 = request.POST.get("branch")
        # t3 = request.POST.get("temp3")
        # t4 = request.POST.get("temp4")
        # print(t1,t2,t3,t4)

        # l1.append(t1)
        # l1.append(t2)
        # l1.append(t3)
        # l1.append(t4)
        # for i in range(4):
        #     if l1[i] == None: 
        #         l2.append('none')
        #     else:
        #         l2.append(l1[i])
        # (tm1,tm2,tm3,tm4) = tuple(l2)
        # print(tm1,tm2,tm3,tm4)
                
        tmplt = Template1(name1 = t1,name2 = t2,name3 = "none",name4 = "none", name5 = MESSAGE_TAGS['name'] )
        tmplt.save()
        return redirect("/query")
    return render(request,"form.html")

def acad(request):
    return render(request,'acad.html')

def clubs(request):
    return render(request,'clubs.html')

def sports(request):
    return render(request,'sports.html')

def queries(request):
    global MESSAGE_TAGS
    context = {}
    data = Template1.objects.all()
    for i in data:

        if i.name5 == MESSAGE_TAGS['name']:
            print(i,i.name5)
            context['year'] = i.name1
            context['branch'] = i.name2
    print(context)


    return render(request,'query.html',context)

