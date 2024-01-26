# Import necessary files. 
import time
import random as rd
import sys

#Input the necessary neurotransmitter
HormoneTracker = input("Which hormone are you tracking? ")

neuronLevels = {
    "acetylcholine": 90,
    "dopamine": 85,
    "Gaba":75,
    "serotonin":70,
    "endorphins":50,
    "glutamate":30
}

neuron = ["acetylcholine",
          "dopamine",
          "serotonin",
          "Gaba",
          "endorphins",
          "glutamate"]


# Function will check for neuron levels and the effect posed by Alzheimer's.
def AlzheimerSim():
    AlzheimerDiseaseCalc = neuronLevels.get(HormoneTracker, "Invalid type!")
    if AlzheimerDiseaseCalc == "Invalid type!":
        print("Invalid neurotransmitter type!")
        # Break the function - I'll change this later
        sys.exit()
    else:
        result = AlzheimerDiseaseCalc - 14
    print("The Alzheimer Simulation is being conducted...")
    time.sleep(1)
    print("Original value: " + str(neuronLevels.get(HormoneTracker)))
    print("Current value: " + str(result))


    # Classify the severity of the condition after checking the results of the Alzheimer simulation. 
    if result > 70:
        print("\033[1mImportant:\033[0m ")
        print("Not too severe!")
    elif result > 60:
        print("\033[1mImportant:\033[0m ")
        print("Could be relatively severe!")
    elif result > 50 and result < 60:
        print("\033[1mImportant:\033[0m ")
        print("Pretty severe!")
    elif result > 40 and result < 50:
        print("\033[1mImportant:\033[0m ")
        print("Very severe!")
    elif result > 30 and result < 40:
        print("\033[1mImportant:\033[0m ")
        print("Go to the hospital!")
    elif result > 15 and result < 30:
        print("\033[1mImportant:\033[0m ")
        print("You are in critical condition")

    for word in neuron:
        # check if the input is in the list.
        if HormoneTracker == word:
            time.sleep(1)
            print(" ")
            print("\033[1mNext Step:\033[0m ")
            # Calls for another neurotransmitter once one is identified.
            print("\x1B[3mI think we should check for \x1B[0m" + str(rd.choice(neuron)))
        else:
            pass

# Alzheimer's Disease will be simulated on sample neurotransmitter values.
AlzheimerSim()
