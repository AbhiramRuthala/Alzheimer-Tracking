
HormoneTracker = input("Which hormone are you tracking? ")

neuronLevels = {
    "acetylcholine": 90,
    "dopamine": 85,
    "Gaba":75,
    "serotonin":70
}

# Function will check for neuron levels and the effect posed by Alzheimer's.
def AlzheimerSim():
    AlzheimerDiseaseCalc = neuronLevels.get(HormoneTracker, " ")
