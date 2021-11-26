import time
import threading

class values:
    eggTart = 0
    time1 = time.perf_counter()
lock = threading.Lock()

class cooker(threading.Thread):
    __name = ''
    __money = 0
    __num = 0
    __price = 1.5
    def setname(self,name):
        self.__name = name
    def getname(self):
        return self.__name
    def setmoney(self,money):
        self.__money = money
    def getmoney(self):
        return self.__money
    def setnum(self,num):
        self.__num = num
    def getnum(self):
        return self.__num
    def setprice(self,price):
        self.__price = price
    def getprice(self):
        return self.__price
    def produce(self):
        while int(time.perf_counter() - values.time1) < 60:
            while values.eggTart >= 500:
                time.sleep(3)
            lock.acquire()
            values.eggTart += 1
            self.__num += 1
            print('厨师{}做了{}份蛋挞'.format(self.__name,self.__num))
            lock.release()
        time.sleep(0.5)
        print('厨师{}总共做出了{}份蛋挞，工资为{}'.format(self.__name,self.__num,self.countmoney()))
    def countmoney(self):
        self.setmoney(self.__num * self.__price)
        return self.getmoney()
    def run(self) -> None:
        self.produce()

class customer(threading.Thread):
    __name = ''
    __money = 5000
    __num = 0
    __price = 0
    def setname(self, name):
        self.__name = name
    def getname(self):
        return self.__name
    def setmoney(self, money):
        self.__money = money
    def getmoney(self):
        return self.__money
    def setnum(self, num):
        self.__num = num
    def getnum(self):
        return self.__num
    def setprice(self, price):
        self.__price = price
    def getprice(self):
        return self.__price
    def buy(self):
        while int(time.perf_counter() - values.time1) < 60 and self.getmoney() > 3:
            while values.eggTart <= 0:
                time.sleep(2)
            lock.acquire()
            self.__money -= 3
            self.__num += 1
            print('顾客{}买了{}份蛋挞,剩{}元'.format(self.__name,self.__num,self.__money))
            lock.release()
        if self.__money < 3:
            return
    def run(self) -> None:
        self.buy()

list1 = []
for i in range(3):
    list1.append(i)
    list1[i] = cooker()
    list1[i].setname(i)
    list1[i].start()
for j in range(3,9):
    list1.append(j)
    list1[j] = customer()
    list1[j].setname(j)
    list1[j].start()
while int(time.perf_counter() - values.time1) < 61:
    # time.sleep(0.1)
    # print(time.perf_counter() - values.time1)
    pass
for k in list1:
    k.join()
exit()

