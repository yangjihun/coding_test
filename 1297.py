D,H,W = map(int,input().split()) # D: 대각선 길이 / H: 높이 / W: 너비

x = ((D**2)*W//(H+W))**(1/2)
print(x)