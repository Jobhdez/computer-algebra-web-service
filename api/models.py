from django.db import models
from django.contrib.auth.models import AbstractUser


class DiffExpression(models.Model):
    exp = models.CharField(max_length=200)
    diff_exp = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'the differentiation of {self.exp} if {self.diff_exp}'

class LinearAlgebra(models.Model):
    exp = models.CharField(max_length=200)
    eval_exp = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'the evaluation of the linear algebra expression {self.exp} is {self.eval_exp}'

class Polynomial(models.Model):
    exp = models.CharField(max_length=200)
    eval_poly = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=200)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'the evaluation of the polynomial expression {self.exp} is {self.eval_poly}'

class User(AbstractUser):
    friends = models.ManyToManyField("User", blank=True)
   
class Friend_Request(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.from_user} wants to befriend {self.to_user}.'


class DiffComment(models.Model):
    exp = models.ForeignKey(DiffExpression, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active =  models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]
    
    def __str__(self):
        return f'Comment by {self.name} on {self.exp}'


class LalgComment(models.Model):
    exp = models.ForeignKey(LinearAlgebra, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active =  models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]
    
    def __str__(self):
        return f'Comment by {self.name} on {self.exp}'


class PolyComment(models.Model):
    exp = models.ForeignKey(Polynomial, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active =  models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]
    
    def __str__(self):
        return f'Comment by {self.name} on {self.exp}'
