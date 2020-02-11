from django.db import models
Cat = (
    ('shirt', 'Shirt'),
    ('trousers', 'Trousers'),
    ('jacket','Jacket')
)
Sat = (
    ('casual', 'Casual'),
    ('formal', 'Formal'),
)
Fat = (
    ('Slim', 'Slim'),
    ('Regular', 'Regular'),
    ('Super Slim','Super Slim'),
)
# Create your models here.
class Order(models.Model):
    order_no=models.IntegerField(null=True,blank=True)
    Category= models.CharField(max_length=55, choices=Cat)
    Style= models.CharField(max_length=55,choices=Sat)
    Fit= models.CharField(max_length=55,choices=Fat,default='Slim')
    Rejection_rate=models.IntegerField(default=2)
    Acception_rate=models.IntegerField(default=2)
    Stock= models.IntegerField(default=10)
    Red0rderquantity=models.IntegerField(default=0,null=True,blank=True)
    RedXS=models.IntegerField(default=0,null=True,blank=True)
    RedS=models.IntegerField(default=0,null=True,blank=True)
    RedM=models.IntegerField(default=0,null=True,blank=True)
    RedL=models.IntegerField(default=0,null=True,blank=True)
    RedXL=models.IntegerField(default=0,null=True,blank=True)
    RedXXL=models.IntegerField(default=0,null=True,blank=True)
    Blue0rderquantity=models.IntegerField(default=0,null=True,blank=True)
    BlueXS=models.IntegerField(default=0,null=True,blank=True)
    BlueS=models.IntegerField(default=0,null=True,blank=True)
    BlueM=models.IntegerField(default=0,null=True,blank=True)
    BlueL=models.IntegerField(default=0,null=True,blank=True)
    BlueXL=models.IntegerField(default=0,null=True,blank=True)
    BlueXXL=models.IntegerField(default=0,null=True,blank=True)
    Yellow0rderquantity=models.IntegerField(default=0,null=True,blank=True)
    YellowXS=models.IntegerField(default=0,null=True,blank=True)
    YellowS=models.IntegerField(default=0,null=True,blank=True)
    YellowM=models.IntegerField(default=0,null=True,blank=True)
    YellowL=models.IntegerField(default=0,null=True,blank=True)
    YellowXL=models.IntegerField(default=0,null=True,blank=True)
    YellowXXL=models.IntegerField(default=0,null=True,blank=True)


    
