
# Basic principle of this algorithm:

- In this algorithm, dataset is processed by the algorithm, and randomly 
  set to None in order to simulate the process of pacekt loss. 

# Simulation situations
- Normal packetloss (including the normal software bugs or some fluctuations)
- Link fluctuations (with this packetloss higher than normal but normally
  will not last long)

- Node failure (specifically energy depletion, packetloss increase 
  from anypoint to 100%)

# Special simulation cases
- As this three events are independent, so that we can set the three 
  situations happening together
- Special cases: when both link failure and normal congestion reasons happen
  the packetloss_type of this datapoint would be a List

# Simulation result
- This simulation result is the combination of the three cases, with node failure
  is always the last event triggered.
- These three events happen independently, which means two may be triggered at 
  the same time

# Packet loss rate analysis
- This analysis mainly uses the lstm network into rate-analysis.
- Basic idea of this analysis would be letting the information gate to capture the 
  possible relationship between lost packets and the happening of battery failure
  to predict a possible value of the future packet loss trend.

