from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Order, Menu, Supper, Meal, Desert


class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['pickup_time'].widget.attrs.update({
        'class': 'form-control',})

    class Meta:
        model = Order
        fields = '__all__'


class MenuForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        self.fields['supper1'].widget.attrs.update({
        'class': 'form-control'})
        self.fields['supper1_portions'].widget.attrs.update({
        'class': 'form-control'})
        self.fields['supper2'].widget.attrs.update({
        'class': 'form-control'})
        self.fields['supper2_portions'].widget.attrs.update({
        'class': 'form-control'})
        self.fields['meal1'].widget.attrs.update({
        'class': 'form-control'})
        self.fields['meal1_portions'].widget.attrs.update({
        'class': 'form-control'})
        self.fields['meal2'].widget.attrs.update({
        'class': 'form-control'})
        self.fields['meal2_portions'].widget.attrs.update({
        'class': 'form-control'})
        self.fields['meal3'].widget.attrs.update({
        'class': 'form-control'})
        self.fields['meal3_portions'].widget.attrs.update({
        'class': 'form-control'})
        self.fields['meal4'].widget.attrs.update({
        'class': 'form-control'})
        self.fields['meal4_portions'].widget.attrs.update({
        'class': 'form-control'})
        self.fields['desert'].widget.attrs.update({
        'class': 'form-control'})
        self.fields['info'].widget.attrs.update({
        'class': 'form-control h-25'})
        self.fields['day'].widget.attrs.update({
        'class': 'form-control'})

    class Meta:
        model = Menu
        fields = '__all__'


class EditSupperForm(ModelForm):
    class Meta:
        model = Supper
        fields = '__all__'


class EditMealForm(ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'


class EditDesertForm(ModelForm):
    class Meta:
        model = Desert
        fields = '__all__'
