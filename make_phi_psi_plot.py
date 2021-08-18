from matplotlib import pyplot as plt

def read_time(time_file_path):
    time_list = []
    with open(time_file_path) as time_file:
        for line in time_file.readlines():
            time_list.append(float(line[0]))
    return time_list

def read_phi_psi(phi_psi_file_path):
    phi_coors = []
    psi_coors = []
    with open(phi_psi_file_path) as phi_psi_file:
        for line in phi_psi_file.readlines():
            splited = line.split(' ')
            # print(line, end='')
            phi_coors.append(float(splited[0]))
            psi_coors.append(float(splited[1]))
    return phi_coors, psi_coors


if __name__ == "__main__":
    time = read_time('time_list.txt')
    phi, psi = read_phi_psi('phi_psi_list.txt')
    plt.figure()
    plt.scatter(phi, psi, c = time, cmap='Blues')
    plt.show()