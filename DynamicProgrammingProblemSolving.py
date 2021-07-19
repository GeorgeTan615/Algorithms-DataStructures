"Name: George Tan Juan Sheng"
"Student_ID: 30884128"


def get_start_week(income:tuple) -> int:
    """
    This function takes a tuple of 3 elements and returns the first value of the tuple.

    Time complexity: Best and worst case is O(1).
    Explanation: Tuples has constant time access hence runs at constant time.

    Auxiliary-space complexity: Best and worst case is O(1).
    Explanation: This function is an in place function and does not require additional space.

    Space-complexity: Input + auxiliary 
                    : O(1) + O(1)
                    : O(1)
    """
    return income[0]

def best_schedule(weekly_income:list, competitions:list) -> int:
    """
    This function a list of non negative integers, weekly_income and a list of tuples, competitions and returns the 
    maximum amount of money that can be earned throughout the weeks.
    
    Pre-cond: weekly_income is a list of non-negative integers, where weekly_income[i] is the amount of 
    money you will earn working as a personal trainer in week i. competitions is a list of tuples, each representing
    a sporting competition. Each tuple contains 3 non-negative integers, (start_time, end_time, winnings).

    Post-cond: This function returns an integer, which is the maximum amount of money that can be earned.

    Time complexity: Best and worst case is O(N log N), where N is the total number of elements in weekly_income and competitions put together.
    Explanation: O(N + N log N + N)
               : O(N (loop through weekly_income to add values into income_options) + 
                 N (loop through competitions to add each item in competitions into income_options) +
                 N log N (sort income_options based on each tuple's start week) + 
                 N (loop through sorted income options to fill out memo))
               : O(N log N)

    Auxiliary-space complexity: O(N), where N is the total number of elements in weekly_income and competitions put together.
    Explanation: We would be creating a list of size N. This list is to input the values of weekly_income in the form
                 of a tuple including its start week and end week and also add the competitions list into this list.

    Space-complexity: Input + Auxiliary-space
                    : O(N) + O(N)           (where N is the total number of elements in weekly income and competitions put together.)
                    : O(2N)
                    : O(N)
    """
    if weekly_income ==[]:
        return 0 

    memo = [None]*(len(weekly_income)+1)
    memo[0] = 0                                                         #initializing base case
    income_options = []
    for i in range(len(weekly_income)):
        income_options.append((i,i,weekly_income[i]))                   #convert items in weekly_income to the format as in competitions
    
    for item in competitions:
        income_options.append(item)                                     #add competitions into the income_options list
    sorted_income_options = sorted(income_options,key=get_start_week)   #sort income_options based on start week 

    for item in sorted_income_options:
        if memo[item[1]+1] is None:                                                 
            memo[item[1]+1] = item[2] + memo[item[0]]                   #if memo[end_week] is none, add current income + memo[start_week-1] (which stores optimal income at start_week-1)
        else:
            if item[2] + memo[item[0]] > memo[item[1]+1]:               #compare if current income + memo[start_week-1] is bigger than memo[end_week]
                memo[item[1]+1] = memo[item[0]] + item[2]
        

    return memo[-1]

def get_exclude_value(day:int,city:int,memo:list,num_cities:int) -> int:
    """
    This function takes day,city,memo and num_cities and returns the maximum profit that will be gotten
    if the profit of input city is excluded at the input day. This function looks at memo[day-1][city-1] and memo[day-1][city+1]
    and extracts the maximum value from the two memo's tuple value.

    Post-cond:The function returns an integer, which is the maximum amount of money that can be earned at input city at input day 
              if the profit gained at the input city at input day is excluded.
    
    Time-Complexity: Best and worst case is O(1)
    Explanation: The function runs at constant time.

    Auxiliary-Space complexity: O(1)
    Explanation: The function always creates a list of at most 2 elements, hence it is of constant space.

    Space Complexity : Input + auxiliary
                     : O(nd) + O(1), where n is the number of cities and d is the number of days (number of interior lists in profit) 
                     : O(nd)          
    """

    res = []
    top_left_city = city-1      #when obtaining exclude value, we would just need to look at the top left and top right's values in our memo, which are memo[day-1][city-1] and memo[day-1][city+1]. We would then take the biggest value out of the two tuples
    top_right_city = city +1

    if top_left_city < 0:
        res.append(0)
    else:
        res.append(max(memo[day-1][top_left_city]))

    if top_right_city >= num_cities:
        res.append(0)
    else:
        res.append(max(memo[day-1][top_right_city]))
    return max(res)

