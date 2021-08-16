from matplotlib import pyplot as plt

def read_points(file_path):
    x_coors = []
    y_coors = []
    with open(file_path) as source:
        for line in source.readlines():
            splited = line.split(" ")
            x_coors.append(float(splited[0]))
            y_coors.append(float(splited[1]))
    return x_coors, y_coors

if __name__ == "__main__":
    x, y = read_points("result.txt")
    plt.figure()
    plt.scatter(x, y)
    plt.show()