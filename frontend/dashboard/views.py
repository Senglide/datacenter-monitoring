from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
import datetime

from django.views.decorators.csrf import csrf_exempt
from django_eventstream import send_event
from .models import Rack_1, Rack_2, Rack_3

# Data prediction test
import pandas as pd
from pandas import datetime as pd_datetime
from statsmodels.tsa.arima_model import ARIMA

# Index page
def index(request):
    return render(request, 'dashboard/index.html')

# Grid testing page
def detail(request):
    return render(request, 'dashboard/detail.html')

# Get newest readings
def get_newest_readings(request, rack, s_type, amount):
    dbRack = get_rack(rack)
    readings = dbRack.objects.filter(sensor_type=s_type).order_by('-_id')[:amount]
    return JsonResponse(format_readings(readings))

# Get readings based on date
def get_readings_by_date(request, rack, s_type, r_date):
    date = datetime.datetime.strptime(r_date, '%d-%m-%Y').date()
    dbRack = get_rack(rack)
    readings = dbRack.objects.filter(sensor_type=s_type).filter(date__contains=date).order_by('time').reverse()
    return JsonResponse(format_readings(readings))

def get_rack(rack):
    return {
        '1': Rack_1,
        '2': Rack_2,
        '3': Rack_3
    }[str(rack)]

def format_readings(readings):
    data = []
    predictions = []
    for reading in readings:
        formatted_reading = {
            'id': str(reading._id),
            'sensor_value': reading.sensor_value,
            'date': reading.date,
            'time': reading.time
        }
        data.append(formatted_reading)
        predictions.append(formatted_reading)

    return {'readings': data, 'predictions': predictions}

# Alarm api link
@csrf_exempt
def alarm(request, alarm):
    send_event('alarmChannel', 'message', {'alarm': alarm})
    return JsonResponse({})

# Data prediction test
# today = str(datetime.datetime.now().date())
# readings = Rack_1.objects.filter(sensor_type='temp').filter(date__contains=today).order_by('time').reverse()
# if(readings):
#     index_data = []
#     sensor_data = []
#     for reading in readings:
#         index_data.insert(0, pd_datetime.strptime(reading.date + ' ' + reading.time, '%Y-%m-%d %H:%M:%S.%f'))
#         sensor_data.insert(0, reading.sensor_value)
#     last_index_data = index_data[-90:]
#     last_sensor_data = sensor_data[-90:]
#     predict_index = pd.date_range(last_index_data[0], periods=60, freq='10S')
#     predict_series = pd.Series(last_sensor_data[0:60], index=predict_index)
#     df = pd.DataFrame({'sensor_value': predict_series})
#     model = ARIMA(df, order=(1, 0, 1))
#     model_fit = model.fit()

#     import itertools
#     p = range(1, 31)
#     d = q = range(0, 6)
#     pdq = list(itertools.product(p, d, q))
#     aic = 1000000
#     results = []
#     i = 0
    
#     for param in pdq:
#         print('working on param ' + str(i) + ' of ' + str(len(pdq)))
#         i += 1
#         try:
#             model = ARIMA(df, order=(param))
#             model_fit = model.fit()
#             model_aic = model_fit.aic
#             if(model_aic < aic):
#                 aic = model_aic
#                 results.append([param, aic])
#         except:
#             continue

#     print(results)

#     print('aic: ' + str(model_fit.aic))
#     predictions = model_fit.forecast(steps=30)
#     print(predict_series[:30])
#     print(predictions)
#     df = pd.DataFrame(data=r_data, columns=['Datetime', 'Sensor_value'])
#     df = df.set_index('Datetime')
#     df = df.asfreq(freq='10S')
#     X = df[:90].Sensor_value
#     train = X[0:60]
#     test= X[:30]
#     import itertools
#     p=d=q=range(0,30)
#     pdq = list(itertools.product(p,d,q))
#     aic = 1000000
#     results = []
#     for param in pdq:
#         try:
#             model = ARIMA(train, order=(param))
#             model_fit = model.fit()
#             if(model_fit.aic < aic):
#                 aic = model_fit.aic
#                 results.append([param, aic])
#         except:
#             continue

#     print(results)

    
#     print(pdq)
#     print(predictions[0])
#     print(predictions)
#     print(df.head(5))
#     print(df.index)
#     print(type(df.index))
#     p = d = q = range(0, 2)
#     pdq = list(itertools.product(p, d, q))
#     seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]