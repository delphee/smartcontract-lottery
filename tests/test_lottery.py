# 0.019
from brownie import Lottery, accounts


def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(????, {"from": account})
