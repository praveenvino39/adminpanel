from django.shortcuts import render
from Order.models import Order
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime
# Create your views here.


@api_view(http_method_names=['GET'])
def shipping_report(request):
    total_amt = 0
    local_count = 0
    regional_count = 0
    national_count = 0
    today = datetime.date.today()
    #getting local orders count
    local_orders = Order.objects.filter(shipping_mode = 'Local',date__year = today.year, date__month=today.month)
    for local_order in local_orders:
        local_count += 1
    total_amt += local_count*15

    #getting regional order count
    regional_orders = Order.objects.filter(shipping_mode = 'Regional',date__year = today.year, date__month=today.month)
    for regional_order in regional_orders:
        regional_count += 1
    total_amt += regional_count * 30

    #getting national order count
    national_orders = Order.objects.filter(shipping_mode = 'National',date__year = today.year, date__month=today.month)
    for national_order in national_orders:
        national_count +=1
    total_amt += national_count * 50
    data = {
        'description': 'Shipping Amount for the month - {}/{}'.format(today.month, today.year),
        'count':{
            'local': local_count,
            'regional': regional_count,
            'national': national_count
        },
        'amount':{
            'local_amount': local_count * 15,
            'regional_amount': regional_count * 30,
            'national_amount': national_count * 50
        },
        'total_amount': total_amt
    }
    return Response(data, status = None)


@api_view(http_method_names=['GET'])
def petrol_report(request):
    order_count = 0
    today = datetime.date.today()
    orders= Order.objects.filter(date__year = today.year, date__month = today.month)
    for order in orders:
        order_count += 1
    data = {
        'description': 'Petrol Amount for the month - {}/{}'.format(today.month, today.year),
        'total_count': order_count,
        'petrol_amount': order_count * 5
    }
    return Response(data, status = None)


@api_view(http_method_names=['GET'])
def envelop_report(request):
    order_count = 0
    today = datetime.date.today()
    orders = Order.objects.filter(date__year = today.year, date__month = today.month)
    for order in orders:
        if order.shipping_mode != 'Self':
            order_count += 1
    data = {
        'description': 'Envelope Amount for the month - {}/{}'.format(today.month, today.year),
        'total_count': order_count,
        'enveloper_amount': order_count * 5
    }
    return Response(data, status = None)


@api_view(http_method_names=['GET'])
def case_report(request):
    profit = 0
    order_count = 0
    today = datetime.date.today()
    orders = Order.objects.filter(date__year=today.year, date__month=today.month)
    for order in orders:
        if order.shipping_mode == 'Local':
            profit += order.collected_price - (order.base_price + 15 + 5 + 5)
        elif order.shipping_mode == 'Regional':
            profit += order.collected_price - (order.base_price + 30 + 5 + 5)
        elif order.shipping_mode == 'National':
            profit += order.collected_price - (order.base_price + 50 + 5 + 5)
        elif order.shipping_mode == 'Self':
            profit += order.collected_price - (order.base_price + 5)
    orders = Order.objects.filter(date__year=today.year, date__month=today.month, is_refered = True)
    for order in orders:
        order_count += 1
    refer = order_count * 25
    data = {
        'description': 'Case Amount for the month - {}/{}'.format(today.month, today.year),
        'profit': profit - refer
    }
    return Response(data, status = None)


@api_view(http_method_names=['GET'])
def refered_report(request):
    order_count = 0
    today = datetime.date.today()
    orders = Order.objects.filter(date__year=today.year, date__month=today.month, is_refered = True)
    for order in orders:
        order_count += 1
    data = {
        'description': 'Referal Amount for the month - {}/{}'.format(today.month, today.year),
        'order_count': order_count,
        'amount': order_count * 25
    }
    return Response(data, status=None)


@api_view(http_method_names=['GET'])
def production_report(request):
    order_count = 0
    total_amount = 0
    today = datetime.date.today()
    orders = Order.objects.filter(date__year=today.year, date__month=today.month)
    for order in orders:
        order_count += 1
        total_amount += order.base_price
    data = {
        'description': 'Production Amount for the month - {}/{}'.format(today.month, today.year),
        'order_count': order_count,
        'amount': total_amount
    }
    return Response(data, status=None)
