from csv import reader
import numpy as np


class TSNE():

    def __init__(self):
        self.all_lists_with_splited_strings = []

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
                only_distances_list = single_number_list[6:]
                self.all_lists_with_splited_strings.append(only_distances_list)
        # print(self.all_lists_with_splited_strings)

    def make_array(self):
        arr = np.array(self.all_lists_with_splited_strings)
        print(arr)
        return arr

    def put_data_into_txt(self):
        self.file_name = 'data_300K_txt.txt'
        self.world_map_file_1 = open(self.file_name, 'w')
        self.world_map_file_1.write(str(self.data_read))
        self.world_map_file_1.close()



    def close_data_file(self):
        return self.data_file.close()

        
if __name__ == "__main__":
    program = TSNE()
    program.open_data_file()
    program.read_data_file()
    program.get_one_row()
    program.make_array()


    program.close_data_file()
