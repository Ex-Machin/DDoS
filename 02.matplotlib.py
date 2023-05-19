import matplotlib.pyplot as plt
import csv
import datetime

filename = 'month.csv'

with open(filename, 'r') as file:
    reader = csv.reader(file)
    header_row = next(reader)
    print(header_row)

    dates, tmax, tmin = [], [], []

    for row in reader:
        tmax.append(int(row[5]))
        tmin.append(int(row[6]))
        dates.append(datetime.datetime.strptime(row[2], '%Y-%m-%d'))

    fig, ax = plt.subplots()
    ax.plot(dates, tmax, color = 'red')
    ax.plot(dates, tmin, color="blue")
    ax.set_title("Najwyżscze i najniższe temperatury w lipcu 2018")
    ax.set_ylabel("Temperatury F")
    ax.grid(True)

    fig.autofmt_xdate()

    plt.show()