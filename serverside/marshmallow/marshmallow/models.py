from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from djangotoolbox.fields import ListField
from mongoengine import *


class User(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=datetime.now)
    premium = models.BooleanField(default=False)
    points = models.IntegerField(default=1)
    biography = models.CharField(max_length=255)

    USERNAME_FIELD = 'username'

    def __unicode__(self):
        return self.username

class Comments(Document):
    product_name = StringField(max_length=255)
    to = StringField(max_length=255, default=product_name)
    comment = StringField(max_length=1024)
    likes = IntField(default=0)
    dislikes = IntField(default=0)
    date_created = DateTimeField(default=datetime.now)


class Products(Document):
    product_owner = StringField(max_length=50)
    product_name = StringField(max_length=50)
    category = StringField(max_length=30)
    rating = FloatField(default=0.0)
    positive_score = IntField(default=0)
    negative_score = IntField(default=0)
    probability = FloatField(default=0)
    date_created = DateTimeField(default=datetime.now)
    last_updated = DateTimeField(default=datetime.now)


class Features(Document):
    name = StringField(max_length=50)
    product_id = ReferenceField(Products)
    rating = FloatField(default=0.0)
    positive_score = IntField(default=0)
    negative_score = IntField(default=0)
    probability = FloatField(default=0.0)
    top_positive_reviews = ListField(default=["No Reviews"])
    top_negative_reviews = ListField(default=["No Reviews"])


