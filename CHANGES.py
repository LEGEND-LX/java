Release 3.5.2 (in development)
==============================

Dependencies
------------

Incompatible changes
--------------------

Deprecated
----------

Features added
--------------

Bugs fixed
----------

Testing
--------

Release 3.5.1 (released Feb 16, 2021)
=====================================

Bugs fixed
----------

* #8883: autodoc: AttributeError is raised on assigning __annotations__ on
  read-only class
* #8884: html: minified js stemmers not included in the distributed package
* #8885: html: AttributeError is raised if CSS/JS files are installed via
  :confval:`html_context`
* #8880: viewcode: ExtensionError is raised on incremental build after
  unparsable python module found

Release 3.5.0 (released Feb 14, 2021)
=====================================

Dependencies
------------

* LaTeX: ``multicol`` (it is anyhow a required part of the official latex2e
  base distribution)

Incompatible changes
--------------------

* Update Underscore.js to 1.12.0
* #6550: html: The config variable ``html_add_permalinks`` is replaced by
  :confval:`html_permalinks` and :confval:`html_permalinks_icon`

Deprecated
----------

* pending_xref node for viewcode extension
* ``sphinx.builders.linkcheck.CheckExternalLinksBuilder.anchors_ignore``
* ``sphinx.builders.linkcheck.CheckExternalLinksBuilder.auth``
* ``sphinx.builders.linkcheck.CheckExternalLinksBuilder.broken``
* ``sphinx.builders.linkcheck.CheckExternalLinksBuilder.good``
* ``sphinx.builders.linkcheck.CheckExternalLinksBuilder.redirected``
* ``sphinx.builders.linkcheck.CheckExternalLinksBuilder.rqueue``
* ``sphinx.builders.linkcheck.CheckExternalLinksBuilder.to_ignore``
* ``sphinx.builders.linkcheck.CheckExternalLinksBuilder.workers``
* ``sphinx.builders.linkcheck.CheckExternalLinksBuilder.wqueue``
* ``sphinx.builders.linkcheck.node_line_or_0()``
* ``sphinx.ext.autodoc.AttributeDocumenter.isinstanceattribute()``
* ``sphinx.ext.autodoc.directive.DocumenterBridge.reporter``
* ``sphinx.ext.autodoc.importer.get_module_members()``
* ``sphinx.ext.autosummary.generate._simple_info()``
* ``sphinx.ext.autosummary.generate._simple_warn()``
* ``sphinx.writers.html.HTMLTranslator.permalink_text``
* ``sphinx.writers.html5.HTML5Translator.permalink_text``

Features added
--------------

* #8022: autodoc: autodata and autoattribute directives does not show right-hand
  value of the variable if docstring contains ``:meta hide-value:`` in
  info-field-list
* #8514: autodoc: Default values of overloaded functions are taken from actual
  implementation if they're ellipsis
* #8775: autodoc: Support type union operator (PEP-604) in Python 3.10 or above
* #8297: autodoc: Allow to extend :confval:`autodoc_default_options` via
  directive options
* #8619: html: kbd role generates customizable HTML tags for compound keys
* #8634: html: Allow to change the order of JS/CSS via ``priority`` parameter
  for :meth:`Sphinx.add_js_file()` and :meth:`Sphinx.add_css_file()`
* #6241: html: Allow to add JS/CSS files to the specific page when an extension
  calls ``app.add_js_file()`` or ``app.add_css_file()`` on
  :event:`html-page-context` event
* #6550: html: Allow to use HTML permalink texts via
  :confval:`html_permalinks_icon`
* #1638: html: Add permalink icons to glossary terms
* #8868: html search: performance issue with massive lists
* #8867: html search: Update JavaScript stemmer code to the latest version of
  Snowball (v2.1.0)
* #8852: i18n: Allow to translate heading syntax in MyST-Parser
* #8649: imgconverter: Skip availability check if builder supports the image
  type
* #8573: napoleon: Allow to change the style of custom sections using
  :confval:`napoleon_custom_styles`
* #8004: napoleon: Type definitions in Google style docstrings are rendered as
  references when :confval:`napoleon_preprocess_types` enabled
* #6241: mathjax: Include mathjax.js only on the document using equations
* #8775: py domain: Support type union operator (PEP-604)
* #8651: std domain: cross-reference for a rubric having inline item is broken
* #7642: std domain: Optimize case-insensitive match of term
* #8681: viewcode: Support incremental build
* #8132: Add :confval:`project_copyright` as an alias of :confval:`copyright`
* #207: Now :confval:`highlight_language` supports multiple languages
* #2030: :rst:dir:`code-block` and :rst:dir:`literalinclude` supports automatic
  dedent via no-argument ``:dedent:`` option
* C++, also hyperlink operator overloads in expressions and alias declarations.
* #8247: Allow production lists to refer to tokens from other production groups
* #8813: Show what extension (or module) caused it on errors on event handler
* #8213: C++: add ``maxdepth`` option to :rst:dir:`cpp:alias` to insert nested
  declarations.
* C, add ``noroot`` option to :rst:dir:`c:alias` to render only nested
  declarations.
* C++, add ``noroot`` option to :rst:dir:`cpp:alias` to render only nested
  declarations.

Bugs fixed
----------

* #8727: apidoc: namespace module file is not generated if no submodules there
* #741: autodoc: inherited-members doesn't work for instance attributes on super
  class
* #8592: autodoc: ``:meta public:`` does not effect to variables
* #8594: autodoc: empty __all__ attribute is ignored
* #8315: autodoc: Failed to resolve struct.Struct type annotation
* #8652: autodoc: All variable comments in the module are ignored if the module
  contains invalid type comments
* #8693: autodoc: Default values for overloaded functions are rendered as string
* #8134: autodoc: crashes when mocked decorator takes arguments
* #8800: autodoc: Uninitialized attributes in superclass are recognized as
  undocumented
* #8655: autodoc: Failed to generate document if target module contains an
  object that raises an exception on ``hasattr()``
* #8306: autosummary: mocked modules are documented as empty page when using
  :recursive: option
* #8232: graphviz: Image node is not rendered if graph file is in subdirectory
* #8618: html: kbd role produces incorrect HTML when compound-key separators (-,
  + or ^) are used as keystrokes
* #8629: html: A type warning for html_use_opensearch is shown twice
* #8714: html: kbd role with "Caps Lock" rendered incorrectly
* #8123: html search: fix searching for terms containing + (Requires a custom
  search language that does not split on +)
* #8665: html theme: Could not override globaltoc_maxdepth in theme.conf
* #8446: html: consecutive spaces are displayed as single space
* #8745: i18n: crashes with KeyError when translation message adds a new auto
  footnote reference
* #4304: linkcheck: Fix race condition that could lead to checking the
  availability of the same URL twice
* #8791: linkcheck: The docname for each hyperlink is not displayed
* #7118: sphinx-quickstart: questionare got Mojibake if libreadline unavailable
* #8094: texinfo: image files on the different directory with document are not
  copied
* #8782: todo: Cross references in todolist get broken
* #8720: viewcode: module pages are generated for epub on incremental build
* #8704: viewcode: anchors are generated in incremental build after singlehtml
* #8756: viewcode: highlighted code is generated even if not referenced
* #8671: :confval:`highlight_options` is not working
* #8341: C, fix intersphinx lookup types for names in declarations.
* C, C++: in general fix intersphinx and role lookup types.
* #8683: :confval:`html_last_updated_fmt` does not support UTC offset (%z)
* #8683: :confval:`html_last_updated_fmt` generates wrong time zone for %Z
* #1112: ``download`` role creates duplicated copies when relative path is
  specified
* #2616 (fifth item): LaTeX: footnotes from captions are not clickable,
  and for manually numbered footnotes only first one with same number is
  an hyperlink
* #7576: LaTeX with French babel and memoir crash: "Illegal parameter number
  in definition of ``\FNH@prefntext``"
* #8055: LaTeX (docs): A potential display bug with the LaTeX generation step
  in Sphinx (how to generate one-column index)
* #8072: LaTeX: Directive :rst:dir:`hlist` not implemented in LaTeX
* #8214: LaTeX: The :rst:role:`index` role and the glossary generate duplicate
  entries in the LaTeX index (if both used for same term)
* #8735: LaTeX: wrong internal links in pdf to captioned code-blocks when
  :confval:`numfig` is not True
* #8442: LaTeX: some indexed terms are ignored when using xelatex engine
  (or pdflatex and :confval:`latex_use_xindy` set to True) with memoir class
* #8750: LaTeX: URLs as footnotes fail to show in PDF if originating from
  inside function type signatures
* #8780: LaTeX: long words in narrow columns may not be hyphenated
* #8788: LaTeX: ``\titleformat`` last argument in sphinx.sty should be
  bracketed, not braced (and is anyhow not needed) 
* #8849: LaTex: code-block printed out of margin (see the opt-in LaTeX syntax
  boolean :ref:`verbatimforcewraps <latexsphinxsetupforcewraps>` for use via
  the :ref:`'sphinxsetup' <latexsphinxsetup>` key of ``latex_elements``)
* #8183: LaTeX: Remove substitution_reference nodes from doctree only on LaTeX
  builds
* #8865: LaTeX: Restructure the index nodes inside title nodes only on LaTeX
  builds
* #8796: LaTeX: potentially critical low level TeX coding mistake has gone
  unnoticed so far
* C, :rst:dir:`c:alias` skip symbols without explicit declarations
  instead of crashing.
* C, :rst:dir:`c:alias` give a warning when the root symbol is not declared.
* C, ``expr`` role should start symbol lookup in the current scope.

Release 3.4.3 (released Jan 08, 2021)
=====================================

Bugs fixed
----------

* #8655: autodoc: Failed to generate document if target module contains an
  object that raises an exception on ``hasattr()``

Release 3.4.2 (released Jan 04, 2021)
=====================================

Bugs fixed
----------

* #8164: autodoc: Classes that inherit mocked class are not documented
* #8602: autodoc: The ``autodoc-process-docstring`` event is emitted to the
  non-datadescriptors unexpectedly
* #8616: autodoc: AttributeError is raised on non-class object is passed to
  autoclass directive

Release 3.4.1 (released Dec 25, 2020)
=====================================

Bugs fixed
----------

* #8559: autodoc: AttributeError is raised when using forward-reference type
  annotations
* #8568: autodoc: TypeError is raised on checking slots attribute
* #8567: autodoc: Instance attributes are incorrectly added to Parent class
* #8566: autodoc: The ``autodoc-process-docstring`` event is emitted to the
  alias classes unexpectedly
* #8583: autodoc: Unnecessary object comparision via ``__eq__`` method
* #8565: linkcheck: Fix PriorityQueue crash when link tuples are not
  comparable

Release 3.4.0 (released Dec 20, 2020)
=====================================

Incompatible changes
--------------------

* #8105: autodoc: the signature of class constructor will be shown for decorated
  classes, not a signature of decorator

Deprecated
----------

* The ``follow_wrapped`` argument of ``sphinx.util.inspect.signature()``
* The ``no_docstring`` argument of
  ``sphinx.ext.autodoc.Documenter.add_content()``
* ``sphinx.ext.autodoc.Documenter.get_object_members()``
* ``sphinx.ext.autodoc.DataDeclarationDocumenter``
* ``sphinx.ext.autodoc.GenericAliasDocumenter``
* ``sphinx.ext.autodoc.InstanceAttributeDocumenter``
* ``sphinx.ext.autodoc.SlotsAttributeDocumenter``
* ``sphinx.ext.autodoc.TypeVarDocumenter``
* ``sphinx.ext.autodoc.importer._getannotations()``
* ``sphinx.ext.autodoc.importer._getmro()``
* ``sphinx.pycode.ModuleAnalyzer.parse()``
* ``sphinx.util.osutil.movefile()``
* ``sphinx.util.requests.is_ssl_error()``

Features added
--------------

* #8119: autodoc: Allow to determine whether a member not included in
  ``__all__`` attribute of the module should be documented or not via
  :event:`autodoc-skip-member` event
* #8219: autodoc: Parameters for generic class are not shown when super class is
  a generic class and show-inheritance option is given (in Python 3.7 or above)
* autodoc: Add ``Documenter.config`` as a shortcut to access the config object
* autodoc: Add Optional[t] to annotation of function and method if a default
  value equal to None is set.
* #8209: autodoc: Add ``:no-value:`` option to :rst:dir:`autoattribute` and
  :rst:dir:`autodata` directive to suppress the default value of the variable
* #8460: autodoc: Support custom types defined by typing.NewType
* #8285: napoleon: Add :confval:`napoleon_attr_annotations` to merge type hints
  on source code automatically if any type is specified in docstring
* #8236: napoleon: Support numpydoc's "Receives" section
* #6914: Add a new event :event:`warn-missing-reference` to custom warning
  messages when failed to resolve a cross-reference
* #6914: Emit a detailed warning when failed to resolve a ``:ref:`` reference
* #6629: linkcheck: The builder now handles rate limits. See
  :confval:`linkcheck_retry_on_rate_limit` for details.

Bugs fixed
----------

* #7613: autodoc: autodoc does not respect __signature__ of the class
* #4606: autodoc: the location of the warning is incorrect for inherited method
* #8105: autodoc: the signature of class constructor is incorrect if the class
  is decorated
* #8434: autodoc: :confval:`autodoc_type_aliases` does not effect to variables
  and attributes
* #8443: autodoc: autodata directive can't create document for PEP-526 based
  type annotated variables
* #8443: autodoc: autoattribute directive can't create document for PEP-526
  based uninitalized variables
* #8480: autodoc: autoattribute could not create document for __slots__
  attributes
* #8503: autodoc: autoattribute could not create document for a GenericAlias as
  class attributes correctly
* #8534: autodoc: autoattribute could not create document for a commented
  attribute in alias class
* #8452: autodoc: autodoc_type_aliases doesn't work when autodoc_typehints is
  set to "description"
* #8541: autodoc: autodoc_type_aliases doesn't work for the type annotation to
  instance attributes
* #8460: autodoc: autodata and autoattribute directives do not display type
  information of TypeVars
* #8493: autodoc: references to builtins not working in class aliases
* #8522: autodoc:  ``__bool__`` method could be called
* #8067: autodoc: A typehint for the instance variable having type_comment on
  super class is not displayed
* #8545: autodoc: a __slots__ attribute is not documented even having docstring
* #741: autodoc: inherited-members doesn't work for instance attributes on super
  class
* #8477: autosummary: non utf-8 reST files are generated when template contains
  multibyte characters
* #8501: autosummary: summary extraction splits text after "el at." unexpectedly
* #8524: html: Wrong url_root has been generated on a document named "index"
* #8419: html search: Do not load ``language_data.js`` in non-search pages
* #8549: i18n: ``-D gettext_compact=0`` is no longer working
* #8454: graphviz: The layout option for graph and digraph directives don't work
* #8131: linkcheck: Use GET when HEAD requests cause Too Many Redirects, to
  accommodate infinite redirect loops on HEAD
* #8437: Makefile: ``make clean`` with empty BUILDDIR is dangerous
* #8365: py domain: ``:type:`` and ``:rtype:`` gives false ambiguous class
  lookup warnings
* #8352: std domain: Failed to parse an option that starts with bracket
* #8519: LaTeX: Prevent page brake in the middle of a seealso
* #8520: C, fix copying of AliasNode.

Release 3.3.1 (released Nov 12, 2020)
=====================================

Bugs fixed
----------

* #8372: autodoc: autoclass directive became slower than Sphinx-3.2
* #7727: autosummary: raise PycodeError when documenting python package
  without __init__.py
* #8350: autosummary: autosummary_mock_imports causes slow down builds
* #8364: C, properly initialize attributes in empty symbols.
* #8399: i18n: Put system locale path after the paths specified by configuration

Release 3.3.0 (released Nov 02, 2020)
=====================================

Deprecated
----------

* ``sphinx.builders.latex.LaTeXBuilder.usepackages``
* ``sphinx.builders.latex.LaTeXBuilder.usepackages_afger_hyperref``
* ``sphinx.ext.autodoc.SingledispatchFunctionDocumenter``
* ``sphinx.ext.autodoc.SingledispatchMethodDocumenter``

Features added
--------------

* #8100: html: Show a better error message for failures on copying
  html_static_files
* #8141: C: added a ``maxdepth`` option to :rst:dir:`c:alias` to insert
  nested declarations.
* #8081: LaTeX: Allow to add LaTeX package via ``app.add_latex_package()`` until
  just before writing .tex file
* #7996: manpage: Add :confval:`man_make_section_directory` to make a section
  directory on build man page
* #8289: epub: Allow to suppress "duplicated ToC entry found" warnings from epub
  builder using :confval:`suppress_warnings`.
* #8298: sphinx-quickstart: Add :option:`sphinx-quickstart --no-sep` option
* #8304: sphinx.testing: Register public markers in sphinx.testing.fixtures
* #8051: napoleon: use the obj role for all See Also items
* #8050: napoleon: Apply :confval:`napoleon_preprocess_types` to every field
* C and C++, show line numbers for previous declarations when duplicates are
  detected.
* #8183: Remove substitution_reference nodes from doctree only on LaTeX builds

Bugs fixed
----------

* #8085: i18n: Add support for having single text domain
* #6640: i18n: Failed to override system message translation
* #8143: autodoc: AttributeError is raised when False value is passed to
  autodoc_default_options
* #8103: autodoc: functools.cached_property is not considered as a property
* #8190: autodoc: parsing error is raised if some extension replaces docstring
  by string not ending with blank lines
* #8142: autodoc: Wrong constructor signature for the class derived from
  typing.Generic
* #8157: autodoc: TypeError is raised when annotation has invalid __args__
* #7964: autodoc: Tuple in default value is wrongly rendered
* #8200: autodoc: type aliases break type formatting of autoattribute
* #7786: autodoc: can't detect overloaded methods defined in other file
* #8294: autodoc: single-string __slots__ is not handled correctly
* #7785: autodoc: autodoc_typehints='none' does not effect to overloaded functions
* #8192: napoleon: description is disappeared when it contains inline literals
* #8142: napoleon: Potential of regex denial of service in google style docs
* #8169: LaTeX: pxjahyper loaded even when latex_engine is not platex
* #8215: LaTeX: 'oneside' classoption causes build warning
* #8175: intersphinx: Potential of regex denial of service by broken inventory
* #8277: sphinx-build: missing and redundant spacing (and etc) for console
  output on building
* #7973: imgconverter: Check availability of imagemagick many times
* #8255: py domain: number in default argument value is changed from hexadecimal
  to decimal
* #8316: html: Prevent arrow keys changing page when button elements are focused
* #8343: html search: Fix unnecessary load of images when parsing the document
* #8254: html theme: Line numbers misalign with code lines
* #8093: The highlight warning has wrong location in some builders (LaTeX,
  singlehtml and so on)
* #8215: Eliminate Fancyhdr build warnings for oneside documents
* #8239: Failed to refer a token in productionlist if it is indented
* #8268: linkcheck: Report HTTP errors when ``linkcheck_anchors`` is ``True``
* #8245: linkcheck: take source directory into account for local files
* #8321: linkcheck: ``tel:`` schema hyperlinks are detected as errors
* #8323: linkcheck: An exit status is incorrect when links having unsupported
  schema found
* #8188: C, add missing items to internal object types dictionary,
  e.g., preventing intersphinx from resolving them.
* C, fix anon objects in intersphinx.
* #8270, C++, properly reject functions as duplicate declarations if a
  non-function declaration of the same name already exists.
* C, fix references to function parameters.
  Link to the function instead of a non-existing anchor.
* #6914: figure numbers are unexpectedly assigned to uncaptioned items
* #8320: make "inline" line numbers un-selectable

Testing
--------

* #8257: Support parallel build in sphinx.testing

Release 3.2.1 (released Aug 14, 2020)
=====================================

Features added
--------------

* #8095: napoleon: Add :confval:`napoleon_preprocess_types` to enable the type
  preprocessor for numpy style docstrings
* #8114: C and C++, parse function attributes after parameters and qualifiers.

Bugs fixed
----------

* #8074: napoleon: Crashes during processing C-ext module
* #8088: napoleon: "Inline literal start-string without end-string" warning in
  Numpy style Parameters section
* #8084: autodoc: KeyError is raised on documenting an attribute of the broken
  class
* #8091: autodoc: AttributeError is raised on documenting an attribute on Python
  3.5.2
* #8099: autodoc: NameError is raised when target code uses ``TYPE_CHECKING``
* C++, fix parsing of template template paramters, broken by the fix of #7944

Release 3.2.0 (released Aug 08, 2020)
=====================================

Deprecated
----------

* ``sphinx.ext.autodoc.members_set_option()``
* ``sphinx.ext.autodoc.merge_special_members_option()``
* ``sphinx.writers.texinfo.TexinfoWriter.desc``
* C, parsing of pre-v3 style type directives and roles, along with the options
  :confval:`c_allow_pre_v3` and :confval:`c_warn_on_allowed_pre_v3`.

Features added
--------------

* #2076: autodoc: Allow overriding of exclude-members in skip-member function
* #8034: autodoc: ``:private-member:`` can take an explicit list of member names
  to be documented
* #2024: autosummary: Add :confval:`autosummary_filename_map` to avoid conflict
  of filenames between two object with different case
* #8011: autosummary: Support instance attributes as a target of autosummary
  directive
* #7849: html: Add :confval:`html_codeblock_linenos_style` to change the style
  of line numbers for code-blocks
* #7853: C and C++, support parameterized GNU style attributes.
* #7888: napoleon: Add aliases Warn and Raise.
* #7690: napoleon: parse type strings and make them hyperlinks as possible.  The
  conversion rule can be updated via :confval:`napoleon_type_aliases`
* #8049: napoleon: Create a hyperlink for each the type of parameter when
  :confval:`napoleon_use_params` is False
* C, added :rst:dir:`c:alias` directive for inserting copies
  of existing declarations.
* #7745: html: inventory is broken if the docname contains a space
* #7991: html search: Allow searching for numbers
* #7902: html theme: Add a new option :confval:`globaltoc_maxdepth` to control
  the behavior of globaltoc in sidebar
* #7840: i18n: Optimize the dependencies check on bootstrap
* #7768: i18n: :confval:`figure_language_filename` supports ``docpath`` token
* #5208: linkcheck: Support checks for local links
* #5090: setuptools: Link verbosity to distutils' -v and -q option
* #6698: doctest: Add ``:trim-doctest-flags:`` and ``:no-trim-doctest-flags:``
  options to doctest, testcode and testoutput directives
* #7052: add ``:noindexentry:`` to the Python, C, C++, and Javascript domains.
  Update the documentation to better reflect the relationship between this option
  and the ``:noindex:`` option.
