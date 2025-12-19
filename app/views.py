"""
Definition of views.
"""

from datetime import datetime
from math import e
from webbrowser import get
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpRequest
from .forms import IlmiyForm, OquvForm 
from .models import Foydalanuvchilar, oquvIshlari, ilmiy_ishlari as ilmiy , ilmiy_ishlari as ilmiy_a, Kafedralar
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.hashers import check_password
def login_view(request):
    if request.method == 'POST':
        login = request.POST.get('login_f')
        password = request.POST.get('password')

        try:
            user = Foydalanuvchilar.objects.get(login_f=login)
        except Foydalanuvchilar.DoesNotExist:
            user = None

        if user and user.parol == password:
            if user.foydalanuvchi_rol == 'kafedra mudiri':
                request.session['user_id'] = user.id
                request.session['username'] = user.login_f
                return redirect('home2')
            elif user.foydalanuvchi_rol =='dekan':
                request.session['user_id'] = user.id
                request.session['username'] = user.login_f
                return redirect('home3')
            else:
                request.session['user_id'] = user.id
                request.session['username'] = user.login_f
                return redirect('home')
        else:
            messages.error(request, 'Login yoki parol xato!')

    return render(request, 'app/login.html', {'year': datetime.now().year})
def login(request):
    """Renders the login page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/login.html',
        {
            'title':'Login',
            'year':datetime.now().year,
        }
    )
def home(request):
    user_id = request.session.get('user_id')
    foydalanuvchi=Foydalanuvchilar.objects.get(id=user_id)
    maqolalar_soni=ilmiy.objects.filter(muallif_id=foydalanuvchi.id, turi='maqola').count()
    scopuslar_soni=ilmiy.objects.filter(muallif_id=foydalanuvchi.id, turi='scopus').count()
    oquv_soni= oquvIshlari.objects.filter(muallif_id=foydalanuvchi.id).count()
    ilmiy_soni= ilmiy.objects.filter(muallif_id=foydalanuvchi.id).count()
    jami= oquv_soni+ilmiy_soni
    yanvar_o=oquvIshlari.objects.filter(sana__month=1, muallif_id=foydalanuvchi.id).count()
    fevral_o=oquvIshlari.objects.filter(sana__month=2, muallif_id=foydalanuvchi.id).count()
    mart_o=oquvIshlari.objects.filter(sana__month=3, muallif_id=foydalanuvchi.id).count()
    aprel_o=oquvIshlari.objects.filter(sana__month=4, muallif_id=foydalanuvchi.id).count()
    may_o=oquvIshlari.objects.filter(sana__month=5, muallif_id=foydalanuvchi.id).count()
    iyun_o=oquvIshlari.objects.filter(sana__month=6, muallif_id=foydalanuvchi.id).count()
    iyul_o=oquvIshlari.objects.filter(sana__month=7, muallif_id=foydalanuvchi.id).count()
    avgust_o=oquvIshlari.objects.filter(sana__month=8, muallif_id=foydalanuvchi.id).count()
    sentabr_o=oquvIshlari.objects.filter(sana__month=9, muallif_id=foydalanuvchi.id).count()
    oktabr_o=oquvIshlari.objects.filter(sana__month=10, muallif_id=foydalanuvchi.id).count()
    noyabr_o=oquvIshlari.objects.filter(sana__month=11, muallif_id=foydalanuvchi.id).count()
    dekabr_o=oquvIshlari.objects.filter(sana__month=12, muallif_id=foydalanuvchi.id).count()
    yanvar_i=ilmiy.objects.filter(sana__month=1, muallif_id=foydalanuvchi.id).count()
    fevral_i=ilmiy.objects.filter(sana__month=2, muallif_id=foydalanuvchi.id).count()
    mart_i=ilmiy.objects.filter(sana__month=3, muallif_id=foydalanuvchi.id).count()
    aprel_i=ilmiy.objects.filter(sana__month=4, muallif_id=foydalanuvchi.id).count()
    may_i=ilmiy.objects.filter(sana__month=5, muallif_id=foydalanuvchi.id).count()
    iyun_i=ilmiy.objects.filter(sana__month=6, muallif_id=foydalanuvchi.id).count()
    iyul_i=ilmiy.objects.filter(sana__month=7, muallif_id=foydalanuvchi.id).count()
    avgust_i=ilmiy.objects.filter(sana__month=8, muallif_id=foydalanuvchi.id).count()
    sentabr_i=ilmiy.objects.filter(sana__month=9, muallif_id=foydalanuvchi.id).count()
    oktabr_i=ilmiy.objects.filter(sana__month=10, muallif_id=foydalanuvchi.id).count()
    noyabr_i=ilmiy.objects.filter(sana__month=11, muallif_id=foydalanuvchi.id).count()
    dekabr_i=ilmiy.objects.filter(sana__month=12, muallif_id=foydalanuvchi.id).count()
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/profil.html',
        {
            'title':'Home Page',
            'foydalanuvchi':foydalanuvchi,
            'year':datetime.now().year,
            'maqolalar_soni':maqolalar_soni,
            'scopuslar_soni':scopuslar_soni,
            'oquv_soni':oquv_soni,
            'jami':jami,
            'oy_o':[yanvar_o, fevral_o, mart_o, aprel_o, may_o, iyun_o, iyul_o, avgust_o, sentabr_o, oktabr_o, noyabr_o, dekabr_o],
            'oy_i':[yanvar_i, fevral_i, mart_i, aprel_i, may_i, iyun_i, iyul_i, avgust_i, sentabr_i, oktabr_i, noyabr_i, dekabr_i],

        }
    )
def home2(request):
    user_id = request.session.get('user_id')
    foydalanuvchi=Foydalanuvchilar.objects.get(id=user_id)
    maqolalar_soni=0
    scopuslar_soni=0
    oquv_soni=0
    ilmiy_soni=0
    for muallif in Foydalanuvchilar.objects.filter(kafedra = foydalanuvchi.kafedra):
        maqolalar_soni+=ilmiy.objects.filter(muallif_id=muallif.id, turi='maqola').count()
        scopuslar_soni+=ilmiy.objects.filter(muallif_id=muallif.id, turi='scopus').count()
        oquv_soni+= oquvIshlari.objects.filter(muallif_id=muallif.id).count()
        ilmiy_soni+= ilmiy.objects.filter(muallif_id=muallif.id).count()
    jami= oquv_soni+ilmiy_soni
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/profil2.html',
        {
            'title':'Home Page',
            'foydalanuvchi':foydalanuvchi,
            'year':datetime.now().year,
            'maqolalar_soni':maqolalar_soni,
            'scopuslar_soni':scopuslar_soni,
            'oquv_soni':oquv_soni,
            'jami':jami,    
        }
    )
def home3(request):
    user_id = request.session.get('user_id')
    foydalanuvchi=Foydalanuvchilar.objects.get(id=user_id)
    maqolalar_soni=0
    scopuslar_soni=0
    oquv_soni=0
    ilmiy_soni=0
    for kafedra_f in Kafedralar.objects.filter(fakultet=foydalanuvchi.fakulteti):
        for muallif in Foydalanuvchilar.objects.filter(kafedra=kafedra_f):
            maqolalar_soni+=ilmiy.objects.filter(muallif_id=muallif.id, turi='maqola').count()
            scopuslar_soni+=ilmiy.objects.filter(muallif_id=muallif.id, turi='scopus').count()
            oquv_soni+= oquvIshlari.objects.filter(muallif_id=muallif.id).count()
            ilmiy_soni+= ilmiy.objects.filter(muallif_id=muallif.id).count()
    jami=oquv_soni+ilmiy_soni
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/profil3.html',
        {
            'title':'Home Page',
            'foydalanuvchi':foydalanuvchi,
            'year':datetime.now().year,
            'maqolalar_soni':maqolalar_soni,
            'scopuslar_soni':scopuslar_soni,
            'oquv_soni':oquv_soni,
            'jami':jami,
        }
    )
def oquv_ishlari(request, user_id):
    """Renders the oquv_ishlari page."""
    assert isinstance(request, HttpRequest)
    foydalanuvchi = Foydalanuvchilar.objects.get(id=user_id)
    maqola=oquvIshlari.objects.filter(muallif_id=foydalanuvchi.id)
    turi=oquvIshlari.objects.values_list('turi', flat=True).distinct()
    ish_muallifiy= oquvIshlari.objects.filter(muallif_id=foydalanuvchi.id).values_list('ish_mualliflari', flat=True).distinct()
    ish_muallifi = []
    for qator in ish_muallifiy:
        if qator: 
            ish_muallifi.extend([m.strip() for m in qator.split(',')])
            ish_muallifi = list(set(ish_muallifi))
    return render(
        request,
        'app/o`quv_ishlari.html',
        {
            'title':'Oquv Ishlari',
            'message':'Your oquv_ishlari page.',
            'year':datetime.now().year,
            'maqola':maqola,
            'foydalanuvchi': foydalanuvchi,
            'turi': turi, 
            'ish_muallifi':ish_muallifi
        }
    )
def ilmiy_ishlari(request, user_id):
    """Renders the oquv_ishlari page."""
    assert isinstance(request, HttpRequest)
    foydalanuvchi = Foydalanuvchilar.objects.get(id=user_id)
    maqolalar=ilmiy.objects.filter(muallif_id=foydalanuvchi.id)
    turi=ilmiy.objects.values_list('turi', flat=True).distinct()
    ish_muallifiy= ilmiy.objects.filter(muallif_id=foydalanuvchi.id).values_list('ish_mualliflari', flat=True).distinct()
    ish_muallifi = []

    for qator in ish_muallifiy:
        if qator: 
            ish_muallifi.extend([m.strip() for m in qator.split(',')])
            ish_muallifi = list(set(ish_muallifi))
    return render(
        request,
        'app/ilmiy_ishlar.html',
        {
            'title':'Ilmiy Ishlari',
            'message':'Your ilmiy_ishlari page.',
            'year':datetime.now().year,
            'maqola':maqolalar,
            'foydalanuvchi': foydalanuvchi,
            'turi': turi, 
            'ish_muallifi':ish_muallifi
        }
    )
def profile(request, user_id):
    
    assert isinstance(request, HttpRequest)
    foydalanuvchi=Foydalanuvchilar.objects.get(id=user_id)
    maqolalar_soni=ilmiy.objects.filter(muallif_id=foydalanuvchi.id, turi='maqola').count()
    scopuslar_soni=ilmiy.objects.filter(muallif_id=foydalanuvchi.id, turi='scopus').count()
    oquv_soni= oquvIshlari.objects.filter(muallif_id=foydalanuvchi.id).count()
    ilmiy_soni= ilmiy.objects.filter(muallif_id=foydalanuvchi.id).count() 
    jami=oquv_soni+ilmiy_soni
    yanvar_o=oquvIshlari.objects.filter(sana__month=1, muallif_id=foydalanuvchi.id).count()
    fevral_o=oquvIshlari.objects.filter(sana__month=2, muallif_id=foydalanuvchi.id).count()
    mart_o=oquvIshlari.objects.filter(sana__month=3, muallif_id=foydalanuvchi.id).count()
    aprel_o=oquvIshlari.objects.filter(sana__month=4, muallif_id=foydalanuvchi.id).count()
    may_o=oquvIshlari.objects.filter(sana__month=5, muallif_id=foydalanuvchi.id).count()
    iyun_o=oquvIshlari.objects.filter(sana__month=6, muallif_id=foydalanuvchi.id).count()
    iyul_o=oquvIshlari.objects.filter(sana__month=7, muallif_id=foydalanuvchi.id).count()
    avgust_o=oquvIshlari.objects.filter(sana__month=8, muallif_id=foydalanuvchi.id).count()
    sentabr_o=oquvIshlari.objects.filter(sana__month=9, muallif_id=foydalanuvchi.id).count()
    oktabr_o=oquvIshlari.objects.filter(sana__month=10, muallif_id=foydalanuvchi.id).count()
    noyabr_o=oquvIshlari.objects.filter(sana__month=11, muallif_id=foydalanuvchi.id).count()
    dekabr_o=oquvIshlari.objects.filter(sana__month=12, muallif_id=foydalanuvchi.id).count()
    yanvar_i=ilmiy.objects.filter(sana__month=1, muallif_id=foydalanuvchi.id).count()
    fevral_i=ilmiy.objects.filter(sana__month=2, muallif_id=foydalanuvchi.id).count()
    mart_i=ilmiy.objects.filter(sana__month=3, muallif_id=foydalanuvchi.id).count()
    aprel_i=ilmiy.objects.filter(sana__month=4, muallif_id=foydalanuvchi.id).count()
    may_i=ilmiy.objects.filter(sana__month=5, muallif_id=foydalanuvchi.id).count()
    iyun_i=ilmiy.objects.filter(sana__month=6, muallif_id=foydalanuvchi.id).count()
    iyul_i=ilmiy.objects.filter(sana__month=7, muallif_id=foydalanuvchi.id).count()
    avgust_i=ilmiy.objects.filter(sana__month=8, muallif_id=foydalanuvchi.id).count()
    sentabr_i=ilmiy.objects.filter(sana__month=9, muallif_id=foydalanuvchi.id).count()
    oktabr_i=ilmiy.objects.filter(sana__month=10, muallif_id=foydalanuvchi.id).count()
    noyabr_i=ilmiy.objects.filter(sana__month=11, muallif_id=foydalanuvchi.id).count()
    dekabr_i=ilmiy.objects.filter(sana__month=12, muallif_id=foydalanuvchi.id).count()
    return render(
        request,
        'app/profil.html',
        {
            'foydalanuvchi':foydalanuvchi,
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'maqolalar_soni':maqolalar_soni,
            'scopuslar_soni':scopuslar_soni,
            'oquv_soni':oquv_soni,
            'jami':jami,
            'oy_o':[yanvar_o, fevral_o, mart_o, aprel_o, may_o, iyun_o, iyul_o, avgust_o, sentabr_o, oktabr_o, noyabr_o, dekabr_o],
            'oy_i':[yanvar_i, fevral_i, mart_i, aprel_i, may_i, iyun_i, iyul_i, avgust_i, sentabr_i, oktabr_i, noyabr_i, dekabr_i],
            
           
        }
    )
def qoshish(request, user_id):
    assert isinstance(request, HttpRequest)
    foydalanuvchi=Foydalanuvchilar.objects.get(id=user_id)
    return render(
        request,
        'app/tahrirlash.html',
        {
            'foydalanuvchi':foydalanuvchi,
            'title':'Qoshish',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def qoshish_i(request, user_id):
    assert isinstance(request, HttpRequest)
    foydalanuvchi=Foydalanuvchilar.objects.get(id=user_id)
    return render(
        request,
        'app/tahrirlash_i.html',
        {
            'foydalanuvchi':foydalanuvchi,
            'title':'Qoshish_i',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def qoshish_oquv(request, user_id):
    foydalanuvchi=Foydalanuvchilar.objects.get(id=user_id)
    assert isinstance(request, HttpRequest)
    if request.method=="POST":
        turi=request.POST.get("turi")
        nomi=request.POST.get("nomi")
        sana=request.POST.get("sana")
        muallif_id=request.POST.get("muallif")
        ish_mualliflari=request.POST.get("ish_mualliflari")
        betlar_soni=request.POST.get("betlar_soni")
        fayl=request.FILES.get("fayl")
        muallif=Foydalanuvchilar.objects.get(id=muallif_id)
        yangi=oquvIshlari(turi=turi,nomi=nomi,sana=sana,muallif=muallif,betlar_soni=betlar_soni,fayl=fayl,ish_mualliflari=ish_mualliflari)
        yangi.save()
    return render(
        request,
        'app/tahrirlash.html',
        {
            'foydalanuvchi':foydalanuvchi,
            'title':'Qoshish',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def qoshish_ilmiy(request, user_id):
    foydalanuvchi=Foydalanuvchilar.objects.get(id=user_id)
    assert isinstance(request, HttpRequest)
    if request.method=="POST":
        turi=request.POST.get("turi")
        nomi=request.POST.get("nomi")
        sana=request.POST.get("sana")
        muallif_id=request.POST.get("muallif")
        haqida=request.POST.get("haqida")
        ish_mualliflari=request.POST.get("ish_mualliflari")
        kategoriya=request.POST.get("kategoriya")
        fayl=request.FILES.get("fayl")
        muallif=Foydalanuvchilar.objects.get(id=muallif_id)
        yangi=ilmiy(turi=turi,nomi=nomi,sana=sana,muallif=muallif, ish_mualliflari=ish_mualliflari ,kategoriya=kategoriya,fayl=fayl, haqida=haqida)
        yangi.save()
    return render(
        request,
        'app/tahrirlash_i.html',
        {

            'title':'Qoshish',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'foydalanuvchi':foydalanuvchi,
        }
    )
def ochir(request, j_id, user_id):
    foydalanuvchi=Foydalanuvchilar.objects.get(id=user_id)
    assert isinstance(request, HttpRequest)
    if j_id==1:
        ochir=oquvIshlari.objects.filter(muallif_id=foydalanuvchi.id)
    else:
        ochir=ilmiy.objects.filter(muallif_id=foydalanuvchi.id)
    return render(
        request,
        'app/ochir.html',
        {
            'ochir':ochir,
            'title':'Ochir',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'j_id':j_id,
            'foydalanuvchi':foydalanuvchi

        }
        )
def ochirish(request, i_id, j_id, user_id):
    assert isinstance(request, HttpRequest)
    foydalanuvchi=Foydalanuvchilar.objects.get(id=user_id)
    if request.method=="POST" and j_id==1:
        maqola=oquvIshlari.objects.filter(muallif_id=foydalanuvchi.id)
        ochir=get_object_or_404(oquvIshlari, id=i_id)
        ochir.delete()
        return render(
        request,
        'app/o`quv_ishlari.html',
        {
            'title':'Oquv Ishlari',
            'message':'Your oquv_ishlari page.',
            'year':datetime.now().year,
            'maqola':maqola,
            'foydalanuvchi':foydalanuvchi
        }
        )
    elif request.method=="POST" and j_id==2:
        maqola=ilmiy.objects.filter(muallif_id=foydalanuvchi.id)
        ochir=get_object_or_404(ilmiy, id=i_id)
        ochir.delete()
        return render(
        request,
        'app/ilmiy_ishlar.html',
        {
            'title':'Oquv Ishlari',
            'message':'Your oquv_ishlari page.',
            'year':datetime.now().year,
            'maqola':maqola,
            'foydalanuvchi':foydalanuvchi
        }
        )
def filtrlash_ilmiy(request, user_id):
    foydalanuvchi=Foydalanuvchilar.objects.get(id=user_id)
    start = request.GET.get('from')
    end = request.GET.get('to')
    data = ilmiy.objects.filter(muallif_id=foydalanuvchi.id)
    turi= request.GET.get('turi')
    turlar = ilmiy.objects.values_list('turi', flat=True).distinct()
    ish_muallifi = request.GET.get('ish_muallifi')
    if start and end:
        data = data.filter(sana__range=[start, end], muallif_id=foydalanuvchi.id)
    if turi=="":
        data = data
    else:
        data = [item for item in data if item.turi == turi]
    if ish_muallifi=="":
        data = data
    else:
        data = [item for item in data if item.ish_mualliflari and ish_muallifi in [m.strip() for m in item.ish_mualliflari.split(',')]]
    ish_muallifiy= ilmiy.objects.filter(muallif_id=foydalanuvchi.id).values_list('ish_mualliflari', flat=True).distinct()
    ish_muallifi = []

    for qator in ish_muallifiy:
        if qator: 
            ish_muallifi.extend([m.strip() for m in qator.split(',')])
            ish_muallifi = list(set(ish_muallifi))
    return render(request, 'app/ilmiy_ishlar.html', {'maqola': data, 'foydalanuvchi':foydalanuvchi, 'turi': turlar, 'ish_muallifi':ish_muallifi})
def filtrlash_ilmiy2(request, user_id):
    foydalanuvchi=Foydalanuvchilar.objects.get(id=user_id)
    start = request.GET.get('from')
    end = request.GET.get('to')
    turi= request.GET.get('turi')
    ish_muallifi = request.GET.get('ish_muallifi')
    ish_muallifiy= []
    turlar = ilmiy.objects.values_list('turi', flat=True).distinct()
    maqolalar=[]
    for muallif in Foydalanuvchilar.objects.filter(kafedra = foydalanuvchi.kafedra):
        maqolalar+=ilmiy.objects.filter(muallif_id=muallif.id)
        ish_muallifiy += ilmiy.objects.filter(muallif_id=muallif.id).values_list('ish_mualliflari', flat=True).distinct()
    data = maqolalar
    if start and end:
        data = [item for item in maqolalar if start <= item.sana.strftime('%Y-%m-%d') <= end]
    if turi=="":
        data = data
    else:
        data = [item for item in data if item.turi == turi]
    if ish_muallifi=="":
        data = data
    else:
        data = [item for item in data if item.ish_mualliflari and ish_muallifi in [m.strip() for m in item.ish_mualliflari.split(',')]]
    
    ish_muallifi = []

    for qator in ish_muallifiy:
        if qator: 
            ish_muallifi.extend([m.strip() for m in qator.split(',')])
            ish_muallifi=list(set(ish_muallifi))
    return render(request, 'app/ilmiy_ishlar2.html', {'maqola': data, 'foydalanuvchi':foydalanuvchi, 'turi': turlar, 'ish_muallifi':ish_muallifi})
def filtrlash_ilmiy3(request, user_id):
    start = request.GET.get('from')
    end = request.GET.get('to')
    foydalanuvchi=Foydalanuvchilar.objects.get(id=user_id)
    turi= request.GET.get('turi')
    kafedra = request.GET.get('kafedra')
    ish_muallifi = request.GET.get('ish_muallifi')
    ish_muallifiy= []
    turlar = ilmiy.objects.values_list('turi', flat=True).distinct()
    if kafedra=="":
        kafedra_1=Kafedralar.objects.filter(fakultet = foydalanuvchi.fakulteti)
    else:
        kafedra_1= Kafedralar.objects.get(nomi=kafedra)
    kafedralar = Kafedralar.objects.filter(fakultet = foydalanuvchi.fakulteti)
    maqolalar=[]
    if kafedra=="":
        for kafedra_1 in Kafedralar.objects.filter(fakultet = foydalanuvchi.fakulteti):
            for muallif in Foydalanuvchilar.objects.filter(kafedra = kafedra_1):
                maqolalar+=ilmiy.objects.filter(muallif_id=muallif.id)
                ish_muallifiy +=ilmiy.objects.filter(muallif_id=muallif.id).values_list('ish_mualliflari', flat=True).distinct()
    else:
        for muallif in Foydalanuvchilar.objects.filter(kafedra=kafedra_1.id):
                maqolalar+=ilmiy.objects.filter(muallif_id=muallif.id)
                ish_muallifiy +=ilmiy.objects.filter(muallif_id=muallif.id).values_list('ish_mualliflari', flat=True).distinct()
    data = maqolalar
    
    if start and end:
        data = [item for item in maqolalar if start <= item.sana.strftime('%Y-%m-%d') <= end]
    if turi=="":
        data = data
    else:
        data = [item for item in data if item.turi == turi]
    if ish_muallifi=="":
        data = data
    else:
        data = [item for item in data if item.ish_mualliflari and ish_muallifi in [m.strip() for m in item.ish_mualliflari.split(',')]]
    
    ish_muallifi = []

    for qator in ish_muallifiy:
        if qator: 
            ish_muallifi.extend([m.strip() for m in qator.split(',')])
            ish_muallifi=list(set(ish_muallifi))
    return render(request, 'app/ilmiy_ishlar3.html', {'maqola': data, 'foydalanuvchi':foydalanuvchi, 'kafedralar': kafedralar, 'turi': turlar, 'ish_muallifi':ish_muallifi })

def filtrlash_oquv(request, user_id):
    foydalanuvchi=Foydalanuvchilar.objects.get(id=user_id)
    start = request.GET.get('from')
    end = request.GET.get('to')
    turi= request.GET.get('turi')
    turlar = oquvIshlari.objects.values_list('turi', flat=True).distinct()
    ish_muallifi = request.GET.get('ish_muallifi')
    data = oquvIshlari.objects.filter(muallif_id=foydalanuvchi.id)
    if start and end:
        data = data.filter(sana__range=[start, end], muallif_id=foydalanuvchi.id)
    if turi=="":
        data = data
    else:
        data = [item for item in data if item.turi == turi]
    if ish_muallifi=="":
        data = data
    else:
        data = [item for item in data if item.ish_mualliflari and ish_muallifi in [m.strip() for m in item.ish_mualliflari.split(',')]]
    ish_muallifiy= oquvIshlari.objects.filter(muallif_id=foydalanuvchi.id).values_list('ish_mualliflari', flat=True).distinct()
    ish_muallifi = []

    for qator in ish_muallifiy:
        if qator: 
            ish_muallifi.extend([m.strip() for m in qator.split(',')])
            ish_muallifi=list(set(ish_muallifi))
    return render(request, 'app/o`quv_ishlari.html', {'maqola': data, 'foydalanuvchi': foydalanuvchi, 'turi': turlar, 'ish_muallifi':ish_muallifi})
def filtrlash_oquv2(request, user_id):
    foydalanuvchi=Foydalanuvchilar.objects.get(id=user_id)
    start = request.GET.get('from')
    end = request.GET.get('to')
    turi= request.GET.get('turi')
    ish_muallifi = request.GET.get('ish_muallifi')
    ish_muallifiy= []
    turlar = oquvIshlari.objects.values_list('turi', flat=True).distinct()
    maqolalar=[]
    for muallif in Foydalanuvchilar.objects.filter(kafedra = foydalanuvchi.kafedra):
        maqolalar+=oquvIshlari.objects.filter(muallif_id=muallif.id)
        ish_muallifiy += oquvIshlari.objects.filter(muallif_id=muallif.id).values_list('ish_mualliflari', flat=True).distinct()
    data = maqolalar
    if start and end:
        data = [item for item in maqolalar if start <= item.sana.strftime('%Y-%m-%d') <= end]
    if turi=="":
        data = data
    else:
        data = [item for item in data if item.turi == turi]
    if ish_muallifi=="":
        data = data
    else:
        data = [item for item in data if item.ish_mualliflari and ish_muallifi in [m.strip() for m in item.ish_mualliflari.split(',')]]
    
    ish_muallifi = []

    for qator in ish_muallifiy:
        if qator: 
            ish_muallifi.extend([m.strip() for m in qator.split(',')])
            ish_muallifi=list(set(ish_muallifi))
    return render(request, 'app/o`quv_ishlari2.html', {'maqola': data, 'foydalanuvchi':foydalanuvchi, 'turi': turlar, 'ish_muallifi':ish_muallifi})
def filtrlash_oquv3(request, user_id):
    start = request.GET.get('from')
    end = request.GET.get('to')
    foydalanuvchi=Foydalanuvchilar.objects.get(id=user_id)
    kafedra = request.GET.get('kafedra')
    turi= request.GET.get('turi')
    ish_muallifi = request.GET.get('ish_muallifi')
    ish_muallifiy= []
    turlar = oquvIshlari.objects.values_list('turi', flat=True).distinct()
    if kafedra=="":
        kafedra_1=Kafedralar.objects.filter(fakultet = foydalanuvchi.fakulteti)
    else:
        kafedra_1= Kafedralar.objects.get(nomi=kafedra)
    kafedralar = Kafedralar.objects.filter(fakultet = foydalanuvchi.fakulteti)
    maqolalar=[]
    if kafedra=="":
        for kafedra_1 in Kafedralar.objects.filter(fakultet = foydalanuvchi.fakulteti):
            for muallif in Foydalanuvchilar.objects.filter(kafedra = kafedra_1):
                maqolalar+=oquvIshlari.objects.filter(muallif_id=muallif.id)
                ish_muallifiy +=oquvIshlari.objects.filter(muallif_id=muallif.id).values_list('ish_mualliflari', flat=True).distinct()
    else:
        for muallif in Foydalanuvchilar.objects.filter(kafedra=kafedra_1.id):
                maqolalar+=oquvIshlari.objects.filter(muallif_id=muallif.id)
                ish_muallifiy +=oquvIshlari.objects.filter(muallif_id=muallif.id).values_list('ish_mualliflari', flat=True).distinct()
    data = maqolalar
    if start and end:
        data = [item for item in maqolalar if start <= item.sana.strftime('%Y-%m-%d') <= end]
    if turi=="":
        data = data
    else:
        data = [item for item in data if item.turi == turi]
    if ish_muallifi=="":
        data = data
    else:
        data = [item for item in data if item.ish_mualliflari and ish_muallifi in [m.strip() for m in item.ish_mualliflari.split(',')]]
    
    ish_muallifi = []

    for qator in ish_muallifiy:
        if qator: 
            ish_muallifi.extend([m.strip() for m in qator.split(',')])
            ish_muallifi=list(set(ish_muallifi))
    return render(request, 'app/o`quv_ishlari3.html', {'maqola': data, 'foydalanuvchi':foydalanuvchi, 'kafedralar': kafedralar, 'turi': turlar, 'ish_muallifi':ish_muallifi })
def tahrirlash_ilmiy(request, i_id, t_id, user_id):
    foydalanuvchi=Foydalanuvchilar.objects.get(id=user_id)

    if t_id == 1:
        model = ilmiy_a
        form_class = IlmiyForm
        
    else:
        model = oquvIshlari
        form_class = OquvForm

    ilmiy = get_object_or_404(model, id=i_id)

    if request.method == "POST":
        form = form_class(request.POST, request.FILES, instance=ilmiy)
        if form.is_valid():
            form.save()
         
            if int(t_id) == 1:
                return render(request, 'app/ilmiy_ishlar.html', {
                    'title':'Oquv Ishlari',
                    'message':'Your oquv_ishlari page.',
                    'year':datetime.now().year,
                    'maqola':ilmiy_a.objects.filter(muallif_id=foydalanuvchi.id),
                    'foydalanuvchi':foydalanuvchi})
            else:
                return render(request, 'app/o`quv_ishlari.html', {
                                'title':'Oquv Ishlari',
                                'message':'Your oquv_ishlari page.',
                                'year':datetime.now().year,
                                'maqola':oquvIshlari.objects.filter(muallif_id=foydalanuvchi.id),
                                'foydalanuvchi':foydalanuvchi})

    else:
        form = form_class(instance=ilmiy)

    return render(request, 'app/tahrirlash_A.html', {
        'form': form,
        'ilmiy': ilmiy,
        't_id': t_id,
        'foydalanuvchi':foydalanuvchi,
    })

def profile2(request, user_id):
    assert isinstance(request, HttpRequest)
    foydalanuvchi=Foydalanuvchilar.objects.get(id=user_id)
    maqolalar_soni=0
    scopuslar_soni=0
    oquv_soni=0
    ilmiy_soni=0
    for muallif in Foydalanuvchilar.objects.filter(kafedra = foydalanuvchi.kafedra):
        maqolalar_soni+=ilmiy.objects.filter(muallif_id=muallif.id, turi='maqola').count()
        scopuslar_soni+=ilmiy.objects.filter(muallif_id=muallif.id, turi='scopus').count()
        oquv_soni+= oquvIshlari.objects.filter(muallif_id=muallif.id).count()
        ilmiy_soni+= ilmiy.objects.filter(muallif_id=muallif.id).count()
    jami=oquv_soni+ilmiy_soni
    return render(
        request,
        'app/profil2.html',
        {
            'foydalanuvchi':foydalanuvchi,
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'maqolalar_soni':maqolalar_soni,
            'scopuslar_soni':scopuslar_soni,
            'oquv_soni':oquv_soni,
            'jami':jami,
        }
    )
def profile3(request, user_id):
    assert isinstance(request, HttpRequest)
    foydalanuvchi=Foydalanuvchilar.objects.get(id=user_id)
    maqolalar_soni=0
    scopuslar_soni=0
    oquv_soni=0
    ilmiy_soni=0
    for kafedra_f in Kafedralar.objects.filter(fakultet=foydalanuvchi.fakulteti):
        for muallif in Foydalanuvchilar.objects.filter(kafedra=kafedra_f):
            maqolalar_soni+=ilmiy.objects.filter(muallif_id=muallif.id, turi='maqola').count()
            scopuslar_soni+=ilmiy.objects.filter(muallif_id=muallif.id, turi='scopus').count()
            oquv_soni+= oquvIshlari.objects.filter(muallif_id=muallif.id).count()
            ilmiy_soni+= ilmiy.objects.filter(muallif_id=muallif.id).count()
    jami=oquv_soni+ilmiy_soni
    return render(
        request,
        'app/profil3.html',
        {
            'foydalanuvchi':foydalanuvchi,
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'maqolalar_soni':maqolalar_soni,
            'scopuslar_soni':scopuslar_soni,
            'oquv_soni':oquv_soni,
            'jami':jami,
        }
    )
def ilmiy_ishlari2(request, user_id):
    """Renders the oquv_ishlari page."""
    assert isinstance(request, HttpRequest)
    
    foydalanuvchi = Foydalanuvchilar.objects.get(id=user_id)
    maqolalar=[]
    turi=ilmiy.objects.values_list('turi', flat=True).distinct()
    ish_muallifiy= []
    ish_muallifi = []

    
    for muallif in Foydalanuvchilar.objects.filter(kafedra = foydalanuvchi.kafedra):

        maqolalar+=ilmiy.objects.filter(muallif_id=muallif.id)
        ish_muallifiy += ilmiy.objects.filter(muallif_id=muallif.id).values_list('ish_mualliflari', flat=True).distinct()
    for qator in ish_muallifiy:
        if qator: 
            ish_muallifi.extend([m.strip() for m in qator.split(',')])
            ish_muallifi=list(set(ish_muallifi))
    return render(
        request,
        'app/ilmiy_ishlar2.html',
        {
            'title':'Ilmiy Ishlari',
            'message':'Your ilmiy_ishlari page.',
            'year':datetime.now().year,
            'maqola':maqolalar,
            'foydalanuvchi': foydalanuvchi,
            'turi': turi,
            'ish_muallifi': ish_muallifi
        }
    )
def ilmiy_ishlari3(request, user_id):
    assert isinstance(request, HttpRequest)
    foydalanuvchi = Foydalanuvchilar.objects.get(id=user_id)
    kafedralar = Kafedralar.objects.filter(fakultet = foydalanuvchi.fakulteti)
    turi=ilmiy.objects.values_list('turi', flat=True).distinct()
    ish_muallifiy= []
    ish_muallifi = []

    
    maqolalar=[]
    for kafedra_1 in Kafedralar.objects.filter(fakultet=foydalanuvchi.fakulteti):
        for muallif in Foydalanuvchilar.objects.filter(kafedra = kafedra_1):
            maqolalar+=ilmiy.objects.filter(muallif_id=muallif.id)
            ish_muallifiy+=ilmiy.objects.filter(muallif_id=muallif.id).values_list('ish_mualliflari', flat=True).distinct()
    for qator in ish_muallifiy:
        if qator: 
            ish_muallifi.extend([m.strip() for m in qator.split(',')])
            ish_muallifi=list(set(ish_muallifi))
    return render(
        request,
        'app/ilmiy_ishlar3.html',
        {
            'title':'Ilmiy Ishlari',
            'message':'Your ilmiy_ishlari page.',
            'year':datetime.now().year,
            'maqola':maqolalar,
            'foydalanuvchi': foydalanuvchi,
            'kafedralar': kafedralar,
            'turi': turi,
            'ish_muallifi': ish_muallifi

        }
    )
def oquv_ishlari2(request, user_id):
    """Renders the oquv_ishlari page."""
    assert isinstance(request, HttpRequest)
    foydalanuvchi = Foydalanuvchilar.objects.get(id=user_id)
    maqolalar=[]
    turi=oquvIshlari.objects.values_list('turi', flat=True).distinct()
    ish_muallifiy= []
    ish_muallifi = []
    
    for muallif in Foydalanuvchilar.objects.filter(kafedra = foydalanuvchi.kafedra):
        maqolalar+=oquvIshlari.objects.filter(muallif_id=muallif.id)
        ish_muallifiy += oquvIshlari.objects.filter(muallif_id=muallif.id).values_list('ish_mualliflari', flat=True).distinct()
    for qator in ish_muallifiy:
        if qator: 
            ish_muallifi.extend([m.strip() for m in qator.split(',')])
            ish_muallifi=list(set(ish_muallifi))
    return render(
        request,
        'app/o`quv_ishlari2.html',
        {
            'title':'Oquv Ishlari',
            'message':'Your oquv_ishlari page.',
            'year':datetime.now().year,
            'maqola':maqolalar,
            'foydalanuvchi': foydalanuvchi,
            'turi': turi,
            'ish_muallifi': ish_muallifi
        }
    )
def oquv_ishlari3(request,user_id):
    assert isinstance(request, HttpRequest)
    foydalanuvchi = Foydalanuvchilar.objects.get(id=user_id)
    kafedralar = Kafedralar.objects.filter(fakultet = foydalanuvchi.fakulteti)
    maqolalar=[]
    turi=oquvIshlari.objects.values_list('turi', flat=True).distinct()
    ish_muallifiy= []
    ish_muallifi = []
    
    for kafedra_1 in Kafedralar.objects.filter(fakultet=foydalanuvchi.fakulteti):
        for muallif in Foydalanuvchilar.objects.filter(kafedra = kafedra_1):
            maqolalar+=oquvIshlari.objects.filter(muallif_id=muallif.id)
            ish_muallifiy +=oquvIshlari.objects.filter(muallif_id=muallif.id).values_list('ish_mualliflari', flat=True).distinct()
    for qator in ish_muallifiy:
        if qator: 
            ish_muallifi.extend([m.strip() for m in qator.split(',')])
            ish_muallifi=list(set(ish_muallifi))
    return render(
        request,
        'app/o`quv_ishlari3.html',
        {
            'title':'Ilmiy Ishlari',
            'message':'Your ilmiy_ishlari page.',
            'year':datetime.now().year,
            'maqola':maqolalar,
            'foydalanuvchi': foydalanuvchi,
            'kafedralar': kafedralar,
            'turi': turi,
            'ish_muallifi': ish_muallifi

        }
    )

def logout(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/login.html'
    )


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import base64, json, os, io, zipfile
from datetime import datetime

@csrf_exempt
def download_zip(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    try:
        data = json.loads(request.body.decode())
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    excel_base64 = data.get("excel")
    files = data.get("files", [])

    if not excel_base64:
        return JsonResponse({"error": "Excel data missing!"}, status=400)

    # Agar base64 stringda data URI bo'lsa
    if "," in excel_base64:
        excel_base64 = excel_base64.split(",", 1)[1]

    try:
        excel_bytes = base64.b64decode(excel_base64)
    except Exception:
        return JsonResponse({"error": "Invalid base64 data"}, status=400)

    # ZIP yaratish
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
        # Excel faylni qo'shish
        zipf.writestr("jadval.xlsx", excel_bytes)

        # Jadvaldagi fayllar
        for i, f in enumerate(files, start=1):  
            if isinstance(f, str):
                rel = os.path.normpath(f).lstrip("/\\")
                basename = os.path.basename(rel)
            else:
                rel = os.path.normpath(f.get('path', '')).lstrip("/\\")
                prefix = str(i)  # loop indeksi prefix sifatida ishlatiladi
                basename = f"{prefix}_{os.path.basename(rel)}" if prefix else os.path.basename(rel)

            full_path = os.path.join(settings.MEDIA_ROOT, rel)

            # Xavfsizlik: MEDIA_ROOT ichidan chiqmasligi
            if not os.path.abspath(full_path).startswith(os.path.abspath(settings.MEDIA_ROOT)):
                continue

            if os.path.exists(full_path):
                zipf.write(full_path, basename)


    zip_buffer.seek(0)

    # Sana bilan ZIP fayl nomi
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"jadval_va_fayllar_{date_str}.zip"

    response = HttpResponse(zip_buffer.getvalue(), content_type="application/zip")
    response["Content-Disposition"] = f'attachment; filename="{filename}"; filename*=UTF-8\'\'{filename}'

    return response 

def logout(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/login.html'
    )

