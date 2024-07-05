function k = inverse_kinematics(px,py,pz)
%Thông s? robot(mm)
d1 = 96.28;
a1 = 13.9;
a2 = 120;
a3 = 117.85;
a4 = 63.64;
%Tính theta1
theta1 = atan2(py,px);
%Tính theta3
A = px*cos(theta1)+py*sin(theta1)-a1-a4;
B = pz-d1;
c3 = (A^2+B^2-a3^2-a2^2)/(2*a3*a2);
s3 = sqrt(1-c3^2);
theta3 = atan2(s3,c3);
%Tính theta2
c2 = A*(a3*c3+a2)+a3*s3*B;
s2 = B*(a3*c3+a2)-a3*s3*A;
theta2 = atan2(s2,c2);
%Tính theta4
theta4 = -theta2-theta3;
k = [theta1,theta2,theta3,theta4];