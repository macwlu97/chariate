from django.db import models

class AbstractBaseModel(models.Model):
    '''
        Class contains common fields for all models
    '''

    add_user = models.ForeignKey(
        'User',
        models.PROTECT,
        blank=True,
        null=True,
        related_name='%(class)s_add_user'
    )
    add_date = models.DateTimeField(auto_now_add=True)
    mod_user = models.ForeignKey(
        'User',
        models.PROTECT,
        blank=True,
        null=True,
        related_name='%(class)s_mod_user'
    )
    mod_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        app_label = 'chariate_app'
