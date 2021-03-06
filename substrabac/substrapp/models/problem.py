from django.db import models

from libs.timestampModel import TimeStamped
from .utils import compute_hash


def upload_to(instance, filename):
    return 'problems/{0}/{1}'.format(instance.pk, filename)


class Problem(TimeStamped):
    """Storage Problem table"""
    pkhash = models.CharField(primary_key=True, max_length=64, blank=True)
    validated = models.BooleanField(default=False, blank=True)
    description = models.FileField(upload_to=upload_to)
    metrics = models.FileField(upload_to=upload_to)

    def save(self, *args, **kwargs):
        """Use hash of description file as primary key"""
        if not self.pkhash:
            self.pkhash = compute_hash(self.description)
        super(Problem, self).save(*args, **kwargs)

    def __str__(self):
        return "Problem with pkhash %(pkhash)s with validated %(validated)s" % {'pkhash': self.pkhash, 'validated': self.validated}
