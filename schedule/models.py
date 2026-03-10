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

    def __str__(self):
        return str.join(' ', [self.lastname, self.name, self.surname])


class Subject(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return self.title


class Group(models.Model):
    name = models.CharField(max_length=50)


    def get_key_value_pair(self):
        l = self.name.split('К')
        return (l[0], l[1])

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    def __str__(self):
        return self.name


class Schedule(models.Model):
    class Day(models.TextChoices):
        Monday = 'Mn', 'Monday'
        Tuesday = 'Tu', 'Tuesday'
        Wednesday = 'We', 'Wednesday'
        Thursday = 'Th', 'Thursday'
        Friday = 'Fr', 'Friday'
        Saturday = 'Sa', 'Saturday'

    class Time(models.IntegerChoices):
        First = 1, '8:00 - 9:40'
        Second = 2, '9:50 - 11:30'
        Third = 3, '11:50 - 13:30'
        Fourth = 4, '13:40 - 15:20'
        Fifth = 5, '15:40 - 17:20'
        Sixth = 6, '17:30 - 19:10'
        Seventh = 7, '19:20 - 21:00'

    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    day = models.CharField(max_length=2, choices=Day.choices)
    time = models.IntegerField(choices=Time.choices)

    def __str__(self):
        return f'{self.group} at {self.Day(self.day).label} in {self.Time(self.time).label}'


    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedule'