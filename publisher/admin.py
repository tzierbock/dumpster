from django.contrib import admin
from publisher.models import Tag, Category, Author, Image, ImageGallary, Article
# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Image)
admin.site.register(ImageGallary)
admin.site.register(Article)