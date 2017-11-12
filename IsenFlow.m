function [P,rho,T,A,PtA,v,mu] = IsenFlow(k,M)
% this function takes in k and a Mach number and will compute the ratios
% for P/Pt rho/rhot T/Tt A/A* PA/PtA* v(Prandtl turning angle) mu(shock angle) for
% isentropic flow

P = (1+0.5*(k-1)*M^2)^(k/(k-1));
rho = (1+0.5*(k-1)*M^2)^(1/(k-1));
T = 1 + (k-1)/2*M^2;
A = (1/M*((1+0.5*(k-1)*M^2)/(0.5*(k+1)))^(0.5*(k+1)/(k-1)))^-1;
v = ((k+1)/(k-1))^(1/2)*atand(((k-1)/(k+1)*(M^2-1))^(1/2))-atand((M^2-1)^(1/2));
mu = asind(1/M);

P = P^-1;
rho = rho^-1;
T = T^-1;
A = A^-1;
PtA = P*A;
end