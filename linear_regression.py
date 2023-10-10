import numpy as np
import matplotlib.pyplot as plt

def main():
    linear_regression()

def draw(pt1, pt2):
    ln = plt.plot(pt1, pt2)
    plt.pause(0.001)
    ln[0].remove()


def sigmoid(score):
    return 1/(1 + np.exp(-score))


def calculate_error(line_parameters, points, y):
    m = all_points.shape[0]
    p = sigmoid(points * line_parameters)
    cross_entropy = -(1/m) *( (np.log(p).T)*y + np.log(1-p).T*(1-y))
    return cross_entropy


def gradient_descent(line_parameters, points, y, learning_rate):
    m = points.shape[0]
    for i in range(500):
        p = sigmoid(points * line_parameters)
        gradient = (points.T*(p-y))*(learning_rate/m)
        line_parameters = line_parameters - gradient
        w1 = line_parameters.item(0)
        w2 = line_parameters.item(1)
        b = line_parameters.item(2)
        x1 = np.array([points[:, 0].min(), points[:, 0].max()])
        x2 = -b/w2 + x1 * (-w1/w2)
        draw(x1, x2)


def linear_regression():
    n_pts = 500
    np.random.seed(0)
    bias = np.ones(n_pts)
    y = np.array([np.zeros(n_pts), np.ones(n_pts)]).reshape(n_pts*2, 1)
    random_x1_values = np.random.normal(10, 2, n_pts)
    random_x2_values = np.random.normal(12, 2, n_pts)
    top_region = np.array([random_x1_values, random_x2_values, bias]).T
    bottom_region = np.array([np.random.normal(5, 2, n_pts), 
    np.random.normal(6, 2, n_pts), bias]).T
    all_points = np.vstack((top_region, bottom_region))
    # Choose random starting line
    #w1 = -0.8
    #w2 = -0.9
    #b = 6
    line_parameters = np.matrix([np.zeros(3)]).T

    #x1 = np.array([bottom_region[:, 0].min(), top_region[:, 0].max()]) 
    # w1x1 + w2x2 + b = 0
    #x2 = -b/w2 + x1 * (-w1/w2)
    #linear_combination = all_points * line_parameters
    #probabilities = sigmoid(linear_combination)
    #print(probabilities)
    #print(calculate_error(line_parameters, all_points, y))

    fig, ax = plt.subplots(figsize=(4, 4))
    ax.scatter(top_region[:, 0], top_region[:, 1], color='r')
    ax.scatter(bottom_region[:, 0], bottom_region[:, 1], color='b')
    gradient_descent(line_parameters, all_points, y, 1)
    #draw(x1, x2)
    plt.show()


if __name__ == '__main__':
    main()