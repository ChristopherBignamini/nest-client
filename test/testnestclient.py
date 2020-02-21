from nestclient import *
from devices import NestFixedSpikeGenerator

nestClient = NestClient()
nestClient.startup()

nestClient.load_network("test/brunel.py")

brain_root = nestClient.get_brain_root()
print(brain_root)
brain_source = nestClient.get_brain_source()
print(brain_source)

params = {}
nestClient.create_device(NestFixedSpikeGenerator,params)

#nestClient.run_simulation(1000.)
