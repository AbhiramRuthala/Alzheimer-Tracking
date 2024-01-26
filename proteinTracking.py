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


betaAmyloid = 15+userRate
tauTangles = 17+userRate



class ProteinAggregates:
    def trackBetaAmyloid(self, betaAmyloid):
        self.BetaAmyloid = betaAmyloid

    def trackTauTangles(self, tauTangles):
        self.TauTangles = tauTangles
