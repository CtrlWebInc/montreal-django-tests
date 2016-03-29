from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=30)
    sound = models.CharField(max_length=30)

    def speak(self):
        return 'The %s says "%s"' % (self.name, self.sound)
