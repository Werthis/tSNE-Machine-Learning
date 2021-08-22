from csv import reader
import numpy as np
from sklearn.manifold import TSNE


class ReadDataAndCheckVariances():

    def __init__(self, file_path):
        self.file_path = file_path
        self.all_lists_with_splited_foats = []
        self.all_measurements_of_one_distance = []
        self.variances_list = []
        self.time_list = []
        self.phi_psi_list = []
        self.psi_list = []

    def open_data_file(self):
        self.data_file = open(self.file_path, 'r')
        return self.data_file

    def read_data_file(self):
        self.data_file_read = reader(self.data_file)
        return self.data_file_read

    def iterate_on_rows(self):
        for row in self.data_file_read:
            for element in row:
                self.row_as_string_list = element.split(" ")
                self._make_time_list()
                self._make_phi_psi_list()
                self._make_all_lists_with_splited_foats()
    
    def _make_time_list(self):
        time = self.row_as_string_list[1]
        return self.time_list.append(time)

    def _make_phi_psi_list(self):
        phi = self.row_as_string_list[3]
        psi = self.row_as_string_list[4]
        return self.phi_psi_list.append([phi, psi])

    def _make_all_lists_with_splited_foats(self):
        self.one_row_distances_list = self.row_as_string_list[6:]
        distances_from_one_row_as_float_list = [float(j) for j in self.one_row_distances_list]
        return self.all_lists_with_splited_foats.append(distances_from_one_row_as_float_list)

    def make_list_of_variances(self):
        for i in range(len(self.one_row_distances_list)):
            for j in self.all_lists_with_splited_foats:
                self.all_measurements_of_one_distance.append(j[i])
            single_variance = np.var(self.all_measurements_of_one_distance)
            self.variances_list.append(single_variance)
        return self.variances_list

    def cut_column_if_variance_smaller_than_2e4(self):
        for i in self.variances_list:
            if i < 2e-4:
                _index_to_cut = self.variances_list.index(i)
                print(f'variance no. {_index_to_cut + 1} was smaller than 2e-4 nm^2, it was removed')
                for row in self.all_lists_with_splited_foats:
                    row.pop(_index_to_cut)
        return self.all_lists_with_splited_foats

    def put_data_into_txt_files(self):      
        with open('time_list.txt', "w") as time_file:
            for i in self.time_list:
                time_file.write(f"{i}\n")
        
        with open('phi_psi_list.txt', "w") as phi_psi_file:
            for i, j in self.phi_psi_list:
                phi_psi_file.write(f"{i} {j}\n")
        
    def close_data_files(self):
        self.data_file.close()


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
        data_read = ReadDataAndCheckVariances(file_path)
        data_read.open_data_file()
        data_read.read_data_file()
        data_read.iterate_on_rows()
        data_read.make_list_of_variances()
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
