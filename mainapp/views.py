from django.shortcuts import render,redirect,reverse
from .models import User,Cof,Cofextension,Danti,Rongji,Cuihuaji
from django.http import JsonResponse
import os
from CMS.settings import BASE_DIR

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
        kw = request.GET.get('kw')
        if kw:
            cof = Cof.objects.filter(name=kw.strip()).first()
            if cof:
                return redirect(reverse('cof_detail',kwargs={'cof_id':cof.id}))
            else:
                return render(request, 'index.html', context={'user': request.cmsuser})
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

def edit_cof(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        connection = request.POST.get('connection')
        dimension = request.POST.get('dimension')
        cof = Cof.objects.get(id=id)
        cof.name = name
        cof.connection = connection
        cof.dimension = dimension
        cof.save()
        return JsonResponse({'code':200,'message':''})

def cof_detail(request,cof_id):
    kw = request.GET.get('kw')
    cof = Cof.objects.get(id=cof_id)
    cofexts = cof.cofextension_set.all()
    if kw:
        print('-' * 20)
        print(kw)
        print('-'*20)
        if kw in '单体':
            print('单体')
            dantis = cof.cofextension_set.all()
            return render(request, 'cof_detail.html', context={'cof': cof, 'dantis': dantis, 'kw': kw})
        elif kw in '溶剂':
            print('进入溶剂')
            rongjis = cof.cofextension_set.all()
            return render(request, 'cof_detail.html', context={'cof': cof, 'rongjis': rongjis, 'kw': kw})
        elif kw in ('AcOH浓度' or 'AcOH量'):
            print('进入AcOH')
            acohs = cof.cofextension_set.all()
            return render(request, 'cof_detail.html', context={'cof': cof, 'acohs': acohs, 'kw': kw})
        elif kw in '温度':
            print('进入温度')
            temperatures = cof.cofextension_set.all()
            return render(request, 'cof_detail.html', context={'cof': cof, 'temperatures': temperatures, 'kw': kw})
        elif kw in '时间':
            print('进入时间')
            times = cof.cofextension_set.all()
            return render(request, 'cof_detail.html', context={'cof': cof, 'times': times, 'kw': kw})
        elif kw in 'PXRD主峰高度':
            print('进入PXRD主峰高度')
            pxrds = cof.cofextension_set.all()
            return render(request, 'cof_detail.html', context={'cof': cof, 'pxrds': pxrds, 'kw': kw})
        elif kw in 'ssnmr半峰宽(PPM)':
            print('ssnmr半峰宽')
            ssnmrs = cof.cofextension_set.all()
            return render(request, 'cof_detail.html', context={'cof': cof, 'ssnmrs': ssnmrs, 'kw': kw})
        elif kw in 'HP129Xe位移(PPM)':
            print('HP129Xe位移')
            hp129s = cof.cofextension_set.all()
            return render(request, 'cof_detail.html', context={'cof': cof, 'hp129s': hp129s, 'kw': kw})
        elif kw in '封管129Xe位移(PPM)':
            print('封管129Xe位移')
            _129xes = cof.cofextension_set.all()
            return render(request, 'cof_detail.html', context={'cof': cof, '129xes': _129xes, 'kw': kw})
        elif kw in '孔径大小(nm)':
            print('孔径大小')
            kongjings = cof.cofextension_set.all()
            return render(request, 'cof_detail.html', context={'cof': cof, 'kongjings': kongjings, 'kw': kw})
        elif kw in 'BET比表面积':
            print('BET比表面积')
            bets = cof.cofextension_set.all()
            return render(request, 'cof_detail.html', context={'cof': cof, 'bets': bets, 'kw': kw})
        elif kw in ('理论结构图' or 'graph'):
            print('理论结构图')
            graphs = cof.cofextension_set.all()
            return render(request, 'cof_detail.html', context={'cof': cof, 'graphs': graphs, 'kw': kw})
        elif kw in ('结构CIF' or 'cif'):
            print('cif')
            cifs = cof.cofextension_set.all()
            return render(request, 'cof_detail.html', context={'cof': cof, 'cifs': cifs, 'kw': kw})
        elif kw in 'PXRD图':
            pxrdgraphs = cof.cofextension_set.all()
            return render(request, 'cof_detail.html', context={'cof': cof, 'pxrdgraphs': pxrdgraphs, 'kw': kw})
        elif kw in ('其他文件' or 'other'):
            print('其他文件')
            others = cof.cofextension_set.all()
            return render(request, 'cof_detail.html', context={'cof': cof, 'others': others, 'kw': kw})
        elif kw in '备注':
            remarks = cof.cofextension_set.all()
            return render(request, 'cof_detail.html', context={'cof': cof, 'remarks': remarks, 'kw': kw})
        else:
            print('暂无结果')
            return render(request, 'cof_detail.html',context={'cof':cof,'error':'暂无结果'})
    print('over')
    return render(request,'cof_detail.html',context={'cof':cof,'cofexts':cofexts})


def add_cof_ext(request,cof_id):
    cof = Cof.objects.get(id=cof_id)
    if request.method == 'GET':
        return render(request,'add_cof.html',context={'cof':cof})
    else:
        try:
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
            if graph:
                with open(os.path.join(BASE_DIR,'static','files',graph.name), 'wb') as fp:
                    for chunk in graph.chunks():
                        fp.write(chunk)

            cif = request.FILES.get('cif')
            if cif:
                with open(os.path.join(BASE_DIR,'static','files',cif.name), 'wb') as fp:
                    for chunk in cif.chunks():
                        fp.write(chunk)

            graphpxrd = request.FILES.get('graphpxrd')
            if graphpxrd:
                with open(os.path.join(BASE_DIR,'static','files',graphpxrd.name), 'wb') as fp:
                    for chunk in graphpxrd.chunks():
                        fp.write(chunk)

            other = request.FILES.get('other')
            if other:
                with open(os.path.join(BASE_DIR,'static','files',other.name), 'wb') as fp:
                    for chunk in other.chunks():
                        fp.write(chunk)

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
        except ValueError:
            return render(request,'add_cof.html',context={'cof':cof,'error':'请输入必要数据！'})


def delete_cofext(request):
    if request.method == 'POST':
        cofext_id = request.POST.get('cofext_id')
        cofext = Cofextension.objects.get(id=cofext_id)
        cofext.delete()
        return JsonResponse({'code':200,'message':''})

def edit_cofext(request,cofext_id):
    cofext = Cofextension.objects.get(id=cofext_id)
    if request.method == 'GET':
        return render(request,'edit_cofext.html',context={'cofext':cofext})
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
        if graph:
            with open(os.path.join(BASE_DIR,'static','files',graph.name), 'wb') as fp:
                for chunk in graph.chunks():
                    fp.write(chunk)


        cif = request.FILES.get('cif')
        if cif:
            with open(os.path.join(BASE_DIR,'static','files',cif.name), 'wb') as fp:
                for chunk in cif.chunks():
                    fp.write(chunk)

        graphpxrd = request.FILES.get('graphpxrd')
        if graphpxrd:
            with open(os.path.join(BASE_DIR,'static','files',graphpxrd.name), 'wb') as fp:
                for chunk in graphpxrd.chunks():
                    fp.write(chunk)

        other = request.FILES.get('other')
        if other:
            with open(os.path.join(BASE_DIR,'static','files',other.name), 'wb') as fp:
                for chunk in other.chunks():
                    fp.write(chunk)

        remark = request.POST.get('remark')

        cofext.number = number
        cofext.acohnongdu = acohnongdu
        cofext.acohliang = acohliang
        cofext.temperature = temperature
        cofext.time = time
        cofext.is_solid = is_solid
        cofext.is_crystal = is_crystal
        cofext.pxrd = pxrd
        cofext.hp129 = hp129
        cofext.ssnmr = ssnmr
        cofext.fengguan129 = fengguan129
        cofext.kongjing = kongjing
        cofext.bet = bet
        if graph:
            cofext.graph = graph.name
        if cif:
            cofext.cif = cif.name
        if graphpxrd:
            cofext.graphpxrd = graphpxrd.name
        if other:
            cofext.other = other.name

        cofext.remark = remark

        cofext.save()

        if not danti == ['']:
            danti_list = list(zip(danti, danti_name, danti_structure))
            a = list(zip(danti_list,cofext.danti_set.all()))
            for item in a:
                item[-1].danti = item[0][0]
                item[-1].name = item[0][1]
                item[-1].structure = item[0][2]
                item[-1].save()

        if not rongji_name == ['']:
            rongji_list = list(zip(rongji_name, rongji_ml))
            a = list(zip(rongji_list, cofext.rongji_set.all()))
            for item in a:
                item[-1].name = item[0][0]
                item[-1].rongjiml = item[0][1]

                item[-1].save()

        if not cuihuaji == ['']:
            cuihuaji_list = list(zip(cuihuaji, cuihuaji_mg))
            a = list(zip(cuihuaji_list, cofext.cuihuaji_set.all()))
            for item in a:
                item[-1].cas1 = item[0][0]
                item[-1].cas1liang = item[0][1]
                item[-1].save()

        return redirect(reverse('cof_detail',kwargs={"cof_id":cofext.cof.id}))
