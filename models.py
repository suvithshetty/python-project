from django.db import models

class Dsu(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stocks = models.IntegerField()
    image = models.CharField(max_length=2083)

    def __str__(self):
        return self.name

# Cart Model
class CartItem(models.Model):
    product = models.ForeignKey(Dsu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
