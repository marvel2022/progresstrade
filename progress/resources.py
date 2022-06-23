from import_export import resources
from progress.models import Product

class ProductResource(resources.ModelResource):
  
    class Meta:
        model = Product

