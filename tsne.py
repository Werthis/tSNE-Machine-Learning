from csv import reader
import numpy as np
from sklearn.datasets import load_digits


class ReadAndTransformData():

    def __init__(self):
        self.all_lists_with_splited_strings = []
        self.all_measurements_of_one_distance = []
        self.variances_list = []

    def open_data_file(self):
        self.data_file = open('dialanine-300K.data', 'r')
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

    def make_all_vaiances(self):
        for i in range(len(self.only_distances_list)):
            for j in self.all_lists_with_splited_strings:
                self.all_measurements_of_one_distance.append(float(j[i]))
            # self.all_measurements_of_one_distance.append('|||||||||||||')
            single_variance = np.var(self.all_measurements_of_one_distance)
            self.variances_list.append(single_variance)
        
    def cut_variances_smaller_than_2e4(self):
        for i in self.variances_list:
            if i < 2e-4:
                _index = self.variances_list.index(i) + 1
                print(f'variance no. {_index} was smaller than 2e-4 nm^2, it was removed')
                self.variances_list.remove(i)
        print('\n', self.variances_list, '\n', len(self.variances_list))

    # def make_array(self):
    #     arr = np.array(self.all_lists_with_splited_strings)
    #     # print(arr)
    #     return arr

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
        self.world_map_file_1.write(str(self.all_measurements_of_one_distance))
        self.world_map_file_1.close()

        self.file_4 = 'variances_list.txt'
        self.world_map_file_1 = open(self.file_4, 'w')
        self.world_map_file_1.write(str(self.variances_list))
        self.world_map_file_1.close()

        

    def close_data_file(self):
        return self.data_file.close()



class TSNE():

    def __init__(self):
        pass



class Main():

    def __init__(self):
        self.read_data()

    def read_data(self):
        data_read = ReadAndTransformData()
        data_read.open_data_file()
        data_read.read_data_file()
        data_read.get_one_row()
        data_read.make_all_vaiances()
        data_read.cut_variances_smaller_than_2e4()
        data_read.put_data_into_txt()
        data_read.close_data_file()

        
if __name__ == "__main__":
    main = Main()
