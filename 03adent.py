"""03advent.py
Santa Claus 🎅 is checking his workshop inventory to prepare gift delivery. The elves have recorded the toys in an array of objects, but the information is a bit disorganized. You need to help Santa organize the inventory.

You will receive an array of objects, where each object represents a toy and has the properties:

    name: the name of the toy (string).
    quantity: the available quantity of that toy (integer).
    category: the category to which the toy belongs (string).

Write a function that processes this array and returns an object that organizes the toys as follows:

    The keys of the object will be the categories of toys.
    The values will be objects that have the toy names as keys and the total quantities of each toy in that category as values.
    If there are toys with the same name in the same category, you must sum their quantities.
    If the array is empty, the function should return an empty object {}.

const inventory = [
  { name: 'doll', quantity: 5, category: 'toys' },
  { name: 'car', quantity: 3, category: 'toys' },
  { name: 'ball', quantity: 2, category: 'sports' },
  { name: 'car', quantity: 2, category: 'toys' },
  { name: 'racket', quantity: 4, category: 'sports' }
]

organizeInventory(inventory)

// Expected result:
// {
//   toys: {
//     doll: 5,
//     car: 5
//   },
//   sports: {
//     ball: 2,
//     racket: 4
//   }

const inventory2 = [
  { name: 'book', quantity: 10, category: 'education' },
  { name: 'book', quantity: 5, category: 'education' },
  { name: 'paint', quantity: 3, category: 'art' }
]

organizeInventory(inventory2)

// Expected result:
// {
//   education: {
//     book: 15
//   },
//   art: {
//     paint: 3
//   }
// }
"""

import unittest

inventory2 = [{}]
expected2 = {}

inventory3 = [{"name": "doll", "quantity": 5, "category": "toys"}]
expected3 = {"toys": {"doll": 5}}

gift6 = {"name": "book", "quantity": 10, "category": "education"}
gift7 = {"name": "book", "quantity": 5, "category": "education"}
gift8 = {"name": "paint", "quantity": 3, "category": "art"}
inventory4 = [gift6, gift7, gift8]
expected4 = {"education": {"book": 15}, "art": {"paint": 3}}

gift1 = {"name": "doll", "quantity": 5, "category": "toys"}
gift2 = {"name": "car", "quantity": 3, "category": "toys"}
gift3 = {"name": "ball", "quantity": 2, "category": "sports"}
gift4 = {"name": "car", "quantity": 2, "category": "toys"}
gift5 = {"name": "racket", "quantity": 4, "category": "sports"}
inventory5 = [gift1, gift2, gift3, gift4, gift5]
expected5 = {"toys": {"doll": 5, "car": 5}, "sports": {"ball": 2, "racket": 4}}


def organizeInventory(inventory):
    res = {}
    for gift in inventory:
        if not bool(gift.values()):
            continue
        name, quantity, category = gift.values()

        if not res.get(category, None):
            res[category] = {name: quantity}
        else:
            if not res[category].get(name, None):
                res[category][name] = quantity
            else:
                res[category][name] += quantity
    return res


class ExampleTestCases(unittest.TestCase):
    test_cases = [
        (inventory2, expected2),
        (inventory3, expected3),
        (inventory4, expected4),
        (inventory5, expected5),
    ]

    def test_return_type_is_object(self):
        for test_case in self.test_cases:
            inventory, _ = test_case
            self.assertIsInstance(organizeInventory(inventory=inventory), dict)

    def test_return_objects_match_expected(self):
        for test_case in self.test_cases:
            inventory, expected = test_case
            self.assertEqual(organizeInventory(inventory), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
