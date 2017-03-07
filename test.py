#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import os
import random
import csv
import re
import time
import numpy
#进数据、买卖逻辑、统计信息概要输出，详细输出、外围操作

def load_data_mock():
	data_yuan=[]
	data_yuan.append(1.07821)

	# r=10
	# for y in xrange(0,r_count):

	# 	for x in xrange(1,r):
	# 		if y%2==0:
			
	# 			data_yuan.append(data_yuan[x+(r-1)*y-1]+1)
	# 		if y%2==1:
			
	# 			data_yuan.append(data_yuan[x+(r-1)*y-1]-1)
	for x in xrange(1,35961):
		task=data_yuan[x-1]-0.00001
		data_yuan.append(task)
		

	return data_yuan


def load_data(str1):
	f=file("data/"+str1+".csv","rb")
	reader=csv.reader(f)
	data=[]
	reader.next()
	for line in reader:
		#print(float(line[-3]))
		#data.append(float(re.split(" ",line[0])[-3]))
		 data.append(float(line[-3]))
	f.close()

	return data

def strategy_test():
	static_=static()
	data_=stock_data_all[0:144000*365*4]
	print(len(data_),max(data_),min(data_))
	print(data_[-1])
	dis=0.002 	
	hope_open_low=data_[0]-dis
	hope_open_high=data_[0]+dis
	hope_open_sell_low=data_[0]+dis
	hope_open_sell_high=data_[0]-dis
	num_low=[]
	num_sell_low=[]
	num_low.append(1)
	num_sell_low.append(1)
	num_low.append(1)
	num_sell_low.append(1)
	last_AccountEquity=0
	last_x=0

	num_high=[]
	num_sell_high=[]
	num_high.append(1)
	num_sell_high.append(1)
	num_high.append(1)
	num_sell_high.append(1)






	book=order_opreation()
	book.order_open(static_,"testpinzhong",0,1,1,data_[0],data_[0]+dis)
	book.order_open(static_,"testpinzhong",0,2,1,data_[0],data_[0]-dis)




	#print(data_)
	for x in xrange(0,len(data_)):

		temp=0
		for y in xrange(0,len(book.order_id)):


			y=y-temp

			if book.order_status[y]==1 and data_[x]>=book.order_hope_close[y] and book.order_buyorsell[y]==1:
				#print(x,book.order_hope_close[y],hope_open_high,data_[x],num_low[-1])
				if len(num_low)>2:
					num_low.pop()
				book.order_close(static_,y,x,-1,data_[x])
				hope_open_low=hope_open_low+dis
				temp=temp+1
		temp=0

		for y in xrange(0,len(book.order_id)):

			y=y-temp
			if book.order_status[y]==1 and data_[x]<=book.order_hope_close[y] and book.order_buyorsell[y]==2:
				#print("b",x,book.order_open_time[y],book.order_hope_close[y],hope_open_sell_high,data_[x],num_sell_low[-1])
				if len(num_sell_low)>2:
					num_sell_low.pop()
				book.order_close(static_,y,x,-2,data_[x])
				hope_open_sell_low=hope_open_sell_low-dis		 
				temp=temp+1
		##########必须有初始单
		########## 正向
		#当前有一个开单值，到了开单
		#print("s1",num_low[-1])
		if data_[x]<=hope_open_low:
			book.order_open(static_,"testpinzhong",x,1,num_low[-1],hope_open_low,hope_open_low+dis)
			hope_open_low=hope_open_low-dis
			num_low.append(num_low[-1]+num_low[-2])
		if data_[x]>=hope_open_high:
			
			#print(x,num_low[-1],data_[x])
			book.order_open(static_,"testpinzhong",x,1,num_high[-1],hope_open_high,hope_open_high+dis)
			hope_open_high=hope_open_high+dis
			num_high.append(num_high[-1]+num_high[-2])
		
		#每个单有一个关单值，超过了9关单


		########## 逆向

		if data_[x]>=hope_open_sell_low:
			book.order_open(static_,"testpinzhong",x,2,1,hope_open_sell_low,hope_open_sell_low-dis)
			hope_open_sell_low=hope_open_sell_low+dis
			num_sell_low.append(num_sell_low[-1]+num_sell_low[-2])
		if data_[x]<=hope_open_sell_high:
			#print(x,num_sell_low[-1],data_[x])
			book.order_open(static_,"testpinzhong",x,2,num_sell_high[-1],hope_open_sell_high,hope_open_sell_high-dis)
			hope_open_sell_high=hope_open_sell_high-dis
			num_sell_high.append(num_sell_high[-1]+num_sell_high[-2])
		#每个单有一个关单值，超过了9关单

		#print(round(float(x)/float(len(data_)),4)*100)


		static_.realtime_status_update("testpinzhong",x,data_[x])
		if static_.AccountEquity[-1]-last_AccountEquity>3 or (x-last_x>144000 and static_.AccountEquity[-1]-last_AccountEquity>=0) :
			#print(x,static_.AccountEquity[-1],last_AccountEquity)
			last_AccountEquity=static_.AccountEquity[-1]
			last_x=x+1
			book.report_detail()
			static_.clear_store()
			num_high=[]
			num_sell_high=[]
			num_high.append(1)
			num_sell_high.append(1)
			num_high.append(1)
			num_sell_high.append(1)


			num_low=[]
			num_sell_low=[]
			num_low.append(1)
			num_sell_low.append(1)
			num_low.append(1)
			num_sell_low.append(1)

			hope_open_low=data_[x+1]-dis
			hope_open_high=data_[x+1]+dis
			hope_open_sell_low=data_[x+1]+dis
			hope_open_sell_high=data_[x+1]-dis
			book=order_opreation()
			book.order_open(static_,"testpinzhong",0,1,1,data_[x+1],data_[x+1]+dis)
			book.order_open(static_,"testpinzhong",0,2,1,data_[x+1],data_[x+1]-dis)

	book.report_detail()
	static_.result()
	#static_.test()
