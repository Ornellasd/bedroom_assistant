from time import sleep, strftime
import datetime
import json
import os.path

import paho.mqtt.client as mqtt
import pygal


while True:
    
    temp_file = 'chart_json/temps.json'
    humidity_file = 'chart_json/humidity.json'
    
    def write_temp():
        with open(temp_file, 'w') as f:
            json.dump(temp_list, f)
                
    def write_humidity():        
        with open(humidity_file, 'w') as f:
            json.dump(humidity_list, f)

    def write_files():
        write_temp()
        write_humidity()
      
    if os.path.isfile(temp_file):
        with open(temp_file, 'r') as D:
            temp_list = json.load(D)
    else:
        temp_list = []
        write_temp()
        
    if os.path.isfile(humidity_file):
        with open(humidity_file, 'r') as V:
            humidity_list = json.load(V)
    else:
        humidity_list = []
        write_humidity()
        
    def display_data(fahrenheit, h):
        print('Temperature: ' + str(fahrenheit) + 'F \n' + 'Humidity: ' + str(h) + '%')
        
    def on_connect(client, userdata, flags, rc):
        client.subscribe('temp_humidity')
        
    def on_message(client, userdata, msg):
    
        fahrenheit, h = [float(x) for x in msg.payload.decode("utf-8").split(',')]
        
        temp_list.append(fahrenheit)
        humidity_list.append(h)
        
        display_data(fahrenheit, h)
        
        #derp_time = strftime("%H:%M:%S")
        #time_list.append(derp_time)
        chart = pygal.Line(x_label_rotation=45)
        chart.title = 'Bedroom Temperature/Humidity'
        #chart.x_labels = time_list
        chart.add('Temps in °F', temp_list)
        chart.add('Humidity in %', humidity_list)
        chart.render_to_file('../static/climate/chart.svg')    
        write_files()
            
        sleep(1800)
        #sleep(5)
          
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect('localhost', 1883, 60)
            
    client.loop_forever()
        
        
