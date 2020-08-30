from django.db import models

class AdminModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.IntegerField(unique=True)
    email = models.EmailField()
    photo = models.ImageField(upload_to='product/',default=False)
    password = models.CharField(max_length=50,default=False)


class FormarModel(models.Model):
    fid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    contact=models.IntegerField(unique=True)
    email=models.EmailField()
    photo = models.ImageField(upload_to='product/')
    date_of_register=models.DateField()
    password=models.CharField(max_length=50)

class ProductModel(models.Model):
    fid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    photo = models.ImageField(upload_to='product/')
    date_of_register = models.DateField()


class MerchantModel(models.Model):
    mid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.IntegerField(unique=True)
    email = models.EmailField()
    photo = models.ImageField(upload_to='product/')
    date_of_register = models.DateField()
    password= models.CharField(max_length=100)
    gst=models.CharField(max_length=15)


class OrderModel(models.Model):
    oid = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    Merchant = models.ForeignKey(MerchantModel, on_delete=models.CASCADE)
    Product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)



class Newlicence(models.Model):
    lid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.IntegerField(unique=True)
    email = models.EmailField()
    gst = models.CharField(max_length=15)
    firm=models.CharField(max_length=100)
    photo = models.ImageField(upload_to='product/')
    status=models.CharField(max_length=50,default=False)


class viewlicense(models.Model):
       vid=models.AutoField(primary_key=True)
       date=models.DateField(auto_now_add=True)
       newlicence=models.ForeignKey(Newlicence,on_delete=models.CASCADE)
       admin=models.ForeignKey(AdminModel,on_delete=models.CASCADE,default=False)

class AcceptAppModel(models.Model):
    rid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.IntegerField(unique=True)
    email = models.EmailField()
    gst = models.CharField(max_length=15)
    firm = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='product/')
    status = models.CharField(max_length=50, default=False)