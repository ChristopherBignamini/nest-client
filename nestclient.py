import nest
from common import CustomPythonBrainLoader as BrainLoader # TODO: to be removed

# TODO: add exception handling
# TODO: add input parameter check
class NestClient:
    
    def __init__(self):
        
        self.__nest = nest
        
        self.__generator_devices = []
        self.__detector_devices = []

    # TODO: jochen why do we need to return a handler to the NEST instance?    
    def startup(self, resolution = 0.1, min_delay = 0.1, max_delay = 20.0, num_processes = 1, num_thread_per_process = 1): # TODO: maps to  initialize()
        """
        Initializes the neuronal simulator
        :param timestep: The timestep used for the neuronal simulation
        :param min_delay: The minimum delay
        :param max_delay: The maximum delay
        :param num_thread_per_process: The amount of threads that should be used to run the simulation
        """
        #    :return a handle to the NEST instance 

        self.__nest.ResetKernel()
        
        # TODO: where is the full parameter list?
        # TODO: jochen, what about these inputs?  
        pars = {"resolution": resolution,
                "min_delay": min_delay,
                "max_delay": max_delay}
        
        self.__nest.SetKernelStatus(pars)

    def load_network(self, filename): # TODO: maps to load_brain
        """
        :param filename: the NEST simulation script setting up the brain
        """
        #    :return an enumeration of all valid neurons. #TODO: jochen why?        

        self.__brain_root = BrainLoader.load_py_network(filename)
        with open(filename) as source:
           self.__brain_source = source.read()

#            self.__setup_access_to_population(
#                brain_root, **self.populations_using_python_slice(populations))

    
    def run_simulation(self, duration): # TODO: maps to run_step
        """
        Run the brain simulation for the given time
        :param duration: The biological simulation time in ms
        """
        self.__nest.Simulate(duration)

    def create_device(type, **params): #TODO: maps to register_spike_sink/register_spike_source
        """
        Create a device of the given type
        :param type: the type of device to create
        :params: a dictionary of configuration parameters #TODO: to be removed, needed by current NRP implementation 
        :return a handle to the created device
        """
        # TODO: implement creation of NRP abstract device

        node_id = self.__nest.Create(type, params)
        return node_id

    def connect_device(device, neurons_ids, **params): #TODO: maps to __register_device 
        """
        Connect a device with a number of neurons
        :param device: the handle of the device to be connected
        :param neuron_ids: the identifiers of the neurons to connect the device to
        :param params: a dictionary of configuration parameters #TODO: to be removed, needed by current NRP implementation
        """
        # TODO: implement connection of NRP abstract device

        if pre: # TODO: is there a way to find if a device is a spike gen o sink?
            self.__nest.Connect(neurons_ids, device)
        else:
            self.__nest.Connect(device, neurons_ids)

    def delete_device:
        
    def get_brain_root(self): #TODO: delete
        if(self.__brain_root):
            return self.__brain_root

    def get_brain_source(self): #TODO: delete
        if(self.__brain_source):
            return self.__brain_source
