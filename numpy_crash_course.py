import numpy as np

def main():
    #test_no_numpy()
    #test_numpy()
    #multi_array()
    #test_slicing()
    #test_reshaping()
    #multi_dim_slicing()
    #test_conditionals()
    #flatten_array()
    #test_matrices()
    #mult_matrices()
    test_stacking()
    #test_depth_stacking()


def test_depth_stacking():
    x = np.arange(4).reshape((2, 2))
    print(x)
    y = x * 2
    depth_stack = np.dstack((x, y))
    print(depth_stack.shape)


def test_stacking():
    x = np.arange(4).reshape((2, 2))
    print(x)
    y = np.arange(4, 8).reshape((2, 2))
    z = np.hstack((x, y))
    print(z)
    w = np.concatenate((x, y), axis=1)
    print(w)
    print(z == w)
    print(np.column_stack((x, y)) == np.hstack((x, y)))
    print(np.row_stack((x, y)) == np.vstack((x, y)))


def mult_matrices():
    mat_a = np.array([0, 3, 5, 5, 5, 2]).reshape(2, 3)
    mat_b = np.array([3, 4, 3, -2, 4, -2]).reshape(3, 2)
    print(mat_a @ mat_b)


def test_matrices():
    y = np.arange(9)
    y.shape = [3, 3]
    print(y.transpose())
    print(y.T)
    print(np.resize(y, (6, 6)))
    print(np.ones((3, 2), dtype = int))
    print(np.eye(3))
    print(np.random.rand(4,4))



def flatten_array():
    x = np.arange(9).reshape(3, 3)
    print(x)
    ravelled_array = x.ravel()
    print(ravelled_array)

    flattened_array = x.flatten()
    print(flattened_array)
    flattened_array[2] = 1000000
    print(flattened_array)
    print(x)

    #ravelled_array[2] = 1000000
    #print(ravelled_array)
    #print(x)


def test_conditionals():
    x = np.arange(9).reshape(3, 3)
    comparison_operation = x > 5
    print(comparison_operation)
    print(x.max())
    print(x.min())


def multi_dim_slicing():
    x = np.arange(9).reshape(3, 3)
    print(x)
    print(x[2, 1])
    x = np.arange(18).reshape(3, 2, 3)
    print(x)
    print(x[1, 1, 1])
    # slice all of the numbers from 6 to 11
    print(x[1, ...])
    print(x[:, 0, 0])



def test_reshaping():
    x = np.arange(9)
    print(x)
    x = x.reshape((3, -1))
    z = np.arange(18).reshape(2, 3 ,3)

    print(z)


def test_slicing():
    x = np.arange(1, 10)
    print(x[2:7:2])
    print(x[2:])


def multi_array():
    x = np.arange(3)
    y = np.arange(3)
    z = np.arange(3)

    multi_array = np.array([x, y, z])
    print(multi_array)
    print(multi_array.shape)

    w = np.linspace(1, 10, 50)
    print(w)
    b = np.arange(1, 30, 3)
    print(b)
    c = np.linspace(1, 30, 3, False)
    print(c)

    x = np.arange(3)
    y = np.arange(3,6)
    z = np.arange(6,9)
    multi_array = np.array([x, y, z])
    print(multi_array)
    print(multi_array[0, 0])
    print(multi_array[1, 2])

    print(multi_array.dtype)


def test_numpy():
    array_two = np.arange(1, 4) ** 2
    print(array_two)
    array_three = np.arange(1, 4) ** 3
    print(array_two + array_three)
    sample_array = np.array([1,2,3,4])
    np.power(sample_array, 4)
    np.negative(sample_array)
    np.exp(sample_array)
    np.log(sample_array)
    np.sin(sample_array) # Radians


def test_no_numpy():
    list_two = list(range(1, 4))
    list_three = list(range(1, 4))
    list_sum = []

    for index in range(3):
        list_two[index] = list_two[index] ** 2
        list_three[index] = list_three[index] ** 3
        list_sum.append(list_two[index] + list_three[index])
    print(list_sum)



main()