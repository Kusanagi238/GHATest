import pytest
from app.processor import calculate_average_temp, parse_weather_config

def test_calculate_average_temp():
    assert calculate_average_temp([20.5, 22.5, 26.0]) == 23.0
    assert calculate_average_temp([]) == 0.0
    assert calculate_average_temp(None) == 0.0

def test_parse_weather_config():
    assert parse_weather_config({"region": "Taichung"}) == "Processing region: Taichung"
    with pytest.raises(ValueError):
        parse_weather_config({"timezone": "UTC"})