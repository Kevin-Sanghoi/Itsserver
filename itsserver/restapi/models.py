from django.db import models

# Create your models here.
class Farmer(models.Model):
	name = models.CharField(max_length=50)
	plots = models.IntegerField()
	phone = models.IntegerField()
	area = models.FloatField()
	address = models.CharField(max_length=100)
	wells = models.IntegerField()
	godowns = models.IntegerField()
	capacity = models.IntegerField()

	def __str__(self):
		return self.name