* #7899: C, add possibility of parsing of some pre-v3 style type directives and
  roles and try to convert them to equivalent v3 directives/roles.
  Set the new option :confval:`c_allow_pre_v3` to ``True`` to enable this.
  The warnings printed from this functionality can be suppressed by setting
  :confval:`c_warn_on_allowed_pre_v3`` to ``True``.
  The functionality is immediately deprecated.
* #7999: C, add support for named variadic macro arguments.
* #8071: Allow to suppress "self referenced toctrees" warning

Bugs fixed
----------

* #7886: autodoc: TypeError is raised on mocking generic-typed classes
* #7935: autodoc: function signature is not shown when the function has a
  parameter having ``inspect._empty`` as its default value
* #7901: autodoc: type annotations for overloaded functions are not resolved
* #904: autodoc: An instance attribute cause a crash of autofunction directive
* #1362: autodoc: ``private-members`` option does not work for class attributes
* #7983: autodoc: Generator type annotation is wrongly rendered in py36
* #8030: autodoc: An uninitialized annotated instance variable is not documented
  when ``:inherited-members:`` option given
* #8032: autodoc: A type hint for the instance variable defined at parent class
  is not shown in the document of the derived class
* #8041: autodoc: An annotated instance variable on super class is not
  documented when derived class has other annotated instance variables
* #7839: autosummary: cannot handle umlauts in function names
* #7865: autosummary: Failed to extract summary line when abbreviations found
* #7866: autosummary: Failed to extract correct summary line when docstring
  contains a hyperlink target
* #7469: autosummary: "Module attributes" header is not translatable
* #7940: apidoc: An extra newline is generated at the end of the rst file if a
  module has submodules
* #4258: napoleon: decorated special methods are not shown
* #7799: napoleon: parameters are not escaped for combined params in numpydoc
* #7780: napoleon: multiple paramaters declaration in numpydoc was wrongly
  recognized when napoleon_use_params=True
* #7715: LaTeX: ``numfig_secnum_depth > 1`` leads to wrong figure links
* #7846: html theme: XML-invalid files were generated
* #7894: gettext: Wrong source info is shown when using rst_epilog
* #7691: linkcheck: HEAD requests are not used for checking
* #4888: i18n: Failed to add an explicit title to ``:ref:`` role on translation
* #7928: py domain: failed to resolve a type annotation for the attribute
* #8008: py domain: failed to parse a type annotation containing ellipsis
* #7994: std domain: option directive does not generate old node_id compatible
  with 2.x or older
* #7968: i18n: The content of ``math`` directive is interpreted as reST on
  translation
* #7768: i18n: The ``root`` element for :confval:`figure_language_filename` is
  not a path that user specifies in the document
* #7993: texinfo: TypeError is raised for nested object descriptions
* #7993: texinfo: a warning not supporting desc_signature_line node is shown
* #7869: :rst:role:`abbr` role without an explanation will show the explanation
  from the previous abbr role
* #8048: graphviz: graphviz.css was copied on building non-HTML document
* C and C++, removed ``noindex`` directive option as it did
  nothing.
* #7619: Duplicated node IDs are generated if node has multiple IDs
* #2050: Symbols sections are appeared twice in the index page
* #8017: Fix circular import in sphinx.addnodes
* #7986: CSS: make "highlight" selector more robust
* #7944: C++, parse non-type template parameters starting with
  a dependent qualified name.
* C, don't deepcopy the entire symbol table and make a mess every time an
  enumerator is handled.

Release 3.1.2 (released Jul 05, 2020)
=====================================

Incompatible changes
--------------------

* #7650: autodoc: the signature of base function will be shown for decorated
  functions, not a signature of decorator

Bugs fixed
----------

* #7844: autodoc: Failed to detect module when relative module name given
* #7856: autodoc: AttributeError is raised when non-class object is given to
  the autoclass directive
* #7850: autodoc: KeyError is raised for invalid mark up when autodoc_typehints
  is 'description'
* #7812: autodoc: crashed if the target name matches to both an attribute and
  module that are same name
* #7650: autodoc: function signature becomes ``(*args, **kwargs)`` if the
  function is decorated by generic decorator
* #7812: autosummary: generates broken stub files if the target code contains
  an attribute and module that are same name
* #7806: viewcode: Failed to resolve viewcode references on 3rd party builders
* #7838: html theme: List items have extra vertical space
* #7878: html theme: Undesired interaction between "overflow" and "float"

Release 3.1.1 (released Jun 14, 2020)
=====================================

Incompatible changes
--------------------

* #7808: napoleon: a type for attribute are represented as typed field

Features added
--------------

* #7807: autodoc: Show detailed warning when type_comment is mismatched with its
  signature

Bugs fixed
----------

* #7808: autodoc: Warnings raised on variable and attribute type annotations
* #7802: autodoc: EOFError is raised on parallel build
* #7821: autodoc: TypeError is raised for overloaded C-ext function
* #7805: autodoc: an object which descriptors returns is unexpectedly documented
* #7807: autodoc: wrong signature is shown for the function using contextmanager
* #7812: autosummary: generates broken stub files if the target code contains
  an attribute and module that are same name
* #7808: napoleon: Warnings raised on variable and attribute type annotations
* #7811: sphinx.util.inspect causes circular import problem

Release 3.1.0 (released Jun 08, 2020)
=====================================

Dependencies
------------

* #7746: mathjax: Update to 2.7.5

Incompatible changes
--------------------

* #7477: imgconverter: Invoke "magick convert" command by default on Windows

Deprecated
----------

* The first argument for sphinx.ext.autosummary.generate.AutosummaryRenderer has
  been changed to Sphinx object
* ``sphinx.ext.autosummary.generate.AutosummaryRenderer`` takes an object type
  as an argument
* The ``ignore`` argument of ``sphinx.ext.autodoc.Documenter.get_doc()``
* The ``template_dir`` argument of ``sphinx.ext.autosummary.generate.
  AutosummaryRenderer``
* The ``module`` argument of ``sphinx.ext.autosummary.generate.
  find_autosummary_in_docstring()``
* The ``builder`` argument of ``sphinx.ext.autosummary.generate.
  generate_autosummary_docs()``
* The ``template_dir`` argument of ``sphinx.ext.autosummary.generate.
  generate_autosummary_docs()``
* The ``ignore`` argument of ``sphinx.util.docstring.prepare_docstring()``
* ``sphinx.ext.autosummary.generate.AutosummaryRenderer.exists()``
* ``sphinx.util.rpartition()``

Features added
--------------

* LaTeX: Make the ``toplevel_sectioning`` setting optional in LaTeX theme
* LaTeX: Allow to override papersize and pointsize from LaTeX themes
* LaTeX: Add :confval:`latex_theme_options` to override theme options
* #7410: Allow to suppress "circular toctree references detected" warnings using
  :confval:`suppress_warnings`
* C, added scope control directives, :rst:dir:`c:namespace`,
  :rst:dir:`c:namespace-push`, and :rst:dir:`c:namespace-pop`.
* #2044: autodoc: Suppress default value for instance attributes
* #7473: autodoc: consider a member public if docstring contains
  ``:meta public:`` in info-field-list
* #7487: autodoc: Allow to generate docs for singledispatch functions by
  py:autofunction
* #7143: autodoc: Support final classes and methods
* #7384: autodoc: Support signatures defined by ``__new__()``, metaclasses and
  builtin base classes
* #2106: autodoc: Support multiple signatures on docstring
* #4422: autodoc: Support GenericAlias in Python 3.7 or above
* #3610: autodoc: Support overloaded functions
* #7722: autodoc: Support TypeVar
* #7466: autosummary: headings in generated documents are not translated
* #7490: autosummary: Add ``:caption:`` option to autosummary directive to set a
  caption to the toctree
* #7469: autosummary: Support module attributes
* #248, #6040: autosummary: Add ``:recursive:`` option to autosummary directive
  to generate stub files recursively
* #4030: autosummary: Add :confval:`autosummary_context` to add template
  variables for custom templates
* #7530: html: Support nested <kbd> elements
* #7481: html theme: Add right margin to footnote/citation labels
* #7482, #7717: html theme: CSS spacing for code blocks with captions and line
  numbers
* #7443: html theme: Add new options :confval:`globaltoc_collapse` and
  :confval:`globaltoc_includehidden` to control the behavior of globaltoc in
  sidebar
* #7484: html theme: Avoid clashes between sidebar and other blocks
* #7476: html theme: Relbar breadcrumb should contain current page
* #7506: html theme: A canonical URL is not escaped
* #7533: html theme: Avoid whitespace at the beginning of genindex.html
* #7541: html theme: Add a "clearer" at the end of the "body"
* #7542: html theme: Make admonition/topic/sidebar scrollable
* #7543: html theme: Add top and bottom margins to tables
* #7695: html theme: Add viewport meta tag for basic theme
* #7721: html theme: classic: default codetextcolor/codebgcolor doesn't override
  Pygments
* C and C++: allow semicolon in the end of declarations.
* C++, parse parameterized noexcept specifiers.
* #7294: C++, parse expressions with user-defined literals.
* C++, parse trailing return types.
* #7143: py domain: Add ``:final:`` option to :rst:dir:`py:class:`,
  :rst:dir:`py:exception:` and :rst:dir:`py:method:` directives
* #7596: py domain: Change a type annotation for variables to a hyperlink
* #7770: std domain: :rst:dir:`option` directive support arguments in the form
  of ``foo[=bar]``
* #7582: napoleon: a type for attribute are represented like type annotation
* #7734: napoleon: overescaped trailing underscore on attribute
* #7247: linkcheck: Add :confval:`linkcheck_request_headers` to send custom HTTP
  headers for specific host
* #7792: setuptools: Support ``--verbosity`` option
* #7683: Add ``allowed_exceptions`` parameter to ``Sphinx.emit()`` to allow
  handlers to raise specified exceptions
* #7295: C++, parse (trailing) requires clauses.

Bugs fixed
----------

* #6703: autodoc: incremental build does not work for imported objects
* #7564: autodoc: annotations not to be shown for descriptors
* #6588: autodoc: Decorated inherited method has no documentation
* #7469: autodoc: The change of autodoc-process-docstring for variables is
  cached unexpectedly
* #7559: autodoc: misdetects a sync function is async
* #6857: autodoc: failed to detect a classmethod on Enum class
* #7562: autodoc: a typehint contains spaces is wrongly rendered under
  autodoc_typehints='description' mode
* #7551: autodoc: failed to import nested class
* #7362: autodoc: does not render correct signatures for built-in functions
* #7654: autodoc: ``Optional[Union[foo, bar]]`` is presented as
  ``Union[foo, bar, None]``
* #7629: autodoc: autofunction emits an unfriendly warning if an invalid object
  specified
* #7650: autodoc: undecorated signature is shown for decorated functions
* #7676: autodoc: typo in the default value of autodoc_member_order
* #7676: autodoc: wrong value for :member-order: option is ignored silently
* #7676: autodoc: member-order="bysource" does not work for C module
* #3673: autodoc: member-order="bysource" does not work for a module having
  __all__
* #7668: autodoc: wrong retann value is passed to a handler of
  autodoc-proccess-signature
* #7711: autodoc: fails with ValueError when processing numpy objects
* #7791: autodoc: TypeError is raised on documenting singledispatch function
* #7551: autosummary: a nested class is indexed as non-nested class
* #7661: autosummary: autosummary directive emits warnings twices if failed to
  import the target module
* #7685: autosummary: The template variable "members" contains imported members
  even if :confval:`autossummary_imported_members` is False
* #7671: autosummary: The location of import failure warning is missing
* #7535: sphinx-autogen: crashes when custom template uses inheritance
* #7536: sphinx-autogen: crashes when template uses i18n feature
* #7781: sphinx-build: Wrong error message when outdir is not directory
* #7653: sphinx-quickstart: Fix multiple directory creation for nested relpath
* #2785: html: Bad alignment of equation links
* #7718: html theme: some themes does not respect background color of Pygments
  style (agogo, haiku, nature, pyramid, scrolls, sphinxdoc and traditional)
* #7544: html theme: inconsistent padding in admonitions
* #7581: napoleon: bad parsing of inline code in attribute docstrings
* #7628: imgconverter: runs imagemagick once unnecessary for builders not
  supporting images
* #7610: incorrectly renders consecutive backslashes for docutils-0.16
* #7646: handle errors on event handlers
* #4187: LaTeX: EN DASH disappears from PDF bookmarks in Japanese documents
* #7701: LaTeX: Anonymous indirect hyperlink target causes duplicated labels
* #7723: LaTeX: pdflatex crashed when URL contains a single quote
* #7756: py domain: The default value for positional only argument is not shown
* #7760: coverage: Add :confval:`coverage_show_missing_items` to show coverage
  result to console
* C++, fix rendering and xrefs in nested names explicitly starting
  in global scope, e.g., ``::A::B``.
* C, fix rendering and xrefs in nested names explicitly starting
  in global scope, e.g., ``.A.B``.
* #7763: C and C++, don't crash during display stringification of unary
  expressions and fold expressions.

Release 3.0.4 (released May 27, 2020)
=====================================

Bugs fixed
----------

* #7567: autodoc: parametrized types are shown twice for generic types
* #7637: autodoc: system defined TypeVars are shown in Python 3.9
* #7696: html: Updated jQuery version from 3.4.1 to 3.5.1 for security reasons
* #7611: md5 fails when OpenSSL FIPS is enabled
* #7626: release package does not contain ``CODE_OF_CONDUCT``

Release 3.0.3 (released Apr 26, 2020)
=====================================

Features added
--------------

* C, parse array declarators with static, qualifiers, and VLA specification.

Bugs fixed
----------

* #7516: autodoc: crashes if target object raises an error on accessing
  its attributes

Release 3.0.2 (released Apr 19, 2020)
=====================================

Features added
--------------

* C, parse attributes and add :confval:`c_id_attributes`
  and :confval:`c_paren_attributes` to support user-defined attributes.

Bugs fixed
----------

* #7461: py domain: fails with IndexError for empty tuple in type annotation
* #7510: py domain: keyword-only arguments are documented as having a default of
  None
* #7418: std domain: :rst:role:`term` role could not match case-insensitively
* #7461: autodoc: empty tuple in type annotation is not shown correctly
* #7479: autodoc: Sphinx builds has been slower since 3.0.0 on mocking
* C++, fix spacing issue in east-const declarations.
* #7414: LaTeX: Xindy language options were incorrect
* sphinx crashes with ImportError on python3.5.1

Release 3.0.1 (released Apr 11, 2020)
=====================================

Incompatible changes
--------------------

* #7418: std domain: :rst:dir:`term` role becomes case sensitive

Bugs fixed
----------

* #7428: py domain: a reference to class ``None`` emits a nitpicky warning
* #7445: py domain: a return annotation ``None`` in the function signature is
  not converted to a hyperlink when using intersphinx
* #7418: std domain: duplication warning for glossary terms is case insensitive
* #7438: C++, fix merging overloaded functions in parallel builds.
* #7422: autodoc: fails with ValueError when using autodoc_mock_imports
* #7435: autodoc: ``autodoc_typehints='description'`` doesn't suppress typehints
  in signature for classes/methods
* #7451: autodoc: fails with AttributeError when an object returns non-string
  object as a ``__doc__`` member
* #7423: crashed when giving a non-string object to logger
* #7479: html theme: Do not include xmlns attribute with HTML 5 doctype
* #7426: html theme: Escape some links in HTML templates

Release 3.0.0 (released Apr 06, 2020)
=====================================

Dependencies
------------

3.0.0b1

* LaTeX: drop dependency on :program:`extractbb` for image inclusion in
  Japanese documents as ``.xbb`` files are unneeded by :program:`dvipdfmx`
  since TeXLive2015 (refs: #6189)
* babel-2.0 or above is available (Unpinned)

Incompatible changes
--------------------

3.0.0b1

* Drop features and APIs deprecated in 1.8.x
* #247: autosummary: stub files are overwritten automatically by default.  see
  :confval:`autosummary_generate_overwrite` to change the behavior
* #5923: autodoc: the members of ``object`` class are not documented by default
  when ``:inherited-members:`` and ``:special-members:`` are given.
* #6830: py domain: ``meta`` fields in info-field-list becomes reserved.  They
  are not displayed on output document now
* #6417: py domain: doctree of desc_parameterlist has been changed.  The
  argument names, annotations and default values are wrapped with inline node
* The structure of ``sphinx.events.EventManager.listeners`` has changed
* Due to the scoping changes for :rst:dir:`productionlist` some uses of
  :rst:role:`token` must be modified to include the scope which was previously
  ignored.
* #6903: Internal data structure of Python, reST and standard domains have
  changed.  The node_id is added to the index of objects and modules.  Now they
  contains a pair of docname and node_id for cross reference.
* #7276: C++ domain: Non intended behavior is removed such as ``say_hello_``
  links to ``.. cpp:function:: say_hello()``
* #7210: js domain: Non intended behavior is removed such as ``parseInt_`` links
  to ``.. js:function:: parseInt``
* #7229: rst domain: Non intended behavior is removed such as ``numref_`` links
  to ``.. rst:role:: numref``
* #6903: py domain: Non intended behavior is removed such as ``say_hello_``
  links to ``.. py:function:: say_hello()``
* #7246: py domain: Drop special cross reference helper for exceptions,
  functions and methods
* The C domain has been rewritten, with additional directives and roles.
  The existing ones are now more strict, resulting in new warnings.
* The attribute ``sphinx_cpp_tagname`` in the ``desc_signature_line`` node
  has been renamed to ``sphinx_line_type``.
* #6462: double backslashes in domain directives are no longer replaced by
  single backslashes as default. A new configuration value
  :confval:`strip_signature_backslash` can be used by users to reenable it.

3.0.0 final

* #7222: ``sphinx.util.inspect.unwrap()`` is renamed to ``unwrap_all()``

Deprecated
----------

3.0.0b1

* ``desc_signature['first']``
* ``sphinx.directives.DescDirective``
* ``sphinx.domains.std.StandardDomain.add_object()``
* ``sphinx.domains.python.PyDecoratorMixin``
* ``sphinx.ext.autodoc.get_documenters()``
* ``sphinx.ext.autosummary.process_autosummary_toc()``
* ``sphinx.parsers.Parser.app``
* ``sphinx.testing.path.Path.text()``
* ``sphinx.testing.path.Path.bytes()``
* ``sphinx.util.inspect.getargspec()``
* ``sphinx.writers.latex.LaTeXWriter.format_docclass()``

Features added
--------------

3.0.0b1

* #247: autosummary: Add :confval:`autosummary_generate_overwrite` to overwrite
  old stub file
* #5923: autodoc: ``:inherited-members:`` option takes a name of anchestor class
  not to document inherited members of the class and uppers
* #6830: autodoc: consider a member private if docstring contains
  ``:meta private:`` in info-field-list
* #7165: autodoc: Support Annotated type (PEP-593)
* #2815: autodoc: Support singledispatch functions and methods
* #7079: autodoc: :confval:`autodoc_typehints` accepts ``"description"``
  configuration.  It shows typehints as object description
* #7314: apidoc: Propagate ``--maxdepth`` option through package documents
* #6558: glossary: emit a warning for duplicated glossary entry
* #3106: domain: Register hyperlink target for index page automatically
* #6558: std domain: emit a warning for duplicated generic objects
* #6830: py domain: Add new event: :event:`object-description-transform`
* #6895: py domain: Do not emit nitpicky warnings for built-in types
* py domain: Support lambda functions in function signature
* #6417: py domain: Allow to make a style for arguments of functions and methods
* #7238, #7239: py domain: Emit a warning on describing a python object if the
  entry is already added as the same name
* #7341: py domain: type annotations in singature are converted to cross refs
* Support priority of event handlers. For more detail, see
  :py:meth:`.Sphinx.connect()`
* #3077: Implement the scoping for :rst:dir:`productionlist` as indicated
  in the documentation.
* #1027: Support backslash line continuation in :rst:dir:`productionlist`.
* #7108: config: Allow to show an error message from conf.py via ``ConfigError``
* #7032: html: :confval:`html_scaled_image_link` will be disabled for images having
  ``no-scaled-link`` class
* #7144: Add CSS class indicating its domain for each desc node
* #7211: latex: Use babel for Chinese document when using XeLaTeX
* #6672: LaTeX: Support LaTeX Theming (experimental)
* #7005: LaTeX: Add LaTeX styling macro for :rst:role:`kbd` role
* #7220: genindex: Show "main" index entries at first
* #7103: linkcheck: writes all links to ``output.json``
* #7025: html search: full text search can be disabled for individual document
  using ``:nosearch:`` file-wide metadata
* #7293: html search: Allow to override JavaScript splitter via
  ``SearchLanguage.js_splitter_code``
* #7142: html theme: Add a theme option: ``pygments_dark_style`` to switch the
  style of code-blocks in dark mode
* The C domain has been rewritten adding for example:

  - Cross-referencing respecting the current scope.
  - Possible to document anonymous entities.
  - More specific directives and roles for each type of entitiy,
    e.g., handling scoping of enumerators.
  - New role :rst:role:`c:expr` for rendering expressions and types
    in text.

* Added ``SphinxDirective.get_source_info()``
  and ``SphinxRole.get_source_info()``.
* #7324: sphinx-build: Emit a warning if multiple files having different file
  extensions for same document found

3.0.0 final

* Added ``ObjectDescription.transform_content()``.

Bugs fixed
----------

3.0.0b1

* C++, fix cross reference lookup in certain cases involving
  function overloads.
* #5078: C++, fix cross reference lookup when a directive contains multiple
  declarations.
* C++, suppress warnings for directly dependent typenames in cross references
  generated automatically in signatures.
* #5637: autodoc: Incorrect handling of nested class names on show-inheritance
* #7267: autodoc: error message for invalid directive options has wrong location
* #7329: autodoc: info-field-list is wrongly generated from type hints into the
  class description even if ``autoclass_content='class'`` set
* #7331: autodoc: a cython-function is not recognized as a function
* #5637: inheritance_diagram: Incorrect handling of nested class names
* #7139: ``code-block:: guess`` does not work
* #7325: html: source_suffix containing dot leads to wrong source link
* #7357: html: Resizing SVG image fails with ValueError
* #7278: html search: Fix use of ``html_file_suffix`` instead of
  ``html_link_suffix`` in search results
* #7297: html theme: ``bizstyle`` does not support ``sidebarwidth``
* #3842: singlehtml: Path to images broken when master doc is not in source root
* #7179: std domain: Fix whitespaces are suppressed on referring GenericObject
* #7289: console: use bright colors instead of bold
* #1539: C, parse array types.
* #2377: C, parse function pointers even in complex types.
* #7345: sphinx-build: Sphinx crashes if output directory exists as a file
* #7290: sphinx-build: Ignore bdb.BdbQuit when handling exceptions
* #6240: napoleon: Attributes and Methods sections ignore :noindex: option

3.0.0 final

* #7364: autosummary: crashed when :confval:`autosummary_generate` is False
* #7370: autosummary: raises UnboundLocalError when unknown module given
* #7367: C++, alternate operator spellings are now supported.
* C, alternate operator spellings are now supported.
* #7368: C++, comma operator in expressions, pack expansion in template
  argument lists, and more comprehensive error messages in some cases.
* C, C++, fix crash and wrong duplicate warnings related to anon symbols.
* #6477: Escape first "!" in a cross reference linking no longer possible
* #7219: py domain: The index entry generated by ``py:function`` directive is
  different with one from ``index`` directive with "builtin" type
* #7301: capital characters are not allowed for node_id
* #7301: epub: duplicated node_ids are generated
* #6564: html: a width of table was ignored on HTML builder
* #7401: Incorrect argument is passed for :event:`env-get-outdated` handlers
* #7355: autodoc: a signature of cython-function is not recognized well
* #7222: autodoc: ``__wrapped__`` functions are not documented correctly
* #7409: intersphinx: ValueError is raised when an extension sets up
  :confval:`intersphinx_mapping` on :event:`config-inited` event
* #7343: Sphinx builds has been slower since 2.4.0 on debug mode

Release 2.4.4 (released Mar 05, 2020)
=====================================

Bugs fixed
----------

* #7197: LaTeX: platex cause error to build image directive with target url
* #7223: Sphinx builds has been slower since 2.4.0

Release 2.4.3 (released Feb 22, 2020)
=====================================

Bugs fixed
----------

* #7184: autodoc: ``*args`` and ``**kwarg`` in type comments are not handled
  properly
* #7189: autodoc: classmethod coroutines are not detected
* #7183: intersphinx: ``:attr:`` reference to property is broken
* #6244, #6387: html search: Search breaks/hangs when built with dirhtml builder
* #7195: todo: emit doctree-resolved event with non-document node incorrectly

Release 2.4.2 (released Feb 19, 2020)
=====================================

Bugs fixed
----------

* #7138: autodoc: ``autodoc.typehints`` crashed when variable has unbound object
  as a value
* #7156: autodoc: separator for keyword only arguments is not shown
* #7146: autodoc: IndexError is raised on suppressed type_comment found
* #7161: autodoc: typehints extension does not support parallel build
* #7178: autodoc: TypeError is raised on fetching type annotations
* #7151: crashed when extension assigns a value to ``env.indexentries``
* #7170: text: Remove debug print
* #7137: viewcode: Avoid to crash when non-python code given

Release 2.4.1 (released Feb 11, 2020)
=====================================

Bugs fixed
----------

* #7120: html: crashed when on scaling SVG images which have float dimensions
* #7126: autodoc: TypeError: 'getset_descriptor' object is not iterable

Release 2.4.0 (released Feb 09, 2020)
=====================================

Deprecated
----------

* The ``decode`` argument of ``sphinx.pycode.ModuleAnalyzer()``
* ``sphinx.directives.other.Index``
* ``sphinx.environment.temp_data['gloss_entries']``
* ``sphinx.environment.BuildEnvironment.indexentries``
* ``sphinx.environment.collectors.indexentries.IndexEntriesCollector``
* ``sphinx.ext.apidoc.INITPY``
* ``sphinx.ext.apidoc.shall_skip()``
* ``sphinx.io.FiletypeNotFoundError``
* ``sphinx.io.get_filetype()``
* ``sphinx.pycode.ModuleAnalyzer.encoding``
* ``sphinx.roles.Index``
* ``sphinx.util.detect_encoding()``
* ``sphinx.util.get_module_source()``
* ``sphinx.util.inspect.Signature``
* ``sphinx.util.inspect.safe_getmembers()``
* ``sphinx.writers.latex.LaTeXTranslator.settings.author``
* ``sphinx.writers.latex.LaTeXTranslator.settings.contentsname``
* ``sphinx.writers.latex.LaTeXTranslator.settings.docclass``
* ``sphinx.writers.latex.LaTeXTranslator.settings.docname``
* ``sphinx.writers.latex.LaTeXTranslator.settings.title``
* ``sphinx.writers.latex.ADDITIONAL_SETTINGS``
* ``sphinx.writers.latex.DEFAULT_SETTINGS``
* ``sphinx.writers.latex.LUALATEX_DEFAULT_FONTPKG``
* ``sphinx.writers.latex.PDFLATEX_DEFAULT_FONTPKG``
* ``sphinx.writers.latex.XELATEX_DEFAULT_FONTPKG``
* ``sphinx.writers.latex.XELATEX_GREEK_DEFAULT_FONTPKG``

Features added
--------------

* #6910: inheritance_diagram: Make the background of diagrams transparent
* #6446: duration: Add ``sphinx.ext.durations`` to inspect which documents slow
  down the build
* #6837: LaTeX: Support a nested table
* #7115: LaTeX: Allow to override LATEXOPTS and LATEXMKOPTS via environment
  variable
* #6966: graphviz: Support ``:class:`` option
* #6696: html: ``:scale:`` option of image/figure directive not working for SVG
  images (imagesize-1.2.0 or above is required)
* #6994: imgconverter: Support illustrator file (.ai) to .png conversion
* autodoc: Support Positional-Only Argument separator (PEP-570 compliant)
* autodoc: Support type annotations for variables
* #2755: autodoc: Add new event: :event:`autodoc-before-process-signature`
* #2755: autodoc: Support type_comment style (ex. ``# type: (str) -> str``)
  annotation (python3.8+ or `typed_ast <https://github.com/python/typed_ast>`_
  is required)
* #7051: autodoc: Support instance variables without defaults (PEP-526)
* #6418: autodoc: Add a new extension ``sphinx.ext.autodoc.typehints``. It shows
  typehints as object description if ``autodoc_typehints = "description"`` set.
  This is an experimental extension and it will be integrated into autodoc core
  in Sphinx-3.0
* SphinxTranslator now calls visitor/departure method for super node class if
  visitor/departure method for original node class not found
* #6418: Add new event: :event:`object-description-transform`
* py domain: :rst:dir:`py:data` and :rst:dir:`py:attribute` take new options
  named ``:type:`` and ``:value:`` to describe its type and initial value
* #6785: py domain: ``:py:attr:`` is able to refer properties again
* #6772: apidoc: Add ``-q`` option for quiet mode

Bugs fixed
----------

* #6925: html: Remove redundant type="text/javascript" from <script> elements
* #7112: html: SVG image is not layouted as float even if aligned
* #6906, #6907: autodoc: failed to read the source codes encoeded in cp1251
* #6961: latex: warning for babel shown twice
* #7059: latex: LaTeX compilation falls into infinite loop (wrapfig issue)
* #6581: latex: ``:reversed:`` option for toctree does not effect to LaTeX build
* #6559: Wrong node-ids are generated in glossary directive
* #6986: apidoc: misdetects module name for .so file inside module
* #6899: apidoc: private members are not shown even if ``--private`` given
* #6327: apidoc: Support a python package consisted of __init__.so file
* #6999: napoleon: fails to parse tilde in :exc: role
* #7019: gettext: Absolute path used in message catalogs
* #7023: autodoc: nested partial functions are not listed
* #7023: autodoc: partial functions imported from other modules are listed as
  module members without :impoprted-members: option
* #6889: autodoc: Trailing comma in ``:members::`` option causes cryptic warning
* #6568: autosummary: ``autosummary_imported_members`` is ignored on generating
  a stub file for submodule
* #7055: linkcheck: redirect is treated as an error
* #7088: HTML template: If ``navigation_with_keys`` option is activated,
  modifier keys are ignored, which means the feature can interfere with browser
  features
* #7090: std domain: Can't assign numfig-numbers for custom container nodes
* #7106: std domain: enumerated nodes are marked as duplicated when extensions
  call ``note_explicit_target()``
* #7095: dirhtml: Cross references are broken via intersphinx and ``:doc:`` role
* C++:

  - Don't crash when using the ``struct`` role in some cases.
  - Don't warn when using the ``var``/``member`` role for function
    parameters.
  - Render call and braced-init expressions correctly.
* #7097: Filenames of images generated by
  ``sphinx.transforms.post_transforms.images.ImageConverter``
  or its subclasses (used for latex build) are now sanitized,
  to prevent broken paths

Release 2.3.1 (released Dec 22, 2019)
=====================================

Bugs fixed
----------

* #6936: sphinx-autogen: raises AttributeError

Release 2.3.0 (released Dec 15, 2019)
=====================================

Incompatible changes
--------------------

* #6742: ``end-before`` option of :rst:dir:`literalinclude` directive does not
  match the first line of the code block.
* #1331: Change default User-Agent header to ``"Sphinx/X.Y.Z requests/X.Y.Z
  python/X.Y.Z"``.  It can be changed via :confval:`user_agent`.
* #6867: text: content of admonitions starts after a blank line

Deprecated
----------

* ``sphinx.builders.gettext.POHEADER``
* ``sphinx.io.SphinxStandaloneReader.app``
* ``sphinx.io.SphinxStandaloneReader.env``
* ``sphinx.util.texescape.tex_escape_map``
* ``sphinx.util.texescape.tex_hl_escape_map_new``
* ``sphinx.writers.latex.LaTeXTranslator.no_contractions``

Features added
--------------

* #6707: C++, support bit-fields.
* #267: html: Eliminate prompt characters of doctest block from copyable text
* #6548: html: Use favicon for OpenSearch if available
* #6729: html theme: agogo theme now supports ``rightsidebar`` option
* #6780: Add PEP-561 Support
* #6762: latex: Allow to load additional LaTeX packages via ``extrapackages`` key
  of :confval:`latex_elements`
* #1331: Add new config variable: :confval:`user_agent`
* #6000: LaTeX: have backslash also be an inline literal word wrap break
  character
* #4186: LaTeX: Support upLaTeX as a new :confval:`latex_engine` (experimental)
* #6812: Improve a warning message when extensions are not parallel safe
* #6818: Improve Intersphinx performance for multiple remote inventories.
* #2546: apidoc: .so file support
* #6798: autosummary: emit ``autodoc-skip-member`` event on generating stub file
* #6483: i18n: make explicit titles in toctree translatable
* #6816: linkcheck: Add :confval:`linkcheck_auth` option to provide
  authentication information when doing ``linkcheck`` builds
* #6872: linkcheck: Handles HTTP 308 Permanent Redirect
* #6613: html: Wrap section number in span tag
* #6781: gettext: Add :confval:`gettext_last_translator' and
  :confval:`gettext_language_team` to customize headers of POT file

Bugs fixed
----------

* #6668: LaTeX: Longtable before header has incorrect distance
  (refs: `latex3/latex2e#173`_)

  .. _latex3/latex2e#173: https://github.com/latex3/latex2e/issues/173
* #6618: LaTeX: Avoid section names at the end of a page
* #6738: LaTeX: Do not replace unicode characters by LaTeX macros on unicode
  supported LaTeX engines: ¶, §, €, ∞, ±, →, ‣, –, superscript and subscript
  digits go through "as is" (as default OpenType font supports them)
* #6704: linkcheck: Be defensive and handle newly defined HTTP error code
* #6806: linkcheck: Failure on parsing content
* #6655: image URLs containing ``data:`` causes gettext builder crashed
* #6584: i18n: Error when compiling message catalogs on Hindi
* #6718: i18n: KeyError is raised if section title and table title are same
* #6743: i18n: :confval:`rst_prolog` breaks the translation
* #6708: mathbase: Some deprecated functions have removed
* #6709: autodoc: mock object does not work as a class decorator
* #5070: epub: Wrong internal href fragment links
* #6712: Allow not to install sphinx.testing as runtime (mainly for ALT Linux)
* #6741: html: search result was broken with empty :confval:`html_file_suffix`
* #6001: LaTeX does not wrap long code lines at backslash character
* #6804: LaTeX: PDF build breaks if admonition of danger type contains
  code-block long enough not to fit on one page
* #6809: LaTeX: code-block in a danger type admonition can easily spill over
  bottom of page
* #6793: texinfo: Code examples broken following "sidebar"
* #6813: An orphan warning is emitted for included document on Windows.  Thanks
  to @drillan
* #6850: Fix smartypants module calls re.sub() with wrong options
* #6824: HTML search: If a search term is partially matched in the title and
  fully matched in a text paragraph on the same page, the search does not
  include this match.
* #6848: config.py shouldn't pop extensions from overrides
* #6867: text: extra spaces are inserted to hyphenated words on folding lines
* #6886: LaTeX: xelatex converts straight double quotes into right curly ones
  (shows when :confval:`smartquotes` is ``False``)
* #6890: LaTeX: even with smartquotes off, PDF output transforms straight
  quotes and consecutive hyphens into curly quotes and dashes
* #6876: LaTeX: multi-line display of authors on title page has ragged edges
* #6887: Sphinx crashes with docutils-0.16b0
* #6920: sphinx-build: A console message is wrongly highlighted
* #6900: sphinx-build: ``-D`` option does not considers ``0`` and ``1`` as a
  boolean value

Release 2.2.2 (released Dec 03, 2019)
=====================================

Incompatible changes
--------------------

* #6803: For security reason of python, parallel mode is disabled on macOS and
  Python3.8+

Bugs fixed
----------

* #6776: LaTeX: 2019-10-01 LaTeX release breaks :file:`sphinxcyrillic.sty`
* #6815: i18n: French, Hindi, Chinese, Japanese and Korean translation messages
  has been broken
* #6803: parallel build causes AttributeError on macOS and Python3.8

Release 2.2.1 (released Oct 26, 2019)
=====================================

Bugs fixed
----------

* #6641: LaTeX: Undefined control sequence ``\sphinxmaketitle``
* #6710: LaTeX not well configured for Greek language as main language
* #6759: validation of html static paths and extra paths no longer throws
  an error if the paths are in different directories

Release 2.2.0 (released Aug 19, 2019)
=====================================

Incompatible changes
--------------------

* apidoc: template files are renamed to ``.rst_t``
* html: Field lists will be styled by grid layout

Deprecated
----------

* ``sphinx.domains.math.MathDomain.add_equation()``
* ``sphinx.domains.math.MathDomain.get_next_equation_number()``
* The ``info`` and ``warn`` arguments of
  ``sphinx.ext.autosummary.generate.generate_autosummary_docs()``
* ``sphinx.ext.autosummary.generate._simple_info()``
* ``sphinx.ext.autosummary.generate._simple_warn()``
* ``sphinx.ext.todo.merge_info()``
* ``sphinx.ext.todo.process_todo_nodes()``
* ``sphinx.ext.todo.process_todos()``
* ``sphinx.ext.todo.purge_todos()``

Features added
--------------

* #5124: graphviz: ``:graphviz_dot:`` option is renamed to ``:layout:``
* #1464: html: emit a warning if :confval:`html_static_path` and
  :confval:`html_extra_path` directories are inside output directory
* #6514: html: Add a label to search input for accessability purposes
* #5602: apidoc: Add ``--templatedir`` option
* #6475: Add ``override`` argument to ``app.add_autodocumenter()``
* #6310: imgmath: let :confval:`imgmath_use_preview` work also with the SVG
  format for images rendering inline math
* #6533: LaTeX: refactor visit_enumerated_list() to use ``\sphinxsetlistlabels``
* #6628: quickstart: Use ``https://docs.python.org/3/`` for default setting of
  :confval:`intersphinx_mapping`
* #6419: sphinx-build: give reasons why rebuilded

Bugs fixed
----------

* py domain: duplicated warning does not point the location of source code
* #6499: html: Sphinx never updates a copy of :confval:`html_logo` even if
  original file has changed
* #1125: html theme: scrollbar is hard to see on classic theme and macOS
* #5502: linkcheck: Consider HTTP 503 response as not an error
* #6439: Make generated download links reproducible
* #6486: UnboundLocalError is raised if broken extension installed
* #6567: autodoc: :confval:`autodoc_inherit_docstrings` does not effect to
  ``__init__()`` and ``__new__()``
* #6574: autodoc: :confval:`autodoc_member_order` does not refer order of
  imports when ``'bysource'`` order
