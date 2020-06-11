from common_vars import *

rec_signal=np.loadtxt('modulated_signal_dump.txt')

#@title Demodulation
 
#synthetic signal
import time
# 32 * 15 *160

decoded_symbols = []
cosKernel=np.zeros([num_bands,nB])
sinKernel=np.zeros([num_bands,nB])
# Precalcualing the Kernel matrix 
# Size of Kernel Matrix = 32(num_bands) x 940 (nB)
for i in range(num_bands):
  for j in range(nB):
    cosKernel[i,j]=np.cos(2*np.pi*fArray[i]*(j+1)*ts)
    sinKernel[i,j]=np.sin(2*np.pi*fArray[i]*(j+1)*ts)

dec_time_start = time.time()

# Recorded_data_Size = Number of Symbols * Symbol_length(nB)=160*940
for symbolIndex in range(len(data_symbols)):
    tempData = rec_signal[symbolIndex * nB : (symbolIndex+1) * nB]
    cosScores = [0 for i in range(num_bands)]
    sinScores = [0 for i in range(num_bands)]
    #For each data symbol of length 940 : Multiplication [940X32]*[940]
    #Matrix Multiplication of 32(num_bands) x 940 (nB)
    for i in range(num_bands):
        for j in range(nB):
            cosScores[i] += tempData[j]*cosKernel[i,j]
            sinScores[i] += tempData[j]*sinKernel[i,j]
    
    # Two frequencies per symbol
    finalScores = [0 for i in range(int(num_bands/2))]
 
    for i in range(int(num_bands/2)):
        finalScores[i] = cosScores[i]**2 + cosScores[i+int(num_bands/2)]**2 + \
                          sinScores[i]**2 + sinScores[i+int(num_bands/2)]**2
 
    decodedSymbol_ = np.argmax(finalScores)
 
    decoded_symbols.append(decodedSymbol_)
 
dec_time_end = time.time()
 
time_taken = dec_time_end - dec_time_start
 
print('Time taken to decode : {} seconds'.format(str(time_taken)[:5]))
 
err_arr = ([i==j for  i,j in zip(data_symbols, decoded_symbols)])
 
err_count = err_arr.count(False)
print('Total error : {}'.format(err_count))
