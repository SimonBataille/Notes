import matplotlib.pyplot as plt
import numpy as np


'''
x = np.arange(-10.0, 10.0, 0.01)

# ~ carre = np.vectorize(lambda s: s*s)
# ~ y = carre(x)

y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

# ~ ax.set(xlabel='x', ylabel='x^2', title='Parabole')
ax.set(xlabel='x', ylabel='sin(x)', title='Sinus')
ax.grid()

plt.show()
'''
'''
fig, ax = plt.subplots()
types = ["Essence", "Diesel", "Hybride", "Electrique", "Autres"]
counts = [46, 30, 12, 5, 7]

ax.set_title("Répartition parc automobile")
ax.pie(counts, labels=types, shadow=True)
ax.axis('equal')

plt.show()
'''


x = np.arange(0,10)
y = np.arange(0, 10)

# ~ # basic 
# ~ plt.plot(x,y)

# ~ # object oriented
# ~ fig = plt.figure()
# ~ ax = plt.gca()
# ~ ax.plot(x,y)

# subplot style 1
# ~ fig, [[ax0, ax1],[ax2, ax3]] = plt.subplots(nrows=2, ncols=2)
# ~ ax0.text(0.5, 0.5, "This is axes object 0", ha='center')
# ~ ax1.text(0.5, 0.5, "This is axes object 1", ha='center')
# ~ ax2.text(0.5, 0.5, "This is axes object 2", ha='center')
# ~ ax3.text(0.5, 0.5, "This is axes object 3", ha='center')

# ~ # subplot style 2
# ~ fig, axes = plt.subplots(nrows=2, ncols=2)
# ~ axes[0,0].text(0.5, 0.5, "This is axes object 0", ha='center')
# ~ axes[0,1].text(0.5, 0.5, "This is axes object 1", ha='center')
# ~ axes[1,0].text(0.5, 0.5, "This is axes object 2", ha='center')
# ~ axes[1,1].text(0.5, 0.5, "This is axes object 3", ha='center')

# ~ # subplot style 3
# ~ fig = plt.figure()
# ~ ax0 =fig.add_subplot(221)
# ~ ax0.text(0.5, 0.5, "This is axes object 0", ha='center')
# ~ ax1 =fig.add_subplot(222)
# ~ ax1.text(0.5, 0.5, "This is axes object 1", ha='center')
# ~ ax2 =fig.add_subplot(223)
# ~ ax2.text(0.5, 0.5, "This is axes object 2", ha='center')
# ~ ax3 =fig.add_subplot(224)
# ~ ax3.text(0.5, 0.5, "This is axes object 3", ha='center')

# ~ # room to subplots
# ~ fig, [[ax0, ax1],[ax2, ax3]] = plt.subplots(nrows=2, ncols=2)
# ~ ax0.text(0.5, 0.5, "This is axes object 0", ha='center')
# ~ ax0.set_title('Title 0')
# ~ ax0.set_xlabel('X-axis')
# ~ ax0.set_ylabel('Y-axis')
# ~ ax1.text(0.5, 0.5, "This is axes object 1", ha='center')
# ~ ax1.set_title('Title 1')
# ~ ax1.set_xlabel('X-axis')
# ~ ax1.set_ylabel('Y-axis')
# ~ ax2.text(0.5, 0.5, "This is axes object 2", ha='center')
# ~ ax2.set_title('Title 2')
# ~ ax2.set_xlabel('X-axis')
# ~ ax2.set_ylabel('Y-axis')
# ~ ax3.text(0.5, 0.5, "This is axes object 3", ha='center')
# ~ ax3.set_title('Title 3')
# ~ ax3.set_xlabel('X-axis')
# ~ ax3.set_ylabel('Y-axis')
# ~ plt.tight_layout()
# ~ plt.savefig('tight_layout.png')


# fancy subplots
fig = plt.figure(figsize=(8,6))
gspec = fig.add_gridspec(nrows=2, ncols=3)
 
# the first subplot will span one row and two columns
# it will start at the top left
ax0 = fig.add_subplot(gspec[0,:2])
ax0.text(0.5, 0.5, "This is axes object 0, \ngspec coordinates [0,:2]", ha='center')
 
# the second subplot will span one row and one column
# it will start at the bottom left
ax1 = fig.add_subplot(gspec[1,0])
ax1.text(0.5, 0.5, "This is axes object 1, \ngspec coordinates [1,0]", ha='center')
 
# the third subplot will span one row and one column
# it will start at the bottom middle
ax2 = fig.add_subplot(gspec[1,1])
ax2.text(0.5, 0.5, "This is axes object 2, \ngspec coordinates [1,1]", ha='center')
 
# the fourth subplot will span two rows and one column
# it will start at the top right
ax3 = fig.add_subplot(gspec[:,2])
ax3.text(0.5, 0.5, "This is axes object 3, \ngspec coordinates [:,2]", ha='center')
 
plt.tight_layout()

plt.show()
