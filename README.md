# utra-x-spahinx
Sphinx
Package on PyPI Documentation Status Build Status (Travis CI) Build Status (AppVeyor) Build Status (CircleCI) Code Coverage Status (Codecov) BSD 3 Clause Open Source Helpers badge
Sphinx is a tool that makes it easy to create intelligent and beautiful documentation for Python projects (or other documents consisting of multiple reStructuredText sources), written by Georg Brandl. It was originally created for the new Python documentation, and has excellent facilities for Python project documentation, but C/C++ is supported as well, and more languages are planned.

Sphinx uses reStructuredText as its markup language, and many of its strengths come from the power and straightforwardness of reStructuredText and its parsing and translating suite, the Docutils.

Among its features are the following:

Output formats: HTML (including derivative formats such as HTML Help, Epub and Qt Help), plain text, manual pages and LaTeX or direct PDF output using rst2pdf
Extensive cross-references: semantic markup and automatic links for functions, classes, glossary terms and similar pieces of information
Hierarchical structure: easy definition of a document tree, with automatic links to siblings, parents and children
Automatic indices: general index as well as a module index
Code handling: automatic highlighting using the Pygments highlighter
Flexible HTML output using the Jinja 2 templating engine
Various extensions are available, e.g. for automatic testing of snippets and inclusion of appropriately formatted docstrings
Setuptools integration
For more information, refer to the the documentation.

Installation
Sphinx is published on PyPI and can be installed from there:

pip install -U sphinx
We also publish beta releases:

pip install -U --pre sphinx
If you wish to install Sphinx for development purposes, refer to the contributors guide.

Documentation
Documentation is available from sphinx-doc.org.

Get in touch
Report bugs, suggest features or view the source code on GitHub.
For less well defined questions or ideas, use the mailing list.
Please adhere to our code of conduct.

Testing
Continuous testing is provided by Travis (for unit tests and style checks on Linux), AppVeyor (for unit tests on Windows), and CircleCI (for large processes like TeX compilation).

For information on running tests locally, refer to the contributors guide.

Contributing
Refer to the contributors guide.

Release signatures
Releases are signed with following keys:

498D6B9E
5EBA0E07
