import random

input_file = 'Appliances.jsonl'
output_file = 'mini-appliances.jsonl'

with open(input_file, 'r') as f:
    lines = f.readlines()

random.seed(42)
sampled_lines = random.sample(lines, 100000)

with open(output_file, 'w') as f:
    for line in sampled_lines:
        f.write(line)

print(f"Saved 100,000 random rows to {output_file}.")