
from rediscluster import RedisCluster

#
clusternodes = [
#     每个节点 ip信息
    {'host':'192.168.174.128','port':8001},
    {'host':'192.168.174.128','port':8002},
    {'host':'192.168.174.128','port':8003},
    {'host':'192.168.174.128','port':8004},
    {'host':'192.168.174.128','port':8005},
    {'host':'192.168.174.128','port':8006},
    {'host':'192.168.174.128','port':8007},
]
redis = RedisCluster(startup_nodes=clusternodes)
print(redis)

#  数据操作
# redis.set('age',18)
# redis.set('name','sunge')
# redis.lpush('list1',10,20,30,40,50)
# 读取工作
print(redis.lrange('list1',0,-1))