from django.db import models

Cat = (
    ('shirt', 'Shirt'),
    ('trousers', 'Trousers'),
    ('jacket','Jacket'),
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



class Order(models.Model):
    order_no=models.IntegerField(null=True,blank=True,unique=True)
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


class lay(models.Model):
    order_no=models.IntegerField(null=True,blank=True,unique=True)
    Category= models.CharField(max_length=55, choices=Cat)
    Style= models.CharField(max_length=55,choices=Sat)
    Fit= models.CharField(max_length=55,choices=Fat,default='Slim')
    Red38=models.IntegerField(default=0,null=True,blank=True)
    Red40=models.IntegerField(default=0,null=True,blank=True)
    Red42=models.IntegerField(default=0,null=True,blank=True)
    Red44=models.IntegerField(default=0,null=True,blank=True)
    Red46=models.IntegerField(default=0,null=True,blank=True)
    Red48=models.IntegerField(default=0,null=True,blank=True)
    Red50=models.IntegerField(default=0,null=True,blank=True)
    Red52=models.IntegerField(default=0,null=True,blank=True)
    Red54=models.IntegerField(default=0,null=True,blank=True)
    Blue38=models.IntegerField(default=0,null=True,blank=True)
    Blue40=models.IntegerField(default=0,null=True,blank=True)
    Blue42=models.IntegerField(default=0,null=True,blank=True)
    Blue44=models.IntegerField(default=0,null=True,blank=True)
    Blue46=models.IntegerField(default=0,null=True,blank=True)
    Blue48=models.IntegerField(default=0,null=True,blank=True)
    Blue50=models.IntegerField(default=0,null=True,blank=True)
    Blue52=models.IntegerField(default=0,null=True,blank=True)
    Blue54=models.IntegerField(default=0,null=True,blank=True)
    Yellow38=models.IntegerField(default=0,null=True,blank=True)
    Yellow40=models.IntegerField(default=0,null=True,blank=True)
    Yellow42=models.IntegerField(default=0,null=True,blank=True)
    Yellow44=models.IntegerField(default=0,null=True,blank=True)
    Yellow46=models.IntegerField(default=0,null=True,blank=True)
    Yellow48=models.IntegerField(default=0,null=True,blank=True)
    Yellow50=models.IntegerField(default=0,null=True,blank=True)
    Yellow52=models.IntegerField(default=0,null=True,blank=True)
    Yellow54=models.IntegerField(default=0,null=True,blank=True)
    


class Roll(models.Model):
    order_no=models.IntegerField(null=True,blank=True,unique=True)
    Style= models.CharField(max_length=55,choices=Sat)
    Roll_1=models.IntegerField(default=0,null=True,blank=True)
    Roll_2=models.IntegerField(default=0,null=True,blank=True)
    Roll_3= models.IntegerField(default=0,null=True,blank=True)
    Roll_4=models.IntegerField(default=0,null=True,blank=True)
    Roll_5=models.IntegerField(default=0,null=True,blank=True)
    no_of_plies=models.IntegerField(default=0,null=True,blank=True)
    lay_length=models.DecimalField(max_digits=15,decimal_places=2,default=1.5,null=True,blank=True)









    
