//+------------------------------------------------------------------+
//|                                                    wangge3.0.mq4 |
//|                        Copyright 2016, MetaQuotes Software Corp. |
//|                                             https://www.mql5.com |
//+------------------------------------------------------------------+
#property copyright "Copyright 2016, MetaQuotes Software Corp."
#property link      "https://www.mql5.com"
#property version   "1.00"
#property strict
//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int success_sum=0;
int fail_sum=0;
int fail_sum2=0;
int fail_sum3=0;
string order_id[];
float order_expect_close[];
float finalcost=AccountEquity();
float dis=0.002;
float num_low[];
float num_sell_low[];
int num_low_id=0;
int num_sell_low_id=0;

float num_high[];
float num_sell_high[];
int num_high_id=0;
int num_sell_high_id=0;

float tag;
float totalmoney[];
float totallots_test[];
float Margin[];

int OnInit()
  {
num_low_id=0;
num_sell_low_id=0;
ArrayResize(num_low,200);
ArrayResize(num_sell_low,200);
num_low[0]=0.01;
num_sell_low[0]=0.01;
num_low[1]=0.02;
num_sell_low[1]=0.02;
//for(int i=2;i<200;i++){num_low[i]=num_low[i-1];}
//for(int i=2;i<200;i++){num_sell_low[i]=num_sell_low[i-1];}
//for(int i=2;i<200;i++){num_low[i]=num_low[i-1]+num_low[i-2];}
//for(int i=2;i<200;i++){num_sell_low[i]=num_sell_low[i-1]+num_sell_low[i-2];}
//for(int i=2;i<200;i++){num_low[i]=num_low[i-1];}
//for(int i=2;i<200;i++){num_sell_low[i]=num_sell_low[i-1];}
for(int i=2;i<200;i++){num_low[i]=num_low[i-1]+0.01;}
for(int i=2;i<200;i++){num_sell_low[i]=num_sell_low[i-1]+0.01;}
num_high_id=0;
num_sell_high_id=0;
ArrayResize(num_high,200);
ArrayResize(num_sell_high,200);
num_high[0]=0.01;
num_sell_high[0]=0.01;
num_high[1]=0.02;
num_sell_high[1]=0.02;
//for(int i=2;i<200;i++){num_high[i]=num_high[i-1];}
//for(int i=2;i<200;i++){num_sell_high[i]=num_sell_high[i-1];}
for(int i=2;i<200;i++){num_high[i]=num_high[i-1]+0.01;}
for(int i=2;i<200;i++){num_sell_high[i]=num_sell_high[i-1]+0.01;}
//for(int i=2;i<200;i++){num_high[i]=num_high[i-1]*2;}
//for(int i=2;i<200;i++){num_sell_high[i]=num_sell_high[i-1]*2;}
//for(int i=2;i<200;i++){num_high[i]=num_high[i-1]+num_high[i-2];}
//for(int i=2;i<200;i++){num_sell_high[i]=num_sell_high[i-1]+num_sell_high[i-2];}
   GlobalVariableSet("status",1);
   GlobalVariableSet("hope_open_low",MarketInfo("AUDCAD",MODE_BID)-dis);
   GlobalVariableSet("hope_open_high",MarketInfo("AUDCAD",MODE_BID)+dis);
   GlobalVariableSet("hope_open_sell_low",MarketInfo("AUDCAD",MODE_BID)+dis);
   GlobalVariableSet("hope_open_sell_high",MarketInfo("AUDCAD",MODE_BID)-dis);
   printf(3);
   tag=MarketInfo("AUDCAD",MODE_BID);
   order_send ("AUDCAD",0,0.01,MarketInfo("AUDCAD",MODE_ASK),GlobalVariableGet("hope_open_high"));
   order_send ("AUDCAD",1,0.01,MarketInfo("AUDCAD",MODE_BID),GlobalVariableGet("hope_open_sell_high"));
   OrderSelect(order_id[1], SELECT_BY_TICKET,MODE_TRADES);
   GlobalVariableSet("time",float(OrderOpenTime())); 
   EventSetTimer(3);
   return(INIT_SUCCEEDED);
  }
//+------------------------------------------------------------------+
//| Expert deinitialization function                                 |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {
//--- destroy timer

      static_print();
  }
