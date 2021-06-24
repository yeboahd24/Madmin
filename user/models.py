from django.db import models

CATEGORY_CHOICE = (
		('Web Development', 'Web Development'),
		('Graphic Design', 'Graphic Design'),
		('Tech Gadget', 'Tech Gadget'),
		('Other', 'Other'),
	)

class Category(models.Model):
	title = models.CharField(max_length=200, null=True)
	category = models.CharField(max_length=300, choices=CATEGORY_CHOICE, null=True)
	body = models.TextField(max_length=500, null=True, blank=True)
	slug = models.SlugField(max_length=200)
	date = models.DateField(max_length=200, null=True)


	class Meta:
	    verbose_name = "Category"
	    verbose_name_plural = "Categorys"

	def __str__(self):
	    return self.title
    
class CategoryIndexTitle(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		verbose_name = "Title"
		verbose_name_plural = "Titles"

	def __str__(self):
		return self.name
    
