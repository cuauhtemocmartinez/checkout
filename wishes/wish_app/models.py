from django.db import models
import re

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors['first_name'] = "Your first name must be more than 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Your first name must be more than 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email must be valid format"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = "Password and conform password do not match"
        return errors

class WishManager(models.Manager):
    def validator(self, form):
        errors = {}
        if len(form['item']) < 3:
            errors['length'] = "A wish must consist of at least 3 characters!"
        if len(form['description']) < 3:
            errors['length'] = "A description must be provided!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Wish(models.Model):
    item = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    poster = models.ForeignKey(User, related_name="wishes", on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WishManager()


class Grant(models.Model):
    item = models.CharField(max_length=100)
    poster = models.ForeignKey(User, related_name="granted", on_delete=models.CASCADE)
    message = models.ForeignKey(Wish, related_name="wishlist", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)