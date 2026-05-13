print("Vehicle Telemetry System Starting...")

import obd

connection = obd.OBD()  # auto-connects to USB or Bluetooth OBD-II adapter

print("Connected to vehicle system!")

cmd = obd.commands.RPM  # select an OBD command (RPM in this case)
response = connection.query(cmd)  # send the command and parse the response

print("RPM:", response.value)  # print the RPM value