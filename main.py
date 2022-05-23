#Importações
import pandas as pd
import requests
from termcolor import colored
from unidecode import unidecode
import os


class WeatherForecast:
    def __init__(self) -> None:
        pass
          
    #DataFrame    
    def createDataFrame(self, citySearch):
        try:
            #Requisição
            get_weather = requests.get(f"https://api.hgbrasil.com/weather?key=d2a11df6&city_name={citySearch}")
        
        except Exception as erro:
            print("Ocorreu um erro na requisição da API (╥﹏╥). Entre em contato com o suporte técnico 🔧", erro)

        #Read the JSON, and convert to a DataFrame
        RESPONSE = pd.read_json(get_weather.text)
        self.cityResponse:str = RESPONSE["results"]["city"]
        if unidecode(self.cityResponse.strip().upper()) != unidecode(citySearch.strip().upper()):
            print("Cidade não encontrada! Padrão: São Paulo, SP")
            citySearch = "São Paulo, SP"
        forecastFilter = RESPONSE["results"]["forecast"]       
        self.df = pd.DataFrame.from_dict(forecastFilter)
        self.df.drop(columns=['condition'], inplace=True)
        basedir = os.path.dirname(__file__)
        if os.path.isfile(f"{basedir}/requisicoes.csv"):
            header = False
            
        else:
            header = "index,date,weekday,max,min,description,Data da aquisicao"
        
        with open(f"{basedir}/requisicoes.csv", "a+", encoding="utf-8") as f:
            if header:
                f.write(header + "\n")
            ind = sum(1 for x in open(f"{basedir}/requisicoes.csv", "r")) -1
            print(ind)                   
            for value in forecastFilter:
                ind += 1
                f.write(f"{ind}, {value['date']}, {value['weekday']}, {value['max']}, {value['min']}, {value['description']}, {RESPONSE['results']['date']}\n")
        return self.cityResponse
    
    #Function that returns the weather forecast for a specified date and location.
    
    def dateForecast(self, dateF):
        self.df["localização"] = self.cityResponse
        return self.df.loc[self.df["date"] == dateF]

    #Function that returns the content between two specified dates

    def periodForecast(self, start_date, end_date):
        self.df["localização"] = self.cityResponse
        mask = (self.df['date'] >= start_date) & (self.df['date'] <= end_date)
        resultDf = self.df.loc[mask]
        return resultDf
    
    #Function that allows you to show only the days when the weather will be favorable.

    def perfectWeather(self, pWeather):
        self.df["localização"] = self.cityResponse
        return(self.df.loc[self.df["description"] == pWeather])

#PerfectWeather function menu.
   
def menuPerfWeather(cityResponse):
    print("\n")
    print(colored("█" * 18 + " CLIMA PERFEITO " + "█" * 17, "blue", attrs=["bold"]))
    print(f"Localização: {cityResponse}")
    print("1 - Tempo limpo")
    print("2 - Parcialmente nublado")
    print("3 - Tempo nublado")
    print("4 - Chuvas esparsas")
    print("5 - Chuva")
    print("0 - Voltar para o menu anterior.")
    print(colored("█" * 51, "blue", attrs=["bold"]), "\n")

#Main menu.

def mainMenu(cityResponse):
    print("\n")
    print(colored("█" * 16 + ' PREVISÃO DO TEMPO ' + "█" * 16, "green", attrs=["bold"]))
    print(f"Localização: {cityResponse}")
    print("1 - Previsão por data")
    print("2 - Previsão em um período de tempo")
    print("3 - Clima perfeito")
    print("0 - Sair do programa.")
    print(colored("AVISO: Instruções de uso na documentação", "yellow"))
    print(colored("█" * 51, "green", attrs=["bold"]), "\n")

if __name__ == "__main__":
    
    try:
        while True:
            citySearch = input("\nDigite o nome de uma cidade (Ex: São Paulo, SP): ")
            weather_forecast = WeatherForecast()
            city_response = weather_forecast.createDataFrame(citySearch)
            mainMenu(city_response)

            chooseOption = int(input("\nEscolha uma opção: "))
            
            if chooseOption == 1:
                date_forecast = weather_forecast.dateForecast(str(input("\nDigite uma data: ")))
                print(date_forecast)
            elif chooseOption == 2:
                period_forecast = weather_forecast.periodForecast(str(input("\nDigite uma data: ")), str(input("Digite outra data: ")))
                print(period_forecast)
            elif chooseOption == 3:
                
                while True:
                    menuPerfWeather(city_response)
                
                    chooseClimate = int(input("\nEscolha um clima(Ex: 1): "))
                    
                    if chooseClimate == 1:
                         perfect_weather = weather_forecast.perfectWeather("Tempo limpo")
                    elif chooseClimate == 2:
                        perfect_weather = weather_forecast.perfectWeather("Parcialmente nublado")
                    elif chooseClimate == 3:
                        perfect_weather = weather_forecast.perfectWeather("Tempo nublado")
                    elif chooseClimate == 4:
                        perfect_weather = weather_forecast.perfectWeather("Chuvas esparsas")
                    elif chooseClimate == 5:
                        perfect_weather = weather_forecast.perfectWeather("Chuva")
                    elif chooseClimate == 0:
                        print("Voltando para o menu inicial...")
                        break
                    else:
                        perfect_weather = "Opção inválida! Tente novamente..."
                    print(perfect_weather)

            elif chooseOption == 0:
                print("Fechando o programa...")
                break
            else:
                print("Opção inválida! Tente novamente...")
    except Exception as erro:
        print("Ocorreu um erro (╥﹏╥). Entre em contato com o suporte técnico 🔧", erro)