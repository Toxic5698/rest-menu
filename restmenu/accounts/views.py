from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.db.models import Sum

from django.views.generic import ListView

from django_tables2 import RequestConfig

from datetime import date

from .models import *
from .forms import *
from .tables import OrderTable


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(
                request, f'Wrong user or password, please try again.'
                )

        context={}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    menu = Menu.objects.last()

    orders = Order.objects.all()
    total = orders.count()

    counting_portions1 = [
    'supper1', 'supper2', 'meal1', 'meal2', 'meal3', 'meal4'
    ]
    counting_portions2 = {}
    for i in counting_portions1:
        counting = Order.objects.aggregate(Sum(i))
        counting_portions2.update(counting)

    context = {
    'menu': menu,
    'orders': orders,
    'total': total,
    'c_p': counting_portions2,}

    return render(request, 'accounts/dashboard.html', context)


def status(request):
    return render(request, 'accounts/status.html')


def menu(request):
    return render(request, 'accounts/menu.html')


@login_required(login_url='login')
def editMenu(request, pk):

    menu = Menu.objects.get(id=pk)
    formMenu = MenuForm(instance=menu)
    if request.method == 'POST' and 'EditMenu' in request.POST:
        formMenu = MenuForm(request.POST, instance=menu)
        if formMenu.is_valid():
            formMenu.save()
            messages.success(request, f'Menu edited')
            return redirect('/')

    formSupper = EditSupperForm()
    if request.method == 'POST' and 'AddSupper' in request.POST:
        formSupper = EditSupperForm(request.POST)
        if formSupper.is_valid():
            formSupper.save()
            messages.success(request, f'Supper added')

    formMeal = EditMealForm()
    if request.method == 'POST' and 'AddMeal' in request.POST:
        formMeal = EditMealForm(request.POST)
        if formMeal.is_valid():
            formMeal.save()
            messages.success(request, f'Meal added')

    formDesert = EditDesertForm()
    if request.method == 'POST' and 'AddDesert' in request.POST:
        formDesert = EditDesertForm(request.POST)
        if formDesert.is_valid():
            formDesert.save()
            messages.success(request, f'Desert added')

    supper = Supper.objects.all()
    meal = Meal.objects.all()
    desert = Desert.objects.all()

    context = {
    'menu': menu,
    'formMenu': formMenu,
    'formSupper': formSupper,
    'formMeal': formMeal,
    'formDesert': formDesert,
    'supper': supper,
    'meal': meal,
    'desert': desert,
    }

    return render(request, 'accounts/menu_form.html', context)


def makeOrder(request):
    menu = Menu.objects.last()
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Order complete')
            return redirect('/')


    counting_portions1 = [
    'supper1', 'supper2', 'meal1', 'meal2', 'meal3', 'meal4'
    ]
    counting_portions2 = {}
    for i in counting_portions1:
        counting = Order.objects.aggregate(Sum(i))
        counting_portions2.update(counting)


    context = {'form': form, 'menu': menu, 'c_p': counting_portions2,}


    return render(request, 'accounts/order_form.html', context)


class OrderListView(ListView):
    model = Order
    table_class = OrderTable
    template_name = 'accounts/order_table.html'


@login_required(login_url='login')
def orders(request):
    orders = Order.objects.all()
    menu = Menu.objects.last()
    total = orders.count()

    counting_portions1 = [
    'supper1', 'supper2', 'meal1', 'meal2', 'meal3', 'meal4'
    ]
    counting_portions2 = {}
    for i in counting_portions1:
        counting = Order.objects.aggregate(Sum(i))
        counting_portions2.update(counting)

    table = OrderTable(Order.objects.all())
    RequestConfig(request).configure(table)

    context = {
    'orders': orders,
    'total': total,
    'menu': menu,
    'c_p': counting_portions2,
    'table': table
    }
    return render(request, 'accounts/orders.html', context)


@login_required(login_url='login')
def editOrder(request, pk):
    menu = Menu.objects.last()

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, f'Order edited')
            return redirect('/orders/')

    context = {
    'menu': menu,
    'form': form,
    }
    return render(request, 'accounts/edit_order.html', context)


@login_required(login_url='login')
def deleteOrder(request, pk):
    menu = Menu.objects.last()
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/orders/')

    context = {'item': order, 'menu': menu}
    return render(request, 'accounts/delete.html', context)

@login_required(login_url='login')
def deleteOrders(request):
    menu = Menu.objects.last()
    orders = Order.objects.all()
    if request.method == 'POST':
        orders.delete()
        return redirect('/orders/')

    context = {'orders': orders, 'menu': menu}
    return render(request, 'accounts/delete_all_orders.html', context)


@login_required(login_url='login')
def editSupper(request, pk):
    menu = Menu.objects.last()

    supper = Supper.objects.get(id=pk)
    formSupper = EditSupperForm(instance=supper)
    if request.method == 'POST' and 'AddSupper' in request.POST:
        formSupper = EditSupperForm(request.POST, instance=supper)
        if formSupper.is_valid():
            formSupper.save()
            messages.success(request, f'Supper edited')
            return redirect('/edit_menu/1')

    context = {
    'menu': menu,
    'formSupper': formSupper,
    }
    return render(request, 'accounts/edit_supper.html', context)


@login_required(login_url='login')
def editMeal(request, pk):
    menu = Menu.objects.last()

    meal = Meal.objects.get(id=pk)
    formMeal = EditMealForm(instance=meal)
    if request.method == 'POST' and 'AddMeal' in request.POST:
        formMeal = EditMealForm(request.POST, instance=meal)
        if formMeal.is_valid():
            formMeal.save()
            messages.success(request, f'Meal edited')
            return redirect('/edit_menu/1')

    context = {
    'menu': menu,
    'formMeal': formMeal,
    }
    return render(request, 'accounts/edit_meal.html', context)


@login_required(login_url='login')
def editDesert(request, pk):
    menu = Menu.objects.last()

    desert = Desert.objects.get(id=pk)
    formDesert = EditDesertForm(instance=desert)
    if request.method == 'POST' and 'AddDesert' in request.POST:
        formDesert = EditDesertForm(request.POST, instance=desert)
        if formDesert.is_valid():
            formDesert.save()
            messages.success(request, f'Desert edited')
            return redirect('/edit_menu/1')

    context = {
    'menu': menu,
    'formDesert': formDesert,
    }
    return render(request, 'accounts/edit_desert.html', context)
