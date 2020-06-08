import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import (axes, axis, title, legend, figure,
                               xlabel, ylabel, xticks, yticks,
                               xscale, yscale, text, grid,
                               plot, scatter, errorbar, hist, polar,
                               contour, contourf, colorbar, clabel,
                               imshow)
from mpl_toolkits.mplot3d import Axes3D
from numpy import (linspace, logspace, zeros, ones, outer, meshgrid,
                   pi, sin, cos, sqrt, exp)
from numpy.random import normal


plt.style.use('bmh')

fig, axs = plt.subplots(2, 4, figsize=(15, 5), tight_layout=True)

fig.suptitle('Heading', fontsize=80, verticalalignment='baseline',
             color='white')

# I
axs[0, 0].text(-1, 8.5, 'B', fontsize=28, fontweight='bold')

x1 = normal(-1, 1, 1000)
y1 = normal(2, 1, 1000)
axs[0, 0].boxplot([x1, y1])

axs[0, 0].set_ylabel('boxplot', fontsize=12)

axs[0, 0].yaxis.set_ticks(np.arange(-5, 11, 5))
axs[0, 0].yaxis.set_ticklabels([5, 0, 5, 10])
axs[0, 0].xaxis.set_ticklabels(['first box', 'second box'],
                               fontsize=10, rotation=45)
axs[0, 0].axis([0, 3, -5, 10])

# II
axs[0, 1].text(-1.2, 360, 'C', fontsize=28, fontweight='bold')
axs[0, 1].text(-0.5, 355, '(i)', fontsize=14)

axs[0, 1].set_ylabel('graph 1', fontsize=12)

axs[0, 1].yaxis.set_ticks(np.arange(0, 401, 100))
axs[0, 1].xaxis.set_ticks(np.arange(1, 8))
axs[0, 1].xaxis.set_ticklabels(['$C_{a}$', 'ab', 'abc', 'ab', 'abc'],
                               fontsize=12)

axs[0, 1].axis([0.8, 5.5, 0, 400])

axs[0, 1].errorbar(np.arange(1, 6), [350, 290, 295, 280, 290], lw=2,
                   elinewidth=1, capsize=3, marker='o', color='darkorange',
                   yerr=20*ones(5), markersize=9)
axs[0, 1].errorbar(np.arange(1, 6), [250, 190, 175, 180, 190], lw=2,
                   elinewidth=1, capsize=3, marker='o',
                   markerfacecolor='white', color='darkorange',
                   yerr=20*ones(5), markersize=9)

# III
axs[0, 2].text(-1, 13, '(ii)', fontsize=14)

axs[0, 2].set_ylabel('graph 2', fontsize=12)

axs[0, 2].yaxis.set_ticks(np.arange(0, 16, 5))
axs[0, 2].xaxis.set_ticks(np.arange(1, 5))
axs[0, 2].xaxis.set_ticklabels(['$C_{a}$', 'ab', 'abc', 'ab'], fontsize=12)

axs[0, 2].axis([0.7, 4.5, 0, 15])
axs

axs[0, 2].errorbar(np.arange(1, 5, 1), [5, 10, 11, 10], lw=2, elinewidth=1,
                   capsize=3, marker='o', color='darkorange', yerr=0.7*ones(4),
                   markersize=9)
axs[0, 2].errorbar(np.arange(1, 5, 1), [4, 9, 6, 8.5], lw=2, elinewidth=1,
                   capsize=3, marker='o', markerfacecolor='white',
                   color='darkorange', yerr=0.7*ones(4), markersize=9)

# IV
axs[0, 3].text(-1, 13, '(iii)', fontsize=14)

axs[0, 3].set_ylabel('graph 3', fontsize=12)


axs[0, 3].yaxis.set_ticks(np.arange(0, 16, 5))
axs[0, 3].xaxis.set_ticks(np.arange(1, 8))
axs[0, 3].xaxis.set_ticklabels([0, 1, 2, 3, 4, 5, 6], fontsize=12)
axs[0, 3].axis([0.7, 6.5, 0, 15])

axs[0, 3].errorbar(np.arange(1, 8), [0, 5, 7, 8, 8.5, 9.5, 10], lw=2,
                   elinewidth=1, capsize=5, marker='o', color='darkorange',
                   yerr=1*ones(7), markersize=9, zorder=1)
