from django.db import models

class home(models.Model):
		file = models.ImageField(null=True)
		email = models.EmailField(null=False,max_length=70,blank=True)
		comment = models.TextField(null=True,max_length=100,blank=True)

		class Meta:
			db_table = "File"
