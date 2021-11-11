import random

# 判断输入是否为数字
def notnum(num):
    try:
        num = int(num)
        return False
    except ValueError:
        return True

# 取字典键值
def numkey(dict):
    return ''.join(dict.keys())

def innum(s):
    temp = input('请输入%s'%s)
    while notnum(temp):
        print('输入不合法，请重新输入')
        temp = input('请输入%s'%s)
    return int(temp)

def jiemian():
    print('*'*28)
    print('*',' '*6,'中国工商银行',' '*6,'*')
    print('*',' '*6,'账户管理系统',' '*6,'*')
    print('*',' '*9,'v1.0',' '*9,'*')
    print('*'*28)
    print()
    print('*','1.开户',' '*18,'*')
    print('*','2.存钱',' '*18,'*')
    print('*','3.取钱',' '*18,'*')
    print('*','4.转账',' '*18,'*')
    print('*','5.查询',' '*18,'*')
    print('*','6.再见',' '*18,'*')
    print('*'*28)

# users = {'账号':
#              '',
#               { '姓名':''}, {'密码': ''}, {'地址': ''}, {'存款余额': ''}, {'开户行': ''}
#               ]
#          }
users = {}

def inusers():
    inusers1 = {}
    zhanghao = str(random.randint(0, 99999999)).zfill(8)
    print('您的账号为', zhanghao)
    xingming = input('请输入姓名')
    inusers1[zhanghao] = {'姓名': xingming}
    while 1:
        mima = input('请输入6位整数密码')
        if len(mima) == 6:
            if notnum(mima):
                print('密码输入不合法，请重新输入')
            else:
                break
        else:
            print('密码输入不合法，请重新输入')
    mima = int(mima)
            # try:
            #     mima = int(mima)
            #     break
            # except ValueError:
            #     print('密码输入不合法，请重新输入')
    inusers1[zhanghao].update({'密码': mima})
    guojia = input('请输入国家')
    inusers1[zhanghao]['地址'] = {'国家': guojia}
    shengfen = input('请输入省份')
    inusers1[zhanghao]['地址']['国家'] = {guojia: {'省份': shengfen}}
    jiedao = input('请输入街道')
    inusers1[zhanghao]['地址']['国家'][guojia]['省份'] = {shengfen: {'街道': jiedao}}
    menpai = input('请输入门牌号')
    inusers1[zhanghao]['地址']['国家'][guojia]['省份'][shengfen]['街道'] = {jiedao: {'门牌号': menpai}}
    inusers1[zhanghao].update({'存款余额': 0})
    inusers1[zhanghao].update({'开户行':'中国工商银行'})
    return inusers1

def adduser(dict):
    if len(users) == 100:
        print('用户数量到达上限，添加用户失败')
        return 3
    if numkey(dict) in users.keys():
        print('用户已存在')
        return 2
    users.update(dict)
    return 1

def printdict(dict):
    for i in dict:
        print('{%s:%s}'%(i,dict[i]))

def savemoney(dict):
    if dict['账号'] not in users.keys():
        return False
    else:
        users[dict['账号']]['存款余额'] += dict['存款金额']
        return True

def withdraw(dict):
    if dict['账号'] not in users.keys():
        return 1
    elif dict['密码'] != users[dict['账号']]['密码']:
        return 2
    elif dict['取钱金额'] > users[dict['账号']]['存款余额']:
        return 3
    else:
        users[dict['账号']]['存款余额'] -= dict['取钱金额']
        return 0

def transfer(dict):
    if dict['账号1'] not in users.keys() or dict['账号2'] not in users.keys():
        return 1
    elif dict['密码1'] != users[dict['账号1']]['密码'] or dict['密码2'] != users[dict['账号2']]['密码']:
        return 2
    elif dict['转账金额'] > users[dict['账号1']]['存款余额']:
        return 3
    else:
        users[dict['账号1']]['存款余额'] -= dict['转账金额']
        users[dict['账号2']]['存款余额'] += dict['转账金额']
        return 0

def query(dict):
    if dict['账号'] not in users.keys():
        print('该用户不存在')
        return
    elif dict['密码'] != users[dict['账号']]['密码']:
        print('密码不正确')
        return
    else:
        print('当前账号:',dict['账号'])
        printdict(users[dict['账号']])

while 1:
    jiemian()
    num = input('请选择业务')
    while notnum(num):
        print('输入不合法，请重新输入')
        num = input('请选择业务')
    num = int(num)
    if num == 1:
        print(adduser(inusers()))
        # printdict(users)
    elif num == 2:
        dict = {}
        dict['账号'] = input('请输入账号')
        money = innum('存款金额')
        dict['存款金额'] = money
        print(savemoney(dict))
    elif num == 3:
        dict = {}
        dict['账号'] = input('请输入账号')
        mima = innum('密码')
        dict['密码'] = mima
        money = innum('取钱金额')
        dict['取钱金额'] = money
        print(withdraw(dict))
    elif num == 4:
        dict = {}
        dict['账号1'] = input('请输入转出的账号')
        mima1 = innum('转出账号密码')
        dict['密码1'] = mima1
        money = innum('转账金额')
        dict['转账金额'] = money
        dict['账号2'] = input('请输入转入的账号')
        mima2 = innum('转入账号密码')
        dict['密码2'] = mima2
        print(transfer(dict))
    elif num == 5:
        dict = {}
        dict['账号'] = input('请输入账号')
        mima = innum('密码')
        dict['密码'] = mima
        query(dict)
    elif num == 6:
        print('已退出系统')
        exit()
    else:
        print('输入不合法，请重新输入')