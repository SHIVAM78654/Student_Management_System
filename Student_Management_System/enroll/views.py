from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .forms import Student_login,StudentRegistration
from django.contrib.auth import authenticate, login, logout
from .models import Stundent

# Create your views here.
def home(request):
        return render(request, 'enroll/home.html')

def student_signup(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/student_login/')
    else:
        form = StudentRegistration()
    return render(request, 'enroll/student_signup.html', {'form': form})


def student_login(request):
    if request.method == "POST":
        form=Student_login(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password = form.cleaned_data['password']
            user=Stundent.objects.filter(username=username, password=password).exists()
            if user:
                students = Stundent.objects.filter(username=username)
                return render(request, 'enroll/student_details.html',{'stu':students})
            else:
                 form=Student_login()
                 msg = "Invalid Username or Password !" 
                 return render(request,'enroll/student_login.html',{'msg':msg, 'form':form})

        else:
            form=Student_login()
            error = "Invalid Data !" 
            return render(request, 'enroll/student_login.html',{'msg': error})
    else:
        form=Student_login()
        return render(request,'enroll/student_login.html',{'form':form})
  


def admin_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    student=Stundent.objects.all()
                    return render(request, 'enroll/admin_section.html',{'stu':student})
                # else:
                #     error = "Invalid Username or Password"  # Customize error message for incorrect credentials
                #     return render(request, 'enroll/admin_login.html', {'er': error})
            else:
                error = "Invalid Username or Password !" 
                return render(request, 'enroll/admin_login.html', {'er': error})
        else:
            return render(request, 'enroll/admin_login.html')
    else:
         student=Stundent.objects.all()
         return render(request, 'enroll/admin_section.html',{'stu':student})



def admin_logout(request):
    logout(request)
    return HttpResponseRedirect('/admin_login/')

def update_data_for_student(request, id):
    if request.method == 'POST':
        pi = Stundent.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            student=Stundent.objects.filter(pk=id)
            return render(request, 'enroll/student_details.html',{'stu':student})   
    else:
        pi = Stundent.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/update_details_student.html', {'form':fm})

def update_data_for_admin(request, id):
    if request.method == 'POST':
        pi = Stundent.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            student=Stundent.objects.all()
            return render(request, 'enroll/admin_section.html',{'stu':student})   
        else:
            msg="unable to valid form"
            pi = Stundent.objects.get(pk=id)
            fm = StudentRegistration(instance=pi)
            return render(request, 'enroll/update_student_info.html', {'form':fm,'msg':msg})
            
    else:
        pi = Stundent.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/update_student_info.html', {'form':fm})

def delete_data(request, id):
        pi = Stundent.objects.get(pk=id)
        pi.delete()
        student=Stundent.objects.all()
        return render(request, 'enroll/admin_section.html',{'stu':student})
    
def student_details(request):
        student=Stundent.objects.all()
        return render(request, 'enroll/student_details.html',{'stu':student})


def change_password(request, id):
    if request.method == 'POST':
        pi = Stundent.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            student=Stundent.objects.get(pk=id)
            return render(request, 'enroll/student_details.html',{'stu':student})
        else:
            msg="unable to valid"
            pi = Stundent.objects.get(pk=id)
            fm = StudentRegistration(instance=pi)
            return render(request, 'enroll/change_password.html', {'form':fm,'msg':msg})
               
    else:
        msg="get request"
        pi = Stundent.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        return render(request, 'enroll/change_password.html', {'form':fm,'msg':msg})
    
def changed_details(request,username):
      students = Stundent.objects.filter(username=username)
      return render(request, 'enroll/student_details.html',{'stu':students})