class order_opreation:
	#book  status
	commission=0.0002
	key_id=[]
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
	#book B history
	order_id_history=[]
	order_name_history=[]
	order_open_price_history=[]
	order_hope_open_history=[]
	order_hope_close_history=[]
	order_close_price_history=[]
	order_num_history=[]
	order_open_time_history=[]
	order_close_time_history=[]
	order_status_history=[]
	order_buyorsell_history=[]
	def __init__(self):
			#book  status
		self.order_id=[]
		self.order_name=[]
		self.order_open_price=[]
		self.order_hope_open=[]
		self.order_hope_close=[]
		self.order_close_price=[]
		self.order_num=[]
		self.order_open_time=[]
		self.order_close_time=[]
		self.order_status=[]
		self.order_buyorsell=[]
		#book B history
		self.order_id_history=[]
		self.order_name_history=[]
		self.order_open_price_history=[]
		self.order_hope_open_history=[]
		self.order_hope_close_history=[]
		self.order_close_price_history=[]
		self.order_num_history=[]
		self.order_open_time_history=[]
		self.order_close_time_history=[]
		self.order_status_history=[]
		self.order_buyorsell_history=[]
	def order_open(self,static_object,name,time,buy_or_sell,num,price,hope_close): # 1buy 2 sell
		self.order_id.append(len(self.key_id)+1)
		self.order_name.append(name)
		self.order_buyorsell.append(buy_or_sell)
		self.order_open_time.append(time)
		self.order_hope_open.append(float(price))
		if buy_or_sell==1:
			self.order_open_price.append(float(price)+self.commission)
			static_object.tracking_action(name,time,buy_or_sell,num,float(price)+self.commission)
		else:
			self.order_open_price.append(float(price))
			static_object.tracking_action(name,time,buy_or_sell,num,price)
		self.order_hope_close.append(float(hope_close))
		self.order_status.append(1)#1 正常，2 已关闭
		self.order_num.append(num)

		self.order_close_price.append(0)
		self.order_close_time.append(0)
	
		#记录tracking_action 函数,持仓 金额、单数、单价，账户 金额  变化
		#变更status状态。

	def order_close(self,static_object,orderid,time,buy_or_sell,price):# -1 close buy ,-2 close sell
		#建立历史book
		#print(time,self.order_num[orderid])
		self.order_id_history.append(self.order_id[orderid])
		self.order_name_history.append(self.order_name[orderid])
		self.order_open_price_history.append(self.order_open_price[orderid])
		self.order_hope_open_history.append(self.order_hope_open[orderid])
		self.order_hope_close_history.append(self.order_hope_close[orderid])
		if buy_or_sell==1:
			self.order_close_price_history.append(self.order_hope_close[orderid])
			static_object.tracking_action(self.order_name[orderid],time,buy_or_sell,self.order_num[orderid],self.order_hope_close[orderid])
		else:
			self.order_close_price_history.append(self.order_hope_close[orderid]+self.commission)
			static_object.tracking_action(self.order_name[orderid],time,buy_or_sell,self.order_num[orderid],self.order_hope_close[orderid]+self.commission)
		self.order_num_history.append(self.order_num[orderid])
		self.order_open_time_history.append(self.order_open_time[orderid])
		self.order_close_time_history.append(time)
		self.order_status_history.append(2)
		self.order_buyorsell_history.append(self.order_buyorsell[orderid])
		
		#pop新book

		self.order_id.pop(orderid)
		self.order_name.pop(orderid)
		self.order_open_price.pop(orderid)
		self.order_hope_open.pop(orderid)
		self.order_hope_close.pop(orderid)
		self.order_close_price.pop(orderid)
		self.order_num.pop(orderid)
		self.order_open_time.pop(orderid)
		self.order_close_time.pop(orderid)
		self.order_status.pop(orderid)
		self.order_buyorsell.pop(orderid)



		#标记状态为2
		#记录关闭时间、关闭手数、关闭time

		#记录tracking_action 函数 ，持仓 金额、单数、单价，账户 金额  变化

	def test(self):
		print("order")
		for x in xrange(0,len(self.order_id)):

			print(self.order_id[x],self.order_name[x],"open price:",self.order_open_price[x],"close price",self.order_close_price[x],"num:",self.order_num[x],self.order_open_time[x],"1 open 2 close",self.order_status[x],"buy or sell",self.order_buyorsell[x])
		print("history order")
		for x in xrange(0,len(self.order_id)):
			print(self.order_id_history[x],self.order_name_history[x],"open price:",self.order_open_price_history[x],"close price",self.order_close_price_history[x],"num:",self.order_num_history[x],self.order_open_time_history[x],"1 open 2 close",self.order_status_history[x],"buy or sell",self.order_buyorsell_history[x])

	def report_detail(self):
		csvfile=file("report_detail.csv",'a')
		csvfile.write(str(random.random())+"\n")
		csvfile.write("real  data:"+"\n")
		for x in xrange(0,len(self.order_id)):
			temp=str(self.order_id[x])+",open price,	"+str(self.order_open_price[x])+",close price,	"+str(self.order_close_price[x])+",hope close, 	"+str(self.order_hope_close[x])+",num:,	"+str(self.order_num[x])+",open time ,	"+str(self.order_open_time[x])+"status,	"+str(self.order_status[x])+" buy or sell,	"+str(self.order_buyorsell[x])
			csvfile.write(temp+"\n")
		
		csvfile.write("history data:"+"\n")
		for x in xrange(0,len(self.order_id_history)):
			temp=str(self.order_id_history[x])+",open price,"+str(self.order_open_price_history[x])+",close price,"+str(self.order_close_price_history[x])+",hope close,"+str(self.order_hope_close_history[x])+",num:,"+str(self.order_num_history[x])+",open time ,"+str(self.order_open_time_history[x])+",close time ,"+str(self.order_close_time_history[x])+"status,"+str(self.order_status_history[x])+" buy or sell,"+str(self.order_buyorsell_history[x])
			csvfile.write(temp+"\n")
		csvfile.close()



