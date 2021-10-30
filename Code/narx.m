%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Preprocessing Start
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear all;
dataTrain = {};
XTrain = {}; XTest = {}; XValidation = {};
YTrain = {}; YTest = {}; YValidation = {};

folderTrain = '../Datasets/PTRS-20-0_5-4/Train';
filesTrain = dir([folderTrain '/*.dat']);
folderValid = '../Datasets/PTRS-20-0_5-4/Valid';
filesValid = dir([folderValid '/*.dat']);
folderTest = '../Datasets/PTRS-20-0_5-4/Test';
filesTest = dir([folderTest '/*.dat']);


% Reading the files
for k=1:length(filesTrain)
  filename = filesTrain(k).name;  
  dataTrain{k} = load([folderTrain '/' filename]);
end
for k=1:length(filesValid)
  filename = filesValid(k).name;  
  dataValid{k} = load([folderValid '/' filename]);
end
for k=1:length(filesTest)
  filename = filesTest(k).name;  
  dataTest{k} = load([folderTest '/' filename]);
end

% Separating X and Y
for k=1:length(dataTrain)
  XTrain{k} = dataTrain{k}(:,7:end)';
  YTrain{k} = dataTrain{k}(:,3:6)';
end
XTrain = XTrain';
YTrain = YTrain';

for k=1:length(dataValid)
  XValidation{k} = dataValid{k}(:,7:end)';
  YValidation{k} = dataValid{k}(:,3:6)';
end
XValidation = XValidation';
YValidation = YValidation';

for k=1:length(dataTest)
  XTest{k} = dataTest{k}(:,7:end)';
  YTest{k} = dataTest{k}(:,3:6)';
end
XTest = XTest';
YTest = YTest';

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Preprocessing End
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Declaring the network
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

numFeatures = size(XTrain{1},1);
numResponses = size(YTrain{1},1);
numHiddenUnits = {112}; %TEST THIS NUMBER OF UNITS
DelayY = 2; %TEST THIS DELAY
DelayX = 4; %TEST THIS DELAY
folder_list = {'../Experiment1/NARX-PTRS/112/Run10/'};

for foldernum=1:length(folder_list)

    folder_list{foldernum}
    
    net = narxnet(1:DelayX, 1:DelayY, numHiddenUnits{foldernum});
    XTotTrain = con2seq(XTrain{1});
    YTotTrain = con2seq(YTrain{1});
    for k=2:length(XTrain)
      XTotTrain = catsamples(XTotTrain, con2seq(XTrain{k}), 'pad');
      YTotTrain = catsamples(YTotTrain, con2seq(YTrain{k}), 'pad');
    end

    [XsTrain, XiTrain, AiTrain, YsTrain] = ...
         preparets(net, XTotTrain, {}, YTotTrain);
    net.divideParam.trainRatio = 1;
    net.divideParam.valRatio   = 0;
    net.divideParam.testRatio  = 0;
    net = train(net, XsTrain, YsTrain, XiTrain);


    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Plot Validation Results
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    XTotValidation = con2seq(XValidation{1});
    YTotValidation = con2seq(YValidation{1});
    for k=2:10
      XTotValidation = catsamples(XTotValidation, con2seq(XValidation{k}), 'pad');
      YTotValidation = catsamples(YTotValidation, con2seq(YValidation{k}), 'pad');
    end

    %% now close the loop for testing
    netc = closeloop(net);

    [XsValidation, XiValidation, AiValidation, YsValidation] = ...
         preparets(netc, XTotValidation, {}, YTotValidation);

    YcValidation = netc(XsValidation, XiValidation, AiValidation);
    perval{foldernum} = perform(netc, YsValidation, YcValidation) ;

    [XsTrain, XiTrain, AiTrain, YsTrain] = preparets(netc, XTotTrain, {}, YTotTrain);
    YYY = netc(XsTrain, XiTrain, AiTrain);
    pertrain{foldernum} = perform(netc, YsTrain, YYY);
    for k=1:10
      %% DB1
      figure(1+4*(k-1))
      hold on
      grabkth = @(x) x(1,k);
      plot(cellfun(grabkth, YTotValidation), 'r', 'LineWidth',2);
      plot(cellfun(grabkth, YcValidation), 'k', 'LineWidth',2);
      legend('DB1 -- real','DB1 -- predicted');
      xt = get(gca, 'XTick');
      set(gca, 'XTick',xt, 'XTickLabel',xt/2);
      xlabel('Time [sec]');
      ylabel('Voltage [V]');
      temp = [folder_list{foldernum},'fig',num2str(1+4*(k-1)),'.png'];
      saveas(gca, temp);
      %% LUAL
      figure(2+4*(k-1))
      hold on
      grabkth = @(x) x(2,k);
      plot(cellfun(grabkth, YTotValidation), 'r', 'LineWidth',2);
      plot(cellfun(grabkth, YcValidation), 'k', 'LineWidth',2);
      legend('LUAL -- real','LUAL -- predicted');
      xt = get(gca, 'XTick');
      set(gca, 'XTick',xt, 'XTickLabel',xt/2);
      xlabel('Time [sec]');
      ylabel('Voltage [V]');
      temp = [folder_list{foldernum},'fig',num2str(2+4*(k-1)),'.png'];
      saveas(gca, temp);

      %% PVR
      figure(3+4*(k-1))
      hold on
      grabkth = @(x) x(3,k);
      plot(cellfun(grabkth, YTotValidation), 'r', 'LineWidth',2);
      plot(cellfun(grabkth, YcValidation), 'k', 'LineWidth',2);
      legend('PVR -- real','PVR -- predicted');
      xt = get(gca, 'XTick');
      set(gca, 'XTick',xt, 'XTickLabel',xt/2);
      xlabel('Time [sec]');
      ylabel('Voltage [V]');
      temp = [folder_list{foldernum},'fig',num2str(3+4*(k-1)),'.png'];
      saveas(gca, temp);

      %% VB1
      figure(4+4*(k-1))
      hold on
      grabkth = @(x) x(4,k);
      plot(cellfun(grabkth, YTotValidation), 'r', 'LineWidth',2);
      plot(cellfun(grabkth, YcValidation), 'k', 'LineWidth',2);
      legend('VB1 -- real','VB1 -- predicted');
      xt = get(gca, 'XTick');
      set(gca, 'XTick',xt, 'XTickLabel',xt/2);
      xlabel('Time [sec]');
      ylabel('Voltage [V]');
      temp = [folder_list{foldernum},'fig',num2str(4+4*(k-1)),'.png'];
      saveas(gca, temp);
    end
    
    
