import time

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
    result = AlzheimerDiseaseCalc - 14
    print("The Alzheimer Simulation is being conducted...")
    time.sleep(2)
    print("Original value:" + str(neuronLevels.get(HormoneTracker)))
    print("Final value:" + str(result))

    
    if result > 70:
        print("Not too severe!")
    elif result > 60:
        print("Could be relatively severe!")
    elif result > 50 and result < 60:
        print("Pretty severe!")

# Alzheimer's Disease will be simulated on sample neurotransmitter values.
AlzheimerSim()
