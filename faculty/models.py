from datetime import date

from django.db import models


class MainPage(models.Model):
    title = models.CharField(max_length=200)
    short_text = models.TextField()
    about_text = models.TextField()
    dean = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Головна сторінка"
        verbose_name_plural = "Головна сторінка"

    def __str__(self):
        return self.title


class Department(models.Model):
    name = models.CharField(max_length=200)
    head = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедри"

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    description = models.TextField()
    coordinator_name = models.CharField(max_length=200)
    coordinator_contact = models.CharField(max_length=200)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="programs"
    )
    disciplines = models.TextField(blank=True)

    class Meta:
        verbose_name = "Спеціальність"
        verbose_name_plural = "Спеціальності"

    def __str__(self):
        return self.name

    def disciplines_list(self):
        result = []
        for line in self.disciplines.split("\n"):
            line = line.strip()
            if line != "":
                result.append(line)
        return result


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    degree = models.CharField(max_length=200, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="teachers"
    )

    class Meta:
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"

    def __str__(self):
        return self.name


class ExchangeProgram(models.Model):
    university = models.CharField(max_length=200)
    country = models.CharField(max_length=100, default="", db_index=True)
    languages = models.CharField(max_length=200)
    places_count = models.PositiveIntegerField(default=0)
    deadline = models.DateField()
    description = models.TextField()

    class Meta:
        verbose_name = "Програма обміну"
        verbose_name_plural = "Програми обміну"

    def __str__(self):
        return self.university

    def is_open(self):
        return self.deadline >= date.today()
