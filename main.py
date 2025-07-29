import random
import time
import matplotlib.pyplot as plt

class BidAskQuoter:
    def __init__(self, symbol, base_price):
        self.symbol = symbol
        self.mid_price = base_price
        self.spread = 0.05
        self.history = {"mid": [], "bid": [], "ask": [], "time": []}
        self.update_quote()

    def update_quote(self):
        self.bid = round(self.mid_price - self.spread / 2, 2)
        self.ask = round(self.mid_price + self.spread / 2, 2)

    def simulate_market_move(self):
        change = random.uniform(-1, 1)
        self.mid_price += change
        self.mid_price = round(self.mid_price, 2)
        self.update_quote()

    def record(self, t):
        self.history["time"].append(t)
        self.history["mid"].append(self.mid_price)
        self.history["bid"].append(self.bid)
        self.history["ask"].append(self.ask)


quoter = BidAskQuoter("NIFTY FUTURES", 22500.0)
num_points = 10000
refresh_interval = 0.1  


plt.ion()
fig, ax = plt.subplots()
line_mid, = ax.plot([], [], label="Mid", color='blue')
line_bid, = ax.plot([], [], label="Bid", color='green')
line_ask, = ax.plot([], [], label="Ask", color='red')
ax.set_title("Live Bid-Ask Quoter")
ax.set_xlabel("Time")
ax.set_ylabel("Price")
ax.legend()


for t in range(num_points):
    quoter.simulate_market_move()
    quoter.record(t)

    line_mid.set_data(quoter.history["time"], quoter.history["mid"])
    line_bid.set_data(quoter.history["time"], quoter.history["bid"])
    line_ask.set_data(quoter.history["time"], quoter.history["ask"])
    ax.relim()
    ax.autoscale_view()

    plt.pause(refresh_interval)

plt.ioff()
plt.show()
