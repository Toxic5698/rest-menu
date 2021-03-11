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
    PICKUP_TIME =(
    ('10:30', '10:30'),
    ('11:00', '11:00'),
    ('11:30', '11:30'),
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    )

    name = models.CharField(max_length=200, null=True)
    phone = models.PositiveIntegerField(null=True)
    email = models.EmailField(max_length=254, blank=True, default=None)
<<<<<<< HEAD
    supper1 = models.PositiveIntegerField(null=True, blank=True)
    supper2 = models.PositiveIntegerField(null=True, blank=True)
    meal1 = models.PositiveIntegerField(null=True, blank=True)
    meal2 = models.PositiveIntegerField(null=True, blank=True)
    meal3 = models.PositiveIntegerField(null=True, blank=True)
    meal4 = models.PositiveIntegerField(null=True, blank=True)
=======
    supper1 = models.PositiveIntegerField(null=True, blank=True, default=0)
    supper2 = models.PositiveIntegerField(null=True, blank=True, default=0)
    meal1 = models.PositiveIntegerField(null=True, blank=True, default=0)
    meal2 = models.PositiveIntegerField(null=True, blank=True, default=0)
    meal3 = models.PositiveIntegerField(null=True, blank=True, default=0)
    meal4 = models.PositiveIntegerField(null=True, blank=True, default=0)
>>>>>>> main
    pickup = models.BooleanField(blank=True, default=False)
    pickup_time = models.CharField(
    max_length=200, default=False, blank=True, choices=PICKUP_TIME
    )
    note = models.TextField(max_length=999, blank=True, default=None, null=True)
    #price = models.PositiveIntegerField(null=True, default=None)


    def __str__(self):
        return self.name
