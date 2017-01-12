import generators

if __name__ == '__main__':
    generator = generators.SortTask(batch_size=1, max_iter=1, size=3, max_length=5, end_marker=False)
    generator.sample(3)

# import numpy as np
# import theano
#
# if __name__ == '__main__':
#     example_input = np.zeros((1, 2, 2))
#     example_input[0, 0, 0] = 1  # np.array([[[1, 0], [0, 1]]])
#     example_input[0, 0, 1] = 0
#     example_input[0, 1, 0] = 0
#     example_input[0, 1, 1] = 1
#     example_output = np.zeros((1, 2, 2))
#     example_output[0, 0, 0] = 0  # np.array([[[1, 0], [0, 1]]])
#     example_output[0, 0, 1] = 1
#     example_output[0, 1, 0] = 1
#     example_output[0, 1, 1] = 0
#
#     example_input = np.zeros((1, 2, 5))
#     example_input[0, 0, 0] = 1  # np.array([[[1, 0], [0, 1]]])
#     example_input[0, 0, 1] = 0
#     example_input[0, 1, 0] = 0
#     example_input[0, 1, 1] = 1
#     example_output = np.zeros((1, 2, 2))
#     example_output[0, 0, 0] = 0  # np.array([[[1, 0], [0, 1]]])
#     example_output[0, 0, 1] = 1
#     example_output[0, 1, 0] = 1
#     example_output[0, 1, 1] = 0
#
#     # length = 3
#     # size = 3
#     # batch_size = 1
#     # sequence = np.random.binomial(1, 0, (batch_size, length, size))  # length should be 3, size should be 3?
#     # sequence[0,0,0] = 1
#     # sequence[0,1,1] = 1
#     # sequence[0,2,2] = 1
#     # example_input = np.zeros((batch_size, 2 * length, \
#     #                           size), dtype=theano.config.floatX)
#     # example_output = np.zeros((batch_size, 2 * length, \
#     #                            size), dtype=theano.config.floatX)
#     #
#     # example_input[:, :length, :size] = sequence
#     # # example_input[:, length, -1] = 1
#     #
#     # sequence2 = np.random.binomial(1, 0, (batch_size, length, size))  # length should be 3, size should be 3?
#     # sequence2[0, 2, 0] = 1
#     # sequence2[0, 1, 1] = 1
#     # sequence2[0, 0, 2] = 1
#     # example_output[:, length:2 * length, :size] = sequence2
#
#
#     length = 3
#     size = 3
#     batch_size = 1
#     sequence = np.random.binomial(1, 0, (batch_size, length, size))  # length should be 3, size should be 3?
#     sequence[0, 0, 0] = 1
#     sequence[0, 1, 1] = 1
#     sequence[0, 2, 2] = 1
#     example_input = np.zeros((batch_size, 2 * length + 1, \
#                               size + 1), dtype=theano.config.floatX)
#     example_output = np.zeros((batch_size, 2 * length + 1, \
#                                size + 1), dtype=theano.config.floatX)
#
#     example_input[:, :length, :size] = sequence
#     # example_input[:, length, -1] = 1
#
#     sequence2 = np.random.binomial(1, 0, (batch_size, length, size))  # length should be 3, size should be 3?
#     sequence2[0, 2, 0] = 1
#     sequence2[0, 1, 1] = 1
#     sequence2[0, 0, 2] = 1
#     example_output[:, length + 1:2 * length + 1, :size] = sequence2
#     print("dd")