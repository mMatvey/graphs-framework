import unittest
from Tests.testsUtils import *


class TestWrite(unittest.TestCase):

    def test_graph_write(self):
        for i in range(5):
            test_graph = generate_graph()
            test_graph.write_to_file('./testWrite.txt')
            with open('./testWrite.txt', "r") as file:
                text = file.read()
                self.assertEqual(str(test_graph), text)

class TestRead(unittest.TestCase):

    def test_graph_read(self):
        test_graph = generate_graph()
        test_graph.write_to_file('./testRead.txt')
        new_graph = Graph.read_from_file('./testRead.txt')
        self.assertEqual(new_graph, test_graph)

if __name__ == '__main__':
    unittest.main()