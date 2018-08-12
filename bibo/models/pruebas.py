import datetime
import time
import locale

locale.setlocale(locale.LC_ALL, 'es_MX.UTF-8')
x=datetime.date.today()
#fech = '2017-01-31 00:00:00'
#x = datetime.strptime(fech, '%Y-%m-%d %H:%M:%S').date()
week = x.isocalendar()[1]
print("fecha")
print(x)
#dicdias = {'MONDAY': '1', 'TUESDAY': '2', 'WEDNESDAY': '3', 'THURSDAY': '4', \
#           'FRIDAY': '5', 'SATURDAY': '6', 'SUNDAY': '7'}
#dicdias2 = {'MONDAY': '7', 'TUESDAY': '6', 'WEDNESDAY': '5', 'THURSDAY': '4', \
#            'FRIDAY': '3', 'SATURDAY': '2', 'SUNDAY': '1'}
dicdias = {'MONDAY': '5', 'TUESDAY': '6', 'WEDNESDAY': '7', 'THURSDAY': '1','FRIDAY': '2', 'SATURDAY': '3', 'SUNDAY': '4','JUEVES': '1', 'VIERNES': '2', 'S\xc3\xa1BADO': '3','DOMINGO': '4','LUNES': '5', 'MARTES': '6', 'MI\xc3\xa9RCOLES': '7'}
dicdias2 = {'MONDAY': '3', 'TUESDAY': '2', 'WEDNESDAY': '1', 'THURSDAY': '7','FRIDAY': '6', 'SATURDAY': '5', 'SUNDAY': '4','JUEVES': '7', 'VIERNES': '6', 'S\xc3\xa1BADO': '5','DOMINGO': '4','LUNES': '3', 'MARTES': '2', 'MI\xc3\xa9RCOLES': '1'}
#dicdias = {'JUEVES': '1', 'VIERNES': '2', 'SABADO': '3','DOMINGO': '4','LUNES': '5', 'MARTES': '6', 'MIERCOLES': '7'}
#dicdias2 =  {'JUEVES': '7', 'VIERNES': '6', 'SABADO': '5','DOMINGO': '4','LUNES': '3', 'MARTES': '2', 'MIERCOLES': '1'}
anho = x.year
mes = x.month
dia = x.day
fecha = datetime.date(2018, 8, 4)
noweek = dicdias[fecha.strftime('%A').upper()]
print(fecha.strftime('%A').upper())