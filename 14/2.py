import sys

def block_sort_encode(val):
    res = []
    res.append(val)

    for i in range(len(val) - 1):
        temp = res[-1]
        res.append(temp[1:] + temp[0])
    res.sort()

    idx = res.index(val)
    encoded_str = [v[-1] for v in res]
    return ''.join(encoded_str), idx

def block_sort_decode(val, idx):
    char_last_idx = []
    for i, v in enumerate(val):
        char_last_idx.append((v, i))
    char_last_idx.sort()

    last_to_front_idx = [0] * len(char_last_idx)
    for i, v in enumerate(char_last_idx):
        last_to_front_idx[v[1]] = i
    res = val[idx]

    i = last_to_front_idx[idx]
    while i != idx:
        res += val[i]
        i = last_to_front_idx[i]
    return res[::-1]


mode = sys.argv[1]
input_filename = sys.argv[2]
output_filename = sys.argv[3]

if mode == 'e':
    with open(input_filename, 'r') as f:
        val = f.read()
    encoded_str, idx = block_sort_encode(val)
    with open(output_filename, 'w') as f:
        f.write(encoded_str + '\n')
        f.write(str(idx))
elif mode == 'd':
    with open(input_filename, 'r') as f:
        val = f.read()
    val = val.split('\n')
    encoded_str = val[0]
    idx = int(val[-1])
    decoded_str = block_sort_decode(encoded_str, idx)
    with open(output_filename, 'w') as f:
        f.write(decoded_str)
else:
    print('Invalid mode')
