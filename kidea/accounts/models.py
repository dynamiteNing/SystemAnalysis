from django.db import models

# Create your models here.

class Member(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null= True)
	email = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def _str_(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null= True)
	description = models.CharField(max_length=500, null=True)
	date_created = models.DateTimeField(auto_now_add=True)















