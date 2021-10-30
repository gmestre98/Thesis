import pandas as pd
import matplotlib.pyplot as plt

##################################################################################################
##################################################################################################
# Figure 2.3 - 3 Example input-output PTRS
##################################################################################################
##################################################################################################
datafiles = ["../Datasets/PTRS-20-0_5-4/Train/Sequence04.dat", "../Datasets/PTRS-20-0_5-4/Valid/Sequence15.dat", "../Datasets/PTRS-20-0_5-4/Test/Sequence18.dat"]
nin = ['time', 'PLML', 'PLMR', 'AVBL', 'AVBR']
nout = ['time', 'DB1', 'LUAL', 'PVR', 'VB1']
neurons = ['time','DB1','LUAL','PVR','VB1','PLML','PLMR','AVBL','AVBR']
sequence = ["Train-1", "Valid-4", "Test-1"]

i=0
for seq in datafiles:
    df = pd.read_csv(seq, sep="\s+", names=neurons)
    df = df.set_index('time')
    x = df.drop(columns = nout[1:5])
    y = df.drop(columns = nin[1:5])

    x.plot(kind='line')
    plt.legend(loc='upper right')
    plt.xlabel("Time [sec]")
    plt.ylabel("Voltage [V]")
    plt.savefig("Figures/Fig2-3-Inputs-" + sequence[i] + "_plots.pdf")
    plt.close()

    y.plot(kind='line')
    plt.legend(loc='upper right')
    plt.xlabel("Time [sec]")
    plt.ylabel("Voltage [V]")
    plt.savefig("Figures/Fig2-3-Outputs-" + sequence[i] + "_plots.pdf")
    plt.close()

    i = i + 1

##################################################################################################
##################################################################################################
# Figure 2.4 - 3 Example input-output Nictation
##################################################################################################
##################################################################################################
datafiles = ["../Datasets/Nictation-20-0_5-6/Train/Sequence01.dat", "../Datasets/Nictation-20-0_5-6/Valid/Sequence23.dat", "../Datasets/Nictation-20-0_5-6/Test/Sequence37.dat"]
nin = ['time', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
nout = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR']
neurons = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
sequence = ["Train-0", "Valid-2", "Test-6"]

i=0
for seq in datafiles:
    df = pd.read_csv(seq, sep="\s+", names=neurons)
    df = df.set_index('time')
    x = df.drop(columns = nout[1:7])
    y = df.drop(columns = nin[1:7])

    x.plot(kind='line')
    plt.legend(loc='upper right')
    plt.xlabel("Time [sec]")
    plt.ylabel("Voltage [V]")
    plt.savefig("Figures/Fig2-4-Inputs-" + sequence[i] + "_plots.pdf")
    plt.close()

    y.plot(kind='line')
    plt.legend(loc='upper right')
    plt.xlabel("Time [sec]")
    plt.ylabel("Voltage [V]")
    plt.savefig("Figures/Fig2-4-Outputs-" + sequence[i] + "_plots.pdf")
    plt.close()

    i = i + 1

##################################################################################################
##################################################################################################
# Figure 4.3 - Example of RNN outputs
##################################################################################################
##################################################################################################
output_sequence = "../Hyperparameters/RNN/Size/16/Run1/results_files/valid5_data.dat"
cols = [["DB1", "DB1_Predicted"], ["LUAL", "LUAL_Predicted"],
        ["PVR", "PVR_Predicted"], ["VB1", "VB1_Predicted"]]
headers = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'DB1_Predicted', 'LUAL_Predicted',
            'PVR_Predicted', 'VB1_Predicted',]
color = ["red", "black"]

for col in cols:
    df = pd.read_csv(output_sequence, sep = "\s+", names=headers)
    df = df.set_index('time')

    fig, ax = plt.subplots()
    df[col[0]].plot(ax=ax, kind='line', color=color[0])
    df[col[1]].plot(ax=ax, kind='line', color=color[1])
    plt.xlabel("Time [sec]")
    plt.ylabel("Voltage [V]")
    plt.legend()
    plt.savefig('Figures/Fig-4-3-' + col[0] + '.pdf', bbox_inches='tight')
    plt.close()

