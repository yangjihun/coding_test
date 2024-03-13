N = int(input())
r = [0,0,0]
g = [0,0,0]
b = [0,0,0]
for i in range(N):
  rgb = list(map(int,input().split()))
  if i==1:
    r = [rgb[0]+min(r[1],r[2]),rgb[1]+r[0],rgb[2]+r[0]]
    g = [rgb[0]+g[0],rgb[1]+min(g[0],g[2]),rgb[2]+g[0]]
    g = [rgb[0]+b[2],rgb[1]+b[2],rgb[2]+min(b[0],b[1])]
  elif i==(N-1):
    r = [200,rgb[1]+min(r[0],r[2]),rgb[2]+min(r[0],r[1])]
    g = [rgb[0]+min(g[1],g[2]),200,rgb[2]+min(g[0],g[1])]
    b = [rgb[0]+min(b[1],b[2]),rgb[1]+min(b[0],b[2]),200]
  else:
    r = [rgb[0]+min(r[1],r[2]),rgb[1]+min(r[0],r[2]),rgb[2]+min(r[0],r[1])]
    g = [rgb[0]+min(g[1],g[2]),rgb[1]+min(g[0],g[2]),rgb[2]+min(g[0],g[1])]
    b = [rgb[0]+min(b[1],b[2]),rgb[1]+min(b[0],b[2]),rgb[2]+min(b[0],b[1])]
print(min(min(r),min(g),min(b)))