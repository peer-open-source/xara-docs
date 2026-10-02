"""Link bare ``*`` separators in Python signatures to the signature guide.

Sphinx recognizes keyword-only separators when it can parse a signature as a
Python parameter list.  Some documented calls use a literal selector (such as
``Model.element("ForceFrame", ...)``), which makes Sphinx fall back to a plain
argument list.  Decorate both forms after parsing so they render consistently.
"""

from docutils import nodes
from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.locale import _


_GUIDE_DOCNAME = "user/guides/signatures"


def _link_keyword_only_separators(
    app: Sphinx, 
    doctree: nodes.document, 
    docname: str
) -> None:
    if app.builder.format != "html":
        return

    guide_uri = app.builder.get_relative_uri(docname, _GUIDE_DOCNAME)

    for description in doctree.findall(addnodes.desc):
        if description.get("domain") != "py":
            continue

        for signature in description.children:
            if not isinstance(signature, addnodes.desc_signature):
                continue

            for parameter in signature.findall(addnodes.desc_parameter):
                if parameter.astext() != "*":
                    continue

                tooltip = _("Arguments that follow must be supplied in keyword form; click for help")
                abbreviation = nodes.abbreviation(
                    "*", "*", explanation=tooltip
                )
                operator = addnodes.desc_sig_operator(
                    "*", "", abbreviation, classes=["keyword-only-separator"]
                )
                link = nodes.reference(
                    "", "", operator, refuri=guide_uri, internal=True
                )

                parameter.clear()
                parameter += link


def setup(app: Sphinx) -> dict[str, bool]:
    app.connect("doctree-resolved", _link_keyword_only_separators)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
