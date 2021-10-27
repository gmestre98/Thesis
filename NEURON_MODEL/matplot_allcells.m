% %
% Simulation of C.Elegans network
% All cells (303 neurons), with only LeakConductance channel
% Synapses as in CElegans.net.nml (excitatory and inhibitory)
%
% Generic_GJ conductance changed from 1pS to 100 pS 
% (gap junction as in Kim2019, taken from Varshney2011)
%
% data_all: Forward Crawling Scenario: all cells, all synapses
%           - stimulus as in Kim2019: 1.4nA to PLM*, 2.3nA to AVB*
%           - should see response in most of the neurons
% data_all_noAVB: AVB* Ablation + Forward Crawling Scenario: 
%           - all cells except AVB*, all synapses except AVB* connected
%           - stimulus as in Kim2019: 1.4nA to PLM*, [2.3nA to AVB*]
%           - should see much smaller or even no response in most of the neurons
% data_all_noAVA: AVA* Ablation + Forward Crawling Scenario: 
%           - all cells except AVA*, all synapses except AVA* connected
%           - stimulus as in Kim2019: 1.4nA to PLM*, 2.3nA to AVB*
%           - should be similar to first scenario, response in most of the neurons
% %

close all

% clear all
data_all = load('all_cells.dat');
data_all_noAVB = load('all_cells_noAVB.dat');
data_all_noAVA = load('all_cells_noAVA.dat');
data_all_IL2 = load('all_cells_IL2.dat');

% 
% Positions in array data_all (missing from the next arrays, respectively):
% AVBL: 57, AVBR: 58
% AVAL: 55, AVAR: 56
%
nrn = 'PVCR';
cells=readtable('all_cells_list.txt')

figure(18);
plot(...
    data_all(:,1)*1e3,data_all(:,find(strcmp(cells.Cell,nrn)==1)+1)*1e3,'-',...
    data_all_noAVB(:,1)*1e3,data_all_noAVB(:,find(strcmp(cells.Cell,nrn)==1)+1)*1e3,'-.',...
    data_all_noAVA(:,1)*1e3,data_all_noAVA(:,find(strcmp(cells.Cell,nrn)==1)+1)*1e3,'--',...
'LineWidth',2);
title({'Results simulation of C.Elegans network',...
    'Scenario: Forward Crawling.',['Neuron response: ',nrn]});
legend('Voltage recorded FM',...
    'Voltage recorded FM without AVB',...
    'Voltage recorded FM without AVA');
xlabel('Time [msec]'); ylabel('Voltage [mV]');
grid on;
set(gca,'FontSize',14);

%
% List the strongest responses (>100 mV)
%
fprintf('Cells with response over 100 mV (data_all):\n');
disp(cells(max(data_all)>0.1,1));
fprintf('Cells with response over 100 mV (data_all_noAVB):\n');
disp(cells(max(data_all)>0.1,1))

fprintf('\nCells with response over 100 mV in data_all = %i\n',...
    sum((max(data_all)>0.1)));
fprintf('\nCells with response over 100 mV in data_all_noAVB = %i\n',...
    sum((max(data_all_noAVB)>0.1)));


%
% IL2
%
nrnIL2 = 'IL2DL';
cells=readtable('all_cells_list.txt')

figure(20);
plot(...
    data_all(:,1)*1e3,data_all(:,find(strcmp(cells.Cell,nrn)==1)+1)*1e3,'-',...
    data_all_IL2(:,1)*1e3,data_all_IL2(:,find(strcmp(cells.Cell,nrn)==1)+1)*1e3,'--',...
'LineWidth',2);
title({'Results simulation of C.Elegans network',...
    'Scenario: Nictation.',['Neuron response: ',nrnIL2]});
legend('Voltage recorded FM',...
    'Voltage recorded Nictation');
xlabel('Time [msec]'); ylabel('Voltage [mV]');
grid on;
set(gca,'FontSize',14);