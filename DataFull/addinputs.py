import pandas as pd

simulationtime = 500
ts = 0.05

###########################################################################
############################ Create Inputs ################################
###########################################################################
# pulse1_4nA.mod
pulse1_4nA = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 100
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse1_4nA[int(t/ts)] = amplitude 
    t += ts

# pulse2_3nA.mod
pulse2_3nA = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 100
amplitude = 2.3
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse2_3nA[int(t/ts)] = amplitude 
    t += ts

# pulse1_4nA_200ms_delay100
pulse1_4nA_200ms_delay100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 200
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse1_4nA_200ms_delay100[int(t/ts)] = amplitude 
    t += ts

# pulse2_3nA_200ms_delay100
pulse2_3nA_200ms_delay100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 200
amplitude = 2.3
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse2_3nA_200ms_delay100[int(t/ts)] = amplitude 
    t += ts

# pulse1_4nA_50ms_delay100
pulse1_4nA_50ms_delay100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 50
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse1_4nA_50ms_delay100[int(t/ts)] = amplitude 
    t += ts

# pulse2_3nA_50ms_delay100
pulse2_3nA_50ms_delay100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 50
amplitude = 2.3
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse2_3nA_50ms_delay100[int(t/ts)] = amplitude 
    t += ts

# pulse1_4nA_50ms_delay100_per100
pulse1_4nA_50ms_delay100_per100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 50
amplitude = 1.4
durnoamp = 50
while (t <= simulationtime):
    if ((t >= delay) and (t < delay + duration)):
        pulse1_4nA_50ms_delay100_per100[int(t/ts)] = amplitude
    elif ((t >= delay + duration + durnoamp) and (t < delay + 2*duration + durnoamp)):
        pulse1_4nA_50ms_delay100_per100[int(t/ts)] = amplitude
    elif ((t >= delay + 2*duration + 2*durnoamp) and (t < delay + 3*duration + 2*durnoamp)):
        pulse1_4nA_50ms_delay100_per100[int(t/ts)] = amplitude
    t += ts

# pulse2_3nA_50ms_delay100_per100
pulse2_3nA_50ms_delay100_per100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 50
amplitude = 2.3
durnoamp = 50
while (t <= simulationtime):
    if ((t >= delay) and (t < delay + duration)):
        pulse2_3nA_50ms_delay100_per100[int(t/ts)] = amplitude
    elif ((t >= delay + duration + durnoamp) and (t < delay + 2*duration + durnoamp)):
        pulse2_3nA_50ms_delay100_per100[int(t/ts)] = amplitude
    elif ((t >= delay + 2*duration + 2*durnoamp) and (t < delay + 3*duration + 2*durnoamp)):
        pulse2_3nA_50ms_delay100_per100[int(t/ts)] = amplitude
    t += ts

# pulse0_to_1_4nA
pulse0_to_1_4nA = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 100
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_1_4nA[int(t/ts)] = amplitude * (t-delay)/duration
    t += ts

# pulse0_to_2_3nA
pulse0_to_2_3nA = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 100
amplitude = 2.3
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_2_3nA[int(t/ts)] = amplitude * (t-delay)/duration
    t += ts

# pulse0_to_1_4nA_plus50
pulse0_to_1_4nA_plus50 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 50
durampmax = 50
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_1_4nA_plus50[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < delay + duration + durampmax)):
        pulse0_to_1_4nA_plus50[int(t/ts)] = amplitude
    t += ts

# pulse0_to_2_3nA_plus50
pulse0_to_2_3nA_plus50 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 50
durampmax = 50
amplitude = 2.3
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_2_3nA_plus50[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < delay + duration + durampmax)):
        pulse0_to_2_3nA_plus50[int(t/ts)] = amplitude
    t += ts

# pulse1_4nA_10ms_delay100
pulse1_4nA_10ms_delay100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 10
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse1_4nA_10ms_delay100[int(t/ts)] = amplitude
    t += ts

# pulse2_3nA_10ms_delay100
pulse2_3nA_10ms_delay100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 10
amplitude = 2.3
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse2_3nA_10ms_delay100[int(t/ts)] = amplitude
    t += ts

# pulse1_4nA_20ms_delay100
pulse1_4nA_20ms_delay100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 20
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse1_4nA_20ms_delay100[int(t/ts)] = amplitude
    t += ts

# pulse2_3nA_20ms_delay100
pulse2_3nA_20ms_delay100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 20
amplitude = 2.3
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse2_3nA_20ms_delay100[int(t/ts)] = amplitude
    t += ts

# pulse1_4nA_30ms_delay100
pulse1_4nA_30ms_delay100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 30
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse1_4nA_30ms_delay100[int(t/ts)] = amplitude
    t += ts

# pulse2_3nA_30ms_delay100
pulse2_3nA_30ms_delay100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 30
amplitude = 2.3
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse2_3nA_30ms_delay100[int(t/ts)] = amplitude
    t += ts

# pulse1_4nA_40ms_delay100
pulse1_4nA_40ms_delay100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 40
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse1_4nA_40ms_delay100[int(t/ts)] = amplitude
    t += ts

# pulse2_3nA_40ms_delay100
pulse2_3nA_40ms_delay100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 40
amplitude = 2.3
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse2_3nA_40ms_delay100[int(t/ts)] = amplitude
    t += ts

# pulse1_4nA_10ms_delay100_per20
pulse1_4nA_10ms_delay100_per20 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 10
amplitude = 1.4
durnoamp = 10
while (t <= simulationtime):
    if ((t >= delay) and (t < delay + duration)):
        pulse1_4nA_10ms_delay100_per20[int(t/ts)] = amplitude
    elif ((t >= delay + duration + durnoamp) and (t < delay + 2*duration + durnoamp)):
        pulse1_4nA_10ms_delay100_per20[int(t/ts)] = amplitude
    elif ((t >= delay + 2*duration + 2*durnoamp) and (t < delay + 3*duration + 2*durnoamp)):
        pulse1_4nA_10ms_delay100_per20[int(t/ts)] = amplitude
    t += ts

