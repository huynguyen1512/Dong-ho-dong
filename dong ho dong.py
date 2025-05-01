import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
fig,ax=plt.subplots(figsize=(8,5))
'''Ve duong tron'''
t=np.linspace(0,2*np.pi,1000)
x=np.cos(t)
y=np.sin(t)
plt.plot(x,y,color='black',linewidth=4)
'''Danh so gio'''
for hour in range(1, 13):
    angle = np.pi/6*hour  
    hx = 0.85 * np.sin(angle)
    hy= 0.85 * np.cos(angle)
    ax.text(hx, hy, str(hour), ha='center', va='center', fontsize=14, weight='bold')
'''Ve kim dong ho ban dau'''
gio,=ax.plot([0,0],[0,0.4],color='black',linewidth=3)
phut,=ax.plot([0,0],[0,0.6],color='black',linewidth=3)
giay,=ax.plot([0,0],[0,0.75],color='red',linewidth=2)
def init(): '''ham khoi tao'''
    gio.set_data([],[])
    phut.set_data([],[])
    giay.set_data([],[])
    return gio,phut,giay
def update(fr): '''ham cap nhat'''
    a=fr*0.1
    hrx=np.array([0,0.4*np.sin(2*np.pi/43200 *a)])
    hry=np.array([0,0.4*np.cos(2*np.pi/43200 *a)])
    minx=np.array([0,0.6*np.sin(2*np.pi/3600*a)])
    miny=np.array([0,0.6*np.cos(2*np.pi/3600*a)])
    secx=np.array([0,0.75*np.sin(2*np.pi/60*a)])
    secy=np.array([0,0.75*np.cos(2*np.pi/60*a)])
    gio.set_data(hrx,hry)
    phut.set_data(minx,miny)
    giay.set_data(secx,secy)
    return gio,phut,giay
ani=animation.FuncAnimation(fig,update,frames=10000,init_func=init,interval=50,blit=True)
ax.axis('off')
plt.axis('equal')
plt.show()