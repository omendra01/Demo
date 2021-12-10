from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    return render(request,'home.html')

def index(request):
    obj = StudentRecord.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(obj, 1)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request,'index.html',{'obj':obj,'users':users})
   
def addStudent(request):
    if request.method =='POST':
        student_name = request.POST.get('student')
        father_name = request.POST.get('father')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        phone_no = request.POST.get('phone')
        email = request.POST.get('email')
        class_opted = request.POST.get('clss')
        marks = request.POST.get('marks')
        if StudentRecord.objects.filter(phone_no=phone_no).exists():
            messages.warning(request,"Phone no already Register")   
            return redirect('addstd') 
        if StudentRecord.objects.filter(email=email).exists():
            messages.warning(request,"Eamil already Register")   
            return redirect('addstd')
          
        data=StudentRecord(student_name=student_name,dob=dob,city=city,pin=pin,email=email,marks=marks,
                    father_name=father_name,address=address,state=state,phone_no=phone_no,class_opted=class_opted,

                    )
        data.save()
        return redirect('index')    
    else:  
        return render(request,'new_student.html')


def signups(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpass')
        if password!=confirm_password:
            messages.warning(request,"Password not match")   
            return redirect('signup')         
        user = User.objects.create_user(username=username, email=email, password=password)
        user.set_password(password)
        user.save()
        messages.success(request,"Register Successfuly")
       
        return redirect('login')
    else:
        return render(request,'signup.html')   

def signin(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Username and Password not match? ")
        except:
            messages.error(request, "Invalid Credntial please Check Details")
    return render(request, 'login.html')






