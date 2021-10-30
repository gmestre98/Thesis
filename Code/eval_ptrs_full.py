import argparse
import numpy as np
from keras.models import load_model
from plotread import *

def evaluateresults(model, opt, trainx, trainy, validx, validy, testx, testy, output_size):

    #Evaluate on training, validation and test data
    # train_l = model.evaluate(np.array(trainx), np.array(trainy), batch_size=opt.batch_size,
    #     verbose=1, workers=12, use_multiprocessing=True)
    # valid_l = model.evaluate(np.array(validx), np.array(validy), batch_size=opt.batch_size,
    #     verbose=1, workers=12, use_multiprocessing=True)
    test_l = model.evaluate(np.array(testx), np.array(testy), batch_size=opt.batch_size,
        verbose=1, workers=12, use_multiprocessing=True)
    
    # trainPredict = model.predict(np.array(trainx), batch_size=opt.batch_size, verbose=1,
    #     workers=12, use_multiprocessing=True)
    # plotresults(opt, trainy, trainPredict, opt.model, "/train", opt.savepath, output_size)
    # validPredict = model.predict(np.array(validx), batch_size=opt.batch_size, verbose=1,
    #     workers=12, use_multiprocessing=True)
    # plotresults(opt, validy, validPredict, opt.model, "/valid", opt.savepath, output_size)
    testPredict = model.predict(np.array(testx), batch_size=opt.batch_size, verbose=1,
        workers=12, use_multiprocessing=True)
    plotresults(opt, testy, testPredict, opt.model, "/test", opt.savepath, output_size)

    return test_l #train_l, valid_l, test_l


def plotresults(opt, real, predicted, folder, string, path, out_size):
    #cols = ['DB1_Predicted', 'LUAL_Predicted', 'PVR_Predicted', 'VB1_Predicted']
    cols = ['AS1_Predicted', 'AS7_Predicted', 'DA1_Predicted', 'DA9_Predicted', 'DB1_Predicted', 'DB5_Predicted', 'DD1_Predicted', 'DVA_Predicted',
    'LUAL_Predicted', 'PHCL_Predicted', 'PLML_Predicted', 'PVCL_Predicted', 'PVR_Predicted', 'SIBVL_Predicted', 'VB1_Predicted', 'VD1_Predicted']
    #cols = ['RMED_Predicted', 'RMEL_Predicted', 'RMER_Predicted', 'RMEV_Predicted', 'RMGL_Predicted', 'RMGR_Predicted']
    
    i=0
    for frame in predicted:
        pos = real[i].shape[1]
        for j in range(out_size):
            real[i].insert(
                loc = pos,
                column = cols[j],
                value = frame[:,j]
            )
            pos = pos + 1
        real[i].plot(kind='line')
        Path(path + "results_files").mkdir(parents=True, exist_ok=True)
        real[i].to_csv(
            path + "results_files" + string + str(i) + '_data.dat', sep=' ', header=False)
        if opt.plots_out == True:
            plt.legend(loc='upper right')
            Path(path + "results_plots").mkdir(parents=True, exist_ok=True)
            plt.savefig(path + "results_plots" + string + str(i) + '_response.pdf')
            plt.close()

        i = i + 1

def main():
    ###########################################################################
    # Parser Definition
    ###########################################################################
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-model', choices=['LSTM', 'GRU', 'RNN'], default='GRU')
    parser.add_argument('-datapath', type=str, default="../Datasets/PTRS-20-0_5-16/")
    parser.add_argument('-savepath', type=str, default="Experiment3/GRU-32/PTRS/Run10/")
    parser.add_argument('-extension', type=str, default=".dat")
    parser.add_argument('-batch_size', type=int, default=32)
    parser.add_argument('-plots_in', type=bool, default=False)
    parser.add_argument('-plots_out', type=bool, default=False)
    opt = parser.parse_args()

    ###########################################################################
    # Variables Definition
    ###########################################################################
    input_size = 4
    output_size = 16
    inputs_removed = 0
    #nin = ['time', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
    #nout = ['time', 'DB1', 'LUAL', 'PVR', 'VB1']
    #neurons = ['time','DB1','LUAL','PVR','VB1','PLML2','PLMR','AVBL','AVBR']
    nin = ['time', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
    nout = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
    neurons = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1', 'PLML2','PLMR','AVBL','AVBR']
    #nin = ['time', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
    #nout = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR']
    #neurons = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']

    ###########################################################################
    # Read data
    ###########################################################################
    train, valid, test = getdata(opt.datapath, opt.extension)
    trainx, trainy = readdata(opt.datapath, train, neurons, nin, nout, input_size, output_size, 'Train/', inputs_removed)
    validx, validy = readdata(opt.datapath, valid, neurons, nin, nout, input_size, output_size, 'Valid/', inputs_removed)
    testx, testy = readdata(opt.datapath, test, neurons, nin, nout, input_size, output_size, 'Test/', inputs_removed)
    if opt.plots_in:
        plotdata(trainx, '/train_data', '/x', opt.model, opt.savepath)
        plotdata(trainy, '/train_data', '/y', opt.model, opt.savepath)
        plotdata(validx, '/valid_data', '/x', opt.model, opt.savepath)
        plotdata(validy, '/valid_data', '/y', opt.model, opt.savepath)
        plotdata(testx, '/test_data', '/x', opt.model, opt.savepath)
        plotdata(testy, '/test_data', '/y', opt.model, opt.savepath)
    ###########################################################################
    # Load Model and Evaluate
    ###########################################################################
    model = load_model(opt.savepath + 'model.h5')
    model.summary()
    ltt = evaluateresults(
        model, opt, trainx, trainy, validx, validy, testx, testy, output_size)
    #print(str(lt))
    #print(str(lv))
    print(str(ltt))

if __name__ == "__main__":
    main()