from parentnode import ParentNode
from leafnode import LeafNode
import unittest
class TestParentNode(unittest.TestCase):
    def test_parentnode(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        answer = node.to_html()
        solution = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(answer,solution)

    def test_prop(self):
        node = ParentNode(
            "p",
            [
                LeafNode("a","click me!", {"href":"https://example.com"}),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        answer = node.to_html()
        solution = '<p><a href="https://example.com">click me!</a>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(answer, solution)

    def test_parent_prop(self):
        node = ParentNode(
            "p",
            [
                LeafNode("a", "click me!", {"href": "https://example.com"}),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {"style":"text-align: left",}
        )

        answer = node.to_html()
        solution = '<p style="text-align: left"><a href="https://example.com">click me!</a>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(answer, solution)

    def test_parent_with_prop(self):
        node1= ParentNode(
            "div",
            [LeafNode("b","Hello")],
            {"class":"greeting"}

        )

        answer = '<div class="greeting"><b>Hello</b></div>'
        self.assertEqual(node1.to_html(),answer)

    def test_nested_parents(self):
        node2 = ParentNode("div",[ParentNode("p",[LeafNode("span","nested")])])
        solution = '<div><p><span>nested</span></p></div>'

        self.assertEqual(node2.to_html(),solution)

    def test_value_error(self):
        # Should raise ValueError (no tag)
        node1 = ParentNode(None, [LeafNode("p", "test")])
        with self.assertRaises(ValueError):
            node1.to_html()

        # Should raise ValueError (no children)
        node2 = ParentNode("div", [])
        with self.assertRaises(ValueError):
            node2.to_html()

        # Should raise ValueError (None children)
        node3 = ParentNode("div", None)

        with self.assertRaises(ValueError):
            node3.to_html()


