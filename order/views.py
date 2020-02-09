from django.shortcuts import render
from .models import Order
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .forms import OrderForm
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
            form.save()
            return HttpResponse('Order Succesfully Placed')
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form})
