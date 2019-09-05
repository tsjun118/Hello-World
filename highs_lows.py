import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

filename = r"C:\Users\14326\Desktop\mat\death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(date, "missing data")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(date)


"""绘图"""
fig = plt.figure(figsize=(15, 9))
plt.plot(dates, highs, c='red', linewidth=2, alpha = 0.5)
plt.plot(dates, lows, c = 'blue', linewidth = 2, alpha = 0.5)
plt.fill_between(dates, lows, highs, facecolors = 'blue', alpha = 0.1)
plt.title('Daily high temperatures -2014', fontsize=24)

"""对x轴坐标操作"""
plt.xlabel(" ", fontsize=14)
plt.xlim(datetime(2014, 1, 1), datetime(2014, 12, 22)) #设置坐标轴上下限
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y')) #设置日期格式
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval = 30))   #设置日期间隔
fig.autofmt_xdate()  #将x轴的日期横坐标倾斜显示，以免重叠

"""对y轴坐标操作"""
plt.ylabel("Temperatures (F)", fontsize=14)
plt.yticks(range(10,80,10))
plt.tick_params(axis='both', which='major', direction = 'in', labelsize=16)

plt.savefig('Daily high and low temperatures -2014', bbox_inches = 'tight')
plt.show()  #渲染图
