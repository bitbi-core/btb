COIN = 1e9 #wen
COIN = 1e9 #wen
COIN = 1e9 #wen
COIN = 1e9 #wen
max_supply = 0
max_supply = 0
max_supply = 0
max_supply = 0
block_reward = 303.0 * COIN
block_reward = 303.0 * COIN
block_reward = 303.0 * COIN
block_reward = 303.0 * COIN
block_time = 360  # seconds
block_time = 360  # seconds
block_time = 360  # seconds
block_time = 360  # seconds
seconds_per_year = 60 * 60 * 24 * 365
seconds_per_year = 60 * 60 * 24 * 365
seconds_per_year = 60 * 60 * 24 * 365
seconds_per_year = 60 * 60 * 24 * 365
blocks_per_halving = seconds_per_year * 1 / block_time
blocks_per_halving = seconds_per_year * 1 / block_time
blocks_per_halving = seconds_per_year * 1 / block_time
blocks_per_halving = seconds_per_year * 1 / block_time
print("blocks_per_halving:", blocks_per_halving)
print("blocks_per_halving:", blocks_per_halving)
print("blocks_per_halving:", blocks_per_halving)
print("blocks_per_halving:", blocks_per_halving)
years_per_halving = blocks_per_halving * block_time / seconds_per_year
years_per_halving = blocks_per_halving * block_time / seconds_per_year
years_per_halving = blocks_per_halving * block_time / seconds_per_year
years_per_halving = blocks_per_halving * block_time / seconds_per_year
print("years_per_halving:", years_per_halving)
print("years_per_halving:", years_per_halving)
print("years_per_halving:", years_per_halving)
print("years_per_halving:", years_per_halving)
# preferred_block_time = seconds_per_year*4/blocks_per_halving
# preferred_block_time = seconds_per_year*4/blocks_per_halving
# preferred_block_time = seconds_per_year*4/blocks_per_halving
# preferred_block_time = seconds_per_year*4/blocks_per_halving
# print("preferred_block_time:", preferred_block_time)
# print("preferred_block_time:", preferred_block_time)
# print("preferred_block_time:", preferred_block_time)
# print("preferred_block_time:", preferred_block_time)
y = 1
y = 1
y = 1
y = 1
DROPDIV = 36
DROPDIV = 36
DROPDIV = 36
DROPDIV = 36
drop = block_reward // DROPDIV
drop = block_reward // DROPDIV
drop = block_reward // DROPDIV
drop = block_reward // DROPDIV
while block_reward - drop > 10000:
while block_reward - drop > 10000:
while block_reward - drop > 10000:
while block_reward - drop > 10000:
    # Add the total reward for this halving period
    # Add the total reward for this halving period
    # Add the total reward for this halving period
    # Add the total reward for this halving period
    max_supply += block_reward * blocks_per_halving
    max_supply += block_reward * blocks_per_halving
    max_supply += block_reward * blocks_per_halving
    max_supply += block_reward * blocks_per_halving
    # Reduce the block reward by a quarter for the next period
    # Reduce the block reward by a quarter for the next period
    # Reduce the block reward by a quarter for the next period
    # Reduce the block reward by a quarter for the next period
    block_reward -= drop
    block_reward -= drop
    block_reward -= drop
    block_reward -= drop
    # print(f"y:{y*1} reward: {block_reward / 1e9} supply: {max_supply / 1e9}")
    # print(f"y:{y*1} reward: {block_reward / 1e9} supply: {max_supply / 1e9}")
    # print(f"y:{y*1} reward: {block_reward / 1e9} supply: {max_supply / 1e9}")
    # print(f"y:{y*1} reward: {block_reward / 1e9} supply: {max_supply / 1e9}")
    y = y + 1
    y = y + 1
    y = y + 1
    y = y + 1
    
    
    
    
    drop = block_reward // DROPDIV
    drop = block_reward // DROPDIV
    drop = block_reward // DROPDIV
    drop = block_reward // DROPDIV








# 63714326
# 63714326
# 63714326
# 63714326
print(f"The maximum supply of the coin is {max_supply / 1e9} smallest units or {max_supply} coins.")
print(f"The maximum supply of the coin is {max_supply / 1e9} smallest units or {max_supply} coins.")
print(f"The maximum supply of the coin is {max_supply / 1e9} smallest units or {max_supply} coins.")
print(f"The maximum supply of the coin is {max_supply / 1e9} smallest units or {max_supply} coins.")
print(f"Need premine {1e9 - max_supply / 1e9} coins.");
print(f"Need premine {1e9 - max_supply / 1e9} coins.");
print(f"Need premine {1e9 - max_supply / 1e9} coins.");
print(f"Need premine {1e9 - max_supply / 1e9} coins.");
