#!/bin/bash

# Receive data to be written to the database

# Imports
import paho.mqtt.client as mqtt
import json

from reading_class import Reading
from db_writer import write_reading

# Script variables
subscribe_channel = 'datacenter'
cert_location = '/etc/mosquitto/ca_certificates/ca.crt'
client_ip = '10.140.10.21'
client_port = 8883
app_name = 'dashboard'

# The callback for when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and reconnect then subscriptions will be renewed
    client.subscribe(subscribe_channel)

# The callback for when a PUBLISH message is received from the server
def on_message(client, userdata, message):
    # Receive and convert incoming message
    str_message = str(message.payload)[2:-1]
    str_message = str_message.replace("'", '"')
    json_message = json.loads(str_message)
    
    # Get individual readings from the message and send them to processing
    for incoming_reading in json_message['readings']:
        process_reading(incoming_reading)

# Process and write the reading
def process_reading(reading):
    # Create new reading
    new_reading = Reading(
        reading['rack'],
        reading['sensor'],
        reading['sensor_type'],
        reading['sensor_value'],
        reading['date'],
        reading['time']
    )

    # Format reading for the db
    new_writeable_reading = new_reading.make_writeable()
    # Determin the correct collection for the reading
    if new_reading.rack == '0':
        collection_name = app_name + '_' + new_reading.sensor_type
    else:
        collection_name = app_name + '_rack_' + str(new_reading.rack)
    # Send the reading to the db_writer
    write_reading(new_writeable_reading, collection_name)

# Configure client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Encryption settings
client.tls_set(cert_location)

# Connect to client
client.connect(client_ip, client_port)

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting
client.loop_forever()

