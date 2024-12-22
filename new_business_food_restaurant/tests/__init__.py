from framework.configuration import config
from new_business_food_restaurant.configuration import config as project_config

for key, value in project_config.__dict__.items():
    config.__dict__[key] = value