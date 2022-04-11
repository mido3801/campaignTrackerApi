"""Contains abstract Route object to be used for CRUD operations on varying
   MongoDB document models"""
from flask import Response, request
from flask.views import MethodView
import mongoengine as me


class Route(MethodView):
    """Abstract object for simple routes"""

    def __init__(self, model):
        """Set provided model"""
        self.resource = model

    def get(self):
        body = request.get_json()
        id = body.get('id')
        if id is None:
            objects = self.resource.objects().to_json()
            return Response(objects,
                            mimetype="application/json",
                            status=200)
        specified_object = self.resource.objects.get(id=body['id']).to_json()
        return Response(specified_object,
                        mimetype="application/json",
                        status=200)

    def post(self):
        # Go through all fields in designated object model.
        # If we have a field that is a reference field then we
        # need to check if we are trying to associate any data with
        # that field. If we are then we need to grab the actual objects
        # that we are trying to associate with the id's that are included
        # in the request body
        body = request.get_json()
        field_dict = self.resource._fields
        for field_name, field in field_dict.items():

            if isinstance(field, me.ReferenceField):
                if field_name in body:
                    reference_key = body[field_name]
                    reference_object = field.document_type.objects.\
                        get(id=reference_key)
                    body[field_name] = reference_object

            elif isinstance(field, me.ListField):
                if field_name in body:
                    reference_keys = body[field_name]
                    reference_objects = [field.field.document_type.objects.
                                         get(id=key) for key in reference_keys]
                    body[field_name] = reference_objects

        created_object = self.resource(**body).save()
        id = created_object.id
        return {'id': str(id)}, 200

    def put(self):
        body = request.get_json()
        self.resource.objects.get(id=body['id']).update(**body)
        return '', 200

    def delete(self):
        body = request.get_json()
        self.resource.objects.get(id=body['id']).delete()
        return '', 200
