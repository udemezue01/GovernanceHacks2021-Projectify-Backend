from django.db import models
from django.conf import settings
# Create your models here.

PROJECT_TYPE = (

	('D', 'DIGITAL PROJECT'),

	('P', 'PHYSICAL PROJECT'),


	)

STATUS = (

	('P', 'PENDING'),

	('R', 'REJECTED'),

	('C', 'COMPLETED')

	)

class Contractor(models.Model):

	user 			= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	name 			= models.CharField(max_length = 3000, blank = True, null = True)
	website 		= models.CharField(max_length = 3000, blank = True, null = True)
	logo 			= models.FileField(blank = True, null = True)
	phone 			= models.CharField(max_length = 3000, blank = True, null = True)
	email 			= models.CharField(max_length = 3000, blank = True, null = True)
	address 		= models.CharField(max_length = 3000, blank = True, null = True)
	facebook 		= models.CharField(max_length = 3000, blank = True, null = True)
	twitter 		= models.CharField(max_length = 3000, blank = True, null = True)
	instagram 		= models.CharField(max_length = 3000, blank = True, null = True)
	website 		= models.CharField(max_length = 3000, blank = True, null = True)

	def __str__(self):

		return f'{self.name}'





class Project(models.Model):

	user 			=  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

	contractor 		=  models.ForeignKey(Contractor, on_delete = models.CASCADE)

	title			=  models.CharField(max_length = 300)
	description		=  models.CharField(max_length = 3000, blank = True, null = True)

	price 			=  models.IntegerField(blank = True, null = True)
	project_type	=  models.CharField(max_length = 3000, choices = PROJECT_TYPE)


	location 		=  models.CharField(max_length = 3000, blank = True, null = True)


	start_date 		=  models.DateField(auto_now = False, auto_now_add = True)
	end_date	 	=  models.DateField(auto_now = False, auto_now_add = True)

	images 			=  models.FileField(blank = True, null = True)
	Videos 			=  models.FileField(blank = True, null = True)

	status 			=  models.CharField(max_length = 3000, choices = STATUS)

	subscribers 	=  models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'Subscribers')


	def __str__(self):

		return f'{self.title}'




class Review(models.Model):
	user 			= 	models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	target 			= 	models.ForeignKey(Project, on_delete = models.CASCADE)
	text 			= 	models.CharField(max_length = 4000, blank = True)
	rating 			= 	models.BooleanField(blank = True, default = False)

	def __str__(self):

		return f'{self.user.full_name} - Review'
	