//+------------------------------------------------------------------+
//| Expert tick function                                             |
//+------------------------------------------------------------------+
void OnTick()

  {
  
  
  static_();
  
  clear_all();
  if(GlobalVariableGet("status")==1)
      {


        order_close();
 //  printf(GlobalVariableGet("hope_open_low"));
 // printf( GlobalVariableGet("hope_open_high"));
 //  printf(GlobalVariableGet("hope_open_sell_low"));
 //  printf(GlobalVariableGet("hope_open_sell_high"));
 //  printf(MarketInfo("AUDCAD",MODE_BID)+","+MarketInfo("AUDCAD",MODE_ASK));
         if(MarketInfo("AUDCAD",MODE_BID)<GlobalVariableGet("hope_open_low") )
         {
         order_send ("AUDCAD",0,num_low[num_low_id],MarketInfo("AUDCAD",MODE_ASK),MarketInfo("AUDCAD",MODE_BID)+dis);
         GlobalVariableSet("hope_open_low",GlobalVariableGet("hope_open_low")-dis);
            num_low_id=num_low_id+1;
         }

         if(MarketInfo("AUDCAD",MODE_BID)>GlobalVariableGet("hope_open_high"))
         {order_send ("AUDCAD",0,num_high[num_high_id],MarketInfo("AUDCAD",MODE_ASK),MarketInfo("AUDCAD",MODE_BID)+dis);
         GlobalVariableSet("hope_open_high",GlobalVariableGet("hope_open_high")+dis);
                 num_high_id=num_high_id+1; }
         
         if(MarketInfo("AUDCAD",MODE_BID)<GlobalVariableGet("hope_open_sell_high"))
         {order_send ("AUDCAD",1,num_sell_high[num_sell_high_id],MarketInfo("AUDCAD",MODE_BID),MarketInfo("AUDCAD",MODE_BID)-dis);
         GlobalVariableSet("hope_open_sell_high",GlobalVariableGet("hope_open_sell_high")-dis);
                  num_sell_high_id=num_sell_high_id+1;} 
         if(MarketInfo("AUDCAD",MODE_BID)>GlobalVariableGet("hope_open_sell_low") )
         {order_send ("AUDCAD",1,num_sell_low[num_sell_low_id],MarketInfo("AUDCAD",MODE_BID),MarketInfo("AUDCAD",MODE_BID)-dis);
         GlobalVariableSet("hope_open_sell_low",GlobalVariableGet("hope_open_sell_low")+dis);
                   num_sell_low_id=num_sell_low_id+1;
         }  
         } 
  }
//+------------------------------------------------------------------+
//| Timer function                                                   |
//+------------------------------------------------------------------+
void OnTimer()
  {


  
  }
//+------------------------------------------------------------------+

void order_send (string nameA,int open_status,string open_number,float hope_price,float zhiying_price)
{  int ticket_buy;
   int open_s2=9;
  
   if (open_status==1){open_s2=9;}else{open_s2=10;}
   ticket_buy=OrderSend(nameA,open_status,open_number,MarketInfo(nameA,open_s2),3,0,0,"",1,0);
   while(ticket_buy<0){ticket_buy=OrderSend(nameA,open_status,open_number,MarketInfo(nameA,open_s2),3,0,0,"",1,0);}
   
   //ArrayResize(order_num,ArraySize(order_num)+1);
   ArrayResize(order_id,ArraySize(order_id)+1);
   ArrayResize(order_expect_close,ArraySize(order_expect_close)+1);
   order_id[ArraySize(order_id)-1]=ticket_buy;
   //order_num[ArraySize(order_num)-1]=open_number;
   order_expect_close[ArraySize(order_expect_close)-1]=zhiying_price;
  
}

void order_close()

{ 
for(int i=0;i<ArraySize(order_id);i++)
  {if(StringLen(order_id[i])>0)
   {string buy_ticket="";
    string nameA="";
    float ln_close;
    float open_type;
    float open_price;
    buy_ticket=order_id[i];
    ln_close=order_expect_close[i];   
    OrderSelect(buy_ticket, SELECT_BY_TICKET,MODE_TRADES); 
    nameA=OrderSymbol();
    open_type=OrderType();
    open_price=OrderOpenPrice();
     
    if(MarketInfo(nameA,MODE_BID)>ln_close&&open_type==0)
    
    {   
     int i_close=1;
       int ticket=0;
       ticket=OrderClose(buy_ticket,OrderLots(),MarketInfo(nameA,MODE_BID),3);
       while(ticket<0&&i_close<5){ticket=OrderClose(buy_ticket,OrderLots(),MarketInfo(nameA,MODE_BID),3);i_close=i_close+1;}
       if(ticket>0)
             {
             order_id[i]="";
             order_expect_close[i]="";
             if(num_low_id>0){num_low_id=num_low_id-1;}
             GlobalVariableSet("hope_open_low",GlobalVariableGet("hope_open_low")+dis);
             }
     }
     
     
    if(MarketInfo(nameA,MODE_BID)<ln_close&&open_type==1)
    
    {  
    int i_close=1;
       int ticket=0;
       ticket=OrderClose(buy_ticket,OrderLots(),MarketInfo(nameA,MODE_ASK),3);
       while(ticket<0&&i_close<5){ticket=OrderClose(buy_ticket,OrderLots(),MarketInfo(nameA,MODE_ASK),3);i_close=i_close+1;}
       if(ticket>0)
             {
             order_id[i]="";
             order_expect_close[i]="";
            if(num_sell_low_id>0){num_sell_low_id=num_sell_low_id-1;}
             GlobalVariableSet("hope_open_sell_low",GlobalVariableGet("hope_open_sell_low")-dis);
             }
     }
   }
 
 
 
 
 
 
 
  }




}



