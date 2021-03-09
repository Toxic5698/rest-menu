import django_tables2 as tables
from .models import Order

class OrderTable(tables.Table):
    class Meta:
        model = Order
        template_name = 'django_tables2/bootstrap-responsive.html'
        #update = tables.Column('update')
        #delete = tables.Column('delete')
        fields = (
        'name', 'phone', 'email',
        'supper1', 'supper2', 'meal1', 'meal2', 'meal3', 'meal4',
        'pickup', 'pickup_time', 'note',
        #'update', 'delete'
        )
        attrs = {"class": "table table-hover"}
