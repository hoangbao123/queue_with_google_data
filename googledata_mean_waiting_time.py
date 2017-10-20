import matplotlib.pyplot as plt

theta = [2.5E-4, 5.0E-4, 7.5E-4, 0.001, 0.00125, 0.0015, 0.00175, 0.002, 0.00225, 0.0025, 0.00275, 0.003]
mean_waitting_time_nomiddle_hostnum_500_queuecapacity_500 = [86.40872419266348, 83.74202126646135, 81.46927718136614, 79.41261105601559, 77.44570610704021, 75.65480456391901, 74.20546364875426, 72.80556921049242, 71.37566445368259, 70.06870656318637, 68.75819061650037, 67.72179636855678]
mean_waitting_time_hostnum_500_queuecapacity_500= [75.68821445611907, 68.09706592780464, 63.538069534177176, 59.027150379551266, 55.842559984282914, 53.0879448463402, 50.692615679342026, 48.518626362556155, 46.910439616272846, 45.49401753360742, 44.043675695034786, 42.697925719242996]
plt.plot(theta,mean_waitting_time_hostnum_500_queuecapacity_500,marker="o",label="With Middle")
plt.plot(theta,mean_waitting_time_nomiddle_hostnum_500_queuecapacity_500,marker="x",label="Without Middle")
plt.ylabel("Mean Waiting Time (s)")
plt.xlabel("Abandonment rate ($\\theta$)")
plt.axis([0.00022,0.0031,0,100])
plt.grid(b='on')
plt.legend(loc='best')
plt.show()