class RomanNumerals:
    def __init__(self, value):
        self.value = value
    def to_roman(self):
        roman_numerals = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        roman_numeral = ""
        for numeral, value in roman_numerals.items():
            while self.value >= value:
                roman_numeral += value
                self.value -= value
        return roman_numeral
    def to_integer(self):
        roman_numerals = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }
        integer = 0
        for numeral, value in roman_numerals.items():
            while self.value.startswith(numeral):
                integer += value
                self.value = self.value[len(numeral) :]
        return integer
roman_numerals = RomanNumerals(123)
print(roman_numerals.to_roman())  
roman_numerals = RomanNumerals("CXXIII")
print(roman_numerals.to_integer())