import matplotlib.pyplot as plt

def plot():
    v = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    t = [1.8008999177254736e-05, 3.616199683165178e-05, 0.00014762800128664821, 0.0009160240006167442, 0.0060122930008219555, 0.05050924500392284, 0.4120638020031038, 4.373493354003585, 48.617937107002945, 590.928217464003, 7817.853531592002]
    plt.plot(v,t)
    plt.xlabel("Number of Vertices")
    plt.ylabel("Time Taken (in seconds)")
    plt.title("Time Taken for generating Minimum Hamiltonian Circuit by Brute force approach")
    plt.show()

