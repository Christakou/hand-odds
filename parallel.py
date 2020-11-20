import time
import concurrent.futures
from  hand_odds import simulate_play
from collections import Counter

start = time.perf_counter()

def do_something(s):
    print("Sleeping ")
    time.sleep(s)
    return 'Done sleeping' 

def hand_odds(your_hand,cards_shown,number_of_opponents, n=20):
    t = time.time()
    winners = []
    # Doing it in parallel 
    with  concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(simulate_play,your_hand,cards_shown,number_of_opponents) for _ in range(n)]
        for f in concurrent.futures.as_completed(results):
            #print(f.result())
            winners.append(f.result())

    #  Doing  it in series
    #for i in range(n):
    #print(simulate_play(your_hand,cards_shown,number_of_opponents))
    #    winners.append(simulate_play(your_hand,cards_shown,number_of_opponents))
    counter = Counter(winners)
    print(sorted(counter.items()))
    print(f'{time.time()-t :.3f}s')
    print(f'{float(100*Counter(winners)[0]/n):.2f}% chance of winning with {your_hand}')







if __name__ ==  '__main__':
    hand_odds(["14D","14H"],[],4,1500)



