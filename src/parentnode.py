from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):

        if self.tag is None:
            raise ValueError("to_html requires a tag")

        if self.children is None or len(self.children) == 0:
            raise ValueError("to_html requires children")

        prop = self.props_to_html()
        opening_tag = f"<{self.tag}{prop}>"
        body= ""
        closing_tag = f"</{self.tag}>"

        for child in self.children:
            body+= child.to_html()
        return opening_tag + body + closing_tag

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"