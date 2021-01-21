from import_export import resources
from .models import Cars


class CarsResource(resources.ModelResource):
    class Meta:
        model = Cars
