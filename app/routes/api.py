from flask import Blueprint, request, jsonify
from app import db
from app.schemas.schemas import *

api_bp = Blueprint('api', __name__)

# Initialize schema instances
distance_travelled_to_work_schema = DistanceTravelledToWorkSchema()
method_of_travel_to_work_schema = MethodOfTravelToWorkSchema()
economic_activity_schema = EconomicActivitySchema()
hours_worked_schema = HoursWorkedSchema()
nssec_schema = NSSECSchema()
occupation_schema = OccupationSchema()


# Common function to create API routes
def create_endpoints(blueprint, url, endpoint_suffix, model, schema):
    @blueprint.route(url, methods=['GET'])
    def get_items():
        items = model.query.all()
        return jsonify(schema.dump(items, many=True)), 200

    @blueprint.route(url, methods=['POST'])
    def create_item():
        data = request.get_json()
        item = schema.load(data)
        db.session.add(item)
        db.session.commit()
        return schema.jsonify(item), 201

    get_items.__name__ = f'get_{endpoint_suffix}'
    create_item.__name__ = f'create_{endpoint_suffix}'

    blueprint.add_url_rule(url, view_func=get_items, methods=['GET'])
    blueprint.add_url_rule(url, view_func=create_item, methods=['POST'])


# Register API routes
create_endpoints(api_bp, '/distance_travelled_to_work', 'distance_travelled_to_work', DistanceTravelledToWork,
                 distance_travelled_to_work_schema)
create_endpoints(api_bp, '/method_of_travel_to_work', 'method_of_travel_to_work', MethodOfTravelToWork,
                 method_of_travel_to_work_schema)
create_endpoints(api_bp, '/economic_activity', 'economic_activity', EconomicActivity, economic_activity_schema)
create_endpoints(api_bp, '/hours_worked', 'hours_worked', HoursWorked, hours_worked_schema)
create_endpoints(api_bp, '/nssec', 'nssec', NSSEC, nssec_schema)
create_endpoints(api_bp, '/occupation', 'occupation', Occupation, occupation_schema)
