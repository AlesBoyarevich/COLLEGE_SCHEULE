from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    lastname = models.CharField(max_length=100, null=False, blank=False)
    surname = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(null=True, blank=True, upload_to='media/teachers')

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


class Subject(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'


class Group(models.Model):
    name = models.CharField(max_length=50)


    def get_key_value_pair(self):
        l = self.name.split('К')
        return (l[0], l[1])

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'