# pulse2_3nA_10ms_delay100_per20
pulse2_3nA_10ms_delay100_per20 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 10
amplitude = 2.3
durnoamp = 10
while (t <= simulationtime):
    if ((t >= delay) and (t < delay + duration)):
        pulse2_3nA_10ms_delay100_per20[int(t/ts)] = amplitude
    elif ((t >= delay + duration + durnoamp) and (t < delay + 2*duration + durnoamp)):
        pulse2_3nA_10ms_delay100_per20[int(t/ts)] = amplitude
    elif ((t >= delay + 2*duration + 2*durnoamp) and (t < delay + 3*duration + 2*durnoamp)):
        pulse2_3nA_10ms_delay100_per20[int(t/ts)] = amplitude
    t += ts

# pulse0_to_1_4nA_to_0
pulse0_to_1_4nA_to_0 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 50
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_1_4nA_to_0[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < 2*duration + delay)):
        pulse0_to_1_4nA_to_0[int(t/ts)] = amplitude * (2 - (t-delay)/duration)
    t += ts

# pulse0_to_2_3nA_to_0
pulse0_to_2_3nA_to_0 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 50
amplitude = 2.3
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_2_3nA_to_0[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < 2*duration + delay)):
        pulse0_to_2_3nA_to_0[int(t/ts)] = amplitude * (2 - (t-delay)/duration)
    t += ts

# pulse0_to_1_4nA_to_0_per100
pulse0_to_1_4nA_to_0_per100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 50
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_1_4nA_to_0_per100[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < 2*duration + delay)):
        pulse0_to_1_4nA_to_0_per100[int(t/ts)] = amplitude * (2 - (t-delay)/duration)
    elif ((t >= 2*duration + delay) and (t < 3*duration + delay)):
        pulse0_to_1_4nA_to_0_per100[int(t/ts)] = amplitude * (t-delay-2*duration)/duration
    elif ((t >= 3*duration + delay) and (t < 4*duration + delay)):
        pulse0_to_1_4nA_to_0_per100[int(t/ts)] = amplitude * (2 - (t-delay-2*duration)/duration)
    elif ((t >= 4*duration + delay) and (t < 5*duration + delay)):
        pulse0_to_1_4nA_to_0_per100[int(t/ts)] = amplitude * (t-delay-4*duration)/duration
    elif ((t >= 5*duration + delay) and (t < 6*duration + delay)):
        pulse0_to_1_4nA_to_0_per100[int(t/ts)] = amplitude * (2 - (t-delay-4*duration)/duration)
    t += ts

# pulse0_to_2_3nA_to_0_per100
pulse0_to_2_3nA_to_0_per100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 50
amplitude = 2.3
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_2_3nA_to_0_per100[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < 2*duration + delay)):
        pulse0_to_2_3nA_to_0_per100[int(t/ts)] = amplitude * (2 - (t-delay)/duration)
    elif ((t >= 2*duration + delay) and (t < 3*duration + delay)):
        pulse0_to_2_3nA_to_0_per100[int(t/ts)] = amplitude * (t-delay-2*duration)/duration
    elif ((t >= 3*duration + delay) and (t < 4*duration + delay)):
        pulse0_to_2_3nA_to_0_per100[int(t/ts)] = amplitude * (2 - (t-delay-2*duration)/duration)
    elif ((t >= 4*duration + delay) and (t < 5*duration + delay)):
        pulse0_to_2_3nA_to_0_per100[int(t/ts)] = amplitude * (t-delay-4*duration)/duration
    elif ((t >= 5*duration + delay) and (t < 6*duration + delay)):
        pulse0_to_2_3nA_to_0_per100[int(t/ts)] = amplitude * (2 - (t-delay-4*duration)/duration)

    t += ts

# pulse1_4nA_delay0
pulse1_4nA_delay0 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 100
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse1_4nA_delay0[int(t/ts)] = amplitude 
    t += ts

# pulse2_3nA_delay0
pulse2_3nA_delay0 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 100
amplitude = 2.3
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse2_3nA_delay0[int(t/ts)] = amplitude 
    t += ts

# pulse0_to_1_4nA_per150
pulse0_to_1_4nA_per150 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 100
stay0 = 50
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_1_4nA_per150[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay + stay0) and (t < 2*duration + delay + stay0)):
        pulse0_to_1_4nA_per150[int(t/ts)] = amplitude * (t-delay-duration-stay0)/duration
    elif ((t >= 2*duration + delay + 2*stay0) and (t < 3*duration + delay + 2*stay0)):
        pulse0_to_1_4nA_per150[int(t/ts)] = amplitude * (t-delay-2*duration-2*stay0)/duration
    t += ts

# pulse0_to_2_3nA_per150
pulse0_to_2_3nA_per150 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 100
stay0 = 50
amplitude = 2.3
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_2_3nA_per150[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay + stay0) and (t < 2*duration + delay + stay0)):
        pulse0_to_2_3nA_per150[int(t/ts)] = amplitude * (t-delay-duration-stay0)/duration
    elif ((t >= 2*duration + delay + 2*stay0) and (t < 3*duration + delay + 2*stay0)):
        pulse0_to_2_3nA_per150[int(t/ts)] = amplitude * (t-delay-2*duration-2*stay0)/duration
    t += ts

# pulse0_to_1_4nA_delay0_per150
pulse0_to_1_4nA_delay0_per150 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 100
stay0 = 50
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_1_4nA_delay0_per150[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay + stay0) and (t < 2*duration + delay + stay0)):
        pulse0_to_1_4nA_delay0_per150[int(t/ts)] = amplitude * (t-delay-duration-stay0)/duration
    elif ((t >= 2*duration + delay + 2*stay0) and (t < 3*duration + delay + 2*stay0)):
        pulse0_to_1_4nA_delay0_per150[int(t/ts)] = amplitude * (t-delay-2*duration-2*stay0)/duration
    t += ts

# pulse0_to_1_4nA_plus50_delay0
pulse0_to_1_4nA_plus50_delay0 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 50
durampmax = 50
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_1_4nA_plus50_delay0[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < delay + duration + durampmax)):
        pulse0_to_1_4nA_plus50_delay0[int(t/ts)] = amplitude
    t += ts

# pulse2_3nA_200ms_delay0
pulse2_3nA_200ms_delay0 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 200
amplitude = 2.3
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse2_3nA_200ms_delay0[int(t/ts)] = amplitude 
    t += ts

