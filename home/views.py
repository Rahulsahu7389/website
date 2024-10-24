from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from home.models import Logged
from django.contrib import messages
MESSAGE_TAGS = {
    
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