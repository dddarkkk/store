'''
    方法：
        就是解决某一类问题的模型。
    如何申明一个方法？
    def 方法的名称():
        方法体

   任务1：
        旅游的导航系统 + 商城结合在一起。
    任务2：
        看下工商银行的系统。
'''

city = {
    "北京":{
        "昌平":{
            "八达岭":["八达岭长城"],
            "回龙观":["永旺超市","永辉超市","呷哺呷哺"]
        },
        "朝阳":{
            "景观":["玉渊潭公园"]
        },
        "海淀":{
            "高校":["清华","北大"],
            "公园":["香山","植物园"],
            "博物馆":["军事博物馆","国家地质公园"]
        }
    },
    "上海":{

    }
}

Friuts = {
	"苹果":12.3,  # 水果和单价
	"草莓":4.5,
    "香蕉":6.3,
    "葡萄":5.8,
    "橘子":6.4,
    "樱桃":15.8
}

def showCity(data):
    for i in data:
        print(i)

dict={}

while True:
    print("---------------欢迎来到Jason旅行社-----------------")
    print("有以下城市可以去：")
    showCity(city)
    print("请输入您要去的城市：")
    chose = input("")

    if chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break
    elif chose not in city:
        print("输入非法！请重新输入：")
    else:
        showCity(city[chose])
        chose2 = input("请输入您要去二级城市：")
        if chose2 == "q" or chose2 == "Q":
            print("欢迎下次光临！")
            break
        elif chose2 not in city[chose]:
            print("输入错误，别瞎弄！")

        else:
            showCity(city[chose][chose2])
            print("请输入要去的具体景点：")
            chose3 = input("")
            if chose3 == "q" or chose3 == "Q":
                print("欢迎下次光临！")
                break
            elif chose3 not in city[chose][chose2]:
                print("不好意思，没有这个景点！别瞎弄！")
            else:
                showCity(city[chose][chose2][chose3])
                print("每张票1000元/人！")
                inp = input("是否买点纪念品？输入y/Y进入商店")
                if inp == 'y' or inp == 'Y':
                    name = input("谁")
                    list = []
                    dict[name] = {'fruits': {}, "money": 0}
                    while True:
                        b = input("买什么")
                        if b in Friuts:
                            dict[name]['fruits'].update({b: Friuts[b]})
                            if b == "q" or b == 'Q':
                                break
                for i in dict[name]['fruits']:
                    list.append(dict[name]['fruits'][i])
                if name in dict:
                    dict[name]["money"] = sum(list)
                print(dict)



















