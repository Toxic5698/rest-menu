from django_tables2.utils import A
import django_tables2 as tables
from .models import Order

class OrderTable(tables.Table):
    edit = tables.LinkColumn(
    'edit_order', text='Změnit', args=[A('pk')], verbose_name="Změnit",
    orderable=False,
    )
    delete = tables.LinkColumn(
    'delete', text='Smazat', args=[A('pk')], orderable=False,
    verbose_name="Smazat",
    )

    class Meta:
        model = Order
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = (
        'name', 'phone', 'email',
        'supper1', 'supper2', 'meal1', 'meal2', 'meal3', 'meal4',
        'pickup', 'pickup_time', 'note',
        )
        attrs = {"class": "table table-hover"}
