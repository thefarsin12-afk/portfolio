from rest_framework import serializers

class AdminRegisterSerializer(serializers.Serializer):

    username = serializers.CharField()

    email = serializers.EmailField()

    password = serializers.CharField()


class AboutSerializer(serializers.Serializer):

    full_name = serializers.CharField()

    title = serializers.CharField()

    bio = serializers.CharField()

    email = serializers.EmailField()

    github_url = serializers.URLField()

    linkedin_url = serializers.URLField()
    
    resume_download_url = serializers.URLField()


class EducationSerializer(serializers.Serializer):

    institution = serializers.CharField()

    degree = serializers.CharField()

    start_date = serializers.DateField()

    end_date = serializers.DateField()

    grade_or_cgpa = serializers.CharField()

    description = serializers.CharField()    
