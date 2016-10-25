import numpy as num

class NetworkLayers(object):
    #It will create Neural Network Architecture and Assign Weights and Biases to
    #np.random.randn function to generate
    #Gaussian distributions with mean and standard deviation in given range
    #if we want to create neural network with 3 layers we create NetworkLayers
    #object like net = NetworkLayers([2, 3, 1]) means
    #first layer contain 2 input neuron hidden layer contain 3 neurons
    #nuber of hidden layer  = 1 and one output layer contain 1 neuron
    def __init__(self, configuration):
        self.number_of_layers = len(configuration);
        self.configuration = configuration;
        self.weights = [np.random.randn(y, 1) for y in configuration[1:]]
        self.biases = [np.random.randn(y, x) for x, y in zip([:-1], [1:])]