class static:
	def test(self):
		print(self.trader_buy_num,self.trader_sell_num)
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
	def __init__(self):
		self.name_=[]
		self.price_=[]
		self.num_sell_all=[]#持有空单手数
		self.num_buy_all=[]#持有多单手数
		self.num_all=[]#总持仓数
		self.trader_buy_count=[]#多单交易次数，已平
		self.trader_sell_count=[]#空单交易次数，已平
		self.trader_buy_num=[]#多单交易手数，已平
		self.trader_sell_num=[]#空单交易手数，已平
		self.AccountEquity=[]#净值
		self.AccountBalance=0#累积收益
		self.AccountFreeMargin=0#现金
		self.restart_count=0#止盈次数
	def clear_store(self):
		self.num_sell_all=[]
		self.num_buy_all=[]
		self.AccountFreeMargin=self.AccountEquity[-1]/1000
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
		#	print(self.AccountFreeMargin,self.AccountFreeMargin-sum(self.num_sell_all)*price+sum(self.num_buy_all)*price,price,sum(self.num_sell_all),sum(self.num_buy_all))
	def realtime_status_update(self,name,time,price):
		#更新名称，价格，账户金额，持仓
		self.name_.append(name)
		self.price_.append(price)
		self.num_all.append(sum(self.num_sell_all)+sum(self.num_buy_all))
		#print(self.AccountFreeMargin,sum(self.num_sell_all),sum(self.num_sell_all)*price,sum(self.num_buy_all),sum(self.num_buy_all)*price,self.AccountFreeMargin-sum(self.num_sell_all)*price+sum(self.num_buy_all)*price,price)
		self.AccountEquity.append(1000*(self.AccountFreeMargin-sum(self.num_sell_all)*price+sum(self.num_buy_all)*price))
	def result(self):
		self.json_write(self.AccountEquity,"money","w","/Library/WebServer/Documents/")
		self.json_write(self.price_,"price","w","/Library/WebServer/Documents/")
		self.json_write(self.num_all,"num","w","/Library/WebServer/Documents/")

		#print("last sell num :",sum(self.num_sell_all),"lase buy num :",sum(self.num_buy_all),"trade buy count:",sum(self.trader_buy_count),"trade sell count:",sum(self.trader_sell_count),"trade sell num:",sum(self.trader_sell_num),"trade buy num:",sum(self.trader_buy_num))
		#print("last money:",self.AccountEquity[-1],"min money:",min(self.AccountEquity),"restart_count:",self.restart_count)
		csvfile=file("report_all.csv",'a')
		csvfile.write("\n")

		#temp="last sell num:,	"+str(sum(self.num_sell_all))+",lase buy num:,	"+str(sum(self.num_buy_all))+",trade buy count:,	"+str(sum(self.trader_buy_count))+",trade sell count:,	"+str(sum(self.trader_sell_count))+",trade sell num:,	"+str(sum(self.trader_sell_num))+",trade buy num:,	"+str(sum(self.trader_buy_num))+",last money:,	"+str(self.AccountEquity[-1])+",min money:,	"+str(min(self.AccountEquity))+",restart_count:,	"+str(self.restart_count)
		temp="trade count num:,	"+str(sum(self.trader_sell_num)+sum(self.trader_buy_num))+",last money:,	"+str(self.AccountEquity[-1])+",min money:,	"+str(min(self.AccountEquity))+",max money:,	"+str(max(self.AccountEquity))+",max num:,	"+str(max(self.num_all))+",盈利率:,	"+str(round(float(self.AccountEquity[-1]/max(self.num_all)/10),5)*100)+"%,sharpe:,	"+str(self.AccountEquity[-1]/numpy.std(self.AccountEquity))
		csvfile.write(temp)
		csvfile.close()
		#print(str(round(float(self.AccountEquity[-1]/numpy.std(self.AccountEquity)),5)*100)+"%",self.AccountEquity[-1],numpy.std(self.AccountEquity))
	def json_write(self,data,name,type,path):
		file_object=open(str(path)+name+'.json',str(type))
		file_object.write("[\n")
		for x in xrange(0,len(data)):
			
			file_object.write("["+str(x)+","+str(data[x])+"],\n")

		file_object.seek(-2, os.SEEK_END)
		file_object.write("]\n")

class tt:
	test=[]
	def __init__(self):
		self.test=[]
	def add(self):
		self.test.append(1)
	def get(self):
		print(self.test)

if __name__ == '__main__':
	if  os.path.exists("report_all.csv"):
		os.remove("report_all.csv")
	if  os.path.exists("report_detail.csv"):
		os.remove("report_detail.csv")
	stock_data_all=[]
	stock_data_all=load_data("AUDCAD_tick")
	strategy_test()
	print time.asctime(time.localtime(time.time()))
