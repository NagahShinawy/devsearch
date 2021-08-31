from apps.core.db.models import UUIDMixin, InfoMixin, SlugMixin, TimestampMixin


class Project(UUIDMixin, InfoMixin, SlugMixin, TimestampMixin):

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
        verbose_name = "Project"
        verbose_name_plural = "Lean Projects"



