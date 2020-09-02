import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data/san_francisco_2020.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # определение индексов столбцов с датой и температурами 
    for index, column in enumerate(header_row):
        if column == 'TMIN':
            index_low = index
        if column == 'TMAX':
            index_high = index
        if column == 'DATE':
            index_date = index

    # извлечение дат, температурных максимумов и минимумов
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[index_date], '%Y-%m-%d')
        try:
            high = int(row[index_high])
            low = int(row[index_low])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# построение диаграммы
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# форматирование диаграммы
plt.title('San Francisco-2020', fontsize=22)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()