from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
file = "e:\\test.csv"
df = pd.read_csv(file)
X = df.loc[:, df.columns != 'label']
y = df.loc[:, df.columns == 'label'].values.ravel()
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X,y,test_size=0.3,random_state=90)
rfc = RandomForestClassifier(random_state=0)
rfc = rfc.fit(Xtrain,Ytrain)
score_r = rfc.score(Xtest,Ytest)
print("Random Forest:{}".format(score_r) )

h = rfc.predict(X_test)
np.savetxt("d:\\result2.txt", h)

def para1():
    # 调参，绘制学习曲线来调参n_estimators（对随机森林影响最大）
    score_lt = []
    for i in range(390,410,1):
        rfc = RandomForestClassifier(n_estimators=i+1
                                    ,random_state=90,n_jobs=4)
        score = cross_val_score(rfc, X, y, cv=10).mean()
        print(i)
        score_lt.append(score)
    score_max = max(score_lt)
    print('最大得分：{}'.format(score_max),
          '子树数量为：{}'.format(score_lt.index(score_max)*10+1))
    # 绘制学习曲线
    x = np.arange(390,410,1)
    plt.subplot(211)
    plt.plot(x, score_lt, 'r-')
    plt.show()
    
def para2():
    # 用网格搜索调整max_depth
    param_grid = {'max_depth':np.arange(10,50)}
    GS = GridSearchCV(rfc, param_grid, cv=10)
    GS.fit(X, y)
    best_param = GS.best_params_
    best_score = GS.best_score_
    print(best_param, best_score)