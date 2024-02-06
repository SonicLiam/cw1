from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models import *


class DistanceTravelledToWorkSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = DistanceTravelledToWork
        load_instance = True


class MethodOfTravelToWorkSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = MethodOfTravelToWork
        load_instance = True


class EconomicActivitySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = EconomicActivity
        load_instance = True


class HoursWorkedSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = HoursWorked
        load_instance = True


class NSSECSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = NSSEC
        load_instance = True


class OccupationSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Occupation
        load_instance = True
