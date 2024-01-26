import time

#Input to take the neurotransmitter
HormoneTracker = input("Which hormone are you tracking? ")

#Dictionary for intial neurotransmitter levels
neuronLevels = {
    "acetylcholine": 90,
    "dopamine": 85,
    "GABA":75,
    "serotonin":70
}

# Function will check for neuron levels and the effect posed by Alzheimer's.
def AlzheimerSim():
    AlzheimerDiseaseCalc = neuronLevels.get(HormoneTracker, " ")
    result = AlzheimerDiseaseCalc - 14
    print("The Alzheimer Simulation is being conducted...")
    time.sleep(1.5)
    print("Original value:" + str(neuronLevels.get(HormoneTracker)))
    print("Final value:" + str(result))

# Alzheimer's Disease will be simulated on sample neurotransmitter values.
AlzheimerSim()
