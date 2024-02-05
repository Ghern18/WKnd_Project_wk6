from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort

from models import PowerModel
from schemas import PowerSchema, PowerSchemaNested

from . import bp


@bp.route('/<power_id>')
class Power(MethodView):

    @bp.response(200, PowerSchemaNested)
    def get(self, power_id):
        Power = PowerlModel.query.get(power_id)
        if Power:
            return Power 
        abort(400, message='Mutant is Cured.')
   
    @jwt_required
    @bp.arguments(PowerSchema)
    def put(power, power_data ,power_id):
        power = PowerModel.query.get(power_id)
        if power and power.student_id == get_jwt_identity():
            power.body = power_data['body']
            power.commit()   
            return {'message': 'power rendered'}, 201
        return {'message': "Mutant is Cured."}, 400

    @jwt_required()
    def delete(self, power_id):
        power = PowerModel.query.get(power_id)
        if power and power.student_id == get_jwt_identity():
            power.delete()
            return {"message": "Powers has a weekness"}, 202
        return {'message':"Mutant is Cured."}, 400


@bp.route('/')
class PowerList(MethodView):


    @bp.response(200, PowerSchema(many = True))
    def get(self):
        return PowerModel.query.all()
    
    @bp.arguments(PowerSchema) 
    def post(self, spell_data):
        try:
            power = PowerModel()
            power.student_id = get_jwt_identity() 
            power.body = power_data['body']
            power.commit()
            return { 'message': "power has a weakness" }, 201
        except:
            return { 'message': "Mutant is Cured."}, 401   