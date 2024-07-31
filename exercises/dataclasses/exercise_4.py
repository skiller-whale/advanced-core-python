from html import HtmlNode, HtmlAttribute

# pylint: disable=pointless-string-statement
"""
-----------------------
DATACLASSES: Exercise 4
-----------------------

1) Update the `HtmlNode` class so that it's a data class.
    * Think about its `render` function. Should this functionality
        be in `__str__`? Why or why not? Discuss with your coach.

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
            ])
        ])
    ])

    print(html_tree.render())
    with open('output.html', 'w') as html_file:
        html_file.write(html_tree.render())
