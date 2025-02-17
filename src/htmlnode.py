class HTMLNode:
    def __init__(self, tag=None , value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        html_attributes = ""
        if self.props is None or len(self.props) == 0:
            return html_attributes
        for key, value in self.props.items():
            html_attributes += f' {key}="{value}"'
        return html_attributes

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'

