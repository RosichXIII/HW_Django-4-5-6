from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta
from app_6.models import *
from .forms import *
import logging

logger = logging.getLogger(__name__)

def index_extend_base(request):
    return render(request, 'app_6/index.html')

def all_orders(request):
    order = Order.objects.all()
    return HttpResponse(order)

def order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order_id = Order.objects.get(pk=order_id).pk
    date_order = Order.objects.get(pk=order_id).date_order
    customer = Order.objects.get(pk=order_id).customer.name
    price_total_order = Order.objects.get(pk=order_id).price_total_order
    products = Order.objects.get(pk=order_id).products.all()

    return render(
        request, 'app_6/order.html', {
            'order': order,
            'order_id': order_id,
            'date_order': date_order,
            'customer': customer,
            'products': products,
            'price_total_order': price_total_order,
        })

def customer_orders(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer)
    
    return render(
        request, 'app_6/customer_orders.html',
        {
            'customer': customer,
            'orders': orders
        }
    )

def customer_all_products(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    all_orders = Order.objects.filter(customer=customer)

    return render(
        request, 'app_6/customer_all_products.html',
        {
            'customer': customer,
            'all_orders': all_orders,
        }
    )

def orders_order_by(request, customer_id, count_day):
    customer = get_object_or_404(Customer, pk=customer_id)
    all_orders = Order.objects.filter(customer=customer)
    date_now = timezone.now()
    start_date = date_now - timedelta(days=count_day)
    list_filter_orders = []
    
    for order in all_orders:
        if start_date <= order.date_order:
            list_filter_orders.append(order)
            
    return render(
        request,
        'app_6/orders_order_by.html',
        {
            'count_day': count_day,
            'customer': customer,
            'list_filter_orders': list_filter_orders,
        }
    )

def editor_product(request, product_id):
    
    if request.method == 'POST':
        form = EditorProduct(request.POST)
        
        if form.is_valid():
            product = Product.objects.get(pk=product_id)
            product.name_product = form.cleaned_data['name_product']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.count_product = form.cleaned_data['count_product']
            product.save()
    else:
        form = EditorProduct()
    
    return render(request, 'app_6/editor_product.html', {'form': form})

def add_product(request):
    
    if request.method == 'POST':
        form = AddProduct(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EditorProduct()

    return render(request, 'app_6/editor_product.html', {'form': form})

def del_product(request):
    
    if request.method == 'POST':
        form = DelProduct(request.POST)
        
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            Product.objects.filter(pk=product_id).delete()
            
    form = DelProduct()
    
    return render(request, 'app_6/del_product.html', {'form': form})

def product_with_img(request):
    
    if request.method == 'POST':
        form = ProductWithImgForm(request.POST, request.FILES)
        
        if form.is_valid():
            name_product = form.cleaned_data['name_product']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            count_product = form.cleaned_data['count_product']
            product_img = form.cleaned_data['product_img']
            fs = FileSystemStorage()
            filename = fs.save(product_img.name, product_img)
            # file_url = fs.url(filename)  путь к файлу
            product = ProductImg(name_product=name_product,
                                 description=description,
                                 price=price,
                                 count_product=count_product,
                                 product_img=filename)
            product.save()
    else:
        form = ProductWithImgForm()
    
    return render(request, 'app_6/product_with_img.html', {'form': form})

def print_all_product_img(request):
    all_product = ProductImg.objects.all()
    return render(request, 'app_6/print_all_product_img.html',
                  {'all_product': all_product})

class AddMetaProductImg(CreateView):
    model = MetaProductImg
    form_class = FormMetaProductImg
    template_name = 'app_6/add_meta_product_img.html'
    success_url = 'add_meta_product_img'

class ShowMetaProductImg(CreateView):
    model = MetaProductImg
    form_class = FormMetaProductImg
    extra_context = {'imgs': MetaProductImg.objects.all()}
    template_name = 'app_6/print_meta_product_img.html'