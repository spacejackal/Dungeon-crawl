
import unittest

import core


class test_player_class(unittest.TestCase):

    def test_armed_attack_method(self):
        weapon = core.Dagger()
        player = core.Player()
        player.ATK = 10
        player.STR = 4
        player.Weapon = weapon

        expected = player.ATK + player.STR/4 + weapon.ATK

        self.assertEqual(expected, player.Armed_attack(weapon))