##################################################################################################
##################################################################################################
# Figure 4.4 - Example of LSTM outputs
##################################################################################################
##################################################################################################
output_sequence = "../Hyperparameters/LSTM/Size/16/Run1/results_files/valid5_data.dat"
cols = [["DB1", "DB1_Predicted"], ["LUAL", "LUAL_Predicted"],
        ["PVR", "PVR_Predicted"], ["VB1", "VB1_Predicted"]]
headers = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'DB1_Predicted', 'LUAL_Predicted',
            'PVR_Predicted', 'VB1_Predicted',]
color = ["red", "black"]

for col in cols:
    df = pd.read_csv(output_sequence, sep = "\s+", names=headers)
    df = df.set_index('time')

    fig, ax = plt.subplots()
    df[col[0]].plot(ax=ax, kind='line', color=color[0])
    df[col[1]].plot(ax=ax, kind='line', color=color[1])
    plt.xlabel("Time [sec]")
    plt.ylabel("Voltage [V]")
    plt.legend()
    plt.savefig('Figures/Fig-4-4-' + col[0] + '.pdf', bbox_inches='tight')
    plt.close()

##################################################################################################
##################################################################################################
# Figure 4.5 - Example of GRU outputs
##################################################################################################
##################################################################################################
output_sequence = "../Hyperparameters/GRU/Size/16/Run1/results_files/valid5_data.dat"
cols = [["DB1", "DB1_Predicted"], ["LUAL", "LUAL_Predicted"],
        ["PVR", "PVR_Predicted"], ["VB1", "VB1_Predicted"]]
headers = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'DB1_Predicted', 'LUAL_Predicted',
            'PVR_Predicted', 'VB1_Predicted',]
color = ["red", "black"]

for col in cols:
    df = pd.read_csv(output_sequence, sep = "\s+", names=headers)
    df = df.set_index('time')

    fig, ax = plt.subplots()
    df[col[0]].plot(ax=ax, kind='line', color=color[0])
    df[col[1]].plot(ax=ax, kind='line', color=color[1])
    plt.xlabel("Time [sec]")
    plt.ylabel("Voltage [V]")
    plt.legend()
    plt.savefig('Figures/Fig-4-5-' + col[0] + '.pdf', bbox_inches='tight')
    plt.close()


##################################################################################################
##################################################################################################
# Figure 5.1 - Example No AVB neurons
##################################################################################################
##################################################################################################
output_sequence = "../Experiment2/Gru-8/No_AVB/Run1/results_files/test5_data.dat"
cols = [["DB1", "DB1_Predicted"], ["LUAL", "LUAL_Predicted"],
        ["PVR", "PVR_Predicted"], ["VB1", "VB1_Predicted"]]
headers = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'DB1_Predicted', 'LUAL_Predicted',
            'PVR_Predicted', 'VB1_Predicted',]
color = ["red", "black"]

for col in cols:
    df = pd.read_csv(output_sequence, sep = "\s+", names=headers)
    df = df.set_index('time')

    fig, ax = plt.subplots()
    df[col[0]].plot(ax=ax, kind='line', color=color[0])
    df[col[1]].plot(ax=ax, kind='line', color=color[1])
    plt.xlabel("Time [sec]")
    plt.ylabel("Voltage [V]")
    plt.legend()
    plt.savefig('Figures/Fig-5-1-' + col[0] + '.pdf', bbox_inches='tight')
    plt.close()

##################################################################################################
##################################################################################################
# Figure 5.2 - Example No AVB neurons
##################################################################################################
##################################################################################################
output_sequence = "../Experiment2/Gru-8/No_PLM/Run1/results_files/test2_data.dat"
cols = [["DB1", "DB1_Predicted"], ["LUAL", "LUAL_Predicted"],
        ["PVR", "PVR_Predicted"], ["VB1", "VB1_Predicted"]]
headers = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'DB1_Predicted', 'LUAL_Predicted',
            'PVR_Predicted', 'VB1_Predicted']
color = ["red", "black"]

for col in cols:
    df = pd.read_csv(output_sequence, sep = "\s+", names=headers)
    df = df.set_index('time')

    fig, ax = plt.subplots()
    df[col[0]].plot(ax=ax, kind='line', color=color[0])
    df[col[1]].plot(ax=ax, kind='line', color=color[1])
    plt.xlabel("Time [sec]")
    plt.ylabel("Voltage [V]")
    plt.legend()
    plt.savefig('Figures/Fig-5-2-' + col[0] + '.pdf', bbox_inches='tight')
    plt.close()

