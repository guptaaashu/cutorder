from django.shortcuts import render
from .models import Order,lay, Roll
from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .forms import OrderForm, LayForm, RollForm
from django.http import HttpResponse
# Create your views here.
def detail(request):
    Orders= Order.objects.all()
    return render(request, 'detail_view.html', {'Orders': Orders})

def detail_view(request,pk):
    order=get_object_or_404(Order, pk=pk)
    return render(request, 'detailed.html', {'order': order})


def orde(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            new=form.save()
            return redirect('detail',pk=new.pk)
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form})


def laye(request):
    if request.method == 'POST':
        form = LayForm(request.POST)
        print(form)
        if form.is_valid():
            new=form.save()
            return redirect('red2',pk=new.pk)
    else:
        form = LayForm()
    return render(request, 'lay.html', {'form': form})

def lay_detail(request):
    lays= lay.objects.all()
    return render(request, 'lay_detail_view.html', {'Lays': lays})


def lay_detail_view_red(request,pk):
    oay=get_object_or_404(lay, pk=pk)
    def check(bal):
        for i in bal:
            if(i[1]!=0):
                return True
        return False
    def getlay(l,red,t,y,g):
        bal=[]
        for i in red:
            f=[]
            f.append(i[0])
            f.append(i[1])
            bal.append(f)
        while(check(red)):
            red.sort(reverse=True,key=lambda x:x[1])
            s=0
            i=0
            u=[]
            for i in range(3,-1,-1):
                if(red[i][1]!=0):
                    s=red[i][1]
                    break
            l.append(s)
            for j in range(0,i+1):
                u.append(red[j][0])
                red[j][1]=red[j][1]-s
            c=[]
            red.sort(key=lambda x:x[0])
            for i in bal:
                c.append(i[1])
            y.append(c)
            bal=[]
            d=[]
            for i in red:
                d.append(i[1])
                f=[]
                f.append(i[0])
                f.append(i[1])
                bal.append(f)
            t.append(d)
            u.sort()
            g.append(u)
        print(l)
        print(t)
        print(y)
        print(g)
    red=[[38,oay.Red38],[40,oay.Red40],[42,oay.Red42],[44,oay.Red44],[46,oay.Red46],[48,oay.Red48],[50,oay.Red50],[52,oay.Red52],[54,oay.Red54]]
    l=[]
    t=[]
    y=[]
    g=[]
    getlay(l,red,t,y,g)
    f=[]
    te=[]
    it=1
    for i in l:
        te.append(it)
        it=it+1
    u=zip(l,t,y,g,te)
    method=1
    color='red'
    return render(request, 'lay_detail.html', {'data': u,'lay': oay,'method':method,'color':color})


def lay_detail_view_blue(request,pk):
    oay=get_object_or_404(lay, pk=pk)
    def check(bal):
        for i in bal:
            if(i[1]!=0):
                return True
        return False
    def getlay(l,red,t,y,g):
        bal=[]
        for i in red:
            f=[]
            f.append(i[0])
            f.append(i[1])
            bal.append(f)
        while(check(red)):
            red.sort(reverse=True,key=lambda x:x[1])
            s=0
            i=0
            u=[]
            for i in range(3,-1,-1):
                if(red[i][1]!=0):
                    s=red[i][1]
                    break
            l.append(s)
            for j in range(0,i+1):
                u.append(red[j][0])
                red[j][1]=red[j][1]-s
            c=[]
            red.sort(key=lambda x:x[0])
            for i in bal:
                c.append(i[1])
            y.append(c)
            bal=[]
            d=[]
            for i in red:
                d.append(i[1])
                f=[]
                f.append(i[0])
                f.append(i[1])
                bal.append(f)
            t.append(d)
            u.sort()
            g.append(u)
        print(l)
        print(t)
        print(y)
        print(g)
    red=[[38,oay.Blue38],[40,oay.Blue40],[42,oay.Blue42],[44,oay.Blue44],[46,oay.Blue46],[48,oay.Blue48],[50,oay.Blue50],[52,oay.Blue52],[54,oay.Blue54]]
    l=[]
    t=[]
    y=[]
    g=[]
    getlay(l,red,t,y,g)
    f=[]
    te=[]
    it=1
    for i in l:
        te.append(it)
        it=it+1
    u=zip(l,t,y,g,te)
    method=1
    color='blue'
    return render(request, 'lay_detail.html', {'data': u,'lay': oay,'method':method,'color':color})

