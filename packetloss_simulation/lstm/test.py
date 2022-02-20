from typing import List
import numpy as np

from lstm import LstmParam, LstmNetwork


class ToyLossLayer:
    """
    Computes square loss with first element of hidden layer array.
    """
    @classmethod
    def loss(self, pred, label):
        return (pred[0] - label) ** 2

    @classmethod
    def bottom_diff(self, pred, label):
        diff = np.zeros_like(pred)
        diff[0] = 2 * (pred[0] - label)
        return diff


def example_0(
        y_list: List
    ):
    # learns to repeat simple sequence from random inputs
    np.random.seed(0)

    # parameters for input data dimension and lstm cell count
    mem_cell_ct = 1000
    x_dim = 60
    lstm_param = LstmParam(mem_cell_ct, x_dim)
    lstm_net = LstmNetwork(lstm_param)
   
    input_val_arr = [np.random.random(x_dim) for _ in y_list]

    for cur_iter in range(1000):
        print("iter", "%2s" % str(cur_iter), end=": ")
        for ind in range(len(y_list)):
            lstm_net.x_list_add(input_val_arr[ind])

        print(
            "y_pred = [" + ", ".join(
                ["% 2.5f" % lstm_net.lstm_node_list[ind].state.h[0] \
                  for ind in range(len(y_list))]
            ) + "]", end=", "
        )

        loss = lstm_net.y_list_is(y_list, ToyLossLayer)
        print("loss:", "%.3e" % loss)
        lstm_param.apply_diff(lr=0.1)
        lstm_net.x_list_clear()

    return ["% 2.5f" % lstm_net.lstm_node_list[ind].state.h[0] \
                  for ind in range(len(y_list))] 


if __name__ == "__main__":
    with open ('../datafile/datafile1.txt') as _f:
       data = _f.read().split('\n')

    data_list = data[1:-1]

    final_list = list()
    for i in range (int(len(data_list)/100)):
        _d = data_list[100*(i-1) : 100*i]
        loss_packets = len([_data for _data in _d if _data == 'None'])
        final_list.append(loss_packets)
    print (final_list)
    x = example_0(final_list)

    print (x)