# pulse0_to_1_4nA_delay0
pulse0_to_1_4nA_delay0 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 100
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_1_4nA_delay0[int(t/ts)] = amplitude * (t-delay)/duration
    t += ts

# pulse2_3nA_10ms_delay0_per20
pulse2_3nA_10ms_delay0_per20 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 10
amplitude = 2.3
durnoamp = 10
while (t <= simulationtime):
    if ((t >= delay) and (t < delay + duration)):
        pulse2_3nA_10ms_delay0_per20[int(t/ts)] = amplitude
    elif ((t >= delay + duration + durnoamp) and (t < delay + 2*duration + durnoamp)):
        pulse2_3nA_10ms_delay0_per20[int(t/ts)] = amplitude
    elif ((t >= delay + 2*duration + 2*durnoamp) and (t < delay + 3*duration + 2*durnoamp)):
        pulse2_3nA_10ms_delay0_per20[int(t/ts)] = amplitude
    t += ts

# pulse0_to_1_4nA_to_0_delay0_per100
pulse0_to_1_4nA_to_0_delay0_per100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 50
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_1_4nA_to_0_delay0_per100[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < 2*duration + delay)):
        pulse0_to_1_4nA_to_0_delay0_per100[int(t/ts)] = amplitude * (2 - (t-delay)/duration)
    elif ((t >= 2*duration + delay) and (t < 3*duration + delay)):
        pulse0_to_1_4nA_to_0_delay0_per100[int(t/ts)] = amplitude * (t-delay-2*duration)/duration
    elif ((t >= 3*duration + delay) and (t < 4*duration + delay)):
        pulse0_to_1_4nA_to_0_delay0_per100[int(t/ts)] = amplitude * (2 - (t-delay-2*duration)/duration)
    elif ((t >= 4*duration + delay) and (t < 5*duration + delay)):
        pulse0_to_1_4nA_to_0_delay0_per100[int(t/ts)] = amplitude * (t-delay-4*duration)/duration
    elif ((t >= 5*duration + delay) and (t < 6*duration + delay)):
        pulse0_to_1_4nA_to_0_delay0_per100[int(t/ts)] = amplitude * (2 - (t-delay-4*duration)/duration)
    t += ts

# pulse0_to_2_3nA_to_0_delay0_per100
pulse0_to_2_3nA_to_0_delay0_per100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 50
amplitude = 2.3
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_2_3nA_to_0_delay0_per100[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < 2*duration + delay)):
        pulse0_to_2_3nA_to_0_delay0_per100[int(t/ts)] = amplitude * (2 - (t-delay)/duration)
    elif ((t >= 2*duration + delay) and (t < 3*duration + delay)):
        pulse0_to_2_3nA_to_0_delay0_per100[int(t/ts)] = amplitude * (t-delay-2*duration)/duration
    elif ((t >= 3*duration + delay) and (t < 4*duration + delay)):
        pulse0_to_2_3nA_to_0_delay0_per100[int(t/ts)] = amplitude * (2 - (t-delay-2*duration)/duration)
    elif ((t >= 4*duration + delay) and (t < 5*duration + delay)):
        pulse0_to_2_3nA_to_0_delay0_per100[int(t/ts)] = amplitude * (t-delay-4*duration)/duration
    elif ((t >= 5*duration + delay) and (t < 6*duration + delay)):
        pulse0_to_2_3nA_to_0_delay0_per100[int(t/ts)] = amplitude * (2 - (t-delay-4*duration)/duration)
    t += ts

# pulse0_to_2_3nA_plus50_delay0
pulse0_to_2_3nA_plus50_delay0 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 50
durampmax = 50
amplitude = 2.3
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_2_3nA_plus50_delay0[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < delay + duration + durampmax)):
        pulse0_to_2_3nA_plus50_delay0[int(t/ts)] = amplitude
    t += ts

# pulse0_to_2_3nA_delay0_per150
pulse0_to_2_3nA_delay0_per150 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 100
stay0 = 50
amplitude = 2.3
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_2_3nA_delay0_per150[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay + stay0) and (t < 2*duration + delay + stay0)):
        pulse0_to_2_3nA_delay0_per150[int(t/ts)] = amplitude * (t-delay-duration-stay0)/duration
    elif ((t >= 2*duration + delay + 2*stay0) and (t < 3*duration + delay + 2*stay0)):
        pulse0_to_2_3nA_delay0_per150[int(t/ts)] = amplitude * (t-delay-2*duration-2*stay0)/duration
    t += ts

# pulse1_4nA_50ms_delay0_per100
pulse1_4nA_50ms_delay0_per100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 50
amplitude = 1.4
durnoamp = 50
while (t <= simulationtime):
    if ((t >= delay) and (t < delay + duration)):
        pulse1_4nA_50ms_delay0_per100[int(t/ts)] = amplitude
    elif ((t >= delay + duration + durnoamp) and (t < delay + 2*duration + durnoamp)):
        pulse1_4nA_50ms_delay0_per100[int(t/ts)] = amplitude
    elif ((t >= delay + 2*duration + 2*durnoamp) and (t < delay + 3*duration + 2*durnoamp)):
        pulse1_4nA_50ms_delay0_per100[int(t/ts)] = amplitude
    t += ts

# pulse1_4nA_200ms_delay0
pulse1_4nA_200ms_delay0 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 200
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse1_4nA_200ms_delay0[int(t/ts)] = amplitude 
    t += ts

# pulse0_to_2_3nA_delay0
pulse0_to_2_3nA_delay0 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 100
amplitude = 2.3
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_2_3nA_delay0[int(t/ts)] = amplitude * (t-delay)/duration
    t += ts

# pulse2_3nA_50ms_delay0_per100
pulse2_3nA_50ms_delay0_per100 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 50
amplitude = 2.3
durnoamp = 50
while (t <= simulationtime):
    if ((t >= delay) and (t < delay + duration)):
        pulse2_3nA_50ms_delay0_per100[int(t/ts)] = amplitude
    elif ((t >= delay + duration + durnoamp) and (t < delay + 2*duration + durnoamp)):
        pulse2_3nA_50ms_delay0_per100[int(t/ts)] = amplitude
    elif ((t >= delay + 2*duration + 2*durnoamp) and (t < delay + 3*duration + 2*durnoamp)):
        pulse2_3nA_50ms_delay0_per100[int(t/ts)] = amplitude
    t += ts

