
import matplotlib.pyplot as plt
import numpy as np



# start = -10
# end = 10
# value_1 = list()
# value_2 = list()
# value_3 = list()
# value_4 = list()
# for i in range(-10, 11):
#     value_1.append(i**5)
#     value_2.append(i**100)
#     value_3.append((2*(i**2) + 4*i -5)**3) 
#     value_4.append((i**2 +2)**(5/4))


# fig, axs = plt.subplots(4)

# axs[0].plot(list(range(start,end+1)) , value_1)
# axs[0].set_title("A")

# axs[1].plot(list(range(start,end+1)) , value_2)
# axs[1].set_title("B")

# axs[2].plot(list(range(start,end+1)) , value_3)
# axs[2].set_title("C")

# axs[3].plot(list(range(start,end+1)) , value_4)
# axs[3].set_title("D")

# plt.tight_layout()
# plt.show()





# #radiant plot
# x = np.linspace(0,2* np.pi,400)
# f1= 1+ np.sin(2*x)+np.cos(x)+np.sin(x)
# f2= 2*np.cos(x)+3*np.sin(x)
# f3= 2*np.sin(x)*np.cos(x)+2*(np.cos(x)+np.sin(x))


# fig, axs = plt.subplots(3)

# axs[0].plot(x,f1)

# axs[1].plot(x,f2)

# axs[2].plot(x,f3)

# plt.tight_layout()
# plt.show()



x1 = np.arange(-5,6)
x2 = np.arange(-5,6)
x3 = np.arange(-5,6)
x4 = np.arange(-5,6)


A1 = np.array([[2, 1,-2], [3, 2,-4],[5,4,-1]])
b1 = np.array([8,15,1])

solution1 = np.linalg.solve(A1, b1)

print(solution1)


f1 = 2*x1 +x2 -2*x3
f2 = 3*x1 + 2*x2 -4*x3
f3 = 5*x1 +4*x2-x3

plt.plot3()




