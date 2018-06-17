import datetime


class Pool:

    def __init__(self):
        self.date = datetime.datetime.now()


class MiningPoolHub(Pool):

    def __init__(self):
        super().__init__()
        self.name = "MiningPoolHub"

    def get_all_coins():
        """Returns a dictionary of coin names and amounts in pool"""
        pass







# Class pool
#     - pool name
#     - date
#     - coin(s) - list of coin objects