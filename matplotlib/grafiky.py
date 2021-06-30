import matplotlib.pyplot as plt

plt.figure()

plt.xlabel('Champ')
plt.ylabel('Kills')
plt.title('Kills by Champs')

lines = plt.plot(['Lux', 'Le Blanc', 'Xayah', 'Karma'], [2, 6, 11, 8])
plt.show()
