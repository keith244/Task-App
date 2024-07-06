from django.db import models
#from django.contrib.auth import get_user_model
# Create your models here.

#User = get_user_model()
class Tasks(models.Model):
    #user        = models.OneToOneField(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length=50, blank=False)  
    description = models.TextField(blank=False )        
    due_date    = models.DateField(blank=True) 
    date_created= models.DateTimeField(blank=False)    
    """A status field to be added. Down here"""
    #status      = models.BooleanField(default='in progress')   
    CATEGORY_CHOICES = [
        ('General', 'General'),
        ('Personal', 'Personal'),
        ('Work', 'Work'),
    ]

    categories = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES,
        default='General'
    )
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    priority = models.CharField(
        max_length=20, 
        choices=PRIORITY_CHOICES,
        default='Medium'
    )

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name_plural = 'Tasks' 