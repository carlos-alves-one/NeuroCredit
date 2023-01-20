
# Goldsmiths University of London
# Author....: Carlos Manuel de Oliveira Alves
# Student...: cdeol003
# Created...: 15/01/2023
# FYP.......: NeuroCredit

# Description: This is the main file of the project. It will be used to run the
#              neural network and the GUI.

# First step: Defined a class called "neuralNetwork" which contains three methods: __init__, train, and query.
#             The __init__ method is the constructor of the class, and it is automatically called when create a new instance of the class. 
#             In this method, we set the number of nodes in the input, hidden, and output layers of the network, as well as the learning rate.
#             The train method will be used to train the neural network, and the query method will be used to query the neural network.
#             The pass statement is also used as a placeholder for code that is not ready to be implemented yet.
#             At the end we create a new instance of the neural network class, and we pass the number of input, hidden, and output nodes, 
#             as well as the learning rate.

# neural network class definition
class neuralNetwork:

    # initialise the neural network
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        # set number of nodes in each input, hidden, output layer
        self.inodes = input_nodes
        self.hnodes = hidden_nodes
        self.onodes = output_nodes

        # learning rate
        self.lr = learning_rate
    
        pass

    # train the neural network
    def train():
        pass

    # query the neural network
    def query():
        pass
    
# declare the number of input, hidden and output nodes
input_nodes  = 3
hidden_nodes = 3
output_nodes = 3

# declare the learning rate is 0.3
learning_rate = 0.3

# create instance of neural network
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

