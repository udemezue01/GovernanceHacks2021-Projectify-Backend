from django.db import models

from django.contrib.auth.models import (
		BaseUserManager,
		AbstractBaseUser

		)


 



class UserManager(BaseUserManager):
	def create_user(self, email, full_name,   password=None):
	    """
	    Creates and saves a User with the given email, date of
	    birth and password.
	    """
	    if not email:
	        raise ValueError('Users must have an email address')

	    user = self.model(
	        email=self.normalize_email(email),
	         full_name = full_name,
		    
	       		) 

	    user.set_password(password)
	    user.save(using=self._db)
	    return user

	def create_superuser(self, email, full_name,  password ):

	    """
	    Creates and saves a superuser with the given email, date of
	    birth and password.
	    """
	    user = self.create_user(
		        email,
				full_name = full_name,
		        password=password,
		        		)


	    user.is_admin = True
	    user.save(using=self._db)
	    return user


# ACCOUNT_TYPE = (
	
# 	('IND', 'personal'),
# 	('BUS', 'Business')

# 	)



class User (AbstractBaseUser):

	full_name 		= 	models.CharField(max_length = 3000, blank = True, null = True)

	email			=	models.EmailField(verbose_name = 'email address', max_length = 225, unique = True)

	# account_type 	=	models.CharField(max_length = 3000 ,choices = ACCOUNT_TYPE)
	verified 		=	models.BooleanField(default = False, blank  = True)





	
	is_active		=	models.BooleanField(default = True)
	is_admin 		=	models.BooleanField(default = False)
	objects 		=   UserManager()

	USERNAME_FIELD = 'email'
	EMAIL_FIELD = "email"
	REQUIRED_FIELDS = ['full_name' ]

	


	def __str__(self):
		return f'{self.user.full_name} - Account'

	def has_perm (self, perm, obj = None):
		# "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		# Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always

		return True

	@property 	
	def is_staff(self):

		# Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
		return self.is_admin


	# @property
	# def owner(self):
	# 	return self.full

	# @property
	# def user(self):
	# 	instance = self
	# 	return Profile.objects.filter_by_instance(instance)




	

	


