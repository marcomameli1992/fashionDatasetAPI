from flask import Flask
from flask_restful import Resource, Api
from apispec import APISpec
from marshmallow import Schema, fields
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs

app=Flask(__name__)
api=Api(app)
/*app.config.update({
    'APISPEC_SPEC':APISpec(
        title='Progetto Moda',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL':'/swagger/',
    'APISPEC_SWAGGER_UI_URL':'/swagger-ui/'
})
docs=FlaskApiSpec(app)

class ModaResponseSchema(Schema):

