import matplotlib.pyplot as plt
# import pandas as pd
#
# # 做平滑处理，我觉得应该可以理解为减弱毛刺，，吧  能够更好地看数据走向
# def tensorboard_smoothing(x ,smooth=0.99):
#     x = x.copy()
#     weight = smooth
#     for i in range(1 ,len(x)):
#         x[i] = (x[ i -1] * weight + x[i]) / (weight + 1)
#         weight = (weight + 1) * smooth
#     return x
#
# if __name__ == '__main__':
#
#     fig, ax1 = plt.subplots(1, 1)    # a figure with a 1x1 grid of Axes
#
#     # 设置上方和右方无框
#     ax1.spines['top'].set_visible(False)                   # 不显示图表框的上边框
#     ax1.spines['right'].set_visible(False)
#
#     # len_mean = pd.read_csv \
#     #     ("2/run-.-tag-maddpg-two-buffer_test6.csv")
#     # len_mean1 =pd.read_csv \
#     #     ("1/run-.-tag-maddpg-two-buffer_test9.csv")
#     # len_mean3 = pd.read_csv \
#     #     ("3/run-.-tag-maddpg-two-buffer_test13.csv")
#
#     # 设置折线颜色，折线标签
#     # 使用平滑处理
#     ax1.plot(len_mean['Step'], tensorboard_smoothing(len_mean['Value'], smooth=0.6), color="red" ,label='alpha1=0.5,alpha2=0.5')
#     ax1.plot(len_mean1['Step'], tensorboard_smoothing(len_mean1['Value'], smooth=0.6), color="blue", label='alpha1=0.9,alpha2=0.5')
#     ax1.plot(len_mean3['Step'], tensorboard_smoothing(len_mean3['Value'], smooth=0.6), color="black", label='alpha1=0.5,alpha2=0.9')
#
#
#     # 不使用平滑处理
#     # ax1.plot(len_mean['Step'], len_mean['Value'], color="red",label='all_data')
#
#     # s设置标签位置，lower upper left right，上下和左右组合
#     plt.legend(loc = 'lower right')
#
#
#     ax1.set_xlabel("epoch")
#     ax1.set_ylabel("reward")
#     # ax1.set_title("actor and critic learning rate")
#     plt.show()
#     # 保存图片，也可以是其他格式，如pdf
#     fig.savefig(fname='./a2 ' +'.png', format='png')
#1、设置数据
x = ['2','3','5','10','20']
y_1 = [232,373,635,1278,2554]
y_2 = [282,453,772,1570,3250]
y_3 = [257,413,703,1419,2847]
#2、创建画布
fig,ax1 = plt.subplots(1, 1)
ax1.spines['top'].set_visible(False)  # 不显示图表框的上边框
ax1.spines['right'].set_visible(False)
#3、绘制柱状图
x_ticks = range(len(x))
ax1.tick_params(bottom=False)
plt.bar([i-0.2 for i in x_ticks],y_1,width=0.2,label='CER-MADDPG',color='red')
plt.bar([i for i in x_ticks],y_2,width=0.2,label='MADDPG',color='green')
plt.bar([i+0.2 for i in x_ticks],y_3,width=0.2,label='SGRA-PERs',color='blue')

# plt.plot(x_ticks, y_1, color="red")
# plt.plot([i+0.2 for i in x_ticks], y_2, color="blue")

plt.legend()
#4、修改X刻度
plt.xticks(x_ticks,x)

plt.xlabel('Number of UAVs')
plt.ylabel('System overhead')
plt.show()