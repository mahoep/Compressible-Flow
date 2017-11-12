function [M_find] = PressureRatio(k,ratio)
%PRESSURERATIO Finds Mach Number for given pressure ratio
%   Detailed explanation goes here
M = [0:0.00001:20];

for i = 1:length(M)
    P_ratio(i) = (1+0.5*(k-1)*M(i)^2)^(k/(k-1));
    P_ratio(i) = P_ratio(i)^-1;
end
 
[~,j] = find(ratio==P_ratio);
M_find = M(j);

if isempty(M_find) == 1
    [~,i] = min(abs(ratio-P_ratio));
    M_find = M(i);
end

    
end

