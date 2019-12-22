import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
class Tasks(models.Model):
    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    STATUSES = (
        ('Assigned', _('Assigned')),
        ('in_progress', _('In Progress')),
        ('blocked', _('Blocked')),
        ('done', _('Done')),
        ('dismissed', _('Dismissed'))
    )

    PRIORITIES = (
        ('Normal', _('Normal')),
        ('High', _('High')),
        ('Critical', _('Critical')),
        ('Blocker', _('Blocker'))
    )
    
    title = models.CharField(max_length=140)
    date_posted = models.DateField(default=timezone.now, blank=True, null=True)
    content = models.TextField(_("content"), max_length=2000, null=True, blank=True)
    created_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name="task_created",
        on_delete=models.CASCADE,
    )
    assigned_to = models.ForeignKey(
        User,
        blank=True,
        null=True,
        related_name="task_assigned",
        on_delete=models.CASCADE,
    )
    state = models.CharField(_("state"), max_length=20, choices=STATUSES, default='Assigned')
    priority = models.CharField(_("priority"), max_length=20, choices=PRIORITIES, default='Normal')
   
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={'pk': self.pk})


    