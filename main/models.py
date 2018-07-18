from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=256)
    summary = models.CharField(max_length=1024)
    description = models.TextField()
    members = models.CharField(max_length=256)
    link = models.CharField(max_length=1024)
    color_r = models.FloatField()
    color_g = models.FloatField()
    color_b = models.FloatField()

    def __str__(self):
        return self.name


class Feedback(models.Model):
    creation_time = models.DateTimeField()
    name = models.CharField(max_length=256)
    content = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return 'Feedback [{},{}]'.format(self.project, self.name)
