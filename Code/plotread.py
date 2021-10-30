import os
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def getdata(data_path, ext):
    train = []
    valid = []
    test = []
    files = os.listdir(data_path + 'Train/')
    for file in files:
        if file.endswith(ext):
            train.append(file)
    files = os.listdir(data_path + 'Valid/')
    for file in files:
        if file.endswith(ext):
            valid.append(file)
    files = os.listdir(data_path + 'Test/')
    for file in files:
        if file.endswith(ext):
            test.append(file)

    return train, valid, test


def readdata(data_path, file_list, cols, nin, nout, totalin, totalout, string, inputs):
    datax = []
    datay = []
    for file in file_list:
        df = pd.read_csv(data_path + string + file,
            sep = "\s+", #separator whitespace
            names=cols)
        df = df.set_index('time')
        x = df.drop(columns = nout[1:1+totalout])
        y = df.drop(columns = nin[1:1+totalin])
        if inputs == 1:
            x = x.drop(columns = ['PLML2', 'PLMR'])
        if inputs == 2:
            x = x.drop(columns = ['AVBL', 'AVBR'])
        if inputs == 3:
            x = x.drop(columns = ['IL2DL', 'IL2DR'])
        if inputs == 4:
            x = x.drop(columns = ['IL2L', 'IL2R'])
        if inputs == 5:
            x = x.drop(columns = ['IL2VL', 'IL2VR'])
            
        datax.append(x)
        datay.append(y)

    return datax, datay

def plotdata(sequences, dtype, var, folder, path):
    
    i=0
    for seq in sequences:
        seq.plot(kind='line')
        plt.legend(loc='upper left')
        Path(path + folder + dtype).mkdir(parents=True, exist_ok=True)
        plt.savefig(path + folder + dtype + var + str(i) + '_plots.pdf')
        plt.close()

        i = i + 1