def best_itinerary(profit:list,quarantine_time:list,home:int) -> int:
    """
    This function takes a list of list called profit,where profit[d][c] is the profit that the
    salesperson will make by working in city c on day d, and a list of non-negative integers called 
    quarantine_time where quarantine_time[i] is the number of days city i requires visitors to quarantine
    before they can work there and a home where the person starts at. This function will then return 
    an integer, which is the maximum amount of money that can be earned by the salesperson.

    Pre-cond: quarantine_time is a list of non-negative integers. home is an integer 
              between 0 and n-1 inclusive, which represents the city that the salesperson 
              starts in.
    Post-cond:The function returns an integer, which is the maximum amount of money that can 
              be earned by the salesperson. 
    
    Time-Complexity: Best and worst case is O(nd), where n is the number of cities and d is the number of days (number of interior lists in profit)
    Explanation: O(nd(creating initial values for memo) +n(initialing day 0 to tuples of (0,0) as base case)+nd(looping through memo to fill in values in memo)
                 +n(loop through last day results in memo to get final answer)) 
               : O(2nd +2n)
               : O(nd)

    Auxiliary-Space complexity: O(nd), where n is the number of cities and d is the number of days (number of interior lists in profit)
    Explanation: O(nd(space for creating memo) +n(space for creating res))
               : O(nd)

    Space Complexity : Input + auxiliary
                     : O(nd) + O(nd), where n is the number of cities and d is the number of days (number of interior lists in profit)
                     : O(2nd)
                     : O(nd)

    """
    if profit == [] or quarantine_time == []:
        return 0 

    memo = [[(None,None)] * len(quarantine_time) for i in range(len(profit)+1)]     
    for i in range(len(memo[0])):
        memo[0][i] = (0,0)                                                          #set all values in day 0 to (0,0) as base case
    num_cities = len(quarantine_time)

    #this block of code is basically to calculate the profit we can get if we decide to include and exclude the current city's profit at the current day
    for day in range(1,len(memo)):
        for city in range(num_cities):
            if day == 1 and city == home:                                       #this is to accomodate the case where we are at the first day at our home
                reach_day = 0
            else:                                                                   
                reach_day = day - 1 - quarantine_time[city]

            realistic_reach_day = abs(city-home)
            
            if realistic_reach_day <= reach_day:                                #this is to test if it is possible to reach the city at the respective day from home at day 0 
                value1 = memo[reach_day][city][1] + profit[day-1][city]
            else:
                value1 = 0
            
            if memo[day-1][city][0] == 0:                                       #if previous day's include value is 0, we would need to check if currently if we are still in quarantine 
                difference = abs(city-home)-1
                day2 = day - 1 - quarantine_time[city]-difference
                if day2 <= 0 :      
                    value2 = 0 
                else:
                    value2 = memo[day-1][city][0] + profit[day-1][city]         #add previous day's include value of profit with today's profit
                    
            else:
                value2 = memo[day-1][city][0] + profit[day-1][city]             #if previous day's include value is not 0, add previous day's include value with today's profit directly

            include_value = max(value1,value2)
            exclude_value = get_exclude_value(day,city,memo,num_cities)
            memo[day][city] = (include_value,exclude_value)                     #store the profit if we were to include and exclude the current city's profit at the current day as a tuple in memo

    res = []
    for item in memo[-1]:
        res.append(max(item))
    return max(res)                                                                 #iterate through all of last day's include and exclude values and get the biggest number



            









