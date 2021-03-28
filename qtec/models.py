from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class QtechKeywordSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    search_keyword = models.CharField(max_length=200)
    search_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.search_keyword
