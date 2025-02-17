import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD,"https://www.fakesite.com")
        node2 = TextNode("This is a text node", TextType.BOLD,"https://www.fakesite.com")
        self.assertEqual(node, node2)

    def test_diff_text(self):
        node = TextNode("This is a text node", TextType.BOLD,"https://www.fakesite.com")
        node2 = TextNode("This is a different text node", TextType.BOLD,"https://www.fakesite2.com")
        self.assertNotEqual(node, node2)


    def test_diff_type(self):
        node = TextNode("This is a text node", TextType.BOLD,)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_type(self):
        node = TextNode("This is a text node", TextType.BOLD,"https://www.fakesite.com")
        node2 = TextNode("This is a text node", TextType.BOLD,"https://www.fakesite.com")
        self.assertEqual(node, node2)


    def test_url_is_none(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_single_url_is_none(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT,"https://www.gamersite.com")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.fakesite.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, text, https://www.fakesite.com)")



if __name__ == "__main__":
    unittest.main()