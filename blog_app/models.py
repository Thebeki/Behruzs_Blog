from django.db import models

STATUS = (
    (0,"Draft"),
    (1,"Publish")
                )

class Post(models.Model):
    sarlavha = models.CharField(max_length=150)
    yangilash_kuni = models.DateField()
    mazmuni = models.TextField()
    yaratilgan_kun = models.DateField()
    status = models.IntegerField(choices=STATUS)

    class Meta:
        ordering = ['-yaratilgan_kun']

    def __str__(self):
        return self.title