from django.shortcuts import render,redirect,reverse
from .models import User,Cof,Cofextension
from django.http import JsonResponse

# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        username = request.POST.get('username')
        name = request.POST.get('name')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).first():
            user = User(username=username,name=name,password=password)
            user.save()
            return JsonResponse({'code': 200, 'message': ''})
        else:
            return JsonResponse({'code': 400, 'message': '用户名已存在'})

def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password).first()
        if user:
            request.session['user_id'] = user.id
            return JsonResponse({'code': 200, 'message': ''})
        else:
            return JsonResponse({'code': 400, 'message': '用户名或密码错误'})


def index(request):
    if request.cmsuser:
        cofs = Cof.objects.all()
        return render(request,'index.html',context={'user':request.cmsuser,'cofs':cofs})
    else:
        return redirect(reverse('signin'))


def logout(request):
    request.session.flush()
    return redirect(reverse('signin'))

def add_cof(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        connection = request.POST.get('connection')
        dimension = request.POST.get('dimension')
        cof = Cof(name=name,connection=connection,dimension=dimension)
        cof.author = request.cmsuser
        cof.save()
        return JsonResponse({'code':200,'message':''})

def delete_cof(request):
    if request.method == 'POST':
        data_id = request.POST.get('data_id')
        cof = Cof.objects.get(id=data_id)
        cof.delete()
        return JsonResponse({'code':200,'message':''})

def cof_detail(request,cof_id):
    cof = Cof.objects.get(id=cof_id)
    return render(request,'cof_detail.html',context={'cof':cof})

def add_cof_ext(request,cof_id):
    if request.method == 'GET':
        cof = Cof.objects.get(id=cof_id)
        return render(request,'add_cof.html',context={'cof':cof})
    else:
        danti = request.POST.getlist('danti')
        print(danti)
        return JsonResponse({})