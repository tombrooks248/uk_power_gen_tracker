import pytest

from app.app import get_current_gen_data

def test_power_gen_api_call():

    power_gen_dict = get_current_gen_data()

    assert type(power_gen_dict) == dict
    assert power_gen_dict['BIOMASS'] >= 0
    assert power_gen_dict['SOLAR'] >= 0
