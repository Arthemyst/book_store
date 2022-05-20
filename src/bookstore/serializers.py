from rest_framework import serializers

from bookstore.models import Book


class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    external_id = serializers.CharField(required=False, max_length=100)
    title = serializers.CharField(required=False, max_length=100)
    authors = serializers.JSONField(required=False)
    acquired = serializers.BooleanField(required=False, default=False)
    published_year = serializers.IntegerField(required=False)
    thumbnail = serializers.CharField(required=False, max_length=300)

    def create(self, validated_data):
        """
        Create and return a new `Book` instance, given the validated data.
        """
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Book` instance, given the validated data.
        """
        instance.external_id = validated_data.get("external_id", instance.external_id)
        instance.title = validated_data.get("title", instance.title)
        instance.authors = validated_data.get("authors", instance.authors)
        instance.acquired = validated_data.get("acquired", instance.acquired)
        instance.published_year = validated_data.get(
            "published_year", instance.published_year
        )
        instance.thumbnail = validated_data.get("thumbnail", instance.thumbnail)
        instance.save()
        return instance

    class Meta:
        model = Book
        fields = [
            "id",
            "external_id",
            "title",
            "authors",
            "acquired",
            "published_year",
            "thumbnail",
        ]
