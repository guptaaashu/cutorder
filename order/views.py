from django.shortcuts import render
from .models import Order,lay
from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .forms import OrderForm, LayForm
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
            return redirect('red',pk=new.pk)
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
    return render(request, 'lay_detail.html', {'data': u,'lay': oay})


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
    return render(request, 'lay_detail.html', {'data': u,'lay': oay})

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
    return render(request, 'lay_detail.html', {'data': u,'lay': oay})
