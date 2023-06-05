import math


class Node:
    def __init__(self, id_number):
        self.id = id_number
        self.layer = 0
        self.input_value = 0
        self.output_value = 0
        self.connections = []

    def activate(self):
        def sigmoid(x):
            return 1 / (1 + math.exp(-x))

        if self.layer == 1:
            self.output_value = sigmoid(self.input_value)

        for i in range(0, len(self.connections)):
            self.connections[i].to_node.input_value += \
                self.connections[i].weight * self.output_value

            # this for loop through all the connections through the connection list
            #  the loop adds the product of the connection's weight and
            # the node's output value to the input value variable of the destination node
            # associated with the connection

    def clone(self):
        clone = Node(self.id)
        clone.id = self.id
        clone.layer = self.layer
        return clone
