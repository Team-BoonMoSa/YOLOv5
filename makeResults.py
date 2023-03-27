import pandas as pd
import matplotlib.pyplot as plt


def makeResults(res, idx='val/box_loss', figname='', fontsize=20, fontfamily='Times New Roman'):
    plt.rcParams['font.size'] = fontsize
    plt.rcParams['font.family'] = fontfamily
    colors = {'YOLOv5n': 'red', 'YOLOv5s': 'olive', 'YOLOv5m': 'black', 'YOLOv5l': 'blue', 'YOLOv5x': 'indigo'}
    fig = plt.figure(figsize=(15, 10))
    plt.grid(True)
    for i in res['models']:
        plt.plot(res[i].loc[:, 'epoch'], res[i].loc[:, idx], color=colors[i], linewidth=3, label=i)
    plt.xlabel('Epoch')
    plt.ylabel(idx)
    plt.legend()
    if figname != '':
        print("Saving...")
        plt.savefig('./Results/' + figname.replace('/', '-') + '.png', dpi=300, bbox_inches='tight', pad_inches=0.3, transparent=False)

if __name__ == "__main__":
    model = 'YOLOv5'
    s = ['n', 's', 'm', 'l', 'x']
    res = {'models': []}
    col = {}
    flag = False
    for i in s:
        try:
            tmp = pd.read_csv(model + i + '.csv')
        except:
            continue
        if not flag:
            for j in tmp.columns:
                col[j] = j.replace(' ', '')
            flag = True
        res[model + i] = tmp.rename(columns = col).iloc[:-1, :]
        res['models'].append(model + i)
    print(res.keys())
    for i in col.values():
        if i != 'epoch':
            makeResults(res, i, i)