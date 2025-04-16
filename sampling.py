import numpy as np

# Setting conversion rates and the number of samples
conversionRates = [0.15, 0.04, 0.13, 0.11, 0.05]
N = 10000 # number of samples
d = len(conversionRates) # number of slot machines

# Making arrays to count our losses and wins
nPosReward = np.zeros(d) # number of wins
nNegReward = np.zeros(d) # number of losses
timesSelected = np.zeros(d)

for i in range(N):
  selected = 0
  maxRandom = 0

  for j in range(0,d):
    #random draw from beta distribution
    randomBeta = np.random.beta(nPosReward[j]+1, nNegReward[j]+1)
    if (randomBeta>maxRandom):
      maxRandom = randomBeta
      selected = j #best machine. Should machine 1 always be gettings selected? Fishy...
  timesSelected[selected]+=1
  #if we won
  if (np.random.rand() < conversionRates[selected]): nPosReward[selected]+=1
  #if we lost
  else: nNegReward[selected]+=1

maxP=0
wins=0
losses=0
for m in range(0,d):
  pos = nPosReward[m]
  wins+=pos
  neg = nNegReward[m]
  losses+=neg
  best = 1
  p = pos/neg
  if(p>maxP):
    maxP = p
    best = m+1
  print("machine number "+str(m+1)+" was selected "+str(timesSelected[m])+" times ("+str(pos)+" wins, "+str(neg)+" losses, P="+str(p)+")")
print("Conclusion: the best machine is machine number "+str(best))
print("total reward: "+str(wins-losses))