%     for k=1:10
%       %% RMED
%       figure(1+6*(k-1))
%       hold on
%       grabkth = @(x) x(1,k);
%       plot(cellfun(grabkth, YTotValidation), 'r', 'LineWidth',2);
%       plot(cellfun(grabkth, YcValidation), 'k', 'LineWidth',2);
%       legend('RMED -- real','RMED -- predicted');
%       xt = get(gca, 'XTick');
%       set(gca, 'XTick',xt, 'XTickLabel',xt/2);
%       xlabel('Time [sec]');
%       ylabel('Voltage [V]');
%       temp = [folder_list{foldernum},'fig',num2str(1+6*(k-1)),'.png'];
%       saveas(gca, temp);
% 
%       %% RMEL
%       figure(2+6*(k-1))
%       hold on
%       grabkth = @(x) x(2,k);
%       plot(cellfun(grabkth, YTotValidation), 'r', 'LineWidth',2);
%       plot(cellfun(grabkth, YcValidation), 'k', 'LineWidth',2);
%       legend('RMEL -- real','RMEL -- predicted');
%       xt = get(gca, 'XTick');
%       set(gca, 'XTick',xt, 'XTickLabel',xt/2);
%       xlabel('Time [sec]');
%       ylabel('Voltage [V]');
%       temp = [folder_list{foldernum},'fig',num2str(2+6*(k-1)),'.png'];
%       saveas(gca, temp);
% 
%       %% RMER
%       figure(3+6*(k-1))
%       hold on
%       grabkth = @(x) x(3,k);
%       plot(cellfun(grabkth, YTotValidation), 'r', 'LineWidth',2);
%       plot(cellfun(grabkth, YcValidation), 'k', 'LineWidth',2);
%       legend('RMER -- real','RMER -- predicted');
%       xt = get(gca, 'XTick');
%       set(gca, 'XTick',xt, 'XTickLabel',xt/2);
%       xlabel('Time [sec]');
%       ylabel('Voltage [V]');
%       temp = [folder_list{foldernum},'fig',num2str(3+6*(k-1)),'.png'];
%       saveas(gca, temp);
% 
%       %% RMEV
%       figure(4+6*(k-1))
%       hold on
%       grabkth = @(x) x(4,k);
%       plot(cellfun(grabkth, YTotValidation), 'r', 'LineWidth',2);
%       plot(cellfun(grabkth, YcValidation), 'k', 'LineWidth',2);
%       legend('RMEV -- real','RMEV -- predicted');
%       xt = get(gca, 'XTick');
%       set(gca, 'XTick',xt, 'XTickLabel',xt/2);
%       xlabel('Time [sec]');
%       ylabel('Voltage [V]');
%       temp = [folder_list{foldernum},'fig',num2str(4+6*(k-1)),'.png'];
%       saveas(gca, temp);
%       
%       %% RMGL
%       figure(4+6*(k-1))
%       hold on
%       grabkth = @(x) x(5,k);
%       plot(cellfun(grabkth, YTotValidation), 'r', 'LineWidth',2);
%       plot(cellfun(grabkth, YcValidation), 'k', 'LineWidth',2);
%       legend('RMGL -- real','RMGL -- predicted');
%       xt = get(gca, 'XTick');
%       set(gca, 'XTick',xt, 'XTickLabel',xt/2);
%       xlabel('Time [sec]');
%       ylabel('Voltage [V]');
%       temp = [folder_list{foldernum},'fig',num2str(5+6*(k-1)),'.png'];
%       saveas(gca, temp);
%       
%       %% RMGR
%       figure(5+6*(k-1))
%       hold on
%       grabkth = @(x) x(6,k);
%       plot(cellfun(grabkth, YTotValidation), 'r', 'LineWidth',2);
%       plot(cellfun(grabkth, YcValidation), 'k', 'LineWidth',2);
%       legend('RMGR -- real','RMGR -- predicted');
%       xt = get(gca, 'XTick');
%       set(gca, 'XTick',xt, 'XTickLabel',xt/2);
%       xlabel('Time [sec]');
%       ylabel('Voltage [V]');
%       temp = [folder_list{foldernum},'fig',num2str(6+6*(k-1)),'.png'];
%       saveas(gca, temp);
%     end

    

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Plot Test Results
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    XTotTest = con2seq(XTest{1});
    YTotTest = con2seq(YTest{1});
    for k=2:10
      XTotTest = catsamples(XTotTest, con2seq(XTest{k}), 'pad');
      YTotTest = catsamples(YTotTest, con2seq(YTest{k}), 'pad');
    end
    
    %% now close the loop for testing
    netc = closeloop(net);
    
    [XsTest, XiTest, AiTest  YsTest] = ...
         preparets(netc, XTotTest, {}, YTotTest);
    
    YcTest = netc(XsTest, XiTest, AiTest);
    pertest{foldernum} = perform(netc, YsTest, YcTest);
    for k=1:10
      % DB1
      figure(41+4*(k-1))
      hold on
      grabkth = @(x) x(1,k);
      plot(cellfun(grabkth, YTotTest), 'r', 'LineWidth',2);
      plot(cellfun(grabkth, YcTest), 'k', 'LineWidth',2);
      legend('DB1 -- real','DB1 -- predicted');
      xt = get(gca, 'XTick');
      set(gca, 'XTick',xt, 'XTickLabel',xt/2);
      xlabel('Time [sec]');
      ylabel('Voltage [V]');
      temp = [folder_list{foldernum},'fig',num2str(41+4*(k-1)),'.png'];
      saveas(gca, temp);
      
      % LUAL
      figure(42+4*(k-1))
      hold on
      grabkth = @(x) x(2,k);
      plot(cellfun(grabkth, YTotTest), 'r', 'LineWidth',2);
      plot(cellfun(grabkth, YcTest), 'k', 'LineWidth',2);
      legend('LUAL -- real','LUAL -- predicted');
      xt = get(gca, 'XTick');
      set(gca, 'XTick',xt, 'XTickLabel',xt/2);
      xlabel('Time [sec]');
      ylabel('Voltage [V]');
      temp = [folder_list{foldernum},'fig',num2str(42+4*(k-1)),'.png'];
      saveas(gca, temp);
      
      % PVR
      figure(43+4*(k-1))
      hold on
      grabkth = @(x) x(3,k);
      plot(cellfun(grabkth, YTotTest), 'r', 'LineWidth',2);
      plot(cellfun(grabkth, YcTest), 'k', 'LineWidth',2);
      legend('PVR -- real','PVR -- predicted');
      xt = get(gca, 'XTick');
      set(gca, 'XTick',xt, 'XTickLabel',xt/2);
      xlabel('Time [sec]');
      ylabel('Voltage [V]');
      temp = [folder_list{foldernum},'fig',num2str(43+4*(k-1)),'.png'];
      saveas(gca, temp);
      
      % VB1
      figure(44+4*(k-1))
      hold on
      grabkth = @(x) x(4,k);
      plot(cellfun(grabkth, YTotTest), 'r', 'LineWidth',2);
      plot(cellfun(grabkth, YcTest), 'k', 'LineWidth',2);
      legend('VB1 -- real','VB1 -- predicted');
      xt = get(gca, 'XTick');
      set(gca, 'XTick',xt, 'XTickLabel',xt/2);
      xlabel('Time [sec]');
      ylabel('Voltage [V]');
      temp = [folder_list{foldernum},'fig',num2str(44+4*(k-1)),'.png'];
      saveas(gca, temp);
    end
    
