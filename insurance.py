def main():
    file = open('input.txt', 'r')
    months_in_year = {1:"31", 2:"28", 3:"31", 4:"30", 5:"31", 6:"30", 7:"31", 8:"31", 9:"30", 10:"31", 11:"30", 12:"31"}
    days_in_policy = 0
    monthEarned = []
    amountEarned = []

    for i in file:
        
        info = i.split(',') # info = (PN, start_date, end_date, premium)
        s_date = list(map(int, info[1].split('/'))) # start date
        e_date = list(map(int, info[2].split('/'))) # end date
        days_in_policy = days_left_in_year(s_date, e_date, months_in_year)

        amountEarned = amount_earned(int(info[3]), days_in_policy, s_date, e_date, months_in_year)
        monthEarned = months_left_in_year(s_date, e_date)

        output(info[0], amountEarned, monthEarned)

    file.close()


def is_it_a_leap(year):
    leap = False
    if ((year % 4 == 0) & ((year % 100 != 0) | (year % 400 == 0))):# if current year is a leap year
        leap = True
    return leap

# Assuming a policy is no longer than a year (not including leap years), and
# that at the longest it ends and starts on the same date
def days_left_in_year(start, end, months):
    day = 0
    start_m = start[0]
    leap = is_it_a_leap(start[2])
    

    if (start[0] == end[0]) & (start[1] == end[1]): # if policy starts and ends on the same date, assuming it ends the following year
        day += 365
        if(start[0] <= 2) & leap: #if policy starts on or before Feb, on a leap year, then +1 day
            day += 1
        return day
    
    # if policy is less than a year
    day += int(months[start_m]) - (start[1] - 1)
    if (start_m < end[0]): # if policy is less than a year, starts and ends in the same year
        if (start_m <= 2) & (leap):
            day += 1
        for i in range(start_m + 1, end[0]):
            day += int(months[i])
    else: #else if policy is less than a year, but starts and ends in different years
        for i in range(start_m + 1, 13):
            day += int(months[i])
        for i in range(1, end[1]):
            day += i(months[i])
        day += int(months[end[0]]) - (end[1] - 1)
    return day


def amount_earned(premium, d, start, end, months):
    premium_per_day = premium / d
    amount = []
    leap = is_it_a_leap(start[2])

    start_month = start[0]
    start_day = start[1]
    days = (int(months[start_month]) - (start_day - 1))
    if (start_month == 2) & (leap):
        days += 1

    amount_earned = premium_per_day * days

    num = round(amount_earned, 2)
    amount.append("$ " + str(num))
    # if the policy starts AND ends on the same year
    if (start[2] == end[2]):  
        for i in range(start_month + 1, end[0]):
            if (i == 2) & leap:
                amount_earned = premium_per_day * (int(months[i]) + 1)
            else:
                amount_earned = premium_per_day * int(months[i])
            num = round(amount_earned, 2)
            #print(num)
            amount.append("$ " + str(num))
    # else if the policy ends on a different year
    else:   
        for i in range(start_month + 1, 13):
            if (i == 2) & leap:
                amount_earned = premium_per_day * (int(months[i]) + 1)
            else:
                amount_earned = premium_per_day * int(months[i])            
            num = round(amount_earned, 2)
            amount.append("$ " + str(num))
    return amount



def months_left_in_year(s_date, e_date):
    m = []
    s = str(s_date[2])
    if s_date[2] < e_date[2]:   # if start year < end year
        for i in range(int(s_date[0]), 13):
            m.append(s + " " + str(i))
    else:
        for i in range(int(s_date[0]), int(e_date[0]) + 1):
            m.append(s + " " + str(i))
    return m


def output(pn, amountEarned, monthEarned):
    title = ['policyNumber', 'monthEarned', 'amountEarned']
    print("\n{0:20} {1:20} {2:20}".format('policyNumber', 'monthEarned', 'amountEarned'))
    for i in range(len(amountEarned)):
        print("{0:20} {1:20} {2:20}".format(pn, monthEarned[i], amountEarned[i]))
    print("\n")

main()