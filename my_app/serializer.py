from rest_framework import serializers

class AdminRegisterSerializer(serializers.Serializer):

    username = serializers.CharField()

    email = serializers.EmailField()

    password = serializers.CharField()


class AboutSerializer(serializers.Serializer):

    full_name = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=150)
    bio = serializers.CharField()

    email = serializers.EmailField()
    github_url = serializers.URLField()
    linkedin_url = serializers.URLField()
    resume_download_url = serializers.URLField()
