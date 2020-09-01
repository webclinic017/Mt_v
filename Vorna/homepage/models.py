from django.db import models
from django.utils import timezone
# Create your models here.

class Currency(models.Model):
    """Model for Currencies exchanges.
       When Updated, a copy should be placed on to the corresponding database
       For Exampled if USD/EUR is updated a copy should be placed in USDtoEUR database."""
    base_currency = models.CharField(max_length=255)
    non_base_currency = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=20, decimal_places=8)
    timestamp = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    
class Currency_base(models.Model):
    """Base model for currency tables."""
    rate = models.DecimalField(max_digits=25, decimal_places=10)
    timestamp = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True
    
    
# to USD
    
class EURtoUSD(Currency_base):
    pass
    

class GBPtoUSD(Currency_base):
    pass
    
 
class AUDtoUSD(Currency_base):
    pass
    
  
# USD TO
  
class USDtoCAD(Currency_base):
    pass
  
  
class USDtoJPY(Currency_base):
    pass
    
    
class USDtoINR(Currency_base):
    pass
    
   
class USDtoTRY(Currency_base):
    pass
    
  
class USDtoCNY(Currency_base):
    pass  
    
    
class USDtoRUB(Currency_base):
    pass  
    
    
class USDtoAED(Currency_base):
    pass 