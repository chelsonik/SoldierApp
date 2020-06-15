from django_elasticsearch_dsl import Document, Index
import posts as posts
from warehouse.models import Cloth

posts = Index('posts')


# Create your models here.
@posts.doc_type
class PostDocument(Document):
    class Django:
        model = Cloth
        fields = [
            'name',
            'id',
            'sizes',
            'description',
            'image',
            'slug'
        ]
