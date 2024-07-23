import time
import csv
import board
import busio
from adafruit_ina219 import INA219

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the INA219 sensor
ina219 = INA219(i2c)

# File to save the data
output_file = "/app/ina219_data.csv"

def log_data():
    # Open the CSV file and write the headers
    with open(output_file, "w", newline='') as csvfile:
        fieldnames = ["Index", "Bus Voltage (V)", "Shunt Voltage (mV)", "Load Voltage (V)", "Current (mA)", "Power (mW)"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for index in range(1, 1801):  # Collect data for 30 minutes (1800 measurements, one per second)
            # Read voltage and power
            bus_voltage = ina219.bus_voltage  # voltage on V- (load side)
            shunt_voltage = ina219.shunt_voltage  # voltage between V+ and V- across the shunt
            current = ina219.current  # current in mA
            power = ina219.power  # power in mW

            # Calculate the load voltage
            load_voltage = bus_voltage + (shunt_voltage / 1000)

            # Write the data to the CSV file
            writer.writerow({
                "Index": index,
                "Bus Voltage (V)": bus_voltage,
                "Shunt Voltage (mV)": shunt_voltage,
                "Load Voltage (V)": load_voltage,
                "Current (mA)": current,
                "Power (mW)": power
            })

            # Wait for one second before taking the next reading
            time.sleep(1)

if __name__ == "__main__":
    log_data()
