from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=255) 
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=14, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', 
                                  related_name='products', 
                                  on_delete=models.SET_NULL, 
                                  null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey('Product',
                                 related_name='images',
                                 on_delete=models.SET_NULL,
                                 null=True)
    image = models.ImageField(upload_to='product/images')


class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField()
    role = models.CharField(max_length=128)
    products = models.ManyToManyField(Product, blank=True) # users_products => like

    def __str__(self):
        return self.username


class Order(models.Model):
    class PaymentChoices(models.IntegerChoices):
        ONE = 1, "Payme"
        TWO = 2, "Click"
        THREE = 3, "Online card"
        FOUR = 4, "Cash"
        FIVE = 5, "Corporate card"
        SIX = 6, "Installment payment"
    payment_method = models.PositiveSmallIntegerField(choices=PaymentChoices.choices, default=PaymentChoices.THREE)
    is_delivery = models.BooleanField()
    store_location = models.CharField()
    description = models.TextField()
    user = models.ForeignKey('user.User', 
                             related_name='orders',
                             on_delete=models.SET_NULL,
                             null=True)
    product = models.ForeignKey('Product',
                                related_name='orders',
                                on_delete=models.SET_NULL,
                                null=True)
    # promocode = models.TextField()
    def __str__(self):
        return f'{self.user} - {self.product}'
    

class Comment(models.Model):
    class RatingChoices(models.IntegerChoices):
        ONE = 1, "⭐"
        TWO = 2, "⭐⭐"
        THREE = 3, "⭐⭐⭐"
        FOUR = 4, "⭐⭐⭐⭐"
        FIVE = 5, "⭐⭐⭐⭐⭐"
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    rating = models.PositiveSmallIntegerField(choices=RatingChoices.choices, default = RatingChoices.FIVE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='comments',
        on_delete=models.SET_NULL,
        null=True
    )
    product = models.ForeignKey(
        'Product',
        related_name='comments',
        on_delete=models.SET_NULL,
        null=True
    )
    
    def __str__(self):
        return self.product.name
    
    




# Vaqt qolsa qilinadi:
# class Store(location, working hours, phone_number)
# Promocode(name, discount)