
from textnode import TextNode, TextType
def main():
    text_node = TextNode("this is an example text",TextType.BOLD, "https://www.fakesite.com")
    print(text_node)

main()