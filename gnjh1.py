import random
from DBUtils import *

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

# 输入数字
def innum(s):
    temp = input('请输入%s'%s)
    while notnum(temp):
        print('输入不合法，请重新输入')
        temp = input('请输入%s'%s)
    return int(temp)


def whatbank(account):
    sql = 'select 开户行 from user1 where 账号 = %s'
    if len(select(sql,account)) == 0:
        return 0
    elif select(sql,account)[0][0] == '中国工商银行昌平支行':
        return '1'
    elif select(sql,account)[0][0] == '中国农业银行的昌平沙河支行':
        return '2'
    else:
        return 3

# 打印账号信息
def printuser(account):
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
开户时间 : %s
开户行名称 : %s'''
    sql = 'select * from user1 where 账号 = %s'
    data = select(sql, account)
    print(data)
    print(info1 % (data[0][2],
                   data[0][0]))
    if whatbank(account) == 2:
        print('账户类型 : %s'%data[0][1])
    print(info2 % (data[0][3],data[0][4],data[0][5],data[0][6],
                   data[0][7],data[0][8],data[0][9],data[0][10]))

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
    zhanghao = str(random.randint(0, 99999999)).zfill(8)
    print('您的账号为', zhanghao)
    usertype = ''
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
    bank_name = '中国工商银行昌平支行' if banktype == '1' else '中国农业银行的昌平沙河支行'
    sql = 'insert into user1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    param = [zhanghao,usertype,xingming,mima,guojia,shengfen,jiedao,menpai,money,'2021-11-18',bank_name]
    status = adduser(sql,param)
    if status == 3:
        print("银行库已经满了！请携带证件到其他银行办理！")
    elif status == 2:
        print("不允许重复开户！")
    elif status == 1:
        print("恭喜，开户成功！")
        printuser(zhanghao)
    return

# 添加用户
def adduser(sql,param):
    sql1 = 'select * from user1 where 开户行 = %s'
    print(param)
    if len(select(sql1,param[10])) >= 100:
        print('用户数量到达上限，添加用户失败')
        return 3
    sql2 = 'select * from user1 where 姓名 = %s and 开户行 = %s'
    if len(select(sql2,[param[2],param[10]])) != 0:
        print('用户已存在')
        return 2
    update(sql,param)
    return 1

# 存款
def save_money(banktype):
    account= input('请输入账号')
    money = innum('存款金额')
    status = savemoney(banktype,account,money)
    if status:
        print("存款成功")
        printuser(account)
    else:
        print('没有该用户，存款失败')
    return

# 添加存款
def savemoney(banktype,account,money):
    sql = 'select * from user1 where 账号 = %s'
    data = select(sql,account,'all')
    if whatbank(account) != banktype:
        return False
    else:
        sql1 = 'update user1 set 存款余额 = %s where 账号 = %s'
        update(sql1,[data[0][8]+money,account])
        return True

# 取款
def with_draw(banktype):
    account = input('请输入账号')
    mima = innum('密码')
    money = innum('取钱金额')
    status = withdraw(banktype,account,mima,money)
    if status == 1:
        print('没有该账户，取钱失败')
    elif status == 2:
        print('密码错误，取钱失败')
    elif status == 3:
        print('余额不足，取钱失败')
    elif status == 0:
        print('取钱成功')
        printuser(account)
    return

# 执行取款
def withdraw(banktype,account,mima,money):
    sql = 'select * from user1 where 账号 = %s'
    data = select(sql, account, 'all')
    if whatbank(account) != banktype:
        return 1
    elif data[0][3] != mima:
        return 2
    elif data[0][8] < money:
        return 3
    else:
        sql1 = 'update user1 set 存款余额 = %s where 账号 = %s'
        update(sql1,[data[0][8]-money,account])
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
    status = transfer(dict)
    if status == 1:
        print('没有该账户，转账失败')
    elif status == 2:
        print('密码错误，转账失败')
    elif status == 3:
        print('余额不足，转账失败')
    elif status == 0:
        print('转账成功')
        printuser(dict['账号1'])
        printuser(dict['账号2'])
    return

# 计算手续费
def trancharge(dict):
    banktype1 = whatbank(dict['账号1'])
    banktype2 = whatbank(dict['账号2'])
    sql = 'select * from user1 where 账号 = %s'
    data1 = select(sql, dict['账号1'], 'all')
    data2 = select(sql, dict['账号2'], 'all')
    sql1 = 'update user1 set 存款余额 = %s where 账号 = %s'
    sql2 = 'update user1 set 存款余额 = %s where 账号 = %s'
    if banktype1 == banktype2:
        charge = 0
    elif dict['转账金额'] <= 2000:
        charge = 1.6
    elif dict['转账金额'] <= 5000 and dict['转账金额'] > 2000:
        charge = 4
    elif dict['转账金额'] <= 10000 and dict['转账金额'] > 5000:
        charge = 8
    elif dict['转账金额'] <= 50000 and dict['转账金额'] > 10000:
        charge = 12
    elif dict['转账金额'] > 50000:
        charge = 50 if dict['转账金额'] * 0.0003 > 50 else dict['转账金额'] * 0.0003
    update(sql1, [data1[0][8] - dict['转账金额'], dict['账号1']])
    data3 = select(sql, dict['账号2'], 'all')
    update(sql2, [data3[0][8] + dict['转账金额'] - charge, dict['账号2']])
    return 0

# 执行转账
def transfer(banktype,dict):
    sql = 'select * from user1 where 账号 = %s'
    data1 = select(sql,dict['账号1'],'all')
    data2 = select(sql,dict['账号2'],'all')
    type1 = whatbank(dict['账号1'])
    type2 = whatbank(dict['账号2'])
    if type1 != banktype or len(data2) < 1:
        return 1
    elif data1[0][3] != dict['密码1'] or data2[0][3] != dict['密码2']:
        return 2
    elif data1[0][8] < dict['转账金额']:
        return 3
    if type1 != type2 and data1[0][8] < 1.6:
        return 3
    if type1 == 1:
        trancharge(dict)
        return 0
    if type1 == 2:
        if data1[0][1] == 1:
            if dict['转账金额'] > 50000:
                return 3
            else:
                trancharge(dict)
                return 0
        elif data1[0][1] == 2:
            if dict['转账金额'] > 20000:
                return 3
            else:
                trancharge(dict)
                return 0

# 查询
def Query(banktype):
    account = input('请输入账号')
    mima = innum('密码')
    query(banktype,account,mima)
    return

# 执行查询
def query(banktype,account,mima):
    sql = 'select * from user1 where 账号 = %s'
    data = select(sql, account, 'all')
    if whatbank(account) != banktype:
        print('该用户不存在')
        return
    elif data[0][3] != mima:
        print('密码不正确')
        return
    else:
        printuser(account)
        return

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