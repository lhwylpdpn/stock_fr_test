#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import os
import random

#进数据、买卖逻辑、统计信息概要输出，详细输出、外围操作

def shujuyuan(rx,r_count):
	data_yuan=[]
	data_yuan.append(1000)
	r=1000+rx
	r2=1000-rx
	# r=10
	# for y in xrange(0,r_count):

	# 	for x in xrange(1,r):
	# 		if y%2==0:
			
	# 			data_yuan.append(data_yuan[x+(r-1)*y-1]+1)
	# 		if y%2==1:
			
	# 			data_yuan.append(data_yuan[x+(r-1)*y-1]-1)
	for x in xrange(1,r_count):
		task=data_yuan[x-1]+random.randint(-1,1)
		while task>r:
			task=data_yuan[x-1]+random.randint(-1,1)
		while task<r2:
			task=data_yuan[x-1]+random.randint(-1,1)
		data_yuan.append(task)
		

	return data_yuan

def caozuo(zuidadanbian,zhiying,rx,r_count):
	static_=static()
	data_=shujuyuan(rx,r_count)
	buy_=[]
	buy_num=[]

	num_static=[]
	num_max_static=[]
	sell_=[]
	sell_num=[]

	sell_static=[]
	sell_max_static=[]
	account_buy=[]
	account_sell=[]
	chengben=[]
	chengben_sell=[]
	result=[]
	account_real=[]

	buy_maxnum=[]
	sell_maxnum=[]
	# buy_maxnum.append(1)
	# buy_maxnum.append(1)
	# buy_maxnum.append(1)
	# buy_maxnum.append(1)
	# buy_maxnum.append(1)
	# buy_maxnum.append(1)
	# buy_maxnum.append(1)
	# buy_maxnum.append(1)
	# buy_maxnum.append(1)
	# buy_maxnum.append(1)
	# sell_maxnum.append(1)
	# sell_maxnum.append(1)
	# sell_maxnum.append(1)
	# sell_maxnum.append(1)
	# sell_maxnum.append(1)
	# sell_maxnum.append(1)
	# sell_maxnum.append(1)
	# sell_maxnum.append(1)
	# sell_maxnum.append(1)
	# sell_maxnum.append(1)

	buy_maxnum.append(0)
	buy_maxnum.append(1)
	sell_maxnum.append(0)
	sell_maxnum.append(1)


	data_start=data_[0]
	data_start_down=data_[0]
	x_sum=0
	x_count=0

	ttt=[]
	yingli=[]



# 时间序列计算变化	 ---- buy
# 考虑统计交易次数、最大手数、最大资金占用、盈余，最大单鞭
	for x in xrange(0,len(data_)):


			buy_now=0
			sell_now=0
			#如果单边超过多少止盈
			if len(buy_)==1 and data_[x]-data_[x-1]>=1 and buy_num[0]>=zuidadanbian:

				buy_.pop()
				buy_num.pop()
				static_.tracking_action("a",x,-1,1,data_[x])
			#涨就抛出
			elif data_[x]-data_[x-1]>=1 and len(buy_)>1:

				buy_.pop()
				buy_num.pop()
				static_.tracking_action("a",x,-1,1,data_[x])
			#跌就加仓
			if  data_[x]-data_[x-1]<=-1:
				buy_.append(data_[x])
				buy_num.append(1)
				static_.tracking_action("a",x,1,1,data_[x])
			#如果单边超过多少止盈
			if len(sell_)==1 and  data_[x]-data_[x-1]<=-1 and sell_num[0]>=zuidadanbian:	
				sell_.pop()
				sell_num.pop()
				static_.tracking_action("a",x,-2,1,data_[x])
			elif data_[x]-data_[x-1]<=-1 and len(sell_)>1:	
				sell_.pop()
				sell_num.pop()
				static_.tracking_action("a",x,-2,1,data_[x])
			if data_[x]-data_[x-1]>=1:
				sell_.append(data_[x])
				sell_num.append(1)
				static_.tracking_action("a",x,2,1,data_[x])

			
		

			# account_real.append(x2)
			# if x2>=zhiying:
			# 	buy_=[]
			# 	buy_num=[]


			# 	sell_=[]
			# 	sell_num=[]


			# 	account_buy=[]
			# 	account_sell=[]
			# 	chengben=[]
			# 	chengben_sell=[]
				
			# 	x_sum=x_sum+x2
			# 	x_count=x_count+1

				
			# 	continue


def json(canshu):

	file_object = open('result.json','a')
	file_object.write(canshu+"\n")
	file_object.close()

def json_clear():

	file_object = open('result.json','w')
	file_object.close()
class static:

	name=[]
	price=[]
	num_sell_all=[]#持有空单手数
	num_buy_all=[]#持有多单手数
	trader_buy_count=[]#多单交易次数，已平
	trader_sell_count=[]#空单交易次数，已平
	trader_buy_num=[]#多单交易手数，已平
	trader_sell_num=[]#空单交易手数，已平
	AccountEquity=0#净值
	AccountBalance=0#累积收益
	AccountFreeMargin=0#可用保证金
	def status_update(self,name,time,buy_or_sell,num,price):
		name.append(name)
		price.append(price)
		if buy_or_sell=="1":
			num_buy_all.append[num]
		if buy_or_sell=="2"
			num_sell_all.append[num]
		if buy_or_sell=="-1"
			trader_buy_count.append[1]
			num_buy_all.remove(num)
			trader_buy_num.append(num)
		if buy_or_sell=="-2"
			trader_sell_count.append[1]
			num_sell_all.remove(num)
			trader_sell_num.append(num)

	def tracking_action(self,name,time,buy_or_sell,num,price):#1 buy create ,-1 buy close ,2 sell create ,-2 sell close
		print("A",name,time,buy_or_sell,num,price)

if __name__ == '__main__':
	
	caozuo(8,5,10,100)


