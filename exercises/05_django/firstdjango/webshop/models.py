from django.db import models

class Product(models.Model):
    """
    Write your model for the exercise 3 here. Remove the pass text.
    """
    #title string 255 characters, unique
    title = models.CharField(max_length=255, unique=True)
    #description unlimited text
    description = models.TextField()
    #image_url: URL, optional
    image_url = models.URLField(blank = True)
    #quantity number: default 0
    quantity = models.IntegerField(default=0)

    def sell(self):
        self.quantity = self.quantity - 1
        self.save()
