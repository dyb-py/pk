# import multiprocessing,time
# info=[1,2,3,4,55,233]
#
# def fun(i):
#     time.sleep(0.01)
#     print(info[i])
# if __name__=='__main__':
#     pool=multiprocessing.Pool(6)
#     for i in range(6):
#         pool.apply_async(func=fun,args=(i,))
#     pool.close()
#     pool.join()
#
#     print('end')

# import multiprocessing,time
#
# def getItems(money):
#     for i in range(100):
#         money.value+=1
#         print(money.value)
#
#
#
# if __name__ == '__main__':
#     q = multiprocessing.Queue()  # 默认无限大
#     money=multiprocessing.Value('i',500)
#     p1=multiprocessing.Process(target=getItems,args=(money,))
#     p2=multiprocessing.Process(target=getItems,args=(money,))
#     p3=multiprocessing.Process(target=getItems,args=(money,))
#     p4=multiprocessing.Process(target=getItems,args=(money,))
#     p5=multiprocessing.Process(target=getItems,args=(money,))
#     p6=multiprocessing.Process(target=getItems,args=(money,))
#     p7=multiprocessing.Process(target=getItems,args=(money,))
#     p8=multiprocessing.Process(target=getItems,args=(money,))
#     p9=multiprocessing.Process(target=getItems,args=(money,))
#     p10=multiprocessing.Process(target=getItems,args=(money,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#     p4.start()
#     p5.start()
#     p6.start()
#     p7.start()
#     p8.start()
#     p9.start()
#     p10.start()
#
#     p1.join()
#     p2.join()
#     p3.join()
#     p4.join()
#     p5.join()
#     p6.join()
#     p7.join()
#     p8.join()
#     p9.join()
#     p10.join()
