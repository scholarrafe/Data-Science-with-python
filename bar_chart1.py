import matplotlib.pyplot as plt

movies = ["Captain", "Opiri", "inception", "intersteller", "taken", "intochables"]
num_oscar = [5, 8, 6, 12, 4, 7]

plt.bar(range(len(movies)), num_oscar, color='purple')

plt.title("My Favourite Movies")
plt.xticks(range(len(movies)), movies)
plt.show()

