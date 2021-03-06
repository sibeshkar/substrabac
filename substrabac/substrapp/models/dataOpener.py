from django.db import models
from .utils import compute_hash


def upload_to(instance, filename):
    return 'dataopeners/{0}/{1}'.format(instance.pk, filename)


class DataOpener(models.Model):
    """Storage DataOpener table"""
    pkhash = models.CharField(primary_key=True, max_length=64, blank=True)
    name = models.CharField(blank=True, max_length=24)
    script = models.FileField(upload_to=upload_to)

    def save(self, *args, **kwargs):
        """Use hash of description file as primary key"""
        if not self.pkhash:
            self.pkhash = compute_hash(self.script)
        super(DataOpener, self).save(*args, **kwargs)

    def __str__(self):
        return "DataOpener with pkhash %(pkhash)s with name %(name)s" % {'pkhash': self.pkhash,
                                                                         'name': self.name}