axs[0, 3].errorbar(np.arange(1, 8), [0, 4, 6, 6.5, 7.5, 7.8, 9], lw=2,
                   elinewidth=1, capsize=5, marker='o',
                   markerfacecolor='white', color='darkorange', yerr=1*ones(7),
                   markersize=9, zorder=2)

# V
axs[1, 0].text(0.51, 5.6, '(iv)', fontsize=14)

axs[1, 0].yaxis.set_ticks(np.arange(0, 7, 2))
axs[1, 0].xaxis.set_ticks([])
axs[1, 0].axis([0.7, 1.3, 0, 6])

axs[1, 0].set_ylabel('errorbar', fontsize=12)

axs[1, 0].errorbar([1], [4], lw=2, elinewidth=1,
                   capsize=5, marker='o', color='darkorange', yerr=1*ones(1),
                   markersize=9)
axs[1, 0].errorbar([1], [2], lw=2, elinewidth=1,
                   capsize=5, marker='o', markerfacecolor='white',
                   color='darkorange', yerr=0.4*ones(1), markersize=9)

# VI
axs[1, 1].text(-2, 380, '(v)', fontsize=14)

axs[1, 1].set_ylabel('graph 5', fontsize=12)

axs[1, 1].yaxis.set_ticks(np.arange(0, 401, 100))
axs[1, 1].xaxis.set_ticks(np.arange(1, 8))
axs[1, 1].xaxis.set_ticklabels([0, 1, 2, 3, 4, 5, 6], fontsize=10)
axs[1, 1].axis([0.7, 7.5, 0, 400])

axs[1, 1].errorbar(np.arange(1, 8), [50, 100, 135, 190, 220, 250, 300], lw=2,
                   elinewidth=1, capsize=5, marker='o', color='darkorange',
                   yerr=20*ones(7), markersize=9, zorder=1,
                   label='Dark-orange with face')
axs[1, 1].errorbar(np.arange(1, 8), [45, 85, 110, 125, 150, 190, 225], lw=2,
                   elinewidth=1, capsize=5, marker='o', color='lightblue',
                   yerr=20*ones(7), markersize=9, zorder=0,
                   label='Light-blue plot')
axs[1, 1].errorbar(np.arange(1, 8), [40, 70, 85, 95, 110, 135, 175], lw=2,
                   elinewidth=1, capsize=5, marker='o',
                   markerfacecolor='white', color='darkorange',
                   yerr=20*ones(7), markersize=9, zorder=2,
                   label='Dark-orange without face')

# VII
axs[1, 2].text(-1.3, 95, '(vi)', fontsize=14)

axs[1, 2].set_ylabel('graph 6', fontsize=12)

axs[1, 2].yaxis.set_ticks(np.arange(0, 101, 20))
axs[1, 2].xaxis.set_ticks(np.arange(1, 6))
axs[1, 2].xaxis.set_ticklabels([0, 6, 12, 18, 24], fontsize=10)
axs[1, 2].axis([0.7, 5.5, 0, 100])

axs[1, 2].errorbar(np.arange(1, 6), [15, 37, 65, 70, 72], lw=2, elinewidth=1,
                   capsize=5, marker='o', color='darkorange', yerr=5*ones(5),
                   markersize=9)
axs[1, 2].errorbar(np.arange(1, 6), [7, 15, 25, 30, 35], lw=2, elinewidth=1,
                   capsize=5, marker='o', markerfacecolor='white',
                   markersize=9, color='darkorange', yerr=5*ones(5))

# VIII
axs[1, 3].text(-0.3, 740, '(vii)', fontsize=14)

axs[1, 3].set_ylabel('graph 7', fontsize=12)

axs[1, 3].yaxis.set_ticks(np.arange(0, 801, 200))
axs[1, 3].xaxis.set_ticks([0.5, 1.5])
axs[1, 3].xaxis.set_ticklabels(['Q', 'second'],
                               fontsize=10)
axs[1, 3].axis([0.3, 1.8, 0, 800])

axs[1, 3].errorbar([0.5, 1.5], [250, 700], lw=2, elinewidth=1,
                   capsize=3, marker='o', color='darkorange', yerr=70*ones(2),
                   markersize=9)
axs[1, 3].errorbar([0.5, 1.5], [200, 400], lw=2, elinewidth=1,
                   capsize=3, marker='o', markerfacecolor='white',
                   color='darkorange', yerr=40*ones(2), markersize=9)

fig.legend(fontsize=15,
           ncol=2,
           facecolor='w',
           edgecolor='w',
           loc='upper center')

plt.show()
