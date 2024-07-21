import poker
import random
from Game import Poker
from SimulateGames import StrategyTester

def main():
    sim = StrategyTester(numGames=20, numPlayers=4, strategyFile='STRATEGY1.json')
    print(sim.strategy)
    
if __name__ == "__main__":
    main()