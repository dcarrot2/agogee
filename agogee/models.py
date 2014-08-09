from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)

	email = models.EmailField()
	picture = models.ImageField(upload_to='profile_images', blank=True)
	about_me = models.CharField(max_length=240)
	ranking = models.IntegerField(default=0)

	def __unicode__(self):
		return self.user.username