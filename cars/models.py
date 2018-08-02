from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Car(models.Model):
	make = models.CharField(max_length=120)
	model = models.CharField(max_length=120)
	year = models.IntegerField()
	car_img = models.ImageField(upload_to='car_img', null=True)

	def __str__(self):
		return "{} {} - {}".format(self.make, self.model, self.year, self.car_img)

	def get_absolute_url(self):
		return reverse('car-detail', kwargs={'car_id':self.id})
