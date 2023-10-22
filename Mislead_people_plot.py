from matplotlib import pyplot as plt

mentions = [500, 505]
years = [2017, 2018]

plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("number of times I heard about Data Science")
plt.xlabel("Year")
plt.title("Look at the Huge increase within a year")
plt.axis([2016.5, 2018.5, 499.5, 506])
plt.xticks(years)
plt.show()