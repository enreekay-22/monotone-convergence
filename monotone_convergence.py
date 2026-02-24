# ================================================
# MONOTONE CONVERGENCE 
# Straight slanted line version (uniform linear steps)
# Pure Python — only matplotlib needed
# ================================================

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# ------------------- Parameters -------------------
n_steps = 30                                   # number of iterations
limit = 1.0                                    # convergence limit

# Monotonically INCREASING straight line
start_inc = 0.25
a_n = [start_inc + (limit - start_inc) * i / (n_steps - 1) for i in range(n_steps)]

# Monotonically DECREASING straight line
start_dec = 1.75
b_n = [start_dec + (limit - start_dec) * i / (n_steps - 1) for i in range(n_steps)]

n = list(range(1, n_steps + 1))

# ------------------- Plot -------------------
fig, axs = plt.subplots(1, 2, figsize=(15, 7), dpi=140, facecolor='white')

# LEFT: Increasing
axs[0].plot(n, a_n, 'o-', color='#1f77b4', markersize=8, linewidth=3.2,
            label=r'Increasing sequence $a_n$')
axs[0].axhline(y=limit, color='red', linestyle='--', linewidth=3, label=f'Limit = {limit}')
for i in [0, 5, 10, 15, 20, 25, 29]:
    axs[0].annotate(f'{a_n[i]:.3f}', xy=(n[i], a_n[i]), xytext=(0, 14),
                    textcoords='offset points', ha='center', va='bottom',
                    fontsize=10, bbox=dict(boxstyle='round,pad=0.4', fc='white', ec='#1f77b4', alpha=0.9))

axs[0].set_title('Monotonically INCREASING\nStraight Slanted Line', fontsize=15, fontweight='bold', pad=20)
axs[0].set_xlabel('Iteration (n)', fontsize=13)
axs[0].set_ylabel('Sequence Value', fontsize=13)
axs[0].set_ylim(0.15, 1.08)
axs[0].legend(loc='lower right', fontsize=12)
axs[0].grid(True, linestyle='--', alpha=0.75)
axs[0].xaxis.set_major_locator(MultipleLocator(5))
axs[0].yaxis.set_major_locator(MultipleLocator(0.2))

# RIGHT: Decreasing
axs[1].plot(n, b_n, 'o-', color='#d62728', markersize=8, linewidth=3.2,
            label=r'Decreasing sequence $b_n$')
axs[1].axhline(y=limit, color='red', linestyle='--', linewidth=3, label=f'Limit = {limit}')
for i in [0, 5, 10, 15, 20, 25, 29]:
    axs[1].annotate(f'{b_n[i]:.3f}', xy=(n[i], b_n[i]), xytext=(0, -18),
                    textcoords='offset points', ha='center', va='top',
                    fontsize=10, bbox=dict(boxstyle='round,pad=0.4', fc='white', ec='#d62728', alpha=0.9))

axs[1].set_title('Monotonically DECREASING\nStraight Slanted Line', fontsize=15, fontweight='bold', pad=20)
axs[1].set_xlabel('Iteration (n)', fontsize=13)
axs[1].set_ylabel('Sequence Value', fontsize=13)
axs[1].set_ylim(0.92, 1.82)
axs[1].legend(loc='upper right', fontsize=12)
axs[1].grid(True, linestyle='--', alpha=0.75)
axs[1].xaxis.set_major_locator(MultipleLocator(5))
axs[1].yaxis.set_major_locator(MultipleLocator(0.2))

plt.suptitle('Monotone Convergence Theorem\n'
             'Uniform Straight Slanted Lines (Increasing vs Decreasing)',
             fontsize=17, fontweight='bold', y=1.02)
plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.savefig('monotone_convergence_plot.png', dpi=400, bbox_inches='tight', facecolor='white')
print("✅ Plot saved as 'monotone_convergence_plot.png'")
plt.show()