def lay_detail_view_yellow(request,pk):
    oay=get_object_or_404(lay, pk=pk)
    def check(bal):
        for i in bal:
            if(i[1]!=0):
                return True
        return False
    def getlay(l,red,t,y,g):
        bal=[]
        for i in red:
            f=[]
            f.append(i[0])
            f.append(i[1])
            bal.append(f)
        while(check(red)):
            red.sort(reverse=True,key=lambda x:x[1])
            s=0
            i=0
            u=[]
            for i in range(3,-1,-1):
                if(red[i][1]!=0):
                    s=red[i][1]
                    break
            l.append(s)
            for j in range(0,i+1):
                u.append(red[j][0])
                red[j][1]=red[j][1]-s
            c=[]
            red.sort(key=lambda x:x[0])
            for i in bal:
                c.append(i[1])
            y.append(c)
            bal=[]
            d=[]
            for i in red:
                d.append(i[1])
                f=[]
                f.append(i[0])
                f.append(i[1])
                bal.append(f)
            t.append(d)
            u.sort()
            g.append(u)
        print(l)
        print(t)
        print(y)
        print(g)
    red=[[38,oay.Yellow38],[40,oay.Yellow40],[42,oay.Yellow42],[44,oay.Yellow44],[46,oay.Yellow46],[48,oay.Yellow48],[50,oay.Yellow50],[52,oay.Yellow52],[54,oay.Yellow54]]
    l=[]
    t=[]
    y=[]
    g=[]
    getlay(l,red,t,y,g)
    f=[]
    te=[]
    it=1
    for i in l:
        te.append(it)
        it=it+1
    u=zip(l,t,y,g,te)
    method=1
    color='yellow'
    return render(request, 'lay_detail.html', {'data': u,'lay': oay,'method':method,'color':color})


def lay_detail_view_red1(request,pk):
    oay=get_object_or_404(lay, pk=pk)
    def check(bal):
        for i in bal:
            if(i[1]!=0):
                return True
        return False
    def getlay(l,red,t,y,g):
        bal=[]
        for i in red:
            f=[]
            f.append(i[0])
            f.append(i[1])
            bal.append(f)
        while(check(red)):
            red.sort(key=lambda x:x[1])
            s=0
            j=0
            tee=4
            u=[]
            for j in range(0,9):
                if(red[j][1]>0):
                    s=red[j][1]
                    red[j][1]=0
                    u.append(red[j][0])
                    tee=tee-1
                    break
            red.sort(key=lambda x:x[0])
            for i in range(0,9):
                if(red[i][1]%s==0):
                    while((tee>0) and (red[i][1])>0):
                        red[i][1]=red[i][1]-s
                        u.append(red[i][0])
                        tee=tee-1
            for i in range(0,9):
                if(red[i][1]>0 and tee>0):
                    red[i][1]=red[i][1]-s
                    u.append(red[i][0])
                    tee=tee-1
            l.append(s)
            c=[]
            red.sort(key=lambda x:x[0])
            for i in bal:
                c.append(i[1])
            y.append(c)
            bal=[]
            d=[]
            for i in red:
                d.append(i[1])
                f=[]
                f.append(i[0])
                f.append(i[1])
                bal.append(f)
            t.append(d)
            u.sort()
            g.append(u)
        print(l)
        print(t)
        print(y)
        print(g)
    red=[[38,oay.Red38],[40,oay.Red40],[42,oay.Red42],[44,oay.Red44],[46,oay.Red46],[48,oay.Red48],[50,oay.Red50],[52,oay.Red52],[54,oay.Red54]]
    l=[]
    t=[]
    y=[]
    g=[]
    getlay(l,red,t,y,g)
    f=[]
    te=[]
    it=1
    for i in l:
        te.append(it)
        it=it+1
    u=zip(l,t,y,g,te)
    method=2
    color='red'
    return render(request, 'lay_detail.html', {'data': u,'lay': oay,'method':method,'color':color})

