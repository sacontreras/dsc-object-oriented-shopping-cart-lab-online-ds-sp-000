class ShoppingCart:
   # write your code here
   def __init__(self, employee_discount=None):
      self.employee_discount = employee_discount
      self.total = 0
      self.items = []
      print(f"items is {self.items}")

   def add_item(self, name, price, quantity=1):
      self.items.append({
         'name': name,
         'price': price,
         'quantity': quantity
      })
      self.total += quantity * price
      return self.total

   def mean_item_price(self):
      mean_price = 0
      for _, item in enumerate(self.items):
         mean_price += item['price']
      print(f"sum of prices: {mean_price}")
      print(f"item count: {len(self.items)}")
      mean_price /= len(self.items)
      print(f"mean price: {mean_price}")
      return mean_price

   def median_item_price(self):
      prices = []
      for _, item in enumerate(self.items):
         prices.append(item['price'])
      prices = sorted(prices)
      print(f"prices: {prices}")
      l = len(prices)
      if l % 2 == 0:
         median = prices[int(l/2)-1]
      else:
         median = prices[int(l/2)]
      print(f"median price: {median}")
      return median

   def apply_discount(self):
      discount_factor = 1
      if self.employee_discount is not None:
         discount_factor = 1 - (self.employee_discount/100)
      else:
         print("Sorry, there is no discount to apply to your cart :(")
      return self.total * discount_factor

   def void_last_item(self):
      print(f"items before removing last item: {self.items}\n")
      print(f"total before removing last item: {self.total}\n")
      if len(self.items) > 0:
         removed_item = self.items.pop(-1)
         print(f"items after removing last item: {self.items}")
         print(f"item removed: {removed_item}\n")
         st_removed = removed_item['price'] * removed_item['quantity']
         print(f"subtotal of removed item: {st_removed}")
         self.total -= st_removed
      else:
         return "There are no items in your cart!"