# from distutils.log import error
from django.shortcuts import render, redirect
from .models import Bus,Train
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import AddBusForm, AddTrainForm, UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request, 'myapp/home.html')
    else:
        return render(request, 'myapp/signin.html')
    

@login_required(login_url='signin')
def findbus(request):
    context = {}
    if request.method == 'POST':
        source_r = request.POST.get('source')
        dest_r = request.POST.get('destination')
        

        bus_list = Bus.objects.filter(source=source_r.upper(), dest=dest_r.upper(),)
        if bus_list:
            return render(request, 'myapp/buslist.html', locals())
        else:
            context["error"] = "Sorry no buses availiable"
            return render(request, 'myapp/findbus.html', context)
    else:
        return render(request, 'myapp/findbus.html')

@login_required(login_url='signin')
def findtrain(request):
    context = {}
    if request.method == 'POST':
        source_r = request.POST.get('source')
        dest_r = request.POST.get('destination')
        

        train_list = Train.objects.filter(source=source_r.upper(), dest=dest_r.upper(),)
        if train_list:
            return render(request, 'myapp/trainlist.html', locals())
        else:
            context["error"] = "Sorry no trains availiable"
            return render(request, 'myapp/findtrain.html', context)
    else:
        return render(request, 'myapp/findtrain.html')

def signup(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        password_r = request.POST.get('password')
        user = User.objects.create_user(name_r, email_r, password_r, )
        if user:
            login(request, user)
            return render(request, 'myapp/thank.html', context)
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'myapp/signup.html', context)
    else:
        return render(request, 'myapp/signup.html', context)

def loginerror(request,context):
    logout(request)  
    return render(request,'myapp/signin.html',context)



def signin(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        password_r = request.POST.get('password')
        user = authenticate(request, username=name_r, password=password_r)
        # validation = User.objects.filter(username = name_r).exists()
        if user:
            # user = User.objects.get(username = name_r)
            login(request, user)
            return render(request,'myapp/thanklogin.html')
            # context["user"] = name_r
            # context["id"] = request.user.id
            # user = request.POST.get('user','off')  
            # admin = request.POST.get('admin','off')    
            # if user!='on' and admin!='on':
            #     context["error"] = "Please choose your character ?"
            #     return loginerror(request,context)
            # elif user=='on' and admin=='on':
            #     context["error"] = "Please choose only one character ?"
            #     return loginerror(request,context)
            # elif user == 'on' and admin== 'off':
            #     return render(request,'myapp/thanklogin.html')

            # elif admin == 'on' and user == 'off':
            #     if request.user.is_superuser == True:
            #         return render(request,'myapp/admin.html')
            # else:
            #     context["error"] = "Please choose your character ?"
            # return loginerror(request,context)
        else:
            context["error"] = "Provide valid credentials"
            return loginerror(request,context)
    else:
        context["error"] = "You are not logged in"
        return render(request, 'myapp/signin.html', context)


def signout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'myapp/signin.html', context)


def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'myapp/success.html', context)

def admin(request):
    return render(request,'admin.html')

def load_form(request):
    form = UserRegisterForm
    return render(request,"myapp/add.html" , {'form':form})


def load_form_train(request):
    form = AddTrainForm
    return render(request,"myapp/addtrain.html" , {'form':form})    


def load_form_bus(request):
    form = AddBusForm
    return render(request,"myapp/addbus.html" , {'form':form})        

def add(request):
    fm = UserRegisterForm(request.POST)
    fm.save()
    messages.info(request,"Your Item Added Successfully !")
    return redirect('/show',)  

def addtrain(request):
    form = AddTrainForm(request.POST)
    form.save()
    messages.info(request,"Your Train Added Successfully !")
    return redirect('/showtrain',)

def addbus(request):
    form = AddBusForm(request.POST)
    form.save()
    messages.info(request,"Your Bus Added Successfully !")
    return redirect('/showbus',)

def show(request):
    user = User.objects.all()
    return render(request,'myapp/show.html',{'user':user})  

def showtrain(request):
    train = Train.objects.all()
    return render(request,'myapp/showtrain.html',{ 'train':train})  

def showbus(request):
    bus = Bus.objects.all()
    return render(request,'myapp/showbus.html',{ 'bus':bus})  

def edit(request, id):
    user = User.objects.get(id=id)
    return  render(request,"myapp/edit.html", {'user':user})

def edittrain(request, id):
    train = Train.objects.get(id=id)
    return  render(request,"myapp/edittrain.html", {'train':train})

def editbus(request, id):
    bus = Bus.objects.get(id=id)
    return  render(request,"myapp/editbus.html", {'bus':bus})

def update(request, id):
    user = User.objects.get(id=id)    
    #form = UserRegisterForm(request.POST, instance=user)
    #form.save()
    user.username = request.POST['username']
    user.email = request.POST['email']
    user.save()
    messages.info(request,"Your Item Updated Successfully !")
    return redirect("/show")

def updatetrain(request, id):
    train= Train.objects.get(id=id)    
    #form = UserRegisterForm(request.POST, instance=user)
    #form.save()
    train.train_no = request.POST['train_no']
    train.train_name = request.POST['train_name']
    train.source = request.POST['source']
    train.dest = request.POST['dest']
    train.total_km = request.POST['total_km']
    train.travel_time = request.POST['travel_time']
    train.nos = request.POST['nos']
    train.price = request.POST['price']
    train.date = request.POST['date']
    train.time = request.POST['time']
    train.save()
    messages.info(request,"Your Item Updated Successfully !")
    return redirect("/showtrain")

def updatebus(request, id):
    bus= Bus.objects.get(id=id)    
    #form = UserRegisterForm(request.POST, instance=user)
    #form.save()
    bus.bus_no = request.POST['bus_no']
    bus.bus_name = request.POST['bus_name']
    bus.source = request.POST['source']
    bus.dest = request.POST['dest']
    bus.total_km = request.POST['total_km']
    bus.travel_time = request.POST['travel_time']
    bus.nos = request.POST['nos']
    bus.price = request.POST['price']
    bus.date = request.POST['date']
    bus.time = request.POST['time']
    bus.save()
    messages.info(request,"Your Item Updated Successfully !")
    return redirect("/showbus")

def delete(request, id):
    user = User.objects.get(id=id)    
    user.delete()
    return redirect("/show")
    
def deletetrain(request, id):
    train = Train.objects.get(id=id)    
    train.delete()
    return redirect("/showtrain")

def deletebus(request, id):
    bus = Bus.objects.get(id=id)    
    bus.delete()
    return redirect("/showbus")
            
