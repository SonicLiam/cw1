from faker import Faker

from app.models import *

fake = Faker()


def create_data(model, **kwargs):
    """生成测试数据的工厂函数"""
    if model == DistanceTravelledToWork:
        return create_distance_travelled_to_work(**kwargs)
    if model == MethodOfTravelToWork:
        return create_method_of_travel_to_work(**kwargs)
    if model == EconomicActivity:
        return create_economic_activity(**kwargs)
    if model == HoursWorked:
        return create_hours_worked(**kwargs)
    if model == NSSEC:
        return create_nssec(**kwargs)
    if model == Occupation:
        return create_occupation(**kwargs)


def create_base_info(**kwargs):
    data = {
        'year': kwargs.get('year', fake.random_int(min=1, max=2024)),
        'local_authority_code': kwargs.get('local_authority_code', fake.bothify(text='????##')),
        'local_authority_name': kwargs.get('local_authority_name', fake.city()),
        'lsoa_code': kwargs.get('LSOA_code', fake.bothify(text='????##')),
        'residents': kwargs.get('residents_aged_16_74_in_employment',
                                                         fake.random_int(min=0, max=10000))
    }
    return data


def create_distance_travelled_to_work(**kwargs):
    baseInfo = create_base_info(**kwargs)
    data = {
        **baseInfo,
        'distance_less_than_2km': kwargs.get('distance_less_than_2km', fake.random_int(min=0, max=1000)),
        'distance_2km_to_less_than_5km': kwargs.get('distance_2km_to_less_than_5km', fake.random_int(min=0, max=1000)),
        'distance_5km_to_less_than_10km': kwargs.get('distance_5km_to_less_than_10km',
                                                     fake.random_int(min=0, max=1000)),
        'distance_10km_to_less_than_20km': kwargs.get('distance_10km_to_less_than_20km',
                                                      fake.random_int(min=0, max=1000)),
        'distance_20km_to_less_than_30km': kwargs.get('distance_20km_to_less_than_30km',
                                                      fake.random_int(min=0, max=1000)),
        'distance_30km_to_less_than_40km': kwargs.get('distance_30km_to_less_than_40km',
                                                      fake.random_int(min=0, max=1000)),
        'distance_40km_to_less_than_60km': kwargs.get('distance_40km_to_less_than_60km',
                                                      fake.random_int(min=0, max=1000)),
        'distance_60km_and_over': kwargs.get('distance_60km_and_over', fake.random_int(min=0, max=1000)),
        'work_mainly_at_or_from_home': kwargs.get('work_mainly_at_or_from_home', fake.random_int(min=0, max=1000)),
        'other': kwargs.get('other', fake.random_int(min=0, max=1000))
    }

    return data


def create_method_of_travel_to_work(**kwargs):
    baseInfo = create_base_info(**kwargs)
    data = {
        **baseInfo,
        'work_mainly_at_or_from_home': kwargs.get('work_mainly_at_or_from_home', fake.random_int(min=0, max=1000)),
        'underground_metro_light_rail_tram': kwargs.get('underground_metro_light_rail_tram',
                                                        fake.random_int(min=0, max=1000)),
        'train': kwargs.get('train', fake.random_int(min=0, max=1000)),
        'bus_minibus_or_coach': kwargs.get('bus_minibus_or_coach', fake.random_int(min=0, max=1000)),
        'taxi': kwargs.get('taxi', fake.random_int(min=0, max=1000)),
        'motorcycle_scooter_or_moped': kwargs.get('motorcycle_scooter_or_moped', fake.random_int(min=0, max=1000)),
        'driving_a_car_or_van': kwargs.get('driving_a_car_or_van', fake.random_int(min=0, max=1000)),
        'passenger_in_a_car_or_van': kwargs.get('passenger_in_a_car_or_van', fake.random_int(min=0, max=1000)),
        'bicycle': kwargs.get('bicycle', fake.random_int(min=0, max=1000)),
        'on_foot': kwargs.get('on_foot', fake.random_int(min=0, max=1000)),
        'other_method_of_travel_to_work': kwargs.get('other_method_of_travel_to_work', fake.random_int(min=0, max=1000))
    }
    return data


