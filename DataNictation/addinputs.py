import pandas as pd

simulationtime = 500
ts = 0.05

###########################################################################
############################ Create Inputs ################################
###########################################################################
# pulse4_8nA
pulse4_8nA = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 100
amplitude = 4.8
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse4_8nA[int(t/ts)] = amplitude 
    t += ts

# pulse4_8nA_50ms_delay100_per100
pulse4_8nA_50ms_delay100_per100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 50
amplitude = 4.8
durnoamp = 50
while (t <= simulationtime):
    if ((t >= delay) and (t < delay + duration)):
        pulse4_8nA_50ms_delay100_per100[int(t/ts)] = amplitude
    elif ((t >= delay + duration + durnoamp) and (t < delay + 2*duration + durnoamp)):
        pulse4_8nA_50ms_delay100_per100[int(t/ts)] = amplitude
    elif ((t >= delay + 2*duration + 2*durnoamp) and (t < delay + 3*duration + 2*durnoamp)):
        pulse4_8nA_50ms_delay100_per100[int(t/ts)] = amplitude
    t += ts

# pulse0_to_4_8nA_to_0
pulse0_to_4_8nA_to_0 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 50
amplitude = 4.8
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_4_8nA_to_0[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < 2*duration + delay)):
        pulse0_to_4_8nA_to_0[int(t/ts)] = amplitude * (2 - (t-delay)/duration)
    t += ts

# pulse0_to_4_8nA_delay0_per150
pulse0_to_4_8nA_delay0_per150 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 100
stay0 = 50
amplitude = 4.8
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_4_8nA_delay0_per150[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay + stay0) and (t < 2*duration + delay + stay0)):
        pulse0_to_4_8nA_delay0_per150[int(t/ts)] = amplitude * (t-delay-duration-stay0)/duration
    elif ((t >= 2*duration + delay + 2*stay0) and (t < 3*duration + delay + 2*stay0)):
        pulse0_to_4_8nA_delay0_per150[int(t/ts)] = amplitude * (t-delay-2*duration-2*stay0)/duration
    t += ts

# pulse4_8nA_delay0
pulse4_8nA_delay0 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 100
amplitude = 4.8
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse4_8nA_delay0[int(t/ts)] = amplitude 
    t += ts

# pulse0_to_4_8nA_to_0_per100
pulse0_to_4_8nA_to_0_per100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 50
amplitude = 4.8
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_4_8nA_to_0_per100[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < 2*duration + delay)):
        pulse0_to_4_8nA_to_0_per100[int(t/ts)] = amplitude * (2 - (t-delay)/duration)
    elif ((t >= 2*duration + delay) and (t < 3*duration + delay)):
        pulse0_to_4_8nA_to_0_per100[int(t/ts)] = amplitude * (t-delay-2*duration)/duration
    elif ((t >= 3*duration + delay) and (t < 4*duration + delay)):
        pulse0_to_4_8nA_to_0_per100[int(t/ts)] = amplitude * (2 - (t-delay-2*duration)/duration)
    elif ((t >= 4*duration + delay) and (t < 5*duration + delay)):
        pulse0_to_4_8nA_to_0_per100[int(t/ts)] = amplitude * (t-delay-4*duration)/duration
    elif ((t >= 5*duration + delay) and (t < 6*duration + delay)):
        pulse0_to_4_8nA_to_0_per100[int(t/ts)] = amplitude * (2 - (t-delay-4*duration)/duration)

    t += ts

# pulse0_to_4_8nA
pulse0_to_4_8nA = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 100
amplitude = 4.8
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_4_8nA[int(t/ts)] = amplitude * (t-delay)/duration
    t += ts

# pulse0_to_4_8nA_per150
pulse0_to_4_8nA_per150 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 100
stay0 = 50
amplitude = 4.8
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_4_8nA_per150[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay + stay0) and (t < 2*duration + delay + stay0)):
        pulse0_to_4_8nA_per150[int(t/ts)] = amplitude * (t-delay-duration-stay0)/duration
    elif ((t >= 2*duration + delay + 2*stay0) and (t < 3*duration + delay + 2*stay0)):
        pulse0_to_4_8nA_per150[int(t/ts)] = amplitude * (t-delay-2*duration-2*stay0)/duration
    t += ts

# pulse4_8nA_50ms_delay100
pulse4_8nA_50ms_delay100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 50
amplitude = 4.8
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse4_8nA_50ms_delay100[int(t/ts)] = amplitude 
    t += ts

# pulse0_to_4_8nA_delay0
pulse0_to_4_8nA_delay0 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 100
amplitude = 4.8
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_4_8nA_delay0[int(t/ts)] = amplitude * (t-delay)/duration
    t += ts

# pulse4_8_nA_delay0
pulse4_8_nA_delay0 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 100
amplitude = 4.8
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse4_8_nA_delay0[int(t/ts)] = amplitude 
    t += ts

