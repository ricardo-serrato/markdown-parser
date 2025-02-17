import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_div_with_children(self):
        node = HTMLNode(
            tag="div",
            children=[
                HTMLNode(tag="p", value="Hello")
            ]
        )
        self.assertEqual(node.tag, "div")
        self.assertEqual(len(node.children), 1)

    def test_single_prop(self):
        props = {"href": "http://example.com"}
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(),' href="http://example.com"')

    def test_multiple_props(self):
        props = {"href": "http://example.com","target": "_blank"}
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(),' href="http://example.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode("a", "this is a sample text")
        self.assertEqual(repr(node), "HTMLNode(a, this is a sample text, children: None, None)")

    def test_empty_prop(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_empty_dict(self):
        node = HTMLNode(props={})  # explicitly empty dict
        self.assertEqual(node.props_to_html(), "")

    def test_value_only(self):
        node = HTMLNode(value="this is a sample text")
        self.assertEqual(node.value, "this is a sample text")
        self.assertIsNone(node.tag)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_to_html_raises(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()
