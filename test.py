#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import os
import random

#进数据、买卖逻辑、统计信息概要输出，详细输出、外围操作

def load_data(r_count):
	data_yuan=[]
	data_yuan.append(1000)
	r=500
	r2=1500
	# r=10
	# for y in xrange(0,r_count):

	# 	for x in xrange(1,r):
	# 		if y%2==0:
			
	# 			data_yuan.append(data_yuan[x+(r-1)*y-1]+1)
	# 		if y%2==1:
			
	# 			data_yuan.append(data_yuan[x+(r-1)*y-1]-1)
	for x in xrange(1,r_count):
		task=data_yuan[x-1]+random.randint(-1,1)
		data_yuan.append(task)
		

	return data_yuan

# def strategy(zhiying,r,distance):
# 	static_=static()
# 	data_=load_data(r)
# 	#print(data_)
# 	zhiying_=zhiying
# 	zuidadanbian=10
# 	buy_=[]
# 	buy_num=[]
# 	sell_=[]
# 	sell_num=[]
# 	dis=float(distance)
# 	buy_open_real=data_[x]
# 	sell_open_real=data_[x]

# # 时间序列计算变化	 ---- buy
# # 考虑统计交易次数、最大手数、最大资金占用、盈余，最大单鞭
# 	for x in xrange(1,len(data_)):

# 			#buy
# 			#如果单边超过多少止盈
# 			if len(buy_)==1 and data_[x]-data_[x-1]>=dis and buy_num[0]>=zuidadanbian:#最大单边暂时无意义

# 				buy_.pop()
# 				buy_num.pop()
# 				static_.tracking_action("a",x,-1,1,data_[x])
# 			#涨就抛出
# 			elif data_[x]-data_[x-1]>=dis and len(buy_)>1:

# 				buy_.pop()
# 				buy_num.pop()
# 				static_.tracking_action("a",x,-1,1,data_[x])
# 			#跌就加仓
# 			if  data_[x]-buy_open_real<=-dis:
# 				buy_.append(data_[x])
# 				buy_num.append(1)
# 				buy_open_real
# 				static_.tracking_action("a",x,1,1,data_[x])
# 			#sell
# 			#如果单边超过多少止盈
# 			if len(sell_)==1 and  data_[x]-data_[x-1]<=-dis and sell_num[0]>=zuidadanbian:#最大单边暂时无意义
# 				sell_.pop()
# 				sell_num.pop()
# 				static_.tracking_action("a",x,-2,1,data_[x])
# 			elif data_[x]-data_[x-1]<=-dis and len(sell_)>1:	
# 				sell_.pop()
# 				sell_num.pop()
# 				static_.tracking_action("a",x,-2,1,data_[x])
# 			if data_[x]-data_[x-1]>=dis:
# 				sell_.append(data_[x])
# 				sell_num.append(1)
# 				static_.tracking_action("a",x,2,1,data_[x])
# 			static_.equity_static("a",x,data_[x]) #按时间记录金额变化
# 			if static_.AccountEquity[-1]>=zhiying_:
# 				buy_=[]
# 				buy_num=[]
# 				sell_=[]
# 				sell_num=[]
# 				static_.clear_store()
# 				zhiying_=zhiying_+zhiying
# 				static_.restart_count=static_.restart_count+1

# 			#if x2>=zhiying:
# 			# 	buy_=[]
# 			# 	buy_num=[]


# 			# 	sell_=[]
# 			# 	sell_num=[]


# 			# 	account_buy=[]
# 			# 	account_sell=[]
# 			# 	chengben=[]
# 			# 	chengben_sell=[]
				
# 			# 	x_sum=x_sum+x2
# 			# 	x_count=x_count+1

				
# 			# 	continue
# 	static_.result()
# #########################################################################################################################


def strategy_test():
	static_=static()
	data_=load_data(100)
	dis=2
	hope_open=data_[0]-dis
	hope_open_sell=data_[0]+dis
	book=order_opreation()
	for x in xrange(0,len(data_)):

		########## 正向
		#当前有一个开单值，到了开单
		if data_[x]<=hope_open:
			book.order_open(static_,"testpinzhong",x,1,1,data_[x],data_[x]+dis)
			hope_open=hope_open-dis
		#每个单有一个关单值，超过了9关单
		for y in xrange(0,len(book.order_id)):
			if book.order_status[y]==1 and data_[x]>book.order_hope_close[y] and book.order_buyorsell[y]==1:
				book.order_close(static_,y,x,-1,1,data_[x])
				hope_open=hope_open+dis

		########## 逆向
		if data_[x]>=hope_open_sell:
			book.order_open(static_,"testpinzhong",x,2,1,data_[x],data_[x]-dis)
			hope_open_sell=hope_open_sell+dis
		#每个单有一个关单值，超过了9关单
		for y in xrange(0,len(book.order_id)):
			if book.order_status[y]==1 and data_[x]<book.order_hope_close[y] and book.order_buyorsell[y]==2:
				book.order_close(static_,y,x,-2,1,data_[x])
				hope_open_sell=hope_open_sell-dis		




		static_.realtime_status_update("testpinzhong",x,data_[x])
	static_.result()

