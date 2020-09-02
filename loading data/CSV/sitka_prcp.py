import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # чтение дат и ежедневных осадков(precipitation)
    dates, prcps = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            prcp = float(row[3])
        except ValueError:
            print(f"Missing PRCP for {current_date}")
        else:
            prcps.append(prcp)
            dates.append(current_date)

# нанесение данных на диаграмму
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, prcps, c='green')

# форматирование диграммы
plt.title("Daily PRCP - 2018", fontsize=20)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('PRCP, mm', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
