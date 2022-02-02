'''This algorithm is describing the process when link fluctuates

At this time, packetloss is generally higher than normal situations
But still randomly dropping, which means that this algorithm is highly 
  similar to the normal situations, so that to reduce redundancy, this algorithm
  is combined to normal_packetloss, which is the final input of this model, and 
  if there are the last input in this algorithm, then this means that this model 
  is showing to be link fluctuation, and this data is tagged into the generated
  data type data_packetloss_type with packetloss_type of 0
'''

