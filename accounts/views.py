from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Sum

from django.views.generic import ListView

from django_tables2 import RequestConfig

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from datetime import date

from .models import *
from .forms import *
from .tables import OrderTable
from .filters import OrderFilter


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
                request, f'Nesprávný uživatel nebo heslo, zkuste znovu.'
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
            messages.success(request, f'Menu změněno!')
            return redirect('/')

    formSupper = EditSupperForm()
    if request.method == 'POST' and 'AddSupper' in request.POST:
        formSupper = EditSupperForm(request.POST)
        if formSupper.is_valid():
            formSupper.save()
            messages.success(request, f'Polívka přidána!')

    formMeal = EditMealForm()
    if request.method == 'POST' and 'AddMeal' in request.POST:
        formMeal = EditMealForm(request.POST)
        if formMeal.is_valid():
            formMeal.save()
            messages.success(request, f'Hlavní jídlo přidáno!')

    formDesert = EditDesertForm()
    if request.method == 'POST' and 'AddDesert' in request.POST:
        formDesert = EditDesertForm(request.POST)
        if formDesert.is_valid():
            formDesert.save()
            messages.success(request, f'Desert přidán!')

    supper = Supper.objects.all().order_by('name')
    meal = Meal.objects.all().order_by('name')
    desert = Desert.objects.all().order_by('name')

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
            messages.success(request, f'Objednávka dokončena!')
            #return redirect('/')


    counting_portions1 = [
    'supper1', 'supper2', 'meal1', 'meal2', 'meal3', 'meal4'
    ]
    counting_portions2 = {}
    for i in counting_portions1:
        counting = Order.objects.aggregate(Sum(i))
        counting_portions2.update(counting)


    context = {'form': form, 'menu': menu, 'c_p': counting_portions2,}


    return render(request, 'accounts/order_form.html', context)


class FilteredOrderListView(LoginRequiredMixin, SingleTableMixin, FilterView):
    login_url = '/login/'
    table_class = OrderTable
    model = Order
    template_name = "accounts/orders.html"

    filterset_class = OrderFilter

    def get_context_data(self, **kwargs):
        context = super(FilteredOrderListView, self).get_context_data(**kwargs)

        counting_portions1 = [
        'supper1', 'supper2', 'meal1', 'meal2', 'meal3', 'meal4'
        ]
        counting_portions2 = {}
        for i in counting_portions1:
            counting = Order.objects.aggregate(Sum(i))
            counting_portions2.update(counting)

        context.update(
            {
                "menu": Menu.objects.last(),
                "total": Order.objects.all().count(),
                "c_p": counting_portions2,
            }
        )
        return context


@login_required(login_url='login')
def editOrder(request, pk):
    menu = Menu.objects.last()

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, f'Objednávka upravena!')
            return redirect('/orders/')

    context = {
    'menu': menu,
    'form': form,
    'order': order,
    }
    return render(request, 'accounts/edit_order.html', context)


@login_required(login_url='login')
def deleteOrder(request, pk):
    menu = Menu.objects.last()
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        messages.success(request, f'Objednávka smazána!')
        return redirect('/orders/')

    context = {'item': order, 'menu': menu}
    return render(request, 'accounts/delete.html', context)

@login_required(login_url='login')
def deleteOrders(request):
    menu = Menu.objects.last()
    orders = Order.objects.all()
    if request.method == 'POST':
        orders.delete()
        messages.success(request, f'Všechny objednávky smazány!')
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
            messages.success(request, f'Polévka upravena!')
            return redirect('/edit_menu/1')

    context = {
    'menu': menu,
    'formSupper': formSupper,
    'supper': supper,
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
            messages.success(request, f'Hlavní jídlo upraveno!')
            return redirect('/edit_menu/1')

    context = {
    'menu': menu,
    'formMeal': formMeal,
    'meal': meal,
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
            messages.success(request, f'Desert upraven!')
            return redirect('/edit_menu/1')

    context = {
    'menu': menu,
    'formDesert': formDesert,
    'desert': desert,
    }
    return render(request, 'accounts/edit_desert.html', context)


@login_required(login_url='login')
def printMenu(request):
    menu = Menu.objects.last()

    context = {'menu': menu}

    return render(request, 'accounts/print_menu.html', context)
