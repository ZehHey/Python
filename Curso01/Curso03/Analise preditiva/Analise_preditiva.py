import yfinance as yf
from prophet import Prophet
import pandas as pd
import matplotlib.pyplot as mlt
import numpy as nmpi
#from prophet.plot import plot_plotly

ticker = str(input('Digite o código da ação: '))
dados = yf.Ticker(ticker).history('2y')
treinamento = dados.reset_index()
treinamento = treinamento[["Date", "Close"]]
treinamento['Date'] = treinamento['Date'].dt.date
treinamento.columns = ['ds', 'y']

modelo = Prophet()

modelo.fit(treinamento)
periodo = modelo.make_future_dataframe(90)
previsoes = modelo.predict(periodo)
print(previsoes[['ds', 'yhat']].head)

"""ypoints = nmpi.array([treinamento["Date"]])
mlt.plot(modelo, previsoes)
mlt.show()"""

#print(plot_plotly(modelo, previsoes))
