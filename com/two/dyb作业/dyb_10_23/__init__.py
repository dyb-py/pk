import MySQLdb
import cp_loader as loader

# 原则上：__init__.py只导入非本路径下的模块


__all__=['MySQLdb','loader']  # 加入模块名：加入别名