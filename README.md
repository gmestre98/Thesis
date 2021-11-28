# Master Thesis

This repository is the official repository for my Master Thesis.
This thesis concerns a comparison on the ability of different machine learning techniques to model the behavior of the *Caenorhabditis elegans* nervous system during Nictation and Posterior Touch Response Stimulation.
More information about the work developed can be found in the documents "Tese.pdf" and "Extended_Abstract.pdf".

## Content

  * Tese.pdf - Full thesis document
  * Extended_Abstract.pdf - Extended Abstract of the thesis
  * Code - Folder containing the Code used in this thesis. This folder will contain its own README.md file in the future.
  * DataFull - Folder containing the data files generated with NEURON for the dataset representing both behaviors
  * DataPTRS - Folder containing the data files generated with NEURON for the dataset representing Posterior Touch Response Stimulation
  * DataFull - Folder containing the data files generated with NEURON for the dataset representing Nictation
  * Datasets - Folder containing the data after some preprocessing, which was used to train and evaluate the models' performance
  * Experiment1 - Folder containing the results and data obtained with experiment 1
  * Experiment2 - Folder containing the results and data obtained with experiment 2
  * Experiment3 - Folder containing the results and data obtained with experiment 3
  * Experiment4 - Folder containing the results and data obtained with experiment 4
  * Hyperparameters - Folder containing the results and data obtained for all the hyperparameters experiments
  * NEURON_MODEL - Folder containing the NEURON model and the files used to generate data corresponding to both behaviors. This folder will contain its own README.md file in the future.
  * SampleRate - Folder containing the results and data obtained for the experiments regarding the Sample Rate

## Experiments folder

  This section explains the structure of the folders "Experiment1", "Experiment2", "Experiment3", "Experiment4", "Hyperparameters" and "SampleRate"
  All of this folders contain various subfolders, for which the folder names correspond to the experiment settings with the structure diverging for each experiment.
  After navigating to the folder of the specific setting you want to check, you may find 10 different folders named "RunX", for each of the 10 different times that setting was run.
  Inside each of these folders you will find the results obtained.
