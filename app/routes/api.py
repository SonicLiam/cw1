from flask import Blueprint, request, jsonify
from app import db
from app.schemas.schemas import *

api_bp = Blueprint('api', __name__)

# Initialize schema instances
distance_travelled_to_work_schema = DistanceTravelledToWorkSchema(session=db.session)
method_of_travel_to_work_schema = MethodOfTravelToWorkSchema(session=db.session)
economic_activity_schema = EconomicActivitySchema(session=db.session)
hours_worked_schema = HoursWorkedSchema(session=db.session)
nssec_schema = NSSECSchema(session=db.session)
occupation_schema = OccupationSchema(session=db.session)


# Common function to create API routes
def create_endpoints(blueprint, url, endpoint_suffix, model, schema):
    @blueprint.route(f'{url}/<int:id>', methods=['GET'])
    def get_item(id):
        item = model.query.get_or_404(id)
        return jsonify(schema.dump(item)), 200

    @blueprint.route(url, methods=['GET'])
    def get_items():
        year = request.args.get('year', type=int)
        if year:
            items = model.query.filter_by(year=year).all()
        else:
            items = model.query.all()
        return jsonify(schema.dump(items, many=True)), 200

    @blueprint.route(url, methods=['POST'])
    def create_item():
        data = request.get_json()
        item = schema.load(data)
        db.session.add(item)
        db.session.commit()
        return jsonify(schema.dump(item)), 201

    # PUT
    @blueprint.route(f'{url}/<int:id>', methods=['PUT'])
    def update_item(id):
        item = model.query.get_or_404(id)
        data = request.get_json()
        schema.load(data, instance=item)
        db.session.commit()
        return jsonify(schema.dump(item)), 200

    # DELETE
    @blueprint.route(f'{url}/<int:id>', methods=['DELETE'])
    def delete_item(id):
        item = model.query.get_or_404(id)
        db.session.delete(item)
        db.session.commit()
        return '', 204

    # Set the function names
    get_item.__name__ = f'get_{endpoint_suffix}'
    get_items.__name__ = f'get_{endpoint_suffix}s'
    create_item.__name__ = f'create_{endpoint_suffix}'
    update_item.__name__ = f'update_{endpoint_suffix}'
    delete_item.__name__ = f'delete_{endpoint_suffix}'

    # Register the routes
    blueprint.add_url_rule(f'{url}/<int:id>', view_func=get_item, methods=['GET'])
    blueprint.add_url_rule(url, view_func=get_items, methods=['GET'])
    blueprint.add_url_rule(url, view_func=create_item, methods=['POST'])
    blueprint.add_url_rule(f'{url}/<int:id>', view_func=update_item, methods=['PUT'])
    blueprint.add_url_rule(f'{url}/<int:id>', view_func=delete_item, methods=['DELETE'])


# Register API routes
create_endpoints(api_bp, '/distance_travelled_to_work', 'distance_travelled_to_work', DistanceTravelledToWork,
                 distance_travelled_to_work_schema)
create_endpoints(api_bp, '/method_of_travel_to_work', 'method_of_travel_to_work', MethodOfTravelToWork,
                 method_of_travel_to_work_schema)
create_endpoints(api_bp, '/economic_activity', 'economic_activity', EconomicActivity, economic_activity_schema)
create_endpoints(api_bp, '/hours_worked', 'hours_worked', HoursWorked, hours_worked_schema)
create_endpoints(api_bp, '/nssec', 'nssec', NSSEC, nssec_schema)
create_endpoints(api_bp, '/occupation', 'occupation', Occupation, occupation_schema)
