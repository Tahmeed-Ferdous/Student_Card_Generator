from django.shortcuts import render
from django.shortcuts import redirect
from .models import Student
import os

# Create your views here.

def firstone(request):
    # number=0
    # if request.method=='POST':
    #     num1=request.POST.get('num1')
    #     num2=request.POST.get('num2')
    #     if num1 and num2:
    #         number=int(num1)+int(num2)
    # return render(request, 'index.html', {'number':number})

    # stu=Student.objects.create(name='Tareef Ferdous', roll=4)
    # stu.save()

    # stu=Student.objects.filter(name__icontains='T')
    # https://docs.djangoproject.com/en/5.1/topics/db/queries/
    # stu=Student.objects.get(id=1)
    # stu.name='sydul'
    # stu.roll=6
    # stu.save()
    # stu.delete()
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        img = request.FILES.get('img')
        
        if email and name and password:
            if Student.objects.filter(name=name).exists():
                error_message = "A student with this name already exists."
                return render(request, 'index.html', {'error': error_message})
            else:
                stu = Student.objects.create(email=email, name=name, password=password, img=img)
        
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

def delete_stu(request, id):
    stu = Student.objects.get(id=id)
    
    if stu.img and stu.img != 'def.png':
        if os.path.exists(stu.img.path):
            os.remove(stu.img.path)
    stu.delete()
    
    return redirect('firstone')

def update(request, id):
    stu=Student.objects.get(id=id)
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        img = request.FILES.get('img')
        stu.name=name
        stu.email=email
        stu.password=password
        stu.img=img
        stu.save()
        return redirect('/')
    return render(request,'update.html', {'stu':stu})