# pulse0_to_4_8nA_plus50
pulse0_to_4_8nA_plus50 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 50
durampmax = 50
amplitude = 4.8
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_4_8nA_plus50[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < delay + duration + durampmax)):
        pulse0_to_4_8nA_plus50[int(t/ts)] = amplitude
    t += ts

# pulse4_8nA_30ms_delay100
pulse4_8nA_30ms_delay100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 30
amplitude = 4.8
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse4_8nA_30ms_delay100[int(t/ts)] = amplitude
    t += ts

# pulse4_8nA_200ms_delay100
pulse4_8nA_200ms_delay100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 200
amplitude = 4.8
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse4_8nA_200ms_delay100[int(t/ts)] = amplitude 
    t += ts

# pulse_0_to_4_8nA_to_0_per100
pulse_0_to_4_8nA_to_0_per100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 50
amplitude = 4.8
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse_0_to_4_8nA_to_0_per100[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < 2*duration + delay)):
        pulse_0_to_4_8nA_to_0_per100[int(t/ts)] = amplitude * (2 - (t-delay)/duration)
    elif ((t >= 2*duration + delay) and (t < 3*duration + delay)):
        pulse_0_to_4_8nA_to_0_per100[int(t/ts)] = amplitude * (t-delay-2*duration)/duration
    elif ((t >= 3*duration + delay) and (t < 4*duration + delay)):
        pulse_0_to_4_8nA_to_0_per100[int(t/ts)] = amplitude * (2 - (t-delay-2*duration)/duration)
    elif ((t >= 4*duration + delay) and (t < 5*duration + delay)):
        pulse_0_to_4_8nA_to_0_per100[int(t/ts)] = amplitude * (t-delay-4*duration)/duration
    elif ((t >= 5*duration + delay) and (t < 6*duration + delay)):
        pulse_0_to_4_8nA_to_0_per100[int(t/ts)] = amplitude * (2 - (t-delay-4*duration)/duration)
    t += ts

# pulse0_to_4_8nA_to_0_delay0_per100
pulse0_to_4_8nA_to_0_delay0_per100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 50
amplitude = 4.8
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_4_8nA_to_0_delay0_per100[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < 2*duration + delay)):
        pulse0_to_4_8nA_to_0_delay0_per100[int(t/ts)] = amplitude * (2 - (t-delay)/duration)
    elif ((t >= 2*duration + delay) and (t < 3*duration + delay)):
        pulse0_to_4_8nA_to_0_delay0_per100[int(t/ts)] = amplitude * (t-delay-2*duration)/duration
    elif ((t >= 3*duration + delay) and (t < 4*duration + delay)):
        pulse0_to_4_8nA_to_0_delay0_per100[int(t/ts)] = amplitude * (2 - (t-delay-2*duration)/duration)
    elif ((t >= 4*duration + delay) and (t < 5*duration + delay)):
        pulse0_to_4_8nA_to_0_delay0_per100[int(t/ts)] = amplitude * (t-delay-4*duration)/duration
    elif ((t >= 5*duration + delay) and (t < 6*duration + delay)):
        pulse0_to_4_8nA_to_0_delay0_per100[int(t/ts)] = amplitude * (2 - (t-delay-4*duration)/duration)
    t += ts

# pulse0_to_4_8nA_delay50
pulse0_to_4_8nA_delay50 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 50
duration = 100
amplitude = 4.8
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_4_8nA_delay50[int(t/ts)] = amplitude * (t-delay)/duration
    t += ts

# pulse0_to_4_8nA_to_0_delay50
pulse0_to_4_8nA_to_0_delay50 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 50
duration = 50
amplitude = 4.8
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_4_8nA_to_0_delay50[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < 2*duration + delay)):
        pulse0_to_4_8nA_to_0_delay50[int(t/ts)] = amplitude * (2 - (t-delay)/duration)
    t += ts

# pulse0_to_4_8nA_to_0_delay0
pulse0_to_4_8nA_to_0_delay0 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 50
amplitude = 4.8
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_4_8nA_to_0_delay0[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < 2*duration + delay)):
        pulse0_to_4_8nA_to_0_delay0[int(t/ts)] = amplitude * (2 - (t-delay)/duration)
    t += ts

# pulse4_8nA_50ms_delay0
pulse4_8nA_50ms_delay0 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 50
amplitude = 4.8
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse4_8nA_50ms_delay0[int(t/ts)] = amplitude 
    t += ts

# pulse4_8nA_10ms_delay100_per20
pulse4_8nA_10ms_delay100_per20 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 10
amplitude = 4.8
durnoamp = 10
while (t <= simulationtime):
    if ((t >= delay) and (t < delay + duration)):
        pulse4_8nA_10ms_delay100_per20[int(t/ts)] = amplitude
    elif ((t >= delay + duration + durnoamp) and (t < delay + 2*duration + durnoamp)):
        pulse4_8nA_10ms_delay100_per20[int(t/ts)] = amplitude
    elif ((t >= delay + 2*duration + 2*durnoamp) and (t < delay + 3*duration + 2*durnoamp)):
        pulse4_8nA_10ms_delay100_per20[int(t/ts)] = amplitude
    t += ts

