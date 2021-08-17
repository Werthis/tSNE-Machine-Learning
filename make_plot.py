from matplotlib import pyplot as plt

def read_points(results_file_path):
    x_coors = []
    y_coors = []
    with open(results_file_path) as source:
        for line in source.readlines():
            splited = line.split(" ")
            x_coors.append(float(splited[0]))
            y_coors.append(float(splited[1]))
    return x_coors, y_coors

def read_time(time_file_path):
    time_list = []
    with open(time_file_path) as time_file:
        for line in time_file.readlines():
            # splited = line.split(" ")
            time_list.append(float(line[0]))
    return time_list
            

if __name__ == "__main__":
    x, y = read_points("result.txt")
    time = read_time('time_list.txt')
    plt.figure()
    plt.scatter(x, y, c = time, cmap='viridis')
    plt.show()