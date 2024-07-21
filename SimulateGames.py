from Game import Poker
import json
from pprint import pformat

class StrategyTester:
    
    def __init__(self, numGames, numPlayers, strategyFile):
        self.strategy = StrategyParser(strategyFile)
        self.numGames = numGames
        self.numPlayers = numPlayers
        self.games = []
        
    def runSimulations(self):
        for _ in range(self.numGames):
            self.games.append(Poker(numPlayers=self.numPlayers).deal_hands())
        return 0
    
    def getPairs(self):
        pairs = []
        for i in range(len(self.games)):
            print("Game " + str(i))
            for hand in self.games[i]:
                print(hand)
                
class StrategyParser:
    
    def __init__(self, strategyFile):
        with open('./strategies/' + strategyFile, 'r') as file:
            strategy = file.read().strip()
        self.strategy = json.loads(strategy)
        
    def __str__(self):
        return pformat(self.strategy)