import csv
import string

rows = []
cod = []
action = []
tipo = []
qtd_Teorica = []
part = []

with open("att_Dia\IBOVDia_27-06-22.csv", 'r') as file:

    # Cria reader object ao passar o arquivo
    # Envia para o método DictReader
    csvreader = csv.DictReader(file)

    # Pula o header
    header = next(csvreader)

    # Iteração por cada linha do arquivo csv
    for row in csvreader:
        print(row)
        # cod.append(row[0])


# print(header)
# print(rows)
# print(cod)
