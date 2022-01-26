from django.db import models
from user.models import UserModel # user 앱에 있는 모델을 사용할건데 이름이 UserModel인것을 사용할거다.
from taggit.managers import TaggableManager

# Create your models here.
# 글쓰기 모델을 만든다.
class TweetModel(models.Model):
    class Meta:
        db_table = 'tweet'

    author = models.ForeignKey(UserModel,on_delete=models.CASCADE) #FroeignKey: 다른 데이터베이스에 모델을 가져오겠다는 명령어
    content = models.CharField(max_length=256)
    tags = TaggableManager(blank=True)#blank=True 비어있어도 작동한다.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class TweetComment(models.Model):
    class Meta:
        db_table = "comment"
    tweet = models.ForeignKey(TweetModel, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

