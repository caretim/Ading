from django.db import models
from accounts.models import NewUser
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey(NewUser,on_delete=models.CASCADE)
    
    
# migrations 폴더 삭제시 변경사항이 감지되지않음,