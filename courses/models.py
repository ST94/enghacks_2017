from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    uw_id = models.CharField(max_length=6)
    category = models.ForeignKey("Category")
    course_number = models.IntegerField()
    prerequisites = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=4)

    def __str__(self):
        return self.name


class Major(models.Model):
    name = models.CharField(max_length=255)
    courses = models.ManyToManyField("Course")

    def __str__(self):
        return self.name


class Option(models.Model):
    name = models.CharField(max_length=255)
    course = models.ManyToManyField("Course")

    def __str__(self):
        return self.name
