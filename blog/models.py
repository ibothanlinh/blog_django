from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    # FRESHMAN = 'FR'
    # SOPHOMORE = 'SO'
    # JUNIOR = 'JR'
    # SENIOR = 'SR'
    # GRADUATE = 'GR'
    # YEAR_IN_SCHOOL_CHOICES = [
    #     (FRESHMAN, 'Freshman'),
    #     (SOPHOMORE, 'Sophomore'),
    #     (JUNIOR, 'Junior'),
    #     (SENIOR, 'Senior'),
    #     (GRADUATE, 'Graduate'),
    # ]
    author = models.ForeignKey(
        'auth.User',
        # choices=YEAR_IN_SCHOOL_CHOICES,
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])