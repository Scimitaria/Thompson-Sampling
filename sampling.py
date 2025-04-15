import numpy as np

# Setting conversion rates and the number of samples
conversionRates = [0.15, 0.04, 0.13, 0.11, 0.05]
N = 10000 # number of samples
d = len(conversionRates) # number of slot machines

# Making arrays to count our losses and wins
nPosReward = np.zeros(d) # number of wins
nNegReward = np.zeros(d) # number of losses

for i in range(N):
  selected = 0
  maxRandom = 0

  #np.random.beta(nPosReward[j] + 1, nNegReward[j] + 1)
  for j in range(0,5): # range (0,5) is the same as range(5)
    randomBeta = np.random.beta(nPosReward[j] + 1, nNegReward[j] + 1)
    if (randomBeta > maxRandom):
      maxRandom = randomBeta
      selected = j
      #return selected
    if np.random.rand() < conversionRates[selected]:
      nPosReward[selected] += 1
    else:
      nNegReward[selected] += 1
    print(selected)
    print(nPosReward[selected])
    print(nNegReward[selected])