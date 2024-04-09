from html import HtmlNode, HtmlAttribute

# pylint: disable=pointless-string-statement
"""
DATACLASSES: Exercise 1
-------------

This code lets you define and render HTML programmatically.

1) Run this script and read briefly through the code in html.py.
    * You can also open `output.html` in a browser to view it.

2) Make the following changes to the classes in html.py:
  * Make `HtmlAttribute` a dataclass.
  * Move the `render` function outside of the data class.

3) Run this script, and ensure that the rendering still works.
    You shouldn't need to change anything in this file.

4) Think about the new render function for `HtmlAttribute`.
    Is there a better way to do this? Discuss with your coach.
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
