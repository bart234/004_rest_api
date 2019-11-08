from rest_framework import serializers

from app_p1.models import BlogPost


#converts to json
#validate date
class BlogPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields= ['pk',
                'user',
                'title',
                'content',
                'timestamp']
        read_only_fields = ['user']

    def validate_title(self,value):
        qs = BlogPost.objects.filter(title__iexact=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("Title mus be unique")
        return value