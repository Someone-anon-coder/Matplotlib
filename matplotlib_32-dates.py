import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime, timedelta

dates = [datetime(2024, 10, 14) + timedelta(days=i) for i in range(5)]
values = [5, 7, 8, 6, 7]

plt.plot(dates, values)

plt.tight_layout()
plt.savefig("Plots/fig_with_dates.png")
plt.clf()

import matplotlib.dates as mdates

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(dates, values)

ax.xaxis.set_major_locator(mdates.AutoDateLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d, %Y'))

plt.gcf().autofmt_xdate()

plt.tight_layout()
plt.savefig("Plots/fig_with_dates_custom.png")
plt.clf()