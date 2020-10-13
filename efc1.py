# imports
import csv
import matplotlib.pyplot as plt
import numpy as np

# abre arquivo com os dados
file = open("monthly-sunspots.csv")
csv_data = csv.reader(file)
# ignora o cabecalho do arquivo
next(csv_data, None)

# cria os arrays de treino e teste vazios
training_data = np.empty((0,2))
testing_data = np.empty((0,2))

# itera sobre o csv e guarda os dados num array
for line in csv_data:
    index, date, value = line

    newLine = [int(index), float(value)]
    
    year = int(date[:4])
    # separa os dados mais novos para teste
    if year >= 2010:
        testing_data = np.concatenate((testing_data, [newLine]), axis=0)
    else:
        training_data = np.concatenate((training_data, [newLine]), axis=0)

plt.plot(training_data[:,1])
plt.show()