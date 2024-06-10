from django.db import models


class URL(models.Model):
    """
       Model representing a URL and its shortened version.

       Attributes:
           url (CharField): The original URL to be shortened.
                            Max length is 2000 characters.
           short_url (CharField): The shortened version of the original URL.
                                  Max length is 30 characters.
           created_at (DateTimeField): The timestamp when the URL was created.
                                       Automatically set to the current date and time when the URL is created.

       Methods:
           __str__(): Returns a string representation of the URL object,
                      showing the first 30 characters of the original URL
                      followed by the shortened URL.

       Meta:
           verbose_name (str): A human-readable name for the model in singular form ("URL").
           verbose_name_plural (str): A human-readable name for the model in plural form ("urls").
       """

    url = models.CharField(max_length=2000)
    short_url = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
               Returns a string representation of the URL object.

               Returns:
                   str: A string showing the first 30 characters of the original URL followed by the shortened URL.
        """
        return f"{self.url[:30]} -> {self.short_url}"

    class Meta:
        verbose_name = "URL"
        verbose_name_plural = "urls"
