# LeetCode_ConvertTemperature
Solution to LeetCode Problem 2469-Convert the Temperature

![image](https://user-images.githubusercontent.com/87345979/210131016-c098d830-49e8-4d96-91bb-226d406c46f7.png)
![image](https://user-images.githubusercontent.com/87345979/210131032-a3140e32-5636-4c48-87fb-a705c989cf2c.png)

# My Solution
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
