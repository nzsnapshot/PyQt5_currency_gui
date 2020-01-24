
import requests
import json
 

class Api:
    def __init__(self):
        super().__init__()
        # self.extract()
        # self.converting()
        self.filename1 = 'Currency_gui\\curr.json'
        self.filename2 = 'Currency_gui\\curr2.json'
        self.valuesload = 'Currency_gui\\values.json'
        with open (self.filename1) as f:
            self.curr = json.load(f)
        with open (self.filename2) as f:
            self.curr2 = json.load(f)
        with open (self.valuesload) as f:
            self.values = json.load(f)

#         self.amount = 120
#         self.froms = 'NZD'
#         self.to = 'USD'
    
#         self.urls = f"https://openexchangerates.org/api/convert/{self.amount}/{self.froms}/{self.to}?app_id=1f39967fe6e9470bb9fbb937967ca3ae"
#         print(self.urls)
#     def extract(self):
#         self.base = input("Convert from: ").upper()
#         self.url = "http://data.fixer.io/api/latest?access_key=70b4fceb11a507986db482d8eaea3631&format=1"
#         response = requests.get(self.url) 
#         self.data = response.text 
#         self.parsed = json.loads(self.data) 
#         self.rates = self.parsed["rates"]
#         self.values = []
#         for k in self.parsed.items():
#             self.values.append(k)
        
#         # If I need to recreate a json with all the currencies
#         with open('values.json', 'w') as f:
#             json.dump(self.values, f, indent=4, sort_keys=True)

#     def converting(self):
#         self.to = input("Convert to: ").upper()
#         self.amount = float(input("Amount: "))
#         for self.currency, self.rate in self.rates.items():
#             if self.currency == self.to:
#                 self.conversion = self.rate * self.amount
#                 print("1", self.base, "=", self.currency, self.rate)
#                 print(self.amount, self.base, "=", self.currency, self.conversion)


# i = Api()
# i
# print(i.values[0][0])