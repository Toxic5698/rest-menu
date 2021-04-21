from django.db import models


# Create your models here.
class Supper(models.Model):
    name = models.CharField(max_length=200, null=True)
    alergens = models.CharField(max_length=200, null=True)
    price = models.PositiveIntegerField(null=True, default=25)

    def __str__(self):
        return self.name


class Meal(models.Model):
    portion = models.IntegerField(null=True)
    name = models.CharField(max_length=200, null=True)
    alergens = models.CharField(max_length=200, null=True)
    price = models.PositiveIntegerField(null=True, default=110)

    def __str__(self):
        return self.name


class Desert(models.Model):
    name = models.CharField(max_length=200, null=True)
    alergens = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    """docstring for Menu."""

    supper1 = models.ForeignKey(
    Supper, related_name='supper1', null=True, on_delete=models.SET_NULL
    )
    supper1_portions = models.PositiveIntegerField(null=True)
    supper2 = models.ForeignKey(
    Supper, related_name='supper2', null=True, on_delete=models.SET_NULL
    )
    supper2_portions = models.PositiveIntegerField(null=True)
    meal1 = models.ForeignKey(
    Meal, related_name='meal1', null=True, on_delete=models.SET_NULL
    )
    meal1_portions = models.PositiveIntegerField(null=True)
    meal2 = models.ForeignKey(
    Meal, related_name='meal2', null=True, on_delete=models.SET_NULL
    )
    meal2_portions = models.PositiveIntegerField(null=True)
    meal3 = models.ForeignKey(
    Meal, related_name='meal3', null=True, on_delete=models.SET_NULL
    )
    meal3_portions = models.PositiveIntegerField(null=True)
    meal4 = models.ForeignKey(
    Meal, related_name='meal4', null=True, on_delete=models.SET_NULL
    )
    meal4_portions = models.PositiveIntegerField(null=True)
    desert = models.ForeignKey(Desert, null=True, on_delete=models.SET_NULL)
    day = models.CharField(max_length=1000, null=True, default='')
    info = models.TextField(max_length=2000, blank=True)


class Order(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name="Jméno")
    phone = models.PositiveIntegerField(null=True, verbose_name="Telefon")
    email = models.EmailField(
    max_length=254, blank=True, default=None, verbose_name="E-mail"
    )
    supper1 = models.PositiveIntegerField(
    null=True, blank=True, verbose_name="Polévka 1"
    )
    supper2 = models.PositiveIntegerField(
    null=True, blank=True, verbose_name="Polévka 2"
    )
    meal1 = models.PositiveIntegerField(
    null=True, blank=True, verbose_name="Hlavní jídlo 1"
    )
    meal2 = models.PositiveIntegerField(
    null=True, blank=True, verbose_name="Hlavní jídlo 2"
    )
    meal3 = models.PositiveIntegerField(
    null=True, blank=True, verbose_name="Hlavní jídlo 3"
    )
    meal4 = models.PositiveIntegerField(
    null=True, blank=True, verbose_name="Hlavní jídlo 4"
    )
    pickup = models.BooleanField(
    blank=True, default=False, verbose_name="S sebou"
    )
    pickup_time = models.CharField(
    max_length=200, default=False, blank=True,
    verbose_name="Čas vyzvednutí"
    )
    note = models.TextField(
    max_length=999, blank=True, default=None, null=True, verbose_name="Poznámka"
    )
    #price = models.PositiveIntegerField(null=True, default=None)


    def __str__(self):
        return self.name
