from csv import reader

lista_rows = []


# URL_DATASET = r'dialanine-300K.csv'
# cov_19_data_frame = pd.read_csv(URL_DATASET)

# for rows in cov_19_data_frame:
#     for row in rows:
#         lista_rows.append(row)



# print(cov_19_data_frame)
# print(lista_rows)


# open file in read mode
with open('probnik.csv', 'r') as data_base:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(data_base)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        for i in row[1:]:
            print(i.split(" "))
            # print(row)
