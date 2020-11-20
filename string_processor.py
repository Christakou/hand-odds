import re
from parallel import hand_odds
if __name__ == '__main__':
    while True:
        class_string = input('Paste html extract:')
        split = (class_string.split(','))
        number_of_players = int(split[-1])
        split = split[:-1]
        print(split)
        match_list = []
        suits = []
        ranks = []
        
        for item in split:
            extraction = re.search(r'(diamonds-(\w|\d))|(clubs-(\w|\d))|(hearts-(\w|\d))|(spades-(\w|\d))',item)[0]
            extraction = extraction.replace('clubs-','C').replace('spades-','S').replace('diamonds-','D').replace('hearts-','H')
            extraction = extraction.replace('Q','12').replace('K','13').replace('A','14').replace('J','11')
            formatted = re.search(r'\d{1,2}',extraction)[0]+re.search(r'\w',extraction)[0]

            match_list.append(formatted)
        hand_odds(match_list[-2:],match_list[:-2],number_of_players-1,1000)