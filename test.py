import numpy as np


while(True):
    global X, Y, V
    x = input("请输入'and','or','not', 'xor'\n")
    if x == 'and':
        V = np.random.random((3, 4)) * 2 - 1
        print(x)
        y = input("请输入x1 x2\n")
        a, b = map(int, y.split())
        # 输入数据
        X = np.array([[1, a, b]])
        if a == 0 or b == 0:
            # 标签
            Y = np.array([[0]])
            break
        elif a == 1 and b == 1:
            Y = np.array([[1]])
            break
    elif x == 'or':
        V = np.random.random((3, 4)) * 2 - 1
        print(x)
        y = input("请输入x1 x2\n")
        a, b = map(int, y.split())
        X = np.array([[1, a, b]])
        if a == 0 and b == 0:
            Y = np.array([[0]])
            break
        elif a == 1 or b == 1:
            Y = np.array([[1]])
            break
    elif x == 'not':
        V = np.random.random((2, 4)) * 2 - 1
        print(x)
        y = int(input("请输入x\n"))
        a = y
        print(a)
        X = np.array([[1, a]])
        if a == 1:
            Y = np.array([[0]])
            break
        elif a == 0:
            Y = np.array([[1]])
            break
    elif x == 'xor':
        V = np.random.random((3, 4)) * 2 - 1
        print(x)
        y = input("请输入x1 x2\n")
        a, b = map(int, y.split())
        X = np.array([[1, a, b]])
        if a == b:
            Y = np.array([[0]])
            break
        elif a != b:
            Y = np.array([[1]])
            break
    else:
        print('请重新输入')
# 权值初始化，取值范围-1到1 ，第一层权值V 第二层权值W

W = np.random.random((4, 1))*2-1
# 学习率设置
alpha = 0.11


def sigmoid(x):
    return 1/(1+np.exp(-x))


def dsigmoid(x):
    return x*(1-x)


def update():
    global X, Y, W, V, alpha
    L1 = sigmoid(np.dot(X, V))  # 隐藏层输出（1，4）
    L2 = sigmoid(np.dot(L1, W))  # 输出层输出（4，1）
    L2_delta = (Y.T - L2) * dsigmoid(L2)
    L1_delta = L2_delta.dot(W.T)*dsigmoid(L1)
    W_change = alpha * L1.T.dot(L2_delta)
    V_change = alpha * X.T.dot(L1_delta)
    W = W + W_change
    V = V + V_change


for i in range(20000):
    update()
    if i%500 ==0:
        L1 = sigmoid(np.dot(X, V))  # 隐藏层输出（1，4）
        L2 = sigmoid(np.dot(L1, W))  # 输出层输出（4，1）
        #print('Error:', np.mean(np.abs(Y.T-L2)))
L1 = sigmoid(np.dot(X, V))  # 隐藏层输出（1，4）
L2 = sigmoid(np.dot(L1, W))  # 输出层输出（4，1）
print(L2)


def judge(l_2):
    if l_2 > 0.5:
        return 1
    else:
        return 0


for i in map(judge, L2):
    print("输入值", y, "运算符", x, "输出结果:", i)