* #6574: autodoc: missing type annotation for variadic and keyword parameters
* #6589: autodoc: Formatting issues with autodoc_typehints='none'
* #6605: autodoc: crashed when target code contains custom method-like objects
* #6498: autosummary: crashed with wrong autosummary_generate setting
* #6507: autosummary: crashes without no autosummary_generate setting
* #6511: LaTeX: autonumbered list can not be customized in LaTeX
  since Sphinx 1.8.0 (refs: #6533)
* #6531: Failed to load last environment object when extension added
* #736: Invalid sort in pair index
* #6527: :confval:`last_updated` wrongly assumes timezone as UTC
* #5592: std domain: :rst:dir:`option` directive registers an index entry for
  each comma separated option
* #6549: sphinx-build: Escaped characters in error messages
* #6545: doctest comments not getting trimmed since Sphinx 1.8.0
* #6561: glossary: Wrong hyperlinks are generated for non alphanumeric terms
* #6620: i18n: classifiers of definition list are not translated with
  docutils-0.15
* #6474: ``DocFieldTransformer`` raises AttributeError when given directive is
  not a subclass of ObjectDescription

Release 2.1.2 (released Jun 19, 2019)
=====================================

Bugs fixed
----------

* #6497: custom lexers fails highlighting when syntax error
* #6478, #6488: info field lists are incorrectly recognized

Release 2.1.1 (released Jun 10, 2019)
=====================================

Incompatible changes
--------------------

* #6447: autodoc: Stop to generate document for undocumented module variables

Bugs fixed
----------

* #6442: LaTeX: admonitions of :rst:dir:`note` type can get separated from
  immediately preceding section title by pagebreak
* #6448: autodoc: crashed when autodocumenting classes with ``__slots__ = None``
* #6451: autodoc: generates docs for "optional import"ed modules as variables
* #6452: autosummary: crashed when generating document of properties
* #6455: napoleon: docstrings for properties are not processed
* #6436: napoleon: "Unknown target name" error if variable name ends with
  underscore
* #6440: apidoc: missing blank lines between modules

Release 2.1.0 (released Jun 02, 2019)
=====================================

Incompatible changes
--------------------

* Ignore filenames without file extension given to ``Builder.build_specific()``
  API directly
* #6230: The anchor of term in glossary directive is changed if it is consisted
  by non-ASCII characters
* #4550: html: Centering tables by default using CSS
* #6239: latex: xelatex and xeCJK are used for Chinese documents by default
* ``Sphinx.add_lexer()`` now takes a Lexer class instead of instance.  An
  instance of lexers are still supported until Sphinx-3.x.

Deprecated
----------

* ``sphinx.builders.latex.LaTeXBuilder.apply_transforms()``
* ``sphinx.builders._epub_base.EpubBuilder.esc()``
* ``sphinx.directives.Acks``
* ``sphinx.directives.Author``
* ``sphinx.directives.Centered``
* ``sphinx.directives.Class``
* ``sphinx.directives.CodeBlock``
* ``sphinx.directives.Figure``
* ``sphinx.directives.HList``
* ``sphinx.directives.Highlight``
* ``sphinx.directives.Include``
* ``sphinx.directives.Index``
* ``sphinx.directives.LiteralInclude``
* ``sphinx.directives.Meta``
* ``sphinx.directives.Only``
* ``sphinx.directives.SeeAlso``
* ``sphinx.directives.TabularColumns``
* ``sphinx.directives.TocTree``
* ``sphinx.directives.VersionChange``
* ``sphinx.domains.python.PyClassmember``
* ``sphinx.domains.python.PyModulelevel``
* ``sphinx.domains.std.StandardDomain._resolve_citation_xref()``
* ``sphinx.domains.std.StandardDomain.note_citations()``
* ``sphinx.domains.std.StandardDomain.note_citation_refs()``
* ``sphinx.domains.std.StandardDomain.note_labels()``
* ``sphinx.environment.NoUri``
* ``sphinx.ext.apidoc.format_directive()``
* ``sphinx.ext.apidoc.format_heading()``
* ``sphinx.ext.apidoc.makename()``
* ``sphinx.ext.autodoc.importer.MockFinder``
* ``sphinx.ext.autodoc.importer.MockLoader``
* ``sphinx.ext.autodoc.importer.mock()``
* ``sphinx.ext.autosummary.autolink_role()``
* ``sphinx.ext.imgmath.DOC_BODY``
* ``sphinx.ext.imgmath.DOC_BODY_PREVIEW``
* ``sphinx.ext.imgmath.DOC_HEAD``
* ``sphinx.transforms.CitationReferences``
* ``sphinx.transforms.SmartQuotesSkipper``
* ``sphinx.util.docfields.DocFieldTransformer.preprocess_fieldtypes()``
* ``sphinx.util.node.find_source_node()``
* ``sphinx.util.i18n.find_catalog()``
* ``sphinx.util.i18n.find_catalog_files()``
* ``sphinx.util.i18n.find_catalog_source_files()``

For more details, see :ref:`deprecation APIs list <dev-deprecated-apis>`.

Features added
--------------

* Add a helper class ``sphinx.transforms.post_transforms.SphinxPostTransform``
* Add helper methods

  - ``PythonDomain.note_module()``
  - ``PythonDomain.note_object()``
  - ``SphinxDirective.set_source_info()``

* #6180: Support ``--keep-going`` with BuildDoc setup command
* ``math`` directive now supports ``:class:`` option
* todo: ``todo`` directive now supports ``:name:`` option
* Enable override via environment of ``SPHINXOPTS`` and ``SPHINXBUILD`` Makefile
  variables (refs: #6232, #6303)
* #6287: autodoc: Unable to document bound instance methods exported as module
  functions
* #6289: autodoc: :confval:`autodoc_default_options` now supports
  ``imported-members`` option
* #4777: autodoc: Support coroutine
* #744: autodoc: Support abstractmethod
* #6325: autodoc: Support attributes in __slots__.  For dict-style __slots__,
  autodoc considers values as a docstring of the attribute
* #6361: autodoc: Add :confval:`autodoc_typehints` to suppress typehints from
  signature
* #1063: autodoc: ``automodule`` directive now handles undocumented module level
  variables
* #6212 autosummary: Add :confval:`autosummary_imported_members` to display
  imported members on autosummary
* #6271: ``make clean`` is catastrophically broken if building into '.'
* #6363: Support ``%O%`` environment variable in make.bat
* #4777: py domain: Add ``:async:`` option to :rst:dir:`py:function` directive
* py domain: Add new options to :rst:dir:`py:method` directive

  - ``:abstractmethod:``
  - ``:async:``
  - ``:classmethod:``
  - ``:property:``
  - ``:staticmethod:``

* rst domain: Add :rst:dir:`directive:option` directive to describe the option
  for directive
* #6306: html: Add a label to search form for accessability purposes
* #4390: html: Consistent and semantic CSS for signatures
* #6358: The ``rawsource`` property of ``production`` nodes now contains the
  full production rule
* #6373: autosectionlabel: Allow suppression of warnings
* coverage: Support a new ``coverage_ignore_pyobjects`` option
* #6239: latex: Support to build Chinese documents

Bugs fixed
----------

* #6230: Inappropriate node_id has been generated by glossary directive if term
  is consisted by non-ASCII characters
* #6213: ifconfig: contents after headings are not shown
* commented term in glossary directive is wrongly recognized
* #6299: rst domain: rst:directive directive generates waste space
* #6379: py domain: Module index (py-modindex.html) has duplicate titles
* #6331: man: invalid output when doctest follows rubric
* #6351: "Hyperlink target is not referenced" message is shown even if
  referenced
* #6165: autodoc: ``tab_width`` setting of docutils has been ignored
* #6347: autodoc: crashes with a plain Tuple on Python 3.6 and 3.5
* #6311: autosummary: autosummary table gets confused by complex type hints
* #6350: autosummary: confused by an argument having some kind of default value
* Generated Makefiles lack a final EOL (refs: #6232)
* #6375: extlinks: Cannot escape angle brackets in link caption
* #6378: linkcheck: Send commonly used User-Agent
* #6387: html search: failed to search document with haiku and scrolls themes
* #6408: html search: Fix the ranking of search results
* #6406: Wrong year is returned for ``SOURCE_DATE_EPOCH``
* #6402: image directive crashes by unknown image format
* #6286: C++, allow 8 and 9 in hexadecimal integer literals.
* #6305: Fix the string in quickstart for 'path' argument of parser
* LaTeX: Figures in admonitions produced errors (refs: #6364)

Release 2.0.1 (released Apr 08, 2019)
=====================================

Bugs fixed
----------

* LaTeX: some system labels are not translated
* RemovedInSphinx30Warning is marked as pending
* deprecation warnings are not emitted

  - sphinx.application.CONFIG_FILENAME
  - sphinx.builders.htmlhelp
  - :confval:`viewcode_import`

* #6208: C++, properly parse full xrefs that happen to have a short xref as
  prefix
* #6220, #6225: napoleon: AttributeError is raised for raised section having
  references
* #6245: circular import error on importing SerializingHTMLBuilder
* #6243: LaTeX: 'releasename' setting for latex_elements is ignored
* #6244: html: Search function is broken with 3rd party themes
* #6263: html: HTML5Translator crashed with invalid field node
* #6262: html theme: The style of field lists has changed in bizstyle theme

Release 2.0.0 (released Mar 29, 2019)
=====================================

Dependencies
------------

2.0.0b1

* LaTeX builder now depends on TeX Live 2015 or above.
* LaTeX builder (with ``'pdflatex'`` :confval:`latex_engine`) will process
  Unicode Greek letters in text (not in math mark-up) via the text font and
  will not escape them to math mark-up. See the discussion of the
  ``'fontenc'`` key of :confval:`latex_elements`; such (optional) support for
  Greek adds, for example on Ubuntu xenial, the ``texlive-lang-greek`` and (if
  default font set-up is not modified) ``cm-super(-minimal)`` as additional
  Sphinx LaTeX requirements.
* LaTeX builder with :confval:`latex_engine` set to ``'xelatex'`` or to
  ``'lualatex'`` requires (by default) the ``FreeFont`` fonts,
  which in Ubuntu xenial are provided by package ``fonts-freefont-otf``, and
  e.g. in Fedora 29 via package ``texlive-gnu-freefont``.
* requests 2.5.0 or above
* The six package is no longer a dependency
* The sphinxcontrib-websupport package is no longer a dependency
* Some packages are separated to sub packages:

  - sphinxcontrib.applehelp
  - sphinxcontrib.devhelp
  - sphinxcontrib.htmlhelp
  - sphinxcontrib.jsmath
  - sphinxcontrib.serializinghtml
  - sphinxcontrib.qthelp

Incompatible changes
--------------------

2.0.0b1

* Drop python 2.7 and 3.4 support
* Drop docutils 0.11 support
* Drop features and APIs deprecated in 1.7.x
* The default setting for :confval:`master_doc` is changed to ``'index'`` which
  has been longly used as default of sphinx-quickstart.
* LaTeX: Move message resources to ``sphinxmessage.sty``
* LaTeX: Stop using ``\captions<lang>`` macro for some labels
* LaTeX: for ``'xelatex'`` and ``'lualatex'``, use the ``FreeFont`` OpenType
  fonts as default choice (refs: #5645)
* LaTeX: ``'xelatex'`` and ``'lualatex'`` now use ``\small`` in code-blocks
  (due to ``FreeMono`` character width) like ``'pdflatex'`` already did (due
  to ``Courier`` character width).  You may need to adjust this via
  :confval:`latex_elements` ``'fvset'`` key, in case of usage of some other
  OpenType fonts (refs: #5768)
* LaTeX: Greek letters in text are not escaped to math mode mark-up, and they
  will use the text font not the math font. The ``LGR`` font encoding must be
  added to the ``'fontenc'`` key of :confval:`latex_elements` for this to work
  (only if it is needed by the document, of course).
* LaTeX: setting the :confval:`language` to ``'en'`` triggered ``Sonny`` option
  of ``fncychap``, now it is ``Bjarne`` to match case of no language specified.
  (refs: #5772)
* #5770: doctest: Follow :confval:`highlight_language` on highlighting doctest
  block.  As a result, they are highlighted as python3 by default.
* The order of argument for ``HTMLTranslator``, ``HTML5Translator`` and
  ``ManualPageTranslator`` are changed
* LaTeX: hard-coded redefinitions of ``\l@section`` and ``\l@subsection``
  formerly done during loading of ``'manual'`` docclass get executed later, at
  time of ``\sphinxtableofcontents``.  This means that custom user definitions
  from LaTeX preamble now get overwritten.  Use ``\sphinxtableofcontentshook``
  to insert custom user definitions.  See :ref:`latex-macros`.
* quickstart: Simplify generated ``conf.py``
* #4148: quickstart: some questions are removed.  They are still able to specify
  via command line options
* websupport: unbundled from sphinx core. Please use sphinxcontrib-websupport
* C++, the visibility of base classes is now always rendered as present in the
  input. That is, ``private`` is now shown, where it was ellided before.
* LaTeX: graphics inclusion of oversized images rescales to not exceed
  the text width and height, even if width and/or height option were used.
  (refs: #5956)
* epub: ``epub_title`` defaults to the :confval:`project` option
* #4550: All tables and figures without ``align`` option are displayed to center
* #4587: html: Output HTML5 by default

2.0.0b2

* texinfo: image files are copied into ``name-figure`` directory

Deprecated
----------

2.0.0b1

* Support for evaluating Python 2 syntax is deprecated. This includes
  configuration files which should be converted to Python 3.
* The arguments of ``EpubBuilder.build_mimetype()``,
  ``EpubBuilder.build_container()``, ``EpubBuilder.bulid_content()``,
  ``EpubBuilder.build_toc()`` and ``EpubBuilder.build_epub()``
* The arguments of ``Epub3Builder.build_navigation_doc()``
* The config variables

  - :confval:`html_experimental_html5_writer`

* The ``encoding`` argument of ``autodoc.Documenter.get_doc()``,
  ``autodoc.DocstringSignatureMixin.get_doc()``,
  ``autodoc.DocstringSignatureMixin._find_signature()``, and
  ``autodoc.ClassDocumenter.get_doc()`` are deprecated.
* The ``importer`` argument of ``sphinx.ext.autodoc.importer._MockModule``
* The ``nodetype`` argument of ``sphinx.search.WordCollector.
  is_meta_keywords()``
* The ``suffix`` argument of ``env.doc2path()`` is deprecated.
* The string style ``base`` argument of ``env.doc2path()`` is deprecated.
* The fallback to allow omitting the ``filename`` argument from an overridden
  ``IndexBuilder.feed()`` method is deprecated.
* ``sphinx.addnodes.abbreviation``
* ``sphinx.application.Sphinx._setting_up_extension``
* ``sphinx.builders.epub3.Epub3Builder.validate_config_value()``
* ``sphinx.builders.html.SingleFileHTMLBuilder``
* ``sphinx.builders.htmlhelp.HTMLHelpBuilder.open_file()``
* ``sphinx.cmd.quickstart.term_decode()``
* ``sphinx.cmd.quickstart.TERM_ENCODING``
* ``sphinx.config.check_unicode()``
* ``sphinx.config.string_classes``
* ``sphinx.domains.cpp.DefinitionError.description``
* ``sphinx.domains.cpp.NoOldIdError.description``
* ``sphinx.domains.cpp.UnsupportedMultiCharacterCharLiteral.decoded``
* ``sphinx.ext.autodoc.importer._MockImporter``
* ``sphinx.ext.autosummary.Autosummary.warn()``
* ``sphinx.ext.autosummary.Autosummary.genopt``
* ``sphinx.ext.autosummary.Autosummary.warnings``
* ``sphinx.ext.autosummary.Autosummary.result``
* ``sphinx.ext.doctest.doctest_encode()``
* ``sphinx.io.SphinxBaseFileInput``
* ``sphinx.io.SphinxFileInput.supported``
* ``sphinx.io.SphinxRSTFileInput``
* ``sphinx.registry.SphinxComponentRegistry.add_source_input()``
* ``sphinx.roles.abbr_role()``
* ``sphinx.roles.emph_literal_role()``
* ``sphinx.roles.menusel_role()``
* ``sphinx.roles.index_role()``
* ``sphinx.roles.indexmarkup_role()``
* ``sphinx.testing.util.remove_unicode_literal()``
* ``sphinx.util.attrdict``
* ``sphinx.util.force_decode()``
* ``sphinx.util.get_matching_docs()``
* ``sphinx.util.inspect.Parameter``
* ``sphinx.util.jsonimpl``
* ``sphinx.util.osutil.EEXIST``
* ``sphinx.util.osutil.EINVAL``
* ``sphinx.util.osutil.ENOENT``
* ``sphinx.util.osutil.EPIPE``
* ``sphinx.util.osutil.walk()``
* ``sphinx.util.PeekableIterator``
* ``sphinx.util.pycompat.NoneType``
* ``sphinx.util.pycompat.TextIOWrapper``
* ``sphinx.util.pycompat.UnicodeMixin``
* ``sphinx.util.pycompat.htmlescape``
* ``sphinx.util.pycompat.indent``
* ``sphinx.util.pycompat.sys_encoding``
* ``sphinx.util.pycompat.terminal_safe()``
* ``sphinx.util.pycompat.u``
* ``sphinx.writers.latex.ExtBabel``
* ``sphinx.writers.latex.LaTeXTranslator._make_visit_admonition()``
* ``sphinx.writers.latex.LaTeXTranslator.babel_defmacro()``
* ``sphinx.writers.latex.LaTeXTranslator.collect_footnotes()``
* ``sphinx.writers.latex.LaTeXTranslator.generate_numfig_format()``
* ``sphinx.writers.texinfo.TexinfoTranslator._make_visit_admonition()``
* ``sphinx.writers.text.TextTranslator._make_depart_admonition()``
* template variables for LaTeX template

  - ``logo``
  - ``numfig_format``
  - ``pageautorefname``
  - ``translatablestrings``

For more details, see :ref:`deprecation APIs list <dev-deprecated-apis>`.

Features added
--------------

2.0.0b1

* #1618: The search results preview of generated HTML documentation is
  reader-friendlier: instead of showing the snippets as raw reStructuredText
  markup, Sphinx now renders the corresponding HTML.  This means the Sphinx
  extension `Sphinx: pretty search results`__ is no longer necessary.  Note that
  changes to the search function of your custom or 3rd-party HTML template might
  overwrite this improvement.

  __ https://github.com/sphinx-contrib/sphinx-pretty-searchresults

* #4182: autodoc: Support :confval:`suppress_warnings`
* #5533: autodoc: :confval:`autodoc_default_options` supports ``member-order``
* #5394: autodoc: Display readable names in type annotations for mocked objects
* #5459: autodoc: :confval:`autodoc_default_options` accepts ``True`` as a value
* #1148: autodoc: Add :rst:dir:`autodecorator` directive for decorators
* #5635: autosummary: Add :confval:`autosummary_mock_imports` to mock external
  libraries on importing targets
* #4018: htmlhelp: Add :confval:`htmlhelp_file_suffix` and
  :confval:`htmlhelp_link_suffix`
* #5559: text: Support complex tables (colspan and rowspan)
* LaTeX: support rendering (not in math, yet) of Greek and Cyrillic Unicode
  letters in non-Cyrillic document even with ``'pdflatex'`` as
  :confval:`latex_engine` (refs: #5645)
* #5660: The ``versionadded``, ``versionchanged`` and ``deprecated`` directives
  are now generated with their own specific CSS classes
  (``added``, ``changed`` and ``deprecated``, respectively) in addition to the
  generic ``versionmodified`` class.
* #5841: apidoc: Add --extensions option to sphinx-apidoc
* #4981: C++, added an alias directive for inserting lists of declarations,
  that references existing declarations (e.g., for making a synopsis).
* C++: add ``cpp:struct`` to complement ``cpp:class``.
* #1341 the HTML search considers words that contain a search term of length
  three or longer a match.
* #4611: epub: Show warning for duplicated ToC entries
* #1851: Allow to omit an argument for :rst:dir:`code-block` directive.  If
  omitted, it follows :rst:dir:`highlight` or :confval:`highlight_language`
* #4587: html: Add :confval:`html4_writer` to use old HTML4 writer
* #6016: HTML search: A placeholder for the search summary prevents search
  result links from changing their position when the search terminates.  This
  makes navigating search results easier.
* #5196: linkcheck also checks remote images exist
* #5924: githubpages: create CNAME file for custom domains when
  :confval:`html_baseurl` set
* #4261: autosectionlabel: restrict the labeled sections by new config value;
  :confval:`autosectionlabel_maxdepth`


Bugs fixed
----------

2.0.0b1

* #1682: LaTeX: writer should not translate Greek unicode, but use textgreek
  package
* #5247: LaTeX: PDF does not build with default font config for Russian
  language and ``'xelatex'`` or ``'lualatex'`` as :confval:`latex_engine`
  (refs: #5251)
* #5248: LaTeX: Greek letters in section titles disappear from PDF bookmarks
* #5249: LaTeX: Unicode Greek letters in math directive break PDF build
  (fix requires extra set-up, see :confval:`latex_elements` ``'textgreek'`` key
  and/or :confval:`latex_engine` setting)
* #5772: LaTeX: should the Bjarne style of fncychap be used for English also
  if passed as language option?
* #5179: LaTeX: (lualatex only) escaping of ``>`` by ``\textgreater{}`` is not
  enough as ``\textgreater{}\textgreater{}`` applies TeX-ligature
* LaTeX: project name is not escaped if :confval:`latex_documents` omitted
* LaTeX: authors are not shown if :confval:`latex_documents` omitted
* HTML: Invalid HTML5 file is generated for a glossary having multiple terms for
  one description (refs: #4611)
* QtHelp: OS dependent path separator is used in .qhp file
* HTML search: search always returns nothing when multiple search terms are
  used and one term is shorter than three characters

2.0.0b2

* #6096: html: Anchor links are not added to figures
* #3620: html: Defer searchindex.js rather than loading it via ajax
* #6113: html: Table cells and list items have large margins
* #5508: ``linenothreshold`` option for ``highlight`` directive was ignored
* texinfo: ``make install-info`` causes syntax error
* texinfo: ``make install-info`` fails on macOS
* #3079: texinfo: image files are not copied on ``make install-info``
* #5391: A cross reference in heading is rendered as literal
* #5946: C++, fix ``cpp:alias`` problems in LaTeX (and singlehtml)
* #6147: classes attribute of ``citation_reference`` node is lost
* AssertionError is raised when custom ``citation_reference`` node having
  classes attribute refers missing citation (refs: #6147)
* #2155: Support ``code`` directive
* C++, fix parsing of braced initializers.
* #6172: AttributeError is raised for old styled index nodes
* #4872: inheritance_diagram: correctly describe behavior of ``parts`` option in
  docs, allow negative values.
* #6178: i18n: Captions missing in translations for hidden TOCs

2.0.0 final

* #6196: py domain: unexpected prefix is generated

Testing
--------

2.0.0b1

* Stop to use ``SPHINX_TEST_TEMPDIR`` envvar

2.0.0b2

* Add a helper function: ``sphinx.testing.restructuredtext.parse()``

Release 1.8.5 (released Mar 10, 2019)
=====================================

Bugs fixed
----------

* LaTeX: Remove extraneous space after author names on PDF title page (refs:
  #6004)
* #6026: LaTeX: A cross reference to definition list does not work
* #6046: LaTeX: ``TypeError`` is raised when invalid latex_elements given
* #6067: LaTeX: images having a target are concatenated to next line
* #6067: LaTeX: images having a target are not aligned even if specified
* #6149: LaTeX: ``:index:`` role in titles causes ``Use of \@icentercr doesn't
  match its definition`` error on latexpdf build
* #6019: imgconverter: Including multipage PDF fails
* #6047: autodoc: ``autofunction`` emits a warning for method objects
* #6028: graphviz: Ensure the graphviz filenames are reproducible
* #6068: doctest: ``skipif`` option may remove the code block from documentation
* #6136: ``:name:`` option for ``math`` directive causes a crash
* #6139: intersphinx: ValueError on failure reporting
* #6135: changes: Fix UnboundLocalError when any module found
* #3859: manpage: code-block captions are not displayed correctly

Release 1.8.4 (released Feb 03, 2019)
=====================================

Bugs fixed
----------

* #3707: latex: no bold checkmark (✔) available.
* #5605: with the documentation language set to Chinese, English words could not
  be searched.
* #5889: LaTeX: user ``numfig_format`` is stripped of spaces and may cause
  build failure
* C++, fix hyperlinks for declarations involving east cv-qualifiers.
* #5755: C++, fix duplicate declaration error on function templates with
  constraints in the return type.
* C++, parse unary right fold expressions and binary fold expressions.
* pycode could not handle egg files on windows
* #5928: KeyError: 'DOCUTILSCONFIG' when running build
* #5936: LaTeX: PDF build broken by inclusion of image taller than page height
  in an admonition
* #5231: "make html" does not read and build "po" files in "locale" dir
* #5954: ``:scale:`` image option may break PDF build if image in an admonition
* #5966: mathjax has not been loaded on incremental build
* #5960: LaTeX: modified PDF layout since September 2018 TeXLive update of
  :file:`parskip.sty`
* #5948: LaTeX: duplicated labels are generated for sections
* #5958: versionadded directive causes crash with Python 3.5.0
* #5995: autodoc: autodoc_mock_imports conflict with metaclass on Python 3.7
* #5871: texinfo: a section title ``.`` is not allowed

Release 1.8.3 (released Dec 26, 2018)
=====================================

Features added
--------------

* LaTeX: it is possible to insert custom material to appear on back of title
  page, see discussion of ``'maketitle'`` key of :confval:`latex_elements`
  (``'manual'`` docclass only)

Bugs fixed
----------

* #5725: mathjax: Use CDN URL for "latest" version by default
* #5460: html search does not work with some 3rd party themes
* #5520: LaTeX, caption package incompatibility since Sphinx 1.6
* #5614: autodoc: incremental build is broken when builtin modules are imported
* #5627: qthelp: index.html missing in QtHelp
* #5659: linkcheck: crashes for a hyperlink containing multibyte character
* #5754: DOC: Fix some mistakes in :doc:`/latex`
* #5810: LaTeX: sphinxVerbatim requires explicit "hllines" set-up since 1.6.6
  (refs: #1238)
* #5636: C++, fix parsing of floating point literals.
* #5496 (again): C++, fix assertion in partial builds with duplicates.
* #5724: quickstart: sphinx-quickstart fails when $LC_ALL is empty
* #1956: Default conf.py is not PEP8-compliant
* #5849: LaTeX: document class ``\maketitle`` is overwritten with no
  possibility to use original meaning in place of Sphinx custom one
* #5834: apidoc: wrong help for ``--tocfile``
* #5800: todo: crashed if todo is defined in TextElement
* #5846: htmlhelp: convert hex escaping to decimal escaping in .hhc/.hhk files
* htmlhelp: broken .hhk file generated when title contains a double quote

Release 1.8.2 (released Nov 11, 2018)
=====================================

Incompatible changes
--------------------

* #5497: Do not include MathJax.js and jsmath.js unless it is really needed

Features added
--------------

* #5471: Show appropriate deprecation warnings

Bugs fixed
----------

* #5490: latex: enumerated list causes a crash with recommonmark
* #5492: sphinx-build fails to build docs w/ Python < 3.5.2
* #3704: latex: wrong ``\label`` positioning for figures with a legend
* #5496: C++, fix assertion when a symbol is declared more than twice.
* #5493: gettext: crashed with broken template
* #5495: csv-table directive with file option in included file is broken (refs:
  #4821)
* #5498: autodoc: unable to find type hints for a ``functools.partial``
* #5480: autodoc: unable to find type hints for unresolvable Forward references
* #5419: incompatible math_block node has been generated
* #5548: Fix ensuredir() in case of pre-existing file
* #5549: graphviz Correctly deal with non-existing static dir
* #3002: i18n: multiple footnote_references referring same footnote cause
  duplicated node_ids
* #5563: latex: footnote_references generated by extension causes a LaTeX
  builder crash
* #5561: make all-pdf fails with old xindy version
* #5557: quickstart: --no-batchfile isn't honored
* #3080: texinfo: multiline rubrics are broken
* #3080: texinfo: multiline citations are broken

Release 1.8.1 (released Sep 22, 2018)
=====================================

Incompatible changes
--------------------

* LaTeX ``\pagestyle`` commands have been moved to the LaTeX template. No
  changes in PDF, except possibly if ``\sphinxtableofcontents``, which
  contained them, had been customized in :file:`conf.py`. (refs: #5455)

Bugs fixed
----------

* #5418: Incorrect default path for sphinx-build -d/doctrees files
* #5421: autodoc emits deprecation warning for :confval:`autodoc_default_flags`
* #5422: lambda object causes PicklingError on storing environment
* #5417: Sphinx fails to build with syntax error in Python 2.7.5
* #4911: add latexpdf to make.bat for non make-mode
* #5436: Autodoc does not work with enum subclasses with properties/methods
* #5437: autodoc: crashed on modules importing eggs
* #5433: latex: ImportError: cannot import name 'DEFAULT_SETTINGS'
* #5431: autodoc: ``autofunction`` emits a warning for callable objects
* #5457: Fix TypeError in error message when override is prohibited
* #5453: PDF builds of 'howto' documents have no page numbers
* #5463: mathbase: math_role and MathDirective was disappeared in 1.8.0
* #5454: latex: Index has disappeared from PDF for Japanese documents
* #5432: py domain: ``:type:`` field can't process ``:term:`` references
* #5426: py domain: TypeError has been raised for class attribute

Release 1.8.0 (released Sep 13, 2018)
=====================================

Dependencies
------------

1.8.0b1

* LaTeX: :confval:`latex_use_xindy`, if ``True`` (default for
  ``xelatex/lualatex``), instructs ``make latexpdf`` to use :program:`xindy`
  for general index.  Make sure your LaTeX distribution includes it.
  (refs: #5134)
* LaTeX: ``latexmk`` is required for ``make latexpdf`` on Windows

Incompatible changes
--------------------

1.8.0b2

* #5282: html theme: refer ``pygments_style`` settings of HTML themes
  preferentially
* The URL of download files are changed
* #5127: quickstart: ``Makefile`` and ``make.bat`` are not overwritten if exists

1.8.0b1

* #5156: the :py:mod:`sphinx.ext.graphviz: extension runs `dot` in the
  directory of the document being built instead of in the root directory of
  the documentation.
* #4460: extensions which stores any data to environment should return the
  version of its env data structure as metadata.  In detail, please see
  :ref:`ext-metadata`.
* Sphinx expects source parser modules to have supported file formats as
  ``Parser.supported`` attribute
* The default value of :confval:`epub_author` and :confval:`epub_publisher` are
  changed from ``'unknown'`` to the value of :confval:`author`.  This is same as
  a ``conf.py`` file sphinx-build generates.
* The ``gettext_compact`` attribute is removed from ``document.settings``
  object.  Please use ``config.gettext_compact`` instead.
* The processing order on reading phase is changed.  smart_quotes, sphinx
  domains, :event:`doctree-read` event and versioning doctrees are invoked
  earlier than so far. For more details, please read a description of
  :py:meth:`.Sphinx.add_transform()`
* #4827: All ``substitution_definition`` nodes are removed from doctree on
  reading phase
* ``docutils.conf`` in ``$HOME`` or ``/etc`` directories are ignored.  Only
  ``docutils.conf`` from confdir is obeyed.
* #789: ``:samp:`` role supports to escape curly braces with backslash
* #4811: The files under :confval:`html_static_path` are excluded from source
  files.
* latex: Use ``\sphinxcite`` for citation references instead ``\hyperref``
* The config value ``viewcode_import`` is renamed to
  :confval:`viewcode_follow_imported_members` (refs: #4035)
* #1857: latex: :confval:`latex_show_pagerefs` does not add pagerefs for
  citations
* #4648: latex: Now "rubric" elements are rendered as unnumbered section title
* #4983: html: The anchor for productionlist tokens has been changed
* Modifying a template variable ``script_files`` in templates is allowed now.
  Please use ``app.add_js_file()`` instead.
* #5072: Save environment object also with only new documents
* #5035: qthelp builder allows dashes in :confval:`qthelp_namespace`
* LaTeX: with lualatex or xelatex use by default :program:`xindy` as
  UTF-8 able replacement of :program:`makeindex` (refs: #5134).  After
  upgrading Sphinx, please clean latex build repertory of existing project
  before new build.
* #5163: html: hlist items are now aligned to top
* ``highlightlang`` directive is processed on resolving phase
* #4000: LaTeX: template changed.  Following elements moved to it:

  - ``\begin{document}``
  - ``shorthandoff`` variable
  - ``maketitle`` variable
  - ``tableofcontents`` variable

Deprecated
----------

1.8.0b2

* ``sphinx.io.SphinxI18nReader.set_lineno_for_reporter()`` is deprecated
* ``sphinx.io.SphinxI18nReader.line`` is deprecated
* ``sphinx.util.i18n.find_catalog_source_file()`` has changed; the
  *gettext_compact* argument has been deprecated
* #5403: ``sphinx.util.images.guess_mimetype()`` has changed; the *content*
  argument has been deprecated

1.8.0b1

* :confval:`source_parsers` is deprecated
* :confval:`autodoc_default_flags` is deprecated
* quickstart: ``--epub`` option becomes default, so it is deprecated
* Drop function based directive support.  For now, Sphinx only supports class
  based directives (see :class:`~Directive`)
* ``sphinx.util.docutils.directive_helper()`` is deprecated
* ``sphinx.cmdline`` is deprecated
* ``sphinx.make_mode`` is deprecated
* ``sphinx.locale.l_()`` is deprecated
* #2157: helper function ``warn()`` for HTML themes is deprecated
* ``app.override_domain()`` is deprecated
* ``app.add_stylesheet()`` is deprecated
* ``app.add_javascript()`` is deprecated
* ``app.import_object()`` is deprecated
* ``app.add_source_parser()`` has changed;  the *suffix* argument has been
  deprecated
* ``sphinx.versioning.prepare()`` is deprecated
* ``Config.__init__()`` has changed;  the *dirname*, *filename* and *tags*
  argument has been deprecated
* ``Config.check_types()`` is deprecated
* ``Config.check_unicode()`` is deprecated
* ``sphinx.application.CONFIG_FILENAME`` is deprecated
* ``highlightlang`` directive is deprecated
* ``BuildEnvironment.load()`` is deprecated
* ``BuildEnvironment.loads()`` is deprecated
* ``BuildEnvironment.frompickle()`` is deprecated
* ``env.read_doc()`` is deprecated
* ``env.update()`` is deprecated
* ``env._read_serial()`` is deprecated
* ``env._read_parallel()`` is deprecated
* ``env.write_doctree()`` is deprecated
* ``env._nitpick_ignore`` is deprecated
* ``env.versionchanges`` is deprecated
* ``env.dump()`` is deprecated
* ``env.dumps()`` is deprecated
* ``env.topickle()`` is deprecated
* ``env.note_versionchange()`` is deprecated
* ``sphinx.writers.latex.Table.caption_footnotetexts`` is deprecated
* ``sphinx.writers.latex.Table.header_footnotetexts`` is deprecated
* ``sphinx.writers.latex.LaTeXTranslator.footnotestack`` is deprecated
* ``sphinx.writers.latex.LaTeXTranslator.in_container_literal_block`` is
  deprecated
* ``sphinx.writers.latex.LaTeXTranslator.next_section_ids`` is deprecated
* ``sphinx.writers.latex.LaTeXTranslator.next_hyperlink_ids`` is deprecated
* ``sphinx.writers.latex.LaTeXTranslator.restrict_footnote()`` is deprecated
* ``sphinx.writers.latex.LaTeXTranslator.unrestrict_footnote()`` is deprecated
* ``sphinx.writers.latex.LaTeXTranslator.push_hyperlink_ids()`` is deprecated
* ``sphinx.writers.latex.LaTeXTranslator.pop_hyperlink_ids()`` is deprecated
* ``sphinx.writers.latex.LaTeXTranslator.check_latex_elements()`` is deprecated
* ``sphinx.writers.latex.LaTeXTranslator.bibitems`` is deprecated
* ``sphinx.writers.latex.LaTeXTranslator.hlsettingstack`` is deprecated
* ``sphinx.writers.latex.ExtBabel.get_shorthandoff()`` is deprecated
* ``sphinx.writers.html.HTMLTranslator.highlightlang`` is deprecated
* ``sphinx.writers.html.HTMLTranslator.highlightlang_base`` is deprecated
* ``sphinx.writers.html.HTMLTranslator.highlightlangopts`` is deprecated
* ``sphinx.writers.html.HTMLTranslator.highlightlinenothreshold`` is deprecated
* ``sphinx.writers.html5.HTMLTranslator.highlightlang`` is deprecated
* ``sphinx.writers.html5.HTMLTranslator.highlightlang_base`` is deprecated
* ``sphinx.writers.html5.HTMLTranslator.highlightlangopts`` is deprecated
* ``sphinx.writers.html5.HTMLTranslator.highlightlinenothreshold`` is deprecated
* ``sphinx.ext.mathbase`` extension is deprecated
* ``sphinx.ext.mathbase.math`` node is deprecated
* ``sphinx.ext.mathbase.displaymath`` node is deprecated
* ``sphinx.ext.mathbase.eqref`` node is deprecated
* ``sphinx.ext.mathbase.is_in_section_title()`` is deprecated
* ``sphinx.ext.mathbase.MathDomain`` is deprecated
* ``sphinx.ext.mathbase.MathDirective`` is deprecated
* ``sphinx.ext.mathbase.math_role`` is deprecated
* ``sphinx.ext.mathbase.setup_math()`` is deprecated
* ``sphinx.directives.other.VersionChanges`` is deprecated
* ``sphinx.highlighting.PygmentsBridge.unhighlight()`` is deprecated
* ``sphinx.ext.mathbase.get_node_equation_number()`` is deprecated
* ``sphinx.ext.mathbase.wrap_displaymath()`` is deprecated
* The ``trim_doctest_flags`` argument of ``sphinx.highlighting.PygmentsBridge``
  is deprecated

For more details, see `deprecation APIs list
<http://www.sphinx-doc.org/en/master/extdev/index.html#deprecated-apis>`_

Features added
--------------

1.8.0b2

* #5388: Ensure frozen object descriptions are reproducible
* #5362: apidoc: Add ``--tocfile`` option to change the filename of ToC

1.8.0b1

* Add :event:`config-inited` event
* Add ``sphinx.config.Any`` to represent the config value accepts any type of
  value
* :confval:`source_suffix` allows a mapping fileext to file types
* Add :confval:`author` as a configuration value
* #2852: imgconverter: Support to convert GIF to PNG
* ``sphinx-build`` command supports i18n console output
* Add ``app.add_message_catalog()`` and ``sphinx.locale.get_translations()`` to
  support translation for 3rd party extensions
* helper function ``warning()`` for HTML themes is added
* Add ``Domain.enumerable_nodes`` to manage own enumerable nodes for domains
  (experimental)
* Add a new keyword argument ``override`` to Application APIs
* LaTeX: new key ``'fvset'`` for :confval:`latex_elements`. For
  XeLaTeX/LuaLaTeX its default sets ``fanvyvrb`` to use normal, not small,
  fontsize in code-blocks (refs: #4793)
* Add :confval:`html_css_files` and :confval:`epub_css_files` for adding CSS
  files from configuration
* Add :confval:`html_js_files` for adding JS files from configuration
* #4834: Ensure set object descriptions are reproducible.
* #4828: Allow to override :confval:`numfig_format` partially.  Full definition
  is not needed.
* Improve warning messages during including (refs: #4818)
* LaTeX: separate customizability of :rst:role:`guilabel` and
  :rst:role:`menuselection` (refs: #4830)
* Add ``Config.read()`` classmethod to create a new config object from
  configuration file
* #4866: Wrap graphviz diagrams in ``<div>`` tag
* viewcode: Add :event:`viewcode-find-source` and
  :event:`viewcode-follow-imported` to load source code without loading
* #4785: napoleon: Add strings to translation file for localisation
* #4927: Display a warning when invalid values are passed to linenothreshold
  option of highlight directive
* C++:

  - Add a ``cpp:texpr`` role as a sibling to ``cpp:expr``.
  - Add support for unions.
  - #3593, #2683: add support for anonymous entities using names staring with
    ``@``.
  - #5147: add support for (most) character literals.
  - Cross-referencing entities inside primary templates is supported,
    and now properly documented.
  - #1552: add new cross-referencing format for ``cpp:any`` and ``cpp:func``
    roles, for referencing specific function overloads.

* #3606: MathJax should be loaded with async attribute
* html: Output ``canonical_url`` metadata if :confval:`html_baseurl` set (refs:
  #4193)
* #5029: autosummary: expose ``inherited_members`` to template
* #3784: mathjax: Add :confval:`mathjax_options` to give options to script tag
  for mathjax
* #726, #969: mathjax: Add :confval:`mathjax_config` to give in-line
  configurations for mathjax
* #4362: latex: Don't overwrite .tex file if document not changed
* #1431: latex: Add alphanumeric enumerated list support
* Add :confval:`latex_use_xindy` for UTF-8 savvy indexing, defaults to ``True``
  if :confval:`latex_engine` is ``'xelatex'`` or ``'lualatex'``. (refs: #5134,
  #5192, #5212)
* #4976: ``SphinxLoggerAdapter.info()`` now supports ``location`` parameter
* #5122: setuptools: support nitpicky option
* #2820: autoclass directive supports nested class
* Add ``app.add_html_math_renderer()`` to register a math renderer for HTML
* Apply :confval:`trim_doctest_flags` to all builders (cf. text, manpages)
* #5140: linkcheck: Add better Accept header to HTTP client
* #4614: sphinx-build: Add ``--keep-going`` option to show all warnings
* Add :rst:role:`math:numref` role to refer equations (Same as :rst:role:`eq`)
* quickstart: epub builder is enabled by default
* #5246: Add :confval:`singlehtml_sidebars` to configure sidebars for singlehtml
  builder
* #5273: doctest: Skip doctest conditionally
* #5306: autodoc: emit a warning for invalid typehints
* #4075, #5215: autodoc: Add :confval:`autodoc_default_options` which accepts
  option values as dict

Bugs fixed
----------

1.8.0b2

* html: search box overrides to other elements if scrolled
* i18n: warnings for translation catalogs have wrong line numbers (refs: #5321)
* #5325: latex: cross references has been broken by multiply labeled objects
* C++, fixes for symbol addition and lookup. Lookup should no longer break
  in partial builds. See also #5337.
* #5348: download reference to remote file is not displayed
* #5282: html theme: ``pygments_style`` of theme was overridden by ``conf.py``
  by default
* #4379: toctree shows confusing warning when document is excluded
* #2401: autodoc: ``:members:`` causes ``:special-members:`` not to be shown
* autodoc: ImportError is replaced by AttributeError for deeper module
* #2720, #4034: Incorrect links with ``:download:``, duplicate names, and
  parallel builds
* #5290: autodoc: failed to analyze source code in egg package
* #5399: Sphinx crashes if unknown po file exists

1.8.0b1

* i18n: message catalogs were reset on each initialization
* #4850: latex: footnote inside footnote was not rendered
* #4945: i18n: fix lang_COUNTRY not fallback correctly for IndexBuilder. Thanks
  to Shengjing Zhu.
* #4983: productionlist directive generates invalid IDs for the tokens
* #5132: lualatex: PDF build fails if indexed word starts with Unicode character
* #5133: latex: index headings "Symbols" and "Numbers" not internationalized
* #5114: sphinx-build: Handle errors on scanning documents
* epub: spine has been broken when "self" is listed on toctree (refs: #4611)
* #344: autosummary does not understand docstring of module level attributes
* #5191: C++, prevent nested declarations in functions to avoid lookup problems.
* #5126: C++, add missing isPack method for certain template parameter types.
* #5187: C++, parse attributes on declarators as well.
* C++, parse delete expressions and basic new expressions as well.
* #5002: graphviz: SVGs do not adapt to the column width

Features removed
----------------

1.8.0b1

* ``sphinx.ext.pngmath`` extension

Documentation
-------------

1.8.0b1

* #5083: Fix wrong make.bat option for internationalization.
* #5115: napoleon: add admonitions added by #4613 to the docs.

Release 1.7.9 (released Sep 05, 2018)
=====================================

Features added
--------------

* #5359: Make generated texinfo files reproducible by sorting the anchors

Bugs fixed
----------

* #5361: crashed on incremental build if document uses include directive

Release 1.7.8 (released Aug 29, 2018)
=====================================

Incompatible changes
--------------------

* The type of ``env.included`` has been changed to dict of set

Bugs fixed
----------

* #5320: intersphinx: crashed if invalid url given
* #5326: manpage: crashed when invalid docname is specified as ``man_pages``
* #5322: autodoc: ``Any`` typehint causes formatting error
* #5327: "document isn't included in any toctree" warning on rebuild with
  generated files
* #5335: quickstart: escape sequence has been displayed with MacPorts' python

Release 1.7.7 (released Aug 19, 2018)
=====================================

Bugs fixed
----------

* #5198: document not in toctree warning when including files only for parallel
  builds
* LaTeX: reduce "Token not allowed in a PDF string" hyperref warnings in latex
  console output (refs: #5236)
* LaTeX: suppress "remreset Warning: The remreset package is obsolete" in latex
  console output with recent LaTeX (refs: #5237)
* #5234: PDF output: usage of PAPER environment variable is broken since Sphinx
  1.5
* LaTeX: fix the :confval:`latex_engine` documentation regarding Latin Modern
  font with XeLaTeX/LuaLateX (refs: #5251)
* #5280: autodoc: Fix wrong type annotations for complex typing
* autodoc: Optional types are wrongly rendered
* #5291: autodoc crashed by ForwardRef types
* #5211: autodoc: No docs generated for functools.partial functions
* #5306: autodoc: ``getargspec()`` raises NameError for invalid typehints
* #5298: imgmath: math_number_all causes equations to have two numbers in html
* #5294: sphinx-quickstart blank prompts in PowerShell

Release 1.7.6 (released Jul 17, 2018)
=====================================

Bugs fixed
----------

* #5037: LaTeX ``\sphinxupquote{}`` breaks in Russian
* sphinx.testing uses deprecated pytest API; ``Node.get_marker(name)``
* #5016: crashed when recommonmark.AutoStrictify is enabled
* #5022: latex: crashed with docutils package provided by Debian/Ubuntu
* #5009: latex: a label for table is vanished if table does not have a caption
* #5048: crashed with numbered toctree
* #2410: C, render empty argument lists for macros.
* C++, fix lookup of full template specializations with no template arguments.
* #4667: C++, fix assertion on missing references in global scope when using
  intersphinx. Thanks to Alan M. Carroll.
* #5019: autodoc: crashed by Form Feed Character
* #5032: autodoc: loses the first staticmethod parameter for old styled classes
* #5036: quickstart: Typing Ctrl-U clears the whole of line
* #5066: html: "relations" sidebar is not shown by default
* #5091: latex: curly braces in index entries are not handled correctly
* #5070: epub: Wrong internal href fragment links
* #5104: apidoc: Interface of ``sphinx.apidoc:main()`` has changed
* #4272: PDF builds of French projects have issues with XeTeX
* #5076: napoleon raises RuntimeError with python 3.7
* #5125: sphinx-build: Interface of ``sphinx:main()`` has changed
* sphinx-build: ``sphinx.cmd.build.main()`` refers ``sys.argv`` instead of given
  argument
* #5146: autosummary: warning is emitted when the first line of docstring ends
  with literal notation
* autosummary: warnings of autosummary indicates wrong location (refs: #5146)
* #5143: autodoc: crashed on inspecting dict like object which does not support
  sorting
* #5139: autodoc: Enum argument missing if it shares value with another
* #4946: py domain: rtype field could not handle "None" as a type
* #5176: LaTeX: indexing of terms containing ``@``, ``!``, or ``"`` fails
* #5161: html: crashes if copying static files are failed
* #5167: autodoc: Fix formatting type annotations for tuples with more than two
  arguments
* #3329: i18n: crashed by auto-symbol footnote references
* #5158: autosummary: module summary has been broken when it starts with heading

Release 1.7.5 (released May 29, 2018)
=====================================

Bugs fixed
----------

* #4924: html search: Upper characters problem in any other languages
* #4932: apidoc: some subpackage is ignored if sibling subpackage contains a
  module starting with underscore
* #4863, #4938, #4939: i18n doesn't handle correctly node.title as used for
  contents, topic, admonition, table and section.
* #4913: i18n: literal blocks in bullet list are not translated
* #4962: C++, raised TypeError on duplicate declaration.
* #4825: C++, properly parse expr roles and give better error messages when
  (escaped) line breaks are present.
* C++, properly use ``desc_addname`` nodes for prefixes of names.
* C++, parse pack expansions in function calls.
* #4915, #4916: links on search page are broken when using dirhtml builder
* #4969: autodoc: constructor method should not have return annotation
* latex: deeply nested enumerated list which is beginning with non-1 causes
  LaTeX engine crashed
* #4978: latex: shorthandoff is not set up for Brazil locale
* #4928: i18n: Ignore dot-directories like .git/ in LC_MESSAGES/
* #4946: py domain: type field could not handle "None" as a type
* #4979: latex: Incorrect escaping of curly braces in index entries
* #4956: autodoc: Failed to extract document from a subclass of the class on
  mocked module
* #4973: latex: glossary directive adds whitespace to each item
* #4980: latex: Explicit labels on code blocks are duplicated
* #4919: node.asdom() crashes if toctree has :numbered: option
* #4914: autodoc: Parsing error when using dataclasses without default values
* #4931: autodoc: crashed when handler for autodoc-skip-member raises an error
* #4931: autodoc: crashed when subclass of mocked class are processed by
  napoleon module
* #5007: sphinx-build crashes when error log contains a "%" character

Release 1.7.4 (released Apr 25, 2018)
=====================================

Bugs fixed
----------

* #4885, #4887: domains: Crashed with duplicated objects
* #4889: latex: sphinx.writers.latex causes recursive import

Release 1.7.3 (released Apr 23, 2018)
=====================================

Bugs fixed
----------

* #4769: autodoc loses the first staticmethod parameter
* #4790: autosummary: too wide two column tables in PDF builds
* #4795: Latex customization via ``_templates/longtable.tex_t`` is broken
* #4789: imgconverter: confused by convert.exe of Windows
* #4783: On windows, Sphinx crashed when drives of srcdir and outdir are
  different
* #4812: autodoc ignores type annotated variables
* #4817: wrong URLs on warning messages
* #4784: latex: :confval:`latex_show_urls` assigns incorrect footnote numbers if
  hyperlinks exists inside substitutions
* #4837: latex with class memoir Error: Font command ``\sf`` is not supported
* #4803: latex: too slow in proportion to number of auto numbered footnotes
* #4838: htmlhelp: The entries in .hhp file is not ordered
* toctree directive tries to glob for URL having query_string
* #4871: html search: Upper characters problem in German
* #4717: latex: Compilation for German docs failed with LuaLaTeX and XeLaTeX
* #4459: duplicated labels detector does not work well in parallel build
* #4878: Crashed with extension which returns invalid metadata

Release 1.7.2 (released Mar 21, 2018)
=====================================

Incompatible changes
--------------------
* #4520: apidoc: folders with an empty __init__.py are no longer excluded from
  TOC

Bugs fixed
----------

* #4669: sphinx.build_main and sphinx.make_main throw NameError
* #4685: autosummary emits meaningless warnings
* autodoc: crashed when invalid options given
* pydomain: always strip parenthesis if empty (refs: #1042)
* #4689: autosummary: unexpectedly strips docstrings containing "i.e."
* #4701: viewcode: Misplaced ``<div>`` in viewcode html output
* #4444: Don't require numfig to use :numref: on sections
* #4727: Option clash for package textcomp
* #4725: Sphinx does not work with python 3.5.0 and 3.5.1
* #4716: Generation PDF file with TexLive on Windows, file not found error
* #4574: vertical space before equation in latex
* #4720: message when an image is mismatched for builder is not clear
* #4655, #4684: Incomplete localization strings in Polish and Chinese
* #2286: Sphinx crashes when error is happens in rendering HTML pages
* #4688: Error to download remote images having long URL
* #4754: sphinx/pycode/__init__.py raises AttributeError
* #1435: qthelp builder should htmlescape keywords
* epub: Fix docTitle elements of toc.ncx is not escaped
* #4520: apidoc: Subpackage not in toc (introduced in 1.6.6) now fixed
* #4767: html: search highlighting breaks mathjax equations

Release 1.7.1 (released Feb 23, 2018)
=====================================

Deprecated
----------

* #4623: ``sphinx.build_main()`` is deprecated.
* autosummary: The interface of ``sphinx.ext.autosummary.get_documenter()`` has
  been changed (Since 1.7.0)
* #4664: ``sphinx.ext.intersphinx.debug()`` is deprecated.

For more details, see `deprecation APIs list
<http://www.sphinx-doc.org/en/master/extdev/index.html#deprecated-apis>`_

Bugs fixed
----------

* #4608: epub: Invalid meta tag is generated
* #4260: autodoc: keyword only argument separator is not disappeared if it is
  appeared at top of the argument list
* #4622: epub: :confval:`epub_scheme` does not effect to content.opf
* #4627: graphviz: Fit graphviz images to page
* #4617: quickstart: PROJECT_DIR argument is required
* #4623: sphinx.build_main no longer exists in 1.7.0
* #4615: The argument of ``sphinx.build`` has been changed in 1.7.0
* autosummary: The interface of ``sphinx.ext.autosummary.get_documenter()`` has
  been changed
* #4630: Have order on msgids in sphinx.pot deterministic
* #4563: autosummary: Incorrect end of line punctuation detection
* #4577: Enumerated sublists with explicit start with wrong number
* #4641: A external link in TOC cannot contain "?" with ``:glob:`` option
* C++, add missing parsing of explicit casts and typeid in expression parsing.
* C++, add missing parsing of ``this`` in expression parsing.
* #4655: Fix incomplete localization strings in Polish
* #4653: Fix error reporting for parameterless ImportErrors
* #4664: Reading objects.inv fails again
* #4662: ``any`` refs with ``term`` targets crash when an ambiguity is
  encountered

Release 1.7.0 (released Feb 12, 2018)
=====================================

Dependencies
------------

1.7.0b1

* Add ``packaging`` package

Incompatible changes
--------------------

1.7.0b1

* #3668: The arguments has changed of main functions for each command
* #3893: Unknown html_theme_options throw warnings instead of errors
* #3927: Python parameter/variable types should match classes, not all objects
* #3962: sphinx-apidoc now recognizes given directory as an implicit namespace
  package when ``--implicit-namespaces`` option given, not subdirectories of
  given directory.
* #3929: apidoc: Move sphinx.apidoc to sphinx.ext.apidoc
* #4226: apidoc: Generate new style makefile (make-mode)
* #4274: sphinx-build returns 2 as an exit code on argument error
* #4389: output directory will be created after loading extensions
* autodoc does not generate warnings messages to the generated document even if
  :confval:`keep_warnings` is True.  They are only emitted to stderr.
* shebang line is removed from generated conf.py
* #2557: autodoc: :confval:`autodoc_mock_imports` only mocks specified modules
  with their descendants.  It does not mock their ancestors.  If you want to
  mock them, please specify the name of ancestors explicitly.
* #3620: html theme: move DOCUMENTATION_OPTIONS to independent JavaScript file
  (refs: #4295)
* #4246: Limit width of text body for all themes. Configurable via theme
  options ``body_min_width`` and ``body_max_width``.
* #4771: apidoc: The ``exclude_patterns`` arguments are ignored if they are
  placed just after command line options

1.7.0b2

* #4467: html theme: Rename ``csss`` block to ``css``

Deprecated
----------

1.7.0b1

* using a string value for :confval:`html_sidebars` is deprecated and only list
  values will be accepted at 2.0.
* ``format_annotation()`` and ``formatargspec()`` is deprecated.  Please use
  ``sphinx.util.inspect.Signature`` instead.
* ``sphinx.ext.autodoc.AutodocReporter`` is replaced by ``sphinx.util.docutils.
  switch_source_input()`` and now deprecated.  It will be removed in Sphinx-2.0.
* ``sphinx.ext.autodoc.add_documenter()`` and ``AutoDirective._register`` is now
  deprecated.  Please use ``app.add_autodocumenter()`` instead.
* ``AutoDirective._special_attrgetters`` is now deprecated.  Please use
  ``app.add_autodoc_attrgetter()`` instead.

Features added
--------------

1.7.0b1

* C++, handle ``decltype(auto)``.
* #2406: C++, add proper parsing of expressions, including linking of
  identifiers.
* C++, add a ``cpp:expr`` role for inserting inline C++ expressions or types.
* C++, support explicit member instantiations with shorthand ``template`` prefix
* C++, make function parameters linkable, like template params.
* #3638: Allow to change a label of reference to equation using
  ``math_eqref_format``
* Now :confval:`suppress_warnings` accepts following configurations:

  - ``ref.python`` (ref: #3866)

* #3872: Add latex key to configure literal blocks caption position in PDF
  output (refs #3792, #1723)
* In case of missing docstring try to retrieve doc from base classes (ref:
  #3140)
* #4023: Clarify error message when any role has more than one target.
* #3973: epub: allow to override build date
* #3972: epub: Sort manifest entries by filename
* #4052: viewcode: Sort before highlighting module code
* #1448: qthelp: Add new config value; :confval:`qthelp_namespace`
* #4140: html themes: Make body tag inheritable
* #4168: improve zh search with jieba
* HTML themes can set up default sidebars through ``theme.conf``
* #3160: html: Use ``<kdb>`` to represent ``:kbd:`` role
* #4212: autosummary: catch all exceptions when importing modules
* #4166: Add :confval:`math_numfig` for equation numbering by section (refs:
  #3991, #4080). Thanks to Oliver Jahn.
* #4311: Let LaTeX obey :confval:`numfig_secnum_depth` for figures, tables, and
  code-blocks
* #947: autodoc now supports ignore-module-all to ignore a module's ``__all__``
* #4332: Let LaTeX obey :confval:`math_numfig` for equation numbering
* #4093: sphinx-build creates empty directories for unknown targets/builders
* Add ``top-classes`` option for the ``sphinx.ext.inheritance_diagram``
  extension to limit the scope of inheritance graphs.
* #4183: doctest: ``:pyversion:`` option also follows PEP-440 specification
* #4235: html: Add :confval:`manpages_url` to make manpage roles to hyperlinks
* #3570: autodoc: Do not display 'typing.' module for type hints
* #4354: sphinx-build now emits finish message.  Builders can modify it through
  ``Builder.epilog`` attribute
* #4245: html themes: Add ``language`` to javascript vars list
* #4079: html: Add ``notranslate`` class to each code-blocks, literals and maths
  to let Google Translate know they are not translatable
* #4137: doctest: doctest block is always highlighted as python console (pycon)
* #4137: doctest: testcode block is always highlighted as python
* #3998: text: Assign section numbers by default.  You can control it using
  :confval:`text_add_secnumbers` and :confval:`text_secnumber_suffix`

1.7.0b2

* #4271: sphinx-build supports an option called ``-j auto`` to adjust numbers of
  processes automatically.
* Napoleon: added option to specify custom section tags.


Features removed
----------------

1.7.0b1

* Configuration variables

  - html_use_smartypants
  - latex_keep_old_macro_names
  - latex_elements['footer']

* utility methods of ``sphinx.application.Sphinx`` class

  - buildername (property)
  - _display_chunk()
  - old_status_iterator()
  - status_iterator()
  - _directive_helper()

* utility methods of ``sphinx.environment.BuildEnvironment`` class

  - currmodule (property)
  - currclass (property)

* epub2 builder
* prefix and colorfunc parameter for warn()
* ``sphinx.util.compat`` module
* ``sphinx.util.nodes.process_only_nodes()``
* LaTeX environment ``notice``, use ``sphinxadmonition`` instead
* LaTeX ``\sphinxstylethead``, use ``\sphinxstyletheadfamily``
* C++, support of function concepts. Thanks to mickk-on-cpp.
* Not used and previously not documented LaTeX macros ``\shortversion``
  and ``\setshortversion``


Bugs fixed
----------

1.7.0b1

* #3882: Update the order of files for HTMLHelp and QTHelp
* #3962: sphinx-apidoc does not recognize implicit namespace packages correctly
* #4094: C++, allow empty template argument lists.
* C++, also hyperlink types in the name of declarations with qualified names.
* C++, do not add index entries for declarations inside concepts.
* C++, support the template disambiguator for dependent names.
* #4314: For PDF 'howto' documents, numbering of code-blocks differs from the
  one of figures and tables
* #4330: PDF 'howto' documents have an incoherent default LaTeX tocdepth counter
  setting
* #4198: autosummary emits multiple 'autodoc-process-docstring' event. Thanks
  to Joel Nothman.
* #4081: Warnings and errors colored the same when building
* latex: Do not display 'Release' label if :confval:`release` is not set

1.7.0b2

* #4415: autodoc classifies inherited classmethods as regular methods
* #4415: autodoc classifies inherited staticmethods as regular methods
* #4472: DOCUMENTATION_OPTIONS is not defined
* #4491: autodoc: prefer _MockImporter over other importers in sys.meta_path
* #4490: autodoc: type annotation is broken with python 3.7.0a4+
* utils package is no longer installed
* #3952: apidoc: module header is too escaped
* #4275: Formats accepted by sphinx.util.i18n.format_date are limited
* #4493: recommonmark raises AttributeError if AutoStructify enabled
* #4209: intersphinx: In link title, "v" should be optional if target has no
  version
* #4230: slowdown in writing pages with sphinx 1.6
* #4522: epub: document is not rebuilt even if config changed

1.7.0b3

* #4019: inheritance_diagram AttributeError stopping make process
* #4531: autosummary: methods are not treated as attributes
* #4538: autodoc: ``sphinx.ext.autodoc.Options`` has been moved
* #4539: autodoc emits warnings for partialmethods
* #4223: doctest: failing tests reported in wrong file, at wrong line
* i18n: message catalogs are not compiled if specific filenames are given for
  ``sphinx-build`` as arguments (refs: #4560)
* #4027: sphinx.ext.autosectionlabel now expects labels to be the same as they
  are in the raw source; no smart quotes, nothig fancy.
* #4581: apidoc: Excluded modules still included


Testing
--------

1.7.0b1

* Add support for docutils 0.14
* Add tests for the ``sphinx.ext.inheritance_diagram`` extension.

Release 1.6.7 (released Feb 04, 2018)
=====================================

Bugs fixed
----------

* #1922: html search: Upper characters problem in French
* #4412: Updated jQuery version from 3.1.0 to 3.2.1
* #4438: math: math with labels with whitespace cause html error
* #2437: make full reference for classes, aliased with "alias of"
* #4434: pure numbers as link targets produce warning
* #4477: Build fails after building specific files
* #4449: apidoc: include "empty" packages that contain modules
* #3917: citation labels are transformed to ellipsis
* #4501: graphviz: epub3 validation error caused if graph is not clickable
* #4514: graphviz: workaround for wrong map ID which graphviz generates
* #4525: autosectionlabel does not support parallel build
* #3953: Do not raise warning when there is a working intersphinx inventory
* #4487: math: ValueError is raised on parallel build. Thanks to jschueller.
* #2372: autosummary: invalid signatures are shown for type annotated functions
* #3942: html: table is not aligned to center even if ``:align: center``

Release 1.6.6 (released Jan 08, 2018)
=====================================

Features added
--------------

* #4181: autodoc: Sort dictionary keys when possible
* ``VerbatimHighlightColor`` is a new
  :ref:`LaTeX 'sphinxsetup' <latexsphinxsetup>` key (refs: #4285)
* Easier customizability of LaTeX macros involved in rendering of code-blocks
* Show traceback if conf.py raises an exception (refs: #4369)
* Add :confval:`smartquotes` to disable smart quotes through ``conf.py``
  (refs: #3967)
* Add :confval:`smartquotes_action` and :confval:`smartquotes_excludes`
  (refs: #4142, #4357)

Bugs fixed
----------

* #4334: sphinx-apidoc: Don't generate references to non-existing files in TOC
* #4206: latex: reST label between paragraphs loses paragraph break
* #4231: html: Apply fixFirefoxAnchorBug only under Firefox
* #4221: napoleon depends on autodoc, but users need to load it manually
* #2298: automodule fails to document a class attribute
* #4099: C++: properly link class reference to class from inside constructor
* #4267: PDF build broken by Unicode U+2116 NUMERO SIGN character
* #4249: PDF output: Pygments error highlighting increases line spacing in
  code blocks
* #1238: Support ``:emphasize-lines:`` in PDF output
* #4279: Sphinx crashes with pickling error when run with multiple processes and
  remote image
* #1421: Respect the quiet flag in sphinx-quickstart
* #4281: Race conditions when creating output directory
* #4315: For PDF 'howto' documents, ``latex_toplevel_sectioning='part'``
  generates ``\chapter`` commands
* #4214: Two todolist directives break sphinx-1.6.5
* Fix links to external option docs with intersphinx (refs: #3769)
* #4091: Private members not documented without :undoc-members:

Release 1.6.5 (released Oct 23, 2017)
=====================================

Features added
--------------

* #4107: Make searchtools.js compatible with pre-Sphinx1.5 templates
* #4112: Don't override the smart_quotes setting if it was already set
* #4125: Display reference texts of original and translated passages on
  i18n warning message
* #4147: Include the exception when logging PO/MO file read/write

Bugs fixed
----------

* #4085: Failed PDF build from image in parsed-literal using ``:align:`` option
* #4100: Remove debug print from autodoc extension
* #3987: Changing theme from alabaster causes HTML build to fail
* #4096: C++, don't crash when using the wrong role type. Thanks to mitya57.
* #4070, #4111: crashes when the warning message contains format strings (again)
* #4108: Search word highlighting breaks SVG images
* #3692: Unable to build HTML if writing .buildinfo failed
* #4152: HTML writer crashes if a field list is placed on top of the document
* #4063: Sphinx crashes when labeling directive ``.. todolist::``
* #4134: [doc] :file:`docutils.conf` is not documented explicitly
* #4169: Chinese language doesn't trigger Chinese search automatically
* #1020: ext.todo todolist not linking to the page in pdflatex
* #3965: New quickstart generates wrong SPHINXBUILD in Makefile
* #3739: ``:module:`` option is ignored at content of pyobjects
* #4149: Documentation: Help choosing :confval:`latex_engine`
* #4090: [doc] :confval:`latex_additional_files` with extra LaTeX macros should
  not use ``.tex`` extension
* Failed to convert reST parser error to warning (refs: #4132)

Release 1.6.4 (released Sep 26, 2017)
=====================================

Features added
--------------

* #3926: Add ``autodoc_warningiserror`` to suppress the behavior of ``-W``
  option during importing target modules on autodoc

Bugs fixed
----------

* #3924: docname lost after dynamically parsing RST in extension
* #3946: Typo in sphinx.sty (this was a bug with no effect in default context)
* :pep: and :rfc: does not supports ``default-role`` directive (refs: #3960)
* #3960: default_role = 'guilabel' not functioning
* Missing ``texinputs_win/Makefile`` to be used in latexpdf builder on windows.
* #4026: nature: Fix macOS Safari scrollbar color
* #3877: Fix for C++ multiline signatures.
* #4006: Fix crash on parallel build
* #3969: private instance attributes causes AttributeError
* #4041: C++, remove extra name linking in function pointers.
* #4038: C, add missing documentation of ``member`` role.
* #4044: An empty multicolumn cell causes extra row height in PDF output
* #4049: Fix typo in output of sphinx-build -h
* #4062: hashlib.sha1() must take bytes, not unicode on Python 3
* Avoid indent after index entries in latex (refs: #4066)
* #4070: crashes when the warning message contains format strings
* #4067: Return non-zero exit status when make subprocess fails
* #4055: graphviz: the :align: option does not work for SVG output
* #4055: graphviz: the :align: center option does not work for latex output
* #4051: ``warn()`` function for HTML theme outputs 'None' string

Release 1.6.3 (released Jul 02, 2017)
=====================================

Features added
--------------

* latex: hint that code-block continues on next page (refs: #3764, #3792)

Bugs fixed
----------

* #3821: Failed to import sphinx.util.compat with docutils-0.14rc1
* #3829: sphinx-quickstart template is incomplete regarding use of alabaster
* #3772: 'str object' has no attribute 'filename'
* Emit wrong warnings if citation label includes hyphens (refs: #3565)
* #3858: Some warnings are not colored when using --color option
* #3775: Remove unwanted whitespace in default template
* #3835: sphinx.ext.imgmath fails to convert SVG images if project directory
  name contains spaces
* #3850: Fix color handling in make mode's help command
* #3865: use of self.env.warn in sphinx extension fails
* #3824: production lists apply smart quotes transform since Sphinx 1.6.1
* latex: fix ``\sphinxbfcode`` swallows initial space of argument
* #3878: Quotes in auto-documented class attributes should be straight quotes
  in PDF output
* #3881: LaTeX figure floated to next page sometimes leaves extra vertical
  whitespace
* #3885: duplicated footnotes raises IndexError
* #3873: Failure of deprecation warning mechanism of
  ``sphinx.util.compat.Directive``
* #3874: Bogus warnings for "citation not referenced" for cross-file citations
* #3860: Don't download images when builders not supported images
* #3860: Remote image URIs without filename break builders not supported remote
  images
* #3833: command line messages are translated unintentionally with ``language``
  setting.
* #3840: make checking ``epub_uid`` strict
* #3851, #3706: Fix about box drawing characters for PDF output
* #3900: autosummary could not find methods
* #3902: Emit error if ``latex_documents`` contains non-unicode string in py2

Release 1.6.2 (released May 28, 2017)
=====================================

Incompatible changes
--------------------

* #3789: Do not require typing module for python>=3.5

Bugs fixed
----------

* #3754: HTML builder crashes if HTML theme appends own stylesheets
* #3756: epub: Entity 'mdash' not defined
* #3758: Sphinx crashed if logs are emitted in conf.py
* #3755: incorrectly warns about dedent with literalinclude
* #3742: `RTD <https://readthedocs.org/>`_ PDF builds of Sphinx own docs are
  missing an index entry in the bookmarks and table of contents. This is
  `rtfd/readthedocs.org#2857
  <https://github.com/rtfd/readthedocs.org/issues/2857>`_ issue, a workaround
  is obtained using some extra LaTeX code in Sphinx's own :file:`conf.py`
* #3770: Build fails when a "code-block" has the option emphasize-lines and the
  number indicated is higher than the number of lines
* #3774: Incremental HTML building broken when using citations
* #3763: got epubcheck validations error if epub_cover is set
* #3779: 'ImportError' in sphinx.ext.autodoc due to broken 'sys.meta_path'.
  Thanks to Tatiana Tereshchenko.
* #3796: env.resolve_references() crashes when non-document node given
* #3803: Sphinx crashes with invalid PO files
* #3791: PDF "continued on next page" for long tables isn't internationalized
* #3788: smartquotes emits warnings for unsupported languages
* #3807: latex Makefile for ``make latexpdf`` is only for unixen
* #3781: double hyphens in option directive are compiled as endashes
* #3817: latex builder raises AttributeError

Release 1.6.1 (released May 16, 2017)
=====================================

Dependencies
------------

1.6b1

* (updated) latex output is tested with Ubuntu trusty's texlive packages (Feb.
  2014) and earlier tex installations may not be fully compliant, particularly
  regarding Unicode engines xelatex and lualatex
* (added) latexmk is required for ``make latexpdf`` on GNU/Linux and Mac OS X
  (refs: #3082)

Incompatible changes
--------------------

1.6b1

* #1061, #2336, #3235: Now generation of autosummary doesn't contain imported
  members by default. Thanks to Luc Saffre.
* LaTeX ``\includegraphics`` command isn't overloaded: only
  ``\sphinxincludegraphics`` has the custom code to fit image to available width
  if oversized.
* The subclasses of ``sphinx.domains.Index`` should override ``generate()``
  method.  The default implementation raises NotImplementedError
* LaTeX positioned long tables horizontally centered, and short ones
  flushed left (no text flow around table.) The position now defaults to center
  in both cases, and it will obey Docutils 0.13 ``:align:`` option (refs #3415,
  #3377)
* option directive also allows all punctuations for the option name (refs:
  #3366)
* #3413: if :rst:dir:`literalinclude`'s ``:start-after:`` is used, make
  ``:lines:`` relative (refs #3412)
* ``literalinclude`` directive does not allow the combination of ``:diff:``
  option and other options (refs: #3416)
* LuaLaTeX engine uses ``fontspec`` like XeLaTeX. It is advised ``latex_engine
  = 'lualatex'`` be used only on up-to-date TeX installs (refs #3070, #3466)
* :confval:`latex_keep_old_macro_names` default value has been changed from
  ``True`` to ``False``. This means that some LaTeX macros for styling are
  by default defined only with ``\sphinx..`` prefixed names. (refs: #3429)
* Footer "Continued on next page" of LaTeX longtable's now not framed (refs:
  #3497)
* #3529: The arguments of ``BuildEnvironment.__init__`` is changed
* #3082: Use latexmk for pdf (and dvi) targets (Unix-like platforms only)
* #3558: Emit warnings if footnotes and citations are not referenced.  The
  warnings can be suppressed by ``suppress_warnings``.
* latex made available (non documented) colour macros from a file distributed
  with pdftex engine for Plain TeX. This is removed in order to provide better
  support for multiple TeX engines. Only interface from ``color`` or
  ``xcolor`` packages should be used by extensions of Sphinx latex writer.
  (refs #3550)
* ``Builder.env`` is not filled at instantiation
* #3594: LaTeX: single raw directive has been considered as block level element
* #3639: If ``html_experimental_html5_writer`` is available, epub builder use it
  by default.
* ``Sphinx.add_source_parser()`` raises an error if duplicated

1.6b2

* #3345: Replace the custom smartypants code with Docutils' smart_quotes.
  Thanks to Dmitry Shachnev, and to Günter Milde at Docutils.

1.6b3

* LaTeX package ``eqparbox`` is not used and not loaded by Sphinx anymore
* LaTeX package ``multirow`` is not used and not loaded by Sphinx anymore
* Add line numbers to citation data in std domain

1.6 final

* LaTeX package ``threeparttable`` is not used and not loaded by Sphinx
  anymore (refs #3686, #3532, #3377)

Features removed
----------------

* Configuration variables

  - epub3_contributor
  - epub3_description
  - epub3_page_progression_direction
  - html_translator_class
  - html_use_modindex
  - latex_font_size
  - latex_paper_size
  - latex_preamble
  - latex_use_modindex
  - latex_use_parts

* ``termsep`` node
* defindex.html template
* LDML format support in ``today``, ``today_fmt`` and ``html_last_updated_fmt``
* ``:inline:`` option for the directives of sphinx.ext.graphviz extension
* sphinx.ext.pngmath extension
* ``sphinx.util.compat.make_admonition()``

Features added
--------------

1.6b1

* #3136: Add ``:name:`` option to the directives in ``sphinx.ext.graphviz``
* #2336: Add ``imported_members`` option to ``sphinx-autogen`` command to
  document imported members.
* C++, add ``:tparam-line-spec:`` option to templated declarations.
  When specified, each template parameter will be rendered on a separate line.
* #3359: Allow sphinx.js in a user locale dir to override sphinx.js from Sphinx
* #3303: Add ``:pyversion:`` option to the doctest directive.
* #3378: (latex) support for ``:widths:`` option of table directives
  (refs: #3379, #3381)
* #3402: Allow to suppress "download file not readable" warnings using
  :confval:`suppress_warnings`.
* #3377: latex: Add support for Docutils 0.13 ``:align:`` option for tables
  (but does not implement text flow around table).
* latex: footnotes from inside tables are hyperlinked (except from captions or
  headers) (refs: #3422)
* Emit warning if over dedent has detected on ``literalinclude`` directive
  (refs: #3416)
* Use for LuaLaTeX same default settings as for XeLaTeX (i.e. ``fontspec`` and
  ``polyglossia``). (refs: #3070, #3466)
* Make ``'extraclassoptions'`` key of ``latex_elements`` public (refs #3480)
* #3463: Add warning messages for required EPUB3 metadata. Add default value to
  ``epub_description`` to avoid warning like other settings.
* #3476: setuptools: Support multiple builders
* latex: merged cells in LaTeX tables allow code-blocks, lists, blockquotes...
  as do normal cells (refs: #3435)
* HTML builder uses experimental HTML5 writer if
  ``html_experimental_html5_writer`` is True and docutils 0.13 or later is
  installed.
* LaTeX macros to customize space before and after tables in PDF output (refs
  #3504)
* #3348: Show decorators in literalinclude and viewcode directives
* #3108: Show warning if :start-at: and other literalinclude options does not
  match to the text
* #3609: Allow to suppress "duplicate citation" warnings using
  ``suppress_warnings``
* #2803: Discovery of builders by entry point
* #1764, #1676: Allow setting 'rel' and 'title' attributes for stylesheets
* #3589: Support remote images on non-HTML builders
* #3589: Support images in Data URI on non-HTML builders
* #2961: improve :confval:`autodoc_mock_imports`. Now the config value only
  requires to declare the top-level modules that should be mocked.
  Thanks to Robin Jarry.
* #3449: On py3, autodoc use inspect.signature for more accurate signature
  calculation. Thanks to Nathaniel J. Smith.
* #3641: Epub theme supports HTML structures that are generated by HTML5 writer.
* #3644 autodoc uses inspect instead of checking types. Thanks to
  Jeroen Demeyer.
* Add a new extension; ``sphinx.ext.imgconverter``. It converts images in the
  document to appropriate format for builders
* latex: Use templates to render tables (refs #3389, 2a37b0e)

1.6b2

* ``LATEXMKOPTS`` variable for the Makefile in ``$BUILDDIR/latex`` to pass
  options to ``latexmk`` when executing ``make latexpdf`` (refs #3695, #3720)
* Add a new event `env-check-consistency` to check consistency to extensions
* Add `Domain.check_consistency()` to check consistency

Bugs fixed
----------

1.6b1

* ``literalinclude`` directive expands tabs after dedent-ing (refs: #3416)
* #1574: Paragraphs in table cell doesn't work in Latex output
* #3288: Table with merged headers not wrapping text
* #3491: Inconsistent vertical space around table and longtable in PDF
* #3506: Depart functions for all admonitions in HTML writer now properly pass
  ``node`` to ``depart_admonition``.
* #2693: Sphinx latex style file wrongly inhibits colours for section headings
  for latex+dvi(ps,pdf,pdfmx)
* C++, properly look up ``any`` references.
* #3624: sphinx.ext.intersphinx couldn't load inventories compressed with gzip
* #3551: PDF information dictionary is lacking author and title data
* #3351: intersphinx does not refers context like ``py:module``, ``py:class``
  and so on.
* Fail to load template file if the parent template is archived

1.6b2

* #3661: sphinx-build crashes on parallel build
* #3669: gettext builder fails with "ValueError: substring not found"
* #3660: Sphinx always depends on sphinxcontrib-websupport and its dependencies
* #3472: smart quotes getting wrong in latex (at least with list of strings via
  autoattribute) (refs: #3345, #3666)

1.6b3

* #3588: No compact (p tag) html output in the i18n document build even when
  :confval:`html_compact_lists` is True.
* The ``make latexpdf`` from 1.6b1 (for GNU/Linux and Mac OS, using
  ``latexmk``) aborted earlier in case of LaTeX errors than was the case with
  1.5 series, due to hard-coded usage of ``--halt-on-error`` option (refs #3695)
* #3683: sphinx.websupport module is not provided by default
* #3683: Failed to build document if builder.css_file.insert() is called
* #3714: viewcode extension not taking ``highlight_code='none'`` in account
* #3698: Moving :doc: to std domain broke backwards compatibility
* #3633: misdetect unreferenced citations

1.6 final

* LaTeX tables do not allow multiple paragraphs in a header cell
* LATEXOPTS is not passed over correctly to pdflatex since 1.6b3
* #3532: Figure or literal block captions in cells of short tables cause havoc
  in PDF output
* Fix: in PDF captions of tables are rendered differently whether table is of
  longtable class or not (refs #3686)
* #3725: Todo looks different from note in LaTeX output
* #3479: stub-columns have no effect in LaTeX output
* #3738: Nonsensical code in theming.py
* #3746: PDF builds fail with latexmk 4.48 or earlier due to undefined
  options ``-pdfxe`` and ``-pdflua``

Deprecated
----------

1.6b1

* ``sphinx.util.compat.Directive`` class is now deprecated. Please use instead
  ``docutils.parsers.rst.Directive``
* ``sphinx.util.compat.docutils_version`` is now deprecated
* #2367: ``Sphinx.warn()``, ``Sphinx.info()`` and other logging methods are now
  deprecated.  Please use ``sphinx.util.logging`` (:ref:`logging-api`) instead.
* #3318: ``notice`` is now deprecated as LaTeX environment name and will be
  removed at Sphinx 1.7. Extension authors please use ``sphinxadmonition``
  instead (as Sphinx does since 1.5.)
* ``Sphinx.status_iterator()`` and ``Sphinx.old_status_iterator()`` is now
  deprecated.  Please use ``sphinx.util:status_iterator()`` instead.
* ``Sphinx._directive_helper()`` is deprecated. Please use
  ``sphinx.util.docutils.directive_helper()`` instead.
* ``BuildEnvironment.set_warnfunc()`` is now deprecated
* Following methods of ``BuildEnvironment`` is now deprecated.

  - ``BuildEnvironment.note_toctree()``
  - ``BuildEnvironment.get_toc_for()``
  - ``BuildEnvironment.get_toctree_for()``
  - ``BuildEnvironment.create_index()``

  Please use ``sphinx.environment.adapters`` modules instead.
* latex package  ``footnote`` is not loaded anymore by its bundled replacement
  ``footnotehyper-sphinx``. The redefined macros keep the same names as in the
  original package.
* #3429: deprecate config setting ``latex_keep_old_macro_names``. It will be
  removed at 1.7, and already its default value has changed from ``True`` to
  ``False``.
* #3221: epub2 builder is deprecated
* #3254: ``sphinx.websupport`` is now separated into independent package;
  ``sphinxcontrib-websupport``.  ``sphinx.websupport`` will be removed in
  Sphinx-2.0.
* #3628: ``sphinx_themes`` entry_point is deprecated.  Please use
  ``sphinx.html_themes`` instead.

1.6b2

* #3662: ``builder.css_files`` is deprecated.  Please use ``add_stylesheet()``
  API instead.

1.6 final

* LaTeX ``\sphinxstylethead`` is deprecated at 1.6 and will be removed at 1.7.
  Please move customization into new macro ``\sphinxstyletheadfamily``.

Testing
--------

1.6 final

* #3458: Add ``sphinx.testing`` (experimental)

Release 1.6 (unreleased)
========================

* not released (because of package script error)

Release 1.5.6 (released May 15, 2017)
=====================================

Bugs fixed
----------

* #3614: Sphinx crashes with requests-2.5.0
* #3618: autodoc crashes with tupled arguments
* #3664: No space after the bullet in items of a latex list produced by Sphinx
* #3657: EPUB builder crashes if a document starting with genindex exists
* #3588: No compact (p tag) html output in the i18n document build even when
  :confval:`html_compact_lists` is True.
* #3685: AttributeError when using 3rd party domains
* #3702: LaTeX writer styles figure legends with a hard-coded ``\small``
* #3708: LaTeX writer allows irc scheme
* #3717: Stop enforcing that favicon's must be .ico
* #3731, #3732: Protect isenumclass predicate against non-class arguments
* #3320: Warning about reference target not being found for container types
* Misspelled ARCHIVEPREFIX in Makefile for latex build repertory

Release 1.5.5 (released Apr 03, 2017)
=====================================

Bugs fixed
----------

* #3597: python domain raises UnboundLocalError if invalid name given
* #3599: Move to new MathJax CDN

Release 1.5.4 (released Apr 02, 2017)
=====================================

Features added
--------------

* #3470: Make genindex support all kinds of letters, not only Latin ones

Bugs fixed
----------

* #3445: setting ``'inputenc'`` key to ``\\usepackage[utf8x]{inputenc}`` leads
  to failed PDF build
* EPUB file has duplicated ``nav.xhtml`` link in ``content.opf``
  except first time build
* #3488: objects.inv has broken when ``release`` or ``version`` contain
  return code
* #2073, #3443, #3490: gettext builder that writes pot files unless the content
  are same without creation date. Thanks to Yoshiki Shibukawa.
* #3487: intersphinx: failed to refer options
* #3496: latex longtable's last column may be much wider than its contents
* #3507: wrong quotes in latex output for productionlist directive
* #3533: Moving from Sphinx 1.3.1 to 1.5.3 breaks LaTeX compilation of links
  rendered as code
* #2665, #2607: Link names in C++ docfields, and make it possible for other
  domains.
* #3542: C++, fix parsing error of non-type template argument with template.
* #3065, #3520: python domain fails to recognize nested class
* #3575: Problems with pdflatex in a Turkish document built with sphinx has
  reappeared (refs #2997, #2397)
* #3577: Fix intersphinx debug tool
* A LaTeX command such as ``\\large`` inserted in the title items of
  :confval:`latex_documents` causes failed PDF build (refs #3551, #3567)

Release 1.5.3 (released Feb 26, 2017)
=====================================

Features added
--------------

* Support requests-2.0.0 (experimental) (refs: #3367)
* (latex) PDF page margin dimensions may be customized (refs: #3387)
* ``literalinclude`` directive allows combination of ``:pyobject:`` and
  ``:lines:`` options (refs: #3416)
* #3400: make-mode doesn't use subprocess on building docs

Bugs fixed
----------

* #3370: the caption of code-block is not picked up for translation
* LaTeX: :confval:`release` is not escaped (refs: #3362)
* #3364: sphinx-quickstart prompts overflow on Console with 80 chars width
* since 1.5, PDF's TOC and bookmarks lack an entry for general Index
  (refs: #3383)
* #3392: ``'releasename'`` in :confval:`latex_elements` is not working
* #3356: Page layout for Japanese ``'manual'`` docclass has a shorter text area
* #3394: When ``'pointsize'`` is not ``10pt``, Japanese ``'manual'`` document
  gets wrong PDF page dimensions
* #3399: quickstart: conf.py was not overwritten by template
* #3366: option directive does not allow punctuations
* #3410: return code in :confval:`release` breaks html search
* #3427: autodoc: memory addresses are not stripped on Windows
* #3428: xetex build tests fail due to fontspec v2.6 defining ``\strong``
* #3349: Result of ``IndexBuilder.load()`` is broken
* #3450: &nbsp is appeared in EPUB docs
* #3418: Search button is misaligned in nature and pyramid theme
* #3421: Could not translate a caption of tables
* #3552: linkcheck raises UnboundLocalError

Release 1.5.2 (released Jan 22, 2017)
=====================================

Incompatible changes
--------------------

* Dependency requirement updates: requests 2.4.0 or above (refs: #3268, #3310)

Features added
--------------

* #3241: emit latex warning if buggy titlesec (ref #3210)
* #3194: Refer the $MAKE environment variable to determine ``make`` command
* Emit warning for nested numbered toctrees (refs: #3142)
* #978: `intersphinx_mapping` also allows a list as a parameter
* #3340: (LaTeX) long lines in :dudir:`parsed-literal` are wrapped like in
  :rst:dir:`code-block`, inline math and footnotes are fully functional.

Bugs fixed
----------

* #3246: xapian search adapter crashes
* #3253: In Py2 environment, building another locale with a non-captioned
  toctree produces ``None`` captions
* #185: References to section title including raw node has broken
* #3255: In Py3.4 environment, autodoc doesn't support documentation for
  attributes of Enum class correctly.
* #3261: ``latex_use_parts`` makes sphinx crash
* The warning type ``misc.highlighting_failure`` does not work
* #3294: ``add_latex_package()`` make crashes non-LaTeX builders
* The caption of table are rendered as invalid HTML (refs: #3287)
* #3268: Sphinx crashes with requests package from Debian jessie
* #3284: Sphinx crashes on parallel build with an extension which raises
  unserializable exception
* #3315: Bibliography crashes on latex build with docclass 'memoir'
* #3328: Could not refer rubric implicitly
* #3329: emit warnings if po file is invalid and can't read it. Also writing mo
* #3337: Ugly rendering of definition list term's classifier
* #3335: gettext does not extract field_name of a field in a field_list
* #2952: C++, fix refs to operator() functions.
* Fix Unicode super- and subscript digits in :rst:dir:`code-block` and
  parsed-literal LaTeX output (ref #3342)
* LaTeX writer: leave ``"`` character inside parsed-literal as is (ref #3341)
* #3234: intersphinx failed for encoded inventories
* #3158: too much space after captions in PDF output
* #3317: An URL in parsed-literal contents gets wrongly rendered in PDF if
  with hyphen
* LaTeX crash if the filename of an image inserted in parsed-literal
  via a substitution contains an hyphen (ref #3340)
* LaTeX rendering of inserted footnotes in parsed-literal is wrong (ref #3340)
* Inline math in parsed-literal is not rendered well by LaTeX (ref #3340)
* #3308: Parsed-literals don't wrap very long lines with pdf builder (ref #3340)
* #3295: Could not import extension sphinx.builders.linkcheck
* #3285: autosummary: asterisks are escaped twice
* LaTeX, pass dvipdfm option to geometry package for Japanese documents (ref
  #3363)
* Fix parselinenos() could not parse left half open range (cf. "-4")


Release 1.5.1 (released Dec 13, 2016)
=====================================

Features added
--------------

* #3214: Allow to suppress "unknown mimetype" warnings from epub builder using
  :confval:`suppress_warnings`.

Bugs fixed
----------

* #3195: Can not build in parallel
* #3198: AttributeError is raised when toctree has 'self'
* #3211: Remove untranslated sphinx locale catalogs (it was covered by
  untranslated it_IT)
* #3212: HTML Builders crashes with docutils-0.13
* #3207: more latex problems with references inside parsed-literal directive
  (``\DUrole``)
* #3205: sphinx.util.requests crashes with old pyOpenSSL (< 0.14)
* #3220: KeyError when having a duplicate citation
* #3200: LaTeX: xref inside desc_name not allowed
* #3228: ``build_sphinx`` command crashes when missing dependency
* #2469: Ignore updates of catalog files for gettext builder. Thanks to
  Hiroshi Ohkubo.
* #3183: Randomized jump box order in generated index page.

Release 1.5 (released Dec 5, 2016)
==================================

Incompatible changes
--------------------

1.5a1

* latex, package fancybox is not any longer a dependency of sphinx.sty
* Use ``'locales'`` as a default value of `locale_dirs`
* latex, package ifthen is not any longer a dependency of sphinx.sty
* latex, style file does not modify fancyvrb's Verbatim (also available as
  OriginalVerbatim) but uses sphinxVerbatim for name of custom wrapper.
* latex, package newfloat is not used (and not included) anymore (ref #2660;
  it was used since 1.3.4 and shipped with Sphinx since 1.4).
* latex, literal blocks in tables do not use OriginalVerbatim but
  sphinxVerbatimintable which handles captions and wraps lines (ref #2704).
* latex, replace ``pt`` by TeX equivalent ``bp`` if found in ``width`` or
  ``height`` attribute of an image.
* latex, if ``width`` or ``height`` attribute of an image is given with no unit,
  use ``px`` rather than ignore it.
* latex: Separate stylesheets of pygments to independent .sty file
* #2454: The filename of sourcelink is now changed.  The value of
  `html_sourcelink_suffix` will be appended to the original filename (like
  ``index.rst.txt``).
* ``sphinx.util.copy_static_entry()`` is now deprecated.
  Use ``sphinx.util.fileutil.copy_asset()`` instead.
* ``sphinx.util.osutil.filecopy()`` skips copying if the file has not been
  changed (ref: #2510, #2753)
* Internet Explorer 6-8, Opera 12.1x or Safari 5.1+ support is dropped
  because jQuery version is updated from 1.11.0 to 3.1.0 (ref: #2634, #2773)
* QtHelpBuilder doesn't generate search page (ref: #2352)
* QtHelpBuilder uses ``nonav`` theme instead of default one
  to improve readability.
* latex: To provide good default settings to Japanese documents, Sphinx uses
  ``jreport`` and ``jsbook`` as docclass if :confval:`language` is
  ``ja``.
* ``sphinx-quickstart`` now allows a project version is empty
* Fix :download: role on epub/qthelp builder. They ignore the role because they
  don't support it.
* ``sphinx.ext.viewcode`` doesn't work on epub building by default.
  ``viewcode_enable_epub`` option
* ``sphinx.ext.viewcode`` disabled on singlehtml builder.
* Use make-mode of ``sphinx-quickstart`` by default.  To disable this, use
  ``-M`` option
* Fix ``genindex.html``, Sphinx's document template, link address to itself to
  satisfy xhtml standard.
* Use epub3 builder by default.  And the old epub builder is renamed to epub2.
* Fix ``epub`` and ``epub3`` builders that contained links to ``genindex`` even
  if ``epub_use_index = False``.
* ``html_translator_class`` is now deprecated.
  Use `Sphinx.set_translator()` API instead.
* Drop python 2.6 and 3.3 support
* Drop epub3 builder's ``epub3_page_progression_direction`` option (use
  ``epub3_writing_mode``).
* #2877: Rename ``latex_elements['footer']`` to
  ``latex_elements['atendofbody']``

1.5a2

* #2983: Rename ``epub3_description`` and ``epub3_contributor`` to
  ``epub_description`` and ``epub_contributor``.
* Remove themes/basic/defindex.html; no longer used
* Sphinx does not ship anymore (but still uses) LaTeX style file ``fncychap``
* #2435: Slim down quickstarted conf.py
* The ``sphinx.sty`` latex package does not load itself "hyperref", as this
  is done later in the preamble of the latex output via ``'hyperref'`` key.
* Sphinx does not ship anymore a custom modified LaTeX style file ``tabulary``.
  The non-modified package is used.
* #3057: By default, footnote marks in latex PDF output are not preceded by a
  space anymore, ``\sphinxBeforeFootnote`` allows user customization if needed.
* LaTeX target requires that option ``hyperfootnotes`` of package ``hyperref``
  be left unchanged to its default (i.e. ``true``) (refs: #3022)

1.5 final

* #2986: ``themes/basic/defindex.html`` is now deprecated
* Emit warnings that will be deprecated in Sphinx 1.6 by default.
  Users can change the behavior by setting the environment variable
  PYTHONWARNINGS. Please refer :ref:`when-deprecation-warnings-are-displayed`.
* #2454: new JavaScript variable ``SOURCELINK_SUFFIX`` is added

Deprecated
----------

These features are removed in Sphinx-1.6:

* LDML format  support in i18n feature
* ``sphinx.addnodes.termsep``
* Some functions and classes in ``sphinx.util.pycompat``:
  ``zip_longest``, ``product``, ``all``, ``any``, ``next``, ``open``,
  ``class_types``, ``base_exception``, ``relpath``, ``StringIO``, ``BytesIO``.
  Please use the standard library version instead;

If any deprecation warning like ``RemovedInSphinxXXXWarning`` are displayed,
please refer :ref:`when-deprecation-warnings-are-displayed`.

Features added
--------------

1.5a1

* #2951: Add ``--implicit-namespaces`` PEP-0420 support to apidoc.
* Add ``:caption:`` option for sphinx.ext.inheritance_diagram.
* #2471: Add config variable for default doctest flags.
* Convert linkcheck builder to requests for better encoding handling
* #2463, #2516: Add keywords of "meta" directive to search index
* ``:maxdepth:`` option of toctree affects ``secnumdepth`` (ref: #2547)
* #2575: Now ``sphinx.ext.graphviz`` allows ``:align:`` option
* Show warnings if unknown key is specified to `latex_elements`
* Show warnings if no domains match with `primary_domain` (ref: #2001)
* C++, show warnings when the kind of role is misleading for the kind
  of target it refers to (e.g., using the `class` role for a function).
* latex, writer abstracts more of text styling into customizable macros, e.g.
  the ``visit_emphasis`` will output ``\sphinxstyleemphasis`` rather than
  ``\emph`` (which may be in use elsewhere or in an added LaTeX package). See
  list at end of ``sphinx.sty`` (ref: #2686)
* latex, public names for environments and parameters used by note, warning,
  and other admonition types, allowing full customizability from the
  ``'preamble'`` key or an input file (ref: feature request #2674, #2685)
* latex, better computes column widths of some tables (as a result, there will
  be slight changes as tables now correctly fill the line width; ref: #2708)
* latex, sphinxVerbatim environment is more easily customizable (ref: #2704).
  In addition to already existing VerbatimColor and VerbatimBorderColor:

  - two lengths ``\sphinxverbatimsep`` and ``\sphinxverbatimborder``,
  - booleans ``\ifsphinxverbatimwithframe`` and ``\ifsphinxverbatimwrapslines``.

* latex, captions for literal blocks inside tables are handled, and long code
  lines wrapped to fit table cell (ref: #2704)
* #2597: Show warning messages as darkred
* latex, allow image dimensions using px unit (default is 96px=1in)
* Show warnings if invalid dimension units found
* #2650: Add ``--pdb`` option to setup.py command
* latex, make the use of ``\small`` for code listings customizable (ref #2721)
* #2663: Add ``--warning-is-error`` option to setup.py command
* Show warnings if deprecated latex options are used
* Add sphinx.config.ENUM to check the config values is in candidates
* math: Add hyperlink marker to each equations in HTML output
* Add new theme ``nonav`` that doesn't include any navigation links.
  This is for any help generator like qthelp.
* #2680: `sphinx.ext.todo` now emits warnings if `todo_emit_warnings` enabled.
  Also, it emits an additional event named `todo-defined` to handle the TODO
  entries in 3rd party extensions.
* Python domain signature parser now uses the xref mixin for 'exceptions',
  allowing exception classes to be autolinked.
* #2513: Add `latex_engine` to switch the LaTeX engine by conf.py
* #2682: C++, basic support for attributes (C++11 style and GNU style).
  The new configuration variables 'cpp_id_attributes' and 'cpp_paren_attributes'
  can be used to introduce custom attributes.
* #1958: C++, add configuration variable 'cpp_index_common_prefix' for removing
  prefixes from the index text of C++ objects.
* C++, added concept directive. Thanks to mickk-on-cpp.
* C++, added support for template introduction syntax. Thanks to mickk-on-cpp.
* #2725: latex builder: allow to use user-defined template file (experimental)
* apidoc now avoids invalidating cached files by not writing to files whose
  content doesn't change. This can lead to significant performance wins if
  apidoc is run frequently.
* #2851: ``sphinx.ext.math`` emits missing-reference event if equation not found
* #1210: ``eqref`` role now supports cross reference
* #2892: Added ``-a`` (``--append-syspath``) option to ``sphinx-apidoc``
* #1604: epub3 builder: Obey font-related CSS when viewing in iBooks.
* #646: ``option`` directive support '.' character as a part of options
* Add document about kindlegen and fix document structure for it.
* #2474: Add ``intersphinx_timeout`` option to ``sphinx.ext.intersphinx``
* #2926: EPUB3 builder supports vertical mode (``epub3_writing_mode`` option)
* #2695: ``build_sphinx`` subcommand for setuptools handles exceptions as same
  as ``sphinx-build`` does
* #326: `numref` role can also refer sections
* #2916: `numref` role can also refer caption as an its linktext

1.5a2

* #3008: ``linkcheck`` builder ignores self-signed certificate URL
* #3020: new ``'geometry'`` key to ``latex_elements`` whose default uses
  LaTeX style file ``geometry.sty`` to set page layout
* #2843: Add :start-at: and :end-at: options to literalinclude directive
* #2527: Add ``:reversed:`` option to toctree directive
* Add ``-t`` and ``-d`` option to ``sphinx-quickstart`` to support templating
  generated sphinx project.
* #3028: Add ``{path}`` and ``{basename}`` to the format of
  ``figure_language_filename``
* new ``'hyperref'`` key in the ``latex_elements`` dictionary (ref #3030)
* #3022: Allow code-blocks in footnotes for LaTeX PDF output

1.5b1

* #2513: A better default settings for XeLaTeX
* #3096: ``'maxlistdepth'`` key to work around LaTeX list limitations
* #3060: autodoc supports documentation for attributes of Enum class. Now
  autodoc render just the value of Enum attributes instead of Enum attribute
  representation.
* Add ``--extensions`` to ``sphinx-quickstart`` to support enable arbitrary
  extensions from command line (ref: #2904)
* #3104, #3122: ``'sphinxsetup'`` for key=value styling of Sphinx LaTeX
* #3071: Autodoc: Allow mocked module decorators to pass-through functions
  unchanged
* #2495: linkcheck: Allow skipping anchor checking using
  :confval:`linkcheck_anchors_ignore`
* #3083: let Unicode no-break space act like LaTeX ``~`` (fixed #3019)
* #3116: allow word wrap in PDF output for inline literals (ref #3110)
* #930: sphinx-apidoc allow wildcards for excluding paths. Thanks to Nick
  Coghlan.
* #3121: add ``inlineliteralwraps`` option to control if inline literal
  word-wraps in latex

1.5 final

* #3095: Add :confval:`tls_verify` and :confval:`tls_cacerts` to support
  self-signed HTTPS servers in linkcheck and intersphinx
* #2215: make.bat generated by sphinx-quickstart can be called from another dir.
  Thanks to Timotheus Kampik.
* #3185: Add new warning type ``misc.highlighting_failure``

Bugs fixed
----------

1.5a1

* #2707: (latex) the column width is badly computed for tabular
* #2799: Sphinx installs roles and directives automatically on importing sphinx
  module.  Now Sphinx installs them on running application.
* `sphinx.ext.autodoc` crashes if target code imports * from mock modules
  by `autodoc_mock_imports`.
* #1953: ``Sphinx.add_node`` does not add handlers the translator installed by
  ``html_translator_class``
* #1797: text builder inserts blank line on top
* #2894: quickstart main() doesn't use argv argument
* #2874: gettext builder could not extract all text under the ``only``
  directives
* #2485: autosummary crashes with multiple source_suffix values
* #1734: Could not translate the caption of toctree directive
* Could not translate the content of meta directive (ref: #1734)
* #2550: external links are opened in help viewer
* #2687: Running Sphinx multiple times produces 'already registered' warnings

1.5a2

* #2810: Problems with pdflatex in an Italian document
* Use ``latex_elements.papersize`` to specify papersize of LaTeX in Makefile
* #2988: linkcheck: retry with GET request if denied HEAD request
* #2990: linkcheck raises "Can't convert 'bytes' object to str implicitly" error
  if linkcheck_anchors enabled
* #3004: Invalid link types "top" and "up" are used
* #3009: Bad rendering of parsed-literals in LaTeX since Sphinx 1.4.4
* #3000: ``option`` directive generates invalid HTML anchors
* #2984: Invalid HTML has been generated if `html_split_index` enabled
* #2986: themes/basic/defindex.html should be changed for html5 friendly
* #2987: Invalid HTML has been generated if multiple IDs are assigned to a list
* #2891: HTML search does not provide all the results
* #1986: Title in PDF Output
* #147: Problem with latex chapter style
* #3018: LaTeX problem with page layout dimensions and chapter titles
* Fix an issue with ``\pysigline`` in LaTeX style file (ref #3023)
* #3038: ``sphinx.ext.math*`` raises TypeError if labels are duplicated
* #3031: incompatibility with LaTeX package ``tocloft``
* #3003: literal blocks in footnotes are not supported by Latex
* #3047: spacing before footnote in pdf output is not coherent and allows breaks
* #3045: HTML search index creator should ignore "raw" content if now html
* #3039: English stemmer returns wrong word if the word is capitalized
* Fix make-mode Makefile template (ref #3056, #2936)

1.5b1

* #2432: Fix unwanted * between varargs and keyword only args. Thanks to Alex
  Grönholm.
* #3062: Failed to build PDF using 1.5a2 (undefined ``\hypersetup`` for
  Japanese documents since PR#3030)
* Better rendering of multiline signatures in html.
* #777: LaTeX output "too deeply nested" (ref #3096)
* Let LaTeX image inclusion obey ``scale`` before textwidth fit (ref #2865,
  #3059)
* #3019: LaTeX fails on description of C function with arguments (ref #3083)
* fix latex inline literals where ``< > -`` gobbled a space

1.5 final

* #3069: Even if ``'babel'`` key is set to empty string, LaTeX output contains
  one ``\addto\captions...``
* #3123: user ``'babel'`` key setting is not obeyed anymore
* #3155: Fix JavaScript for `html_sourcelink_suffix` fails with IE and Opera
* #3085: keep current directory after breaking build documentation. Thanks to
  Timotheus Kampik.
* #3181: pLaTeX crashes with a section contains endash
* #3180: latex: add stretch/shrink between successive singleline or
  multipleline cpp signatures (ref #3072)
* #3128: globing images does not support .svgz file
* #3015: fix a broken test on Windows.
* #1843: Fix documentation of descriptor classes that have a custom metaclass.
  Thanks to Erik Bray.
* #3190: util.split_docinfo fails to parse multi-line field bodies
* #3024, #3037: In Python3, application.Sphinx._log crushed when the log message
  cannot be encoded into console encoding.

Testing
--------

* To simplify, sphinx uses external mock package even if unittest.mock exists.


Release 1.4.9 (released Nov 23, 2016)
=====================================

Bugs fixed
----------

* #2936: Fix doc/Makefile that can't build man because doc/man exists
* #3058: Using the same 'caption' attribute in multiple 'toctree' directives
  results in warning / error
* #3068: Allow the '=' character in the -D option of sphinx-build.py
* #3074: ``add_source_parser()`` crashes in debug mode
* #3135: ``sphinx.ext.autodoc`` crashes with plain Callable
* #3150: Fix query word splitter in JavaScript. It behaves as same as Python's
  regular expression.
* #3093: gettext build broken on substituted images.
* #3093: gettext build broken on image node under ``note`` directive.
* imgmath: crashes on showing error messages if image generation failed
* #3117: LaTeX writer crashes if admonition is placed before first section title
* #3164: Change search order of ``sphinx.ext.inheritance_diagram``

Release 1.4.8 (released Oct 1, 2016)
====================================

Bugs fixed
----------

* #2996: The wheel package of Sphinx got crash with ImportError

Release 1.4.7 (released Oct 1, 2016)
====================================

Bugs fixed
----------

* #2890: Quickstart should return an error consistently on all error conditions
* #2870: flatten genindex columns' heights.
* #2856: Search on generated HTML site doesn't find some symbols
* #2882: Fall back to a GET request on 403 status in linkcheck
* #2902: jsdump.loads fails to load search index if keywords starts with
  underscore
* #2900: Fix epub content.opf: add auto generated orphan files to spine.
* #2899: Fix ``hasdoc()`` function in Jinja2 template. It will detect
  ``genindex``, ``search`` also.
* #2901: Fix epub result: skip creating links from image tags to original image
  files.
* #2917: inline code is hyphenated on HTML
* #1462: autosummary warns for namedtuple with attribute with trailing
  underscore
* Could not reference equations if ``:nowrap:`` option specified
* #2873: code-block overflow in latex (due to commas)
* #1060, #2056: sphinx.ext.intersphinx: broken links are generated if relative
  paths are used in `intersphinx_mapping`
* #2931: code-block directive with same :caption: causes warning of duplicate
  target.  Now `code-block` and `literalinclude` does not define hyperlink
  target using its caption automatically.
* #2962: latex: missing label of longtable
* #2968: autodoc: show-inheritance option breaks docstrings

Release 1.4.6 (released Aug 20, 2016)
=====================================

Incompatible changes
--------------------

* #2867: linkcheck builder crashes with six-1.4.  Now Sphinx depends on six-1.5
  or later

Bugs fixed
----------

* applehelp: Sphinx crashes if ``hiutil`` or ``codesign`` commands not found
* Fix ``make clean`` abort issue when build dir contains regular files like
  ``DS_Store``.
* Reduce epubcheck warnings/errors:

  * Fix DOCTYPE to html5
  * Change extension from .html to .xhtml.
  * Disable search page on epub results

* #2778: Fix autodoc crashes if obj.__dict__ is a property method and raises
  exception
* Fix duplicated toc in epub3 output.
* #2775: Fix failing linkcheck with servers not supporting identity encoding
* #2833: Fix formatting instance annotations in ext.autodoc.
* #1911: ``-D`` option of ``sphinx-build`` does not override the ``extensions``
  variable
* #2789: `sphinx.ext.intersphinx` generates wrong hyperlinks if the inventory is
  given
* parsing errors for caption of code-blocks are displayed in document
  (ref: #2845)
* #2846: ``singlehtml`` builder does not include figure numbers
* #2816: Fix data from builds cluttering the ``Domain.initial_data`` class
  attributes

Release 1.4.5 (released Jul 13, 2016)
=====================================

Incompatible changes
--------------------

* latex, inclusion of non-inline images from image directive resulted in
  non-coherent whitespaces depending on original image width; new behaviour
  by necessity differs from earlier one in some cases. (ref: #2672)
* latex, use of ``\includegraphics`` to refer to Sphinx custom variant is
  deprecated; in future it will revert to original LaTeX macro, custom one
  already has alternative name ``\sphinxincludegraphics``.

Features added
--------------

* new config option ``latex_keep_old_macro_names``, defaults to True. If False,
  lets macros (for text styling) be defined only with ``\sphinx``-prefixed names
* latex writer allows user customization of "shadowed" boxes (topics), via
  three length variables.
* woff-format web font files now supported by the epub builder.

Bugs fixed
----------

* jsdump fix for python 3: fixes the HTML search on python > 3
* #2676: (latex) Error with verbatim text in captions since Sphinx 1.4.4
* #2629: memoir class crashes LaTeX. Fixed by
  ``latex_keep_old_macro_names=False`` (ref 2675)
* #2684: `sphinx.ext.intersphinx` crashes with six-1.4.1
* #2679: ``float`` package needed for ``'figure_align': 'H'`` latex option
* #2671: image directive may lead to inconsistent spacing in pdf
* #2705: ``toctree`` generates empty bullet_list if ``:titlesonly:`` specified
* #2479: `sphinx.ext.viewcode` uses python2 highlighter by default
* #2700: HtmlHelp builder has hard coded index.html
* latex, since 1.4.4 inline literal text is followed by spurious space
* #2722: C++, fix id generation for var/member declarations to include
  namespaces.
* latex, images (from image directive) in lists or quoted blocks did not obey
  indentation (fixed together with #2671)
* #2733: since Sphinx-1.4.4 ``make latexpdf`` generates lots of hyperref
  warnings
* #2731: `sphinx.ext.autodoc` does not access propertymethods which raises any
  exceptions
* #2666: C++, properly look up nested names involving constructors.
* #2579: Could not refer a label including both spaces and colons via
  `sphinx.ext.intersphinx`
* #2718: Sphinx crashes if the document file is not readable
* #2699: hyperlinks in help HTMLs are broken if `html_file_suffix` is set
* #2723: extra spaces in latex pdf output from multirow cell
* #2735: latexpdf ``Underfull \hbox (badness 10000)`` warnings from title page
* #2667: latex crashes if resized images appeared in section title
* #2763: (html) Provide default value for required ``alt`` attribute for image
  tags of SVG source, required to validate and now consistent w/ other formats.


Release 1.4.4 (released Jun 12, 2016)
=====================================

Bugs fixed
----------

* #2630: latex: sphinx.sty notice environment formatting problem
* #2632: Warning directives fail in quote environment latex build
* #2633: Sphinx crashes with old styled indices
* Fix a ``\begin{\minipage}`` typo in sphinx.sty from 1.4.2 (ref: 68becb1)
* #2622: Latex produces empty pages after title and table of contents
* #2640: 1.4.2 LaTeX crashes if code-block inside warning directive
* Let LaTeX use straight quotes also in inline code (ref #2627)
* #2351: latex crashes if enumerated lists are placed on footnotes
* #2646: latex crashes if math contains twice empty lines
* #2480: `sphinx.ext.autodoc`: memory addresses were shown
* latex: allow code-blocks appearing inside lists and quotes at maximal nesting
  depth (ref #777, #2624, #2651)
* #2635: Latex code directives produce inconsistent frames based on viewing
  resolution
* #2639: Sphinx now bundles iftex.sty
* Failed to build PDF with framed.sty 0.95
* Sphinx now bundles needspace.sty


Release 1.4.3 (released Jun 5, 2016)
====================================

Bugs fixed
----------

* #2530: got "Counter too large" error on building PDF if large numbered
  footnotes existed in admonitions
* ``width`` option of figure directive does not work if ``align`` option
  specified at same time (ref: #2595)
* #2590: The ``inputenc`` package breaks compiling under lualatex and xelatex
* #2540: date on latex front page use different font
* Suppress "document isn't included in any toctree" warning if the document is
  included (ref: #2603)
* #2614: Some tables in PDF output will end up shifted if user sets non zero
  \parindent in preamble
* #2602: URL redirection breaks the hyperlinks generated by
  `sphinx.ext.intersphinx`
* #2613: Show warnings if merged extensions are loaded
* #2619: make sure amstext LaTeX package always loaded (ref: d657225, 488ee52,
  9d82cad and #2615)
* #2593: latex crashes if any figures in the table


Release 1.4.2 (released May 29, 2016)
=====================================

Features added
--------------

* Now :confval:`suppress_warnings` accepts following configurations
  (ref: #2451, #2466):

  - ``app.add_node``
  - ``app.add_directive``
  - ``app.add_role``
  - ``app.add_generic_role``
  - ``app.add_source_parser``
  - ``image.data_uri``
  - ``image.nonlocal_uri``

* #2453: LaTeX writer allows page breaks in topic contents; and their
  horizontal extent now fits in the line width (with shadow in margin). Also
  warning-type admonitions allow page breaks and their vertical spacing has
  been made more coherent with the one for hint-type notices (ref #2446).

* #2459: the framing of literal code-blocks in LaTeX output (and not only the
  code lines themselves) obey the indentation in lists or quoted blocks.

* #2343: the long source lines in code-blocks are wrapped (without modifying
  the line numbering) in LaTeX output (ref #1534, #2304).

Bugs fixed
----------

* #2370: the equations are slightly misaligned in LaTeX writer
* #1817, #2077: suppress pep8 warnings on conf.py generated by sphinx-quickstart
* #2407: building docs crash if document includes large data image URIs
* #2436: Sphinx does not check version by :confval:`needs_sphinx` if loading
  extensions failed
* #2397: Setup shorthandoff for Turkish documents
* #2447: VerbatimBorderColor wrongly used also for captions of PDF
* #2456: C++, fix crash related to document merging (e.g., singlehtml and Latex
  builders).
* #2446: latex(pdf) sets local tables of contents (or more generally topic
  nodes) in unbreakable boxes, causes overflow at bottom
* #2476: Omit MathJax markers if :nowrap: is given
* #2465: latex builder fails in case no caption option is provided to toctree
  directive
* Sphinx crashes if self referenced toctree found
* #2481: spelling mistake for mecab search splitter. Thanks to Naoki Sato.
* #2309: Fix could not refer "indirect hyperlink targets" by ref-role
* intersphinx fails if mapping URL contains any port
* #2088: intersphinx crashes if the mapping URL requires basic auth
* #2304: auto line breaks in latexpdf codeblocks
* #1534: Word wrap long lines in Latex verbatim blocks
* #2460: too much white space on top of captioned literal blocks in PDF output
* Show error reason when multiple math extensions are loaded (ref: #2499)
* #2483: any figure number was not assigned if figure title contains only non
  text objects
* #2501: Unicode subscript numbers are normalized in LaTeX
* #2492: Figure directive with :figwidth: generates incorrect Latex-code
* The caption of figure is always put on center even if ``:align:`` was
  specified
* #2526: LaTeX writer crashes if the section having only images
* #2522: Sphinx touches mo files under installed directory that caused
  permission error.
* #2536: C++, fix crash when an immediately nested scope has the same name as
  the current scope.
* #2555: Fix crash on any-references with unicode.
* #2517: wrong bookmark encoding in PDF if using LuaLaTeX
* #2521: generated Makefile causes BSD make crashed if sphinx-build not found
* #2470: ``typing`` backport package causes autodoc errors with python 2.7
* ``sphinx.ext.intersphinx`` crashes if non-string value is used for key of
  `intersphinx_mapping`
* #2518: `intersphinx_mapping` disallows non alphanumeric keys
* #2558: unpack error on devhelp builder
* #2561: Info builder crashes when a footnote contains a link
* #2565: The descriptions of objects generated by ``sphinx.ext.autosummary``
  overflow lines at LaTeX writer
* Extend pdflatex config in sphinx.sty to subparagraphs (ref: #2551)
* #2445: `rst_prolog` and `rst_epilog` affect to non reST sources
* #2576: ``sphinx.ext.imgmath`` crashes if subprocess raises error
* #2577: ``sphinx.ext.imgmath``: Invalid argument are passed to dvisvgm
* #2556: Xapian search does not work with Python 3
* #2581: The search doesn't work if language="es" (Spanish)
* #2382: Adjust spacing after abbreviations on figure numbers in LaTeX writer
* #2383: The generated footnote by `latex_show_urls` overflows lines
* #2497, #2552: The label of search button does not fit for the button itself


Release 1.4.1 (released Apr 12, 2016)
=====================================

Incompatible changes
--------------------

* The default format of `today_fmt` and `html_last_updated_fmt` is back to
  strftime format again.  Locale Date Markup Language is also supported for
  backward compatibility until Sphinx-1.5.

Translations
------------

* Added Welsh translation, thanks to Geraint Palmer.
* Added Greek translation, thanks to Stelios Vitalis.
* Added Esperanto translation, thanks to Dinu Gherman.
* Added Hindi translation, thanks to Purnank H. Ghumalia.
* Added Romanian translation, thanks to Razvan Stefanescu.

Bugs fixed
----------

* C++, added support for ``extern`` and ``thread_local``.
* C++, type declarations are now using the prefixes ``typedef``, ``using``, and
  ``type``, depending on the style of declaration.
* #2413: C++, fix crash on duplicate declarations
* #2394: Sphinx crashes when html_last_updated_fmt is invalid
* #2408: dummy builder not available in Makefile and make.bat
* #2412: hyperlink targets are broken in LaTeX builder
* figure directive crashes if non paragraph item is given as caption
* #2418: time formats no longer allowed in today_fmt
* #2395: Sphinx crashes if unicode character in image filename
* #2396: "too many values to unpack" in genindex-single
* #2405: numref link in PDF jumps to the wrong location
* #2414: missing number in PDF hyperlinks to code listings
* #2440: wrong import for gmtime. Thanks to Uwe L. Korn.


Release 1.4 (released Mar 28, 2016)
===================================

Incompatible changes
--------------------
* Drop ``PorterStemmer`` package support. Use ``PyStemmer`` instead of
  ``PorterStemmer`` to accelerate stemming.
* sphinx_rtd_theme has become optional. Please install it manually.
  Refs #2087, #2086, #1845 and #2097. Thanks to Victor Zverovich.
* #2231: Use DUrole instead of DUspan for custom roles in LaTeX writer. It
  enables to take title of roles as an argument of custom macros.
* #2022: 'Thumbs.db' and '.DS_Store' are added to `exclude_patterns` default
  values in conf.py that will be provided on sphinx-quickstart.
* #2027, #2208: The ``html_title`` accepts string values only. And The None
  value cannot be accepted.
* ``sphinx.ext.graphviz``: show graph image in inline by default
* #2060, #2224: The ``manpage`` role now generate ``sphinx.addnodes.manpage``
  node instead of ``sphinx.addnodes.literal_emphasis`` node.
* #2022: :confval:`html_extra_path` also copies dotfiles in the extra directory,
  and refers to :confval:`exclude_patterns` to exclude extra files and
  directories.
* #2300: enhance autoclass:: to use the docstring of __new__ if __init__
  method's is missing of empty
* #2251: Previously, under glossary directives, multiple terms for one
  definition are converted into single ``term`` node and the each terms in the
  term node are separated by ``termsep`` node. In new implementation, each terms
  are converted into individual ``term`` nodes and ``termsep`` node is removed.
  By this change, output layout of every builders are changed a bit.
* The default highlight language is now Python 3.  This means that source code
  is highlighted as Python 3 (which is mostly a superset of Python 2), and no
  parsing is attempted to distinguish valid code.  To get the old behavior back,
  add ``highlight_language = "python"`` to conf.py.
* `Locale Date Markup Language
  <https://unicode.org/reports/tr35/tr35-dates.html#Date_Format_Patterns>`_ like
  ``"MMMM dd, YYYY"`` is default format for `today_fmt` and
  `html_last_updated_fmt`.  However strftime format like ``"%B %d, %Y"`` is also
  supported for backward compatibility until Sphinx-1.5. Later format will be
  disabled from Sphinx-1.5.
* #2327: ``latex_use_parts`` is deprecated now. Use `latex_toplevel_sectioning`
  instead.
* #2337: Use ``\url{URL}`` macro instead of ``\href{URL}{URL}`` in LaTeX writer.
* #1498: manpage writer: don't make whole of item in definition list bold if it
  includes strong node.
* #582: Remove hint message from quick search box for html output.
* #2378: Sphinx now bundles newfloat.sty

Features added
--------------
* #2092: add todo directive support in napoleon package.
* #1962: when adding directives, roles or nodes from an extension, warn if such
  an element is already present (built-in or added by another extension).
* #1909: Add "doc" references to Intersphinx inventories.
* C++ type alias support (e.g., ``.. type:: T = int``).
* C++ template support for classes, functions, type aliases, and variables
  (#1729, #1314).
* C++, added new scope management directives ``namespace-push`` and
  ``namespace-pop``.
* #1970: Keyboard shortcuts to navigate Next and Previous topics
* Intersphinx: Added support for fetching Intersphinx inventories with URLs
  using HTTP basic auth.
* C++, added support for template parameter in function info field lists.
* C++, added support for pointers to member (function).
* #2113: Allow ``:class:`` option to code-block directive.
* #2192: Imgmath (pngmath with svg support).
* #2200: Support XeTeX and LuaTeX for the LaTeX builder.
* #1906: Use xcolor over color for \fcolorbox where available for LaTeX output.
* #2216: Texinputs makefile improvements.
* #2170: Support for Chinese language search index.
* #2214: Add sphinx.ext.githubpages to publish the docs on GitHub Pages
* #1030: Make page reference names for latex_show_pagerefs translatable
* #2162: Add Sphinx.add_source_parser() to add source_suffix and source_parsers
  from extension
* #2207: Add sphinx.parsers.Parser class; a base class for new parsers
* #656: Add ``graphviz_dot`` option to graphviz directives to switch the ``dot``
  command
* #1939: Added the ``dummy`` builder: syntax check without output.
* #2230: Add ``math_number_all`` option to number all displayed math in math
  extensions
* #2235: ``needs_sphinx`` supports micro version comparison
* #2282: Add "language" attribute to html tag in the "basic" theme
* #1779: Add EPUB 3 builder
* #1751: Add :confval:`todo_link_only` to avoid file path and line indication on
  :rst:dir:`todolist`. Thanks to Francesco Montesano.
* #2199: Use ``imagesize`` package to obtain size of images.
* #1099: Add configurable retries to the linkcheck builder. Thanks to Alex
  Gaynor.  Also don't check anchors starting with ``!``.
* #2300: enhance autoclass:: to use the docstring of __new__ if __init__
  method's is missing of empty
* #1858: Add Sphinx.add_enumerable_node() to add enumerable nodes for numfig
  feature
* #1286, #2099: Add ``sphinx.ext.autosectionlabel`` extension to allow reference
  sections using its title. Thanks to Tadhg O'Higgins.
* #1854: Allow to choose Janome for Japanese splitter.
* #1853: support custom text splitter on html search with ``language='ja'``.
* #2320: classifier of glossary terms can be used for index entries grouping key
  The classifier also be used for translation. See also
  :ref:`glossary-directive`.
* #2308: Define ``\tablecontinued`` macro to redefine the style of continued
  label for longtables.
* Select an image by similarity if multiple images are globbed by
  ``.. image:: filename.*``
* #1921: Support figure substitutions by :confval:`language` and
  :confval:`figure_language_filename`
* #2245: Add ``latex_elements["passoptionstopackages"]`` option to call
  PassOptionsToPackages in early stage of preambles.
* #2340: Math extension: support alignment of multiple equations for MathJax.
* #2338: Define ``\titleref`` macro to redefine the style of ``title-reference``
  roles.
* Define ``\menuselection`` and ``\accelerator`` macros to redefine the style of
  `menuselection` roles.
* Define ``\crossref`` macro to redefine the style of references
* #2301: Texts in the classic html theme should be hyphenated.
* #2355: Define ``\termref`` macro to redefine the style of ``term`` roles.
* Add :confval:`suppress_warnings` to suppress arbitrary warning message
  (experimental)
* #2229: Fix no warning is given for unknown options
* #2327: Add `latex_toplevel_sectioning` to switch the top level sectioning of
  LaTeX document.

Bugs fixed
----------
* #1913: C++, fix assert bug for enumerators in next-to-global and global scope.
* C++, fix parsing of 'signed char' and 'unsigned char' as types.
* C++, add missing support for 'friend' functions.
* C++, add missing support for virtual base classes (thanks to Rapptz).
* C++, add support for final classes.
* C++, fix parsing of types prefixed with 'enum'.
* #2023: Dutch search support uses Danish stemming info.
* C++, add support for user-defined literals.
* #1804: Now html output wraps overflowed long-line-text in the sidebar. Thanks
  to Hassen ben tanfous.
* #2183: Fix porterstemmer causes ``make json`` to fail.
* #1899: Ensure list is sent to OptParse.
* #2164: Fix wrong check for pdftex inside sphinx.sty (for graphicx package
  option).
* #2165, #2218: Remove faulty and non-need conditional from sphinx.sty.
* Fix broken LaTeX code is generated if unknown language is given
* #1944: Fix rst_prolog breaks file-wide metadata
* #2074: make gettext should use canonical relative paths for .pot. Thanks to
  anatoly techtonik.
* #2311: Fix sphinx.ext.inheritance_diagram raises AttributeError
* #2251: Line breaks in .rst files are transferred to .pot files in a wrong way.
* #794: Fix date formatting in latex output is not localized
* Remove ``image/gif`` from supported_image_types of LaTeX writer (#2272)
* Fix ValueError is raised if LANGUAGE is empty string
* Fix unpack warning is shown when the directives generated from
  ``Sphinx.add_crossref_type`` is used
* The default highlight language is now ``default``.  This means that source
  code is highlighted as Python 3 (which is mostly a superset of Python 2) if
  possible.  To get the old behavior back, add ``highlight_language = "python"``
  to conf.py.
* #2329: Refresh environment forcedly if source directory has changed.
* #2331: Fix code-blocks are filled by block in dvi; remove ``xcdraw`` option
  from xcolor package
* Fix the confval type checker emits warnings if unicode is given to confvals
  which expects string value
* #2360: Fix numref in LaTeX output is broken
* #2361: Fix additional paragraphs inside the "compound" directive are indented
* #2364: Fix KeyError 'rootSymbol' on Sphinx upgrade from older version.
* #2348: Move amsmath and amssymb to before fontpkg on LaTeX writer.
* #2368: Ignore emacs lock files like ``.#foo.rst`` by default.
* #2262: literal_block and its caption has been separated by pagebreak in LaTeX
  output.
* #2319: Fix table counter is overridden by code-block's in LaTeX.  Thanks to
  jfbu.
* Fix unpack warning if combined with 3rd party domain extensions.
* #1153: Fix figures in sidebar causes latex build error.
* #2358: Fix user-preamble could not override the tocdepth definition.
* #2358: Reduce tocdepth if ``part`` or ``chapter`` is used for top_sectionlevel
* #2351: Fix footnote spacing
* #2363: Fix ``toctree()`` in templates generates broken links in
  SingleHTMLBuilder.
* #2366: Fix empty hyperref is generated on toctree in HTML builder.

Documentation
-------------

* #1757: Fix for usage of :confval:`html_last_updated_fmt`. Thanks to Ralf
  Hemmecke.


Release 1.3.6 (released Feb 29, 2016)
=====================================

Features added
--------------

* #1873, #1876, #2278: Add ``page_source_suffix`` html context variable. This
  should be introduced with :confval:`source_parsers` feature. Thanks for Eric
  Holscher.


Bugs fixed
----------

* #2265: Fix babel is used in spite of disabling it on ``latex_elements``
* #2295: Avoid mutating dictionary errors while enumerating members in autodoc
  with Python 3
* #2291: Fix pdflatex "Counter too large" error from footnotes inside tables of
  contents
* #2292: Fix some footnotes disappear from LaTeX output
* #2287: ``sphinx.transforms.Locale`` always uses rst parser. Sphinx i18n
  feature should support parsers that specified source_parsers.
* #2290: Fix ``sphinx.ext.mathbase`` use of amsfonts may break user choice of
  math fonts
* #2324: Print a hint how to increase the recursion limit when it is hit.
* #1565, #2229: Revert new warning; the new warning will be triggered from
  version 1.4 on.
* #2329: Refresh environment forcedly if source directory has changed.
* #2019: Fix the domain objects in search result are not escaped

Release 1.3.5 (released Jan 24, 2016)
=====================================

Bugs fixed
----------

* Fix line numbers was not shown on warnings in LaTeX and texinfo builders
* Fix filenames were not shown on warnings of citations
* Fix line numbers was not shown on warnings in LaTeX and texinfo builders
* Fix line numbers was not shown on warnings of indices
* #2026: Fix LaTeX builder raises error if parsed-literal includes links
* #2243: Ignore strange docstring types for classes, do not crash
* #2247: Fix #2205 breaks make html for definition list with classifiers
  that contains regular-expression like string
* #1565: Sphinx will now emit a warning that highlighting was skipped if the
  syntax is incorrect for `code-block`, `literalinclude` and so on.
* #2211: Fix paragraphs in table cell doesn't work in Latex output
* #2253: ``:pyobject:`` option of ``literalinclude`` directive can't detect
  indented body block when the block starts with blank or comment lines.
* Fix TOC is not shown when no ``:maxdepth:`` for toctrees (ref: #771)
* Fix warning message for ``:numref:`` if target is in orphaned doc (ref: #2244)

Release 1.3.4 (released Jan 12, 2016)
=====================================

Bugs fixed
----------

* #2134: Fix figure caption with reference causes latex build error
* #2094: Fix rubric with reference not working in Latex
* #2147: Fix literalinclude code in latex does not break in pages
* #1833: Fix email addresses is showed again if latex_show_urls is not None
* #2176: sphinx.ext.graphviz: use <object> instead of <img> to embed svg
* #967: Fix SVG inheritance diagram is not hyperlinked (clickable)
* #1237: Fix footnotes not working in definition list in LaTeX
* #2168: Fix raw directive does not work for text writer
* #2171: Fix cannot linkcheck url with unicode
* #2182: LaTeX: support image file names with more than 1 dots
* #2189: Fix previous sibling link for first file in subdirectory uses last
  file, not intended previous from root toctree
* #2003: Fix decode error under python2 (only) when ``make linkcheck`` is run
* #2186: Fix LaTeX output of \mathbb in math
* #1480, #2188: LaTeX: Support math in section titles
* #2071: Fix same footnote in more than two section titles => LaTeX/PDF Bug
* #2040: Fix UnicodeDecodeError in sphinx-apidoc when author contains non-ascii
  characters
* #2193: Fix shutil.SameFileError if source directory and destination directory
  are same
* #2178: Fix unparsable C++ cross-reference when referencing a function with
  :cpp:any:
* #2206: Fix Sphinx latex doc build failed due to a footnotes
* #2201: Fix wrong table caption for tables with over 30 rows
* #2213: Set <blockquote> in the classic theme to fit with <p>
* #1815: Fix linkcheck does not raise an exception if warniserror set to true
  and link is broken
* #2197: Fix slightly cryptic error message for missing index.rst file
* #1894: Unlisted phony targets in quickstart Makefile
* #2125: Fix unifies behavior of collapsed fields (``GroupedField`` and
  ``TypedField``)
* #1408: Check latex_logo validity before copying
* #771: Fix latex output doesn't set tocdepth
* #1820: On Windows, console coloring is broken with colorama version 0.3.3.
  Now sphinx use colorama>=0.3.5 to avoid this problem.
* #2072: Fix footnotes in chapter-titles do not appear in PDF output
* #1580: Fix paragraphs in longtable don't work in Latex output
* #1366: Fix centered image not centered in latex
* #1860: Fix man page using ``:samp:`` with braces - font doesn't reset
* #1610: Sphinx crashes in Japanese indexing in some systems
* Fix Sphinx crashes if mecab initialization failed
* #2160: Fix broken TOC of PDFs if section includes an image
* #2172: Fix dysfunctional admonition ``\py@lightbox`` in sphinx.sty. Thanks to
  jfbu.
* #2198,#2205: ``make gettext`` generate broken msgid for definition lists.
* #2062: Escape characters in doctests are treated incorrectly with Python 2.
* #2225: Fix if the option does not begin with dash, linking is not performed
* #2226: Fix math is not HTML-encoded when :nowrap: is given (jsmath, mathjax)
* #1601, #2220: 'any' role breaks extended domains behavior. Affected extensions
  doesn't support resolve_any_xref and resolve_xref returns problematic node
  instead of None.  sphinxcontrib-httpdomain is one of them.
* #2229: Fix no warning is given for unknown options

Release 1.3.3 (released Dec 2, 2015)
====================================

Bugs fixed
----------

* #2177: Fix parallel hangs
* #2012: Fix exception occurred if ``numfig_format`` is invalid
* #2142: Provide non-minified JS code in ``sphinx/search/non-minified-js/*.js``
  for source distribution on PyPI.
* #2148: Error while building devhelp target with non-ASCII document.


Release 1.3.2 (released Nov 29, 2015)
=====================================

Features added
--------------

* #1935: Make "numfig_format" overridable in latex_elements.

Bugs fixed
----------

* #1976: Avoid "2.0" version of Babel because it doesn't work with Windows
  environment.
* Add a "default.css" stylesheet (which imports "classic.css") for compatibility
* #1788: graphviz extension raises exception when caption option is present.
* #1789: ``:pyobject:`` option of ``literalinclude`` directive includes
  following lines after class definitions
* #1790: ``literalinclude`` strips empty lines at the head and tail
* #1802: load plugin themes automatically when theme.conf use it as 'inherit'.
  Thanks to Takayuki Hirai.
* #1794: custom theme extended from alabaster or sphinx_rtd_theme can't find
  base theme.
* #1834: compatibility for docutils-0.13: handle_io_errors keyword argument for
  docutils.io.FileInput cause TypeError.
* #1823: '.' as <module_path> for sphinx-apidoc cause an unfriendly error. Now
  '.' is converted to absolute path automatically.
* Fix a crash when setting up extensions which do not support metadata.
* #1784: Provide non-minified JS code in ``sphinx/search/non-minified-js/*.js``
* #1822, #1892: Fix regression for #1061. autosummary can't generate doc for
  imported members since sphinx-1.3b3. Thanks to Eric Larson.
* #1793, #1819: "see also" misses a linebreak in text output. Thanks to Takayuki
  Hirai.
* #1780, #1866: "make text" shows "class" keyword twice. Thanks to Takayuki
  Hirai.
* #1871: Fix for LaTeX output of tables with one column and multirows.
* Work around the lack of the HTMLParserError exception in Python 3.5.
* #1949: Use ``safe_getattr`` in the coverage builder to avoid aborting with
  descriptors that have custom behavior.
* #1915: Do not generate smart quotes in doc field type annotations.
* #1796: On py3, automated .mo building caused UnicodeDecodeError.
* #1923: Use babel features only if the babel latex element is nonempty.
* #1942: Fix a KeyError in websupport.
* #1903: Fix strange id generation for glossary terms.
* ``make text`` will crush if a definition list item has more than 1 classifiers
  as: ``term : classifier1 : classifier2``.
* #1855: make gettext generates broken po file for definition lists with
  classifier.
* #1869: Fix problems when dealing with files containing non-ASCII characters.
  Thanks to Marvin Schmidt.
* #1798: Fix building LaTeX with references in titles.
* #1725: On py2 environment, doctest with using non-ASCII characters causes
  ``'ascii' codec can't decode byte`` exception.
* #1540: Fix RuntimeError with circular referenced toctree
* #1983: i18n translation feature breaks references which uses section name.
* #1990: Use caption of toctree to title of \tableofcontents in LaTeX
* #1987: Fix ampersand is ignored in ``:menuselection:`` and ``:guilabel:``
  on LaTeX builder
* #1994: More supporting non-standard parser (like recommonmark parser) for
  Translation and WebSupport feature. Now node.rawsource is fall backed to
  node.astext() during docutils transforming.
* #1989: "make blahblah" on Windows indicate help messages for sphinx-build
  every time.  It was caused by wrong make.bat that generated by
  Sphinx-1.3.0/1.3.1.
* On Py2 environment, conf.py that is generated by sphinx-quickstart should have
  u prefixed config value for 'version' and 'release'.
* #2102: On Windows + Py3, using ``|today|`` and non-ASCII date format will
  raise UnicodeEncodeError.
* #1974: UnboundLocalError: local variable 'domain' referenced before assignment
  when using `any` role and `sphinx.ext.intersphinx` in same time.
* #2121: multiple words search doesn't find pages when words across on the page
  title and the page content.
* #1884, #1885: plug-in html themes cannot inherit another plug-in theme. Thanks
  to Suzumizaki.
* #1818: `sphinx.ext.todo` directive generates broken html class attribute as
  'admonition-' when :confval:`language` is specified with non-ASCII linguistic
  area like 'ru' or 'ja'. To fix this, now ``todo`` directive can use
  ``:class:`` option.
* #2140: Fix footnotes in table has broken in LaTeX
* #2127: MecabBinder for html searching feature doesn't work with Python 3.
  Thanks to Tomoko Uchida.


Release 1.3.1 (released Mar 17, 2015)
=====================================

Bugs fixed
----------

* #1769: allows generating quickstart files/dirs for destination dir that
  doesn't overwrite existent files/dirs. Thanks to WAKAYAMA shirou.
* #1773: sphinx-quickstart doesn't accept non-ASCII character as a option
  argument.
* #1766: the message "least Python 2.6 to run" is at best misleading.
* #1772: cross reference in docstrings like ``:param .write:`` breaks building.
* #1770, #1774: ``literalinclude`` with empty file occurs exception. Thanks to
  Takayuki Hirai.
* #1777: Sphinx 1.3 can't load extra theme. Thanks to tell-k.
* #1776: ``source_suffix = ['.rst']`` cause unfriendly error on prior version.
* #1771: automated .mo building doesn't work properly.
* #1783: Autodoc: Python2 Allow unicode string in __all__.
  Thanks to Jens Hedegaard Nielsen.
* #1781: Setting `html_domain_indices` to a list raises a type check warnings.


Release 1.3 (released Mar 10, 2015)
===================================

Incompatible changes
--------------------

* Roles ``ref``, ``term`` and ``menusel`` now don't generate :durole:`emphasis`
  nodes anymore.  If you want to keep italic style, adapt your stylesheet.
* Role ``numref`` uses ``%s`` as special character to indicate position of
  figure numbers instead ``#`` symbol.

Features added
--------------

* Add convenience directives and roles to the C++ domain:
  directive ``cpp:var`` as alias for ``cpp:member``, role ``:cpp:var`` as alias
  for ``:cpp:member``, and role `any` for cross-reference to any C++
  declaraction. #1577, #1744
* The :confval:`source_suffix` config value can now be a list of multiple
  suffixes.
* Add the ability to specify source parsers by source suffix with the
  :confval:`source_parsers` config value.
* #1675: A new builder, AppleHelpBuilder, has been added that builds Apple
  Help Books.

Bugs fixed
----------

* 1.3b3 change breaks a previous gettext output that contains duplicated
  msgid such as "foo bar" and "version changes in 1.3: foo bar".
* #1745: latex builder cause maximum recursion depth exceeded when a
  footnote has a footnote mark itself.
* #1748: SyntaxError in sphinx/ext/ifconfig.py with Python 2.6.
* #1658, #1750: No link created (and warning given) if option does not
  begin with -, / or +. Thanks to Takayuki Hirai.
* #1753: C++, added missing support for more complex declarations.
* #1700: Add ``:caption:`` option for :rst:dir:`toctree`.
* #1742: ``:name:`` option is provided for :rst:dir:`toctree`,
  :rst:dir:`code-block` and :rst:dir:`literalinclude` directives.
* #1756: Incorrect section titles in search that was introduced from 1.3b3.
* #1746: C++, fixed name lookup procedure, and added missing lookups in
  declarations.
* #1765: C++, fix old id generation to use fully qualified names.

Documentation
-------------

* #1651: Add ``vartype`` field description for python domain.


Release 1.3b3 (released Feb 24, 2015)
=====================================

Incompatible changes
--------------------

* Dependency requirement updates: docutils 0.11, Pygments 2.0
* The ``gettext_enables`` config value has been renamed to
  `gettext_additional_targets`.
* #1735: Use https://docs.python.org/ instead of ``http`` protocol.
  It was used for `sphinx.ext.intersphinx` and some documentation.

Features added
--------------

* #1346: Add new default theme;

  * Add 'alabaster' theme.
  * Add 'sphinx_rtd_theme' theme.
  * The 'default' html theme has been renamed to 'classic'. 'default' is still
    available, however it will emit notice a recommendation that using new
    'alabaster' theme.

* Added ``highlight_options`` configuration value.
* The ``language`` config value is now available in the HTML templates.
* The ``env-updated`` event can now return a value, which is interpreted
  as an iterable of additional docnames that need to be rewritten.
* #772: Support for scoped and unscoped enums in C++. Enumerators in unscoped
  enums are injected into the parent scope in addition to the enum scope.
* Add ``todo_include_todos`` config option to quickstart conf file, handled as
  described in documentation.
* HTML breadcrumb items tag has class "nav-item" and "nav-item-N" (like
  nav-item-0, 1, 2...).
* New option `sphinx-quickstart --use-make-mode` for generating Makefile that
  use sphinx-build make-mode.
* #1235: i18n: several node can be translated if it is set to
  `gettext_additional_targets` in conf.py. Supported nodes are:

  - 'literal-block'
  - 'doctest-block'
  - 'raw'
  - 'image'

* #1227: Add `html_scaled_image_link` config option to conf.py, to control
  scaled image link.

Bugs fixed
----------

* LaTeX writer now generates correct markup for cells spanning multiple rows.
* #1674: Do not crash if a module's ``__all__`` is not a list of strings.
* #1629: Use VerbatimBorderColor to add frame to code-block in LaTeX
* On windows, make-mode didn't work on Win32 platform if sphinx was invoked as
  ``python sphinx-build.py``.
* #1687: linkcheck now treats 401 Unauthorized responses as "working".
* #1690: toctrees with ``glob`` option now can also contain entries for single
  documents with explicit title.
* #1591: html search results for C++ elements now has correct interpage links.
* bizstyle theme: nested long title pages make long breadcrumb that breaks page
  layout.
* bizstyle theme: all breadcrumb items become 'Top' on some mobile browser
  (iPhone5s safari).
* #1722: restore ``toctree()`` template function behavior that was changed at
  1.3b1.
* #1732: i18n: localized table caption raises exception.
* #1718: ``:numref:`` does not work with capital letters in the label
* #1630: resolve CSS conflicts, ``div.container`` css target for literal block
  wrapper now renamed to ``div.literal-block-wrapper``.
* ``sphinx.util.pycompat`` has been restored in its backwards-compatibility;
  slated for removal in Sphinx 1.4.
* #1719: LaTeX writer does not respect ``numref_format`` option in captions


Release 1.3b2 (released Dec 5, 2014)
====================================

Incompatible changes
--------------------

* update bundled ez_setup.py for setuptools-7.0 that requires Python 2.6 or
  later.

Features added
--------------

* #1597: Added possibility to return a new template name from
  `html-page-context`.
* PR#314, #1150: Configuration values are now checked for their type.  A
  warning is raised if the configured and the default value do not have the
  same type and do not share a common non-trivial base class.

Bugs fixed
----------

* PR#311: sphinx-quickstart does not work on python 3.4.
* Fix :confval:`autodoc_docstring_signature` not working with signatures
  in class docstrings.
* Rebuilding cause crash unexpectedly when source files were added.
* #1607: Fix a crash when building latexpdf with "howto" class
* #1251: Fix again. Sections which depth are lower than :tocdepth: should not
  be shown on localtoc sidebar.
* make-mode didn't work on Win32 platform if sphinx was installed by wheel
  package.


Release 1.3b1 (released Oct 10, 2014)
=====================================

Incompatible changes
--------------------

* Dropped support for Python 2.5, 3.1 and 3.2.
* Dropped support for docutils versions up to 0.9.
* Removed the ``sphinx.ext.oldcmarkup`` extension.
* The deprecated config values ``exclude_trees``, ``exclude_dirnames`` and
  ``unused_docs`` have been removed.
* A new node, ``sphinx.addnodes.literal_strong``, has been added, for text that
  should appear literally (i.e. no smart quotes) in strong font.  Custom writers
  will have to be adapted to handle this node.
* PR#269, #1476: replace ``<tt>`` tag by ``<code>``. User customized stylesheets
  should be updated If the css contain some styles for ``tt>`` tag.
  Thanks to Takeshi Komiya.
* #1543: `templates_path` is automatically added to
  `exclude_patterns` to avoid reading autosummary rst templates in the
  templates directory.
* Custom domains should implement the new `Domain.resolve_any_xref`
  method to make the `any` role work properly.
* gettext builder: gettext doesn't emit uuid information to generated pot files
  by default. Please set ``True`` to `gettext_uuid` to emit uuid information.
  Additionally, if the ``python-levenshtein`` 3rd-party package is installed,
  it will improve the calculation time.
* gettext builder: disable extracting/apply 'index' node by default. Please set
  'index' to ``gettext_enables`` to enable extracting index entries.
* PR#307: Add frame to code-block in LaTeX. Thanks to Takeshi Komiya.

Features added
--------------

* Add support for Python 3.4.
* Add support for docutils 0.12
* Added ``sphinx.ext.napoleon`` extension for NumPy and Google style docstring
  support.
* Added support for parallel reading (parsing) of source files with the
  `sphinx-build -j` option.  Third-party extensions will need to be checked for
  compatibility and may need to be adapted if they store information in the
  build environment object.  See `env-merge-info`.
* Added the `any` role that can be used to find a cross-reference of
  *any* type in *any* domain.  Custom domains should implement the new
  `Domain.resolve_any_xref` method to make this work properly.
* Exception logs now contain the last 10 messages emitted by Sphinx.
* Added support for extension versions (a string returned by ``setup()``, these
  can be shown in the traceback log files).  Version requirements for extensions
  can be specified in projects using the new `needs_extensions` config
  value.
* Changing the default role within a document with the :dudir:`default-role`
  directive is now supported.
* PR#214: Added stemming support for 14 languages, so that the built-in document
  search can now handle these.  Thanks to Shibukawa Yoshiki.
* PR#296, PR#303, #76: numfig feature: Assign numbers to figures, tables and
  code-blocks. This feature is configured with `numfig`, `numfig_secnum_depth`
  and `numfig_format`. Also `numref` role is available. Thanks to Takeshi
  Komiya.
* PR#202: Allow "." and "~" prefixed references in ``:param:`` doc fields
  for Python.
* PR#184: Add `autodoc_mock_imports`, allowing to mock imports of
  external modules that need not be present when autodocumenting.
* #925: Allow list-typed config values to be provided on the command line,
  like ``-D key=val1,val2``.
* #668: Allow line numbering of `code-block` and `literalinclude` directives
  to start at an arbitrary line number, with a new ``lineno-start`` option.
* PR#172, PR#266: The `code-block` and `literalinclude`
  directives now can have a ``caption`` option that shows a filename before the
  code in the output. Thanks to Nasimul Haque, Takeshi Komiya.
* Prompt for the document language in sphinx-quickstart.
* PR#217: Added config values to suppress UUID and location information in
  generated gettext catalogs.
* PR#236, #1456: apidoc: Add a -M option to put module documentation before
  submodule documentation. Thanks to Wes Turner and Luc Saffre.
* #1434: Provide non-minified JS files for jquery.js and underscore.js to
  clarify the source of the minified files.
* PR#252, #1291: Windows color console support. Thanks to meu31.
* PR#255: When generating latex references, also insert latex target/anchor
  for the ids defined on the node. Thanks to Olivier Heurtier.
* PR#229: Allow registration of other translators. Thanks to Russell Sim.
* Add app.set_translator() API to register or override a Docutils translator
  class like ``html_translator_class``.
* PR#267, #1134: add 'diff' parameter to literalinclude. Thanks to Richard Wall
  and WAKAYAMA shirou.
* PR#272: Added 'bizstyle' theme. Thanks to Shoji KUMAGAI.
* Automatically compile ``*.mo`` files from ``*.po`` files when
  `gettext_auto_build` is True (default) and ``*.po`` is newer than
  ``*.mo`` file.
* #623: `sphinx.ext.viewcode` supports imported function/class aliases.
* PR#275: `sphinx.ext.intersphinx` supports multiple target for the
  inventory. Thanks to Brigitta Sipocz.
* PR#261: Added the `env-before-read-docs` event that can be connected to modify
  the order of documents before they are read by the environment.
* #1284: Program options documented with :rst:dir:`option` can now start with
  ``+``.
* PR#291: The caption of :rst:dir:`code-block` is recognized as a title of ref
  target. Thanks to Takeshi Komiya.
* PR#298: Add new API: :meth:`~sphinx.application.Sphinx.add_latex_package`.
  Thanks to Takeshi Komiya.
* #1344: add ``gettext_enables`` to enable extracting 'index' to gettext
  catalog output / applying translation catalog to generated documentation.
* PR#301, #1583: Allow the line numbering of the directive `literalinclude` to
  match that of the included file, using a new ``lineno-match`` option. Thanks
  to Jeppe Pihl.
* PR#299: add various options to sphinx-quickstart. Quiet mode option
  ``--quiet`` will skips wizard mode. Thanks to WAKAYAMA shirou.
* #1623: Return types specified with ``:rtype:`` are now turned into links if
  possible.

Bugs fixed
----------

* #1438: Updated jQuery version from 1.8.3 to 1.11.1.
* #1568: Fix a crash when a "centered" directive contains a reference.
* Now sphinx.ext.autodoc works with python-2.5 again.
* #1563: :meth:`~sphinx.application.Sphinx.add_search_language` raises
  AssertionError for correct type of argument. Thanks to rikoman.
* #1174: Fix smart quotes being applied inside roles like :rst:role:`program` or
  `makevar`.
* PR#235: comment db schema of websupport lacked a length of the node_id field.
  Thanks to solos.
* #1466,PR#241: Fix failure of the cpp domain parser to parse C+11
  "variadic templates" declarations. Thanks to Victor Zverovich.
* #1459,PR#244: Fix default mathjax js path point to ``http://`` that cause
  mixed-content error on HTTPS server. Thanks to sbrandtb and robo9k.
* PR#157: autodoc remove spurious signatures from @property decorated
  attributes. Thanks to David Ham.
* PR#159: Add coverage targets to quickstart generated Makefile and make.bat.
  Thanks to Matthias Troffaes.
* #1251: When specifying toctree :numbered: option and :tocdepth: metadata,
  sub section number that is larger depth than ``:tocdepth:`` is shrunk.
* PR#260: Encode underscore in citation labels for latex export. Thanks to
  Lennart Fricke.
* PR#264: Fix could not resolve xref for figure node with :name: option.
  Thanks to Takeshi Komiya.
* PR#265: Fix could not capture caption of graphviz node by xref. Thanks to
  Takeshi Komiya.
* PR#263, #1013, #1103: Rewrite of C++ domain. Thanks to Jakob Lykke Andersen.

  * Hyperlinks to all found nested names and template arguments (#1103).
  * Support for function types everywhere, e.g., in
    std::function<bool(int, int)> (#1013).
  * Support for virtual functions.
  * Changed interpretation of function arguments to following standard
    prototype declarations, i.e., void f(arg) means that arg is the type of the
    argument, instead of it being the name.
  * Updated tests.
  * Updated documentation with elaborate description of what declarations are
    supported and how the namespace declarations influence declaration and
    cross-reference lookup.
  * Index names may be different now. Elements are indexed by their fully
    qualified name. It should be rather easy to change this behaviour and
    potentially index by namespaces/classes as well.

* PR#258, #939: Add dedent option for `code-block` and
  `literalinclude`. Thanks to Zafar Siddiqui.
* PR#268: Fix numbering section does not work at singlehtml mode. It still
  ad-hoc fix because there is a issue that section IDs are conflicted.
  Thanks to Takeshi Komiya.
* PR#273, #1536: Fix RuntimeError with numbered circular toctree. Thanks to
  Takeshi Komiya.
* PR#274: Set its URL as a default title value if URL appears in toctree.
  Thanks to Takeshi Komiya.
* PR#276, #1381: `rfc` and `pep` roles support custom link
  text. Thanks to Takeshi Komiya.
* PR#277, #1513: highlights for function pointers in argument list of
  `c:function`. Thanks to Takeshi Komiya.
* PR#278: Fix section entries were shown twice if toctree has been put under
  only directive. Thanks to Takeshi Komiya.
* #1547: pgen2 tokenizer doesn't recognize ``...`` literal (Ellipsis for py3).
* PR#294: On LaTeX builder, wrap float environment on writing literal_block
  to avoid separation of caption and body. Thanks to Takeshi Komiya.
* PR#295, #1520: ``make.bat latexpdf`` mechanism to ``cd`` back to the current
  directory. Thanks to Peter Suter.
* PR#297, #1571: Add imgpath property to all builders. It make easier to
  develop builder extensions. Thanks to Takeshi Komiya.
* #1584: Point to master doc in HTML "top" link.
* #1585: Autosummary of modules broken in Sphinx-1.2.3.
* #1610: Sphinx cause AttributeError when MeCab search option is enabled and
  python-mecab is not installed.
* #1674: Do not crash if a module's ``__all__`` is not a list of strings.
* #1673: Fix crashes with :confval:`nitpick_ignore` and ``:doc:`` references.
* #1686: ifconfig directive doesn't care about default config values.
* #1642: Fix only one search result appearing in Chrome.

Documentation
-------------

* Add clarification about the syntax of tags. (:file:`doc/markup/misc.rst`)


Release 1.2.3 (released Sep 1, 2014)
====================================

Features added
--------------

* #1518: ``sphinx-apidoc`` command now has a ``--version`` option to show
  version information and exit
* New locales: Hebrew, European Portuguese, Vietnamese.

Bugs fixed
----------

* #636: Keep straight single quotes in literal blocks in the LaTeX build.
* #1419: Generated i18n sphinx.js files are missing message catalog entries
  from '.js_t' and '.html'. The issue was introduced from Sphinx-1.1
* #1363: Fix i18n: missing python domain's cross-references with currentmodule
  directive or currentclass directive.
* #1444: autosummary does not create the description from attributes docstring.
* #1457: In python3 environment, make linkcheck cause "Can't convert 'bytes'
  object to str implicitly" error when link target url has a hash part.
  Thanks to Jorge_C.
* #1467: Exception on Python3 if nonexistent method is specified by automethod
* #1441: autosummary can't handle nested classes correctly.
* #1499: With non-callable ``setup`` in a conf.py, now sphinx-build emits
  a user-friendly error message.
* #1502: In autodoc, fix display of parameter defaults containing backslashes.
* #1226: autodoc, autosummary: importing setup.py by automodule will invoke
  setup process and execute ``sys.exit()``. Now sphinx avoids SystemExit
  exception and emits warnings without unexpected termination.
* #1503: py:function directive generate incorrectly signature when specifying
  a default parameter with an empty list ``[]``. Thanks to Geert Jansen.
* #1508: Non-ASCII filename raise exception on make singlehtml, latex, man,
  texinfo and changes.
* #1531: On Python3 environment, docutils.conf with 'source_link=true' in the
  general section cause type error.
* PR#270, #1533: Non-ASCII docstring cause UnicodeDecodeError when uses with
  inheritance-diagram directive. Thanks to WAKAYAMA shirou.
* PR#281, PR#282, #1509: TODO extension not compatible with websupport. Thanks
  to Takeshi Komiya.
* #1477: gettext does not extract nodes.line in a table or list.
* #1544: ``make text`` generates wrong table when it has empty table cells.
* #1522: Footnotes from table get displayed twice in LaTeX. This problem has
  been appeared from Sphinx-1.2.1 by #949.
* #508: Sphinx every time exit with zero when is invoked from setup.py command.
  ex. ``python setup.py build_sphinx -b doctest`` return zero even if doctest
  failed.

Release 1.2.2 (released Mar 2, 2014)
====================================

Bugs fixed
----------

* PR#211: When checking for existence of the `html_logo` file, check
  the full relative path and not the basename.
* PR#212: Fix traceback with autodoc and ``__init__`` methods without docstring.
* PR#213: Fix a missing import in the setup command.
* #1357: Option names documented by :rst:dir:`option` are now again allowed to
  not start with a dash or slash, and referencing them will work correctly.
* #1358: Fix handling of image paths outside of the source directory when using
  the "wildcard" style reference.
* #1374: Fix for autosummary generating overly-long summaries if first line
  doesn't end with a period.
* #1383: Fix Python 2.5 compatibility of sphinx-apidoc.
* #1391: Actually prevent using "pngmath" and "mathjax" extensions at the same
  time in sphinx-quickstart.
* #1386: Fix bug preventing more than one theme being added by the entry point
  mechanism.
* #1370: Ignore "toctree" nodes in text writer, instead of raising.
* #1364: Fix 'make gettext' fails when the '.. todolist::' directive is present.
* #1367: Fix a change of PR#96 that break sphinx.util.docfields.Field.make_field
  interface/behavior for ``item`` argument usage.

Documentation
-------------

* Extended the :ref:`documentation about building extensions <dev-extensions>`.


Release 1.2.1 (released Jan 19, 2014)
=====================================

Bugs fixed
----------

* #1335: Fix autosummary template overloading with exclamation prefix like
  ``{% extends "!autosummary/class.rst" %}`` cause infinite recursive function
  call. This was caused by PR#181.
* #1337: Fix autodoc with ``autoclass_content="both"`` uses useless
  ``object.__init__`` docstring when class does not have ``__init__``.
  This was caused by a change for #1138.
* #1340: Can't search alphabetical words on the HTML quick search generated
  with language='ja'.
* #1319: Do not crash if the `html_logo` file does not exist.
* #603: Do not use the HTML-ized title for building the search index (that
  resulted in "literal" being found on every page with a literal in the
  title).
* #751: Allow production lists longer than a page in LaTeX by using longtable.
* #764: Always look for stopwords lowercased in JS search.
* #814: autodoc: Guard against strange type objects that don't have
  ``__bases__``.
* #932: autodoc: Do not crash if ``__doc__`` is not a string.
* #933: Do not crash if an :rst:role:`option` value is malformed (contains
  spaces but no option name).
* #908: On Python 3, handle error messages from LaTeX correctly in the pngmath
  extension.
* #943: In autosummary, recognize "first sentences" to pull from the docstring
  if they contain uppercase letters.
* #923: Take the entire LaTeX document into account when caching
  pngmath-generated images.  This rebuilds them correctly when
  ``pngmath_latex_preamble`` changes.
* #901: Emit a warning when using docutils' new "math" markup without a Sphinx
  math extension active.
* #845: In code blocks, when the selected lexer fails, display line numbers
  nevertheless if configured.
* #929: Support parsed-literal blocks in LaTeX output correctly.
* #949: Update the tabulary.sty packed with Sphinx.
* #1050: Add anonymous labels into ``objects.inv`` to be referenced via
  :mod:`~sphinx.ext.intersphinx`.
* #1095: Fix print-media stylesheet being included always in the "scrolls"
  theme.
* #1085: Fix current classname not getting set if class description has
  ``:noindex:`` set.
* #1181: Report option errors in autodoc directives more gracefully.
* #1155: Fix autodocumenting C-defined methods as attributes in Python 3.
* #1233: Allow finding both Python classes and exceptions with the "class" and
  "exc" roles in intersphinx.
* #1198: Allow "image" for the "figwidth" option of the :dudir:`figure`
  directive as documented by docutils.
* #1152: Fix pycode parsing errors of Python 3 code by including two grammar
  versions for Python 2 and 3, and loading the appropriate version for the
  running Python version.
* #1017: Be helpful and tell the user when the argument to :rst:dir:`option`
  does not match the required format.
* #1345: Fix two bugs with `nitpick_ignore`; now you don't have to
  remove the store environment for changes to have effect.
* #1072: In the JS search, fix issues searching for upper-cased words by
  lowercasing words before stemming.
* #1299: Make behavior of the :rst:dir:`math` directive more consistent and
  avoid producing empty environments in LaTeX output.
* #1308: Strip HTML tags from the content of "raw" nodes before feeding it
  to the search indexer.
* #1249: Fix duplicate LaTeX page numbering for manual documents.
* #1292: In the linkchecker, retry HEAD requests when denied by HTTP 405.
  Also make the redirect code apparent and tweak the output a bit to be
  more obvious.
* #1285: Avoid name clashes between C domain objects and section titles.
* #848: Always take the newest code in incremental rebuilds with the
  :mod:`sphinx.ext.viewcode` extension.
* #979, #1266: Fix exclude handling in ``sphinx-apidoc``.
* #1302: Fix regression in :mod:`sphinx.ext.inheritance_diagram` when
  documenting classes that can't be pickled.
* #1316: Remove hard-coded ``font-face`` resources from epub theme.
* #1329: Fix traceback with empty translation msgstr in .po files.
* #1300: Fix references not working in translated documents in some instances.
* #1283: Fix a bug in the detection of changed files that would try to access
  doctrees of deleted documents.
* #1330: Fix `exclude_patterns` behavior with subdirectories in the
  `html_static_path`.
* #1323: Fix emitting empty ``<ul>`` tags in the HTML writer, which is not
  valid HTML.
* #1147: Don't emit a sidebar search box in the "singlehtml" builder.

Documentation
-------------

* #1325: Added a "Intersphinx" tutorial section. (:file:`doc/tutorial.rst`)


Release 1.2 (released Dec 10, 2013)
===================================

Features added
--------------

* Added ``sphinx.version_info`` tuple for programmatic checking of the Sphinx
  version.

Incompatible changes
--------------------

* Removed the ``sphinx.ext.refcounting`` extension -- it is very specific to
  CPython and has no place in the main distribution.

Bugs fixed
----------

* Restore ``versionmodified`` CSS class for versionadded/changed and deprecated
  directives.

* PR#181: Fix ``html_theme_path = ['.']`` is a trigger of rebuild all documents
  always (This change keeps the current "theme changes cause a rebuild"
  feature).

* #1296: Fix invalid charset in HTML help generated HTML files for default
  locale.

* PR#190: Fix gettext does not extract figure caption and rubric title inside
  other blocks. Thanks to Michael Schlenker.

* PR#176: Make sure setup_command test can always import Sphinx. Thanks to
  Dmitry Shachnev.

* #1311: Fix test_linkcode.test_html fails with C locale and Python 3.

* #1269: Fix ResourceWarnings with Python 3.2 or later.

* #1138: Fix: When ``autodoc_docstring_signature = True`` and
  ``autoclass_content = 'init'`` or ``'both'``, __init__ line should be
  removed from class documentation.


Release 1.2 beta3 (released Oct 3, 2013)
========================================

Features added
--------------

* The Sphinx error log files will now include a list of the loaded extensions
  for help in debugging.

Incompatible changes
--------------------

* PR#154: Remove "sphinx" prefix from LaTeX class name except 'sphinxmanual'
  and 'sphinxhowto'. Now you can use your custom document class without
  'sphinx' prefix. Thanks to Erik B.

Bugs fixed
----------

* #1265: Fix i18n: crash when translating a section name that is pointed to from
  a named target.
* A wrong condition broke the search feature on first page that is usually
  index.rst.  This issue was introduced in 1.2b1.
* #703: When Sphinx can't decode filenames with non-ASCII characters, Sphinx now
  catches UnicodeError and will continue if possible instead of raising the
  exception.


Release 1.2 beta2 (released Sep 17, 2013)
=========================================

Features added
--------------

* ``apidoc`` now ignores "_private" modules by default, and has an option ``-P``
  to include them.
* ``apidoc`` now has an option to not generate headings for packages and
  modules, for the case that the module docstring already includes a reST
  heading.
* PR#161: ``apidoc`` can now write each module to a standalone page instead of
  combining all modules in a package on one page.
* Builders: rebuild i18n target document when catalog updated.
* Support docutils.conf 'writers' and 'html4css1 writer' section in the HTML
  writer.  The latex, manpage and texinfo writers also support their respective
  'writers' sections.
* The new `html_extra_path` config value allows to specify directories
  with files that should be copied directly to the HTML output directory.
* Autodoc directives for module data and attributes now support an
  ``annotation`` option, so that the default display of the data/attribute
  value can be overridden.
* PR#136: Autodoc directives now support an ``imported-members`` option to
  include members imported from different modules.
* New locales: Macedonian, Sinhala, Indonesian.
* Theme package collection by using setuptools plugin mechanism.

Incompatible changes
--------------------

* PR#144, #1182: Force timezone offset to LocalTimeZone on POT-Creation-Date
  that was generated by gettext builder. Thanks to masklinn and Jakub Wilk.

Bugs fixed
----------

* PR#132: Updated jQuery version to 1.8.3.
* PR#141, #982: Avoid crash when writing PNG file using Python 3. Thanks to
  Marcin Wojdyr.
* PR#145: In parallel builds, sphinx drops second document file to write.
  Thanks to tychoish.
* PR#151: Some styling updates to tables in LaTeX.
* PR#153: The "extensions" config value can now be overridden.
* PR#155: Added support for some C++11 function qualifiers.
* Fix: 'make gettext' caused UnicodeDecodeError when templates contain utf-8
  encoded strings.
* #828: use inspect.getfullargspec() to be able to document functions with
  keyword-only arguments on Python 3.
* #1090: Fix i18n: multiple cross references (term, ref, doc) in the same line
  return the same link.
* #1157: Combination of 'globaltoc.html' and hidden toctree caused exception.
* #1159: fix wrong generation of objects inventory for Python modules, and
  add a workaround in intersphinx to fix handling of affected inventories.
* #1160: Citation target missing caused an AssertionError.
* #1162, PR#139: singlehtml builder didn't copy images to _images/.
* #1173: Adjust setup.py dependencies because Jinja2 2.7 discontinued
  compatibility with Python < 3.3 and Python < 2.6.  Thanks to Alexander Dupuy.
* #1185: Don't crash when a Python module has a wrong or no encoding declared,
  and non-ASCII characters are included.
* #1188: sphinx-quickstart raises UnicodeEncodeError if "Project version"
  includes non-ASCII characters.
* #1189: "Title underline is too short" WARNING is given when using fullwidth
  characters to "Project name" on quickstart.
* #1190: Output TeX/texinfo/man filename has no basename (only extension)
  when using non-ASCII characters in the "Project name" on quickstart.
* #1192: Fix escaping problem for hyperlinks in the manpage writer.
* #1193: Fix i18n: multiple link references in the same line return the same
  link.
* #1176: Fix i18n: footnote reference number missing for auto numbered named
  footnote and auto symbol footnote.
* PR#146,#1172: Fix ZeroDivisionError in parallel builds. Thanks to tychoish.
* #1204: Fix wrong generation of links to local intersphinx targets.
* #1206: Fix i18n: gettext did not translate admonition directive's title.
* #1232: Sphinx generated broken ePub files on Windows.
* #1259: Guard the debug output call when emitting events; to prevent the
  repr() implementation of arbitrary objects causing build failures.
* #1142: Fix NFC/NFD normalizing problem of rst filename on Mac OS X.
* #1234: Ignoring the string consists only of white-space characters.


Release 1.2 beta1 (released Mar 31, 2013)
=========================================

Incompatible changes
--------------------

* Removed ``sphinx.util.compat.directive_dwim()`` and
  ``sphinx.roles.xfileref_role()`` which were deprecated since version 1.0.
* PR#122: the files given in `latex_additional_files` now override TeX
  files included by Sphinx, such as ``sphinx.sty``.
* PR#124: the node generated by `versionadded`,
  `versionchanged` and `deprecated` directives now includes
  all added markup (such as "New in version X") as child nodes, and no
  additional text must be generated by writers.
* PR#99: the :rst:dir:`seealso` directive now generates admonition nodes instead
  of the custom ``seealso`` node.

Features added
--------------

* Markup

  - The :rst:dir:`toctree` directive and the ``toctree()`` template function now
    have an ``includehidden`` option that includes hidden toctree entries (bugs
    #790 and #1047).  A bug in the ``maxdepth`` option for the ``toctree()``
    template function has been fixed (bug #1046).
  - PR#99: Strip down seealso directives to normal admonitions.  This removes
    their unusual CSS classes (admonition-see-also), inconsistent LaTeX
    admonition title ("See Also" instead of "See also"), and spurious
    indentation in the text builder.

* HTML builder

  - #783: Create a link to full size image if it is scaled with width or height.
  - #1067: Improve the ordering of the JavaScript search results: matches in
    titles come before matches in full text, and object results are better
    categorized.  Also implement a pluggable search scorer.
  - #1053: The "rightsidebar" and "collapsiblesidebar" HTML theme options now
    work together.
  - Update to jQuery 1.7.1 and Underscore.js 1.3.1.

* Texinfo builder

  - An "Index" node is no longer added when there are no entries.
  - "deffn" categories are no longer capitalized if they contain capital
    letters.
  - ``desc_annotation`` nodes are now rendered.
  - ``strong`` and ``emphasis`` nodes are now formatted like
    ``literal``\s. The reason for this is because the standard Texinfo markup
    (``*strong*`` and ``_emphasis_``) resulted in confusing output due to the
    common usage of using these constructs for documenting parameter names.
  - Field lists formatting has been tweaked to better display
    "Info field lists".
  - ``system_message`` and ``problematic`` nodes are now formatted in a similar
    fashion as done by the text builder.
  - "en-dash" and "em-dash" conversion of hyphens is no longer performed in
    option directive signatures.
  - ``@ref`` is now used instead of ``@pxref`` for cross-references which
    prevents the word "see" from being added before the link (does not affect
    the Info output).
  - The ``@finalout`` command has been added for better TeX output.
  - ``transition`` nodes are now formatted using underscores ("_") instead of
    asterisks ("*").
  - The default value for the ``paragraphindent`` has been changed from 2 to 0
    meaning that paragraphs are no longer indented by default.
  - #1110: A new configuration value `texinfo_no_detailmenu` has been
    added for controlling whether a ``@detailmenu`` is added in the "Top"
    node's menu.
  - Detailed menus are no longer created except for the "Top" node.
  - Fixed an issue where duplicate domain indices would result in invalid
    output.

* LaTeX builder:

  - PR#115: Add ``'transition'`` item in `latex_elements` for
    customizing how transitions are displayed. Thanks to Jeff Klukas.
  - PR#114: The LaTeX writer now includes the "cmap" package by default. The
    ``'cmappkg'`` item in `latex_elements` can be used to control this.
    Thanks to Dmitry Shachnev.
  - The ``'fontpkg'`` item in `latex_elements` now defaults to ``''``
    when the :confval:`language` uses the Cyrillic script.  Suggested by Dmitry
    Shachnev.
  - The `latex_documents`, `texinfo_documents`, and
    `man_pages` configuration values will be set to default values based
    on the :confval:`master_doc` if not explicitly set in :file:`conf.py`.
    Previously, if these values were not set, no output would be generated by
    their respective builders.

* Internationalization:

  - Add i18n capabilities for custom templates.  For example: The Sphinx
    reference documentation in doc directory provides a ``sphinx.pot`` file with
    message strings from ``doc/_templates/*.html`` when using ``make gettext``.

  - PR#61,#703: Add support for non-ASCII filename handling.

* Other builders:

  - Added the Docutils-native XML and pseudo-XML builders.  See
    :class:`XMLBuilder` and :class:`PseudoXMLBuilder`.
  - PR#45: The linkcheck builder now checks ``#anchor``\ s for existence.
  - PR#123, #1106: Add `epub_use_index` configuration value.  If
    provided, it will be used instead of `html_use_index` for epub
    builder.
  - PR#126: Add `epub_tocscope` configuration value. The setting
    controls the generation of the epub toc. The user can now also include
    hidden toc entries.
  - PR#112: Add `epub_show_urls` configuration value.

* Extensions:

  - PR#52: ``special_members`` flag to autodoc now behaves like ``members``.
  - PR#47: Added :mod:`sphinx.ext.linkcode` extension.
  - PR#25: In inheritance diagrams, the first line of the class docstring
    is now the tooltip for the class.

* Command-line interfaces:

  - PR#75: Added ``--follow-links`` option to sphinx-apidoc.
  - #869: sphinx-build now has the option ``-T`` for printing the full
    traceback after an unhandled exception.
  - sphinx-build now supports the standard ``--help`` and ``--version`` options.
  - sphinx-build now provides more specific error messages when called with
    invalid options or arguments.
  - sphinx-build now has a verbose option ``-v`` which can be repeated for
    greater effect.  A single occurrence provides a slightly more verbose output
    than normal.  Two or more occurrences of this option provides more detailed
    output which may be useful for debugging.

* Locales:

  - PR#74: Fix some Russian translation.
  - PR#54: Added Norwegian bokmaal translation.
  - PR#35: Added Slovak translation.
  - PR#28: Added Hungarian translation.
  - #1113: Add Hebrew locale.
  - #1097: Add Basque locale.
  - #1037: Fix typos in Polish translation. Thanks to Jakub Wilk.
  - #1012: Update Estonian translation.

* Optimizations:

  - Speed up building the search index by caching the results of the word
    stemming routines.  Saves about 20 seconds when building the Python
    documentation.
  - PR#108: Add experimental support for parallel building with a new
    :option:`sphinx-build -j` option.

Documentation
-------------

* PR#88: Added the "Sphinx Developer's Guide" (:file:`doc/devguide.rst`)
  which outlines the basic development process of the Sphinx project.
* Added a detailed "Installing Sphinx" document (:file:`doc/install.rst`).

Bugs fixed
----------

* PR#124: Fix paragraphs in versionmodified are ignored when it has no
  dangling paragraphs.  Fix wrong html output (nested ``<p>`` tag).  Fix
  versionmodified is not translatable.  Thanks to Nozomu Kaneko.
* PR#111: Respect add_autodoc_attrgetter() even when inherited-members is set.
  Thanks to A. Jesse Jiryu Davis.
* PR#97: Fix footnote handling in translated documents.
* Fix text writer not handling visit_legend for figure directive contents.
* Fix text builder not respecting wide/fullwidth characters: title underline
  width, table layout width and text wrap width.
* Fix leading space in LaTeX table header cells.
* #1132: Fix LaTeX table output for multi-row cells in the first column.
* #1128: Fix Unicode errors when trying to format time strings with a
  non-standard locale.
* #1127: Fix traceback when autodoc tries to tokenize a non-Python file.
* #1126: Fix double-hyphen to en-dash conversion in wrong places such as
  command-line option names in LaTeX.
* #1123: Allow whitespaces in filenames given to `literalinclude`.
* #1120: Added improvements about i18n for themes "basic", "haiku" and
  "scrolls" that Sphinx built-in. Thanks to Leonardo J. Caballero G.
* #1118: Updated Spanish translation. Thanks to Leonardo J. Caballero G.
* #1117: Handle .pyx files in sphinx-apidoc.
* #1112: Avoid duplicate download files when referenced from documents in
  different ways (absolute/relative).
* #1111: Fix failure to find uppercase words in search when
  `html_search_language` is 'ja'. Thanks to Tomo Saito.
* #1108: The text writer now correctly numbers enumerated lists with
  non-default start values (based on patch by Ewan Edwards).
* #1102: Support multi-context "with" statements in autodoc.
* #1090: Fix gettext not extracting glossary terms.
* #1074: Add environment version info to the generated search index to avoid
  compatibility issues with old builds.
* #1070: Avoid un-pickling issues when running Python 3 and the saved
  environment was created under Python 2.
* #1069: Fixed error caused when autodoc would try to format signatures of
  "partial" functions without keyword arguments (patch by Artur Gaspar).
* #1062: sphinx.ext.autodoc use __init__ method signature for class signature.
* #1055: Fix web support with relative path to source directory.
* #1043: Fix sphinx-quickstart asking again for yes/no questions because
  ``input()`` returns values with an extra '\r' on Python 3.2.0 +
  Windows. Thanks to Régis Décamps.
* #1041: Fix failure of the cpp domain parser to parse a const type with a
  modifier.
* #1038: Fix failure of the cpp domain parser to parse C+11 "static constexpr"
  declarations.  Thanks to Jakub Wilk.
* #1029: Fix intersphinx_mapping values not being stable if the mapping has
  plural key/value set with Python 3.3.
* #1028: Fix line block output in the text builder.
* #1024: Improve Makefile/make.bat error message if Sphinx is not found. Thanks
  to Anatoly Techtonik.
* #1018: Fix "container" directive handling in the text builder.
* #1015: Stop overriding jQuery contains() in the JavaScript.
* #1010: Make pngmath images transparent by default; IE7+ should handle it.
* #1008: Fix test failures with Python 3.3.
* #995: Fix table-of-contents and page numbering for the LaTeX "howto" class.
* #976: Fix gettext does not extract index entries.
* PR#72: #975: Fix gettext not extracting definition terms before docutils 0.10.
* #961: Fix LaTeX output for triple quotes in code snippets.
* #958: Do not preserve ``environment.pickle`` after a failed build.
* #955: Fix i18n transformation.
* #940: Fix gettext does not extract figure caption.
* #920: Fix PIL packaging issue that allowed to import ``Image`` without PIL
  namespace.  Thanks to Marc Schlaich.
* #723: Fix the search function on local files in WebKit based browsers.
* #440: Fix coarse timestamp resolution in some filesystem generating a wrong
  list of outdated files.


Release 1.1.3 (Mar 10, 2012)
============================

* PR#40: Fix ``safe_repr`` function to decode bytestrings with non-ASCII
  characters correctly.

* PR#37: Allow configuring sphinx-apidoc via ``SPHINX_APIDOC_OPTIONS``.

* PR#34: Restore Python 2.4 compatibility.

* PR#36: Make the "bibliography to TOC" fix in LaTeX output specific to
  the document class.

* #695: When the highlight language "python" is specified explicitly,
  do not try to parse the code to recognize non-Python snippets.

* #859: Fix exception under certain circumstances when not finding
  appropriate objects to link to.

* #860: Do not crash when encountering invalid doctest examples, just
  emit a warning.

* #864: Fix crash with some settings of `modindex_common_prefix`.

* #862: Fix handling of ``-D`` and ``-A`` options on Python 3.

* #851: Recognize and warn about circular toctrees, instead of running
  into recursion errors.

* #853: Restore compatibility with docutils trunk.

* #852: Fix HtmlHelp index entry links again.

* #854: Fix inheritance_diagram raising attribute errors on builtins.

* #832: Fix crashes when putting comments or lone terms in a glossary.

* #834, #818: Fix HTML help language/encoding mapping for all Sphinx
  supported languages.

* #844: Fix crashes when dealing with Unicode output in doctest extension.

* #831: Provide ``--project`` flag in setup_command as advertised.

* #875: Fix reading config files under Python 3.

* #876: Fix quickstart test under Python 3.

* #870: Fix spurious KeyErrors when removing documents.

* #892: Fix single-HTML builder misbehaving with the master document in a
  subdirectory.

* #873: Fix assertion errors with empty ``only`` directives.

* #816: Fix encoding issues in the Qt help builder.


Release 1.1.2 (Nov 1, 2011) -- 1.1.1 is a silly version number anyway!
======================================================================

* #809: Include custom fixers in the source distribution.


Release 1.1.1 (Nov 1, 2011)
===========================

* #791: Fix QtHelp, DevHelp and HtmlHelp index entry links.

* #792: Include "sphinx-apidoc" in the source distribution.

* #797: Don't crash on a misformatted glossary.

* #801: Make intersphinx work properly without SSL support.

* #805: Make the ``Sphinx.add_index_to_domain`` method work correctly.

* #780: Fix Python 2.5 compatibility.


Release 1.1 (Oct 9, 2011)
=========================

Incompatible changes
--------------------

* The `py:module` directive doesn't output its ``platform`` option
  value anymore.  (It was the only thing that the directive did output, and
  therefore quite inconsistent.)

* Removed support for old dependency versions; requirements are now:

  - Pygments >= 1.2
  - Docutils >= 0.7
  - Jinja2   >= 2.3

Features added
--------------

* Added Python 3.x support.

* New builders and subsystems:

  - Added a Texinfo builder.
  - Added i18n support for content, a ``gettext`` builder and related
    utilities.
  - Added the ``websupport`` library and builder.
  - #98: Added a ``sphinx-apidoc`` script that autogenerates a hierarchy
    of source files containing autodoc directives to document modules
    and packages.
  - #273: Add an API for adding full-text search support for languages
    other than English.  Add support for Japanese.

* Markup:

  - #138: Added an :rst:role:`index` role, to make inline index entries.
  - #454: Added more index markup capabilities: marking see/seealso entries,
    and main entries for a given key.
  - #460: Allowed limiting the depth of section numbers for HTML using the
    :rst:dir:`toctree`\'s ``numbered`` option.
  - #586: Implemented improved :rst:dir:`glossary` markup which allows
    multiple terms per definition.
  - #478: Added `py:decorator` directive to describe decorators.
  - C++ domain now supports array definitions.
  - C++ domain now supports doc fields (``:param x:`` inside directives).
  - Section headings in :rst:dir:`only` directives are now correctly
    handled.
  - Added ``emphasize-lines`` option to source code directives.
  - #678: C++ domain now supports superclasses.

* HTML builder:

  - Added ``pyramid`` theme.
  - #559: `html_add_permalinks` is now a string giving the
    text to display in permalinks.
  - #259: HTML table rows now have even/odd CSS classes to enable
    "Zebra styling".
  - #554: Add theme option ``sidebarwidth`` to the basic theme.

* Other builders:

  - #516: Added new value of the `latex_show_urls` option to
    show the URLs in footnotes.
  - #209: Added `text_newlines` and `text_sectionchars`
    config values.
  - Added `man_show_urls` config value.
  - #472: linkcheck builder: Check links in parallel, use HTTP HEAD
    requests and allow configuring the timeout.  New config values:
    `linkcheck_timeout` and `linkcheck_workers`.
  - #521: Added `linkcheck_ignore` config value.
  - #28: Support row/colspans in tables in the LaTeX builder.

* Configuration and extensibility:

  - #537: Added `nitpick_ignore`.
  - #306: Added :event:`env-get-outdated` event.
  - :meth:`.Application.add_stylesheet` now accepts full URIs.

* Autodoc:

  - #564: Add `autodoc_docstring_signature`.  When enabled (the
    default), autodoc retrieves the signature from the first line of the
    docstring, if it is found there.
  - #176: Provide ``private-members`` option for autodoc directives.
  - #520: Provide ``special-members`` option for autodoc directives.
  - #431: Doc comments for attributes can now be given on the same line
    as the assignment.
  - #437: autodoc now shows values of class data attributes.
  - autodoc now supports documenting the signatures of
    ``functools.partial`` objects.

* Other extensions:

  - Added the :mod:`sphinx.ext.mathjax` extension.
  - #443: Allow referencing external graphviz files.
  - Added ``inline`` option to graphviz directives, and fixed the
    default (block-style) in LaTeX output.
  - #590: Added ``caption`` option to graphviz directives.
  - #553: Added `testcleanup` blocks in the doctest extension.
  - #594: `trim_doctest_flags` now also removes ``<BLANKLINE>``
    indicators.
  - #367: Added automatic exclusion of hidden members in inheritance
    diagrams, and an option to selectively enable it.
  - Added ``pngmath_add_tooltips``.
  - The math extension displaymath directives now support ``name`` in
    addition to ``label`` for giving the equation label, for compatibility
    with Docutils.

* New locales:

  - #221: Added Swedish locale.
  - #526: Added Iranian locale.
  - #694: Added Latvian locale.
  - Added Nepali locale.
  - #714: Added Korean locale.
  - #766: Added Estonian locale.

* Bugs fixed:

  - #778: Fix "hide search matches" link on pages linked by search.
  - Fix the source positions referenced by the "viewcode" extension.


Release 1.0.8 (Sep 23, 2011)
============================

* #627: Fix tracebacks for AttributeErrors in autosummary generation.

* Fix the ``abbr`` role when the abbreviation has newlines in it.

* #727: Fix the links to search results with custom object types.

* #648: Fix line numbers reported in warnings about undefined
  references.

* #696, #666: Fix C++ array definitions and template arguments
  that are not type names.

* #633: Allow footnotes in section headers in LaTeX output.

* #616: Allow keywords to be linked via intersphinx.

* #613: Allow Unicode characters in production list token names.

* #720: Add dummy visitors for graphviz nodes for text and man.

* #704: Fix image file duplication bug.

* #677: Fix parsing of multiple signatures in C++ domain.

* #637: Ignore Emacs lock files when looking for source files.

* #544: Allow .pyw extension for importable modules in autodoc.

* #700: Use ``$(MAKE)`` in quickstart-generated Makefiles.

* #734: Make sidebar search box width consistent in browsers.

* #644: Fix spacing of centered figures in HTML output.

* #767: Safely encode SphinxError messages when printing them to
  sys.stderr.

* #611: Fix LaTeX output error with a document with no sections but
  a link target.

* Correctly treat built-in method descriptors as methods in autodoc.

* #706: Stop monkeypatching the Python textwrap module.

* #657: viewcode now works correctly with source files that have
  non-ASCII encoding.

* #669: Respect the ``noindex`` flag option in py:module directives.

* #675: Fix IndexErrors when including nonexisting lines with
  `literalinclude`.

* #676: Respect custom function/method parameter separator strings.

* #682: Fix JS incompatibility with jQuery >= 1.5.

* #693: Fix double encoding done when writing HTMLHelp .hhk files.

* #647: Do not apply SmartyPants in parsed-literal blocks.

* C++ domain now supports array definitions.


Release 1.0.7 (Jan 15, 2011)
============================

* #347: Fix wrong generation of directives of static methods in
  autosummary.

* #599: Import PIL as ``from PIL import Image``.

* #558: Fix longtables with captions in LaTeX output.

* Make token references work as hyperlinks again in LaTeX output.

* #572: Show warnings by default when reference labels cannot be
  found.

* #536: Include line number when complaining about missing reference
  targets in nitpicky mode.

* #590: Fix inline display of graphviz diagrams in LaTeX output.

* #589: Build using app.build() in setup command.

* Fix a bug in the inheritance diagram exception that caused base
  classes to be skipped if one of them is a builtin.

* Fix general index links for C++ domain objects.

* #332: Make admonition boundaries in LaTeX output visible.

* #573: Fix KeyErrors occurring on rebuild after removing a file.

* Fix a traceback when removing files with globbed toctrees.

* If an autodoc object cannot be imported, always re-read the
  document containing the directive on next build.

* If an autodoc object cannot be imported, show the full traceback
  of the import error.

* Fix a bug where the removal of download files and images wasn't
  noticed.

* #571: Implement ``~`` cross-reference prefix for the C domain.

* Fix regression of LaTeX output with the fix of #556.

* #568: Fix lookup of class attribute documentation on descriptors
  so that comment documentation now works.

* Fix traceback with ``only`` directives preceded by targets.

* Fix tracebacks occurring for duplicate C++ domain objects.

* Fix JavaScript domain links to objects with ``$`` in their name.


Release 1.0.6 (Jan 04, 2011)
============================

* #581: Fix traceback in Python domain for empty cross-reference
  targets.

* #283: Fix literal block display issues on Chrome browsers.

* #383, #148: Support sorting a limited range of accented characters
  in the general index and the glossary.

* #570: Try decoding ``-D`` and ``-A`` command-line arguments with
  the locale's preferred encoding.

* #528: Observe `locale_dirs` when looking for the JS
  translations file.

* #574: Add special code for better support of Japanese documents
  in the LaTeX builder.

* Regression of #77: If there is only one parameter given with
  ``:param:`` markup, the bullet list is now suppressed again.

* #556: Fix missing paragraph breaks in LaTeX output in certain
  situations.

* #567: Emit the ``autodoc-process-docstring`` event even for objects
  without a docstring so that it can add content.

* #565: In the LaTeX builder, not only literal blocks require different
  table handling, but also quite a few other list-like block elements.

* #515: Fix tracebacks in the viewcode extension for Python objects
  that do not have a valid signature.

* Fix strange reports of line numbers for warnings generated from
  autodoc-included docstrings, due to different behavior depending
  on docutils version.

* Several fixes to the C++ domain.


Release 1.0.5 (Nov 12, 2010)
============================

* #557: Add CSS styles required by docutils 0.7 for aligned images
  and figures.

* In the Makefile generated by LaTeX output, do not delete pdf files
  on clean; they might be required images.

* #535: Fix LaTeX output generated for line blocks.

* #544: Allow ``.pyw`` as a source file extension.


Release 1.0.4 (Sep 17, 2010)
============================

* #524: Open intersphinx inventories in binary mode on Windows,
  since version 2 contains zlib-compressed data.

* #513: Allow giving non-local URIs for JavaScript files, e.g.
  in the JSMath extension.

* #512: Fix traceback when ``intersphinx_mapping`` is empty.


Release 1.0.3 (Aug 23, 2010)
============================

* #495: Fix internal vs. external link distinction for links coming
  from a docutils table-of-contents.

* #494: Fix the ``maxdepth`` option for the ``toctree()`` template
  callable when used with ``collapse=True``.

* #507: Fix crash parsing Python argument lists containing brackets
  in string literals.

* #501: Fix regression when building LaTeX docs with figures that
  don't have captions.

* #510: Fix inheritance diagrams for classes that are not picklable.

* #497: Introduce separate background color for the sidebar collapse
  button, making it easier to see.

* #502, #503, #496: Fix small layout bugs in several builtin themes.


Release 1.0.2 (Aug 14, 2010)
============================

* #490: Fix cross-references to objects of types added by the
  :func:`~.Sphinx.add_object_type` API function.

* Fix handling of doc field types for different directive types.

* Allow breaking long signatures, continuing with backlash-escaped
  newlines.

* Fix unwanted styling of C domain references (because of a namespace
  clash with Pygments styles).

* Allow references to PEPs and RFCs with explicit anchors.

* #471: Fix LaTeX references to figures.

* #482: When doing a non-exact search, match only the given type
  of object.

* #481: Apply non-exact search for Python reference targets with
  ``.name`` for modules too.

* #484: Fix crash when duplicating a parameter in an info field list.

* #487: Fix setting the default role to one provided by the
  ``oldcmarkup`` extension.

* #488: Fix crash when json-py is installed, which provides a
  ``json`` module but is incompatible to simplejson.

* #480: Fix handling of target naming in intersphinx.

* #486: Fix removal of ``!`` for all cross-reference roles.


Release 1.0.1 (Jul 27, 2010)
============================

* #470: Fix generated target names for reST domain objects; they
  are not in the same namespace.

* #266: Add Bengali language.

* #473: Fix a bug in parsing JavaScript object names.

* #474: Fix building with SingleHTMLBuilder when there is no toctree.

* Fix display names for objects linked to by intersphinx with
  explicit targets.

* Fix building with the JSON builder.

* Fix hyperrefs in object descriptions for LaTeX.


Release 1.0 (Jul 23, 2010)
==========================

Incompatible changes
--------------------

* Support for domains has been added.  A domain is a collection of
  directives and roles that all describe objects belonging together,
  e.g. elements of a programming language.  A few builtin domains are
  provided:

  - Python
  - C
  - C++
  - JavaScript
  - reStructuredText

* The old markup for defining and linking to C directives is now
  deprecated.  It will not work anymore in future versions without
  activating the :mod:`~sphinx.ext.oldcmarkup` extension; in Sphinx
  1.0, it is activated by default.

* Removed support for old dependency versions; requirements are now:

  - docutils >= 0.5
  - Jinja2   >= 2.2

* Removed deprecated elements:

  - ``exclude_dirs`` config value
  - ``sphinx.builder`` module

Features added
--------------

* General:

  - Added a "nitpicky" mode that emits warnings for all missing
    references.  It is activated by the :option:`sphinx-build -n` command-line
    switch or the :confval:`nitpicky` config value.
  - Added ``latexpdf`` target in quickstart Makefile.

* Markup:

  - The `menuselection` and `guilabel` roles now
    support ampersand accelerators.
  - New more compact doc field syntax is now recognized: ``:param type
    name: description``.
  - Added ``tab-width`` option to `literalinclude` directive.
  - Added ``titlesonly`` option to :rst:dir:`toctree` directive.
  - Added the ``prepend`` and ``append`` options to the
    `literalinclude` directive.
  - #284: All docinfo metadata is now put into the document metadata, not
    just the author.
  - The `ref` role can now also reference tables by caption.
  - The :dudir:`include` directive now supports absolute paths, which
    are interpreted as relative to the source directory.
  - In the Python domain, references like ``:func:`.name``` now look for
    matching names with any prefix if no direct match is found.

* Configuration:

  - Added `rst_prolog` config value.
  - Added `html_secnumber_suffix` config value to control
    section numbering format.
  - Added `html_compact_lists` config value to control
    docutils' compact lists feature.
  - The `html_sidebars` config value can now contain patterns
    as keys, and the values can be lists that explicitly select which
    sidebar templates should be rendered.  That means that the builtin
    sidebar contents can be included only selectively.
  - `html_static_path` can now contain single file entries.
  - The new universal config value `exclude_patterns` makes the
    old ``unused_docs``, ``exclude_trees`` and
    ``exclude_dirnames`` obsolete.
  - Added `html_output_encoding` config value.
  - Added the `latex_docclass` config value and made the
    "twoside" documentclass option overridable by "oneside".
  - Added the `trim_doctest_flags` config value, which is true
    by default.
  - Added `html_show_copyright` config value.
  - Added `latex_show_pagerefs` and `latex_show_urls`
    config values.
  - The behavior of `html_file_suffix` changed slightly: the
    empty string now means "no suffix" instead of "default suffix", use
    ``None`` for "default suffix".

* New builders:

  - Added a builder for the Epub format.
  - Added a builder for manual pages.
  - Added a single-file HTML builder.

* HTML output:

  - Inline roles now get a CSS class with their name, allowing styles to
    customize their appearance.  Domain-specific roles get two classes,
    ``domain`` and ``domain-rolename``.
  - References now get the class ``internal`` if they are internal to
    the whole project, as opposed to internal to the current page.
  - External references can be styled differently with the new
    ``externalrefs`` theme option for the default theme.
  - In the default theme, the sidebar can experimentally now be made
    collapsible using the new ``collapsiblesidebar`` theme option.
  - #129: Toctrees are now wrapped in a ``div`` tag with class
    ``toctree-wrapper`` in HTML output.
  - The :data:`toctree` callable in templates now has a ``maxdepth``
    keyword argument to control the depth of the generated tree.
  - The :data:`toctree` callable in templates now accepts a
    ``titles_only`` keyword argument.
  - Added ``htmltitle`` block in layout template.
  - In the JavaScript search, allow searching for object names including
    the module name, like ``sys.argv``.
  - Added new theme ``haiku``, inspired by the Haiku OS user guide.
  - Added new theme ``nature``.
  - Added new theme ``agogo``, created by Andi Albrecht.
  - Added new theme ``scrolls``, created by Armin Ronacher.
  - #193: Added a ``visitedlinkcolor`` theme option to the default
    theme.
  - #322: Improved responsiveness of the search page by loading the
    search index asynchronously.

* Extension API:

  - Added :event:`html-collect-pages`.
  - Added `needs_sphinx` config value and
    :meth:`~sphinx.application.Sphinx.require_sphinx` application API
    method.
  - #200: Added :meth:`~sphinx.application.Sphinx.add_stylesheet`
    application API method.

* Extensions:

  - Added the :mod:`~sphinx.ext.viewcode` extension.
  - Added the :mod:`~sphinx.ext.extlinks` extension.
  - Added support for source ordering of members in autodoc, with
    ``autodoc_member_order = 'bysource'``.
  - Added `autodoc_default_flags` config value, which can be
    used to select default flags for all autodoc directives.
  - Added a way for intersphinx to refer to named labels in other
    projects, and to specify the project you want to link to.
  - #280: Autodoc can now document instance attributes assigned in
    ``__init__`` methods.
  - Many improvements and fixes to the :mod:`~sphinx.ext.autosummary`
    extension, thanks to Pauli Virtanen.
  - #309: The :mod:`~sphinx.ext.graphviz` extension can now output SVG
    instead of PNG images, controlled by the
    `graphviz_output_format` config value.
  - Added ``alt`` option to :rst:dir:`graphviz` extension directives.
  - Added ``exclude`` argument to :func:`.autodoc.between`.

* Translations:

  - Added Croatian translation, thanks to Bojan Mihelač.
  - Added Turkish translation, thanks to Firat Ozgul.
  - Added Catalan translation, thanks to Pau Fernández.
  - Added simplified Chinese translation.
  - Added Danish translation, thanks to Hjorth Larsen.
  - Added Lithuanian translation, thanks to Dalius Dobravolskas.

* Bugs fixed:

  - #445: Fix links to result pages when using the search function
    of HTML built with the ``dirhtml`` builder.
  - #444: In templates, properly re-escape values treated with the
    "striptags" Jinja filter.


Previous versions
=================

The changelog for versions before 1.0 can be found in the file ``CHANGES.old``
in the source distribution or `at GitHub
<https://github.com/sphinx-doc/sphinx/raw/master/CHANGES.old>`__.
