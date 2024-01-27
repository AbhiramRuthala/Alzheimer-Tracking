
# --------- PLEASE READ -------------
# This still requires some major work 

# Input current protein values

proteinInput = input("Protein: ")


if proteinInput == "beta amyloid":
    betaAmyloidInput = float(input("Amount of beta-amyloid present: "))
elif proteinInput == "tau tangles":
    tauTanglesInput = float(input("Amount of tau-tangles present: "))
else:
    print('Invalid protein name!')


# Dictionary to store inputted protein values
proteinTracking={
    "beta-amyloid plaques":betaAmyloidInput,
    "tau tangles":tauTanglesInput
}

def ProteinSense():
    proteinThreshold = 47.265
    if betaAmyloidInput > proteinThreshold or tauTanglesInput > proteinThreshold:
        print("Dangerous build-up of the protein")
    elif betaAmyloidInput < proteinThreshold and tauTanglesInput > proteinThreshold:
        print("Dangerous build-up of the tau tangles protein complex")
    elif betaAmyloidInput > proteinThreshold and tauTanglesInput < proteinThreshold:
        print("Dangerous build-up of the beta amyloid protein complex")
    else:
        print("The protein build-up is safe for now")






# maybe use this list
proteinTracking=[
    [beta-amyloid plaques]
    [tautangles]
]


print(proteinTracking.get(-------))
print(proteinTracking.get(-------))

# Refers to initial value
initialProteinValue = -----


userRate = 2

#Check for both and see how much they build up by.
betaAmyloid = 15+userRate
tauTangles = 17+userRate


#Classify different protein aggregates that help cause neuron degeneration during Alzheimer's and give them specific functions.
class ProteinAggregates:
    def trackBetaAmyloid(self, betaAmyloid):
        self.BetaAmyloid = betaAmyloid

    def trackTauTangles(self, tauTangles):
        self.TauTangles = tauTangles
