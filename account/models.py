from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    followings=models.ManyToManyField('self',symmetrical=False, related_name = 'followers')
    # 팔로우 설정  유저모델에 종속되도록 
    @property # 
    def full_name(self):
        return f'{self.last_name}{self.first_name}'



# Create your models here.
