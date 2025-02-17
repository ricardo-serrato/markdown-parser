import unittest

from src.leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_no_props_parse(self):
        l_node = LeafNode("p","This is a paragraph of text.").to_html()
        solution = f'<p>This is a paragraph of text.</p>'
        self.assertEqual(solution, l_node)

    def test_props_parse(self):
        l_node = LeafNode("a","click me!", {"href":"https://example.com"}).to_html()
        solution = f'<a href="https://example.com">click me!</a>'
        self.assertEqual(solution, l_node)

    def test_multiple_props_parse(self):
        l_node = LeafNode("a","click me!", {"href": "https://example.com","target": "_blank"}).to_html()
        solution = f'<a href="https://example.com" target="_blank">click me!</a>'
        self.assertEqual(solution, l_node)


    def test_values(self):
        node = LeafNode("a","click me!")
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "click me!")
        self.assertEqual(node.props,None)
        self.assertEqual(node.children, None)

    def test_no_tag_parse(self):
        node = LeafNode(None,value="My name is!").to_html()
        solution = "My name is!"
        self.assertEqual(solution, node)

    def test_repr(self):
        pass


