# from datetime import date -> importa a biblioteca especifica 
# import datetime -> importa toda biblioteca

from datetime import date, datetime,time

data = date (2023, 7, 19)
print(data) #2023-07-19
print(date.today()) #data de hoje

#Data e Hora
data_hora = datetime(2024, 8, 5, 5, 30, 20)
print(data_hora)
print(datetime.today()) #data e hora atual

#hora
hora = time(10, 20 , 0)
print(hora)

