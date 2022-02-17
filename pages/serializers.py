from rest_framework import serializers

from pages import models
from pages.utils import get_actual


class PageSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='page_details', read_only=True)

    class Meta:
        model = models.Page
        fields = ['id', 'name', 'url']


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Content
        fields = ['title', 'counter']


class VideoContentSerializer(ContentSerializer):

    class Meta(ContentSerializer.Meta):
        model = models.Video
        fields = ContentSerializer.Meta.fields + ['link']


class AudioContentSerializer(ContentSerializer):

    class Meta(ContentSerializer.Meta):
        model = models.Audio
        fields = ContentSerializer.Meta.fields + ['bitrate']


class TextContentSerializer(ContentSerializer):

    class Meta(ContentSerializer.Meta):
        model = models.Text
        fields = ContentSerializer.Meta.fields + ['text_value']


CONTAINER_SERIALIZERS = {
    'Video': VideoContentSerializer,
    'Audio': AudioContentSerializer,
    'Text': TextContentSerializer,
    'Content': ContentSerializer,
}


def get_content_serializer(instance):
    actual_instance = get_actual(instance)
    return CONTAINER_SERIALIZERS[actual_instance.__class__.__name__](actual_instance)


class RetrievePageSerializer(PageSerializer):
    content = serializers.SerializerMethodField()

    def get_content(self, instance):
        return [get_content_serializer(content).data for content in instance.content.all()]

    class Meta(PageSerializer.Meta):
        fields = ['id', 'name', 'content']
