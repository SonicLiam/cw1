import pytest
from app import create_app, TestingConfig, db
from app.schemas import *
from mock import *


@pytest.fixture
def app():
    app = create_app(TestingConfig)
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


test_configurations = [
    (DistanceTravelledToWork, DistanceTravelledToWorkSchema(), 'distance_travelled_to_work'),
    (MethodOfTravelToWork, MethodOfTravelToWorkSchema(), 'method_of_travel_to_work'),
    (EconomicActivity, EconomicActivitySchema(), 'economic_activity'),
    (HoursWorked, HoursWorkedSchema(), 'hours_worked'),
    (NSSEC, NSSECSchema(), 'nssec'),
    (Occupation, OccupationSchema(), 'occupation'),
]


@pytest.mark.parametrize("model,schema,url_prefix", test_configurations)
def test_create(client, app, model, schema, url_prefix):
    with app.app_context():
        for _ in range(100):
            data = create_data(model)
            response = client.post(f'/api/{url_prefix}', json=data)
            assert response.status_code == 201
            data['id'] = response.json['id']
            assert response.json == data
            assert model.query.get(data['id']) is not None
            assert schema.dump(model.query.get(data['id'])) == data


@pytest.mark.parametrize("model,schema,url_prefix", test_configurations)
def test_get(client, app, model, schema, url_prefix):
    created_data = []
    with app.app_context():
        for _ in range(100):
            data = create_data(model)
            response = client.post(f'/api/{url_prefix}', json=data)
            assert response.status_code == 201
            data['id'] = response.json['id']
            created_data.append(data)
            assert response.json == data
            assert model.query.get(data['id']) is not None
        with app.app_context():
            for data in created_data:
                response = client.get(f'/api/{url_prefix}/{data["id"]}')
                assert response.status_code == 200
                assert response.json['id'] == data['id']
            response = client.get(f'/api/{url_prefix}')
            assert response.status_code == 200
            assert len(response.json) == 100
            for data in response.json:
                assert data in created_data


@pytest.mark.parametrize("model,schema,url_prefix", test_configurations)
def test_update(client, app, model, schema, url_prefix):
    created_data = []
    with app.app_context():
        for _ in range(100):
            data = create_data(model)
            response = client.post(f'/api/{url_prefix}', json=data)
            assert response.status_code == 201
            data['id'] = response.json['id']
            created_data.append(data)
            assert response.json == data
            assert model.query.get(data['id']) is not None
        with app.app_context():
            for data in created_data:
                new_data = create_data(model)
                response = client.put(f'/api/{url_prefix}/{data["id"]}', json=new_data)
                assert response.status_code == 200
                new_data['id'] = data['id']
                assert response.json == new_data
                assert model.query.get(data['id']) is not None
                assert schema.dump(model.query.get(data['id'])) == new_data


@pytest.mark.parametrize("model,schema,url_prefix", test_configurations)
def test_delete(client, app, model, schema, url_prefix):
    created_data = []
    with app.app_context():
        for _ in range(100):
            data = create_data(model)
            response = client.post(f'/api/{url_prefix}', json=data)
            assert response.status_code == 201
            data['id'] = response.json['id']
            created_data.append(data)
            assert response.json == data
            assert model.query.get(data['id']) is not None
        with app.app_context():
            for data in created_data:
                response = client.delete(f'/api/{url_prefix}/{data["id"]}')
                assert response.status_code == 204
                assert model.query.get(data['id']) is None
