# ------------------------------------------------------------------------- #
# APUNTES:
# 		   XXX.
#
#
# IMPORTANTE:
#  			  - models.CharField() = Indica un campo de tipo Char (definido).
#  			  - models.TextField() = Indica un campo de tipo Char (indefinido).
#  			  - models.DateTimeField() = Indica un campo de tipo Date.
# ------------------------------------------------------------------------- #

# Importación
from django.db import models


# ---------------------------------- Modelos --------------------------------- #

# Proyecto
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
