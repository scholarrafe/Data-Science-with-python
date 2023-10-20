    

from matplotlib import pyplot as plt
import random


run = [i for i in range(20)]
over = [i+1 for i in range(50)]
runs = random.choices(run, k=50)
print(f"Total Runs : {sum(runs)}({len(over)})")

plt.bar(over, runs, 1, edgecolor=(1, 0, 1))
plt.axis([1, 50, 0, 25])
plt.xticks([i*5 for i in range(11)])
plt.xlabel("Overs", fontsize=15, color='purple', weight='bold', fontstyle='oblique')
plt.ylabel("Runs", fontsize=15, color='purple', weight='bold', fontstyle='oblique')
plt.title("Runs per Over", fontsize=20, color='purple', weight='bold', fontstyle='oblique')
plt.show()

