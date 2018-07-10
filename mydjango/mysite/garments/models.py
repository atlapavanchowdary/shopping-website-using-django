from django.db import models

# Create your models here.
class FormalShirt(models.Model):  				#super class for formal shirt(model is always represented as a class
    name=models.CharField(max_length=100) 			#name of the shirt is given by CharField
    photo=models.FileField(blank=True)    			#to add photo and not complusary  
    desc=models.TextField(max_length=500) 			# to enter more number of lines(description)
    price=models.DecimalField(max_digits=10,decimal_places=2)   # to give price(2 decimal numbers after point)
    stock=models.PositiveIntegerField()				# age,quantity,stock etc
    availability=models.BooleanField(default=True)              #defautly product is always available
    created=models.DateTimeField(auto_now_add=True)             # when first time we are creating a time then that date and time stamp is taken and stored
    updated=models.DateTimeField(auto_now=True)                 # at particular interval the upataed information is stored(updated time to time and replaces frequently date and time)
    
    def __str__(self): 						#__(magic method)__ (query lst otherwise displays object memory address )hidden method returns one or more strings written in the method
        return self.name     					#displays name of the shirt(example print obj)

    #converting formal shirt class into a model(in cmd)
class CausualShirt(models.Model):
    name=models.CharField(max_length=100) 			
    photo=models.FileField(blank=True)    			
    desc=models.TextField(max_length=500) 			
    price=models.DecimalField(max_digits=10,decimal_places=2)   
    stock=models.PositiveIntegerField()				
    availability=models.BooleanField(default=True)             
    created=models.DateTimeField(auto_now_add=True)             
    updated=models.DateTimeField(auto_now=True)                 
    
    def __str__(self): 						
        return self.name 
class TShirt(models.Model):
    name=models.CharField(max_length=100) 			
    photo=models.FileField(blank=True)    			
    desc=models.TextField(max_length=500) 			
    price=models.DecimalField(max_digits=10,decimal_places=2)   
    stock=models.PositiveIntegerField()				
    availability=models.BooleanField(default=True)             
    created=models.DateTimeField(auto_now_add=True)             
    updated=models.DateTimeField(auto_now=True)                 
    
    def __str__(self): 						
        return self.name     	
class Trouser(models.Model):
    name=models.CharField(max_length=100) 			
    photo=models.FileField(blank=True)    			
    desc=models.TextField(max_length=500) 			
    price=models.DecimalField(max_digits=10,decimal_places=2)   
    stock=models.PositiveIntegerField()				
    availability=models.BooleanField(default=True)             
    created=models.DateTimeField(auto_now_add=True)             
    updated=models.DateTimeField(auto_now=True)                 
    
    def __str__(self): 						
        return self.name   
class Jean(models.Model):
    name=models.CharField(max_length=100) 			
    photo=models.FileField(blank=True)    			
    desc=models.TextField(max_length=500) 			
    price=models.DecimalField(max_digits=10,decimal_places=2)   
    stock=models.PositiveIntegerField()				
    availability=models.BooleanField(default=True)             
    created=models.DateTimeField(auto_now_add=True)             
    updated=models.DateTimeField(auto_now=True)                 
    
    def __str__(self): 						
        return self.name
class TrackPant(models.Model):
    name=models.CharField(max_length=100) 			
    photo=models.FileField(blank=True)    			
    desc=models.TextField(max_length=500) 			
    price=models.DecimalField(max_digits=10,decimal_places=2)   
    stock=models.PositiveIntegerField()				
    availability=models.BooleanField(default=True)             
    created=models.DateTimeField(auto_now_add=True)             
    updated=models.DateTimeField(auto_now=True)                 
    
    def __str__(self): 						
        return self.name     					

         


