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
