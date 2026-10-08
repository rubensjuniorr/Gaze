from engine import split_text, current_block, backward, forward

text = "Today I want to present my first project made in Python"
blocks = split_text(text)
spot = 0

print(current_block(spot, blocks))

spot = forward(spot, blocks)
print(current_block(spot, blocks))

spot = backward(spot,blocks)
print(current_block(spot, blocks))