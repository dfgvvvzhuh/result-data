import matplotlib.pyplot as plt

#1、设置数据
x = ['30 Mbits','60 Mbits','100Mbits','1000Mbits']
y_1 = [33,71,129,354]  # cer-maddpg
y_2 = [36,89,152,398]  # maddpg
y_3 = [34,75,142,386]  # sgra-per
#2、创建画布
fig,ax1 = plt.subplots(1, 1)
ax1.spines['top'].set_visible(False)                   # 不显示图表框的上边框
ax1.spines['right'].set_visible(False)
#3、绘制柱状图
x_ticks = range(len(x))
ax1.tick_params(bottom=False)
plt.bar([i-0.2 for i in x_ticks],y_1,width=0.2,label='CER-MADDPG',color='red')
plt.bar([i for i in x_ticks],y_2,width=0.2,label='MADDPG',color='green')
plt.bar([i+0.2 for i in x_ticks],y_3,width=0.2,label='SGRA-PERs',color='blue')

plt.plot([i-0.2 for i in x_ticks], y_1, color="red")
plt.plot([i for i in x_ticks], y_2, color="green")
plt.plot([i+0.2 for i in x_ticks], y_3, color="blue")

plt.legend()
#4、修改X刻度
plt.xticks(x_ticks,x)

plt.xlabel('Initial mission size of UAV')
plt.ylabel('Average task completion time of UAVs')
plt.show()