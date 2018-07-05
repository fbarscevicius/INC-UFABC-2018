%Fitzhugh-Nagumo

clear all

I=1;
a=0.7; b=0.8; c=0.08;

%solucao plano de fase
vminmax=-3:0.5:3;
rminmax=-3:0.5:3;

[V,R]=meshgrid(vminmax,rminmax);
VV=V-V.^3/3-R+I;
RR=c*(V+a-b*R);

figure
subplot(221)
hold on
quiver(V,R,VV,RR);
xlabel('v')
ylabel('r')
axis([-3 3 -3 3])

%solucao temporal com metodo de euler
tmax=100;

dt=0.25;

tempo=0:dt:tmax;

%I=0*(tempo>50 & tempo<55);

v(1)=0.15;
r(1)=-0.6243;

for p=1:length(tempo) 
 dvdt=(v(p)-v(p).^3/3-r(p)+I);
 v(p+1)=v(p)+dvdt*dt;
 drdt=c*(v(p)+a-b*r(p));
 r(p+1)=r(p)+drdt*dt;

 figure(1)
 subplot(221)
 hold on
 plot(v(p),r(p),'b.')
 axis([-3 3 -3 3])
 axis square
 subplot(222)
 plot(tempo(p),v(p),'k.')
 hold on
 axis([0 tmax -3 3])
 axis square
 ylabel('v')
 xlabel('Time(ms)')
 subplot(224)
 plot(tempo(p),r(p),'r.')
 hold on
 axis([0 tmax -3 3])
 axis square
 ylabel('r')
 xlabel('Time(ms)')
 subplot(223)
 quiver(v(p),r(p),dvdt,drdt,'k')
 xlabel('v')
 ylabel('r')
 axis square
 drawnow
end
v(end)=[];
r(end)=[];

subplot(221)
hold on
plot(v,r,'-b','linewidth',2);

subplot(222)
hold on
plot(tempo,v,'-k','linewidth',2)

subplot(224)
hold on
plot(tempo,r,'-r','linewidth',2)
 