##################################################################################################
##################################################################################################
# Figure 5.3 - Example No IL2D neurons
##################################################################################################
##################################################################################################
output_sequence = "../Experiment2/Gru-8/No_IL2D/Run1/results_files/test6_data.dat"
cols = [['RMED', 'RMED_Predicted'], ['RMEL', 'RMEL_Predicted'], ['RMER', 'RMER_Predicted'],
        ['RMEV', 'RMEV_Predicted'], ['RMGL', 'RMGL_Predicted'], ['RMGR', 'RMGR_Predicted']]
headers = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMED_Predicted', 'RMEL_Predicted',
            'RMER_Predicted', 'RMEV_Predicted', 'RMGL_Predicted', 'RMGR_Predicted']
color = ["red", "black"]

for col in cols:
    df = pd.read_csv(output_sequence, sep = "\s+", names=headers)
    df = df.set_index('time')

    fig, ax = plt.subplots()
    df[col[0]].plot(ax=ax, kind='line', color=color[0])
    df[col[1]].plot(ax=ax, kind='line', color=color[1])
    plt.xlabel("Time [sec]")
    plt.ylabel("Voltage [V]")
    plt.legend()
    plt.savefig('Figures/Fig-5-3-' + col[0] + '.pdf', bbox_inches='tight')
    plt.close()

##################################################################################################
##################################################################################################
# Figure 5.4 - Example No IL2 neurons
##################################################################################################
##################################################################################################
output_sequence = "../Experiment2/Gru-8/No_IL2/Run1/results_files/test9_data.dat"
cols = [['RMED', 'RMED_Predicted'], ['RMEL', 'RMEL_Predicted'], ['RMER', 'RMER_Predicted'],
        ['RMEV', 'RMEV_Predicted'], ['RMGL', 'RMGL_Predicted'], ['RMGR', 'RMGR_Predicted']]
headers = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMED_Predicted', 'RMEL_Predicted',
            'RMER_Predicted', 'RMEV_Predicted', 'RMGL_Predicted', 'RMGR_Predicted']
color = ["red", "black"]

for col in cols:
    df = pd.read_csv(output_sequence, sep = "\s+", names=headers)
    df = df.set_index('time')

    fig, ax = plt.subplots()
    df[col[0]].plot(ax=ax, kind='line', color=color[0])
    df[col[1]].plot(ax=ax, kind='line', color=color[1])
    plt.xlabel("Time [sec]")
    plt.ylabel("Voltage [V]")
    plt.legend()
    plt.savefig('Figures/Fig-5-4-' + col[0] + '.pdf', bbox_inches='tight')
    plt.close()

##################################################################################################
##################################################################################################
# Figure 5.5 - Example Full Output PTRS
##################################################################################################
##################################################################################################
output_sequence = "../Experiment3/Gru-16/PTRS/Run1/results_files/test2_data.dat"
cols = [["AS1", "AS1_Predicted", "AS7", "AS7_Predicted"], ["DA1", "DA1_Predicted", "DA9", "DA9_Predicted"],
        ["DB1", "DB1_Predicted", "DB5", "DB5_Predicted"], ["DD1", "DD1_Predicted", "DVA", "DVA_Predicted"],
        ["LUAL", "LUAL_Predicted", "PHCL", "PHCL_Predicted"], ["PLML", "PLML_Predicted", "PVCL", "PVCL_Predicted"],
        ["PVR", "PVR_Predicted", "SIBVL", "SIBVL_Predicted"], ["VB1", "VB1_Predicted", "VD1", "VD1_Predicted"]]
headers = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML',
    'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1', 'AS1_Predicted', 'AS7_Predicted', 'DA1_Predicted',
    'DA9_Predicted', 'DB1_Predicted', 'DB5_Predicted', 'DD1_Predicted', 'DVA_Predicted', 'LUAL_Predicted',
    'PHCL_Predicted', 'PLML_Predicted', 'PVCL_Predicted', 'PVR_Predicted', 'SIBVL_Predicted', 'VB1_Predicted',
    'VD1_Predicted']
color = ["red", "black", "orange", "blue"]

