from django.db import models


class About(models.Model):

    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    bio = models.TextField()

    email = models.EmailField()
    github_url = models.URLField()
    linkedin_url = models.URLField()
    resume_download_url = models.URLField()

    def __str__(self):
        return self.full_name

   