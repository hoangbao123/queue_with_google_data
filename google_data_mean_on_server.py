import matplotlib.pyplot as plt



plt.plot(theta,mean_number_of,marker="o",label="With Middle")
plt.plot(theta,mean_number_of_on_server_no_middle,marker="x",label="No Middle")
plt.ylabel("Mean Number of On Server (s)")
plt.xlabel("Theta")
plt.grid(b='on')
plt.legend(loc='best')
plt.show()
