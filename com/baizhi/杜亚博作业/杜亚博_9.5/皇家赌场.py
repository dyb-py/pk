# 皇家赌场
# 1. 掷骰子   2. 人类玩家，电脑玩家    3. 对比骰子的大小
# 压点 ， 电脑和人 分别有500点   每次游戏，分别需要投入1点作为底
# 人类玩家和电脑玩家投掷骰子后，不立刻开盘，要加价： 由人提出是否开盘，
# 加价：人类玩家，加多少点，电脑玩家也跟多少，人类玩家，可以多次加价
# 特殊情况： 任何一方如果不够加价数量，则全部加出，并立刻开盘
# 直到有任何一方输光为止，才公布谁赢谁输
# 如果两方的点数一样，则返还各自所有点

import random

# 玩家的骰子点数
player=0
# 电脑的骰子点数
computer=0
#奖池
pool=0

playerMoney=computerMoney=500

print('**********欢迎来到飞哥皇家赌场，平台有小姐姐发牌，还送3天VIP************')
while 1:
    r=input('1. 开始游戏 2. 充值 3. 退出游戏')
    if r=='1':
        # 开始游戏
        #玩家和电脑点数减1
        playerMoney=playerMoney-1
        computerMoney=computerMoney-1
        #输入当前money
        print('当前money为' + str(playerMoney))
        player = random.randint(1,6)
        computer=random.randint(1,6)
        A=1
        while A:
            a = int(input('1.加价 2.开盘'))
            if a == 1:
                # 加价
                while 1:
                    #输入加价点数
                    money = int(input('输入加的点数'))
                    if money <= playerMoney and money > 0 and money<=computerMoney:
                        #加价成功 是否继续加价
                        print('加价成功')
                        playerMoney -= money
                        computerMoney -= money
                        pool =pool+ money * 2
                        print('是否继续加价  当前剩余点数为' + str(playerMoney))
                        break
                    else:
                        #点数不够，all in 开盘
                        print('玩家或电脑点数不够 all in 开盘')
                        if player < computer:
                            #玩家输
                            # 判断玩家和电脑money多少，加价为少的一方
                            if playerMoney<=computerMoney:
                               pool=playerMoney*2
                            else:pool=computerMoney*2
                            playerMoney=playerMoney-pool/2
                            computerMoney=computerMoney+pool/2
                            print('这次你输了' + str(pool/2) + '点' + '  还剩' + str(playerMoney)+'  电脑还有'+str(computerMoney)+'点')
                            pool = 0
                            if playerMoney <= 0:
                                print('你输了')
                                exit()
                            else:
                                A=0
                                break
                        elif player > computer:
                            #玩家赢
                            #判断玩家和电脑money多少，加价为少的一方
                            if playerMoney <= computerMoney:
                                pool = playerMoney * 2
                            else:
                                pool = computerMoney * 2
                            playerMoney = playerMoney + pool/2
                            computerMoney =computerMoney - pool/2
                            print('这次你赢了' + str(pool/2) + '点' + '  还剩' + str(playerMoney)+'  电脑还有'+str(computerMoney)+'点')
                            pool = 0
                            if computerMoney <= 0:
                                #money为零 游戏结束
                                print('你赢了')
                                exit()
                            else:
                                A=0
                                break
                        elif player == computer:
                            #平局
                            print('平局')
                            playerMoney += (pool/2)
                            computerMoney += (pool/2)
                            pool = 0
                            A=0
                            break
            elif a == 2:
                print('开盘')
                if player < computer:
                    #玩家输
                    computerMoney += pool
                    print('这次你输了' + str(pool/2) + '点' + '  还剩' + str(playerMoney)+'  电脑还有'+str(computerMoney)+'点')
                    pool = 0
                    if playerMoney <= 0:
                        print('你输了')
                        exit()
                    else:
                        break
                elif player > computer:
                    #玩家赢
                    playerMoney += pool
                    print('这次你赢了' + str(pool/2) + '点' + '  还剩' + str(playerMoney)+'  电脑还有'+str(computerMoney)+'点')
                    pool = 0
                    if computerMoney <= 0:
                        print('你赢了')
                        exit()
                    else:
                        break
                elif player == computer:
                    print('平局')
                    playerMoney += money
                    computerMoney += money
                    pool = 0
                    break

            else:
                print('输入错误，重新输入')
    elif r=='2':
        # 充值
        add=int(input('输入充值金额'))
        playerMoney+=add
        print('现在money为'+str(playerMoney))
    elif r=='3':
        # 退出
        print('欢迎下次光临')
        exit()
    else:
        print('输入有误，请重新输入')











