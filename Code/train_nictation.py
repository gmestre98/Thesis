import argparse
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import GRU
from keras.layers import SimpleRNN
from keras.layers import TimeDistributed
from keras.layers import Dense
from keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.optimizers import SGD
import os
import glob
from plotread import *

def createmodel(opt, output_size):
    model = Sequential()
    if opt.model == 'LSTM':
        model.add(LSTM(opt.hidden_size, return_sequences=True))
    elif opt.model == 'GRU':
        model.add(GRU(opt.hidden_size, return_sequences=True))
    elif opt.model == 'RNN':
        model.add(SimpleRNN(opt.hidden_size, return_sequences=True))
    model.add(TimeDistributed(Dense(output_size)))

    return model

def getcallbacks(opt):
    filepath= opt.savepath + "weights/weights-{epoch:02d}-{val_loss:.6f}.hdf5"
    checkpoint = ModelCheckpoint(filepath, monitor='val_loss', verbose=1,
        save_best_only=True, save_weights_only=False, mode='auto', period=1)
    if opt.early_stop == False:
        callbacks_list = [checkpoint]
    elif opt.early_stop == True:
        early_stop = EarlyStopping(monitor='val_loss', min_delta=0, patience=opt.patience,
            verbose=1, mode="auto")
        callbacks_list = [checkpoint, early_stop]

    return callbacks_list

def savehistory(history, opt):

    dat = np.array([history.history['loss'], history.history['val_loss']])
    a= np.column_stack((dat))
    np.savetxt(opt.savepath + 'training_history.dat', a, delimiter=' ')

    return

def loadweights(opt, model):
    checkpoint_dir = opt.savepath + "weights/*"
    list_files = glob.glob(checkpoint_dir)
    latest = max(list_files, key=os.path.getctime)
    print(latest)
    model.load_weights(latest)

    return model


