from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.


class Customer(AbstractUser):
    username = models.CharField(unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length=10)
    is_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    forgot_password = models.CharField(max_length=100, null=True, blank=True)
    last_login_time = models.DateTimeField(null=True, blank=True)
    last_logout_time = models.DateTimeField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="products", null=True, blank=True)
    referral_code = models.CharField(max_length=100, null=True, unique=True)
    referral_amount = models.IntegerField(default=0)
    wallet_bal= models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default="")
    image = models.ImageField(upload_to="products")
    category_offer_description = models.CharField(max_length=100, null=True, blank=True)
    category_offer = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="products")
    product_offer = models.PositiveBigIntegerField(default=0, null=True)
    is_deleted = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def __str__(self):
        return self.product_name


class Slider(models.Model):
    DISCOUNT_DEAL = (
        ("HOT DEALS", "HOT DEALS"),
        ("New Arrivals", "New Arrivals"),
    )

    Image = models.ImageField(upload_to="media/slider_imgs")
    Discount_Deal = models.CharField(choices=DISCOUNT_DEAL, max_length=100)
    SALE = models.IntegerField()

    Discount = models.IntegerField()