# pulse0_to_4_8nA_50ms_delay0
pulse0_to_4_8nA_50ms_delay0 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 50
amplitude = 4.8
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_4_8nA_50ms_delay0[int(t/ts)] = amplitude * (t-delay)/duration
    t += ts







###########################################################################
########################## Add + Write Files ##############################
###########################################################################
########################################################################################################################################################################
# Sequence 01
file = "Sequence01.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA
df['IL2DR'] = pulse4_8nA
df['IL2L'] = pulse4_8nA
df['IL2R'] = pulse4_8nA
df['IL2VL'] = pulse4_8nA
df['IL2VR'] = pulse4_8nA
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/train/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/train/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/train/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/train/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/train/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/train/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence 02
file = "Sequence02.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA_50ms_delay100_per100
df['IL2DR'] = pulse4_8nA_50ms_delay100_per100
df['IL2L'] = pulse4_8nA_50ms_delay100_per100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse4_8nA_50ms_delay100_per100
df['IL2VR'] = pulse4_8nA_50ms_delay100_per100
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/train/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/train/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/train/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/train/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/train/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/train/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence 03
file = "Sequence03.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_to_0
df['IL2DR'] = pulse0_to_4_8nA_to_0
df['IL2L'] = pulse0_to_4_8nA_to_0
df['IL2R'] = pulse0_to_4_8nA_to_0
df['IL2VL'] = pulse0_to_4_8nA_to_0
df['IL2VR'] = pulse0_to_4_8nA_to_0
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/train/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/train/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/train/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/train/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/train/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/train/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence 04
file = "Sequence04.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_delay0_per150
df['IL2DR'] = pulse0_to_4_8nA_delay0_per150
df['IL2L'] = pulse0_to_4_8nA_delay0_per150
df['IL2R'] = pulse0_to_4_8nA_delay0_per150
df['IL2VL'] = pulse0_to_4_8nA_delay0_per150
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/train/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/train/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/train/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/train/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/train/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/train/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence 05
file = "Sequence05.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA_delay0
df['IL2DR'] = pulse4_8nA_delay0
df['IL2L'] = pulse0_to_4_8nA_delay0_per150
df['IL2R'] = pulse0_to_4_8nA_to_0_per100
df['IL2VL'] = pulse0_to_4_8nA_delay0_per150
df['IL2VR'] = pulse0_to_4_8nA_to_0_per100
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/train/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/train/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/train/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/train/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/train/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/train/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence 06
file = "Sequence06.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA_delay0
df['IL2DR'] = pulse0_to_4_8nA_delay0_per150
df['IL2L'] = pulse0_to_4_8nA_delay0_per150
df['IL2R'] = pulse0_to_4_8nA_to_0_per100
df['IL2VL'] = pulse0_to_4_8nA_delay0_per150
df['IL2VR'] = pulse0_to_4_8nA_to_0_per100
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/train/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/train/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/train/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/train/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/train/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/train/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence 07
file = "Sequence07.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA_50ms_delay100_per100
df['IL2DR'] = pulse4_8nA_50ms_delay100_per100
df['IL2L'] = pulse0_to_4_8nA
df['IL2R'] = pulse0_to_4_8nA
df['IL2VL'] = pulse0_to_4_8nA_to_0
df['IL2VR'] = pulse0_to_4_8nA_to_0
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/train/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/train/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/train/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/train/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/train/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/train/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence 08
file = "Sequence08.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA_50ms_delay100_per100
df['IL2DR'] = pulse4_8nA_50ms_delay100_per100
df['IL2L'] = pulse0_to_4_8nA_per150
df['IL2R'] = pulse0_to_4_8nA_per150
df['IL2VL'] = pulse0_to_4_8nA_to_0_per100
df['IL2VR'] = pulse0_to_4_8nA_to_0_per100
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/train/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/train/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/train/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/train/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/train/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/train/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence 09
file = "Sequence09.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA
df['IL2DR'] = pulse0_to_4_8nA_to_0
df['IL2L'] = pulse4_8nA
df['IL2R'] = pulse0_to_4_8nA_to_0
df['IL2VL'] = pulse4_8nA
df['IL2VR'] = pulse0_to_4_8nA_to_0
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/train/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/train/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/train/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/train/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/train/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/train/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence 10
file = "Sequence10.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA_50ms_delay100_per100
df['IL2DR'] = pulse0_to_4_8nA_to_0_per100
df['IL2L'] = pulse4_8nA_50ms_delay100_per100
df['IL2R'] = pulse0_to_4_8nA_to_0_per100
df['IL2VL'] = pulse4_8nA_50ms_delay100_per100
df['IL2VR'] = pulse0_to_4_8nA_to_0_per100
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/train/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/train/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/train/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/train/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/train/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/train/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence 11
file = "Sequence11.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_to_0_per100
df['IL2DR'] = pulse0_to_4_8nA
df['IL2L'] = pulse4_8nA_50ms_delay100_per100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA_to_0_per100
df['IL2VR'] = pulse0_to_4_8nA
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/train/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/train/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/train/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/train/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/train/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/train/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence 12
file = "Sequence12.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_to_0
df['IL2DR'] = pulse0_to_4_8nA_delay0_per150
df['IL2L'] = pulse4_8nA_50ms_delay100_per100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA_to_0
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/train/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/train/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/train/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/train/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/train/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/train/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence 13
file = "Sequence13.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_to_0
df['IL2DR'] = pulse0_to_4_8nA_delay0_per150
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA_delay0
df['IL2VR'] = pulse0_to_4_8nA_delay0
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/train/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/train/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/train/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/train/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/train/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/train/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence 14
file = "Sequence14.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_to_0
df['IL2DR'] = pulse0_to_4_8nA_delay0_per150
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA_delay0_per150
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/train/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/train/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/train/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/train/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/train/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/train/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence 15
file = "Sequence15.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8_nA_delay0
df['IL2DR'] = pulse4_8nA_50ms_delay100_per100
df['IL2L'] = pulse0_to_4_8nA_delay0_per150
df['IL2R'] = pulse4_8nA_50ms_delay100
df['IL2VL'] = pulse4_8_nA_delay0
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/train/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/train/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/train/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/train/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/train/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/train/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence 16
file = "Sequence16.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA_50ms_delay100_per100
df['IL2DR'] = pulse0_to_4_8nA_delay0
df['IL2L'] = pulse0_to_4_8nA_delay0
df['IL2R'] = pulse4_8nA_50ms_delay100
df['IL2VL'] = pulse0_to_4_8nA_delay0_per150
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/train/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/train/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/train/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/train/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/train/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/train/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence 17
file = "Sequence17.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA_50ms_delay100_per100
df['IL2DR'] = pulse4_8nA_50ms_delay100
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse0_to_4_8nA_delay0
df['IL2VL'] = pulse0_to_4_8nA_per150
df['IL2VR'] = pulse0_to_4_8nA_per150
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/train/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/train/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/train/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/train/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/train/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/train/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence 18
file = "Sequence18.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_plus50
df['IL2DR'] = pulse0_to_4_8nA_per150
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse4_8nA_30ms_delay100
df['IL2VL'] = pulse4_8nA_delay0
df['IL2VR'] = pulse0_to_4_8nA_per150
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/train/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/train/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/train/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/train/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/train/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/train/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence 19
file = "Sequence19.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA_200ms_delay100
df['IL2DR'] = pulse0_to_4_8nA_to_0_per100
df['IL2L'] = pulse0_to_4_8nA
df['IL2R'] = pulse4_8nA_200ms_delay100
df['IL2VL'] = pulse0_to_4_8nA_to_0_per100
df['IL2VR'] = pulse0_to_4_8nA
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/train/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/train/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/train/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/train/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/train/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/train/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence 20
file = "Sequence20.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA_200ms_delay100
df['IL2DR'] = pulse_0_to_4_8nA_to_0_per100
df['IL2L'] = pulse4_8nA_200ms_delay100
df['IL2R'] = pulse4_8nA_200ms_delay100
df['IL2VL'] = pulse_0_to_4_8nA_to_0_per100
df['IL2VR'] = pulse4_8nA_200ms_delay100
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/train/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/train/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/train/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/train/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/train/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/train/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence 21
file = "Sequence21.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA
df['IL2DR'] = pulse0_to_4_8nA
df['IL2L'] = pulse0_to_4_8nA
df['IL2R'] = pulse0_to_4_8nA
df['IL2VL'] = pulse0_to_4_8nA
df['IL2VR'] = pulse0_to_4_8nA
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/valid/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/valid/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/valid/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/valid/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/valid/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/valid/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/valid/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/valid/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/valid/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/valid/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence 22
file = "Sequence22.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_to_0_per100
df['IL2DR'] = pulse0_to_4_8nA_to_0_per100
df['IL2L'] = pulse0_to_4_8nA_to_0_per100
df['IL2R'] = pulse0_to_4_8nA_to_0_per100
df['IL2VL'] = pulse0_to_4_8nA_to_0_per100
df['IL2VR'] = pulse0_to_4_8nA_to_0_per100
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/valid/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/valid/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/valid/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/valid/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/valid/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/valid/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/valid/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/valid/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/valid/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence 23
file = "Sequence23.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA_delay0
df['IL2DR'] = pulse4_8nA_delay0
df['IL2L'] = pulse0_to_4_8nA_to_0_per100
df['IL2R'] = pulse0_to_4_8nA_delay0_per150
df['IL2VL'] = pulse0_to_4_8nA_to_0_per100
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/valid/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/valid/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/valid/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/valid/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/valid/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/valid/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/valid/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/valid/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/valid/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence 24
file = "Sequence24.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA
df['IL2DR'] = pulse0_to_4_8nA_to_0_per100
df['IL2L'] = pulse4_8nA_50ms_delay100_per100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA
df['IL2VR'] = pulse0_to_4_8nA_to_0_per100
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/valid/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/valid/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/valid/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/valid/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/valid/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/valid/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/valid/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/valid/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/valid/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence 25
file = "Sequence25.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA_50ms_delay100_per100
df['IL2DR'] = pulse4_8nA_delay0
df['IL2L'] = pulse0_to_4_8nA_delay0_per150
df['IL2R'] = pulse4_8nA_50ms_delay100
df['IL2VL'] = pulse0_to_4_8nA_delay0_per150
df['IL2VR'] = pulse4_8nA_delay0
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/valid/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/valid/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/valid/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/valid/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/valid/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/valid/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/valid/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/valid/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/valid/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence 26
file = "Sequence26.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_to_0
df['IL2DR'] = pulse0_to_4_8nA_delay0_per150
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA_to_0_delay0_per100
df['IL2VR'] = pulse0_to_4_8nA_to_0_delay0_per100
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/valid/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/valid/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/valid/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/valid/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/valid/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/valid/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/valid/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/valid/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/valid/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence 27
file = "Sequence27.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_delay0
df['IL2DR'] = pulse0_to_4_8nA_delay0
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA_to_0
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/valid/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/valid/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/valid/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/valid/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/valid/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/valid/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/valid/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/valid/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/valid/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence 28
file = "Sequence28.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA_50ms_delay100_per100
df['IL2DR'] = pulse4_8nA_50ms_delay100
df['IL2L'] = pulse0_to_4_8nA_delay0
df['IL2R'] = pulse4_8nA_50ms_delay100
df['IL2VL'] = pulse0_to_4_8nA_per150
df['IL2VR'] = pulse0_to_4_8nA_per150
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/valid/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/valid/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/valid/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/valid/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/valid/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/valid/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/valid/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/valid/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/valid/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence 29
file = "Sequence29.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_plus50
df['IL2DR'] = pulse0_to_4_8nA_per150
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse4_8nA_30ms_delay100
df['IL2VL'] = pulse0_to_4_8nA_per150
df['IL2VR'] = pulse4_8nA_delay0
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/valid/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/valid/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/valid/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/valid/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/valid/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/valid/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/valid/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/valid/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/valid/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence 30
file = "Sequence30.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA_200ms_delay100
df['IL2DR'] = pulse0_to_4_8nA
df['IL2L'] = pulse0_to_4_8nA
df['IL2R'] = pulse4_8nA_200ms_delay100
df['IL2VL'] = pulse0_to_4_8nA
df['IL2VR'] = pulse0_to_4_8nA
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/valid/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/valid/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/valid/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/valid/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/valid/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/valid/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/valid/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/valid/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/valid/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/valid/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence 31
file = "Sequence31.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_delay50
df['IL2DR'] = pulse0_to_4_8nA_delay50
df['IL2L'] = pulse0_to_4_8nA_delay50
df['IL2R'] = pulse0_to_4_8nA_delay50
df['IL2VL'] = pulse0_to_4_8nA_delay50
df['IL2VR'] = pulse0_to_4_8nA_delay50
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/test/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/test/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/test/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/test/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/test/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/test/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/test/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/test/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/test/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence 32
file = "Sequence32.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_to_0_delay50
df['IL2DR'] = pulse0_to_4_8nA_to_0_delay50
df['IL2L'] = pulse0_to_4_8nA_to_0_delay50
df['IL2R'] = pulse0_to_4_8nA_to_0_delay50
df['IL2VL'] = pulse0_to_4_8nA_to_0_delay50
df['IL2VR'] = pulse0_to_4_8nA_to_0_delay50
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/test/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/test/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/test/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/test/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/test/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/test/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/test/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/test/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/test/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence 33
file = "Sequence33.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA_delay0
df['IL2DR'] = pulse0_to_4_8nA_delay0_per150
df['IL2L'] = pulse0_to_4_8nA_to_0_per100
df['IL2R'] = pulse0_to_4_8nA_delay0_per150
df['IL2VL'] = pulse0_to_4_8nA_to_0_per100
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/test/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/test/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/test/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/test/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/test/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/test/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/test/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/test/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/test/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence 34
file = "Sequence34.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_delay0_per150
df['IL2DR'] = pulse0_to_4_8nA_to_0
df['IL2L'] = pulse4_8nA_50ms_delay100_per100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA_delay0_per150
df['IL2VR'] = pulse0_to_4_8nA_to_0
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/test/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/test/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/test/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/test/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/test/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/test/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/test/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/test/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/test/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence 35
file = "Sequence35.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_delay0
df['IL2DR'] = pulse4_8nA_50ms_delay100_per100
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse0_to_4_8nA_delay0
df['IL2VL'] = pulse0_to_4_8nA_delay0_per150
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/test/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/test/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/test/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/test/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/test/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/test/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/test/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/test/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/test/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence 36
file = "Sequence36.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_to_0
df['IL2DR'] = pulse0_to_4_8nA_delay0_per150
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA_to_0_delay0
df['IL2VR'] = pulse0_to_4_8nA_to_0_delay0
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/test/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/test/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/test/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/test/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/test/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/test/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/test/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/test/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/test/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence 37
file = "Sequence37.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_delay0_per150
df['IL2DR'] = pulse0_to_4_8nA_delay0_per150
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA_to_0
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/test/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/test/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/test/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/test/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/test/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/test/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/test/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/test/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/test/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence 38
file = "Sequence38.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_delay0
df['IL2DR'] = pulse4_8nA_50ms_delay100
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA_per150
df['IL2VR'] = pulse0_to_4_8nA_per150
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/test/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/test/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/test/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/test/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/test/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/test/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/test/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/test/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/test/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence 39
file = "Sequence39.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_to_0_per100
df['IL2DR'] = pulse0_to_4_8nA_to_0_per100
df['IL2L'] = pulse0_to_4_8nA
df['IL2R'] = pulse0_to_4_8nA_to_0_per100
df['IL2VL'] = pulse0_to_4_8nA_to_0_per100
df['IL2VR'] = pulse0_to_4_8nA
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/test/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/test/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/test/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/test/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/test/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/test/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/test/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/test/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/test/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence 40
file = "Sequence40.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA_50ms_delay0
df['IL2DR'] = pulse0_to_4_8nA_plus50
df['IL2L'] = pulse4_8nA
df['IL2R'] = pulse4_8nA_10ms_delay100_per20
df['IL2VL'] = pulse4_8nA_10ms_delay100_per20
df['IL2VR'] = pulse4_8nA
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/test/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/test/" + file, sep = " ", header=False)
# Save Experiment 1
df[save6].to_csv("../Datasets/Nictation-20-0_05-6/test/" + file, sep = " ", header=False)
df01 = df.iloc[df.index % 2 == 0]
df01[save6].to_csv("../Datasets/Nictation-20-0_1-6/test/" + file, sep = " ", header=False)
df05 = df.iloc[df.index % 10 == 0]
df05[save6].to_csv("../Datasets/Nictation-20-0_5-6/test/" + file, sep = " ", header=False)
df1 = df.iloc[df.index % 20 == 0]
df1[save6].to_csv("../Datasets/Nictation-20-1-6/test/" + file, sep = " ", header=False)
df5 = df.iloc[df.index % 100 == 0]
df5[save6].to_csv("../Datasets/Nictation-20-5-6/test/" + file, sep = " ", header=False)
df10 = df.iloc[df.index % 200 == 0]
df10[save6].to_csv("../Datasets/Nictation-20-10-6/test/" + file, sep = " ", header=False)
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-5-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-10-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/test/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/test/" + file, sep = " ", header=False)
# Save Experiment 5
df05.to_csv("../Datasets/Nictation-20-0_5-12/test/" + file, sep = " ", header=False)

