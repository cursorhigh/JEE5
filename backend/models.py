from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=255)
    content_description = models.TextField(default='No Context')
    content = models.ImageField(upload_to='question_images/', null=True, blank=True)
    tags = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    question_upvotes = models.IntegerField(default=0)
    question_downvotes = models.IntegerField(default=0)
    created_by = models.CharField(max_length=255,default='Unknown')
    def __str__(self):
        return self.title
    

class Solution(models.Model):
    content_description = models.TextField(default='No Context')
    content = models.ImageField(upload_to='solution_images/', null=True, blank=True)
    solution_upvotes = models.IntegerField(default=0)
    solution_downvotes = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="solutions")

    def __str__(self):
        return f"Solution for question: {self.question.title}"

class Profile(models.Model):
    profile_img=models.ImageField(upload_to='user_images/', null=True, blank=True)
    profile_name=models.CharField(max_length=255)
    profile_id=models.IntegerField(null=True,unique=True)