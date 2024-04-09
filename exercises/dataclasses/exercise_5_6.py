from html import HtmlNode, HtmlAttribute

# pylint: disable=pointless-string-statement
"""
-----------------------
DATACLASSES: Exercise 5
-----------------------

1) Add the following top-level constant in `html.py`:

    ALLOWED_NODE_NAMES = [
        'html', 'head', 'title', 'body',
        'a', 'button', 'input',
        'h1', 'h2', 'h3', 'h4', 'h5'
    ] 

2) Implement validation so that only tags in `ALLOWED_NODE_NAMES`
    are allowed for `HtmlNode` objects.
    * You should `raise` a `ValueError` with an appropriate message.

3) Run this file and make sure the `whale` node isn't allowed.

-----------------------
DATACLASSES: Exercise 6
-----------------------

1) Make `ALLOWED_NODE_NAMES` a class attribute.

HINT: You may need to import some types from `dataclasses` (not `typing`).
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
            ]),
            HtmlNode('whale', 'Orca')
        ])
    ])

    print(html_tree.render())
    with open('output.html', 'w') as html_file:
        html_file.write(html_tree.render())
