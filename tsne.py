from csv import reader
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split


class ReadAndTransformData():

    def __init__(self):
        self.all_lists_with_splited_foats = []
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
        # print('\n', self.variances_list, '\n', len(self.all_measurements_of_one_distance))

    # def make_array(self):
    #     arr = np.array(self.all_lists_with_splited_foats)
    #     # print(arr)
    #     return arr

    def put_data_into_txt(self):
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
        
    def close_data_file(self):
        self.data_file.close()
        self.world_map_file_1.close()
        self.world_map_file_2.close()
        self.world_map_file_3.close()
        self.world_map_file_4.close()


class TSNE():

    def __init__(self):
        self.digits = load_digits()
        # print(self.digits.images[0])

    def show_plots(self):
        self.fig = plt.figure(figsize=(12, 12))
        self.fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
        for i in range(64):
            ax = self.fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
            ax.imshow(self.digits.images[i], cmap=plt.cm.binary, interpolation='none')
            ax.text(0, 7, str(self.digits.target[i]))

        plt.show()

    def train(self):
        x_train, x_test, y_train, y_test = train_test_split(self.digits.data, self.digits.target)
        clf = GaussianNB()
        clf.fit(x_train, y_train)
        predicted = clf.predict(x_test)
        expected = y_test
        # print(expected)

        fig = plt.figure(figsize=(12, 12))
        fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

        for i in range(64):
            ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
            ax.imshow(x_test.reshape(-1, 8, 8)[i], cmap=plt.cm.binary, interpolation='none')

            if predicted[i] == expected[i]:
                ax.text(0, 7, str(predicted[i]), color='green')
            else:
                ax.text(0, 7, str(predicted[i]), color='red')

        plt.show()

        matches = (predicted == expected)
        print(matches.sum())
        print(len(matches))



class Main():

    def __init__(self):
        self.read_data()
        self.load_tSNE()

    def read_data(self):
        data_read = ReadAndTransformData()
        data_read.open_data_file()
        data_read.read_data_file()
        data_read.get_one_row()
        data_read.make_all_variances()
        data_read.cut_column_if_variance_smaller_than_2e4()
        data_read.put_data_into_txt()
        data_read.close_data_file()

    def load_tSNE(self):
        tsne = TSNE()
        # tsne.show_plots()
        tsne.train()
        
        
if __name__ == "__main__":
    main = Main()
