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
        '-model', choices=['LSTM', 'GRU', 'RNN'], default='LSTM')
    parser.add_argument('-epochs', type=int, default=1000)
    parser.add_argument('-hidden_size', type=int, default=8)
    parser.add_argument('-learning_rate', type=float, default=0.05)
    parser.add_argument(
        '-optimizer', choices=['sgd', 'rmsprop', 'adam'], default='adam')
    parser.add_argument('-datapath', type=str, default="../Datasets/PTRS-20-0_5-4/")
    parser.add_argument('-savepath', type=str, default="RNN/Batch/4/Run10/")
    parser.add_argument('-extension', type=str, default=".dat")
    parser.add_argument('-batch_size', type=int, default=32)
    parser.add_argument('-plots', type=bool, default=False)
    parser.add_argument('-early_stop', type=bool, default=False)
    parser.add_argument('-patience', type=int, default=50)
    opt = parser.parse_args()

    inputs_removed = 0

    saveplace = ['Experiment2/LSTM-8/No_AVB/Run1/', 'Experiment2/LSTM-8/No_AVB/Run2/', 'Experiment2/LSTM-8/No_AVB/Run3/', 'Experiment2/LSTM-8/No_AVB/Run4/', 'Experiment2/LSTM-8/No_AVB/Run5/',
    'Experiment2/LSTM-8/No_AVB/Run6/', 'Experiment2/LSTM-8/No_AVB/Run7/', 'Experiment2/LSTM-8/No_AVB/Run8/', 'Experiment2/LSTM-8/No_AVB/Run9/', 'Experiment2/LSTM-8/No_AVB/Run10/',
    'Experiment2/LSTM-8/No_PLM/Run1/', 'Experiment2/LSTM-8/No_PLM/Run2/', 'Experiment2/LSTM-8/No_PLM/Run3/', 'Experiment2/LSTM-8/No_PLM/Run4/', 'Experiment2/LSTM-8/No_PLM/Run5/',
    'Experiment2/LSTM-8/No_PLM/Run6/', 'Experiment2/LSTM-8/No_PLM/Run7/', 'Experiment2/LSTM-8/No_PLM/Run8/', 'Experiment2/LSTM-8/No_PLM/Run9/', 'Experiment2/LSTM-8/No_PLM/Run10/',
    
    'Experiment2/LSTM-16/No_AVB/Run1/', 'Experiment2/LSTM-16/No_AVB/Run2/', 'Experiment2/LSTM-16/No_AVB/Run3/', 'Experiment2/LSTM-16/No_AVB/Run4/', 'Experiment2/LSTM-16/No_AVB/Run5/',
    'Experiment2/LSTM-16/No_AVB/Run6/', 'Experiment2/LSTM-16/No_AVB/Run7/', 'Experiment2/LSTM-16/No_AVB/Run8/', 'Experiment2/LSTM-16/No_AVB/Run9/', 'Experiment2/LSTM-16/No_AVB/Run10/',
    'Experiment2/LSTM-16/No_PLM/Run1/', 'Experiment2/LSTM-16/No_PLM/Run2/', 'Experiment2/LSTM-16/No_PLM/Run3/', 'Experiment2/LSTM-16/No_PLM/Run4/', 'Experiment2/LSTM-16/No_PLM/Run5/',
    'Experiment2/LSTM-16/No_PLM/Run6/', 'Experiment2/LSTM-16/No_PLM/Run7/', 'Experiment2/LSTM-16/No_PLM/Run8/', 'Experiment2/LSTM-16/No_PLM/Run9/', 'Experiment2/LSTM-16/No_PLM/Run10/',

    'Experiment2/LSTM-32/No_AVB/Run1/', 'Experiment2/LSTM-32/No_AVB/Run2/', 'Experiment2/LSTM-32/No_AVB/Run3/', 'Experiment2/LSTM-32/No_AVB/Run4/', 'Experiment2/LSTM-32/No_AVB/Run5/',
    'Experiment2/LSTM-32/No_AVB/Run6/', 'Experiment2/LSTM-32/No_AVB/Run7/', 'Experiment2/LSTM-32/No_AVB/Run8/', 'Experiment2/LSTM-32/No_AVB/Run9/', 'Experiment2/LSTM-32/No_AVB/Run10/',
    'Experiment2/LSTM-32/No_PLM/Run1/', 'Experiment2/LSTM-32/No_PLM/Run2/', 'Experiment2/LSTM-32/No_PLM/Run3/', 'Experiment2/LSTM-32/No_PLM/Run4/', 'Experiment2/LSTM-32/No_PLM/Run5/',
    'Experiment2/LSTM-32/No_PLM/Run6/', 'Experiment2/LSTM-32/No_PLM/Run7/', 'Experiment2/LSTM-32/No_PLM/Run8/', 'Experiment2/LSTM-32/No_PLM/Run9/', 'Experiment2/LSTM-32/No_PLM/Run10/',

    'Experiment2/GRU-8/No_AVB/Run1/', 'Experiment2/GRU-8/No_AVB/Run2/', 'Experiment2/GRU-8/No_AVB/Run3/', 'Experiment2/GRU-8/No_AVB/Run4/', 'Experiment2/GRU-8/No_AVB/Run5/',
    'Experiment2/GRU-8/No_AVB/Run6/', 'Experiment2/GRU-8/No_AVB/Run7/', 'Experiment2/GRU-8/No_AVB/Run8/', 'Experiment2/GRU-8/No_AVB/Run9/', 'Experiment2/GRU-8/No_AVB/Run10/',
    'Experiment2/GRU-8/No_PLM/Run1/', 'Experiment2/GRU-8/No_PLM/Run2/', 'Experiment2/GRU-8/No_PLM/Run3/', 'Experiment2/GRU-8/No_PLM/Run4/', 'Experiment2/GRU-8/No_PLM/Run5/',
    'Experiment2/GRU-8/No_PLM/Run6/', 'Experiment2/GRU-8/No_PLM/Run7/', 'Experiment2/GRU-8/No_PLM/Run8/', 'Experiment2/GRU-8/No_PLM/Run9/', 'Experiment2/GRU-8/No_PLM/Run10/',
    
    'Experiment2/GRU-16/No_AVB/Run1/', 'Experiment2/GRU-16/No_AVB/Run2/', 'Experiment2/GRU-16/No_AVB/Run3/', 'Experiment2/GRU-16/No_AVB/Run4/', 'Experiment2/GRU-16/No_AVB/Run5/',
    'Experiment2/GRU-16/No_AVB/Run6/', 'Experiment2/GRU-16/No_AVB/Run7/', 'Experiment2/GRU-16/No_AVB/Run8/', 'Experiment2/GRU-16/No_AVB/Run9/', 'Experiment2/GRU-16/No_AVB/Run10/',
    'Experiment2/GRU-16/No_PLM/Run1/', 'Experiment2/GRU-16/No_PLM/Run2/', 'Experiment2/GRU-16/No_PLM/Run3/', 'Experiment2/GRU-16/No_PLM/Run4/', 'Experiment2/GRU-16/No_PLM/Run5/',
    'Experiment2/GRU-16/No_PLM/Run6/', 'Experiment2/GRU-16/No_PLM/Run7/', 'Experiment2/GRU-16/No_PLM/Run8/', 'Experiment2/GRU-16/No_PLM/Run9/', 'Experiment2/GRU-16/No_PLM/Run10/',

    'Experiment2/GRU-32/No_AVB/Run1/', 'Experiment2/GRU-32/No_AVB/Run2/', 'Experiment2/GRU-32/No_AVB/Run3/', 'Experiment2/GRU-32/No_AVB/Run4/', 'Experiment2/GRU-32/No_AVB/Run5/',
    'Experiment2/GRU-32/No_AVB/Run6/', 'Experiment2/GRU-32/No_AVB/Run7/', 'Experiment2/GRU-32/No_AVB/Run8/', 'Experiment2/GRU-32/No_AVB/Run9/', 'Experiment2/GRU-32/No_AVB/Run10/',
    'Experiment2/GRU-32/No_PLM/Run1/', 'Experiment2/GRU-32/No_PLM/Run2/', 'Experiment2/GRU-32/No_PLM/Run3/', 'Experiment2/GRU-32/No_PLM/Run4/', 'Experiment2/GRU-32/No_PLM/Run5/',
    'Experiment2/GRU-32/No_PLM/Run6/', 'Experiment2/GRU-32/No_PLM/Run7/', 'Experiment2/GRU-32/No_PLM/Run8/', 'Experiment2/GRU-32/No_PLM/Run9/', 'Experiment2/GRU-32/No_PLM/Run10/'
    ]

    valor = 0
    for sp in saveplace:
        opt.savepath = sp

        if valor/10 == 0:
            opt.model = 'LSTM'
            opt.hidden_size = 8
            inputs_removed = 2
        if valor/10 == 1:
            opt.model = 'LSTM'
            opt.hidden_size = 8
            inputs_removed = 1
        if valor/10 == 2:
            opt.model = 'LSTM'
            opt.hidden_size = 16
            inputs_removed = 2
        if valor/10 == 3:
            opt.model = 'LSTM'
            opt.hidden_size = 16
            inputs_removed = 1
        if valor/10 == 4:
            opt.model = 'LSTM'
            opt.hidden_size = 32
            inputs_removed = 2
        if valor/10 == 5:
            opt.model = 'LSTM'
            opt.hidden_size = 32
            inputs_removed = 1
        if valor/10 == 6:
            opt.model = 'GRU'
            opt.hidden_size = 8
            inputs_removed = 2
        if valor/10 == 7:
            opt.model = 'GRU'
            opt.hidden_size = 8
            inputs_removed = 1
        if valor/10 == 8:
            opt.model = 'GRU'
            opt.hidden_size = 16
            inputs_removed = 2
        if valor/10 == 9:
            opt.model = 'GRU'
            opt.hidden_size = 16
            inputs_removed = 1
        if valor/10 == 10:
            opt.model = 'GRU'
            opt.hidden_size = 32
            inputs_removed = 2
        if valor/10 == 11:
            opt.model = 'GRU'
            opt.hidden_size = 32
            inputs_removed = 1

        ###########################################################################
        # Variables Definition
        ###########################################################################
        input_size = 4
        output_size = 4
        nin = ['time', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
        nout = ['time', 'DB1', 'LUAL', 'PVR', 'VB1']
        neurons = ['time','DB1','LUAL','PVR','VB1','PLML2','PLMR','AVBL','AVBR']
        #nin = ['time', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
        #nout = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR']
        #neurons = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
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
        trainx, trainy = readdata(opt.datapath, train, neurons, nin, nout, input_size, output_size, 'Train/', inputs_removed)
        validx, validy = readdata(opt.datapath, valid, neurons, nin, nout, input_size, output_size, 'Valid/', inputs_removed)
        testx, testy = readdata(opt.datapath, test, neurons, nin, nout, input_size, output_size, 'Test/', inputs_removed)
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