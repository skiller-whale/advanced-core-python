from html import HtmlNode, HtmlAttribute

# pylint: disable=pointless-string-statement
"""
-----------------------
DATACLASSES: Exercise 2
-----------------------

Python has a dunder method called `__str__` that can (and should) be used
    to convert an object to its string representation.

1) Instead of using a separate render function for `HtmlAttribute`, use `__str__`:
    * Define and implement `__str__` in `HtmlAttribute` - it takes no arguments.
    * Use it inside `HtmlNode` - calling `str(<node>)` will call `__str__`.

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
