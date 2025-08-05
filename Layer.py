import numpy as np
from abc import ABC, abstractmethod

class Layer():
    def 


class ConvolutionalLayer(Layer):
    def __init__(self, n_in, n_out, kernel_size, stride, padding):
        self.n_in = n_in
        self.n_out = n_out
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        
        