def create_economic_activity(**kwargs):
    baseInfo = create_base_info(**kwargs)
    data = {
        **baseInfo,
        'economically_active_employee_full_time': kwargs.get('economically_active_employee_full_time',
                                                             fake.random_int(min=0, max=1000)),
        'economically_active_employee_part_time': kwargs.get('economically_active_employee_part_time',
                                                                fake.random_int(min=0, max=1000)),
        'economically_active_full_time_student': kwargs.get('economically_active_full_time_student',
                                                            fake.random_int(min=0, max=1000)),
        'economically_active_self_employed_with_employees_full_time': kwargs.get(
            'economically_active_self_employed_with_employees_full_time',
            fake.random_int(min=0, max=1000)),
        'economically_active_self_employed_with_employees_part_time': kwargs.get(
            'economically_active_self_employed_with_employees_part_time',
            fake.random_int(min=0, max=1000)),
        'economically_active_self_employed_without_employees_full_time': kwargs.get(
            'economically_active_self_employed_without_employees_full_time',
            fake.random_int(min=0, max=1000)),
        'economically_active_self_employed_without_employees_part_time': kwargs.get(
            'economically_active_self_employed_without_employees_part_time',
            fake.random_int(min=0, max=1000)),
        'economically_active_unemployed': kwargs.get('economically_active_unemployed', fake.random_int(min=0, max=1000)),
        'economically_inactive_long_term_sick_or_disabled': kwargs.get('economically_inactive_long_term_sick_or_disabled',
                                                                      fake.random_int(min=0, max=1000)),
        'economically_inactive_looking_after_home_or_family': kwargs.get('economically_inactive_looking_after_home_or_family',
                                                                        fake.random_int(min=0, max=1000)),
        'economically_inactive_other': kwargs.get('economically_inactive_other', fake.random_int(min=0, max=1000)),
        'economically_inactive_retired': kwargs.get('economically_inactive_retired', fake.random_int(min=0, max=1000)),
        'economically_inactive_full_time_students': kwargs.get('economically_inactive_full_time_students',
                                                              fake.random_int(min=0, max=1000))
    }
    return data


def create_hours_worked(**kwargs):
    baseInfo = create_base_info(**kwargs)
    data = {
        **baseInfo,
        'hours_worked_15_or_less': kwargs.get('hours_worked_15_or_less', fake.random_int(min=0, max=1000)),
        'hours_worked_16_to_30': kwargs.get('hours_worked_16_to_30', fake.random_int(min=0, max=1000)),
        'hours_worked_31_to_48': kwargs.get('hours_worked_31_to_48', fake.random_int(min=0, max=1000)),
        'hours_worked_49_or_more': kwargs.get('hours_worked_49_or_more', fake.random_int(min=0, max=1000))
    }
    return data


def create_nssec(**kwargs):
    baseInfo = create_base_info(**kwargs)
    data = {
        **baseInfo,
        'higher_managerial_admin_and_professional': kwargs.get('higher_managerial_admin_and_professional',
                                                               fake.random_int(min=0, max=1000)),
        'lower_managerial_admin_and_professional': kwargs.get('lower_managerial_admin_and_professional',
                                                              fake.random_int(min=0, max=1000)),
        'intermediate': kwargs.get('intermediate', fake.random_int(min=0, max=1000)),
        'small_employers_own_account_workers': kwargs.get('small_employers_own_account_workers',
                                                          fake.random_int(min=0, max=1000)),
        'lower_supervisory_and_technical': kwargs.get('lower_supervisory_and_technical',
                                                      fake.random_int(min=0, max=1000)),
        'semi_routine': kwargs.get('semi_routine', fake.random_int(min=0, max=1000)),
        'routine': kwargs.get('routine', fake.random_int(min=0, max=1000)),
        'never_worked_and_long_term_unemployed': kwargs.get('never_worked_and_long_term_unemployed',
                                                            fake.random_int(min=0, max=1000)),
        'full_time_students': kwargs.get('full_time_students', fake.random_int(min=0, max=1000))
    }
    return data


def create_occupation(**kwargs):
    baseInfo = create_base_info(**kwargs)
    data = {
        **baseInfo,
        'managers_directors_and_senior_officials': kwargs.get('managers_directors_and_senior_officials',
                                                              fake.random_int(min=0, max=1000)),
        'professional_occupations': kwargs.get('professional_occupations', fake.random_int(min=0, max=1000)),
        'associate_professional_and_technical_occupations': kwargs.get(
            'associate_professional_and_technical_occupations',
            fake.random_int(min=0, max=1000)),
        'administrative_and_secretarial_occupations': kwargs.get('administrative_and_secretarial_occupations',
                                                                 fake.random_int(min=0, max=1000)),
        'skilled_trades_occupations': kwargs.get('skilled_trades_occupations', fake.random_int(min=0, max=1000)),
        'caring_leisure_and_other_service_occupations': kwargs.get('caring_leisure_and_other_service_occupations',
                                                                   fake.random_int(min=0, max=1000)),
        'sales_and_customer_service_occupations': kwargs.get('sales_and_customer_service_occupations',
                                                             fake.random_int(min=0, max=1000)),
        'process_plant_and_machine_operatives': kwargs.get('process_plant_and_machine_operatives',
                                                           fake.random_int(min=0, max=1000)),
        'elementary_occupations': kwargs.get('elementary_occupations', fake.random_int(min=0, max=1000)),
    }
    return data
