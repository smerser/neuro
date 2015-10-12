from django.core.serializers import serialize
from django.db.models.query import QuerySet
import json
from django.utils.safestring import mark_safe
from django.template import Library
from django.core.serializers.json import DjangoJSONEncoder
register = Library()

def jsonify(object):
        # if isinstance(object, QuerySet):
        #     return mark_safe(serialize('json', object))
    return mark_safe(json.dumps(list(object), cls=DjangoJSONEncoder))

register.filter('jsonify', jsonify)
jsonify.is_safe = True
