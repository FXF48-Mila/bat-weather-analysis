import csv

# The txt data is downloaded from:
# url = "https://svs.gsfc.nasa.gov/vis/a000000/a004900/a004955/mooninfo_2022.txt"

# Specify the text file path
txt_file_path = "mooninfo_2022.txt"

# Specify the output csv file path
csv_file_path = "NASA_mooninfo_2022.csv"

with open(txt_file_path, "r") as input_file:
    lines = input_file.readlines()

with open(csv_file_path, "w", newline='') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(["Date", "Time", "Phase", "Age", "Diam", "Dist", "RA", "Dec", "Slon", "Slat", "Elon", "Elat", "AxisA"])

    for line in lines[1:]:
        date = line[0:17].strip()
        columns = [date] + line[18:].strip().split()
        csv_writer.writerow(columns)

print(csv_file_path)