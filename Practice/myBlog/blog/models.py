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
from ckeditor.fields import RichTextField


# ---------------------------------- Modelos --------------------------------- #

# Posteo
class Post(models.Model):
    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        ordering = ["-dateUpdated"]  # Orden inicial.

    image = models.ImageField(verbose_name="Imagen", upload_to="blog")
    title = models.CharField(verbose_name="Título", max_length=200)
    description = models.TextField(verbose_name="Descripción")
    content = RichTextField(verbose_name="Contenido")

    dateCreated = models.DateTimeField(
        verbose_name="Fecha de creación", auto_now_add=True
    )

    dateUpdated = models.DateTimeField(
        verbose_name="Fecha de actualización", auto_now=True
    )

    def __str__(self):
        return self.title
