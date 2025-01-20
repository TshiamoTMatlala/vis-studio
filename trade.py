import random
import numpy as np
import time

class StockBot:
    def __init__(self, initial_balance=10000, moving_average_window=5):
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.stocks = 0
        self.stock_price_history = []
        self.moving_average_window = moving_average_window
        self.steps = 0  # Track the number of steps

    def generate_dummy_stock_price(self):
        return round(random.uniform(50, 150), 2)

    def calculate_moving_average(self):
        if len(self.stock_price_history) < self.moving_average_window:
            return None
        return np.mean(self.stock_price_history[-self.moving_average_window:])

    def buy_stock(self, price):
        max_stocks_to_buy = int(self.balance / price)
        stocks_to_buy = random.randint(1, max_stocks_to_buy)
        cost = price * stocks_to_buy
        self.balance -= cost
        self.stocks += stocks_to_buy
        print(f"Buying {stocks_to_buy} stocks at ${price:.2f}. Balance: ${self.balance:.2f}")

    def sell_stock(self, price):
        stocks_to_sell = self.stocks
        revenue = price * stocks_to_sell
        self.balance += revenue
        self.stocks = 0
        print(f"Selling all {stocks_to_sell} stocks at ${price:.2f}. Balance: ${self.balance:.2f}")

    def trade(self, stock_price):
        self.stock_price_history.append(stock_price)
        self.steps += 1  # Increment the number of steps

        moving_average = self.calculate_moving_average()
        if moving_average is not None and stock_price < moving_average:
            self.buy_stock(stock_price)
        elif moving_average is not None and stock_price > moving_average:
            self.sell_stock(stock_price)

def simulate_stock_market(bot, num_steps=100, sell_stocks_after=35):
    print(f"Initial Balance: ${bot.initial_balance:.2f}")
    for step in range(1, num_steps + 1):
        stock_price = bot.generate_dummy_stock_price()
        bot.trade(stock_price)
        time.sleep(1)
        if bot.steps == sell_stocks_after:
            print(f"\nSell all stocks after {sell_stocks_after} steps.")
            bot.sell_stock(stock_price)
            break
    print(f"\nSimulation completed after {num_steps} steps.")
    print(f"Final Balance: ${bot.balance:.2f}")

if __name__ == "__main__":
    trading_bot = StockBot()
    simulate_stock_market(trading_bot, num_steps=40, sell_stocks_after=35)
