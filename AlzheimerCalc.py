#Input to check for a certain neurotransmitter
HormoneTracker = input("Which hormone are you tracking? ")

#Dictionary for neurotransmitter levels
neuronLevels = {
    "acetylcholine": 90,
    "dopamine": 85,
    "Gaba":75,
    "serotonin":70
}

# Function will check for neurotransmitter levels and the effect posed by Alzheimer's.
def AlzheimerSim():
    AlzheimerDiseaseCalc = neuronLevels.get(HormoneTracker, " ")
