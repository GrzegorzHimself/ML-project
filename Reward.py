class Reward:
    @staticmethod
    def reward_hunter_calculation(position_pray, position_hunter):
        x, y = position_pray
        x1, y1 = position_hunter
        if x == x1 and y == y1:
            return 10
        distance = (x - x1) ** 2 + (y - y1) ** 2
        return 1 / distance

    @staticmethod
    def reward_pray_calculation(position_pray, position_hunter):
        x, y = position_pray
        x1, y1 = position_hunter
        if x == x1 and y == y1:
            return -10
        distance = (x - x1) ** 2 + (y - y1) ** 2
        return distance * 0.1
