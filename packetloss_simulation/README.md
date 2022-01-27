
# Basic principle of this algorithm:

- In this algorithm, dataset is processed by the algorithm, and randomly 
  set to None in order to simulate the process of pacekt loss. 

# Simulation situations
- Normal packetloss (including the normal software bugs or some fluctuations)
- Link fluctuations (with this packetloss higher than normal but normally
  will not last long)

- Node failure (specifically energy depletion, packetloss increase 
  from anypoint to 100%)

# Simulation result
- This simulation result is the combination of the three cases, with node failure
  is always the last event triggered.
- These three events happen independently, which means two may be triggered at 
  the same time

