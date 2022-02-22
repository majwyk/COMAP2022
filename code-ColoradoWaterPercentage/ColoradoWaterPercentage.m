close all
clear
clc
stateName = ["Arizona", "California", "Colorado", "NewMexico", "Wyoming"];
sz = size(stateName);
sz = sz(2);
totalUsage = readtable('2010年美国用水情况.xlsx');
coloradoUsage = readtable('2010年Colorado River取水情况');
coloradoUsage = coloradoUsage(1:5,1:2:5);
coloradoUsage.Properties.RowNames = coloradoUsage(:,1).Variables;
coloradoUsage.Properties.RowNames{4} = 'NewMexico';
for i = 1:sz
    coloradoUsage(stateName(i),2) = {coloradoUsage(stateName(i),2).Variables+coloradoUsage(stateName(i),3).Variables};
end
coloradoUsage = coloradoUsage(:,2);
coloradoUsage = rows2vars(coloradoUsage);
coloradoUsage = coloradoUsage(:,2:6);
totalUsage.Properties.RowNames = totalUsage(:,1).Variables;
totalUsage = totalUsage([3,5,6,32,51],15);
totalUsage = rows2vars(totalUsage);
totalUsage = totalUsage(:,2:6);
for i = 1:sz
    totalUsage(1,i) = {totalUsage(1,i).Variables/1000};
end
dependence = table();
for i = 1:sz
    dependence(1,stateName(i)) = {coloradoUsage(1,stateName(i)).Variables/totalUsage(1,stateName(i)).Variables};
end

disp(dependence);
