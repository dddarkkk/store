import random

bank = {'1':{},'2':{}}

# 判断输入是否为大于0的整数
def notnum(num):
    try:
        num = int(num)
        if num >= 0:
            return False
        else:
            return True
    except ValueError:
        return True

# 取字典键值
def numkey(dict):
    return ''.join(dict.keys())

# 输入数字
def innum(s):
    temp = input('请输入%s'%s)
    while notnum(temp):
        print('输入不合法，请重新输入')
        temp = input('请输入%s'%s)
    return int(temp)

# 判断账号在哪个银行
def whatbank(user):
    if user in bank['1'].keys():
        return '1'
    elif user in bank['2'].keys():
        return '2'
    else:
        return 0

# 打印账号信息
def printuser(banktype,user):
    info1 = '''------------个人信息------------
用户名 : %s
账号 : %s'''
    info2 = '''取款密码 : %s
地址信息 :
国籍 : %s
省份 : %s
街道 : %s
门牌号 : %s
余额 : %s
开户行名称 : %s'''
    print(info1 % (bank[banktype][user]['姓名'],
                  user))
    if banktype == '2':
        print('账户类型 : %s'%bank[banktype][user]['账户类型'])
    print(info2 % (
        bank[banktype][user]['密码'],
        bank[banktype][user]['国家'],
        bank[banktype][user]['省份'],
        bank[banktype][user]['街道'],
        bank[banktype][user]['门牌号'],
        bank[banktype][user]['存款余额'],
        bank[banktype][user]['开户行'])
          )

# 界面
def jiemian(banktype):
    msg_info = '''\033[1;31;5m
    ******************************************************************************************************
                                今日银行消息：
                            【今日银行转账手续费通知：】
                            1.转账2000元以下。    异地同行或跨行转账手续费是ATM转账是1.6元/笔.
                            2.转账2000-5000元。   异地同行或跨行转账手续费是ATM转账是4元/笔.
                            3.转账5000-10000元。  异地同行或跨行转账手续费是ATM转账是8元/笔
                            4.转账10000-50000元。 异地同行或跨行转账手续费是ATM转账是12元/笔。
                            5.转账50000元以上。   异地同行或跨行转账手续费是ATM转账金额的0.03%，最高50元。
    ******************************************************************************************************
    \033[0m
    '''
    print(msg_info)
    print(' ' * 36,'*' * 28)
    if banktype == '1':
        print(' ' * 36,'*', ' ' * 6, '中国工商银行', ' ' * 6, '*')
        print(' ' * 36,'*', ' ' * 6, '账户管理系统', ' ' * 6, '*')
        print(' ' * 36,'*', ' ' * 9, 'v1.0', ' ' * 9, '*')
        print(' ' * 36,'*' * 28)
        print()
    else:
        print(' ' * 36,'*', ' ' * 1, '中国农业银行账户管理系统', ' ' * 1, '*')
        print(' ' * 36,'*' * 28)
        print(' ' * 36,'*', ' ' * 9, '选项', ' ' * 10, '*')
    print(' ' * 36,'*', '1.开户', ' ' * 18, '*')
    print(' ' * 36,'*', '2.存钱', ' ' * 18, '*')
    print(' ' * 36,'*', '3.取钱', ' ' * 18, '*')
    print(' ' * 36,'*', '4.转账', ' ' * 18, '*')
    print(' ' * 36,'*', '5.查询', ' ' * 18, '*')
    print(' ' * 36,'*', '6.再见', ' ' * 18, '*')
    print(' ' * 36,'*' * 28)


