from django.db import models
Cat = (
    ('sh', 'Shirt'),
    ('tr', 'Trousers'),
)
Sat = (
    ('ca', 'Casual'),
    ('gl', 'Looking'),
)
# Create your models here.
class Order(models.Model):
    Category= models.CharField(max_length=55, choices=Cat)
    Style= models.CharField(max_length=55,choices=Sat)
    Rejection_rate=models.IntegerField(default=2)
    Acception_rate=models.IntegerField(default=2)
    Stock= models.IntegerField(default=10)
    Red0rderquantity=models.IntegerField()
    RedXS=models.IntegerField()
    RedS=models.IntegerField()
    RedM=models.IntegerField()
    RedL=models.IntegerField()
    RedXL=models.IntegerField()
    RedXXL=models.IntegerField()
    Blue0rderquantity=models.IntegerField()
    BlueXS=models.IntegerField()
    BlueS=models.IntegerField()
    BlueM=models.IntegerField()
    BlueL=models.IntegerField()
    BlueXL=models.IntegerField()
    BlueXXL=models.IntegerField()
    Yellow0rderquantity=models.IntegerField()
    YellowXS=models.IntegerField()
    YellowS=models.IntegerField()
    YellowM=models.IntegerField()
    YellowL=models.IntegerField()
    YellowXL=models.IntegerField()
    YellowXXL=models.IntegerField()


    