# ########################################################################################################################################################################
# # Sequence 41
# file = "Sequence41.dat"
# cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
# save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
# df = pd.read_csv(file, sep = "\s+", names=cols)
# df['IL2DL'] = pulse0_to_4_8nA_50ms_delay0
# df['IL2DR'] = pulse0_to_4_8nA_plus50
# df['IL2L'] = pulse4_8nA
# df['IL2R'] = pulse4_8nA_10ms_delay100_per20
# df['IL2VL'] = pulse4_8nA_10ms_delay100_per20
# df['IL2VR'] = pulse4_8nA
# # Save Base
# df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
# df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# # Reduce Timestep
# df05 = df.iloc[df.index % 10 == 0]
# # Save Experiment 1
# df[save6].to_csv("../Datasets/Nictation-25-0_5-6/train/" + file, sep = " ", header=False)
# df[save6].to_csv("../Datasets/Nictation-45-0_5-6/train/" + file, sep = " ", header=False)
# # Save Experiment 2
# # Save Experiment 5

# ########################################################################################################################################################################
# # Sequence 42
# file = "Sequence42.dat"
# cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
# save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
# df = pd.read_csv(file, sep = "\s+", names=cols)
# df['IL2DL'] = pulse4_8nA
# df['IL2DR'] = pulse4_8nA_10ms_delay100_per20
# df['IL2L'] = pulse4_8nA_50ms_delay0
# df['IL2R'] = pulse0_to_4_8nA_plus50
# df['IL2VL'] = pulse4_8nA_10ms_delay100_per20
# df['IL2VR'] = pulse4_8nA
# # Save Base
# df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
# df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# # Reduce Timestep
# df05 = df.iloc[df.index % 10 == 0]
# # Save Experiment 1
# df[save6].to_csv("../Datasets/Nictation-25-0_5-6/train/" + file, sep = " ", header=False)
# df[save6].to_csv("../Datasets/Nictation-45-0_5-6/train/" + file, sep = " ", header=False)
# # Save Experiment 2
# # Save Experiment 5

