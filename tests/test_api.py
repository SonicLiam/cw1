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
    """Test creating items with proper data"""
    with app.app_context():
        for _ in range(100):
            data = create_data(model)
            response = client.post(f'/api/{url_prefix}', json=data)
            assert response.status_code == 201
            data['id'] = response.json['id']
            # Check if the response is the same as the data sent
            assert response.json == data
            # Check if the item was added to the database
            assert model.query.get(data['id']) is not None
            assert schema.dump(model.query.get(data['id'])) == data


@pytest.mark.parametrize("model,schema,url_prefix", test_configurations)
def test_create_with_invalid_data(client, app, model, schema, url_prefix):
    """Test creating items with invalid data"""
    with app.app_context():
        data = create_data(model)
        del data['year']
        response = client.post(f'/api/{url_prefix}', json=data)
        assert response.status_code == 400
        assert response.json == {'year': ['Missing data for required field.']}


@pytest.mark.parametrize("model,schema,url_prefix", test_configurations)
def test_get(client, app, model, schema, url_prefix):
    """Test getting items is successful."""
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
def test_get_with_query(client, app, model, schema, url_prefix):
    """Test getting items with query is successful."""
    created_data = []
    with app.app_context():
        for _ in range(100):
            data = create_data(model, year=2011)
            response = client.post(f'/api/{url_prefix}', json=data)
            assert response.status_code == 201
            data['id'] = response.json['id']
            created_data.append(data)
            assert response.json == data
            assert model.query.get(data['id']) is not None
        with app.app_context():
            response = client.get(f'/api/{url_prefix}?year=2011')
            assert response.status_code == 200
            assert len(response.json) == 100
            for data in response.json:
                assert data['year'] == 2011
            response = client.get(f'/api/{url_prefix}?year=2012')
            assert response.status_code == 200
            assert len(response.json) == 0


@pytest.mark.parametrize("model,schema,url_prefix", test_configurations)
def test_get_with_invalid_query(client, app, model, schema, url_prefix):
    """Test getting items with invalid query returns 400."""
    with app.app_context():
        response = client.get(f'/api/{url_prefix}?year=invalid')
        assert response.status_code == 400
        json_data = response.get_json()
        assert json_data == {'year': ['Not a valid integer']}


@pytest.mark.parametrize("model,schema,url_prefix", test_configurations)
def test_get_with_invalid_id(client, app, model, schema, url_prefix):
    """Test getting items with invalid id returns 404."""
    with app.app_context():
        response = client.get(f'/api/{url_prefix}/invalid')
        assert response.status_code == 404


@pytest.mark.parametrize("model,schema,url_prefix", test_configurations)
def test_update(client, app, model, schema, url_prefix):
    """Test updating items with proper data is successful."""
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
def test_update_with_partial_data(client, app, model, schema, url_prefix):
    """Test updating items with partial data (missing fields) is successful."""
    with app.app_context():
        data = create_data(model)
        response = client.post(f'/api/{url_prefix}', json=data)
        assert response.status_code == 201
        data['id'] = response.json['id']
        new_data = create_data(model)
        del new_data['year']
        response = client.put(f'/api/{url_prefix}/{data["id"]}', json=new_data)
        assert response.status_code == 200
        new_data['id'] = data['id']
        new_data['year'] = data['year']
        assert response.json == new_data
        assert model.query.get(data['id']) is not None
        assert schema.dump(model.query.get(data['id'])) == new_data


@pytest.mark.parametrize("model,schema,url_prefix", test_configurations)
def test_update_with_invalid_id(client, app, model, schema, url_prefix):
    """Test updating items with invalid id returns 404."""
    with app.app_context():
        response = client.put(f'/api/{url_prefix}/invalid', json={})
        assert response.status_code == 404


@pytest.mark.parametrize("model,schema,url_prefix", test_configurations)
def test_delete(client, app, model, schema, url_prefix):
    """Test deleting items is successful."""
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


@pytest.mark.parametrize("model,schema,url_prefix", test_configurations)
def test_delete_with_invalid_id(client, app, model, schema, url_prefix):
    """Test deleting items with invalid id returns 404."""
    with app.app_context():
        response = client.delete(f'/api/{url_prefix}/invalid')
        assert response.status_code == 404