class order_opreation:
	#book A status
	order_id=[]
	order_name=[]
	order_open_price=[]
	order_hope_open=[]
	order_hope_close=[]
	order_close_price=[]
	order_num=[]
	order_open_time=[]
	order_close_time=[]
	order_status=[]
	order_buyorsell=[]

	def order_open(self,static_object,name,time,buy_or_sell,num,price,hope_close): # 1buy 2 sell
		self.order_id.append(len(self.order_id)+1)
		self.order_name.append(name)
		self.order_buyorsell.append(buy_or_sell)
		self.order_open_time.append(time)
		self.order_hope_open.append(float(price))
		self.order_open_price.append(float(price))
		self.order_hope_close.append(float(hope_close))
		self.order_status.append(1)#1 正常，2 已关闭
		self.order_num.append(num)
		self.order_close_price.append(0)
		self.order_close_time.append(0)
		static_object.tracking_action(name,time,buy_or_sell,num,price)
		
		#记录tracking_action 函数,持仓 金额、单数、单价，账户 金额  变化
		#变更status状态。

	def order_close(self,static_object,orderid,time,buy_or_sell,num,price):# -1 close buy ,-2 close sell
		self.order_hope_close[orderid]=0
		self.order_close_price[orderid]=float(price)
		self.order_close_time[orderid]=time
		self.order_status[orderid]=2

		#1 正常，2 已关闭


		static_object.tracking_action(self.order_name[orderid],time,buy_or_sell,num,price)

		#标记状态为2
		#记录关闭时间、关闭手数、关闭time

		#记录tracking_action 函数 ，持仓 金额、单数、单价，账户 金额  变化

	def test(self):
		for x in xrange(0,len(self.order_id)):
			print(self.order_id[x],self.order_name[x],self.order_open_price[x],self.order_hope_close[x],self.order_num[x],self.order_open_time[x],self.order_status[x],self.order_buyorsell[x])




def json(canshu):

	file_object = open('result.json','a')
	file_object.write(canshu+"\n")
	file_object.close()

def json_clear():

	file_object = open('result.json','w')
	file_object.close()


class static:
	# a=3
	# def add(self):
	# 	self.a=self.a+1
	# def test(self):
	# 	print(self.a)
	name_=[]
	price_=[]
	num_sell_all=[]#持有空单手数
	num_buy_all=[]#持有多单手数
	num_all=[]#总持仓数
	trader_buy_count=[]#多单交易次数，已平
	trader_sell_count=[]#空单交易次数，已平
	trader_buy_num=[]#多单交易手数，已平
	trader_sell_num=[]#空单交易手数，已平
	AccountEquity=[]#净值
	AccountBalance=0#累积收益
	AccountFreeMargin=0#现金
	restart_count=0#止盈次数
	def clear_store(self):
		self.num_sell_all=[]
		self.num_buy_all=[]
		self.AccountFreeMargin=self.AccountEquity[-1]
	def status_update(self,name,time,buy_or_sell,num,price):

		if str(buy_or_sell)=="1":
			self.num_buy_all.append(num)
			self.AccountFreeMargin=self.AccountFreeMargin-num*price#每次开多仓应该减去
		if str(buy_or_sell)=="2":
			self.num_sell_all.append(num)
			self.AccountFreeMargin=self.AccountFreeMargin+num*price#每次开空仓应该加上
		if str(buy_or_sell)=="-1":
			self.trader_buy_count.append(1)
			self.num_buy_all.remove(num)
			self.trader_buy_num.append(num)
			self.AccountFreeMargin=self.AccountFreeMargin+num*price
		if str(buy_or_sell)=="-2":
			self.trader_sell_count.append(1)
			self.num_sell_all.remove(num)
			self.trader_sell_num.append(num)
			self.AccountFreeMargin=self.AccountFreeMargin-num*price
	def tracking_action(self,name,time,buy_or_sell,num,price):#1 buy create ,-1 buy close ,2 sell create ,-2 sell close
		self.status_update(name,time,buy_or_sell,num,price)
	def realtime_status_update(self,name,time,price):
		#更新名称，价格，账户金额，持仓
		self.name_.append(name)
		self.price_.append(price)
		self.num_all.append(sum(self.num_sell_all)+sum(self.num_buy_all))
		#print(self.AccountFreeMargin,sum(self.num_sell_all),sum(self.num_sell_all)*price,sum(self.num_buy_all),sum(self.num_buy_all)*price,self.AccountFreeMargin-sum(self.num_sell_all)*price+sum(self.num_buy_all)*price,price)
		self.AccountEquity.append(self.AccountFreeMargin-sum(self.num_sell_all)*price+sum(self.num_buy_all)*price)
	def result(self):
		self.json_write(self.AccountEquity,"money","w","/Library/WebServer/Documents/")
		self.json_write(self.price_,"price","w","/Library/WebServer/Documents/")
		self.json_write(self.num_all,"num","w","/Library/WebServer/Documents/")
		print("last sell num :",sum(self.num_sell_all),"lase buy num :",sum(self.num_buy_all),"trade buy count:",sum(self.trader_buy_count),"trade sell count:",sum(self.trader_sell_count),"trade sell num:",sum(self.trader_sell_num),"trade buy num:",sum(self.trader_buy_num))
		print("last money:",self.AccountEquity[-1],"min money:",min(self.AccountEquity),"restart_count:",self.restart_count)
	def json_write(self,data,name,type,path):
		file_object=open(str(path)+name+'.json',str(type))
		file_object.write("[\n")
		for x in xrange(0,len(data)):
			
			file_object.write("["+str(x)+","+str(data[x])+"],\n")

		file_object.seek(-2, os.SEEK_END)
		file_object.write("]\n")
if __name__ == '__main__':

	strategy_test()
	tt=order_opreation()
	tt.test()


