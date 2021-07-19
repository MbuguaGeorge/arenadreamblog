from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Customblogname(models.Model):
    blogname=models.CharField(max_length=100)

    def __str__(self):
        return self.blogname

    class Meta:
        verbose_name_plural='Blog name'


class OverViewtext(models.Model):
    overview_text=models.TextField(max_length=255,default="Arena fitness gym is aimed towards building a fit community in all fields.\n\n Enjoy!!")

    def __str__(self):
        return self.overview_text

    class Meta:
        verbose_name_plural='set blog overview text'


class Blogintroheading(models.Model):
    site_intro_heading=models.CharField(max_length=100,default='Quick intro to our site')

    def __str__(self):
        return self.site_intro_heading

    class Meta:
        verbose_name_plural='Set blog intro context heading'

class Site_intro_context(models.Model):
    site_intro_context=models.TextField(max_length=255,default="Welcome arena fitness gym where fitness is not an option")

    def __str__(self):
        return self.site_intro_context

    class Meta:
        verbose_name_plural='Set intro context'


class Site_random_context(models.Model):
      random_content=models.TextField(max_length=255,default="Random page content will appear here")

      def __str__(self):
        return self.random_content

      class Meta:
        verbose_name_plural='Set random content'

class Subscribe_newslater_description(models.Model):
    subscribe_newslater_description=models.TextField(max_length=255,default="Subscribe to our RSS feeds and newslater for quick updates")

    def __str__(self):
        return self.subscribe_newslater_description

    class Meta:
        verbose_name_plural='Subscribe Newslate description'


class Ranks(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Ranks'

class Contacts(models.Model):
     user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
     rank=models.ForeignKey(Ranks,on_delete=models.CASCADE,blank=True,null=True)
     phone=models.CharField(max_length=12)
     dateadded=models.DateTimeField(auto_now_add=True,blank=True,null=True)

     def __str__(self):
        return f'{self.rank} ({self.phone})'

     class Meta:
        verbose_name_plural='Set Contacts'

class Helpdesk(models.Model):
    street_address=models.TextField(max_length=255,default="Siriba campus - Nyawita")
    physical_location=models.CharField(max_length=255,default="Maseno student center - Wing A")
    email=models.EmailField(max_length=100,default="asiafric@gmail.com")
    tel=models.CharField(max_length=12,default="254711349412")
    facebook=models.URLField()
    twitter=models.URLField()
    youtube=models.URLField()
    instagram=models.URLField()
    other=models.URLField(default="enter any aditional social media url")
    rights_year=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="Help desk setup"

    def __str__(self):
        return self.email

class Gallery(models.Model):
    image=models.ImageField(upload_to="gallery/images/%d/")
    timestamp=models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.image.url

    class Meta:
        ordering=['-timestamp']
        verbose_name_plural="Gallery"


