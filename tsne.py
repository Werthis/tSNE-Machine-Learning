from csv import reader
import numpy as np


class TSNE():

    def __init__(self):
        self.all_lists_with_splited_strings = []
        self.all_distances_sorted = []
        self.variances_list = []

    def open_data_file(self):
        self.data_file = open('probnik.csv', 'r')
        return self.data_file

    def read_data_file(self):
        self.data_file_read = reader(self.data_file)
        return self.data_file_read

    def get_one_row(self):
        for row in self.data_file_read:
            for i in row:
                single_number_list = i.split(" ")
                self.only_distances_list = single_number_list[6:]
                self.all_lists_with_splited_strings.append(self.only_distances_list)
        # print(self.all_lists_with_splited_strings)
        # print(len(self.only_distances_list))

    def iterate(self):
        for i in range(len(self.only_distances_list) - 1):
            for j in self.all_lists_with_splited_strings:
                self.all_distances_sorted.append(float(j[i]))
            # self.all_distances_sorted.append('|||||||||||||')
            single_variance = np.var(self.all_distances_sorted)
            self.variances_list.append(single_variance)
        print(self.variances_list)
        

    def make_array(self):
        arr = np.array(self.all_lists_with_splited_strings)
        # print(arr)
        return arr

    def put_data_into_txt(self):
        self.file_1 = 'data_300K_txt.txt'
        self.world_map_file_1 = open(self.file_1, 'w')
        self.world_map_file_1.write(str(self.data_file_read))
        self.world_map_file_1.close()

        self.file_2 = 'all_lists_with_splited_strings.txt'
        self.world_map_file_1 = open(self.file_2, 'w')
        self.world_map_file_1.write(str(self.all_lists_with_splited_strings))
        self.world_map_file_1.close()

        self.file_3 = 'iterowanie.txt'
        self.world_map_file_1 = open(self.file_3, 'w')
        self.world_map_file_1.write(str(self.all_distances_sorted))
        self.world_map_file_1.close()

        self.file_4 = 'variances_list.txt'
        self.world_map_file_1 = open(self.file_4, 'w')
        self.world_map_file_1.write(str(self.variances_list))
        self.world_map_file_1.close()

        

    def close_data_file(self):
        return self.data_file.close()

        
if __name__ == "__main__":
    program = TSNE()
    program.open_data_file()
    program.read_data_file()
    program.get_one_row()

    program.iterate()

    program.make_array()
    program.put_data_into_txt()

    program.close_data_file()
