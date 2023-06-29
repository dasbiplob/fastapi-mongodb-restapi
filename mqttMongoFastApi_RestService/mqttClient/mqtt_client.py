import json
import time
import logging
import paho.mqtt.client as mqtt

# MQTT broker details
broker_address = 'mqtt.eclipseprojects.io'
broker_port = 1883
topic = 'charger/1/connector/1/session/1'

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

# MQTT client initialization
def init_mqtt_client(on_connect_callback, on_message_callback):
    client = mqtt.Client()
    client.on_connect = on_connect_callback
    client.on_message = on_message_callback
    client.connect(broker_address, broker_port)

    # Start the MQTT client loop
    client.loop_start()

    return client

# Publish new sessions every 1 minute
def publish_new_sessions(client):
    session_id = 1
    energy_delivered = 30
    duration = 45
    session_cost = 70

    # Create the session payload
    payload = {
        'session_id': session_id,
        'energy_delivered_in_kWh': energy_delivered,
        'duration_in_seconds': duration,
        'session_cost_in_cents': session_cost
    }

    # Convert the payload to JSON
    json_payload = json.dumps(payload)

    # Publish the message
    client.publish(topic, json_payload)

# MQTT on_connect callback
def on_connect(client, userdata, flags, rc):
    logger.info('Connected to MQTT broker')

    # Subscribe to topic after connection is established
    client.subscribe(topic)

# MQTT on_message callback
def on_message(client, userdata, msg):
    logger.info(f'Received MQTT message: {msg.payload.decode()}')

# Main function
def main():
    # Initialize MQTT client
    client = init_mqtt_client(on_connect, on_message)

    # Publish new sessions every 1 minute
    while True:
        publish_new_sessions(client)
        time.sleep(60)

# Run the main function
if __name__ == '__main__':
    main()