for col in cols:
    df = pd.read_csv(output_sequence, sep = "\s+", names=headers)
    df = df.set_index('time')

    fig, ax = plt.subplots()
    df[col[0]].plot(ax=ax, kind='line', color=color[0])
    df[col[1]].plot(ax=ax, kind='line', color=color[1])
    df[col[2]].plot(ax=ax, kind='line', color=color[2])
    df[col[3]].plot(ax=ax, kind='line', color=color[3])
    plt.xlabel("Time [sec]")
    plt.ylabel("Voltage [V]")
    plt.legend()
    plt.savefig('Figures/Fig-5-5-' + col[0] + '.pdf', bbox_inches='tight')
    plt.close()

##################################################################################################
##################################################################################################
# Figure 5.6 - Example Full Output Nictation
##################################################################################################
##################################################################################################
output_sequence = "../Experiment3/Gru-16/Nictation/Run1/results_files/test6_data.dat"
cols = [["RMED", "RMED_Predicted", "RMEL", "RMEL_Predicted"], ["RMER", "RMER_Predicted", "RMEV", "RMEV_Predicted"],
        ["RMGL", "RMGL_Predicted", "RMGR", "RMGR_Predicted"], ["RMHL", "RMHL_Predicted", "RMHR", "RMHR_Predicted"],
        ["SMDDL", "SMDDL_Predicted", "SMDDR", "SMDDR_Predicted"], ["SMDVL", "SMDVL_Predicted", "SMDVR", "SMDVR_Predicted"]]
headers = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR',
    'SMDVL', 'SMDVR', 'RMED_Predicted', 'RMEL_Predicted', 'RMER_Predicted', 'RMEV_Predicted', 'RMGL_Predicted',
    'RMGR_Predicted', 'RMHL_Predicted', 'RMHR_Predicted', 'SMDDL_Predicted', 'SMDDR_Predicted',
    'SMDVL_Predicted', 'SMDVR_Predicted']
color = ["red", "black", "orange", "blue"]

for col in cols:
    df = pd.read_csv(output_sequence, sep = "\s+", names=headers)
    df = df.set_index('time')

    fig, ax = plt.subplots()
    df[col[0]].plot(ax=ax, kind='line', color=color[0])
    df[col[1]].plot(ax=ax, kind='line', color=color[1])
    df[col[2]].plot(ax=ax, kind='line', color=color[2])
    df[col[3]].plot(ax=ax, kind='line', color=color[3])
    plt.xlabel("Time [sec]")
    plt.ylabel("Voltage [V]")
    plt.legend()
    plt.savefig('Figures/Fig-5-6-' + col[0] + '.pdf', bbox_inches='tight')
    plt.close()

##################################################################################################
##################################################################################################
# Figure 5.7 - Example 2 Behaviors
##################################################################################################
##################################################################################################
output_sequence = "../Experiment4/Gru-16/Run1/results_files/test2_data.dat"
cols = [["AS1", "AS1_Predicted", "AS7", "AS7_Predicted"], ["DA1", "DA1_Predicted", "DA9", "DA9_Predicted"],
    ["DB1", "DB1_Predicted", "DB5", "DB5_Predicted"], ["DD1", "DD1_Predicted", "DVA", "DVA_Predicted"],
    ["LUAL", "LUAL_Predicted", "PHCL", "PHCL_Predicted"], ["PLML", "PLML_Predicted", "PVCL", "PVCL_Predicted"],
    ["PVR", "PVR_Predicted", "SIBVL", "SIBVL_Predicted"], ["VB1", "VB1_Predicted", "VD1", "VD1_Predicted"],
    ["RMED", "RMED_Predicted", "RMEL", "RMEL_Predicted"], ["RMER", "RMER_Predicted", "RMEV", "RMEV_Predicted"],
    ["RMGL", "RMGL_Predicted", "RMGR", "RMGR_Predicted"], ["RMHL", "RMHL_Predicted", "RMHR", "RMHR_Predicted"],
    ["SMDDL", "SMDDL_Predicted", "SMDDR", "SMDDR_Predicted"], ["SMDVL", "SMDVL_Predicted", "SMDVR", "SMDVR_Predicted"]]
