import obd
import time


print("Vehicle Telemetry System Starting...")

connection = obd.OBD("COM3", fast=False)  # auto-connects to USB or Bluetooth OBD-II adapter

if connection.is_connected():
    print("Connected to vehicle system!")

    while True:
        rpm = connection.query(obd.commands.RPM)  # query RPM
        speed = connection.query(obd.commands.SPEED)  # query Speed

        rpm_value = rpm.value.magnitude if rpm.value else 0
        speed_value = speed.value.magnitude if speed.value else 0

        print(f"RPM: {rpm_value:>6} | Speed: {speed_value}")

        time.sleep(1)  # wait for 1 second before the next query

else:
    print("Failed to connect to vehicle system. Please check your OBD-II adapter and try again.")
