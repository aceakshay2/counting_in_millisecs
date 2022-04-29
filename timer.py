
import time

sec = 12    
break_time1 = 666
break_time2 = 1500



for i in range(20):
    count_break1 = 0
    count_break2 = 0
    prev = time.time()
    while (time.time()-prev <= sec):
        time.sleep(0.0008)
        diff = int((time.time()-prev)*1000)
        #print(diff)
        
        
        if( diff  % break_time1 == 0):
            count_break1+=1
            #print(diff)
        
        if( diff  % break_time2 == 0):
            count_break2+=1
            #print(diff)
        

    print(f"Expected result for {break_time1} milli sec for {sec} seconds : " ,int(sec*1000/break_time1) , 'Arrived result : '  , count_break1)
    print(f"Expected result for {break_time2} milli sec for {sec} seconds : " ,int(sec*1000/break_time2) , 'Arrived result : '  , count_break2)
    print()


# for i in range(10):
#     check_timer()
# print("Expected result for 500ms : " , int(4000/500) , 'Arrived result : '  , count500)