def lay_detail_view_blue1(request,pk):
    oay=get_object_or_404(lay, pk=pk)
    def check(bal):
        for i in bal:
            if(i[1]!=0):
                return True
        return False
    def getlay(l,red,t,y,g):
        bal=[]
        for i in red:
            f=[]
            f.append(i[0])
            f.append(i[1])
            bal.append(f)
        while(check(red)):
            red.sort(key=lambda x:x[1])
            s=0
            j=0
            tee=4
            u=[]
            for j in range(0,9):
                if(red[j][1]>0):
                    s=red[j][1]
                    red[j][1]=0
                    u.append(red[j][0])
                    tee=tee-1
                    break
            red.sort(key=lambda x:x[0])
            for i in range(0,9):
                if(red[i][1]%s==0):
                    while((tee>0) and (red[i][1])>0):
                        red[i][1]=red[i][1]-s
                        u.append(red[i][0])
                        tee=tee-1
            for i in range(0,9):
                if(red[i][1]>0 and tee>0):
                    red[i][1]=red[i][1]-s
                    u.append(red[i][0])
                    tee=tee-1
            l.append(s)
            c=[]
            red.sort(key=lambda x:x[0])
            for i in bal:
                c.append(i[1])
            y.append(c)
            bal=[]
            d=[]
            for i in red:
                d.append(i[1])
                f=[]
                f.append(i[0])
                f.append(i[1])
                bal.append(f)
            t.append(d)
            u.sort()
            g.append(u)
        print(l)
        print(t)
        print(y)
        print(g)
    red=[[38,oay.Blue38],[40,oay.Blue40],[42,oay.Blue42],[44,oay.Blue44],[46,oay.Blue46],[48,oay.Blue48],[50,oay.Blue50],[52,oay.Blue52],[54,oay.Blue54]]
    l=[]
    t=[]
    y=[]
    g=[]
    getlay(l,red,t,y,g)
    f=[]
    te=[]
    it=1
    for i in l:
        te.append(it)
        it=it+1
    u=zip(l,t,y,g,te)
    method=2
    color='blue'
    return render(request, 'lay_detail.html', {'data': u,'lay': oay,'method':method,'color':color})

def lay_detail_view_yellow1(request,pk):
    oay=get_object_or_404(lay, pk=pk)
    def check(bal):
        for i in bal:
            if(i[1]!=0):
                return True
        return False
    def getlay(l,red,t,y,g):
        bal=[]
        for i in red:
            f=[]
            f.append(i[0])
            f.append(i[1])
            bal.append(f)
        while(check(red)):
            red.sort(key=lambda x:x[1])
            s=0
            j=0
            tee=4
            u=[]
            for j in range(0,9):
                if(red[j][1]>0):
                    s=red[j][1]
                    red[j][1]=0
                    u.append(red[j][0])
                    tee=tee-1
                    break
            red.sort(key=lambda x:x[0])
            for i in range(0,9):
                if(red[i][1]%s==0):
                    while((tee>0) and (red[i][1])>0):
                        red[i][1]=red[i][1]-s
                        u.append(red[i][0])
                        tee=tee-1
            for i in range(0,9):
                if(red[i][1]>0 and tee>0):
                    red[i][1]=red[i][1]-s
                    u.append(red[i][0])
                    tee=tee-1
            l.append(s)
            c=[]
            red.sort(key=lambda x:x[0])
            for i in bal:
                c.append(i[1])
            y.append(c)
            bal=[]
            d=[]
            for i in red:
                d.append(i[1])
                f=[]
                f.append(i[0])
                f.append(i[1])
                bal.append(f)
            t.append(d)
            u.sort()
            g.append(u)
        print(l)
        print(t)
        print(y)
        print(g)
    red=[[38,oay.Yellow38],[40,oay.Yellow40],[42,oay.Yellow42],[44,oay.Yellow44],[46,oay.Yellow46],[48,oay.Yellow48],[50,oay.Yellow50],[52,oay.Yellow52],[54,oay.Yellow54]]
    l=[]
    t=[]
    y=[]
    g=[]
    getlay(l,red,t,y,g)
    f=[]
    te=[]
    it=1
    for i in l:
        te.append(it)
        it=it+1
    u=zip(l,t,y,g,te)
    method=2
    color='yellow'
    return render(request, 'lay_detail.html', {'data': u,'lay': oay,'method':method,'color':color})