# pulse1_4nA_50ms_delay0
pulse1_4nA_50ms_delay0 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 50
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse1_4nA_50ms_delay0[int(t/ts)] = amplitude 
    t += ts

# pulse_ramp_42
pulse_ramp_42 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 50
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse_ramp_42[int(t/ts)] = amplitude * (t-delay)/duration
    t += ts

# pulse_triangle_43
pulse_triangle_43 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 25
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse_triangle_43[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < 2*duration + delay)):
        pulse_triangle_43[int(t/ts)] = amplitude * (2 - (t-delay)/duration)
    t += ts

# pulse_ramp_47_1
pulse_ramp_47_1 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 50
durampmax = 50
stay0 = 50
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse_ramp_47_1[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < duration + delay + durampmax)):
        pulse_ramp_47_1[int(t/ts)] = amplitude
    elif ((t >= duration  +  delay  + durampmax + stay0) and (t < 2*duration  +  delay  + durampmax + stay0)):
        pulse_ramp_47_1[int(t/ts)] = amplitude * (t-duration-delay-durampmax-stay0)/duration
    elif ((t >= 2*duration  +  delay  + durampmax + stay0) and (t < 2*duration  +  delay  + 2*durampmax + stay0)):
        pulse_ramp_47_1[int(t/ts)] = amplitude
    elif ((t >= 2*duration  +  delay  + 2*durampmax + 2*stay0) and (t < 3*duration  +  delay  + 2*durampmax + 2*stay0)):
        pulse_ramp_47_1[int(t/ts)] = amplitude * (t-2*duration-delay-2*durampmax-2*stay0)/duration
    elif ((t >= 3*duration  +  delay  + 2*durampmax + 2*stay0) and (t < 3*duration  +  delay  + 3*durampmax + 2*stay0)):
        pulse_ramp_47_1[int(t/ts)] = amplitude
    t += ts

# pulse_ramp_47_2
pulse_ramp_47_2 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 50
durampmax = 50
stay0 = 50
amplitude = 2.3
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse_ramp_47_2[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < duration + delay + durampmax)):
        pulse_ramp_47_2[int(t/ts)] = amplitude
    elif ((t >= duration  +  delay  + durampmax + stay0) and (t < 2*duration  +  delay  + durampmax + stay0)):
        pulse_ramp_47_2[int(t/ts)] = amplitude * (t-duration-delay-durampmax-stay0)/duration
    elif ((t >= 2*duration  +  delay  + durampmax + stay0) and (t < 2*duration  +  delay  + 2*durampmax + stay0)):
        pulse_ramp_47_2[int(t/ts)] = amplitude
    elif ((t >= 2*duration  +  delay  + 2*durampmax + 2*stay0) and (t < 3*duration  +  delay  + 2*durampmax + 2*stay0)):
        pulse_ramp_47_2[int(t/ts)] = amplitude * (t-2*duration-delay-2*durampmax-2*stay0)/duration
    elif ((t >= 3*duration  +  delay  + 2*durampmax + 2*stay0) and (t < 3*duration  +  delay  + 3*durampmax + 2*stay0)):
        pulse_ramp_47_2[int(t/ts)] = amplitude
    t += ts

# pulse_triangle_48
pulse_triangle_48 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 100
duration = 100
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse_triangle_48[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= delay) and (t < duration + delay)):
        pulse_triangle_48[int(t/ts)] = amplitude * (2 - (t-delay)/duration)
    t += ts

# pulse_triangle_49_1
pulse_triangle_49_1 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 50
duration = 100
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse_triangle_49_1[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < 2*duration + delay)):
        pulse_triangle_49_1[int(t/ts)] = amplitude * (2 - (t-delay)/duration)
    elif ((t >= 2*duration + delay) and (t < 3*duration + delay)):
        pulse_triangle_49_1[int(t/ts)] = amplitude * (t-delay-2*duration)/duration
    elif ((t >= 3*duration + delay) and (t < 4*duration + delay)):
        pulse_triangle_49_1[int(t/ts)] = amplitude * (2 - (t-delay-2*duration)/duration)
    elif ((t >= 4*duration + delay) and (t < 5*duration + delay)):
        pulse_triangle_49_1[int(t/ts)] = amplitude * (t-delay-4*duration)/duration
    elif ((t >= 5*duration + delay) and (t < 6*duration + delay)):
        pulse_triangle_49_1[int(t/ts)] = amplitude * (2 - (t-delay-4*duration)/duration)

    t += ts

# pulse_triangle_49_2
pulse_triangle_49_2 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 50
duration = 100
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse_triangle_49_2[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < 2*duration + delay)):
        pulse_triangle_49_2[int(t/ts)] = amplitude * (2 - (t-delay)/duration)
    elif ((t >= 2*duration + delay) and (t < 3*duration + delay)):
        pulse_triangle_49_2[int(t/ts)] = amplitude * (t-delay-2*duration)/duration
    elif ((t >= 3*duration + delay) and (t < 4*duration + delay)):
        pulse_triangle_49_2[int(t/ts)] = amplitude * (2 - (t-delay-2*duration)/duration)
    elif ((t >= 4*duration + delay) and (t < 5*duration + delay)):
        pulse_triangle_49_2[int(t/ts)] = amplitude * (t-delay-4*duration)/duration
    elif ((t >= 5*duration + delay) and (t < 6*duration + delay)):
        pulse_triangle_49_2[int(t/ts)] = amplitude * (2 - (t-delay-4*duration)/duration)

    t += ts

# pulse0_to_1_4nA_50ms_delay0
pulse0_to_1_4nA_50ms_delay0 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 50
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_1_4nA_50ms_delay0[int(t/ts)] = amplitude * (t-delay)/duration
    t += ts

