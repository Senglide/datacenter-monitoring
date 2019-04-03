# Script used for testing because the mqtt broker doesn't throw python errors and exceptions

import json

from ./code/reading_class import Reading
from ./code/db_writer import write_reading

myobj = {
    "readings": [
        {"rack": 1, "sensor": 1, "sensor_type": "temp", "sensor_value": 25},
        {"rack": 1, "sensor": 1, "sensor_type": "hum", "sensor_value": 70},
        {"rack": 1, "sensor": 2, "sensor_type": "temp", "sensor_value": 23},
        {"rack": 1, "sensor": 2, "sensor_type": "hum", "sensor_value": 80},
        {"rack": 2, "sensor": 1, "sensor_type": "temp", "sensor_value": 24},
        {"rack": 2, "sensor": 1, "sensor_type": "hum", "sensor_value": 72},
        {"rack": 2, "sensor": 2, "sensor_type": "temp", "sensor_value": 25},
        {"rack": 2, "sensor": 2, "sensor_type": "hum", "sensor_value": 76},
        {"rack": 3, "sensor": 1, "sensor_type": "temp", "sensor_value": 26},
        {"rack": 3, "sensor": 1, "sensor_type": "hum", "sensor_value": 85},
        {"rack": 3, "sensor": 2, "sensor_type": "temp", "sensor_value": 28},
        {"rack": 3, "sensor": 2, "sensor_type": "hum", "sensor_value": 82},
        {"rack": 0, "sensor": 1, "sensor_type": "movement", "sensor_value": 1},
        {"rack": 0, "sensor": 1, "sensor_type": "smoke", "sensor_value": 0},
        {"rack": 0, "sensor": 2, "sensor_type": "movement", "sensor_value": 0},
        {"rack": 0, "sensor": 2, "sensor_type": "smoke", "sensor_value": 1}
    ]
}

str_myobj = str(myobj)
str_myobj = str_myobj.replace("'", '"')
json_myobj = json.loads(str_myobj)

for reading in myobj['readings']:
    reading = reading.copy()
    new_reading = Reading(
        reading['rack'],
        reading['sensor'],
        reading['sensor_type'],
        reading['sensor_value']
    )
    new_writeable_reading = new_reading.make_writeable()
    print(new_writeable_reading)
    write_reading(new_writeable_reading, 'diy_rack_' + str(reading['rack']))