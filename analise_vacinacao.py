# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 13:34:22 2023

Análise da situação da vacinação de covid-19 global

@author: Gabriel Ratão
"""

#%% importação das bibliotecas
import pandas as pd
import matplotlib.pyplot as plt


#%%importando a base de dados
df_total_vacidanos = pd.read_csv(r"C:\Users\User\Documents\Python\vacinacao\analise_vacinacao\people-fully-vaccinated-covid (1)_atualizado.csv")
display(df_total_vacidanos)




#%%obtendo valores de cada país  NUMERO TOTAL DE PESSOAS VACINADAS

for i, v in enumerate(df_total_vacidanos["Entity"]):
    if v == "Brazil":
        brasil = df_total_vacidanos["people_fully_vaccinated"][i]
    elif v == "United States":
        eua = df_total_vacidanos["people_fully_vaccinated"][i]
    elif v == "Israel":
        israel = df_total_vacidanos["people_fully_vaccinated"][i]
    elif v == "Russia":
        russia = df_total_vacidanos["people_fully_vaccinated"][i]
    elif v == "Germany":
        alemanha = df_total_vacidanos["people_fully_vaccinated"][i]
    elif v == "Argentina":
        argentina = df_total_vacidanos["people_fully_vaccinated"][i]
    elif v == "United Arab Emirates":
        arabe = df_total_vacidanos["people_fully_vaccinated"][i]
    elif v == "United Kingdom":
        uk = df_total_vacidanos["people_fully_vaccinated"][i]
    
print(f'brasil: {brasil:2f}')
print(f'eua: {eua:2f}')
print(f'israel: {israel:2f}')
print(f'russia: {russia:2f}')
print(f'alemanha: {alemanha:2f}')
print(f'argentina: {argentina:2f}')
print(f'Arabe: {arabe}')
print(uk)

#%%criando as figuras


#Número total de pessoas vacindas com duas doses

cor = ('FireBrick', 'MediumBlue', 'LimeGreen', 'Gold', "Green", 'LightSteelBlue',"Purple", 'Pink')
paises = ('Eua', 'Israel', 'Brasil', 'Alemanha',"Emirados\n Arabes", 'Russia',"Reino\nUnido", 'Argentina')
valores = (eua, israel, brasil, alemanha, arabe, russia, uk, argentina)

# Create horizontal bar plot here
plt.barh(paises, valores, color = cor)

#plt.figure(figsize=(10, 2))

plt.xticks([eua], [f'{(eua / 1000000 ):.2f} milhões'])
for i in range(len(valores)): #valores ao lado da barra
    
    valor = (valores[i]) / 1000000
    if i < len(valores) - 1:
        plt.annotate((f'{valor:.2f} milhões'), xy=(valores[i] + 4000000, paises[i]), ha='center', va='bottom') #va muda a posião do valor ao lado da barra
    
plt.title("Número total de pessoas vacinadas (2 doses) por país")
plt.grid()
plt.show()





#%%importando dados sobre a porcentagem da população vacianda desses mesmos países
df_parcela_vacinada = pd.read_csv(r"C:\Users\User\Documents\Python\vacinacao\analise_vacinacao\share-people-fully-vaccinated-covid_ATUALIZADO.csv")
display(df_parcela_vacinada)


#%%obtendo valor de cada país
for i, v in enumerate(df_parcela_vacinada["Entity"]):
    if v == "Brazil":
        p_brasil = df_parcela_vacinada["people_fully_vaccinated_per_hundred"][i]
    elif v == "United States":
        p_eua = df_parcela_vacinada["people_fully_vaccinated_per_hundred"][i]
    elif v == "Israel":
        p_israel = df_parcela_vacinada["people_fully_vaccinated_per_hundred"][i]
    elif v == "Russia":
        p_russia = df_parcela_vacinada["people_fully_vaccinated_per_hundred"][i]
    elif v == "Germany":
        p_alemanha = df_parcela_vacinada["people_fully_vaccinated_per_hundred"][i]
    elif v == "Argentina":
        p_argentina = df_parcela_vacinada["people_fully_vaccinated_per_hundred"][i]
    elif v == "United Arab Emirates":
        p_arabe = df_parcela_vacinada["people_fully_vaccinated_per_hundred"][i]
    elif v == "United Kingdom":
        p_uk = df_parcela_vacinada["people_fully_vaccinated_per_hundred"][i]
    
print(f'brasil: {p_brasil:2f}')
print(f'eua: {p_eua:2f}')
print(f'israel: {p_israel:2f}')
print(f'russia: {p_russia:2f}')
print(f'alemanha: {p_alemanha:2f}')
print(f'argentina: {p_argentina:2f}')
print(f'Arabe: {p_arabe}')
print(p_uk)




#%%criando a figura

paises = ('Israel', 'Emirados\nArabes', 'Eua', 'Alemanha', 'Reino Unido', 'Russia', 'Brasil', 'Argentina')
valores = (p_israel, p_arabe, p_eua, p_alemanha, p_uk, p_russia, p_brasil, p_argentina)
cor = ('MediumBlue', 'Green', 'FireBrick', 'Gold', "Purple", 'LightSteelBlue', 'LimeGreen', 'Pink')


plt.barh(paises, valores, color = cor)


plt.xticks([p_israel, p_eua, p_brasil, p_arabe], [f'{p_israel}%\nIsrael', f'{p_eua}%\nEUA', f'{p_brasil}%\nBrasil', f'{p_arabe}%\nEmirados\nArabes'])
#aqui coloca os valores no eixo X
#for i in range(len(valores)):
    
    
    
    #plt.annotate((f'{valores[i]}%'), xy=(valores[i], paises[i]), ha='center', va='bottom')

plt.title("Porcentagem da população vacinada (com duas doses) em cada país")
plt.grid()
plt.show()





#%%



























