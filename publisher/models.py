from django.db import models
from django.contrib.auth.models import User
from django.core.files import File

# Author
class Author(models.Model):
	hasLocalAccount = models.BooleanField(default=False)
	hasGAppAccount = models.BooleanField(default=True)

	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.user.__unicode__()

# Category
class Category(models.Model):
	label = models.CharField(max_length=20, primary_key=True)
	description = models.CharField(max_length=200)

	def __unicode__(self):
		return self.label


# Tag
class Tag(models.Model):
	label = models.CharField(max_length=20, primary_key=True)

	def __unicode__(self):
		return self.label

class Image(models.Model):
	title = models.CharField(max_length=50)
	caption = models.CharField(max_length=200)
	image_file = models.ImageField(upload_to='images')

	def __unicode__(self):
		return self.title

# Article
class Article(models.Model):
	date_published = models.DateTimeField(auto_now=True)
	date_updated = models.DateTimeField(auto_now=True)

	shortTitle = models.CharField(max_length=50, primary_key=True, default="Title")

	author = models.ForeignKey(Author)
	heading = models.CharField(max_length=50)
	caption = models.CharField(max_length=100)
	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag)

	content = models.TextField()
	title_image = models.ForeignKey(Image)

	def __unicode__(self):
		return self.shortTitle

	def getAuthor(self):
		u = self.author.user
		return u.first_name + " " + u.last_name

class ImageGallary(models.Model):
	article = models.ForeignKey(Article)
	images = models.ManyToManyField(Image)

	def __unicode__(self):
		return self.article.heading
