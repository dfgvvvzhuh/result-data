import matplotlib.pyplot as plt
import pandas as pd

def tensorboard_smoothing(x ,smooth=0.99):
    x = x.copy()
    weight = smooth
    for i in range(1 ,len(x)):
        x[i] = (x[ i -1] * weight + x[i]) / (weight + 1)
        weight = (weight + 1) * smooth
    return x

if __name__ == '__main__':

    fig, ax1 = plt.subplots(1, 1)

    ax1.spines['top'].set_visible(False)                   
    ax1.spines['right'].set_visible(False)

    len_mean = pd.read_csv \
        ("cermaddpg/run-.-tag-maddpg-two-buffer_test6.csv")
    len_mean1 =pd.read_csv \
        ("maddpg/run-.-tag-maddpg_test11.csv")
    len_mean3 = pd.read_csv \
        ("sgra_per/run-.-tag-SGRA_PER_test5.csv")

    ax1.plot(len_mean['Step'], tensorboard_smoothing(-len_mean['Value'], smooth=0.6), color="red" ,label='CER-MADDPG')
    ax1.plot(len_mean1['Step'], tensorboard_smoothing(-len_mean1['Value'], smooth=0.6), color="green", label='MADDPG')
    ax1.plot(len_mean3['Step'], tensorboard_smoothing(-len_mean3['Value'], smooth=0.6), color="blue", label='SGRA-PERs')
    plt.legend(loc = 'upper right')


    ax1.set_xlabel("Episodes")
    ax1.set_ylabel("System overhead")
    plt.show()
    fig.savefig(fname='./a2 ' +'.png', format='png')