# ########################################################################################################################################################################
# # Sequence 43
# file = "Sequence43.dat"
# cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
# save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
# df = pd.read_csv(file, sep = "\s+", names=cols)
# df['IL2DL'] = pulse4_8nA
# df['IL2DR'] = pulse4_8nA_10ms_delay100_per20
# df['IL2L'] = pulse0_to_4_8nA_50ms_delay0
# df['IL2R'] = pulse0_to_4_8nA_plus50
# df['IL2VL'] = pulse4_8nA_10ms_delay100_per20
# df['IL2VR'] = pulse4_8nA
# # Save Base
# df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
# df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# # Reduce Timestep
# df05 = df.iloc[df.index % 10 == 0]
# # Save Experiment 1
# df[save6].to_csv("../Datasets/Nictation-25-0_5-6/train/" + file, sep = " ", header=False)
# df[save6].to_csv("../Datasets/Nictation-45-0_5-6/train/" + file, sep = " ", header=False)
# # Save Experiment 2
# # Save Experiment 5

# ########################################################################################################################################################################
# # Sequence 44
# file = "Sequence44.dat"
# cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
# save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
# df = pd.read_csv(file, sep = "\s+", names=cols)
# df['IL2DL'] = pulse4_8nA_10ms_delay100_per20
# df['IL2DR'] = pulse4_8nA
# df['IL2L'] = pulse4_8nA
# df['IL2R'] = pulse4_8nA_10ms_delay100_per20
# df['IL2VL'] = pulse4_8nA_50ms_delay0
# df['IL2VR'] = pulse4_8nA_50ms_delay0
# # Save Base
# df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
# df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# # Reduce Timestep
# df05 = df.iloc[df.index % 10 == 0]
# # Save Experiment 1
# df[save6].to_csv("../Datasets/Nictation-25-0_5-6/train/" + file, sep = " ", header=False)
# df[save6].to_csv("../Datasets/Nictation-45-0_5-6/train/" + file, sep = " ", header=False)
# # Save Experiment 2
# # Save Experiment 5

