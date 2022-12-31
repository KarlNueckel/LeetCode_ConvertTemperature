class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.8 + 32]

    
""""
Solution that is easier to understand
def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.8 + 32


        return [kelvin, Fahrenheit]
"""""