headers = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML',
    'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL',
    'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR', 'AS1_Predicted', 'AS7_Predicted', 'DA1_Predicted',
    'DA9_Predicted', 'DB1_Predicted', 'DB5_Predicted', 'DD1_Predicted', 'DVA_Predicted', 'LUAL_Predicted',
    'PHCL_Predicted', 'PLML_Predicted', 'PVCL_Predicted', 'PVR_Predicted', 'SIBVL_Predicted', 'VB1_Predicted',
    'VD1_Predicted', 'RMED_Predicted', 'RMEL_Predicted', 'RMER_Predicted', 'RMEV_Predicted', 'RMGL_Predicted',
    'RMGR_Predicted', 'RMHL_Predicted', 'RMHR_Predicted', 'SMDDL_Predicted', 'SMDDR_Predicted',
    'SMDVL_Predicted', 'SMDVR_Predicted']
color = ["red", "black", "orange", "blue"]

for col in cols:
    df = pd.read_csv(output_sequence, sep = "\s+", names=headers)
    df = df.set_index('time')

    fig, ax = plt.subplots()
    df[col[0]].plot(ax=ax, kind='line', color=color[0])
    df[col[1]].plot(ax=ax, kind='line', color=color[1])
    df[col[2]].plot(ax=ax, kind='line', color=color[2])
    df[col[3]].plot(ax=ax, kind='line', color=color[3])
    plt.xlabel("Time [sec]")
    plt.ylabel("Voltage [V]")
    plt.legend()
    plt.savefig('Figures/Fig-5-7-' + col[0] + '.pdf', bbox_inches='tight')
    plt.close()

##################################################################################################
##################################################################################################
# Figure 5.8 - Example 2 Behaviors
##################################################################################################
##################################################################################################
output_sequence = "../Experiment4/Gru-16/Run1/results_files/test16_data.dat"
cols = [["AS1", "AS1_Predicted", "AS7", "AS7_Predicted"], ["DA1", "DA1_Predicted", "DA9", "DA9_Predicted"],
    ["DB1", "DB1_Predicted", "DB5", "DB5_Predicted"], ["DD1", "DD1_Predicted", "DVA", "DVA_Predicted"],
    ["LUAL", "LUAL_Predicted", "PHCL", "PHCL_Predicted"], ["PLML", "PLML_Predicted", "PVCL", "PVCL_Predicted"],
    ["PVR", "PVR_Predicted", "SIBVL", "SIBVL_Predicted"], ["VB1", "VB1_Predicted", "VD1", "VD1_Predicted"],
    ["RMED", "RMED_Predicted", "RMEL", "RMEL_Predicted"], ["RMER", "RMER_Predicted", "RMEV", "RMEV_Predicted"],
    ["RMGL", "RMGL_Predicted", "RMGR", "RMGR_Predicted"], ["RMHL", "RMHL_Predicted", "RMHR", "RMHR_Predicted"],
    ["SMDDL", "SMDDL_Predicted", "SMDDR", "SMDDR_Predicted"], ["SMDVL", "SMDVL_Predicted", "SMDVR", "SMDVR_Predicted"]]
headers = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML',
    'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL',
    'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR', 'AS1_Predicted', 'AS7_Predicted', 'DA1_Predicted',
    'DA9_Predicted', 'DB1_Predicted', 'DB5_Predicted', 'DD1_Predicted', 'DVA_Predicted', 'LUAL_Predicted',
    'PHCL_Predicted', 'PLML_Predicted', 'PVCL_Predicted', 'PVR_Predicted', 'SIBVL_Predicted', 'VB1_Predicted',
    'VD1_Predicted', 'RMED_Predicted', 'RMEL_Predicted', 'RMER_Predicted', 'RMEV_Predicted', 'RMGL_Predicted',
    'RMGR_Predicted', 'RMHL_Predicted', 'RMHR_Predicted', 'SMDDL_Predicted', 'SMDDR_Predicted',
    'SMDVL_Predicted', 'SMDVR_Predicted']
color = ["red", "black", "orange", "blue"]

for col in cols:
    df = pd.read_csv(output_sequence, sep = "\s+", names=headers)
    df = df.set_index('time')

    fig, ax = plt.subplots()
    df[col[0]].plot(ax=ax, kind='line', color=color[0])
    df[col[1]].plot(ax=ax, kind='line', color=color[1])
    df[col[2]].plot(ax=ax, kind='line', color=color[2])
    df[col[3]].plot(ax=ax, kind='line', color=color[3])
    plt.xlabel("Time [sec]")
    plt.ylabel("Voltage [V]")
    plt.legend()
    plt.savefig('Figures/Fig-5-8-' + col[0] + '.pdf', bbox_inches='tight')
    plt.close()