# 开户
def add_users(banktype):
    inusers1 = {}
    zhanghao = str(random.randint(0, 99999999)).zfill(8)
    print('您的账号为', zhanghao)
    if banktype == '2':
        while 1:
            usertype = input('请选择账户类型[1:金卡，2：普通会员卡]')
            if usertype == '1' or usertype == '2':
                break
    xingming = input('请输入姓名')
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
    guojia = input('请输入国籍')
    shengfen = input('请输入省份')
    jiedao = input('请输入街道')
    menpai = input('请输入门牌号')
    money = innum('预存金额')
    if banktype == '1':
        inusers1[zhanghao] = {'姓名': xingming, '密码': mima, '国家': guojia, '省份': shengfen,
                              '街道': jiedao, '门牌号': menpai, '存款余额': money, '开户行': '中国工商银行昌平支行'}
    else:
        inusers1[zhanghao] = {'账户类型': usertype, '姓名': xingming, '密码': mima, '国家': guojia, '省份': shengfen,
                          '街道': jiedao, '门牌号': menpai, '存款余额': money, '开户行': '中国农业银行的昌平沙河支行'}
    status = adduser(banktype,inusers1)
    if status == 3:
        print("银行库已经满了！请携带证件到其他银行办理！")
    elif status == 2:
        print("不允许重复开户！")
    elif status == 1:
        print("恭喜，开户成功！")
        printuser(banktype,zhanghao)
    return

# 添加用户
def adduser(banktype,dict):
    if len(bank[banktype]) >= 100:
        print('用户数量到达上限，添加用户失败')
        return 3
    for i in bank[banktype].values():
        if dict[numkey(dict)]['姓名'] in i['姓名']:
            print('用户已存在')
            return 2
    bank[banktype].update(dict)
    return 1

# 换行输出字典
def printdict(dict):
    for i in dict:
        print('{%s:%s}'%(i,dict[i]))

# 存款
def save_money(banktype):
    dict = {}
    dict['账号'] = input('请输入账号')
    money = innum('存款金额')
    dict['存款金额'] = money
    status = savemoney(banktype,dict)
    if status:
        print("存款成功")
        printuser(banktype,dict['账号'])
    else:
        print('没有该用户，存款失败')
    return

# 添加存款
def savemoney(banktype,dict):
    if dict['账号'] not in bank[banktype].keys():
        return False
    else:
        bank[banktype][dict['账号']]['存款余额'] += dict['存款金额']
        return True

# 取款
def with_draw(banktype):
    dict = {}
    dict['账号'] = input('请输入账号')
    mima = innum('密码')
    dict['密码'] = mima
    money = innum('取钱金额')
    dict['取钱金额'] = money
    status = withdraw(banktype,dict)
    if status == 1:
        print('没有该账户，取钱失败')
    elif status == 2:
        print('密码错误，取钱失败')
    elif status == 3:
        print('余额不足，取钱失败')
    elif status == 0:
        print('取钱成功')
        printuser(banktype,dict['账号'])
    return

# 执行取款
def withdraw(banktype,dict):
    if dict['账号'] not in bank[banktype].keys():
        return 1
    elif dict['密码'] != bank[banktype][dict['账号']]['密码']:
        return 2
    elif dict['取钱金额'] > bank[banktype][dict['账号']]['存款余额']:
        return 3
    else:
        bank[banktype][dict['账号']]['存款余额'] -= dict['取钱金额']
        return 0

# 转账
def Transfer(banktype):
    dict = {}
    dict['账号1'] = input('请输入转出的账号')
    mima1 = innum('转出账号密码')
    dict['密码1'] = mima1
    money = innum('转账金额')
    dict['转账金额'] = money
    dict['账号2'] = input('请输入转入的账号')
    mima2 = innum('转入账号密码')
    dict['密码2'] = mima2
    status = transfer(banktype,dict)
    if status == 1:
        print('没有该账户，转账失败')
    elif status == 2:
        print('密码错误，转账失败')
    elif status == 3:
        print('余额不足，转账失败')
    elif status == 0:
        print('转账成功')
        printuser(banktype,dict['账号1'])
        printuser(whatbank(dict['账号2']),dict['账号2'])
    return