# pulse0_to_1_4nA_to_0_50ms_delay0
pulse0_to_1_4nA_to_0_50ms_delay0 = [0.0000] * int(simulationtime/ts + 1)
t = 0
delay = 0
duration = 25
amplitude = 1.4
while (t <= simulationtime):
    if ((t >= delay) and (t < duration + delay)):
        pulse0_to_1_4nA_to_0_50ms_delay0[int(t/ts)] = amplitude * (t-delay)/duration
    elif ((t >= duration + delay) and (t < 2*duration + delay)):
        pulse0_to_1_4nA_to_0_50ms_delay0[int(t/ts)] = amplitude * (2 - (t-delay)/duration)
    t += ts

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
# Sequence PTRS - 01
file = "Sequence001.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA
df['PLMR'] = pulse1_4nA
df['AVBL'] = pulse2_3nA
df['AVBR'] = pulse2_3nA
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 02
file = "Sequence002.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_200ms_delay100
df['PLMR'] = pulse1_4nA_200ms_delay100
df['AVBL'] = pulse2_3nA_200ms_delay100
df['AVBR'] = pulse2_3nA_200ms_delay100
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 03
file = "Sequence003.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_50ms_delay100
df['PLMR'] = pulse1_4nA_50ms_delay100
df['AVBL'] = pulse2_3nA_50ms_delay100
df['AVBR'] = pulse2_3nA_50ms_delay100
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)



########################################################################################################################################################################
# Sequence PTRS - 04
file = "Sequence004.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_50ms_delay100_per100
df['PLMR'] = pulse1_4nA_50ms_delay100_per100
df['AVBL'] = pulse2_3nA_50ms_delay100_per100
df['AVBR'] = pulse2_3nA_50ms_delay100_per100
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 05
file = "Sequence005.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA
df['PLMR'] = pulse0_to_1_4nA
df['AVBL'] = pulse0_to_2_3nA
df['AVBR'] = pulse0_to_2_3nA
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 06
file = "Sequence006.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_plus50
df['PLMR'] = pulse0_to_1_4nA_plus50
df['AVBL'] = pulse0_to_2_3nA_plus50
df['AVBR'] = pulse0_to_2_3nA_plus50
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS 07
file = "Sequence007.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_10ms_delay100
df['PLMR'] = pulse1_4nA_10ms_delay100
df['AVBL'] = pulse2_3nA_10ms_delay100
df['AVBR'] = pulse2_3nA_10ms_delay100
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 08
file = "Sequence008.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_20ms_delay100
df['PLMR'] = pulse1_4nA_20ms_delay100
df['AVBL'] = pulse2_3nA_20ms_delay100
df['AVBR'] = pulse2_3nA_20ms_delay100
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 09
file = "Sequence009.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_30ms_delay100
df['PLMR'] = pulse1_4nA_30ms_delay100
df['AVBL'] = pulse2_3nA_30ms_delay100
df['AVBR'] = pulse2_3nA_30ms_delay100
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 10
file = "Sequence010.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_40ms_delay100
df['PLMR'] = pulse1_4nA_40ms_delay100
df['AVBL'] = pulse2_3nA_40ms_delay100
df['AVBR'] = pulse2_3nA_40ms_delay100
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 11
file = "Sequence011.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_10ms_delay100_per20
df['PLMR'] = pulse1_4nA_10ms_delay100_per20
df['AVBL'] = pulse2_3nA_10ms_delay100_per20
df['AVBR'] = pulse2_3nA_10ms_delay100_per20
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 12
file = "Sequence012.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_to_0
df['PLMR'] = pulse0_to_1_4nA_to_0
df['AVBL'] = pulse0_to_1_4nA_to_0
df['AVBR'] = pulse0_to_1_4nA_to_0
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 13
file = "Sequence013.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_to_0_per100
df['PLMR'] = pulse0_to_1_4nA_to_0_per100
df['AVBL'] = pulse0_to_2_3nA_to_0_per100
df['AVBR'] = pulse0_to_2_3nA_to_0_per100
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 14
file = "Sequence014.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_10ms_delay100
df['PLMR'] = pulse1_4nA_delay0
df['AVBL'] = pulse0_to_2_3nA_to_0
df['AVBR'] = pulse2_3nA_delay0
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence PTRS - 15
file = "Sequence015.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_20ms_delay100
df['PLMR'] = pulse1_4nA_200ms_delay100
df['AVBL'] = pulse2_3nA_50ms_delay100_per100
df['AVBR'] = pulse0_to_2_3nA_to_0_per100
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 16
file = "Sequence016.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_30ms_delay100
df['PLMR'] = pulse0_to_1_4nA_plus50
df['AVBL'] = pulse2_3nA_delay0
df['AVBR'] = pulse0_to_2_3nA_to_0
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 17
file = "Sequence017.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_40ms_delay100
df['PLMR'] = pulse1_4nA_50ms_delay100_per100
df['AVBL'] = pulse0_to_2_3nA
df['AVBR'] = pulse0_to_2_3nA_to_0_per100
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 18
file = "Sequence018.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_10ms_delay100_per20
df['PLMR'] = pulse0_to_1_4nA_to_0_per100
df['AVBL'] = pulse2_3nA_50ms_delay100_per100
df['AVBR'] = pulse2_3nA_delay0
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 19
file = "Sequence019.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_to_0
df['PLMR'] = pulse0_to_1_4nA_per150
df['AVBL'] = pulse2_3nA_delay0
df['AVBR'] = pulse0_to_2_3nA_to_0_per100
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 20
file = "Sequence020.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_to_0_per100
df['PLMR'] = pulse0_to_1_4nA_plus50
df['AVBL'] = pulse0_to_2_3nA_per150
df['AVBR'] = pulse2_3nA
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 21
file = "Sequence021.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_delay0_per150
df['PLMR'] = pulse0_to_1_4nA_plus50_delay0
df['AVBL'] = pulse2_3nA_200ms_delay0
df['AVBR'] = pulse0_to_2_3nA
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 22
file = "Sequence022.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_50ms_delay100
df['PLMR'] = pulse0_to_1_4nA_delay0
df['AVBL'] = pulse2_3nA_10ms_delay0_per20
df['AVBR'] = pulse0_to_2_3nA_to_0
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 23
file = "Sequence023.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_to_0_delay0_per100
df['PLMR'] = pulse0_to_1_4nA_delay0
df['AVBL'] = pulse0_to_2_3nA_per150
df['AVBR'] = pulse2_3nA_200ms_delay100
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 24
file = "Sequence024.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_to_0
df['PLMR'] = pulse0_to_1_4nA_per150
df['AVBL'] = pulse0_to_2_3nA_plus50_delay0
df['AVBR'] = pulse0_to_2_3nA_to_0_delay0_per100
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 25
file = "Sequence025.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_50ms_delay0_per100
df['PLMR'] = pulse1_4nA_40ms_delay100
df['AVBL'] = pulse2_3nA_10ms_delay0_per20
df['AVBR'] = pulse0_to_2_3nA_delay0_per150
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 26
file = "Sequence026.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_200ms_delay100
df['PLMR'] = pulse1_4nA_200ms_delay0
df['AVBL'] = pulse0_to_2_3nA_to_0_per100
df['AVBR'] = pulse0_to_2_3nA_delay0
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 27
file = "Sequence027.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_to_0_delay0_per100
df['PLMR'] = pulse0_to_1_4nA_to_0
df['AVBL'] = pulse2_3nA_50ms_delay0_per100
df['AVBR'] = pulse2_3nA_50ms_delay100
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 28
file = "Sequence028.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA
df['PLMR'] = pulse1_4nA_delay0
df['AVBL'] = pulse2_3nA_delay0
df['AVBR'] = pulse0_to_2_3nA
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 29
file = "Sequence029.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_200ms_delay100
df['PLMR'] = pulse1_4nA_delay0
df['AVBL'] = pulse2_3nA_50ms_delay100_per100
df['AVBR'] = pulse0_to_2_3nA_to_0
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 30
file = "Sequence030.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_50ms_delay100
df['PLMR'] = pulse1_4nA_50ms_delay100_per100
df['AVBL'] = pulse0_to_2_3nA_plus50
df['AVBR'] = pulse0_to_2_3nA_to_0_per100
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence PTRS - 31
file = "Sequence031.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_50ms_delay100_per100
df['PLMR'] = pulse0_to_1_4nA
df['AVBL'] = pulse2_3nA_10ms_delay100
df['AVBR'] = pulse2_3nA_delay0
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence PTRS - 32
file = "Sequence032.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA
df['PLMR'] = pulse1_4nA_delay0
df['AVBL'] = pulse2_3nA_200ms_delay100
df['AVBR'] = pulse2_3nA_50ms_delay100_per100
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 33
file = "Sequence033.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_plus50
df['PLMR'] = pulse1_4nA_50ms_delay0
df['AVBL'] = pulse2_3nA
df['AVBR'] = pulse2_3nA_10ms_delay100_per20
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 34
file = "Sequence034.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_plus50
df['PLMR'] = pulse1_4nA_50ms_delay0
df['AVBL'] = pulse2_3nA_50ms_delay0_per100
df['AVBR'] = pulse2_3nA_200ms_delay0
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 35
file = "Sequence035.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_200ms_delay0
df['PLMR'] = pulse0_to_1_4nA_to_0
df['AVBL'] = pulse2_3nA_10ms_delay100_per20
df['AVBR'] = pulse0_to_2_3nA_delay0
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 36
file = "Sequence036.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_50ms_delay0_per100
df['PLMR'] = pulse1_4nA_50ms_delay100
df['AVBL'] = pulse0_to_2_3nA_to_0_delay0_per100
df['AVBR'] = pulse0_to_2_3nA_to_0
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 37
file = "Sequence037.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_50ms_delay0_per100
df['PLMR'] = pulse1_4nA_50ms_delay100
df['AVBL'] = pulse0_to_2_3nA_delay0_per150
df['AVBR'] = pulse0_to_2_3nA
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 38
file = "Sequence038.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_50ms_delay0
df['PLMR'] = pulse1_4nA_200ms_delay0
df['AVBL'] = pulse2_3nA_50ms_delay100
df['AVBR'] = pulse2_3nA_200ms_delay100
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 39
file = "Sequence039.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_200ms_delay0
df['PLMR'] = pulse1_4nA_200ms_delay100
df['AVBL'] = pulse2_3nA_200ms_delay0
df['AVBR'] = pulse2_3nA_200ms_delay100
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence PTRS - 40
file = "Sequence040.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_200ms_delay0
df['PLMR'] = pulse1_4nA_50ms_delay100_per100
df['AVBL'] = pulse2_3nA_200ms_delay0
df['AVBR'] = pulse2_3nA_10ms_delay100_per20
df['IL2DL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2L'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2R'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VL'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2VR'] = [0.0000] * int(simulationtime/ts + 1)
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)


