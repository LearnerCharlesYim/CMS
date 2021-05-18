from django.shortcuts import render,redirect,reverse
from .models import User,Cof,Cofextension,Danti,Rongji,Cuihuaji
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
    cofexts = cof.cofextension_set.all()
    return render(request,'cof_detail.html',context={'cof':cof,'cofexts':cofexts})

def add_cof_ext(request,cof_id):
    if request.method == 'GET':
        cof = Cof.objects.get(id=cof_id)
        return render(request,'add_cof.html',context={'cof':cof})
    else:
        number = request.POST.get('number')

        danti = request.POST.getlist('danti')
        danti_name = request.POST.getlist('danti_name')
        danti_structure = request.POST.getlist('danti_structure')

        rongji_name = request.POST.getlist('rongji_name')
        rongji_ml = request.POST.getlist('rongji_ml')

        cuihuaji = request.POST.getlist('cuihuaji')
        cuihuaji_mg = request.POST.getlist('cuihuaji_mg')

        acohnongdu = request.POST.get('acohnongdu')
        acohliang = request.POST.get('acohliang')
        temperature = request.POST.get('temperature')
        time = request.POST.get('time')
        is_solid = request.POST.get('is_solid')
        is_crystal = request.POST.get('is_crystal')
        pxrd = request.POST.get('pxrd')
        ssnmr = request.POST.get('ssnmr')
        hp129 = request.POST.get('hp129')
        fengguan129 = request.POST.get('fengguan129')
        kongjing = request.POST.get('kongjing')
        bet = request.POST.get('bet')

        graph = request.FILES.get('graph')
        cif = request.FILES.get('cif')
        graphpxrd = request.FILES.get('graphpxrd')
        other = request.FILES.get('other')

        remark = request.POST.get('remark')

        cofext = Cofextension(
            number=number,
            acohnongdu=acohnongdu,
            acohliang=acohliang,
            temperature=temperature,
            time=time,
            is_solid=is_solid,
            is_crystal=is_crystal,
            pxrd=pxrd,
            ssnmr=ssnmr,
            hp129=hp129,
            fengguan129=fengguan129,
            kongjing=kongjing,
            bet=bet,
            graph=graph.name if graph else None,
            cif=cif.name if cif else None,
            graphpxrd=graphpxrd.name if graphpxrd else None,
            other=other.name if other else None,
            remark=remark,
        )
        cofext.cof = Cof.objects.get(id=cof_id)
        cofext.save()

        if not danti == ['']:
            danti_list = list(zip(danti, danti_name, danti_structure))
            for item in danti_list:
                danti = Danti(danti=item[0],name=item[1],structure=item[2])
                danti.owner = cofext
                danti.save()

        if not rongji_name == ['']:
            rongji_list = list(zip(rongji_name, rongji_ml))
            for item in rongji_list:
                rongji = Rongji(name=item[0],rongjiml=item[1])
                rongji.owner = cofext
                rongji.save()

        if not cuihuaji == ['']:
            cuihuaji_list = list(zip(cuihuaji, cuihuaji_mg))
            for item in cuihuaji_list:
                cuihuaji_ = Cuihuaji(cas1=item[0],cas1liang=item[1])
                cuihuaji_.owner = cofext
                cuihuaji_.save()

        return redirect(reverse('cof_detail',kwargs={"cof_id":cof_id}))