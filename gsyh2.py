import random
import pymysql

host="localhost"
user="root"
# password="root"
database="bank"


# 针对增删改
def update(sql,param=''):
    con = pymysql.connect(host=host,user=user,database=database)
    cursor = con.cursor()
    cursor.execute(sql) if len(param) == 0 else cursor.execute(sql, param)
    con.commit()
    cursor.close()
    con.close()


# 查询
def select(sql,param='',mode="many",size=1):
    con = pymysql.connect(host=host, user=user,database=database)
    cursor = con.cursor()
    cursor.execute(sql) if len(param) == 0 else cursor.execute(sql, param)
    cursor.close()
    con.close()
    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)

# 判断输入是否为数字
def notnum(num):
    try:
        num = int(num)
        return False
    except ValueError:
        return True

# 输入数字
def innum(s):
    temp = input('请输入%s'%s)
    while notnum(temp):
        print('输入不合法，请重新输入')
        temp = input('请输入%s'%s)
    return int(temp)

# 打印账号信息
def printuser(account):
    info = '''
------------个人信息------------
用户名 : %s
账号 : %s
取款密码 : %s
地址信息 :
国籍 : %s
省份 : %s
街道 : %s
门牌号 : %s
余额 : %s
开户日期 : %s
开户行名称 : %s
    '''
    sql = 'select * from user where 账号 = %s'
    data = select(sql,account)
    print(info % (data[0][1],data[0][0],data[0][2],data[0][3],data[0][4],
                  data[0][5],data[0][6],data[0][7],data[0][8],data[0][9])
          )

# 界面
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

# 开户
def add_users():
    inusers1 = {}
    zhanghao = str(random.randint(0, 99999999)).zfill(8)
    print('您的账号为', zhanghao)
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
    sql = 'insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    param = [zhanghao,xingming,mima,guojia,shengfen,jiedao,menpai,money,'2021-11-18','中国工商银行昌平支行']
    status = adduser(sql,param)
    if status == 3:
        print("银行库已经满了！请携带证件到其他银行办理！")
    elif status == 2:
        print("不允许重复开户！")
    elif status  == 1:
        print("恭喜，开户成功！")
        printuser(zhanghao)
    return

# 添加用户
def adduser(sql,param):
    if len(select('select * from user')) >= 100:
        print('用户数量到达上限，添加用户失败')
        return 3
    sql2 = 'select * from user where 姓名 = %s'
    if len(select(sql2,param[1])) != 0:
        print('用户已存在')
        return 2
    update(sql,param)
    return 1

# 存款
def save_money():
    account = input('请输入账号')
    money = innum('存款金额')
    status = savemoney(account,money)
    if status:
        print("存款成功")
        printuser(account)
    else:
        print('没有该用户，存款失败')
    return

# 添加存款
def savemoney(account,money):
    sql = 'select * from user where 账号 = %s'
    data = select(sql,account,'all')
    if len(data) == 0:
        return False
    else:
        sql1 = 'update user set 存款余额 = %s where 账号 = %s'
        update(sql1,[data[0][7]+money,account])
        return True

# 取款
def with_draw():
    account = input('请输入账号')
    mima = innum('密码')
    money = innum('取钱金额')
    status = withdraw(account,mima,money)
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
def withdraw(account,mima,money):
    sql = 'select * from user where 账号 = %s'
    data = select(sql, account, 'all')
    if len(data) == 0:
        return 1
    elif data[0][2] != mima:
        return 2
    elif data[0][7] < money:
        return 3
    else:
        sql1 = 'update user set 存款余额 = %s where 账号 = %s'
        update(sql1,[data[0][7]-money,account])
        return 0

# 转账
def Transfer():
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

# 执行转账
def transfer(dict):
    sql = 'select * from user where 账号 = %s'
    data1 = select(sql,dict['账号1'],'all')
    data2 = select(sql,dict['账号2'],'all')
    if len(data1) < 1 or len(data2) < 1:
        return 1
    elif data1[0][2] != dict['密码1'] or data2[0][2] != dict['密码2']:
        return 2
    elif data1[0][7] < dict['转账金额']:
        return 3
    else:
        sql1 = 'update user set 存款余额 = %s where 账号 = %s'
        sql2 = 'update user set 存款余额 = %s where 账号 = %s'
        data3 = select(sql, dict['账号2'], 'all')
        update(sql1, [data1[0][7]-dict['转账金额'],dict['账号1']])
        update(sql2, [data3[0][7]+dict['转账金额'],dict['账号2']])
        return 0

# 查询
def Query():
    acount = input('请输入账号')
    mima = innum('密码')
    query(acount,mima)
    return

# 执行查询
def query(account,mima):
    sql = 'select * from user where 账号 = %s'
    data = select(sql, account, 'all')
    if len(data) == 0:
        print('该用户不存在')
        return
    elif data[0][2] != mima:
        print('密码不正确')
        return
    else:
        printuser(account)

# 主程序
while 1:
    jiemian()
    num = input('请选择业务')
    while notnum(num):
        print('输入不合法，请重新输入')
        num = input('请选择业务')
    num = int(num)
    if num == 1:
        add_users()
    elif num == 2:
        save_money()
    elif num == 3:
        with_draw()
    elif num == 4:
        Transfer()
    elif num == 5:
        Query()
    elif num == 6:
        print('*',' '*6,'欢迎下次使用',' '*6,'*')
        exit()
    else:
        print('输入不合法，请重新输入')