#user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser #장고에서 제공하는 기본 모델
from django.conf import settings

# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"

    bio = models.CharField(max_length=256, default='')
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name ='followee')
    # 팔로우는 상대 사용자를 팔로우 하기때문에

