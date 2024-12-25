from django.db import models


class Task(models.Model):
    """
    name: String
    status: string choicefield ['draft', 'in progress', 'completed']
    description: string
    """
    pass