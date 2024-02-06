from flask import request, jsonify
from app.models.models import DistanceTravelledToWork
from app.schemas.schemas import DistanceTravelledToWorkSchema

# Distance to work
distance_travelled_to_work_schema = DistanceTravelledToWorkSchema()


@app.route('/distance', methods=['GET', 'POST'])
def distance_travelled_to_work():
    if request.method == 'POST':
        data = request.get_json()
        new_distance_travelled_to_work = DistanceTravelledToWork(distance=data['distance'])
        db.session.add(new_distance_travelled_to_work)
        db.session.commit()
        return distance_travelled_to_work_schema.jsonify(new_distance_travelled_to_work)
    else:
        all_distance_travelled_to_work = DistanceTravelledToWork.query.all()
        result = distance_travelled_to_work_schema.dump(all_distance_travelled_to_work)
        return jsonify(result)
