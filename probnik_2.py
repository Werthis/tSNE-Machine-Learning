from csv import reader
import numpy as np



with open('probnik.csv', 'r') as data_base:
    lista_var = []

    csv_reader = reader(data_base)
    for row in csv_reader:
        for i in row:
            single_number_list = i.split(" ")
            # print(single_number_list)
            only_distances_list = single_number_list[6:]
            arr = np.array(only_distances_list)
            print(arr)
            # variance = np.var(arr, ddof=1)
            # print(variance)
            # # lista_var.append(variance)
            # print(lista_var)
            for j in single_number_list[5:]:
                pass
                
    print(len(i.split(" ")))
