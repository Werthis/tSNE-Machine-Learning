import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

# digits = load_digits()

# print(digits.images[0])

class TSNE():

    def __init__(self):
        pass

    def open_deta_file(self):
        self.data_file = open("dialanine-300K.data", "r")
        self.data_file.read()
        # print(self.data_file.head)


    def close_data_file(self):
        return self.data_file.close()

if __name__ == "__main__":
    program = TSNE()
    program.open_deta_file()



    program.close_data_file()
