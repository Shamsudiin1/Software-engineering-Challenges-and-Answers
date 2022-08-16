# enter the starting range number
start_num = int(29)

# enter the ending range number
end_num = int(36)
  
# initialise counter with starting number
cnt = start_num
  
# check until end of the range is achieved
while cnt <= end_num:
    
    # if number divisible by 7 and 5
    if cnt % 7 == 0 and cnt % 5 == 0:
        print(cnt, " is divisible by 7 and 5.")
          
    # increment counter
    cnt += 1