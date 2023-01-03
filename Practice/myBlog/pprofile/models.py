# ------------------------------------------------------------------------- #
# APUNTES:
# 		   XXX.
#
#
# IMPORTANTE:
#  			  - verbose_name = Define el nombre "traducido" del dato.
#  			  - models.CharField() = Indica un campo de tipo Char (definido).
#  			  - models.TextField() = Indica un campo de tipo Char (indefinido).
#  			  - models.DateTimeField() = Indica un campo de tipo Date.
# ------------------------------------------------------------------------- #

# Importación
from django.db import models


# ---------------------------------- Modelos --------------------------------- #

# Proyecto
class Project(models.Model):
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-dateUpdated"]  # Orden inicial.

    title = models.CharField(verbose_name="Título", max_length=200)
    description = models.TextField(verbose_name="Descripción")

    dateCreated = models.DateTimeField(
        verbose_name="Fecha de creación", auto_now_add=True
    )

    dateUpdated = models.DateTimeField(
        verbose_name="Fecha de actualización", auto_now=True
    )

    def __str__(self):
        return self.title
