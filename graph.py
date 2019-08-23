import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
n = 1

rs_parquet = (1.09)
rs_json = (13.81 )

triple_parquet = (1.12)
triple_json = (4.08)


fig, ax = plt.subplots()
ax.set_facecolor('xkcd:white')
index = np.arange(n)
bar_width = 0.10
opacity = 0.99
rects1 = ax.bar(index, rs_parquet, bar_width, alpha=opacity, color='#6cbdbd',
                label='EC RS(6,3)')
rects3 =ax.bar(index+bar_width, triple_parquet, bar_width, alpha=opacity, color='#6060b5',
                label='3x replication')


rects2 =ax.bar(index+bar_width+bar_width+bar_width, rs_json, bar_width, alpha=opacity, color='#6cbdbd')

rects4 =ax.bar(index+bar_width+bar_width+bar_width+bar_width, triple_json , bar_width, alpha=opacity, color='#6060b5')


ax.set_xlabel('File format')
ax.set_ylabel('Elapsed time in hours')
ax.set_title('TPC-DS benchmark test on 3X & EC RS(6,3), 1TB\n(Lower is better) ')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('', 'JSON'))

def autolabel(rects):

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.0*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects3)
autolabel(rects2)
autolabel(rects4)


ax.legend()
plt.show()

''' 
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
n = 2
rs= (15.69,65.66 )
triple_rep = (16.53, 67.31)
fig, ax = plt.subplots()
index = np.arange(n)
bar_width = 0.20
opacity = 0.9
ax.bar(index, rs, bar_width, alpha=opacity, color='r',
                label='EC RS(6,3)')
ax.bar(index+bar_width, triple_rep, bar_width, alpha=opacity, color='b',
                label='3x replication')
ax.set_xlabel('File size')
ax.set_ylabel('Elapsed time in minutes')
ax.set_title('TPCDS benchmark test on 3X & EC RS(6,3) in Parquet format')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('100GB', '1TB'))
ax.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
missing_blocks = (24,384, 1562)
recovery_time = (1,18,91)



# Plot the data
fig = plt.figure()
plt.plot(missing_blocks, recovery_time, label='EC RS(6,3)')

fig.suptitle('Time of Recovery', fontsize=18)
plt.xlabel('Missing blocks', fontsize=16)
plt.ylabel('Time (s)', fontsize=16)
# Add a legend
plt.legend()

# Show the plot
plt.show()



'''
