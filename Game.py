import sys
import pygame
import random

from Grid import Grid
from Player import Hunter, Pray
from Reward import Reward


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Grid.SCREEN_SIZE, Grid.SCREEN_SIZE))
        pygame.display.set_caption("NN Tags")
        self.clock = pygame.time.Clock()

        self.hunter = Hunter(1, 1)
        self.pray = Pray(Grid.GRID_SIZE - 2, Grid.GRID_SIZE - 2)
        self.turns = 6
        self.running = True

        self.hunter_rewards = []
        self.pray_rewards = []

    def run(self):
        round_number = 1

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if round_number > self.turns:
                self.running = False
                continue

            print(f"Round {round_number}:")

            self.hunter.position = self.hunter.random_move(self.hunter.position)
            hunter_reward = Reward.reward_hunter_calculation(self.pray.position, self.hunter.position)
            self.hunter_rewards.append(hunter_reward)

            if self.hunter.position == self.pray.position:
                print(f"Hunter caught the Pray!")
                hunter_reward = Reward.reward_hunter_calculation(self.pray.position, self.hunter.position)
                pray_reward = Reward.reward_pray_calculation(self.pray.position, self.hunter.position)

                self.hunter_rewards[-1] = hunter_reward
                self.pray_rewards.append(pray_reward)
                self.draw_game_state()
                break

            self.pray.position = self.pray.random_move(self.pray.position)
            pray_reward = Reward.reward_pray_calculation(self.pray.position, self.hunter.position)
            self.pray_rewards.append(pray_reward)

            self.draw_game_state()

            round_number += 1

            self.clock.tick(4)

        self.show_statistics()

        pygame.quit()
        sys.exit()

    def draw_game_state(self):
        self.screen.fill(Grid.BLACK)
        Grid.draw_grid(self.screen)
        Hunter.draw_visibility(self.screen, self.hunter.position, Grid.LIGHT_BLUE)
        Pray.draw_visibility(self.screen, self.pray.position, Grid.LIGHT_RED)
        Hunter.draw_player(self.screen, *self.hunter.position, Grid.BLUE)
        Pray.draw_player(self.screen, *self.pray.position, Grid.RED)
        pygame.display.flip()

    def show_statistics(self):
        total_hunter_reward = sum(self.hunter_rewards)
        total_pray_reward = sum(self.pray_rewards)

        print("\nGame Over!")
        print(f"Hunter Rewards: {self.hunter_rewards}")
        print(f"Pray Rewards: {self.pray_rewards}")
        print(f"Total Hunter Reward: {total_hunter_reward}")
        print(f"Total Pray Reward: {total_pray_reward}")


if __name__ == "__main__":
    game = Game()
    game.run()
