from pathlib import Path

from html import escape
from docutils import nodes

import nbformat
from myst_sphinx_gallery.directives import RefGalleryDirective


class MetadataRefGallery(RefGalleryDirective):
    def create_cards_for_row_node(self, entry_files, row_node, save_thumbnail):
        for entry_file in entry_files:
            entry_file = Path(entry_file)
            self.env.note_dependency(str(entry_file))

            # Let the existing directive build one complete card.
            super().create_cards_for_row_node(
                [entry_file], row_node, save_thumbnail
            )

            if entry_file.suffix != ".ipynb":
                continue

            nb = nbformat.read(entry_file, as_version=4)
            tooltip = nb.metadata.get("gallery", {}).get("tooltip", "")
            if not isinstance(tooltip, str):
                raise TypeError(
                    f"{entry_file}: gallery.tooltip must be a string"
                )

            card = row_node.children[-1]
            card["tooltip"] = tooltip.strip()

            # An empty attribute alone still activates the tooltip CSS.
            if not card["tooltip"]:
                card["classes"] = [
                    c for c in card["classes"] if c != "msg-tooltip"
                ]

        return row_node



class NotebookTitle(nodes.title):
    pass


def add_download(app, doctree, docname):
    if app.builder.format != "html":
        return

    url = app.env.metadata.get(docname, {}).get("download_url")
    if not url:
        return

    title = next(
        (node for node in doctree.findall(nodes.title)
         if isinstance(node.parent, nodes.section)),
        None,
    )
    if title is None:
        return

    replacement = NotebookTitle(title.rawsource, "", **title.attributes)
    replacement.extend(title.children)
    replacement["download_url"] = url
    title.replace_self(replacement)


def visit_notebook_title(self, node):
    self.body.append('<div class="notebook-heading">')
    self.visit_title(node)


def depart_notebook_title(self, node):
    self.depart_title(node)
    url = escape(node["download_url"], quote=True)
    self.body.append(
        f'<a class="notebook-download" href="{url}">'
        'Download notebook</a></div>'
    )

def setup(app):
    app.add_node(
        NotebookTitle,
        html=(visit_notebook_title, depart_notebook_title),
    )
    app.connect("doctree-resolved", add_download)

    app.setup_extension("myst_sphinx_gallery")
    app.add_directive("ref-gallery", MetadataRefGallery, override=True)
    return {"version": "1", "parallel_read_safe": False}
