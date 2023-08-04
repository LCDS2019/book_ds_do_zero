from tqdm import tqdm
import time

for i in tqdm(range(50), ncols = 100, desc ="Processing: ", colour='RED'):
    time.sleep(0.05)
print("Iteration Successful")

#[hex (#00ff00), BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]