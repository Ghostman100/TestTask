from django.db import models


# Create your models here.
class Page(models.Model):
    name = models.CharField(max_length=124)


class Content(models.Model):
    title = models.CharField(max_length=124)
    counter = models.IntegerField(default=0)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='content')

    # def get_content_serializer(self):
    #     return serializer_factory(self.__class__)(self)


class Video(Content):
    link = models.URLField()


class Audio(Content):
    bitrate = models.IntegerField()


class Text(Content):
    text_value = models.TextField()

