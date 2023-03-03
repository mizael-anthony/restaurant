from django.db import models




# Create your models here.


class Menu(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
        
    )

    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE
    )

    dispo = models.BooleanField(default=True, null=False)

    price = models.IntegerField(null=False)


    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        unique=True
    )

    def __str__(self) -> str:
        return self.name


class Client(models.Model):
    table = models.IntegerField(null=False, unique=True)