def lay_detail_view_red2(request,pk):
    oay=get_object_or_404(lay, pk=pk)
    def check(bal):
        for i in bal:
            if(i[1]!=0):
                return True
        return False
    def getlay(l,red,t,y,g):
        bal=[]
        for i in red:
            f=[]
            f.append(i[0])
            f.append(i[1])
            bal.append(f)
        while(check(red)):
            red.sort(key=lambda x:x[1])
            s=10
            j=0
            tee=4
            u=[]
            se=set()
            for j in range(0,9):
                if(red[j][1]>0):
                    se.add((red[j][1]))
            se= list(se)
            se.sort()
            leng=len(se)
            if(leng%2==0):
                uee=int(leng/2)
                print(uee)
                print(se[uee])
                if(se[uee]>se[uee-1]):
                    s=se[uee-1]
                else:
                    s=se[uee]
            else:
                uee=int(leng/2)
                s=se[uee]
            red.sort(key=lambda x:x[0])
            for i in range(0,9):
                if(red[i][1]%s==0):
                    while((tee>0) and (red[i][1])>0):
                        red[i][1]=red[i][1]-s
                        u.append(red[i][0])
                        tee=tee-1
            for i in range(0,9):
                if(red[i][1]>s and tee>0):
                    red[i][1]=red[i][1]-s
                    u.append(red[i][0])
                    tee=tee-1
            l.append(s)
            c=[]
            red.sort(key=lambda x:x[0])
            for i in bal:
                c.append(i[1])
            y.append(c)
            bal=[]
            d=[]
            for i in red:
                d.append(i[1])
                f=[]
                f.append(i[0])
                f.append(i[1])
                bal.append(f)
            t.append(d)
            u.sort()
            g.append(u)
        print(l)
        print(t)
        print(y)
        print(g)
    red=[[38,oay.Red38],[40,oay.Red40],[42,oay.Red42],[44,oay.Red44],[46,oay.Red46],[48,oay.Red48],[50,oay.Red50],[52,oay.Red52],[54,oay.Red54]]
    l=[]
    t=[]
    y=[]
    g=[]
    getlay(l,red,t,y,g)
    te=[]
    it=1
    for i in l:
        te.append(it)
        it=it+1
    u=zip(l,t,y,g,te)
    method=2
    color='red'
    return render(request, 'lay_detail.html', {'data': u,'lay': oay,'method':method,'color':color})

def lay_detail_view_blue2(request,pk):
    oay=get_object_or_404(lay, pk=pk)
    def check(bal):
        for i in bal:
            if(i[1]!=0):
                return True
        return False
    def getlay(l,red,t,y,g):
        bal=[]
        for i in red:
            f=[]
            f.append(i[0])
            f.append(i[1])
            bal.append(f)
        while(check(red)):
            red.sort(key=lambda x:x[1])
            s=10
            j=0
            tee=4
            u=[]
            se=set()
            for j in range(0,9):
                if(red[j][1]>0):
                    se.add((red[j][1]))
            se= list(se)
            se.sort()
            leng=len(se)
            if(leng%2==0):
                uee=int(leng/2)
                print(uee)
                print(se[uee])
                if(se[uee]>se[uee-1]):
                    s=se[uee-1]
                else:
                    s=se[uee]
            else:
                uee=int(leng/2)
                s=se[uee]
            red.sort(key=lambda x:x[0])
            for i in range(0,9):
                if(red[i][1]%s==0):
                    while((tee>0) and (red[i][1])>0):
                        red[i][1]=red[i][1]-s
                        u.append(red[i][0])
                        tee=tee-1
            for i in range(0,9):
                if(red[i][1]>s and tee>0):
                    red[i][1]=red[i][1]-s
                    u.append(red[i][0])
                    tee=tee-1
            l.append(s)
            c=[]
            red.sort(key=lambda x:x[0])
            for i in bal:
                c.append(i[1])
            y.append(c)
            bal=[]
            d=[]
            for i in red:
                d.append(i[1])
                f=[]
                f.append(i[0])
                f.append(i[1])
                bal.append(f)
            t.append(d)
            u.sort()
            g.append(u)
        print(l)
        print(t)
        print(y)
        print(g)
    red=[[38,oay.Blue38],[40,oay.Blue40],[42,oay.Blue42],[44,oay.Blue44],[46,oay.Blue46],[48,oay.Blue48],[50,oay.Blue50],[52,oay.Blue52],[54,oay.Blue54]]
    l=[]
    t=[]
    y=[]
    g=[]
    getlay(l,red,t,y,g)
    te=[]
    it=1
    for i in l:
        te.append(it)
        it=it+1
    u=zip(l,t,y,g,te)
    method=2
    color='red'
    return render(request, 'lay_detail.html', {'data': u,'lay': oay,'method':method,'color':color})


