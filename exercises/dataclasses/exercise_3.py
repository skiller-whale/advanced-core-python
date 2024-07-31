from html import HtmlNode, HtmlAttribute

# pylint: disable=pointless-string-statement
"""
-----------------------
DATACLASSES: Exercise 3
-----------------------

There's a bug when rendering 'disabled' for the button, as it has no value:

    <button disabled=''>test button</button>

It instead should be:

    <button disabled>test button</button>

1) Add a new class called 'BaseHtmlAttribute' that contains only a key.
    * Also define its `__str__` function appropriately.
    * Use it in this file to make buttons render correctly.

2) Make `HtmlAttribute` inherit from `BaseHtmlAttribute`.
    * `HtmlAttribute` should not redefine `key`.
"""

if __name__ == '__main__':
    html_tree = HtmlNode('html', children=[
        HtmlNode('head', children=[
            HtmlNode('title', 'Hello, World')
        ]),
        HtmlNode('body', children=[
            HtmlNode('h1', 'Hi, there!'),
            HtmlNode('a', 'Example link', attrs=[
                HtmlAttribute('href', 'http://example.com')
            ]),
            HtmlNode('button', 'test button', attrs=[
                HtmlAttribute('disabled', '')
            ])
        ])
    ])

    print(html_tree.render())
    with open('output.html', 'w') as html_file:
        html_file.write(html_tree.render())
