from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None,props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        props = self.props_to_html()

        final_html = f'<{self.tag}{props}>{self.value}</{self.tag}>'
        return final_html

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

