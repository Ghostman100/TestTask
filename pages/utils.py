from rest_framework import serializers

# Попытка сделать фабрику сериалазеров
# def serializer_factory(cls):
#     class Serializer(serializers.ModelSerializer):
#         content_type = serializers.SerializerMethodField()
#
#         def get_content_type(self, instance):
#             return cls.__name__
#
#         class Meta:
#             model = cls
#             exclude = ['id', 'page']
#
#     return Serializer


def get_actual(obj):
    """Expands `obj` to the actual object type.
    """
    for name in dir(obj):
        try:
            attr = getattr(obj, name)
            if isinstance(attr, obj.__class__):
                return attr
        except:
            pass
    return obj
