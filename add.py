import math
import random

# GLOBAL VARIABLES:

vertices = []
faces = []

# LITTLE LIBRARY (version 1.2b): 

def newface(A,RGB):
  global vertices, faces
  Q = ''
  for i in range (len(A)):
    Q += ' '+str(i+len(vertices))
  faces += [str(len(A))+str(Q)+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  for i in range (len(A)):
    vertices += [str(A[i][0])+' '+str(A[i][1])+' '+str(A[i][2])]

def cube(c,e,RGB): # c - center, e - edge width, RGB - color
  global vertices, faces
  F = [[0,4,5,1],[0,1,3,2],[0,2,6,4],[1,5,7,3],[2,3,7,6],[4,6,7,5]]
  V = [[0,0,0],[0,0,e],[0,e,0],[0,e,e],[e,0,0],[e,0,e],[e,e,0],[e,e,e]] 
  for i in range (0,6):
    faces += ['4 '+str(F[i][0]+len(vertices))+' '+str(F[i][1]+len(vertices))+' '+str(F[i][2]+len(vertices))+
    ' '+str(F[i][3]+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  for j in range (0,8):
    vertices += [str(c[0]+V[j][0]-e/2)+' '+str(c[1]+V[j][1]-e/2)+' '+str(c[2]+V[j][2]-e/2)]

def rectangle3D(c,e,RGB): # c - center, e - width of edges, RGB - color
  global vertices, faces
  F = [[0,4,5,1],[0,1,3,2],[0,2,6,4],[1,5,7,3],[2,3,7,6],[4,6,7,5]]
  V = [[0,0,0],[0,0,e[2]],[0,e[1],0],[0,e[1],e[2]],[e[0],0,0],[e[0],0,e[2]],[e[0],e[1],0],[e[0],e[1],e[2]]] 
  for i in range (0,6):
    faces += ['4 '+str(F[i][0]+len(vertices))+' '+str(F[i][1]+len(vertices))+' '+str(F[i][2]+len(vertices))+
    ' '+str(F[i][3]+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  for j in range (0,8):
    vertices += [str(c[0]+V[j][0]-e[0]/2)+' '+str(c[1]+V[j][1]-e[1]/2)+' '+str(c[2]+V[j][2]-e[2]/2)]

def circle(A,B,r,k,RGB): # A - start point, B - end point, r - radius, k - detail, RGB - color
  global vertices, faces
  for i in range (1,k):
    faces += ['3 '+str(2*i+len(vertices))+' '+str(2*k+len(vertices))+
    ' '+str(2*i-2+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  faces += ['3 '+str(0+len(vertices))+' '+str(2*k+len(vertices))+
  ' '+str(2*k-2+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  if A[0]==B[0] and A[1]==B[1]:
    p1=-math.sqrt(2)*r/2
    p2=(B[2]-A[2])/abs(B[2]-A[2])*p1
    p3=-p1
    p4=p2
    p5=0
  else:
    d=math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2)+math.pow(B[2]-A[2],2))
    f=math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2))
    p1=-r*(B[1]-A[1])/f
    p2=-r*(B[0]-A[0])*(B[2]-A[2])/(d*f)
    p3=r*(B[0]-A[0])/f
    p4=-r*(B[1]-A[1])*(B[2]-A[2])/(d*f)
    p5=r*f/d
  for i in range (0,k):
    sinn=math.sin(i/k*2*math.pi)
    coss=math.cos(i/k*2*math.pi)
    q1=coss*p1+sinn*p2
    q2=coss*p3+sinn*p4
    q3=sinn*p5
    vertices += [str(A[0]+q1)+' '+str(A[1]+q2)+' '+str(A[2]+q3)] + [str(B[0]+q1)+' '+str(B[1]+q2)+' '+str(B[2]+q3)]
  vertices += [str(A[0])+' '+str(A[1])+' '+str(A[2])]

def spin3D(A,B,S,min_t,max_t,grid_t,k,RGB): # A - start point, B - end point, r - radius, k - detail, RGB - color, S - parametric function
  global vertices, faces
  def rendervertices(A,B,r):
    global vertices
    if A[0]==B[0] and A[1]==B[1]:
      p1=-math.sqrt(2)*r/2
      p2=(B[2]-A[2])/abs(B[2]-A[2])*p1
      p3=-p1
      p4=p2
      p5=0
    else:
      d=math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2)+math.pow(B[2]-A[2],2))
      f=math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2))
      p1=-r*(B[1]-A[1])/f
      p2=-r*(B[0]-A[0])*(B[2]-A[2])/(d*f)
      p3=r*(B[0]-A[0])/f
      p4=-r*(B[1]-A[1])*(B[2]-A[2])/(d*f)
      p5=r*f/d
    for i in range (1,k+1):
      sinn=math.sin(i/k*2*math.pi)
      coss=math.cos(i/k*2*math.pi)
      q1=coss*p1+sinn*p2
      q2=coss*p3+sinn*p4
      q3=sinn*p5
      vertices += [str(B[0]+q1)+' '+str(B[1]+q2)+' '+str(B[2]+q3)]
  for j in range (grid_t):
    for i in range (k-1):
      faces += ['4 '+str(j*k+i+len(vertices))+' '+str(j*k+i+1+len(vertices))+' '+str((j+1)*k+i+1+len(vertices))+
      ' '+str((j+1)*k+i+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
    faces += ['4 '+str((j+1)*k-1+len(vertices))+' '+str(j*k+len(vertices))+' '+str((j+1)*k+len(vertices))+
      ' '+str((j+1)*k-1+k+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  AB = math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2)+math.pow(B[2]-A[2],2))
  for j in range (grid_t+1):
    t = min_t+(max_t-min_t)/grid_t*j
    g = S(t)
    C = [None,None,None]
    for h in range (3):
      C[h] = A[h] + (B[h]-A[h]) * g[1] / AB
    if A[0] == C[0] and A[1] == C[1] and A[2] == C[2]:
      rendervertices([2*C[0]-B[0],2*C[1]-B[1],2*C[2]-B[2]],C,g[0])  
    else:
      if g[1]<=0:
        rendervertices([2*C[0]-A[0],2*C[1]-A[1],2*C[2]-A[2]],C,g[0])
      else:
        rendervertices(A,C,g[0])
	
def pyramid(c,e,h,RGB): # c - center, e - edge width, h - high, RGB - color
  global vertices, faces
  F = [[[0,1,2,3],[1,4,2],[3,2,4],[0,3,4],[0,4,1]],[[3,2,1,0],[2,4,1],[4,2,3],[4,3,0],[1,4,0]]]
  V = [[0,0,0],[e,0,0],[e,0,e],[0,0,e],[e/2,h,e/2]]
  idx = 0
  if h < 0:
    idx = 1
  for i in range (1,5):
    faces += ['3 '+str(F[idx][i][0]+len(vertices))+' '+str(F[idx][i][1]+len(vertices))+' '+str(F[idx][i][2]+len(vertices))+
    ' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  faces += ['4 '+str(F[idx][0][0]+len(vertices))+' '+str(F[idx][0][1]+len(vertices))+' '+str(F[idx][0][2]+len(vertices))+
    ' '+str(F[idx][0][3]+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  for j in range (0,5):
    vertices += [str(c[0]+V[j][0]-e/2)+' '+str(c[1]+V[j][1]-e/2)+' '+str(c[2]+V[j][2]-e/2)]

def cube2(c,e,b,RGB): # c - center, b - border width, e - edge width, RGB - color
  global vertices, faces
  F = [[2,3,9,7],[1,6,9,3],[7,5,0,2],[0,5,6,1],[8,9,12,13],[12,9,6,10],[8,13,11,5],[6,5,11,10],
  [19,14,12,18],[12,10,15,18],[11,14,19,16],[10,11,16,15],[4,17,18,3],[3,18,15,1],[1,15,16,0],[0,16,17,4],
  [21,22,4,3],[21,3,2,20],[22,23,0,4],[23,20,2,0],[26,27,9,8],[7,9,27,25],[8,5,28,26],[25,28,5,7],
  [32,30,12,14],[12,30,31,13],[31,34,11,13],[34,32,14,11],[37,19,18,36],[35,36,18,17],[39,35,17,16],[39,16,19,37],
  [21,24,38,36],[22,21,36,35],[23,22,35,39],[24,23,39,38],[27,29,24,21],[21,20,25,27],[23,28,25,20],[23,24,29,28],
  [29,27,30,33],[27,26,31,30],[28,29,33,34],[26,28,34,31],[36,38,33,30],[37,36,30,32],[34,33,38,39],[39,37,32,34]]
  V = [[0,0,0],[0,b,b],[b,0,b],[b,b,b],[b,b,0],[0,0,e],[0,b,e-b],[b,0,e-b],
  [b,b,e],[b,b,e-b],[0,e-b,e-b],[0,e,e],[b,e-b,e-b],[b,e-b,e],[b,e,e-b],[0,e-b,b],
  [0,e,0],[b,e-b,0],[b,e-b,b],[b,e,b],[e-b,0,b],[e-b,b,b],[e-b,b,0],[e,0,0],
  [e,b,b],[e-b,0,e-b],[e-b,b,e],[e-b,b,e-b],[e,0,e],[e,b,e-b],[e-b,e-b,e-b],[e-b,e-b,e],
  [e-b,e,e-b],[e,e-b,e-b],[e,e,e],[e-b,e-b,0],[e-b,e-b,b],[e-b,e,b],[e,e-b,b],[e,e,0]] 
  for i in range (0,48):
    faces += ['4 '+str(F[i][0]+len(vertices))+' '+str(F[i][1]+len(vertices))+' '+str(F[i][2]+len(vertices))+
    ' '+str(F[i][3]+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  for j in range (0,40):
    vertices += [str(c[0]+V[j][0]-e/2)+' '+str(c[1]+V[j][1]-e/2)+' '+str(c[2]+V[j][2]-e/2)]

def parametric(S,min_u,max_u,grid_u,min_v,max_v,grid_v,RGB): # S - parametric uv surface, grid - detail, RGB - color
  global vertices, faces
  for i in range (grid_u):
    for j in range (grid_v):
      A = i*(grid_v+1)+j
      B = A+grid_v+1
      faces += ['4 '+str(A+len(vertices))+' '+str(B+len(vertices))+' '+str(B+1+len(vertices))+
      ' '+str(A+1+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  for i in range (grid_u+1):
    for j in range (grid_v+1):
      u = min_u+(max_u-min_u)/grid_u*i
      v = min_v+(max_v-min_v)/grid_v*j
      f = S(u,v)
      vertices += [str(f[0])+' '+str(f[1])+' '+str(f[2])]

def curve(P,min_t,max_t,grid_t,k,r,RGB,isConnected): # P - parametric 3D curve, ranges (min_t, max_t), detail parameters (grid_t, k), r - radiusm RGB - color, isConnected - connectivity (True/False)
  global vertices, faces
  for i in range(grid_t-1):
    for j in range (k-1):
      faces += ['4 '+str(i*k+j+len(vertices))+' '+str(i*k+j+1+len(vertices))+' '+str(i*k+j+k+1+len(vertices))+
      ' '+str(i*k+j+k+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
    faces += ['4 '+str(i*k+k-1+len(vertices))+' '+str(i*k+0+len(vertices))+' '+str(i*k+k+len(vertices))+
    ' '+str(i*k+2*k-1+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  if isConnected==True:
    for j in range (k-1):
      faces += ['4 '+str((grid_t-2)*k+j+k+len(vertices))+' '+str((grid_t-2)*k+j+k+1+len(vertices))+' '+str(j+1+len(vertices))+
      ' '+str(j+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
    faces += ['4 '+str((grid_t-2)*k+2*k-1+len(vertices))+' '+str((grid_t-2)*k+k+len(vertices))+' '+str((0)*k+0+len(vertices))+
    ' '+str((0)*k+k-1+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  else:
    for j in range (k-1):
      faces += ['4 '+str((grid_t-1)*k+j+len(vertices))+' '+str((grid_t-1)*k+j+1+len(vertices))+' '+str((grid_t-1)*k+j+k+1+len(vertices))+
      ' '+str((grid_t-1)*k+j+k+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
      faces += ['3 '+str(grid_t*k+j+len(vertices))+' '+str(grid_t*k+j+1+len(vertices))+
      ' '+str((grid_t+1)*k+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
      faces += ['3 '+str(j+1+len(vertices))+' '+str(j+len(vertices))+
      ' '+str((grid_t+1)*k+1+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
    faces += ['4 '+str((grid_t-1)*k+k-1+len(vertices))+' '+str((grid_t-1)*k+0+len(vertices))+' '+str((grid_t-1)*k+k+len(vertices))+
    ' '+str((grid_t-1)*k+2*k-1+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
    faces += ['3 '+str(grid_t*k+k-1+len(vertices))+' '+str(grid_t*k+len(vertices))+
    ' '+str((grid_t+1)*k+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
    faces += ['3 '+str(0+len(vertices))+' '+str(k-1+len(vertices))+
    ' '+str((grid_t+1)*k+1+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  def qvect1(P,t,h):
    a = P(t)
    b = P(t+h)
    return([a[0]+(b[0]-a[0])/h,a[1]+(b[1]-a[1])/h,a[2]+(b[2]-a[2])/h])
  def taylor(R,h):
    return(R[2]+(-R[0]+8*R[1]-8*R[3]+R[4])/(12*h))
  def qvect2(P,t,h):
    R = [[None for i in range(5)] for j in range(3)]
    for i in range(5): 
      c = P(t-(i-2)*h)
      for j in range(3):
        R[j][i] = c[j]
    return([taylor(R[0],h),taylor(R[1],h),taylor(R[2],h)])
  def vproject(A,B):
    q = (A[0]*B[0]+A[1]*B[1]+A[2]*B[2])/(A[0]**2+A[1]**2+A[2]**2)
    return([B[0]-A[0]*q,B[1]-A[1]*q,B[2]-A[2]*q])
  def anglev(A,B):
    return((A[0]*B[0]+A[1]*B[1]+A[2]*B[2])/math.sqrt((A[0]**2+A[1]**2+A[2]**2)*(B[0]**2+B[1]**2+B[2]**2)))
  def acos2(x):
    if x < -1:
      return (math.pi)
    elif x > 1:
      return (0)
    else:
      return (math.acos(x))
  def arot(A,B,C1,C2):
    alpha = 0
    A1 = vproject(A,B)
    if A1[0]**2+A1[1]**2+A1[2]**2>1e-12:
      A2 = [A[1]*A1[2]-A[2]*A1[1],A[2]*A1[0]-A[0]*A1[2],A[0]*A1[1]-A[1]*A1[0]]
      B1 = vproject(B,[-A[0],-A[1],-A[2]])
      alpha1 = acos2(anglev(A1,C1))
      if anglev(A2,C1) < 0:
        alpha1 = -alpha1
      alpha2 = acos2(anglev(B1,C2))
      if anglev(A2,C2) < 0:
        alpha2 = -alpha2
      alpha = alpha1-alpha2
    else:
      if anglev(A,B) < 0:
        alpha = math.pi
    return(alpha)
  def brot(A,B,pre):
    if A[0]==B[0] and A[1]==B[1]:
      p1=-math.sqrt(2)/2
      p2=(B[2]-A[2])/abs(B[2]-A[2])*p1
      p3=-p1
      p4=p2
      p5=0
    else:
      d=math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2)+math.pow(B[2]-A[2],2))
      f=math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2))
      p1=-(B[1]-A[1])/f
      p2=-(B[0]-A[0])*(B[2]-A[2])/(d*f)
      p3=(B[0]-A[0])/f
      p4=-(B[1]-A[1])*(B[2]-A[2])/(d*f)
      p5=f/d
    alpha = arot(pre[0],[B[0]-A[0],B[1]-A[1],B[2]-A[2]],pre[1],[p1,p3,0])
    sinn=math.sin(alpha)
    coss=math.cos(alpha) 
    new = [[B[0]-A[0],B[1]-A[1],B[2]-A[2]],[coss*p1+sinn*p2,coss*p3+sinn*p4,sinn*p5],alpha]
    return(new)
  def cpoints(A,B,r,k,pre,beta):
    global vertices
    if A[0]==B[0] and A[1]==B[1]:
      p1=-math.sqrt(2)*r/2
      p2=(B[2]-A[2])/abs(B[2]-A[2])*p1
      p3=-p1
      p4=p2
      p5=0
    else:
      d=math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2)+math.pow(B[2]-A[2],2))
      f=math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2))
      p1=-r*(B[1]-A[1])/f
      p2=-r*(B[0]-A[0])*(B[2]-A[2])/(d*f)
      p3=r*(B[0]-A[0])/f
      p4=-r*(B[1]-A[1])*(B[2]-A[2])/(d*f)
      p5=r*f/d
    alpha = arot(pre[0],[B[0]-A[0],B[1]-A[1],B[2]-A[2]],pre[1],[p1,p3,0])
    sinn=math.sin(alpha)
    coss=math.cos(alpha) 
    new = [[B[0]-A[0],B[1]-A[1],B[2]-A[2]],[coss*p1+sinn*p2,coss*p3+sinn*p4,sinn*p5]]
    for i in range (0,k):
      sinn=math.sin(i/k*2*math.pi+alpha+beta)
      coss=math.cos(i/k*2*math.pi+alpha+beta)
      q1=coss*p1+sinn*p2
      q2=coss*p3+sinn*p4
      q3=sinn*p5
      vertices += [str(A[0]+q1)+' '+str(A[1]+q2)+' '+str(A[2]+q3)]
    return(new)
  P1 = P(min_t)
  if isConnected==False:
    P2 = qvect1(P,min_t,1e-8)
  else:
    P2 = qvect2(P,min_t,1e-4)
  rconstant = True
  if isinstance(r, int) == False and isinstance(r, float) == False:
    rconstant = False
  if rconstant:
    pre = cpoints(P1,P2,r,k,[[P2[0]-P1[0],P2[1]-P1[1],P2[2]-P1[2]],[0,0,1]],0)
  else:
    pre = cpoints(P1,P2,r(min_t),k,[[P2[0]-P1[0],P2[1]-P1[1],P2[2]-P1[2]],[0,0,1]],0)
  beta = 0 
  if isConnected==True:
    pre2 = pre
    for i in range(1,grid_t+1):
      t = min_t+i*(max_t-min_t)/grid_t
      pre2 = brot(P(t),qvect2(P,t,1e-4),pre2)
    beta = pre2[2]
  for i in range(1,grid_t):
    t = min_t+i*(max_t-min_t)/grid_t
    if rconstant:
      pre = cpoints(P(t),qvect2(P,t,1e-4),r,k,pre,-i*beta/(grid_t))
    else:
      pre = cpoints(P(t),qvect2(P,t,1e-4),r(t),k,pre,-i*beta/(grid_t))
  if isConnected==False:
    P3 = P(max_t)
    if rconstant:
      cpoints(P3,qvect1(P,max_t,-1e-8),r,k,pre,0)
    else:
      cpoints(P3,qvect1(P,max_t,-1e-8),r(max_t),k,pre,0)
    vertices += [str(P3[0])+' '+str(P3[1])+' '+str(P3[2])]
    vertices += [str(P1[0])+' '+str(P1[1])+' '+str(P1[2])]

def sphere(c,r,k,RGB): # c - center, r - radius, k - detail, RGB - color
  global vertices, faces
  M = [[None for j in range(k+1)] for i in range(k)]
  def render1(pr,k,st,RGB):
    global faces
    Q = [[None for j in range(k+1)] for i in range(k+1)]
    for i in range (k):
      for j in range (k+1):
        Q[i][j] = pr+j+i*(k+1)
    for i in range (k+1):
      Q[k][i] = st+i+1
    for i in range (k):
      for j in range (k):
        faces += ['4 '+str(Q[i][j]+len(vertices))+' '+str(Q[i+1][j]+len(vertices))+' '+str(Q[i+1][j+1]+len(vertices))+
        ' '+str(Q[i][j+1]+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  def render2(pr,k,RGB):
    global faces
    Q = [[None for j in range(k-1)] for i in range(k-1)]
    for i in range (k-1):
      for j in range (k-1):
        Q[i][j] = pr+j+i*(k-1)
    for i in range (k-2):
      for j in range (k-2):
        faces += ['4 '+str(Q[i][j]+len(vertices))+' '+str(Q[i+1][j]+len(vertices))+' '+str(Q[i+1][j+1]+len(vertices))+
        ' '+str(Q[i][j+1]+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  def render3(a,b,c,d,RGB):
    global faces
    faces += ['4 '+str(a+len(vertices))+' '+str(b+len(vertices))+' '+str(c+len(vertices))+' '+str(d+len(vertices))+
    ' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  def render4(a1,a2,b1,b2,k,RGB):
    global faces
    p = a2-a1
    q = b2-b1
    for i in range (k-2):
      faces += ['4 '+str(a1+i*p+len(vertices))+' '+str(a1+(i+1)*p+len(vertices))+' '+str(b1+(i+1)*q+len(vertices))+
      ' '+str(b1+i*q+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  render1(0,k,k**2+k-1,RGB)
  render1(k*(k+1),k,2*k**2+2*k-1,RGB)
  render1(2*k*(k+1),k,3*k**2+3*k-1,RGB)
  render1(3*k*(k+1),k,-1,RGB)
  if k == 1:
    faces += ['4 '+str(0+len(vertices))+' '+str(6+len(vertices))+' '+str(4+len(vertices))+' '+str(2+len(vertices))+
    ' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
    faces += ['4 '+str(1+len(vertices))+' '+str(3+len(vertices))+' '+str(5+len(vertices))+' '+str(7+len(vertices))+
    ' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  else:
    render2(4*k*(k+1),k,RGB)
    render2(5*k**2+2*k+1,k,RGB)
    render3(k+1,0,(k+1)*(4*k-1),4*k**2+5*k-2,RGB)
    render3((k+1)**2,k*(k+1),(k-1)*(k+1),k*(5*k+2),RGB)
    render3((k+1)*(2*k+1),2*k*(k+1),(k+1)*(2*k-1),5*k**2+k+2,RGB)
    render3((k+1)*(3*k+1),3*k*(k+1),(k+1)*(3*k-1),4*k*(k+1),RGB)
    render3(4*k**2+4*k-1,k,2*k+1,5*k**2+2*k+1,RGB)
    render3(3*k**2+3*k-1,k*(3*k+4),3*k**2+5*k+1,5*k**2+3*k-1,RGB)
    render3(2*k**2+2*k-1,k*(2*k+3),2*k**2+4*k+1,6*k**2+1,RGB)
    render3(k**2+k-1,k*(k+2),k**2+3*k+1,6*k**2-k+3,RGB)
    render4(4*k**2+5*k-2,4*k**2+6*k-3,k+1,2*k+2,k,RGB)
    render4(k*(5*k+2),5*k**2+2*k-1,(k+1)**2,(k+2)*(k+1),k,RGB)
    render4(5*k**2+k+2,5*k**2+3,(k+1)*(2*k+1),2*(k+1)**2,k,RGB)
    render4(4*k*(k+1),(2*k+1)**2,(k+1)*(3*k+1),(k+1)*(3*k+2),k,RGB)
    render4(2*k+1,3*k+2,5*k**2+2*k+1,k*(5*k+3),k,RGB)
    render4(k**2+3*k+1,k**2+4*k+2,6*k**2-k+3,6*k**2-k+4,k,RGB)
    render4(2*k**2+4*k+1,(k+2)*(2*k+1),6*k**2+1,6*k**2-k+2,k,RGB)
    render4(3*k**2+5*k+1,3*k**2+6*k+2,5*k**2+3*k-1,(k+1)*(5*k-2),k,RGB)
  for i in range (k):
    for j in range (k+1):
      x = 1/math.tan(math.pi/4+math.pi/2*i/k)
      y = 1/math.tan(math.pi/4+math.pi/2*j/k)
      d = r/math.sqrt(math.pow(x,2)+math.pow(y,2)+1)
      M[i][j] = [x*d,y*d,d]
      vertices += [str(c[0]+M[i][j][0])+' '+str(c[1]+M[i][j][1])+' '+str(c[2]+M[i][j][2])]
  for i in range (k):
    for j in range (k+1):
      vertices += [str(c[0]-M[i][j][2])+' '+str(c[1]+M[i][j][1])+' '+str(c[2]+M[i][j][0])]
  for i in range (k):
    for j in range (k+1):
      vertices += [str(c[0]-M[i][j][0])+' '+str(c[1]+M[i][j][1])+' '+str(c[2]-M[i][j][2])]
  for i in range (k):
    for j in range (k+1):
      vertices += [str(c[0]+M[i][j][2])+' '+str(c[1]+M[i][j][1])+' '+str(c[2]-M[i][j][0])]
  for i in range (1,k):
    for j in range (1,k):
      vertices += [str(c[0]+M[i][j][0])+' '+str(c[1]+M[i][j][2])+' '+str(c[2]-M[i][j][1])]
  for i in range (1,k):
    for j in range (1,k):
      vertices += [str(c[0]+M[i][j][0])+' '+str(c[1]-M[i][j][2])+' '+str(c[2]+M[i][j][1])]

def cylinder(A,B,r,k,RGB): # A - start point, B - end point, r - radius, k - detail, RGB - color
  global vertices, faces
  for i in range (1,k):
    faces += ['4 '+str(2*i-2+len(vertices))+' '+str(2*i+len(vertices))+' '+str(2*i+1+len(vertices))+
    ' '+str(2*i-1+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
    faces += ['3 '+str(2*i+len(vertices))+' '+str(2*i-2+len(vertices))+' '+str(2*k+len(vertices))+
    ' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
    faces += ['3 '+str(2*i-1+len(vertices))+' '+str(2*i+1+len(vertices))+' '+str(2*k+1+len(vertices))+
    ' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  faces += ['4 '+str(2*k-2+len(vertices))+' '+str(0+len(vertices))+' '+str(1+len(vertices))+
  ' '+str(2*k-1+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  faces += ['3 '+str(0+len(vertices))+' '+str(2*k-2+len(vertices))+' '+str(2*k+len(vertices))+
  ' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  faces += ['3 '+str(1+len(vertices))+' '+str(2*k+1+len(vertices))+' '+str(2*k-1+len(vertices))+
  ' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  if A[0]==B[0] and A[1]==B[1]:
    p1=-math.sqrt(2)*r/2
    p2=(B[2]-A[2])/abs(B[2]-A[2])*p1
    p3=-p1
    p4=p2
    p5=0
  else:
    d=math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2)+math.pow(B[2]-A[2],2))
    f=math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2))
    p1=-r*(B[1]-A[1])/f
    p2=-r*(B[0]-A[0])*(B[2]-A[2])/(d*f)
    p3=r*(B[0]-A[0])/f
    p4=-r*(B[1]-A[1])*(B[2]-A[2])/(d*f)
    p5=r*f/d
  for i in range (1,k+1):
    sinn=math.sin(i/k*2*math.pi)
    coss=math.cos(i/k*2*math.pi)
    q1=coss*p1+sinn*p2
    q2=coss*p3+sinn*p4
    q3=sinn*p5
    vertices += [str(A[0]+q1)+' '+str(A[1]+q2)+' '+str(A[2]+q3)] + [str(B[0]+q1)+' '+str(B[1]+q2)+' '+str(B[2]+q3)]
  vertices += [str(A[0])+' '+str(A[1])+' '+str(A[2])] + [str(B[0])+' '+str(B[1])+' '+str(B[2])]

def cylinder2(A,B,r,k,RGB): # A - start point, B - end point, r - radius, k - detail, RGB - color
  global vertices, faces
  for i in range (1,k):
    faces += ['4 '+str(2*i-2+len(vertices))+' '+str(2*i+len(vertices))+' '+str(2*i+1+len(vertices))+
    ' '+str(2*i-1+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  faces += ['4 '+str(2*k-2+len(vertices))+' '+str(0+len(vertices))+' '+str(1+len(vertices))+
  ' '+str(2*k-1+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  if A[0]==B[0] and A[1]==B[1]:
    p1=-math.sqrt(2)*r/2
    p2=(B[2]-A[2])/abs(B[2]-A[2])*p1
    p3=-p1
    p4=p2
    p5=0
  else:
    d=math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2)+math.pow(B[2]-A[2],2))
    f=math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2))
    p1=-r*(B[1]-A[1])/f
    p2=-r*(B[0]-A[0])*(B[2]-A[2])/(d*f)
    p3=r*(B[0]-A[0])/f
    p4=-r*(B[1]-A[1])*(B[2]-A[2])/(d*f)
    p5=r*f/d
  for i in range (1,k+1):
    sinn=math.sin(i/k*2*math.pi)
    coss=math.cos(i/k*2*math.pi)
    q1=coss*p1+sinn*p2
    q2=coss*p3+sinn*p4
    q3=sinn*p5
    vertices += [str(A[0]+q1)+' '+str(A[1]+q2)+' '+str(A[2]+q3)] + [str(B[0]+q1)+' '+str(B[1]+q2)+' '+str(B[2]+q3)]

def cylinder3(A,B,r,k,RGB): # A - start point, B - end point, r - radius, k - detail, RGB - color
  global vertices, faces
  for i in range (1,k):
    faces += ['4 '+str(2*i-2+len(vertices))+' '+str(2*i+len(vertices))+' '+str(2*i+1+len(vertices))+
    ' '+str(2*i-1+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
    faces += ['3 '+str(2*i+len(vertices))+' '+str(2*i-2+len(vertices))+' '+str(2*k+len(vertices))+
    ' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  faces += ['4 '+str(2*k-2+len(vertices))+' '+str(0+len(vertices))+' '+str(1+len(vertices))+
  ' '+str(2*k-1+len(vertices))+' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  faces += ['3 '+str(0+len(vertices))+' '+str(2*k-2+len(vertices))+' '+str(2*k+len(vertices))+
  ' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  if A[0]==B[0] and A[1]==B[1]:
    p1=-math.sqrt(2)*r/2
    p2=(B[2]-A[2])/abs(B[2]-A[2])*p1
    p3=-p1
    p4=p2
    p5=0
  else:
    d=math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2)+math.pow(B[2]-A[2],2))
    f=math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2))
    p1=-r*(B[1]-A[1])/f
    p2=-r*(B[0]-A[0])*(B[2]-A[2])/(d*f)
    p3=r*(B[0]-A[0])/f
    p4=-r*(B[1]-A[1])*(B[2]-A[2])/(d*f)
    p5=r*f/d
  for i in range (1,k+1):
    sinn=math.sin(i/k*2*math.pi)
    coss=math.cos(i/k*2*math.pi)
    q1=coss*p1+sinn*p2
    q2=coss*p3+sinn*p4
    q3=sinn*p5
    vertices += [str(A[0]+q1)+' '+str(A[1]+q2)+' '+str(A[2]+q3)] + [str(B[0]+q1)+' '+str(B[1]+q2)+' '+str(B[2]+q3)]
  vertices += [str(A[0])+' '+str(A[1])+' '+str(A[2])]

def cone(A,B,r,k,RGB): # A - start point, B - end point, r - radius, k - detail, RGB - color
  global vertices, faces
  for i in range (1,k):
    faces += ['3 '+str(i+len(vertices))+' '+str(i-1+len(vertices))+' '+str(k+len(vertices))+
    ' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
    faces += ['3 '+str(i-1+len(vertices))+' '+str(i+len(vertices))+' '+str(k+1+len(vertices))+
    ' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  faces += ['3 '+str(0+len(vertices))+' '+str(k-1+len(vertices))+' '+str(k+len(vertices))+
  ' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  faces += ['3 '+str(k-1+len(vertices))+' '+str(0+len(vertices))+' '+str(k+1+len(vertices))+
  ' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  if A[0]==B[0] and A[1]==B[1]:
    p1=-math.sqrt(2)*r/2
    p2=(B[2]-A[2])/abs(B[2]-A[2])*p1
    p3=-p1
    p4=p2
    p5=0
  else:
    d=math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2)+math.pow(B[2]-A[2],2))
    f=math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2))
    p1=-r*(B[1]-A[1])/f
    p2=-r*(B[0]-A[0])*(B[2]-A[2])/(d*f)
    p3=r*(B[0]-A[0])/f
    p4=-r*(B[1]-A[1])*(B[2]-A[2])/(d*f)
    p5=r*f/d
  for i in range (1,k+1):
    sinn=math.sin(i/k*2*math.pi)
    coss=math.cos(i/k*2*math.pi)
    q1=coss*p1+sinn*p2
    q2=coss*p3+sinn*p4
    q3=sinn*p5
    vertices += [str(A[0]+q1)+' '+str(A[1]+q2)+' '+str(A[2]+q3)]
  vertices += [str(A[0])+' '+str(A[1])+' '+str(A[2])] + [str(B[0])+' '+str(B[1])+' '+str(B[2])]

def cone2(A,B,r,k,RGB): # A - start point, B - end point, r - radius, k - detail, RGB - color
  global vertices, faces
  for i in range (1,k):
    faces += ['3 '+str(i-1+len(vertices))+' '+str(i+len(vertices))+' '+str(k+len(vertices))+
    ' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  faces += ['3 '+str(k-1+len(vertices))+' '+str(0+len(vertices))+' '+str(k+len(vertices))+
  ' '+str(RGB[0])+' '+str(RGB[1])+' '+str(RGB[2])]
  if A[0]==B[0] and A[1]==B[1]:
    p1=-math.sqrt(2)*r/2
    p2=(B[2]-A[2])/abs(B[2]-A[2])*p1
    p3=-p1
    p4=p2
    p5=0
  else:
    d=math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2)+math.pow(B[2]-A[2],2))
    f=math.sqrt(math.pow(B[0]-A[0],2)+math.pow(B[1]-A[1],2))
    p1=-r*(B[1]-A[1])/f
    p2=-r*(B[0]-A[0])*(B[2]-A[2])/(d*f)
    p3=r*(B[0]-A[0])/f
    p4=-r*(B[1]-A[1])*(B[2]-A[2])/(d*f)
    p5=r*f/d
  for i in range (1,k+1):
    sinn=math.sin(i/k*2*math.pi)
    coss=math.cos(i/k*2*math.pi)
    q1=coss*p1+sinn*p2
    q2=coss*p3+sinn*p4
    q3=sinn*p5
    vertices += [str(A[0]+q1)+' '+str(A[1]+q2)+' '+str(A[2]+q3)]
  vertices += [str(B[0])+' '+str(B[1])+' '+str(B[2])]

def clear():
  global vertices, faces
  vertices = []
  faces = []

def off(mesh): # mesh - off file
  global vertices, faces
  file = open(mesh, 'w')
  file.write('%s\n%d %d %d\n' % ('OFF',len(vertices),len(faces),0))
  for i in range (len(vertices)):
    file.write('%s\n' % vertices[i])
  for j in range (len(faces)):
    file.write('%s\n' % faces[j])
  file.close()
  clear()

def layer():
  global vertices, faces
  M = [vertices, faces]
  clear()
  return(M)

def center(M):
  N = []
  C = [0,0,0]
  T = [None for i in range(len(M[0]))]
  for i in range(len(M[0])):
    T[i] = [float(j) for j in M[0][i].split(' ',2)]
    C[0] += T[i][0]
    C[1] += T[i][1]
    C[2] += T[i][2]
  C[0] /= len(M[0])
  C[1] /= len(M[0])
  C[2] /= len(M[0])
  return(C)

def rotateX(M,angle,P):
  N = []
  for i in range(len(M[0])):
    T = [float(j) for j in M[0][i].split(' ',2)]
    y = P[1]+(T[1]-P[1])*math.cos(angle)-(T[2]-P[2])*math.sin(angle)
    z = P[2]+(T[1]-P[1])*math.sin(angle)+(T[2]-P[2])*math.cos(angle)
    N += [str(T[0]) + ' ' + str(y) + ' ' + str(z)]
  return([N,M[1]])

def rotateY(M,angle,P):
  N = []
  for i in range(len(M[0])):
    T = [float(j) for j in M[0][i].split(' ',2)]
    x = P[0]+(T[2]-P[2])*math.sin(angle)+(T[0]-P[0])*math.cos(angle)
    z = P[2]+(T[2]-P[2])*math.cos(angle)-(T[0]-P[0])*math.sin(angle)
    N += [str(x) + ' ' + str(T[1]) + ' ' + str(z)]
  return([N,M[1]])

def rotateZ(M,angle,P):
  N = []
  for i in range(len(M[0])):
    T = [float(j) for j in M[0][i].split(' ',2)]
    x = P[0]+(T[0]-P[0])*math.cos(angle)-(T[1]-P[1])*math.sin(angle)
    y = P[1]+(T[0]-P[0])*math.sin(angle)+(T[1]-P[1])*math.cos(angle)
    N += [str(x) + ' ' + str(y) + ' ' + str(T[2])]
  return([N,M[1]])

def move(M,V):
  N = []
  for i in range(len(M[0])):
    T = [float(j) for j in M[0][i].split(' ',2)]
    N += [str(T[0]+V[0]) + ' ' + str(T[1]+V[1]) + ' ' + str(T[2]+V[2])]
  return([N,M[1]])

def zoom(M,s):
  N = []
  C = [0,0,0]
  T = [None for i in range(len(M[0]))]
  for i in range(len(M[0])):
    T[i] = [float(j) for j in M[0][i].split(' ',2)]
    C[0] += T[i][0]
    C[1] += T[i][1]
    C[2] += T[i][2]
  C[0] /= len(M[0])
  C[1] /= len(M[0])
  C[2] /= len(M[0])
  for i in range(len(M[0])):
    N += [str(C[0]+(T[i][0]-C[0])*s) + ' ' + str(C[1]+(T[i][1]-C[1])*s) + ' ' + str(C[2]+(T[i][2]-C[2])*s)]
  return([N,M[1]])

def stretch(M,s):
  N = []
  C = [0,0,0]
  T = [None for i in range(len(M[0]))]
  for i in range(len(M[0])):
    T[i] = [float(j) for j in M[0][i].split(' ',2)]
    C[0] += T[i][0]
    C[1] += T[i][1]
    C[2] += T[i][2]
  C[0] /= len(M[0])
  C[1] /= len(M[0])
  C[2] /= len(M[0])
  for i in range(len(M[0])):
    N += [str(C[0]+(T[i][0]-C[0])*s[0]) + ' ' + str(C[1]+(T[i][1]-C[1])*s[1]) + ' ' + str(C[2]+(T[i][2]-C[2])*s[2])]
  return([N,M[1]])

def merge(M):
  V = []
  F = []
  k = 0
  for i in range(len(M)):
    for N in M[i][1]:
      n = int(N.split(' ',1)[0])
      f = N.split(' ',n + 1)
      f2 = ''
      for j in range(1, n + 1):
        f2 += str(int(f[j]) + k) + ' '
      F += [str(n) + ' ' + f2 + f[n+1]]
    V += M[i][0]
    k += len(M[i][0])
  return([V,F])

def load(mesh):
  V = []
  F = []
  RGB = ''
  f = open(mesh, 'r')
  f.readline()
  A = [int(num) for num in f.readline().split(' ')]
  for i in range(A[0]):
    S = [float(num) for num in f.readline().split(' ')]
    V += [str(S[0]) + ' ' + str(S[1]) + ' ' + str(S[2])]
  S = [int(num) for num in f.readline().split(' ')]
  if S[0] == len(S) - 1:
    RGB = ' 100 100 100' # default color
  f2 = str(S[0])
  for k in range(1, len(S)):
    f2 += ' ' + str(S[k])
  F += [f2 + RGB]
  for j in range(A[1]-1):
    S = [int(num) for num in f.readline().split(' ')] 
    f2 = str(S[0])
    for k in range(1, len(S)):
      f2 += ' ' + str(S[k])
    F += [f2 + RGB]
  f.close()
  return([V,F])

def mesh(M):
  global vertices, faces
  for F in M[1]:
    n = int(F.split(' ',1)[0])
    f = F.split(' ',n + 1)
    f2 = ''
    for j in range(1, n + 1):
      f2 += str(int(f[j]) + len(vertices)) + ' '
    faces += [str(n) + ' ' + f2 + f[n+1]]
  vertices += M[0]

def color(M,RGB):
  F = []
  s = str(RGB[0]) + ' ' + str(RGB[1]) + ' ' + str(RGB[2])
  for i in range(len(M[1])):
    S = [int(j) for j in M[1][i].split(' ')]
    f2 = ''
    for j in range(1,S[0]+1):
      f2 += str(S[j]) + ' '
    F += [str(S[0]) + ' ' + f2 + s]
  return(M[0],F)

def axes(C):
  h = 4 # height
  w = 0.03 # width
  cylinder(C,[C[0]+h,C[1],C[2]],w,9,[255,0,0])
  cylinder(C,[C[0],C[1]+h,C[2]],w,9,[0,255,0])
  cylinder(C,[C[0],C[1],C[2]+h],w,9,[0,0,255])
  cone([C[0]+h,C[1],C[2]],[C[0]+h+0.7,C[1],C[2]],2*w,9,[255,0,0])
  cone([C[0],C[1]+h,C[2]],[C[0],C[1]+h+0.7,C[2]],2*w,9,[0,255,0])
  cone([C[0],C[1],C[2]+h],[C[0],C[1],C[2]+h+0.7],2*w,9,[0,0,255])
  X = [['4.2171572875253815 0.30000000000000004 0.1414213562373094', '4.287867965644036 0.30000000000000004 0.07071067811865488', '4.429289321881345 0.7 -0.07071067811865474', '4.570710678118655 0.30000000000000004 -0.21213203435596434', '4.641421356237309 0.30000000000000004 -0.28284271247461884', '4.5 0.8 -0.14142135623730923', '4.641421356237309 1.3 -0.28284271247461884', '4.570710678118655 1.3 -0.21213203435596434', '4.429289321881345 0.9000000000000001 -0.07071067811865474', '4.287867965644036 1.3 0.07071067811865488', '4.2171572875253815 1.3 0.1414213562373094', '4.358578643762691 0.8 -2.498001805406602e-16', '4.358578643762691 0.30000000000000004 0.28284271247461884', '4.429289321881345 0.30000000000000004 0.21213203435596434', '4.570710678118655 0.7 0.07071067811865474', '4.712132034355964 0.30000000000000004 -0.07071067811865488', '4.7828427124746185 0.30000000000000004 -0.1414213562373094', '4.641421356237309 0.8 2.498001805406602e-16', '4.7828427124746185 1.3 -0.1414213562373094', '4.712132034355964 1.3 -0.07071067811865488', '4.570710678118655 0.9000000000000001 0.07071067811865474', '4.429289321881345 1.3 0.21213203435596434', '4.358578643762691 1.3 0.28284271247461884', '4.5 0.8 0.14142135623730923'], ['4 2 1 0 11 255 0 0', '4 5 4 3 2 255 0 0', '4 5 2 11 8 255 0 0', '4 8 7 6 5 255 0 0', '4 11 10 9 8 255 0 0', '4 23 12 13 14 255 0 0', '4 14 15 16 17 255 0 0', '4 20 23 14 17 255 0 0', '4 17 18 19 20 255 0 0', '4 20 21 22 23 255 0 0', '4 0 1 13 12 255 0 0', '4 1 2 14 13 255 0 0', '4 2 3 15 14 255 0 0', '4 3 4 16 15 255 0 0', '4 4 5 17 16 255 0 0', '4 5 6 18 17 255 0 0', '4 6 7 19 18 255 0 0', '4 7 8 20 19 255 0 0', '4 8 9 21 20 255 0 0', '4 9 10 22 21 255 0 0', '4 10 11 23 22 255 0 0', '4 11 0 12 23 255 0 0']]
  Y = [['-0.30606601717798215 4.0777777777777775 0.26464466094067274', '-0.23535533905932732 4.0777777777777775 0.1939339828220179', '-0.23535533905932732 4.627777777777778 0.1939339828220179', '-0.058578643762690424 5.0777777777777775 0.017157287525381038', '-0.12928932188134526 5.0777777777777775 0.08786796564403587', '-0.27071067811865474 4.777777777777778 0.22928932188134532', '-0.41213203435596424 5.0777777777777775 0.37071067811865477', '-0.4828427124746191 5.0777777777777775 0.4414213562373096', '-0.30606601717798215 4.627777777777778 0.26464466094067274', '-0.16464466094067268 4.0777777777777775 0.4060660171779822', '-0.09393398282201784 4.0777777777777775 0.33535533905932735', '-0.09393398282201784 4.627777777777778 0.33535533905932735', '0.08284271247461905 5.0777777777777775 0.15857864376269049', '0.012132034355964216 5.0777777777777775 0.22928932188134532', '-0.12928932188134526 4.777777777777778 0.37071067811865477', '-0.27071067811865474 5.0777777777777775 0.5121320343559642', '-0.34142135623730957 5.0777777777777775 0.582842712474619', '-0.16464466094067268 4.627777777777778 0.4060660171779822'], ['5 8 5 2 1 0 0 255 0', '4 5 4 3 2 0 255 0', '4 8 7 6 5 0 255 0', '5 9 10 11 14 17 0 255 0', '4 11 12 13 14 0 255 0', '4 14 15 16 17 0 255 0', '4 0 1 10 9 0 255 0', '4 1 2 11 10 0 255 0', '4 2 3 12 11 0 255 0', '4 3 4 13 12 0 255 0', '4 4 5 14 13 0 255 0', '4 5 6 15 14 0 255 0', '4 6 7 16 15 0 255 0', '4 7 8 17 16 0 255 0', '4 8 0 9 17 0 255 0']]
  Z = [['-0.38284271247461954 0.30000000000000004 4.54142135623731', '0.04142135623730911 0.30000000000000004 4.11715728752538', '0.04142135623730911 0.5000000000000002 4.11715728752538', '-0.24142135623731004 0.5000000000000002 4.3999999999999995', '0.04142135623730911 1.0999999999999999 4.11715728752538', '0.04142135623730911 1.3 4.11715728752538', '-0.38284271247461954 1.3 4.54142135623731', '-0.38284271247461954 1.0999999999999999 4.54142135623731', '-0.10000000000000038 1.0999999999999999 4.25857864376269', '-0.38284271247461954 0.5000000000000002 4.54142135623731', '-0.24142135623730993 0.30000000000000004 4.682842712474619', '0.1828427124746187 0.30000000000000004 4.258578643762691', '0.1828427124746187 0.5000000000000002 4.258578643762691', '-0.10000000000000042 0.5000000000000002 4.54142135623731', '0.1828427124746187 1.0999999999999999 4.258578643762691', '0.1828427124746187 1.3 4.258578643762691', '-0.24142135623730993 1.3 4.682842712474619', '-0.24142135623730993 1.0999999999999999 4.682842712474619', '0.04142135623730922 1.0999999999999999 4.4', '-0.24142135623730993 0.5000000000000002 4.682842712474619'], ['4 0 3 2 1 0 0 255', '6 0 9 8 5 4 3 0 0 255', '4 8 7 6 5 0 0 255', '4 11 12 13 10 0 0 255', '6 13 14 15 18 19 10 0 0 255', '4 15 16 17 18 0 0 255', '4 0 1 11 10 0 0 255', '4 1 2 12 11 0 0 255', '4 2 3 13 12 0 0 255', '4 3 4 14 13 0 0 255', '4 4 5 15 14 0 0 255', '4 5 6 16 15 0 0 255', '4 6 7 17 16 0 0 255', '4 7 8 18 17 0 0 255', '4 8 9 19 18 0 0 255', '4 9 0 10 19 0 0 255']]
  mesh(merge([move(X,C),move(Y,C),move(Z,C)]))

# EXAMPLES:

def example1():
  m = 10
  for k in range (m):
    for i in range (m-k):
      for j in range (m-k):
        if i == 0 or i == m-k-1 or j == 0 or j == m-k-1:
          cube([i+k/2,k/2,j+k/2],0.8,[random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)])
          if k != 0:
            cube([i+k/2,-k/2,j+k/2],0.8,[random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)])
  off('example1.off')

def example2():
  m = 10
  for k in range (m):
    for i in range (m-k):
      for j in range (m-k):
        if i == 0 or i == m-k-1 or j == 0 or j == m-k-1:
          cube2([i+k/2,k/2,j+k/2],0.8,0.1,[random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)])
          if k != 0:
            cube2([i+k/2,-k/2,j+k/2],0.8,0.1,[random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)])
  off('example2.off')

def example3():
  a = 5
  b = 1
  def toras1(u,v):
    x = (a+b*math.cos(u))*math.cos(v)
    y = b*math.sin(u)
    z = (a+b*math.cos(u))*math.sin(v)
    return ([x, y, z])
  def toras2(u,v):
    x = (a+b*math.cos(u))*math.cos(v)
    y = -(a+b*math.cos(u))*math.sin(v)
    z = b*math.sin(u)
    return ([x, y, z])
  def toras3(u,v):
    x = b*math.sin(u)
    y = -(a+b*math.cos(u))*math.cos(v)
    z = (a+b*math.cos(u))*math.sin(v)
    return ([x, y, z])
  parametric(toras1,0,2*math.pi,50,0,2*math.pi,200,[0,255,0])
  parametric(toras2,0,2*math.pi,50,0,2*math.pi,200,[255,0,0])
  parametric(toras3,0,2*math.pi,50,0,2*math.pi,200,[0,0,255])
  off('example3.off')

def example4():
  a = 36
  b = 0.85
  c = 1
  h = 15
  r = 0.15
  s = 0.5
  def sakos(u,v):
    x = math.sqrt(u)*math.cos(u)*v
    y = h-h/a*u
    z = math.sqrt(u)*math.sin(u)*v
    return ([x, y, z])
  def virsune(u,v):
    w = (3/2)*math.sqrt(3)
    x = c*math.sqrt(1-u*u)*(1-u)/w*math.cos(v)
    y = h+c*u+c
    z = c*math.sqrt(1-u*u)*(1-u)/w*math.sin(v)
    return ([x, y, z])
  def vamzdis(u,v):
    x = math.sqrt(b)*math.cos(a*b)*(-s*u+u*math.sqrt(a)+s)+r*math.cos(v)*math.sin(a*b)
    y = -r*math.sin(v)-b*h+h
    z = math.sqrt(b)*math.sin(a*b)*(-s*u+u*math.sqrt(a)+s)-r*math.cos(v)*math.cos(a*b)
    return ([x, y, z])
  def papuosimai(u,v):
    x = math.sqrt(u)*math.cos(u)-r*(math.cos(v)*(2*u*math.cos(u)+math.sin(u))/math.sqrt(4*u*u+1)-2*h*r*math.sqrt(u)*math.sin(v)*(2*u*math.sin(u)-math.cos(u))/math.sqrt((4*a*a*u*u+4*h*h*u+a*a)*(4*u*u+1)))
    y = h*(a-u)/a+a*r*math.sin(v)*math.sqrt(4*u*u+1)/math.sqrt(4*a*a*u*u+4*h*h*u+a*a)
    z = math.sqrt(u)*math.sin(u)-r*(math.cos(v)*(2*u*math.sin(u)-math.cos(u))/math.sqrt(4*u*u+1)-2*r*math.sqrt(u)*math.sin(v)*(2*u*math.cos(u)+math.sin(u))*h/math.sqrt((4*a*a*u*u+4*h*h*u+a*a)*(4*u*u+1)))
    return ([x, y, z])
  def stiebas(u,v):
    x = s*math.cos(u)*math.sqrt(v/h)
    y = h-v
    z = s*math.sin(u)*math.sqrt(v/h)
    return ([x, y, z])
  def dugnas(u,v):
    x = u*math.cos(v)
    y = 0
    z = u*math.sin(v)
    return ([x, y, z])
  def sfera1(u,v):
    x = r*math.cos(u)*math.sin(v)
    y = r*math.cos(v)+h
    z = r*math.sin(u)*math.sin(v)
    return ([x, y, z])
  def sfera2(u,v):
    x = math.sqrt(a*b)*math.cos(a*b)-r*math.cos(u)*math.sin(v)
    y = h*(1-b)+r*math.cos(v)
    z = math.sqrt(a*b)*math.sin(a*b)-r*math.sin(u)*math.sin(v)
    return ([x, y, z])
  parametric(sakos,0,a*b,500,0.98*s/math.sqrt(a),1,15,[0,255,0])
  parametric(virsune,-1,1,50,0,2*math.pi,40,[255,0,0])
  parametric(vamzdis,-0.01,1,5,0,2*math.pi,20,[255,255,255])
  parametric(papuosimai,0,a*b,500,0,2*math.pi,20,[255,255,255])
  parametric(stiebas,0,2*math.pi,20,0,h,100,[139,69,19])
  parametric(dugnas,0,s,1,0,2*math.pi,20,[139,69,19])
  parametric(sfera1,0,2*math.pi,30,0,math.pi,30,[255,255,255])
  parametric(sfera2,0,2*math.pi,30,0,math.pi,30,[255,255,255])
  off('example4.off')

def example5():
  m = 7
  for i in range (m):
    for j in range (m-i):
      for k in range (m-i-j):
        sphere([i*math.sqrt(3)/2+(k-1)*math.sqrt(3)/6,k*math.sqrt(2/3),j+0.5*(i-1)+(k-1)/2],0.5,10,[random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)])
  off('example5.off')

def example6():
  V = [[-0.262865,0,0.425325],[0.262865,0,0.425325],[-0.262865,0,-0.425325],[0.262865,0,-0.425325],
  [0,0.425325,0.262865],[0,0.425325,-0.262865],[0,-0.425325,0.262865],[0,-0.425325,-0.262865],
  [0.425325,0.262865,0],[-0.425325,0.262865,0],[0.425325,-0.262865,0],[-0.425325,-0.262865,0]]
  E = [[0,1],[0,4],[0,6],[0,9],[0,11],[1,4],[1,6],[1,8],[1,10],[2,3],[2,5],[2,7],[2,9],[2,11],[3,5],
  [3,7],[3,8],[3,10],[4,5],[4,8],[4,9],[5,8],[5,9],[6,7],[6,10],[6,11],[7,10],[7,11],[8,10],[9,11]]
  for v in V:
    sphere(v,0.06,10,[0,255,0])
  for e in E:
    cylinder2(V[e[0]],V[e[1]],0.02,15,[0,0,255])
  off('example6.off')

def example7():
  V = [[-1.411334,3.199887,0],[-.705666,3.199887,1.222252],[.705666,3.199887,1.222252],[1.411334,3.199887,0],
  [.705666,3.199887,-1.22225],[-.705666,3.199887,-1.22225],[-2.55312,2.385067,-.155618],[-2.98926,1.570227,.911012],
  [-2.28358,1.570227,2.133254],[-1.141792,2.385067,2.288874],[-1.411334,2.385067,-2.133266],[-2.55312,1.881465,-1.474048],
  [-.705666,1.570228,-3.044266],[1.411334,2.385067,-2.133266],[.705666,1.570228,-3.044266],[-1.141792,.251797,-3.296066],
  [-2.28358,-.251797,-2.636866],[-2.98926,.563037,-1.725844],[0,-.563034,-3.451686],[0,-1.881465,-2.948087],
  [-1.141792,-2.385053,-2.288887],[-2.28358,-1.570225,-2.133266],[1.141792,.251797,-3.296066],[2.28358,-.251797,-2.636866],
  [2.28358,-1.570225,-2.133266],[1.141792,-2.385053,-2.288887],[2.55312,1.881465,-1.474048],[2.98926,.563037,-1.725844],
  [2.55312,2.385067,-.155618],[2.98926,1.570227,.911012],[3.42538,.251797,.659216],[3.42538,-.251797,-.659214],
  [1.141792,2.385067,2.288874],[2.28358,1.570227,2.133254],[0,1.881464,2.948094],[-2.28358,.251797,2.636854],
  [-1.141792,-.251798,3.296074],[0,.563036,3.451694],[-3.42538,.251797,.659216],[-2.98926,-.563035,1.725846],
  [-3.42538,-.251797,-.659214],[-2.98926,-1.570225,-.91101],[-2.55312,-2.385053,.15562],[-2.55312,-1.881465,1.474048],
  [-.705666,-3.199893,-1.222251],[-1.411334,-3.199893,0],[.705666,-3.199893,-1.222251],[2.98926,-1.570225,-.91101],
  [2.55312,-2.385053,.15562],[1.411334,-3.199893,0],[2.98926,-.563035,1.725846],[2.55312,-1.881465,1.474048],
  [2.28358,.251797,2.636854],[1.141792,-.251798,3.296074],[.705666,-1.570226,3.044274],[1.411334,-2.385053,2.133253],
  [-.705666,-1.570226,3.044274],[-1.411334,-2.385053,2.133253],[-.705666,-3.199893,1.222251],[.705666,-3.199893,1.222251]]
  E = [[0,1],[0,5],[0,6],[1,2],[1,9],[2,3],[2,32],[3,4],[3,28],[4,5],[4,13],[5,10],[6,7],[6,11],[7,8],[7,38],[8,9],
  [8,35],[9,34],[10,11],[10,12],[11,17],[12,14],[12,15],[13,14],[13,26],[14,22],[15,16],[15,18],[16,17],[16,21],[17,40],
  [18,19],[18,22],[19,20],[19,25],[20,21],[20,44],[21,41],[22,23],[23,24],[23,27],[24,25],[24,47],[25,46],[26,27],[26,28],
  [27,31],[28,29],[29,30],[29,33],[30,31],[30,50],[31,47],[32,33],[32,34],[33,52],[34,37],[35,36],[35,39],[36,37],[36,56],
  [37,53],[38,39],[38,40],[39,43],[40,41],[41,42],[42,43],[42,45],[43,57],[44,45],[44,46],[45,58],[46,49],[47,48],[48,49],
  [48,51],[49,59],[50,51],[50,52],[51,55],[52,53],[53,54],[54,55],[54,56],[55,59],[56,57],[57,58],[58,59]]
  for v in V:
    sphere(v,0.2,10,[0,255,0])
  for e in E:
    cylinder2(V[e[0]],V[e[1]],0.08,15,[0,0,255])
  off('example7.off')

def example8():
  V = [[-1.411334,3.199887,0],[-.705666,3.199887,1.222252],[.705666,3.199887,1.222252],[1.411334,3.199887,0],
  [.705666,3.199887,-1.22225],[-.705666,3.199887,-1.22225],[-2.55312,2.385067,-.155618],[-2.98926,1.570227,.911012],
  [-2.28358,1.570227,2.133254],[-1.141792,2.385067,2.288874],[-1.411334,2.385067,-2.133266],[-2.55312,1.881465,-1.474048],
  [-.705666,1.570228,-3.044266],[1.411334,2.385067,-2.133266],[.705666,1.570228,-3.044266],[-1.141792,.251797,-3.296066],
  [-2.28358,-.251797,-2.636866],[-2.98926,.563037,-1.725844],[0,-.563034,-3.451686],[0,-1.881465,-2.948087],
  [-1.141792,-2.385053,-2.288887],[-2.28358,-1.570225,-2.133266],[1.141792,.251797,-3.296066],[2.28358,-.251797,-2.636866],
  [2.28358,-1.570225,-2.133266],[1.141792,-2.385053,-2.288887],[2.55312,1.881465,-1.474048],[2.98926,.563037,-1.725844],
  [2.55312,2.385067,-.155618],[2.98926,1.570227,.911012],[3.42538,.251797,.659216],[3.42538,-.251797,-.659214],
  [1.141792,2.385067,2.288874],[2.28358,1.570227,2.133254],[0,1.881464,2.948094],[-2.28358,.251797,2.636854],
  [-1.141792,-.251798,3.296074],[0,.563036,3.451694],[-3.42538,.251797,.659216],[-2.98926,-.563035,1.725846],
  [-3.42538,-.251797,-.659214],[-2.98926,-1.570225,-.91101],[-2.55312,-2.385053,.15562],[-2.55312,-1.881465,1.474048],
  [-.705666,-3.199893,-1.222251],[-1.411334,-3.199893,0],[.705666,-3.199893,-1.222251],[2.98926,-1.570225,-.91101],
  [2.55312,-2.385053,.15562],[1.411334,-3.199893,0],[2.98926,-.563035,1.725846],[2.55312,-1.881465,1.474048],
  [2.28358,.251797,2.636854],[1.141792,-.251798,3.296074],[.705666,-1.570226,3.044274],[1.411334,-2.385053,2.133253],
  [-.705666,-1.570226,3.044274],[-1.411334,-2.385053,2.133253],[-.705666,-3.199893,1.222251],[.705666,-3.199893,1.222251]]
  sphere([0,0,0],1.5,15,[0,0,255])
  for v in V:
    cylinder2([0,0,0],v,0.2,15,[255,255,0])
    cone(v,[1.3*v[0],1.3*v[1],1.3*v[2]],0.5,15,[255,0,0])
  off('example8.off')