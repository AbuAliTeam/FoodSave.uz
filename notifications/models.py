from django.db import models
from accounts.models import User
from products.models import Category

# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Уведомление для {self.user.username}"

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    region = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Подписка {self.user.username} на {self.region} / {self.category}"
