from csv import reader
import numpy as np



with open('probnik.csv', 'r') as data_base:
    distances_foat_list = []
    lista_var = []

    csv_reader = reader(data_base)
    for row in csv_reader:
        for i in row:
            single_number_list = i.split(" ")
            only_distances_list = single_number_list[6:]

            for j in only_distances_list:
                a = float(j)
                distances_foat_list.append(a)
        print(distances_foat_list)
                                #ZAMIEŃ NA TYP FLOAT
            # arr = np.array(distances_foat_list)
            # # print(arr)
            # variance = np.var(arr, ddof=1)
            # print(variance)
            # # lista_var.append(variance)
            # print(lista_var)
            # for j in only_distances_list:
            #     pass

file_name = 'distances_foat_list.txt'
distances_foat_list_file_1 = open(file_name, 'w')
distances_foat_list_file_1.write(str(distances_foat_list))
distances_foat_list_file_1.close()

                
print(len(single_number_list[6:]))