###########################################################################
########################## Add + Write Files ##############################
###########################################################################
########################################################################################################################################################################
# Sequence Nictation - 01
file = "Sequence101.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse4_8nA
df['IL2DR'] = pulse4_8nA
df['IL2L'] = pulse4_8nA
df['IL2R'] = pulse4_8nA
df['IL2VL'] = pulse4_8nA
df['IL2VR'] = pulse4_8nA
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 02
file = "Sequence102.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse4_8nA_50ms_delay100_per100
df['IL2DR'] = pulse4_8nA_50ms_delay100_per100
df['IL2L'] = pulse4_8nA_50ms_delay100_per100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse4_8nA_50ms_delay100_per100
df['IL2VR'] = pulse4_8nA_50ms_delay100_per100
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence Nictation - 03
file = "Sequence103.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse0_to_4_8nA_to_0
df['IL2DR'] = pulse0_to_4_8nA_to_0
df['IL2L'] = pulse0_to_4_8nA_to_0
df['IL2R'] = pulse0_to_4_8nA_to_0
df['IL2VL'] = pulse0_to_4_8nA_to_0
df['IL2VR'] = pulse0_to_4_8nA_to_0
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence Nictation - 04
file = "Sequence104.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse0_to_4_8nA_delay0_per150
df['IL2DR'] = pulse0_to_4_8nA_delay0_per150
df['IL2L'] = pulse0_to_4_8nA_delay0_per150
df['IL2R'] = pulse0_to_4_8nA_delay0_per150
df['IL2VL'] = pulse0_to_4_8nA_delay0_per150
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 05
file = "Sequence105.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse4_8nA_delay0
df['IL2DR'] = pulse4_8nA_delay0
df['IL2L'] = pulse0_to_4_8nA_delay0_per150
df['IL2R'] = pulse0_to_4_8nA_to_0_per100
df['IL2VL'] = pulse0_to_4_8nA_delay0_per150
df['IL2VR'] = pulse0_to_4_8nA_to_0_per100
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence Nictation - 06
file = "Sequence106.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse4_8nA_delay0
df['IL2DR'] = pulse0_to_4_8nA_delay0_per150
df['IL2L'] = pulse0_to_4_8nA_delay0_per150
df['IL2R'] = pulse0_to_4_8nA_to_0_per100
df['IL2VL'] = pulse0_to_4_8nA_delay0_per150
df['IL2VR'] = pulse0_to_4_8nA_to_0_per100
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 07
file = "Sequence107.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse4_8nA_50ms_delay100_per100
df['IL2DR'] = pulse4_8nA_50ms_delay100_per100
df['IL2L'] = pulse0_to_4_8nA
df['IL2R'] = pulse0_to_4_8nA
df['IL2VL'] = pulse0_to_4_8nA_to_0
df['IL2VR'] = pulse0_to_4_8nA_to_0
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)


