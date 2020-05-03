from django.db import models


def image_folder(instanse, filename):
	filename = instanse.slug + '.' + filename.split('.')[1]
	return '{0}/{1}'.format(instanse.slug, filename)


class Star(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	nickname = models.CharField(max_length=255, blank=True, db_index=True)
	description = models.CharField(max_length=255)
	link = models.CharField(max_length=255, blank=True)
	image = models.ImageField(upload_to=image_folder)
	subscribers = models.IntegerField(default=0)
	price = models.PositiveIntegerField(default=0)
	available = models.BooleanField(default=False)
	slug = models.SlugField(max_length=200, db_index=True)
	video = models.FileField(upload_to=image_folder, blank=True, default='')

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


class Order(models.Model):
	REASONS = [
		('UR', 'urodziny'),
		('WE', 'weding'),
		('PO', 'pozdrowienia'),
		('NE', 'new cos'),
		('OT', 'cos innego'),
	]

	myName = models.CharField(max_length=50)
	reason = models.CharField(max_length=50, choices=REASONS)
	description = models.TextField(max_length=200)
	email = models.EmailField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False)
	price = models.PositiveIntegerField(default=0)
	star = models.ForeignKey(Star, on_delete=models.CASCADE)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return self.email
