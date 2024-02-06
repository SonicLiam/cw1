from app import db


class BaseInfo(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    local_authority_code = db.Column(db.String(255), nullable=False)
    local_authority_name = db.Column(db.String(255), nullable=False)
    LSOA_code = db.Column(db.String(255), nullable=False)
    residents_aged_16_74_in_employment = db.Column(db.Integer)


class DistanceTravelledToWork(BaseInfo):
    distance_less_than_2km = db.Column(db.Integer)
    distance_2km_to_less_than_5km = db.Column(db.Integer)
    distance_5km_to_less_than_10km = db.Column(db.Integer)
    distance_10km_to_less_than_20km = db.Column(db.Integer)
    distance_20km_to_less_than_30km = db.Column(db.Integer)
    distance_30km_to_less_than_40km = db.Column(db.Integer)
    distance_40km_to_less_than_60km = db.Column(db.Integer)
    distance_60km_and_over = db.Column(db.Integer)
    work_mainly_at_or_from_home = db.Column(db.Integer)
    other = db.Column(db.Integer)


class MethodOfTravelToWork(BaseInfo):
    work_mainly_at_or_from_home = db.Column(db.Integer)
    underground_metro_light_rail_tram = db.Column(db.Integer)
    train = db.Column(db.Integer)
    bus_minibus_or_coach = db.Column(db.Integer)
    taxi = db.Column(db.Integer)
    motorcycle_scooter_or_moped = db.Column(db.Integer)
    driving_a_car_or_van = db.Column(db.Integer)
    passenger_in_a_car_or_van = db.Column(db.Integer)
    bicycle = db.Column(db.Integer)
    on_foot = db.Column(db.Integer)
    other_method_of_travel_to_work = db.Column(db.Integer)


class EconomicActivity(BaseInfo):
    economically_active_full_time_employee = db.Column(db.Integer)
    economically_active_part_time_employee = db.Column(db.Integer)
    economically_active_full_time_student = db.Column(db.Integer)
    economically_active_self_employed_with_employees_full_time = db.Column(db.Integer)
    economically_active_self_employed_with_employees_part_time = db.Column(db.Integer)
    economically_active_self_employed_without_employees_full_time = db.Column(db.Integer)
    economically_active_self_employed_without_employees_part_time = db.Column(db.Integer)
    economically_active_unemployed = db.Column(db.Integer)
    economically_inactive_long_term_sick_or_disabled = db.Column(db.Integer)
    economically_inactive_looking_after_home_or_family = db.Column(db.Integer)
    economically_inactive_other = db.Column(db.Integer)
    economically_inactive_retired = db.Column(db.Integer)
    economically_inactive_full_time_students = db.Column(db.Integer)


class HoursWorked(BaseInfo):
    hours_worked_15_or_less = db.Column(db.Integer)
    hours_worked_16_to_30 = db.Column(db.Integer)
    hours_worked_31_to_48 = db.Column(db.Integer)
    hours_worked_49_or_more = db.Column(db.Integer)


class NSSEC(BaseInfo):
    higher_managerial_admin_and_professional = db.Column(db.Integer)
    lower_managerial_admin_and_professional = db.Column(db.Integer)
    intermediate = db.Column(db.Integer)
    small_employers_own_account_workers = db.Column(db.Integer)
    lower_supervisory_and_technical = db.Column(db.Integer)
    semi_routine = db.Column(db.Integer)
    routine = db.Column(db.Integer)
    never_worked_and_long_term_unemployed = db.Column(db.Integer)
    full_time_students = db.Column(db.Integer)


class Occupation(BaseInfo):
    managers_directors_and_senior_officials = db.Column(db.Integer)
    professional_occupations = db.Column(db.Integer)
    associate_professional_and_technical_occupations = db.Column(db.Integer)
    administrative_and_secretarial_occupations = db.Column(db.Integer)
    skilled_trades_occupations = db.Column(db.Integer)
    caring_leisure_and_other_service_occupations = db.Column(db.Integer)
    sales_and_customer_service_occupations = db.Column(db.Integer)
    process_plant_and_machine_operatives = db.Column(db.Integer)
    elementary_occupations = db.Column(db.Integer)
