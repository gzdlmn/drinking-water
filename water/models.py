from django.db import models
# Create your models here.
class Water(models.Model):
    user = models.ForeignKey("auth.user", null=True, blank=False, on_delete=models.CASCADE)
    drinking = models.BooleanField(null=True, blank=False)
    created_date = models.DateField(auto_now_add=True, null=True, blank=False)
    class Meta:
        verbose_name_plural = "Did you drink water"
    def __str__(self):
        return "{}-{}-{}".format(self.user, self.drinking, self.created_date)

    def glasses(self):
        if self.drinking is True:
            return '<img src="/media/icons8-sparkling-water-24.png"/>'.format(self.drinking)
