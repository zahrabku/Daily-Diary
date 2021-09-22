from django.db import models

class diary(models.Model):
    diary_text=models.TextField(blank=True, null=True)
    pub_date=models.DateTimeField('data published')
    # created_at = models.DateTimeField(auto_now_add=True)
    # modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('pub_date',)