########################################################################################################################################################################
# Sequence Nictation - 08
file = "Sequence108.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse4_8nA_50ms_delay100_per100
df['IL2DR'] = pulse4_8nA_50ms_delay100_per100
df['IL2L'] = pulse0_to_4_8nA_per150
df['IL2R'] = pulse0_to_4_8nA_per150
df['IL2VL'] = pulse0_to_4_8nA_to_0_per100
df['IL2VR'] = pulse0_to_4_8nA_to_0_per100
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 09
file = "Sequence109.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse4_8nA
df['IL2DR'] = pulse0_to_4_8nA_to_0
df['IL2L'] = pulse4_8nA
df['IL2R'] = pulse0_to_4_8nA_to_0
df['IL2VL'] = pulse4_8nA
df['IL2VR'] = pulse0_to_4_8nA_to_0
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 10
file = "Sequence110.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse4_8nA_50ms_delay100_per100
df['IL2DR'] = pulse0_to_4_8nA_to_0_per100
df['IL2L'] = pulse4_8nA_50ms_delay100_per100
df['IL2R'] = pulse0_to_4_8nA_to_0_per100
df['IL2VL'] = pulse4_8nA_50ms_delay100_per100
df['IL2VR'] = pulse0_to_4_8nA_to_0_per100
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 11
file = "Sequence111.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse0_to_4_8nA_to_0_per100
df['IL2DR'] = pulse0_to_4_8nA
df['IL2L'] = pulse4_8nA_50ms_delay100_per100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA_to_0_per100
df['IL2VR'] = pulse0_to_4_8nA
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 12
file = "Sequence112.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse0_to_4_8nA_to_0
df['IL2DR'] = pulse0_to_4_8nA_delay0_per150
df['IL2L'] = pulse4_8nA_50ms_delay100_per100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA_to_0
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 13
file = "Sequence113.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse0_to_4_8nA_to_0
df['IL2DR'] = pulse0_to_4_8nA_delay0_per150
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA_delay0
df['IL2VR'] = pulse0_to_4_8nA_delay0
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 14
file = "Sequence114.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse0_to_4_8nA_to_0
df['IL2DR'] = pulse0_to_4_8nA_delay0_per150
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA_delay0_per150
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 15
file = "Sequence115.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse4_8_nA_delay0
df['IL2DR'] = pulse4_8nA_50ms_delay100_per100
df['IL2L'] = pulse0_to_4_8nA_delay0_per150
df['IL2R'] = pulse4_8nA_50ms_delay100
df['IL2VL'] = pulse4_8_nA_delay0
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 16
file = "Sequence116.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse4_8nA_50ms_delay100_per100
df['IL2DR'] = pulse0_to_4_8nA_delay0
df['IL2L'] = pulse0_to_4_8nA_delay0
df['IL2R'] = pulse4_8nA_50ms_delay100
df['IL2VL'] = pulse0_to_4_8nA_delay0_per150
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 17
file = "Sequence117.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse4_8nA_50ms_delay100_per100
df['IL2DR'] = pulse4_8nA_50ms_delay100
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse0_to_4_8nA_delay0
df['IL2VL'] = pulse0_to_4_8nA_per150
df['IL2VR'] = pulse0_to_4_8nA_per150
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 18
file = "Sequence118.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse0_to_4_8nA_plus50
df['IL2DR'] = pulse0_to_4_8nA_per150
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse4_8nA_30ms_delay100
df['IL2VL'] = pulse4_8nA_delay0
df['IL2VR'] = pulse0_to_4_8nA_per150
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 19
file = "Sequence119.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse4_8nA_200ms_delay100
df['IL2DR'] = pulse0_to_4_8nA_to_0_per100
df['IL2L'] = pulse0_to_4_8nA
df['IL2R'] = pulse4_8nA_200ms_delay100
df['IL2VL'] = pulse0_to_4_8nA_to_0_per100
df['IL2VR'] = pulse0_to_4_8nA
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 20
file = "Sequence120.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse4_8nA_200ms_delay100
df['IL2DR'] = pulse_0_to_4_8nA_to_0_per100
df['IL2L'] = pulse4_8nA_200ms_delay100
df['IL2R'] = pulse4_8nA_200ms_delay100
df['IL2VL'] = pulse_0_to_4_8nA_to_0_per100
df['IL2VR'] = pulse4_8nA_200ms_delay100
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Train/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 21
file = "Sequence121.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse0_to_4_8nA
df['IL2DR'] = pulse0_to_4_8nA
df['IL2L'] = pulse0_to_4_8nA
df['IL2R'] = pulse0_to_4_8nA
df['IL2VL'] = pulse0_to_4_8nA
df['IL2VR'] = pulse0_to_4_8nA
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 22
file = "Sequence122.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse0_to_4_8nA_to_0_per100
df['IL2DR'] = pulse0_to_4_8nA_to_0_per100
df['IL2L'] = pulse0_to_4_8nA_to_0_per100
df['IL2R'] = pulse0_to_4_8nA_to_0_per100
df['IL2VL'] = pulse0_to_4_8nA_to_0_per100
df['IL2VR'] = pulse0_to_4_8nA_to_0_per100
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 23
file = "Sequence123.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse4_8nA_delay0
df['IL2DR'] = pulse4_8nA_delay0
df['IL2L'] = pulse0_to_4_8nA_to_0_per100
df['IL2R'] = pulse0_to_4_8nA_delay0_per150
df['IL2VL'] = pulse0_to_4_8nA_to_0_per100
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 24
file = "Sequence124.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse0_to_4_8nA
df['IL2DR'] = pulse0_to_4_8nA_to_0_per100
df['IL2L'] = pulse4_8nA_50ms_delay100_per100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA
df['IL2VR'] = pulse0_to_4_8nA_to_0_per100
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 25
file = "Sequence125.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse4_8nA_50ms_delay100_per100
df['IL2DR'] = pulse4_8nA_delay0
df['IL2L'] = pulse0_to_4_8nA_delay0_per150
df['IL2R'] = pulse4_8nA_50ms_delay100
df['IL2VL'] = pulse0_to_4_8nA_delay0_per150
df['IL2VR'] = pulse4_8nA_delay0
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 26
file = "Sequence126.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse0_to_4_8nA_to_0
df['IL2DR'] = pulse0_to_4_8nA_delay0_per150
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA_to_0_delay0_per100
df['IL2VR'] = pulse0_to_4_8nA_to_0_delay0_per100
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 27
file = "Sequence127.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse0_to_4_8nA_delay0
df['IL2DR'] = pulse0_to_4_8nA_delay0
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA_to_0
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 28
file = "Sequence128.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse4_8nA_50ms_delay100_per100
df['IL2DR'] = pulse4_8nA_50ms_delay100
df['IL2L'] = pulse0_to_4_8nA_delay0
df['IL2R'] = pulse4_8nA_50ms_delay100
df['IL2VL'] = pulse0_to_4_8nA_per150
df['IL2VR'] = pulse0_to_4_8nA_per150
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 29
file = "Sequence129.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse0_to_4_8nA_plus50
df['IL2DR'] = pulse0_to_4_8nA_per150
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse4_8nA_30ms_delay100
df['IL2VL'] = pulse0_to_4_8nA_per150
df['IL2VR'] = pulse4_8nA_delay0
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 30
file = "Sequence130.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse4_8nA_200ms_delay100
df['IL2DR'] = pulse0_to_4_8nA
df['IL2L'] = pulse0_to_4_8nA
df['IL2R'] = pulse4_8nA_200ms_delay100
df['IL2VL'] = pulse0_to_4_8nA
df['IL2VR'] = pulse0_to_4_8nA
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Valid/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 31
file = "Sequence131.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse0_to_4_8nA_delay50
df['IL2DR'] = pulse0_to_4_8nA_delay50
df['IL2L'] = pulse0_to_4_8nA_delay50
df['IL2R'] = pulse0_to_4_8nA_delay50
df['IL2VL'] = pulse0_to_4_8nA_delay50
df['IL2VR'] = pulse0_to_4_8nA_delay50
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 32
file = "Sequence132.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse0_to_4_8nA_to_0_delay50
df['IL2DR'] = pulse0_to_4_8nA_to_0_delay50
df['IL2L'] = pulse0_to_4_8nA_to_0_delay50
df['IL2R'] = pulse0_to_4_8nA_to_0_delay50
df['IL2VL'] = pulse0_to_4_8nA_to_0_delay50
df['IL2VR'] = pulse0_to_4_8nA_to_0_delay50
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 33
file = "Sequence133.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse4_8nA_delay0
df['IL2DR'] = pulse0_to_4_8nA_delay0_per150
df['IL2L'] = pulse0_to_4_8nA_to_0_per100
df['IL2R'] = pulse0_to_4_8nA_delay0_per150
df['IL2VL'] = pulse0_to_4_8nA_to_0_per100
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 34
file = "Sequence134.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse0_to_4_8nA_delay0_per150
df['IL2DR'] = pulse0_to_4_8nA_to_0
df['IL2L'] = pulse4_8nA_50ms_delay100_per100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA_delay0_per150
df['IL2VR'] = pulse0_to_4_8nA_to_0
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 35
file = "Sequence135.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse0_to_4_8nA_delay0
df['IL2DR'] = pulse4_8nA_50ms_delay100_per100
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse0_to_4_8nA_delay0
df['IL2VL'] = pulse0_to_4_8nA_delay0_per150
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 36
file = "Sequence136.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse0_to_4_8nA_to_0
df['IL2DR'] = pulse0_to_4_8nA_delay0_per150
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA_to_0_delay0
df['IL2VR'] = pulse0_to_4_8nA_to_0_delay0
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 37
file = "Sequence137.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse0_to_4_8nA_delay0_per150
df['IL2DR'] = pulse0_to_4_8nA_delay0_per150
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA_to_0
df['IL2VR'] = pulse0_to_4_8nA_delay0_per150
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 38
file = "Sequence138.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse0_to_4_8nA_delay0
df['IL2DR'] = pulse4_8nA_50ms_delay100
df['IL2L'] = pulse4_8nA_50ms_delay100
df['IL2R'] = pulse4_8nA_50ms_delay100_per100
df['IL2VL'] = pulse0_to_4_8nA_per150
df['IL2VR'] = pulse0_to_4_8nA_per150
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 39
file = "Sequence139.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse0_to_4_8nA_to_0_per100
df['IL2DR'] = pulse0_to_4_8nA_to_0_per100
df['IL2L'] = pulse0_to_4_8nA
df['IL2R'] = pulse0_to_4_8nA_to_0_per100
df['IL2VL'] = pulse0_to_4_8nA_to_0_per100
df['IL2VR'] = pulse0_to_4_8nA
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Test/" + file, sep = " ", header=False)

########################################################################################################################################################################
# Sequence Nictation - 40
file = "Sequence140.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1',
'RMED', 'RMEL', 'RMER', 'RMEV', 'RMGL', 'RMGR', 'RMHL', 'RMHR', 'SMDDL', 'SMDDR', 'SMDVL', 'SMDVR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
df['IL2DL'] = pulse4_8nA_50ms_delay0
df['IL2DR'] = pulse0_to_4_8nA_plus50
df['IL2L'] = pulse4_8nA
df['IL2R'] = pulse4_8nA_10ms_delay100_per20
df['IL2VL'] = pulse4_8nA_10ms_delay100_per20
df['IL2VR'] = pulse4_8nA
# Save
df05 = df.iloc[df.index % 10 == 0]
df05.to_csv("../Datasets/CompleteData/Test/" + file, sep = " ", header=False)