# 计算手续费
def trancharge(banktype1,banktype2,dict):
    if banktype1 == banktype2:
        bank[banktype1][dict['账号1']]['存款余额'] -= dict['转账金额']
        bank[banktype2][dict['账号2']]['存款余额'] += dict['转账金额']
    elif dict['转账金额'] <= 2000:
        bank[banktype1][dict['账号1']]['存款余额'] -= dict['转账金额']
        bank[banktype2][dict['账号2']]['存款余额'] += dict['转账金额'] - 1.6
    elif dict['转账金额'] <= 5000 and dict['转账金额'] > 2000:
        bank[banktype1][dict['账号1']]['存款余额'] -= dict['转账金额']
        bank[banktype2][dict['账号2']]['存款余额'] += dict['转账金额'] - 4
    elif dict['转账金额'] <= 10000 and dict['转账金额'] > 5000:
        bank[banktype1][dict['账号1']]['存款余额'] -= dict['转账金额']
        bank[banktype2][dict['账号2']]['存款余额'] += dict['转账金额'] - 8
    elif dict['转账金额'] <= 50000 and dict['转账金额'] > 10000:
        bank[banktype1][dict['账号1']]['存款余额'] -= dict['转账金额']
        bank[banktype2][dict['账号2']]['存款余额'] += dict['转账金额'] - 12
    elif dict['转账金额'] > 50000:
        charge = 50 if dict['转账金额'] * 0.0003 > 50 else dict['转账金额'] * 0.0003
        bank[banktype1][dict['账号1']]['存款余额'] -= dict['转账金额']
        bank[banktype2][dict['账号2']]['存款余额'] += dict['转账金额'] - charge
    return 0

# 执行转账
def transfer(banktype,dict):
    if whatbank(dict['账号1']) == 0 or whatbank(dict['账号2']) == 0:
        return 1
    elif dict['密码1'] != bank[banktype][dict['账号1']]['密码'] or dict['密码2'] != bank[whatbank(dict['账号2'])][dict['账号2']]['密码']:
        return 2
    elif dict['转账金额'] > bank[banktype][dict['账号1']]['存款余额']:
        return 3
    elif bank[banktype][dict['账号1']]['存款余额'] < 1.6:
        return 3
    if banktype == '1':
        trancharge(banktype,whatbank(dict['账号2']),dict)
        return 0
    if banktype == '2':
        if bank[banktype][dict['账号1']]['账户类型'] == '1':
            if dict['转账金额'] > 50000:
                return 3
            else:
                trancharge(banktype,whatbank(dict['账号2']),dict)
                return 0
        elif bank[banktype][dict['账号1']]['账户类型'] == '2':
            if dict['转账金额'] > 20000:
                return 3
            else:
                trancharge(banktype,whatbank(dict['账号2']),dict)
                return 0

# 查询
def Query(banktype):
    dict = {}
    dict['账号'] = input('请输入账号')
    mima = innum('密码')
    dict['密码'] = mima
    query(banktype,dict)
    return

# 执行查询
def query(banktype,dict):
    if dict['账号'] not in bank[banktype].keys():
        print('该用户不存在')
        return
    elif dict['密码'] != bank[banktype][dict['账号']]['密码']:
        print('密码不正确')
        return
    else:
        printuser(banktype,dict['账号'])

def main(banktype):
    while 1:
        jiemian(banktype)
        num = input('请选择业务')
        if num == '1':
            add_users(banktype)
        elif num == '2':
            save_money(banktype)
        elif num == '3':
            with_draw(banktype)
        elif num == '4':
            Transfer(banktype)
        elif num == '5':
            Query(banktype)
        elif num == '6':
            print('*', ' ' * 6, '已退出此系统', ' ' * 6, '*')
            break
        else:
            print('输入不合法，请重新输入')

while 1:
    banktype = input('请选择您要操作的银行（1：工商银行，2：农业银行）,输入q/Q退出')
    if banktype == '1':
        main(banktype)
    elif banktype == '2':
        main(banktype)
    elif banktype == 'q' or banktype == 'Q':
        print('*', ' ' * 6, '欢迎下次使用', ' ' * 6, '*')
        exit()
    else:
        print('输入不合法，请重新输入')