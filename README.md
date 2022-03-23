# Read this file before the actual project

- <big>***Project outcome***</big>
  - Heart rate data packet loss recovery
  - Sensor node depletion detection

## Packet loss gap filling
- LSTM is used as the algorithm, getting a heart rate curve fitting error of within
  10%, so that the filling of packet loss would be within en error of 10%

## Sensor node depletion detection
- LSTM is used in this scenario, and the depletion would be detected before a 
  catastrophic value is reached

`For further details of methodology, please see the files in 
heartrate_lossfilling and node_depletion_detection`