void clear_all()
  
{  
   

  // if(float(TimeCurrent()-GlobalVariableGet("time"))>86390 )
   if(  AccountEquity()-finalcost>=3  || AccountEquity()-finalcost<=-100000  || totallots()==0 )
     { 
      if (AccountEquity()-finalcost>=3)
     {success_sum=success_sum+1;}
       if (AccountEquity()-finalcost<=-100000)
     {fail_sum=fail_sum+1;}    
       if ( AccountEquity()-finalcost<=0)
     {fail_sum2=fail_sum2+1;
     printf("失败计算"+(AccountEquity()-finalcost));}   
       if (totallots()==0)
     {fail_sum3=fail_sum3+1;}   
     GlobalVariableSet("status","close");
      
     

 while(OrdersTotal()>0)
   {for(int i=0;i<OrdersTotal();i++)
    {  int type;
       if(OrderSelect(i,SELECT_BY_POS)==false)
                   { Print("OrderSelect 失败错误代码是",GetLastError());
                     
                   }
       if(OrderType()==0){type=9;}
       if(OrderType()==1){type=10;}       
       OrderClose(OrderTicket(),OrderLots(),MarketInfo(OrderSymbol(),type),10,Red);
    }
   }
       ArrayResize(order_id,0);
       ArrayResize(order_expect_close,0); 
       finalcost=AccountEquity();
       OnInit();
   }
}


void static_print()
{
  printf("最大占用保证金:"+Margin[ArrayMaximum(Margin)]);
  printf("最多净值:"+totalmoney[ArrayMaximum(totalmoney)]);
  printf("最多盈利百分之:"+float((totalmoney[ArrayMaximum(totalmoney)]-totalmoney[0])/totalmoney[0]*100));
  printf("最多回撤:"+totalmoney[ArrayMinimum(totalmoney)]); 
  printf("最多回撤百分之:"+float((totalmoney[ArrayMinimum(totalmoney)]-totalmoney[0])/totalmoney[0]*100));  
  printf("最多持仓:"+totallots_test[ArrayMaximum(totallots_test)]);
  printf("最大加仓:"+maxlots()); 
  printf("盘末净值"+AccountEquity());
  printf("成功次数:"+success_sum);
  printf("失败次数:"+fail_sum);
  printf("成功次数-隔天0清理:"+fail_sum2);
  printf("成功次数-自动空仓:"+fail_sum3);}
float maxlots()


{

float max[];

   for(int i=0;i<OrdersHistoryTotal();i++)
    {  int type;
       if(OrderSelect(i,SELECT_BY_POS,MODE_HISTORY)==false)
                   { Print("OrderSelect 失败错误代码是",GetLastError());       }
       ArrayResize(max,ArraySize(max)+1);
       max[ArraySize(max)-1]=float(OrderLots());
    }
   

   return max[ArrayMaximum(max)];
    
}

float totallots()


{

float total=0;
   
 if(OrdersTotal()>0)
   {for(int i=0;i<OrdersTotal();i++)
    {  int type;
       if(OrderSelect(i,SELECT_BY_POS)==false)
                   { Print("OrderSelect 失败错误代码是",GetLastError());       }
       total=total+OrderLots();
     //  printf(OrderLots());
    }
   }

   return total;
    
}

void static_()
{

   ArrayResize(totalmoney,ArraySize(totalmoney)+1);
   totalmoney[ArraySize(totalmoney)-1]=float(AccountEquity());
   ArrayResize(totallots_test,ArraySize(totallots_test)+1);
   totallots_test[ArraySize(totallots_test)-1]=float(totallots());
   ArrayResize(Margin,ArraySize(Margin)+1);
   Margin[ArraySize(Margin)-1]=float(AccountMargin());
}