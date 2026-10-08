def split_text(text, block_size=4):
    if block_size < 1:
        raise ValueError("block_size must be at least 1")   
    words = text.split()
    blocks = []
    for start in range(0, len(words), block_size):
        block = words[start:start + block_size]
        blocks.append(" ".join(block))
    return blocks

def current_block(spot, blocks):
    if not blocks:
        return ""
    return blocks[spot]

def backward(spot, blocks):
    if spot > 0:
        spot -= 1
    return spot

def forward(spot, blocks):
    if spot < len(blocks) - 1:
        spot += 1
    return spot
