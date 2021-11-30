import scipy.io as sio

data_mat = sio.loadmat('data.mat')
peak_mat = sio.loadmat('peak.mat')
ecg_peak = peak_mat['R_pk'].tolist()
ecg_raw_data = data_mat['data'].tolist()


'''a list containing ECG peaks
'''

ecg_final = [str(data).strip('[]') for data in ecg_peak]


'''take 20s count for average heartbeat analysis

As Fs = 100, we take 2000 data from data_mat
and count how many peak_data is contained
'''

with open ('heartbeat.txt','w') as _txt:
    for j in range (0,29570,5):
        '''Fs = 100, 2957000 points in total

        So 29570 seconds, and take 5s interval
        '''

        heartrate = len([peak for peak in  ecg_raw_data[100*j:100*(j+5)] if peak in ecg_peak])*12
        print (f'heartrate is:{heartrate} and the time is {j}s')
        _txt.write(str(heartrate) + '\n')