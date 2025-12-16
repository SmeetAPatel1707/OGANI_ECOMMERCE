from django.db import models
from .models import*
from django.db.models import Sum


class Department(models.Model):
    
    dept_name = models.CharField(max_length=100)
    dept_image = models.ImageField(upload_to='dept_image')
    
    def __str__(self):
        return self.dept_name
    
class Color_filter(models.Model):
    
    p_color = models.CharField(max_length=20)
    
    def __str__(self):
        return self.p_color
    
class Size_filter(models.Model):
    
    p_size = models.CharField(max_length=20)
    
    def __str__(self):
        return self.p_size
    
class User_Detail(models.Model):
    
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=8)
    c_password = models.CharField(max_length=8)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.f_name
    
    
class Product(models.Model):
    
    Department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    Color_filter = models.ForeignKey(Color_filter, on_delete=models.CASCADE, blank=True, null=True)
    Size_filter = models.ForeignKey(Size_filter, on_delete=models.CASCADE, blank=True, null=True)
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='Product Images')
    product_price = models.IntegerField()
    
    def __str__(self):
        return self.product_name
    
class Cart(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to="cart_images/")
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
        
    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.product_price 
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.product_name
    
    def get_cart_total():
        total = Cart.objects.aggregate(Sum('total_price'))['total_price__sum'] 
        return total
    
class Wishlist(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to="cart_images/")
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name
    
    
class Billingdetail(models.Model):
    
    user_id=models.ForeignKey(User_Detail,on_delete=models.CASCADE,blank=True,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    f_name=models.CharField(max_length=100,blank=True,null=True)
    l_name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField()
    phone=models.IntegerField(blank=True,null=True)
    address=models.CharField(max_length=250,blank=True,null=True)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50,blank=True,null=True)
    postcode=models.IntegerField(blank=True,null=True)
    payment_mode=models.CharField(max_length=50,blank=True,null=True)
    order_id=models.CharField(max_length=50,blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,blank=True,null=True)
    country=models.CharField(max_length=50,blank=True,null=True)
    
    def __str__(self):
        return self.f_name
    
class Order(models.Model):
    user_id=models.ForeignKey(User_Detail,on_delete=models.CASCADE,blank=True,null=True)
    cart_id=models.ForeignKey(Cart,on_delete=models.CASCADE,blank=True,null=True)
    Billingdetails_id=models.ForeignKey(Billingdetail,on_delete=models.CASCADE,blank=True,null=True)
    date_time=models.DateTimeField(auto_now_add=True,blank=True,null=True)   
    
