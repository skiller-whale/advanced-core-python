from html import HtmlNode, HtmlAttribute

# pylint: disable=pointless-string-statement
"""
-----------------------
DATACLASSES: Exercise 5
-----------------------

1) Make `HtmlNode` frozen, then uncomment the line at the end
    of this file.
    * Can you explain why that does or doesn't work?

2) Add the following top-level constant in `html.py`:

    ALLOWED_NODE_NAMES = [
        'html', 'head', 'title', 'body',
        'a', 'button', 'input',
        'h1', 'h2', 'h3', 'h4', 'h5'
    ] 

3) Implement validation so that only tags in `ALLOWED_NODE_NAMES`
    are allowed for `HtmlNode` objects.
    * You should `raise` a `ValueError` with an appropriate message.

4) Run this file and make sure the neither `whale` nodes are allowed.

HINT: You may need to import some types and utility functions
    from `dataclasses` and `typing`.
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

    # [Part 1] uncomment this after making `HtmlNode` frozen
    # html_tree.children.append(HtmlNode('whale', 'hello there'))

    print(html_tree.render())
    with open('output.html', 'w') as html_file:
        html_file.write(html_tree.render())