# ########################################################################################################################################################################
# # Sequence 45
# file = "Sequence45.dat"
# cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
# save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
# df = pd.read_csv(file, sep = "\s+", names=cols)
# df['IL2DL'] = pulse4_8nA_10ms_delay100_per20
# df['IL2DR'] = pulse4_8nA
# df['IL2L'] = pulse4_8nA
# df['IL2R'] = pulse4_8nA_10ms_delay100_per20
# df['IL2VL'] = pulse0_to_4_8nA_50ms_delay0
# df['IL2VR'] = pulse0_to_4_8nA_plus50
# # Save Base
# df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
# df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# # Reduce Timestep
# df05 = df.iloc[df.index % 10 == 0]
# # Save Experiment 1
# df[save6].to_csv("../Datasets/Nictation-25-0_5-6/train/" + file, sep = " ", header=False)
# df[save6].to_csv("../Datasets/Nictation-45-0_5-6/train/" + file, sep = " ", header=False)
# # Save Experiment 2
# # Save Experiment 5

########################################################################################################################################################################
# Sequence 46
file = "Sequence46.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_to_0
df['IL2DR'] = pulse4_8nA
df['IL2L'] = pulse0_to_4_8nA_to_0
df['IL2R'] = pulse4_8nA
df['IL2VL'] = pulse0_to_4_8nA_to_0
df['IL2VR'] = pulse4_8nA
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5

