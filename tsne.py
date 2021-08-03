import numpy as np
import matplotlib.pyplot as plt
# from sklearn.datasets import load_digits

# digits = load_digits()

# print(digits.images[0])

class TSNE():

    def __init__(self):
        pass

    def open_data_file(self):
        self.data_file = open("dialanine-300K.data", "r")
        self.data_read = self.data_file.read()
        print(self.data_read[5])

    def get_one_line(self):
        for line in self.data_read[5:]:
            pass

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
    program.put_data_into_txt()


    program.close_data_file()
