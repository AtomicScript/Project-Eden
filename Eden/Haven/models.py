from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Diary(models.Model):
    Feelings_CHOICES = [
        ('anger', "Anger"),
        ('frustrated', "Frustrated"),
        ('happy', "Happy"),
        ('calm', "Calm"),
        ('numb', "Numb"),
        ('sad', "Sad"),
        ('excited', "Excited")
    ]
    Privacy_Choise = [
        ('public', "Public"),
        ('private', 'Private')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    thoughts_for_the_day = models.TextField()
    expectation = models.TextField()
    reflection = models.TextField()
    feeling = models.CharField(max_length=10, choices=Feelings_CHOICES)
    privacy = models.CharField(max_length=10, choices=Privacy_Choise, default='Private')
    gratitude = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self):
        return reverse("diary_detail", kwargs={"pk": self.pk})
    