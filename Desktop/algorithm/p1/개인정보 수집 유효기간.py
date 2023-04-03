terms = ["A 6", "B 12", "C 3"]
today = "2022.05.19"
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]



import datetime

each_term = {term[0]:int(term[2:]) for term in terms} #{'A': 6, 'B': 12, 'C': 3}

def con_date(date):
    return datetime.datetime.strptime(date, '%Y.%m.%d')

con_today = con_date(today)
print(con_today)
#expire_date = con_date(날짜입력).replace(month=날짜입력.month + 딕셔너리value)

#print(today.replace(month=today.month+11))

print(list(filter(lambda x: con_date(x[:10]).replace(month=con_date(x[:10]).month + each_term[x[-1]])- datetime.timedelta(days=1) if con_date(x[:10]).month + each_term[x[-1]] <= 12 else
                    con_date(x[:10]).replace(year=con_date(x[:10]).year+1,  month=con_date(x[:10]).month + each_term[x[-1]]-12)- datetime.timedelta(days=1) < con_today ,privacies)) )


print(list(map(lambda x: con_date(x[:10]).replace(month=con_date(x[:10]).month + each_term[x[-1]])- datetime.timedelta(days=1) if con_date(x[:10]).month + each_term[x[-1]] <= 12 else
                    con_date(x[:10]).replace(year=con_date(x[:10]).year+1,  month=con_date(x[:10]).month + each_term[x[-1]]-12)- datetime.timedelta(days=1)  ,privacies)))


#[privacies.index(x)+1  for x in privacies con_date(x[:10]).replace(month=con_date(x[:10]).month + each_term[x[-1]]) if con_date(x[:10]).month + each_term[x[-1]] <= 12 else con_date(x[:10]).replace(year=con_date(x[:10]).year+1,  month=con_date(x[:10]).month + each_term[x[-1]]-12) <= today]


print(datetime.datetime(2022, 5, 18, 0, 0) < con_today)
print(datetime.datetime(2021, 11, 1, 0, 0) < con_today)