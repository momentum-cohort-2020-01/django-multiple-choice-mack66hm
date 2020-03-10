from django.db import models
from users.models import User
import datetime

class Question(models.Model):
    title = models.CharField(max_length= 500)
    body = models.TextField(max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User, related_name='users_quesitons', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Question: {self.title} {self.body} {self.created_at}'


    class Meta:
        ordering: ['-created_at']


class Answer(models.Model):
    body = models.TextField(max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User, related_name='users_answers', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Answer: {self.body} {self.created_at}'