def main():
    ###########################################################################
    # Parser Definition
    ###########################################################################
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-model', choices=['LSTM', 'GRU', 'RNN'], default='GRU')
    parser.add_argument('-epochs', type=int, default=1000)
    parser.add_argument('-hidden_size', type=int, default=16)
    parser.add_argument('-learning_rate', type=float, default=0.05)
    parser.add_argument(
        '-optimizer', choices=['sgd', 'rmsprop', 'adam'], default='adam')
    parser.add_argument('-datapath', type=str, default="../Datasets/Nictation-20-0_5-6/")
    parser.add_argument('-savepath', type=str, default="RNN/Batch/4/Run10/")
    parser.add_argument('-extension', type=str, default=".dat")
    parser.add_argument('-batch_size', type=int, default=32)
    parser.add_argument('-plots', type=bool, default=False)
    parser.add_argument('-early_stop', type=bool, default=False)
    parser.add_argument('-patience', type=int, default=50)
    opt = parser.parse_args()

    saveplace = ['Experiment1/GRU-Nictation/8/Run1/', 'Experiment1/GRU-Nictation/8/Run2/', 'Experiment1/GRU-Nictation/8/Run3/', 'Experiment1/GRU-Nictation/8/Run4/', 'Experiment1/GRU-Nictation/8/Run5/',
    'Experiment1/GRU-Nictation/8/Run6/', 'Experiment1/GRU-Nictation/8/Run7/', 'Experiment1/GRU-Nictation/8/Run8/', 'Experiment1/GRU-Nictation/8/Run9/', 'Experiment1/GRU-Nictation/8/Run10/',
    'Experiment1/GRU-Nictation/16/Run1/', 'Experiment1/GRU-Nictation/16/Run2/', 'Experiment1/GRU-Nictation/16/Run3/', 'Experiment1/GRU-Nictation/16/Run4/', 'Experiment1/GRU-Nictation/16/Run5/',
    'Experiment1/GRU-Nictation/16/Run6/', 'Experiment1/GRU-Nictation/16/Run7/', 'Experiment1/GRU-Nictation/16/Run8/', 'Experiment1/GRU-Nictation/16/Run9/', 'Experiment1/GRU-Nictation/16/Run10/',
    'Experiment1/GRU-Nictation/32/Run1/', 'Experiment1/GRU-Nictation/32/Run2/', 'Experiment1/GRU-Nictation/32/Run3/', 'Experiment1/GRU-Nictation/32/Run4/', 'Experiment1/GRU-Nictation/32/Run5/',
    'Experiment1/GRU-Nictation/32/Run6/', 'Experiment1/GRU-Nictation/32/Run7/', 'Experiment1/GRU-Nictation/32/Run8/', 'Experiment1/GRU-Nictation/32/Run9/', 'Experiment1/GRU-Nictation/32/Run10/',
    'Experiment1/LSTM-Nictation/7/Run1/', 'Experiment1/LSTM-Nictation/7/Run2/', 'Experiment1/LSTM-Nictation/7/Run3/', 'Experiment1/LSTM-Nictation/7/Run4/', 'Experiment1/LSTM-Nictation/7/Run5/',
    'Experiment1/LSTM-Nictation/7/Run6/', 'Experiment1/LSTM-Nictation/7/Run7/', 'Experiment1/LSTM-Nictation/7/Run8/', 'Experiment1/LSTM-Nictation/7/Run9/', 'Experiment1/LSTM-Nictation/7/Run10/',
    'Experiment1/LSTM-Nictation/14/Run1/', 'Experiment1/LSTM-Nictation/14/Run2/', 'Experiment1/LSTM-Nictation/14/Run3/', 'Experiment1/LSTM-Nictation/14/Run4/', 'Experiment1/LSTM-Nictation/14/Run5/',
    'Experiment1/LSTM-Nictation/14/Run6/', 'Experiment1/LSTM-Nictation/14/Run7/', 'Experiment1/LSTM-Nictation/14/Run8/', 'Experiment1/LSTM-Nictation/14/Run9/', 'Experiment1/LSTM-Nictation/14/Run10/',
    'Experiment1/LSTM-Nictation/27/Run1/', 'Experiment1/LSTM-Nictation/27/Run2/', 'Experiment1/LSTM-Nictation/27/Run3/', 'Experiment1/LSTM-Nictation/27/Run4/', 'Experiment1/LSTM-Nictation/27/Run5/',
    'Experiment1/LSTM-Nictation/27/Run6/', 'Experiment1/LSTM-Nictation/27/Run7/', 'Experiment1/LSTM-Nictation/27/Run8/', 'Experiment1/LSTM-Nictation/27/Run9/', 'Experiment1/LSTM-Nictation/27/Run10/',
    'Experiment1/RNN-Nictation/15/Run1/', 'Experiment1/RNN-Nictation/15/Run2/', 'Experiment1/RNN-Nictation/15/Run3/', 'Experiment1/RNN-Nictation/15/Run4/', 'Experiment1/RNN-Nictation/15/Run5/',
    'Experiment1/RNN-Nictation/15/Run6/', 'Experiment1/RNN-Nictation/15/Run7/', 'Experiment1/RNN-Nictation/15/Run8/', 'Experiment1/RNN-Nictation/15/Run9/', 'Experiment1/RNN-Nictation/15/Run10/',
    'Experiment1/RNN-Nictation/29/Run1/', 'Experiment1/RNN-Nictation/29/Run2/', 'Experiment1/RNN-Nictation/29/Run3/', 'Experiment1/RNN-Nictation/29/Run4/', 'Experiment1/RNN-Nictation/29/Run5/',
    'Experiment1/RNN-Nictation/29/Run6/', 'Experiment1/RNN-Nictation/29/Run7/', 'Experiment1/RNN-Nictation/29/Run8/', 'Experiment1/RNN-Nictation/29/Run9/', 'Experiment1/RNN-Nictation/29/Run10/',
    'Experiment1/RNN-Nictation/56/Run1/', 'Experiment1/RNN-Nictation/56/Run2/', 'Experiment1/RNN-Nictation/56/Run3/', 'Experiment1/RNN-Nictation/56/Run4/', 'Experiment1/RNN-Nictation/56/Run5/',
    'Experiment1/RNN-Nictation/56/Run6/', 'Experiment1/RNN-Nictation/56/Run7/', 'Experiment1/RNN-Nictation/56/Run8/', 'Experiment1/RNN-Nictation/56/Run9/', 'Experiment1/RNN-Nictation/56/Run10/']

    valor = 0
    for sp in saveplace:
        opt.savepath = sp

        if valor/10 == 0:
            opt.hidden_size = 8
        if valor/10 == 1:
            opt.hidden_size = 16
        if valor/10 == 2:
            opt.hidden_size = 32
        if valor/10 == 3:
            opt.model = 'LSTM'
            opt.hidden_size = 7
        if valor/10 == 4:
            opt.model = 'LSTM'
            opt.hidden_size = 14
        if valor/10 == 5: 
            opt.model = 'LSTM'
            opt.hidden_size = 27
        if valor/10 == 6: 
            opt.model = 'RNN'
            opt.hidden_size = 15
            opt.learning_rate = 0.001
        if valor/10 == 7: 
            opt.model = 'RNN'
            opt.hidden_size = 29
            opt.learning_rate = 0.001
        if valor/10 == 8: 
            opt.model = 'RNN'
            opt.hidden_size = 56
            opt.learning_rate = 0.001

        print(opt.datapath)      

        ###########################################################################
        # Variables Definition
        ###########################################################################
        input_size = 6
        output_size = 6
        #nin = ['time', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
        #nout = ['time', 'DB1', 'LUAL', 'PVR', 'VB1']
        #neurons = ['time','DB1','LUAL','PVR','VB1','PLML2','PLMR','AVBL','AVBR']
        nin = ['time', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
        nout = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR']
        neurons = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
        if opt.optimizer == 'adam':
            opt_function = Adam(learning_rate=opt.learning_rate)
        elif opt.optimizer == 'sgd':
            opt_function = SGD(learning_rate=opt.learning_rate)
        elif opt.optimizer == 'rmsprop':
            opt_function = RMSprop(learning_rate=opt.learning_rate)

        ###########################################################################
        # Read data
        ###########################################################################
        train, valid, test = getdata(opt.datapath, opt.extension)
        trainx, trainy = readdata(opt.datapath, train, neurons, nin, nout, input_size, output_size, 'Train/', 0)
        validx, validy = readdata(opt.datapath, valid, neurons, nin, nout, input_size, output_size, 'Valid/', 0)
        testx, testy = readdata(opt.datapath, test, neurons, nin, nout, input_size, output_size, 'Test/', 0)
        if opt.plots:
            plotdata(trainx, '/train_data', '/x', opt.model, opt.savepath)
            plotdata(trainy, '/train_data', '/y', opt.model, opt.savepath)
            plotdata(validx, '/valid_data', '/x', opt.model, opt.savepath)
            plotdata(validy, '/valid_data', '/y', opt.model, opt.savepath)
            plotdata(testx, '/test_data', '/x', opt.model, opt.savepath)
            plotdata(testy, '/test_data', '/y', opt.model, opt.savepath)
        ###########################################################################
        # Create and Train Model
        ###########################################################################
        model = createmodel(opt, output_size)
        model.compile(optimizer=opt_function, loss='mean_squared_error')
        callbacks_list = getcallbacks(opt)
        history=model.fit(
            np.array(trainx),
            np.array(trainy),
            batch_size=opt.batch_size,
            epochs=opt.epochs,
            verbose=1,
            callbacks=callbacks_list,
            validation_data=(np.array(validx), np.array(validy)),
            validation_freq=1,
            workers=12,
            use_multiprocessing=True
        )
        model.summary()
        savehistory(history, opt)
        model = loadweights(opt, model)
        model.save(opt.savepath + 'model.h5')

        valor = valor + 1

if __name__ == "__main__":
    main()