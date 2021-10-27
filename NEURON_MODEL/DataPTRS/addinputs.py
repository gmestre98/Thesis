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


###########################################################################
########################## Add + Write Files ##############################
###########################################################################
########################################################################################################################################################################
# Sequence 01
file = "Sequence01.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA
df['PLMR'] = pulse1_4nA
df['AVBL'] = pulse2_3nA
df['AVBR'] = pulse2_3nA
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/valid/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/valid/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/valid/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 02
file = "Sequence02.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_200ms_delay100
df['PLMR'] = pulse1_4nA_200ms_delay100
df['AVBL'] = pulse2_3nA_200ms_delay100
df['AVBR'] = pulse2_3nA_200ms_delay100
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/valid/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/valid/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/valid/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 03
file = "Sequence03.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_50ms_delay100
df['PLMR'] = pulse1_4nA_50ms_delay100
df['AVBL'] = pulse2_3nA_50ms_delay100
df['AVBR'] = pulse2_3nA_50ms_delay100
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5


########################################################################################################################################################################
# Sequence 04
file = "Sequence04.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_50ms_delay100_per100
df['PLMR'] = pulse1_4nA_50ms_delay100_per100
df['AVBL'] = pulse2_3nA_50ms_delay100_per100
df['AVBR'] = pulse2_3nA_50ms_delay100_per100
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 05
file = "Sequence05.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA
df['PLMR'] = pulse0_to_1_4nA
df['AVBL'] = pulse0_to_2_3nA
df['AVBR'] = pulse0_to_2_3nA
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/valid/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/valid/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/valid/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 06
file = "Sequence06.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_plus50
df['PLMR'] = pulse0_to_1_4nA_plus50
df['AVBL'] = pulse0_to_2_3nA_plus50
df['AVBR'] = pulse0_to_2_3nA_plus50
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 07
file = "Sequence07.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_10ms_delay100
df['PLMR'] = pulse1_4nA_10ms_delay100
df['AVBL'] = pulse2_3nA_10ms_delay100
df['AVBR'] = pulse2_3nA_10ms_delay100
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/valid/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/valid/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/valid/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 08
file = "Sequence08.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_20ms_delay100
df['PLMR'] = pulse1_4nA_20ms_delay100
df['AVBL'] = pulse2_3nA_20ms_delay100
df['AVBR'] = pulse2_3nA_20ms_delay100
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 09
file = "Sequence09.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_30ms_delay100
df['PLMR'] = pulse1_4nA_30ms_delay100
df['AVBL'] = pulse2_3nA_30ms_delay100
df['AVBR'] = pulse2_3nA_30ms_delay100
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 10
file = "Sequence10.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_40ms_delay100
df['PLMR'] = pulse1_4nA_40ms_delay100
df['AVBL'] = pulse2_3nA_40ms_delay100
df['AVBR'] = pulse2_3nA_40ms_delay100
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 11
file = "Sequence11.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_10ms_delay100_per20
df['PLMR'] = pulse1_4nA_10ms_delay100_per20
df['AVBL'] = pulse2_3nA_10ms_delay100_per20
df['AVBR'] = pulse2_3nA_10ms_delay100_per20
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/test/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/test/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/test/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 12
file = "Sequence12.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_to_0
df['PLMR'] = pulse0_to_1_4nA_to_0
df['AVBL'] = pulse0_to_1_4nA_to_0
df['AVBR'] = pulse0_to_1_4nA_to_0
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 13
file = "Sequence13.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_to_0_per100
df['PLMR'] = pulse0_to_1_4nA_to_0_per100
df['AVBL'] = pulse0_to_2_3nA_to_0_per100
df['AVBR'] = pulse0_to_2_3nA_to_0_per100
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 14
file = "Sequence14.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_10ms_delay100
df['PLMR'] = pulse1_4nA_delay0
df['AVBL'] = pulse0_to_2_3nA_to_0
df['AVBR'] = pulse2_3nA_delay0
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 15
file = "Sequence15.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_20ms_delay100
df['PLMR'] = pulse1_4nA_200ms_delay100
df['AVBL'] = pulse2_3nA_50ms_delay100_per100
df['AVBR'] = pulse0_to_2_3nA_to_0_per100
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/valid/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/valid/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/valid/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 16
file = "Sequence16.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_30ms_delay100
df['PLMR'] = pulse0_to_1_4nA_plus50
df['AVBL'] = pulse2_3nA_delay0
df['AVBR'] = pulse0_to_2_3nA_to_0
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 17
file = "Sequence17.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_40ms_delay100
df['PLMR'] = pulse1_4nA_50ms_delay100_per100
df['AVBL'] = pulse0_to_2_3nA
df['AVBR'] = pulse0_to_2_3nA_to_0_per100
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/valid/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/valid/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/valid/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 18
file = "Sequence18.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_10ms_delay100_per20
df['PLMR'] = pulse0_to_1_4nA_to_0_per100
df['AVBL'] = pulse2_3nA_50ms_delay100_per100
df['AVBR'] = pulse2_3nA_delay0
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/test/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/test/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/test/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 19
file = "Sequence19.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_to_0
df['PLMR'] = pulse0_to_1_4nA_per150
df['AVBL'] = pulse2_3nA_delay0
df['AVBR'] = pulse0_to_2_3nA_to_0_per100
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/valid/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/valid/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/valid/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 20
file = "Sequence20.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_to_0_per100
df['PLMR'] = pulse0_to_1_4nA_plus50
df['AVBL'] = pulse0_to_2_3nA_per150
df['AVBR'] = pulse2_3nA
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 21
file = "Sequence21.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_delay0_per150
df['PLMR'] = pulse0_to_1_4nA_plus50_delay0
df['AVBL'] = pulse2_3nA_200ms_delay0
df['AVBR'] = pulse0_to_2_3nA
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/valid/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/valid/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/valid/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 22
file = "Sequence22.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_50ms_delay100
df['PLMR'] = pulse0_to_1_4nA_delay0
df['AVBL'] = pulse2_3nA_10ms_delay0_per20
df['AVBR'] = pulse0_to_2_3nA_to_0
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 23
file = "Sequence23.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_to_0_delay0_per100
df['PLMR'] = pulse0_to_1_4nA_delay0
df['AVBL'] = pulse0_to_2_3nA_per150
df['AVBR'] = pulse2_3nA_200ms_delay100
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 24
file = "Sequence24.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_to_0
df['PLMR'] = pulse0_to_1_4nA_per150
df['AVBL'] = pulse0_to_2_3nA_plus50_delay0
df['AVBR'] = pulse0_to_2_3nA_to_0_delay0_per100
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/test/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/test/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/test/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 25
file = "Sequence25.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_50ms_delay0_per100
df['PLMR'] = pulse1_4nA_40ms_delay100
df['AVBL'] = pulse2_3nA_10ms_delay0_per20
df['AVBR'] = pulse0_to_2_3nA_delay0_per150
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/test/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/test/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/test/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 26
file = "Sequence26.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_200ms_delay100
df['PLMR'] = pulse1_4nA_200ms_delay0
df['AVBL'] = pulse0_to_2_3nA_to_0_per100
df['AVBR'] = pulse0_to_2_3nA_delay0
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 27
file = "Sequence27.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_to_0_delay0_per100
df['PLMR'] = pulse0_to_1_4nA_to_0
df['AVBL'] = pulse2_3nA_50ms_delay0_per100
df['AVBR'] = pulse2_3nA_50ms_delay100
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/test/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/test/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/test/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 28
file = "Sequence28.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA
df['PLMR'] = pulse1_4nA_delay0
df['AVBL'] = pulse2_3nA_delay0
df['AVBR'] = pulse0_to_2_3nA
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 29
file = "Sequence29.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_200ms_delay100
df['PLMR'] = pulse1_4nA_delay0
df['AVBL'] = pulse2_3nA_50ms_delay100_per100
df['AVBR'] = pulse0_to_2_3nA_to_0
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 30
file = "Sequence30.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_50ms_delay100
df['PLMR'] = pulse1_4nA_50ms_delay100_per100
df['AVBL'] = pulse0_to_2_3nA_plus50
df['AVBR'] = pulse0_to_2_3nA_to_0_per100
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 31
file = "Sequence31.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_50ms_delay100_per100
df['PLMR'] = pulse0_to_1_4nA
df['AVBL'] = pulse2_3nA_10ms_delay100
df['AVBR'] = pulse2_3nA_delay0
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 32
file = "Sequence32.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA
df['PLMR'] = pulse1_4nA_delay0
df['AVBL'] = pulse2_3nA_200ms_delay100
df['AVBR'] = pulse2_3nA_50ms_delay100_per100
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/test/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/test/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/test/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 33
file = "Sequence33.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_plus50
df['PLMR'] = pulse1_4nA_50ms_delay0
df['AVBL'] = pulse2_3nA
df['AVBR'] = pulse2_3nA_10ms_delay100_per20
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/valid/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/valid/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/valid/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 34
file = "Sequence34.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_plus50
df['PLMR'] = pulse1_4nA_50ms_delay0
df['AVBL'] = pulse2_3nA_50ms_delay0_per100
df['AVBR'] = pulse2_3nA_200ms_delay0
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/test/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/test/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/test/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 35
file = "Sequence35.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_200ms_delay0
df['PLMR'] = pulse0_to_1_4nA_to_0
df['AVBL'] = pulse2_3nA_10ms_delay100_per20
df['AVBR'] = pulse0_to_2_3nA_delay0
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/test/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/test/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/test/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 36
file = "Sequence36.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_50ms_delay0_per100
df['PLMR'] = pulse1_4nA_50ms_delay100
df['AVBL'] = pulse0_to_2_3nA_to_0_delay0_per100
df['AVBR'] = pulse0_to_2_3nA_to_0
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/test/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/test/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/test/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 37
file = "Sequence37.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_50ms_delay0_per100
df['PLMR'] = pulse1_4nA_50ms_delay100
df['AVBL'] = pulse0_to_2_3nA_delay0_per150
df['AVBR'] = pulse0_to_2_3nA
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/valid/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/valid/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/valid/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/valid/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 38
file = "Sequence38.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_50ms_delay0
df['PLMR'] = pulse1_4nA_200ms_delay0
df['AVBL'] = pulse2_3nA_50ms_delay100
df['AVBR'] = pulse2_3nA_200ms_delay100
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 39
file = "Sequence39.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_200ms_delay0
df['PLMR'] = pulse1_4nA_200ms_delay100
df['AVBL'] = pulse2_3nA_200ms_delay0
df['AVBR'] = pulse2_3nA_200ms_delay100
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/test/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/test/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-05-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/test/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/test/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 40
file = "Sequence40.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_200ms_delay0
df['PLMR'] = pulse1_4nA_50ms_delay100_per100
df['AVBL'] = pulse2_3nA_200ms_delay0
df['AVBR'] = pulse2_3nA_10ms_delay100_per20
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-10-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-20-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 41
file = "Sequence41.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_50ms_delay0
df['PLMR'] = pulse0_to_1_4nA_plus50
df['AVBL'] = pulse2_3nA
df['AVBR'] = pulse2_3nA_10ms_delay100_per20
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 42
file = "Sequence42.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_plus50
df['PLMR'] = pulse0_to_1_4nA_50ms_delay0
df['AVBL'] = pulse2_3nA
df['AVBR'] = pulse2_3nA_10ms_delay100_per20
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 43
file = "Sequence43.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_plus50
df['PLMR'] = pulse0_to_1_4nA_to_0_50ms_delay0
df['AVBL'] = pulse2_3nA
df['AVBR'] = pulse2_3nA_10ms_delay100_per20
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 44
file = "Sequence44.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_50ms_delay0
df['PLMR'] = pulse0_to_1_4nA_plus50
df['AVBL'] = pulse2_3nA
df['AVBR'] = pulse2_3nA_10ms_delay100_per20
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 45
file = "Sequence45.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_to_0_50ms_delay0
df['PLMR'] = pulse0_to_1_4nA_plus50
df['AVBL'] = pulse2_3nA
df['AVBR'] = pulse2_3nA_10ms_delay100_per20
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-25-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 46
file = "Sequence46.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_delay0_per150
df['PLMR'] = pulse0_to_1_4nA_delay0_per150
df['AVBL'] = pulse0_to_2_3nA_delay0_per150
df['AVBR'] = pulse0_to_2_3nA_delay0_per150
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 47
file = "Sequence47.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse_ramp_47_1
df['PLMR'] = pulse_ramp_47_1
df['AVBL'] = pulse_ramp_47_2
df['AVBR'] = pulse_ramp_47_2
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 48
file = "Sequence48.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse_triangle_48
df['PLMR'] = pulse_triangle_48
df['AVBL'] = pulse_triangle_48
df['AVBR'] = pulse_triangle_48
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 49
file = "Sequence49.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse_triangle_49_1
df['PLMR'] = pulse_triangle_49_1
df['AVBL'] = pulse_triangle_49_2
df['AVBR'] = pulse_triangle_49_2
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 50
file = "Sequence50.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_10ms_delay100
df['PLMR'] = pulse1_4nA_delay0
df['AVBL'] = pulse2_3nA_delay0
df['AVBR'] = pulse0_to_2_3nA_to_0
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 51
file = "Sequence51.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_to_0
df['PLMR'] = pulse1_4nA_delay0
df['AVBL'] = pulse2_3nA_delay0
df['AVBR'] = pulse2_3nA_delay0
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 52
file = "Sequence52.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_10ms_delay100
df['PLMR'] = pulse0_to_1_4nA_to_0
df['AVBL'] = pulse2_3nA_delay0
df['AVBR'] = pulse2_3nA_delay0
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 53
file = "Sequence53.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_to_0_per100
df['PLMR'] = pulse0_to_1_4nA_plus50
df['AVBL'] = pulse2_3nA
df['AVBR'] = pulse0_to_2_3nA_per150
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 54
file = "Sequence54.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_40ms_delay100
df['PLMR'] = pulse1_4nA_50ms_delay100_per100
df['AVBL'] = pulse0_to_2_3nA_to_0_per100
df['AVBR'] = pulse0_to_2_3nA
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 55
file = "Sequence55.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_50ms_delay100
df['PLMR'] = pulse1_4nA_50ms_delay100_per100
df['AVBL'] = pulse0_to_2_3nA_to_0_per100
df['AVBR'] = pulse0_to_2_3nA_plus50
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 56
file = "Sequence56.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA
df['PLMR'] = pulse1_4nA
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 57
file = "Sequence57.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = pulse2_3nA
df['AVBR'] = pulse2_3nA
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 58
file = "Sequence58.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA_to_0
df['PLMR'] = pulse0_to_1_4nA_to_0
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 59
file = "Sequence59.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = pulse0_to_1_4nA_to_0
df['AVBR'] = pulse0_to_1_4nA_to_0
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 60
file = "Sequence60.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse0_to_1_4nA
df['PLMR'] = pulse0_to_1_4nA
df['AVBL'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBR'] = [0.0000] * int(simulationtime/ts + 1)
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 61
file = "Sequence61.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = [0.0000] * int(simulationtime/ts + 1)
df['PLMR'] = [0.0000] * int(simulationtime/ts + 1)
df['AVBL'] = pulse0_to_2_3nA
df['AVBR'] = pulse0_to_2_3nA
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 62
file = "Sequence62.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_50ms_delay0
df['PLMR'] = pulse0_to_1_4nA_plus50
df['AVBL'] = pulse2_3nA_200ms_delay0
df['AVBR'] = pulse2_3nA_50ms_delay0_per100
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 63
file = "Sequence63.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA
df['PLMR'] = pulse1_4nA_delay0
df['AVBL'] = pulse0_to_2_3nA
df['AVBR'] = pulse2_3nA_delay0
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 64
file = "Sequence64.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_50ms_delay100_per100
df['PLMR'] = pulse1_4nA_200ms_delay0
df['AVBL'] = pulse2_3nA_10ms_delay100_per20
df['AVBR'] = pulse2_3nA_200ms_delay0
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5

########################################################################################################################################################################
# Sequence 65
file = "Sequence65.dat"
cols = ['time', 'AS1', 'AS7', 'DA1', 'DA9', 'DB1', 'DB5', 'DD1', 'DVA', 'LUAL', 'PHCL', 'PLML', 'PVCL', 'PVR', 'SIBVL', 'VB1', 'VD1']
save4 = ['time', 'DB1', 'LUAL', 'PVR', 'VB1', 'PLML2', 'PLMR', 'AVBL', 'AVBR']
df = pd.read_csv(file, sep = "\s+", names=cols)
df['PLML2'] = pulse1_4nA_200ms_delay100
df['PLMR'] = pulse1_4nA_200ms_delay0
df['AVBL'] = pulse2_3nA_200ms_delay100
df['AVBR'] = pulse2_3nA_200ms_delay0
# Save Base
df.to_csv("../Datasets/PTRS-45-0_05-16/train/" + file, sep = " ", header=False)
df[save4].to_csv("../Datasets/PTRS-45-0_05-4/train/" + file, sep = " ", header=False)
# Reduce Timestep
df05 = df.iloc[df.index % 10 == 0]
# Save Experiment 1
df05[save4].to_csv("../Datasets/PTRS-40-0_5-4/train/" + file, sep = " ", header=False)
df05[save4].to_csv("../Datasets/PTRS-45-0_5-4/train/" + file, sep = " ", header=False)
# Save Experiment 2
# Save Experiment 5