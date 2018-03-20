from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.TextField('Text of question',max_length=200)
    pub_date = models.DateTimeField('Date of publication','date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    choice_text = models.CharField('The choice',max_length = 200)
    votes = models.IntegerField('Number of votes of a choice',default=0)
    def __str__(self):
        return self.choice_text
    