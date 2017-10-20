import matplotlib.pyplot as plt

theta = [2.5E-4, 5.0E-4, 7.5E-4, 0.001, 0.00125, 0.0015, 0.00175, 0.002, 0.00225, 0.0025, 0.00275, 0.003]
#mean_waitting_time_nomiddle_hostnum_500_queuecapacity_500 = [86.40872419266348, 83.74202126646135, 81.46927718136614, 79.41261105601559, 77.44570610704021, 75.65480456391901, 74.20546364875426, 72.80556921049242, 71.37566445368259, 70.06870656318637, 68.75819061650037, 67.72179636855678]
#mean_waitting_time_hostnum_500_queuecapacity_500= [75.68821445611907, 68.09706592780464, 63.538069534177176, 59.027150379551266, 55.842559984282914, 53.0879448463402, 50.692615679342026, 48.518626362556155, 46.910439616272846, 45.49401753360742, 44.043675695034786, 42.697925719242996]

job_left_ratio_withmiddle_hostnum_500_queuecapacity_500  = [0.018959371368926878, 0.034777556767827955, 0.04822458987336786, 0.0597317683203025, 0.06981507375386493, 0.08038088110758808, 0.0887508123756819, 0.09819209484609173, 0.10616617760009453, 0.1136636666207141, 0.12122417630029345, 0.12854638911318117]
job_left_ratio_nomiddle_hostnum_500_queuecapacity_500  = [0.021401421903617778, 0.04136124623353093, 0.05990889593931122, 0.0779329223861197, 0.0950627252496209, 0.11162731157807669, 0.12724461862654352, 0.14254091419343404, 0.15748468794926837, 0.17087854737381097, 0.18443783602812297, 0.1969415286448589]
plt.plot(theta,job_left_ratio_withmiddle_hostnum_500_queuecapacity_500,marker="o",label="With Middle")
plt.plot(theta,job_left_ratio_nomiddle_hostnum_500_queuecapacity_500,marker="x",label="Without Middle")
plt.axis([0,0.0031,0,0.2])
plt.ylabel("Proportion Of Left Job(%)")
plt.xlabel("Abandonment rate ($\\theta$)")
plt.grid(b='on')
plt.legend(loc='best')
plt.show()