from dataclasses import dataclass


class HtmlAttribute:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def render(self):
        return f"{self.key}='{self.value}'"


class HtmlNode:
    def __init__(self, tag, content='', attrs='', children=None):
        self.tag = tag
        self.content = content
        self.attrs = [] if attrs is None else attrs
        self.children = [] if children is None else children

    def render(self, tabs=0):
        child_content = '\n'.join([
            child.render(tabs + 1)
            for child in self.children
        ])

        attr_content = ' '.join([
            attr.render()
            for attr in self.attrs
        ])

        tabs = '  ' * tabs

        # (formatting) add leading space
        if attr_content:
            attr_content = f' {attr_content}'

        # (formating) add a new line at the start
        if child_content:
            child_content = f'\n{child_content}{tabs}'

        content = f'{self.content}{child_content}'
        return f'{tabs}<{self.tag}{attr_content}>{content}</{self.tag}>\n'