%     for k=1:10
%       %% RMED
%       figure(61+6*(k-1))
%       hold on
%       grabkth = @(x) x(1,k);
%       plot(cellfun(grabkth, YTotTest), 'r', 'LineWidth',2);
%       plot(cellfun(grabkth, YcTest), 'k', 'LineWidth',2);
%       legend('RMED -- real','RMED -- predicted');
%       xt = get(gca, 'XTick');
%       set(gca, 'XTick',xt, 'XTickLabel',xt/2);
%       xlabel('Time [sec]');
%       ylabel('Voltage [V]');
%       temp = [folder_list{foldernum},'fig',num2str(61+6*(k-1)),'.png'];
%       saveas(gca, temp);
% 
%       %% RMEL
%       figure(62+6*(k-1))
%       hold on
%       grabkth = @(x) x(2,k);
%       plot(cellfun(grabkth, YTotTest), 'r', 'LineWidth',2);
%       plot(cellfun(grabkth, YcTest), 'k', 'LineWidth',2);
%       legend('RMEL -- real','RMEL -- predicted');
%       xt = get(gca, 'XTick');
%       set(gca, 'XTick',xt, 'XTickLabel',xt/2);
%       xlabel('Time [sec]');
%       ylabel('Voltage [V]');
%       temp = [folder_list{foldernum},'fig',num2str(62+6*(k-1)),'.png'];
%       saveas(gca, temp);
% 
%       %% RMER
%       figure(63+6*(k-1))
%       hold on
%       grabkth = @(x) x(3,k);
%       plot(cellfun(grabkth, YTotTest), 'r', 'LineWidth',2);
%       plot(cellfun(grabkth, YcTest), 'k', 'LineWidth',2);
%       legend('RMER -- real','RMER -- predicted');
%       xt = get(gca, 'XTick');
%       set(gca, 'XTick',xt, 'XTickLabel',xt/2);
%       xlabel('Time [sec]');
%       ylabel('Voltage [V]');
%       temp = [folder_list{foldernum},'fig',num2str(63+6*(k-1)),'.png'];
%       saveas(gca, temp);
% 
%       %% RMEV
%       figure(64+6*(k-1))
%       hold on
%       grabkth = @(x) x(4,k);
%       plot(cellfun(grabkth, YTotTest), 'r', 'LineWidth',2);
%       plot(cellfun(grabkth, YcTest), 'k', 'LineWidth',2);
%       legend('RMEV -- real','RMEV -- predicted');
%       xt = get(gca, 'XTick');
%       set(gca, 'XTick',xt, 'XTickLabel',xt/2);
%       xlabel('Time [sec]');
%       ylabel('Voltage [V]');
%       temp = [folder_list{foldernum},'fig',num2str(64+6*(k-1)),'.png'];
%       saveas(gca, temp);
%       
%       %% RMGL
%       figure(65+6*(k-1))
%       hold on
%       grabkth = @(x) x(5,k);
%       plot(cellfun(grabkth, YTotTest), 'r', 'LineWidth',2);
%       plot(cellfun(grabkth, YcTest), 'k', 'LineWidth',2);
%       legend('RMGL -- real','RMGL -- predicted');
%       xt = get(gca, 'XTick');
%       set(gca, 'XTick',xt, 'XTickLabel',xt/2);
%       xlabel('Time [sec]');
%       ylabel('Voltage [V]');
%       temp = [folder_list{foldernum},'fig',num2str(65+6*(k-1)),'.png'];
%       saveas(gca, temp);
%       
%       %% RMGR
%       figure(66+6*(k-1))
%       hold on
%       grabkth = @(x) x(6,k);
%       plot(cellfun(grabkth, YTotTest), 'r', 'LineWidth',2);
%       plot(cellfun(grabkth, YcTest), 'k', 'LineWidth',2);
%       legend('RMGR -- real','RMGR -- predicted');
%       xt = get(gca, 'XTick');
%       set(gca, 'XTick',xt, 'XTickLabel',xt/2);
%       xlabel('Time [sec]');
%       ylabel('Voltage [V]');
%       temp = [folder_list{foldernum},'fig',num2str(66+6*(k-1)),'.png'];
%       saveas(gca, temp);
%     end
    close all
end
