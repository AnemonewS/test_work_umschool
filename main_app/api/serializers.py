from rest_framework import serializers
from main_app.models import *


class FilterCommentSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(comment_reply=None)
        return super().to_representation(data)


class RecursiveCommentSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        exclude = ('updated_at',)


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    comment_reply = serializers.SlugRelatedField(read_only=True, slug_field='text')
    comment_reply_ids = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), source='replies',
                                                           required=False, write_only=True, many=True)
    replies = RecursiveCommentSerializer(read_only=True, many=True)

    class Meta:
        list_serializer_class = FilterCommentSerializer
        model = Comment
        exclude = ('updated_at',)
