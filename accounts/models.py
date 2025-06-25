from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models as geomodels

class User(AbstractUser):
    USER = 'user'
    STORE = 'store'
    ROLE_CHOICES = [
        (USER, 'Покупатель'),
        (STORE, 'Заведение'),
    ]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=USER)
    
    # Add related_name to avoid conflicts with auth.User
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="custom_user_set",
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_set",
        related_query_name="custom_user",
    )
    
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    region = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Профиль {self.user.username}"

class Store(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='store')
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    location = geomodels.PointField(geography=True, null=True, blank=True)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='store_photos/', blank=True, null=True)

    def __str__(self):
        return self.name