from csv import reader
from time import sleep
import numpy as np
from sklearn.manifold import TSNE



class ReadDataAndMakeVariances():

    def __init__(self, file_path):
        self.file_path = file_path
        self.all_lists_with_splited_foats = []
        self.all_measurements_of_one_distance = []
        self.variances_list = []

    def open_data_file(self):
        self.data_file = open(self.file_path, 'r')
        return self.data_file

    def read_data_file(self):
        self.data_file_read = reader(self.data_file)
        return self.data_file_read

    def make_list_of_foats(self):
        for row in self.data_file_read:
            for i in row:
                single_number_as_string_list = i.split(" ")
                self.distances_list = single_number_as_string_list[6:]
                single_number_as_float_list = [float(j) for j in self.distances_list]
                self.all_lists_with_splited_foats.append(single_number_as_float_list)

    def make_all_variances(self):
        for i in range(len(self.distances_list)):
            for j in self.all_lists_with_splited_foats:
                self.all_measurements_of_one_distance.append(j[i])
            single_variance = np.var(self.all_measurements_of_one_distance)
            self.variances_list.append(single_variance)

    def cut_column_if_variance_smaller_than_2e4(self):
        for i in self.variances_list:
            if i < 2e-4:
                _index_to_cut = self.variances_list.index(i)
                print(f'variance no. {_index_to_cut + 1} was smaller than 2e-4 nm^2, it was removed')
                for row in self.all_lists_with_splited_foats:
                    row.pop(_index_to_cut)
        return self.all_lists_with_splited_foats

    def put_data_into_txt_files(self):
        self.file_1 = 'data_300K_txt.txt'
        self.world_map_file_1 = open(self.file_1, 'w')
        self.world_map_file_1.write(str(self.data_file_read))

        self.file_2 = 'all_lists_with_splited_foats.txt'
        self.world_map_file_2 = open(self.file_2, 'w')
        self.world_map_file_2.write(str(self.all_lists_with_splited_foats))

        self.file_3 = 'iterowanie.txt'
        self.world_map_file_3 = open(self.file_3, 'w')
        self.world_map_file_3.write(str(self.all_measurements_of_one_distance))

        self.file_4 = 'variances_list.txt'
        self.world_map_file_4 = open(self.file_4, 'w')
        self.world_map_file_4.write(str(self.variances_list))

        
    def close_data_files(self):
        self.data_file.close()
        self.world_map_file_1.close()
        self.world_map_file_2.close()
        self.world_map_file_3.close()
        self.world_map_file_4.close()


class Training():
    
    def __init__(self):
        pass

    def make_training(self, training_data):
        tsne = TSNE(n_components=2, random_state=0)
        results = tsne.fit_transform(training_data)
        return results


class Main():

    def __init__(self, file_path):
        print("Reading data:", end = "")
        self.read_data(file_path)
        print(f"{len(self.training_data_list)} rows")
        print("Training:")
        self.train()
        print(f"{len(self.results)} points")
        self.save_results(self.results, "result.txt")

    def read_data(self, file_path):
        data_read = ReadDataAndMakeVariances(file_path)
        data_read.open_data_file()
        data_read.read_data_file()
        data_read.make_list_of_foats()
        data_read.make_all_variances()
        self.training_data_list = data_read.cut_column_if_variance_smaller_than_2e4()
        data_read.put_data_into_txt_files()
        data_read.close_data_files()

    def train(self):
        tsne = Training()
        self.results = tsne.make_training(self.training_data_list)
        
    def save_results(self, results, file_path):
        print(f"Writing to file '{file_path}': ", end = "")
        with open(file_path, "w") as outputfile:
            for idx, point in enumerate(results):
                if idx % 1000 == 0:
                    print(".", end="")
                outputfile.write(f"{point[0]} {point[1]}\n")
        print("DONE")




if __name__ == "__main__":
    main = Main('dialanine-300K.data')

# simple_file.data
# 'dialanine-300K.data'
