import os

summer_21_dates = [164, 220]
summer_22_dates = [401, 448]

_weather_effect = 0.081

# computed from national average. In the US, precipitation effects business by -5.4%
# moderate_precip_effect = (2/3) * x = 0.054
# x = 0.081


if os.path.exists(os.path.join('src', 'constants', 'business_specific_constants.py')):
    from src.constants.business_specific_constants import specific_business_weather_effect
    _weather_effect = specific_business_weather_effect

heavy_precip_effect = _weather_effect * (3 / 3)
moderate_precip_effect = _weather_effect * (2 / 3)
light_precip_effect = _weather_effect * (1 / 3)

precip_dict = {
    'None': 0,
    'Light': light_precip_effect,
    'Moderate': moderate_precip_effect,
    'Heavy': heavy_precip_effect
}
