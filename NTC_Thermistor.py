import csv
import math

def resistance_to_temperature(resistance, beta, nominal_resistance):
    return (1.0 / (math.log(resistance / nominal_resistance) / beta + 1 / 298.15) - 273.15)

def temperature_to_resistance(temperature, beta, nominal_resistance):
    return nominal_resistance * math.exp(beta * (1 / (temperature + 273.15) - 1 / 298.15))

def generate_ntc_data(beta, nominal_temp, nominal_resistance, start_temp, end_temp, step):
    data = []
    for temp in range(start_temp, end_temp + 1, step):
        resistance = temperature_to_resistance(temp, beta, nominal_resistance)
        data.append([temp, resistance / 1000.0])  # Convert resistance to kilohms
    return data

def save_to_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Temperature (C)', 'Resistance (Kohms)'])
        writer.writerows(data)

# Thermistor parameters
beta = 4092
nominal_temp = 25  # in Celsius
nominal_resistance = 85 * 1000  # Convert to ohms

# Generate data
start_temp = -25
end_temp = 135
step = 1
ntc_data = generate_ntc_data(beta, nominal_temp, nominal_resistance, start_temp, end_temp, step)

# Save data to CSV
csv_filename = 'ntc_thermistor_data.csv'
save_to_csv(csv_filename, ntc_data)

print(f"CSV data has been generated and saved to '{csv_filename}'.")
