from django.db import models
# Create your models here.
class Suppilerdb(models.Model):
    s_name = models.CharField(max_length=100,null=True,blank=True)
    s_mobileno = models.IntegerField( null=True, blank=True)
    s_email = models.CharField(max_length=100, null=True, blank=True)
    s_address = models.CharField(max_length=100, null=True, blank=True)
    s_gstin = models.CharField(max_length=100,null=True)

class Stocksdb(models.Model):
    stockname = models.CharField(max_length=100,null=True,blank=True)
    quantity = models.IntegerField(null=True)


class Salesdb(models.Model):
    cname = models.CharField(max_length=100, null=True, blank=True)
    cmobileno = models.IntegerField(null=True, blank=True)
    cemail = models.CharField(max_length=100, null=True, blank=True)
    caddress = models.CharField(max_length=100, null=True, blank=True)
    cgstin = models.CharField(max_length=100, null=True)
    stock = models.ForeignKey(Stocksdb, on_delete=models.CASCADE, null=True)
    stockprice = models.PositiveIntegerField(null=True, blank=True)
    stockquantity = models.PositiveIntegerField(null=True, blank=True)
    totalprice = models.IntegerField(null=True, blank=True)

class Purchasesdb(models.Model):
    suppliername = models.CharField(max_length=100,null=True,blank=True)
    suppliermobileno = models.IntegerField( null=True, blank=True)
    suppliergstin = models.CharField(max_length=100,null=True)
    stock = models.ForeignKey(Stocksdb, on_delete=models.CASCADE,null=True)
    stockprice = models.PositiveIntegerField( null=True, blank=True)
    stockquantity = models.PositiveIntegerField( null=True, blank=True)
    totalprice = models.IntegerField( null=True, blank=True)







# class Purchase(models.Model):
#     stock = models.ForeignKey(Stocksdb, on_delete=models.CASCADE)
#     stockquantity = models.IntegerField()
#     purchase_date = models.DateTimeField(auto_now_add=True)