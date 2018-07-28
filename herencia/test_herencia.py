import unittest
from herencia import *


class AnimalTests(unittest.TestCase):

	def setUp(self):
		self.func = Animal()

	def test_sight_returns_message_i_am_seeing(self):
	    self.assertEqual(self.func.sight(), "I'm seeing...")

	def test_who_am_i_returns_message_i_am_an_animal_and(self):
		self.assertEqual(self.func.who_am_i(), "I'm an animal and")

class MammalTests(unittest.TestCase):

	def setUp(self):
		self.func = Mammal()

	def test_sight_returns_message_i_am_seeing(self):
	    self.assertEqual(self.func.sight(), "I'm seeing...")

	def test_who_am_i_returns_message_i_am_an_animal_and_i_am_a_mammal(self):
		self.assertEqual(self.func.who_am_i(), "I'm an animal and I'm a Mammal.")

class ReptileTests(unittest.TestCase):

	def setUp(self):
		self.func = Reptile()

	def test_sight_returns_message_i_am_seeing(self):
	    self.assertEqual(self.func.sight(), "I'm seeing...")

	def test_who_am_i_returns_message_i_am_an_animal_and_i_am_a_reptile(self):
		self.assertEqual(self.func.who_am_i(), "I'm an animal and I'm a Reptile.")

class BirdTests(unittest.TestCase):

	def setUp(self):
		self.func = Bird()

	def test_sight_returns_message_i_am_seeing(self):
	    self.assertEqual(self.func.sight(), "I'm seeing...")

	def test_who_am_i_returns_message_i_am_an_animal_and_i_am_a_bird(self):
		self.assertEqual(self.func.who_am_i(), "I'm an animal and I'm a Bird.")

class FishTests(unittest.TestCase):

	def setUp(self):
		self.func = Fish()

	def test_sight_returns_message_i_am_seeing(self):
	    self.assertEqual(self.func.sight(), "I'm seeing...")

	def test_who_am_i_returns_message_i_am_an_animal_and_i_am_a_fish_i_live_in_sea(self):
		self.assertEqual(self.func.who_am_i(), "I'm an animal and I'm a Fish. I live in the sea.")


class SeaTurtleTests(unittest.TestCase):

	def setUp(self):
		self.func = SeaTurtle()

	def test_sight_returns_message_i_am_seeing(self):
	    self.assertEqual(self.func.sight(), "I'm seeing...")

	def test_who_am_i_returns_message_i_am_an_animal_and_i_am_a_reptile_i_am_a_turtle_too_i_live_in_sea(self):
		self.assertEqual(self.func.who_am_i(), "I'm an animal and I'm a Reptile. I'm a Turtle too. I live in the sea.")


class DogTests(unittest.TestCase):

	def setUp(self):
		self.func = Dog()

	def test_sight_returns_message_i_am_seeing(self):
	    self.assertEqual(self.func.sight(), "I'm seeing...")

	def test_who_am_i_returns_message_i_am_an_animal_and_i_am_a_mammal_i_am_a_dog_too(self):
		self.assertEqual(self.func.who_am_i(), "I'm an animal and I'm a Mammal. I'm a Dog too.")


class MacawTests(unittest.TestCase):

	def setUp(self):
		self.func = Macaw()

	def test_sight_returns_message_i_am_seeing(self):
	    self.assertEqual(self.func.sight(), "I'm seeing...")

	def test_who_am_i_returns_message_i_am_an_animal_and_i_am_a_bird_i_am_a_macaw_too(self):
		self.assertEqual(self.func.who_am_i(), "I'm an animal and I'm a Bird. I'm a Macaw too.")

class DolphinTests(unittest.TestCase):

	def setUp(self):
		self.func = Dolphin()

	def test_sight_returns_message_i_am_seeing(self):
	    self.assertEqual(self.func.sight(), "I'm seeing...")

	def test_who_am_i_returns_message_i_am_an_animal_and_i_am_a_mammal_i_am_a_dolphin_too_i_live_in_sea(self):
		self.assertEqual(self.func.who_am_i(), "I'm an animal and I'm a Mammal. I'm a Dolphin too. I live in the sea.")


class CatTests(unittest.TestCase):

	def setUp(self):
		self.func = Cat()

	def test_sight_returns_message_i_am_seeing(self):
	    self.assertEqual(self.func.sight(), "I'm seeing...")

	def test_who_am_i_returns_message_i_am_an_animal_and_i_am_a_mammal_i_am_a_cat_too(self):
		self.assertEqual(self.func.who_am_i(), "I'm an animal and I'm a Mammal. I'm a Cat too.")

class WhaleTests(unittest.TestCase):

	def setUp(self):
		self.func = Whale()

	def test_sight_returns_message_i_am_seeing(self):
	    self.assertEqual(self.func.sight(), "I'm seeing...")

	def test_who_am_i_returns_message_i_am_an_animal_and_i_am_a_mammal_i_am_a_whale_too_i_live_in_sea(self):
		self.assertEqual(self.func.who_am_i(), "I'm an animal and I'm a Mammal. I'm a Whale. I live in the sea.")

class SnakeTests(unittest.TestCase):

	def setUp(self):
		self.func = Snake()

	def test_sight_returns_message_i_am_seeing(self):
	    self.assertEqual(self.func.sight(), "I'm seeing...")

	def test_who_am_i_returns_message_i_am_an_animal_and_i_am_a_reptile_i_am_a_snake_too(self):
		self.assertEqual(self.func.who_am_i(), "I'm an animal and I'm a Reptile. I'm a Snake too.")


if __name__=="__main__":
    unittest.main()