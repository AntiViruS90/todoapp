from django.db import models as m


class Todo(m.Model):
    title = m.CharField(max_length=200)
    description = m.CharField(max_length=300, blank=True)
    date = m.DateTimeField(auto_now_add=True)
    done = m.BooleanField(default=False)

    def __str__(self):
        return self.title
