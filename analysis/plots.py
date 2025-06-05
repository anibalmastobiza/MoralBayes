import matplotlib.pyplot as plt
import numpy as np

def raincloud(df, factors, value):
    cats = df.groupby(factors)[value]
    pos = np.arange(len(cats))
    plt.figure()
    for i,(label,series) in enumerate(cats):
        plt.violinplot(series, positions=[pos[i]], widths=0.8, showextrema=False)
        plt.boxplot(series, positions=[pos[i]], widths=0.2, showfliers=False)
        plt.scatter(np.random.normal(pos[i],0.04,len(series)), series, s=8, alpha=0.6)
    plt.xticks(pos, [",").join(map(str,l)) for l,_ in cats.items()])
    plt.ylabel(value)
    plt.tight_layout()
