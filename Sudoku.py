#!/usr/bin/env python
# coding: utf-8

# In[81]:


#在下面输入数独题目，需要填数字的地方用0表示
a = [[0, 0, 0, 0, 9, 8, 0, 0, 1],
     [0, 0, 4, 0, 0, 0, 0, 2, 0],
     [0, 0, 1, 7, 0, 0, 6, 5, 0],
     [0, 0, 5, 0, 0, 0, 0, 3, 4],
     [0, 0, 9, 6, 3, 5, 7, 0, 0],
     [7, 3, 0, 0, 0, 0, 5, 0, 0],
     [0, 4, 7, 0, 0, 3, 9, 0, 0],
     [0, 1, 0, 0, 0, 0, 2, 0, 0],
     [9, 0, 0, 4, 8, 0, 0, 0, 0]]

def need_what(ty, i):#need_what函数表示这一行或者这一列缺哪些元素;ty表示行还是列；i表示第i个
    b = [False] * 9 #b用来标记哪些数字已经用过
    ans = [] #ans用来记录哪些数字还没使用过
    loc = [] #loc用来记录哪些位置还是空着的
    if ty == 0:#ty=0表示对行进行判断
        for j in range(9):
            if a[i][j] != 0: #搜索本行中不为0的元素即此处已经有数字,且该数字已经被使用，0表示此处空着还没填
                b[a[i][j] - 1] = True
            else:
                loc.append(j)
        for j in range(9):
            if b[j] == False:
                ans.append(j + 1)

    if ty == 1:#ty=1表示对列进行判断
        for j in range(9):
            if a[j][i] != 0:
                b[a[j][i] - 1] = True
            else:
                loc.append(j)
        for j in range(9):
            if b[j] == False:
                ans.append(j + 1)
    return ans, loc

def need_what_nine(i): #need_what_nine函数表示第i个小九宫格缺哪些元素，之所以与need_what函数分开是因为小九宫格内未填位置的坐标需要用x，y来表示，因为返回值有3个，而need_what函数返回值只有两个
    b = [False] * 9 #b用来标记哪些数字已经用过
    ans = [] #ans用来记录哪些数字还没使用过
    loc_x = [] #loc_x用来记录哪些位置还是空着的（x坐标）
    loc_y = [] #loc_y用来记录哪些位置还是空着的（y坐标）
    x_min = (i % 3) * 3  #x_min,x_max,y_min,y_max用来表示此小九宫格的坐标范围
    x_max = (i % 3 + 1) * 3
    y_min = (i // 3) * 3
    y_max = (i // 3 + 1) * 3
    for j in range(x_min, x_max):
        for k in range(y_min, y_max):
            if a[j][k] != 0:
                 b[a[j][k]-1] =True
            else:
                loc_x.append(j)
                loc_y.append(k)
        for j in range(9):
            if b[j] ==False:
                ans.append(j + 1)
    return ans, loc_x, loc_y

def check(x, y, num):#判断（x, y）这个位置是否可以填数字num
    for i in range(9): #先判断这一行内和这一列内是否有重复
        if a[x][i] == num or a[i][y] == num:
            return False
    #接下来判断小九宫格内是否有重复元素,x_min和x_max分别用来表示对应小九宫格的横坐标范围；y表示纵坐标范围
    x_min = (x // 3) * 3
    x_max = (x // 3 + 1) * 3
    y_min = (y // 3) *3
    y_max = (y // 3 + 1) *3
    for i in range(x_min, x_max):
        for j in range(y_min, y_max):
            if a[i][j] == num:
                return False
    return True

def done(): #done函数用来判断数独是否已经做完？
    for i in range(9):
        for j in range(9):
            if a[i][j] == 0:
                return False
    return True

steps = 0 #step用来记录第几步数独填数字的操作
while done() != True:
#while steps<=50:
    #首先对每一行试着填数字
    for i in range(9):
        b, loc = need_what(0, i)  #b为这一行还没有填的数字；loc为空缺的位置
        for j in b:
            counts = 0
            for k in loc:
                if check(i, k, j) == True:
                    counts += 1
                    loc_in = k #loc_in表示填入数字的位置
            if counts == 1:
                a[i][loc_in] = j
                steps = steps + 1 
                print("第{0}步：在({1}, {2})位置填入数字{3}".format(steps, i + 1, loc_in + 1, j))
   
    #接下来对每一列试着填数字
    for i in range(9):
        b, loc = need_what(1, i) #b为这一列还没有填的数字；loc为空缺的位置
        for j in b:
            counts = 0
            for k in loc:
                if check(k, i, j) == True:
                    counts += 1
                    loc_in = k #loc_in表示填入数字的位置
            if counts == 1:
                a[loc_in][i] = j
                steps += 1 
                print("第{0}步：在({1}, {2})位置填入数字{3}".format(steps, loc_in + 1, i + 1, j))
     
    #最后对每一个小九宫格进行填数字
    for i in range(9):
        b, loc_x, loc_y = need_what_nine(i)
        for j in b:
            counts = 0
            for k in range(len(loc_x)):
                if check(loc_x[k], loc_y[k], j) == True:
                    counts += 1
                    loc_in_x = loc_x[k] #loc_in_x表示填入数字位置的x坐标
                    loc_in_y = loc_y[k] #loc_in_y表示填入数字位置的y坐标
            if counts ==1:
                a[loc_in_x][loc_in_y] = j
                steps += 1
                print("第{0}步：在({1}, {2})位置填入数字{3}".format(steps, loc_in_x + 1, loc_in_y + 1, j))
                
for i in range(9):
    print(a[i])


# In[79]:


done()

