TITLE Mod file for component: Component(id=pulse0_to_4_8nA_delay0 type=pulseGenerator)

COMMENT

    This NEURON file has been generated by org.neuroml.export (see https://github.com/NeuroML/org.neuroml.export)
         org.neuroml.export  v1.7.0
         org.neuroml.model   v1.7.0
         jLEMS               v0.10.2

ENDCOMMENT

NEURON {
    POINT_PROCESS pulse0_to_4_8nA_delay0
    ELECTRODE_CURRENT i
    RANGE weight                            : property
    RANGE delay                             : parameter
    RANGE duration                          : parameter
    RANGE amplitude                         : parameter
    
}

UNITS {
    
    (nA) = (nanoamp)
    (uA) = (microamp)
    (mA) = (milliamp)
    (A) = (amp)
    (mV) = (millivolt)
    (mS) = (millisiemens)
    (uS) = (microsiemens)
    (molar) = (1/liter)
    (kHz) = (kilohertz)
    (mM) = (millimolar)
    (um) = (micrometer)
    (umol) = (micromole)
    (S) = (siemens)
    
}

PARAMETER {
    
    weight = 1
    delay = 0 (ms)
    duration = 100 (ms)
    amplitude = 4.8 (nA)
}

STATE {
    i (nA) 
    
}

INITIAL {
    rates()
    rates() ? To ensure correct initialisation.
    
}

BREAKPOINT {
    
    rates()
    if (t <  delay) {
        i = 0 ? standard OnCondition
    }
    
    if (t >=  delay  && t <  duration  +  delay) {
        i = weight  *  amplitude * (t-delay)/duration ? standard OnCondition
    }
    
    if (t >=  duration  +  delay) {
        i = 0 ? standard OnCondition
    }
    
    
}

PROCEDURE rates() {
    
    
     
    
}

