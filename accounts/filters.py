import django_filters
from django_filters import CharFilter, DateFilter
from .models import *

class OrderFilter(django_filters.FilterSet):
    name = CharFilter(field_name = 'name', lookup_expr = 'icontains')
    phone = CharFilter(field_name = 'phone', lookup_expr = 'icontains')
    note = CharFilter(field_name = 'note', lookup_expr = 'icontains')



    class Meta:
        model = Order
        fields = ['name','phone', 'note', 'pickup', 'pickup_time' ]
