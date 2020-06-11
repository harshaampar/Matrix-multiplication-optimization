#@title Variables
#@markdown Defining variables for the current notebook
import numpy as np

fs = 44100
num_bands = 32

#test data
#@markdown Test symbols : [0, 1, 2 ...., num_bands/2]

#@markdown Number of repetitions of test symbols 
reps =  10 #@param {type:'integer'}
data_symbols = []
for r_ in range(reps):
  for i in range(int(num_bands/2)):
    data_symbols.append(i)

print('len of data symbols : {}'.format(len(data_symbols)))

fc = 17000
B = 3000.0
H = 4.0

delf = B/num_bands

tB = H/(2*delf)

nB = int(tB*fs)

tB = float(nB)/fs

delf = H/(2*tB)

fArray = [fc+i*delf for i in range(num_bands)]
ts = 1.0/fs

