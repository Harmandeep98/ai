# dict comprehension brief explanation

tea_price_inr = {'tea': 10, 'coffee': 20, 'juice': 30, 'water': 40};

tea_price_usd = {key: value * 0.012 for key, value in tea_price_inr.items()};

print(f"Tea price in USD: {tea_price_usd}");