def lay_detail_view_yellow2(request,pk):
    oay=get_object_or_404(lay, pk=pk)
    def check(bal):
        for i in bal:
            if(i[1]!=0):
                return True
        return False
    def getlay(l,red,t,y,g):
        bal=[]
        for i in red:
            f=[]
            f.append(i[0])
            f.append(i[1])
            bal.append(f)
        while(check(red)):
            red.sort(key=lambda x:x[1])
            s=10
            j=0
            tee=4
            u=[]
            se=set()
            for j in range(0,9):
                if(red[j][1]>0):
                    se.add((red[j][1]))
            se= list(se)
            se.sort()
            leng=len(se)
            if(leng%2==0):
                uee=int(leng/2)
                print(uee)
                print(se[uee])
                if(se[uee]>se[uee-1]):
                    s=se[uee-1]
                else:
                    s=se[uee]
            else:
                uee=int(leng/2)
                s=se[uee]
            red.sort(key=lambda x:x[0])
            for i in range(0,9):
                if(red[i][1]%s==0):
                    while((tee>0) and (red[i][1])>0):
                        red[i][1]=red[i][1]-s
                        u.append(red[i][0])
                        tee=tee-1
            for i in range(0,9):
                if(red[i][1]>s and tee>0):
                    red[i][1]=red[i][1]-s
                    u.append(red[i][0])
                    tee=tee-1
            l.append(s)
            c=[]
            red.sort(key=lambda x:x[0])
            for i in bal:
                c.append(i[1])
            y.append(c)
            bal=[]
            d=[]
            for i in red:
                d.append(i[1])
                f=[]
                f.append(i[0])
                f.append(i[1])
                bal.append(f)
            t.append(d)
            u.sort()
            g.append(u)
        print(l)
        print(t)
        print(y)
        print(g)
    red=[[38,oay.Yellow38],[40,oay.Yellow40],[42,oay.Yellow42],[44,oay.Yellow44],[46,oay.Yellow46],[48,oay.Yellow48],[50,oay.Yellow50],[52,oay.Yellow52],[54,oay.Yellow54]]
    l=[]
    t=[]
    y=[]
    g=[]
    getlay(l,red,t,y,g)
    te=[]
    it=1
    for i in l:
        te.append(it)
        it=it+1
    u=zip(l,t,y,g,te)
    method=2
    color='red'
    return render(request, 'lay_detail.html', {'data': u,'lay': oay,'method':method,'color':color})


def roll_detail(request):
    Rolls= Roll.objects.all()
    return render(request, 'roll_detail_view.html', {'Rolls': Rolls})

def roll_detail_view(request,pk):
    roll=get_object_or_404(Roll, pk=pk)
    return render(request, 'roll_detailed.html', {'Roll': roll})


def roll(request):
    if request.method == 'POST':
        form = RollForm(request.POST)
        if form.is_valid():
            new=form.save()
            return redirect('roll_detail',pk=new.pk)
    else:
        form = RollForm()
    return render(request, 'roll.html', {'form': form})
