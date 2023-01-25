
x = int(input())
count_hour = 0
count_min = 0
count_sec = 0
total_count = 0

while count_hour < x:
  while count_min < 60:
    while count_sec < 60:
      current_time = f"{count_hour}:{count_min}:{count_sec}"
      current_string_time = list(str(current_time))
      if "3" in current_string_time:
        print(current_string_time)
        total_count += 1
      count_sec += 1
    count_sec = 0
    count_min += 1
  count_min = 0
  count_hour += 1
print(total_count)
      




    
    # if count_min % 3 == 0:
    #   total_count += 1

    # else:
    #   while count_sec < 60:
    #     if count_sec % 3 == 0:
    #       total_count +=1
          


    