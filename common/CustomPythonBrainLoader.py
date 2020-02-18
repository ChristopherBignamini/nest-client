import imp

__brain_index = 0

def load_py_network(path):
    """
    Load a python network file

    :param path: path to the .py file
    """
    global __brain_index
    brain_module = imp.load_source('__brain_model' + str(__brain_index), path)
    __brain_index += 1
    return brain_module