########################################################################################################################################################################
# Sequence 47
file = "Sequence47.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_to_0_per100
df['IL2DR'] = pulse4_8nA_50ms_delay100_per100
df['IL2L'] = pulse0_to_4_8nA_to_0_per100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA_to_0_per100
df['IL2VR'] = pulse4_8nA_50ms_delay100_per100
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5

########################################################################################################################################################################
# Sequence 48
file = "Sequence48.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA_50ms_delay100_per100
df['IL2DR'] = pulse0_to_4_8nA_delay0
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse4_8nA_50ms_delay100
df['IL2VL'] = pulse0_to_4_8nA_per150
df['IL2VR'] = pulse0_to_4_8nA_per150
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5

########################################################################################################################################################################
# Sequence 49
file = "Sequence49.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA_50ms_delay100_per100
df['IL2DR'] = pulse4_8nA_50ms_delay100
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse0_to_4_8nA_per150
df['IL2VL'] = pulse0_to_4_8nA_delay0
df['IL2VR'] = pulse0_to_4_8nA_per150
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5

########################################################################################################################################################################
# Sequence 50
file = "Sequence50.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_to_0
df['IL2DR'] = pulse0_to_4_8nA_delay0_per150
df['IL2L'] = pulse0_to_4_8nA_delay0
df['IL2R'] = pulse0_to_4_8nA_delay0
df['IL2VL'] = pulse4_8nA_50ms_delay100
df['IL2VR'] = pulse4_8nA_50ms_delay100_per100
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5

