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
# Runtime
![image](https://user-images.githubusercontent.com/87345979/210131128-a7b7ddbb-0bc7-4745-8ce5-1bb70a0e1e0b.png)

# Memory
![image](https://user-images.githubusercontent.com/87345979/210131145-fa04b403-b4e3-4974-b24b-e3a3b7a0d60b.png)