########################################################################################################################################################################
# Sequence 51
file = "Sequence51.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA_delay0
df['IL2DR'] = pulse4_8nA_50ms_delay100_per100
df['IL2L'] = pulse4_8nA_delay0
df['IL2R'] = pulse4_8nA_50ms_delay100
df['IL2VL'] = pulse0_to_4_8nA_delay0_per150
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5

########################################################################################################################################################################
# Sequence 52
file = "Sequence52.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA_50ms_delay100_per100
df['IL2DR'] = pulse4_8nA_delay0
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse4_8nA_delay0
df['IL2VL'] = pulse0_to_4_8nA_delay0_per150
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5

########################################################################################################################################################################
# Sequence 53
file = "Sequence53.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA_50ms_delay100_per100
df['IL2DR'] = pulse0_to_4_8nA_delay0
df['IL2L'] = pulse0_to_4_8nA_delay0_per150
df['IL2R'] = pulse4_8nA_50ms_delay100
df['IL2VL'] = pulse0_to_4_8nA_delay0
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5

########################################################################################################################################################################
# Sequence 54
file = "Sequence54.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_delay0
df['IL2DR'] = pulse4_8nA_50ms_delay100_per100
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse0_to_4_8nA_delay0_per150
df['IL2VL'] = pulse0_to_4_8nA_delay0_per150
df['IL2VR'] = pulse0_to_4_8nA_delay0
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5

########################################################################################################################################################################
# Sequence 55
file = "Sequence55.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA
df['IL2DR'] = pulse0_to_4_8nA_to_0_per100
df['IL2L'] = pulse4_8nA_200ms_delay100
df['IL2R'] = pulse0_to_4_8nA
df['IL2VL'] = pulse0_to_4_8nA_to_0_per100
df['IL2VR'] = pulse4_8nA_200ms_delay100
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5

########################################################################################################################################################################
# Sequence 56
file = "Sequence56.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_to_0_per100
df['IL2DR'] = pulse4_8nA_200ms_delay100
df['IL2L'] = pulse0_to_4_8nA
df['IL2R'] = pulse0_to_4_8nA_to_0_per100
df['IL2VL'] = pulse4_8nA_200ms_delay100
df['IL2VR'] = pulse0_to_4_8nA
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5

########################################################################################################################################################################
# Sequence 57
file = "Sequence57.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse4_8nA
df['IL2DR'] = pulse4_8nA
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5

########################################################################################################################################################################
# Sequence 58
file = "Sequence58.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = pulse4_8nA
df['IL2R'] = pulse4_8nA
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5

########################################################################################################################################################################
# Sequence 59
file = "Sequence59.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = pulse4_8nA
df['IL2VR'] = pulse4_8nA
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5

########################################################################################################################################################################
# Sequence 60
file = "Sequence60.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_delay0_per150
df['IL2DR'] = pulse0_to_4_8nA_delay0_per150
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5

########################################################################################################################################################################
# Sequence 61
file = "Sequence61.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = pulse0_to_4_8nA_delay0_per150
df['IL2R'] = pulse0_to_4_8nA_delay0_per150
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5

########################################################################################################################################################################
# Sequence 62
file = "Sequence62.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = pulse0_to_4_8nA_delay0_per150
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5

########################################################################################################################################################################
# Sequence 63
file = "Sequence63.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = pulse0_to_4_8nA_to_0_per100
df['IL2DR'] = pulse0_to_4_8nA_to_0_per100
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5

########################################################################################################################################################################
# Sequence 64
file = "Sequence64.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = pulse0_to_4_8nA_to_0_per100
df['IL2R'] = pulse0_to_4_8nA_to_0_per100
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-30-0_5-6/train/" + file, sep = " ", header=False)
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5

########################################################################################################################################################################
# Sequence 65
file = "Sequence65.dat"
cols = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
save6 = ['time', 'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'IL2DL', 'IL2DR', 'IL2L', 'IL2R', 'IL2VL', 'IL2VR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = pulse0_to_4_8nA_to_0_per100
df['IL2VR'] = pulse0_to_4_8nA_to_0_per100
# Save Base
df.to_csv("../Datasets/Nictation-45-0_05-12/train/" + file, sep = " ", header=False)
df[save6].to_csv("../Datasets/Nictation-45-0_05-6/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 2
df05[save6].to_csv("../Datasets/Nictation-40-0_5-6/train/" + file, sep = " ", header=False)
# Save Experiment 5