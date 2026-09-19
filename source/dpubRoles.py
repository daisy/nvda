# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2026 NV Access Limited, DAISY Consortium, Noelia Ruiz Martínez
# This file may be used under the terms of the GNU General Public License, version 2 or later, as modified by the NVDA license.
# For full terms and any additional permissions, see the NVDA license file: https://github.com/nvaccess/nvda/blob/master/copying.txt

from dataclasses import dataclass

from config.configFlags import DpubRolesLevel


@dataclass
class DpubRole:
	name: str
	output: str
	priority: DpubRolesLevel
	landmark: bool

	def __str__(self):
		return f"{self.name} ({self.output}, priority {self.priority})"

	def __repr__(self):
		return f"DpubRole(name={self.name}, output={self.output}, priority={self.priority})"


dpubRoles: dict[str, DpubRole] = {
	"doc-abstract": DpubRole(
		name="doc-abstract",
		# Translators: The output for a dpub role, used to identify the abstract of a document.
		output=pgettext("aria", "abstract"),
		priority=DpubRolesLevel.SOME,
		landmark=True,
	),
	"doc-acknowledgments": DpubRole(
		name="doc-acknowledgments",
		# Translators: The output for a dpub role, used to identify the acknowledgments section of a document.
		output=pgettext("aria", "acknowledgments"),
		priority=DpubRolesLevel.ALL,
		landmark=True,
	),
	"doc-afterword": DpubRole(
		name="doc-afterword",
		# Translators: The output for a dpub role, used to identify the afterword section of a document.
		output=pgettext("aria", "afterword"),
		priority=DpubRolesLevel.MOST,
		landmark=True,
	),
	"doc-appendix": DpubRole(
		name="doc-appendix",
		# Translators: The output for a dpub role, used to identify the appendix section of a document.
		output=pgettext("aria", "appendix"),
		priority=DpubRolesLevel.MOST,
		landmark=True,
	),
	"doc-backlink": DpubRole(
		name="doc-backlink",
		# Translators: The output for a dpub role, used to identify the backlink section of a document.
		output=pgettext("aria", "back link"),
		priority=DpubRolesLevel.SOME,
		landmark=False,
	),
	"doc-bibliography": DpubRole(
		name="doc-bibliography",
		# Translators: The output for a dpub role, used to identify the bibliography section of a document.
		output=pgettext("aria", "bibliography"),
		priority=DpubRolesLevel.MOST,
		landmark=True,
	),
	"doc-biblioref": DpubRole(
		name="doc-biblioref",
		# Translators: The output for a dpub role, used to identify the bibliographic reference section of a document.
		output=pgettext("aria", "bibliographic reference"),
		priority=DpubRolesLevel.SOME,
		landmark=False,
	),
	"doc-chapter": DpubRole(
		name="doc-chapter",
		# Translators: The output for a dpub role, used to identify the chapter section of a document.
		output=pgettext("aria", "chapter"),
		priority=DpubRolesLevel.SOME,
		landmark=True,
	),
	"doc-colophon": DpubRole(
		name="doc-colophon",
		# Translators: The output for a dpub role, used to identify the colophon section of a document.
		output=pgettext("aria", "colophon"),
		priority=DpubRolesLevel.ALL,
		landmark=False,
	),
	"doc-conclusion": DpubRole(
		name="doc-conclusion",
		# Translators: The output for a dpub role, used to identify the conclusion section of a document.
		output=pgettext("aria", "conclusion"),
		priority=DpubRolesLevel.MOST,
		landmark=True,
	),
	"doc-cover": DpubRole(
		name="doc-cover",
		# Translators: The output for a dpub role, used to identify the cover section of a document.
		output=pgettext("aria", "cover"),
		priority=DpubRolesLevel.MOST,
		landmark=False,
	),
	"doc-credit": DpubRole(
		name="doc-credit",
		# Translators: The output for a dpub role, used to identify the credit section of a document.
		output=pgettext("aria", "credit"),
		priority=DpubRolesLevel.ALL,
		landmark=False,
	),
	"doc-credits": DpubRole(
		name="doc-credits",
		# Translators: The output for a dpub role, used to identify the credits section of a document.
		output=pgettext("aria", "credits"),
		priority=DpubRolesLevel.ALL,
		landmark=True,
	),
	"doc-dedication": DpubRole(
		name="doc-dedication",
		# Translators: The output for a dpub role, used to identify the dedication section of a document.
		output=pgettext("aria", "dedication"),
		priority=DpubRolesLevel.MOST,
		landmark=False,
	),
	"doc-endnotes": DpubRole(
		name="doc-endnotes",
		# Translators: The output for a dpub role, used to identify the endnotes section of a document.
		output=pgettext("aria", "endnotes"),
		priority=DpubRolesLevel.SOME,
		landmark=True,
	),
	"doc-epigraph": DpubRole(
		name="doc-epigraph",
		# Translators: The output for a dpub role, used to identify the epigraph section of a document.
		output=pgettext("aria", "epigraph"),
		priority=DpubRolesLevel.ALL,
		landmark=False,
	),
	"doc-epilogue": DpubRole(
		name="doc-epilogue",
		# Translators: The output for a dpub role, used to identify the epilogue section of a document.
		output=pgettext("aria", "epilogue"),
		priority=DpubRolesLevel.MOST,
		landmark=True,
	),
	"doc-errata": DpubRole(
		name="doc-errata",
		# Translators: The output for a dpub role, used to identify the errata section of a document.
		output=pgettext("aria", "errata"),
		priority=DpubRolesLevel.ALL,
		landmark=True,
	),
	"doc-examples": DpubRole(
		name="doc-examples",
		# Translators: The output for a dpub role, used to identify the examples section of a document.
		output=pgettext("aria", "examples"),
		priority=DpubRolesLevel.MOST,
		landmark=False,
	),
	"doc-footnote": DpubRole(
		name="doc-footnote",
		# Translators: The output for a dpub role, used to identify the footnote section of a document.
		output=pgettext("aria", "footnote"),
		priority=DpubRolesLevel.SOME,
		landmark=False,
	),
	"doc-foreword": DpubRole(
		name="doc-foreword",
		# Translators: The output for a dpub role, used to identify the foreword section of a document.
		output=pgettext("aria", "foreword"),
		priority=DpubRolesLevel.MOST,
		landmark=True,
	),
	"doc-glossary": DpubRole(
		name="doc-glossary",
		# Translators: The output for a dpub role, used to identify the glossary section of a document.
		output=pgettext("aria", "glossary"),
		priority=DpubRolesLevel.MOST,
		landmark=True,
	),
	"doc-glossref": DpubRole(
		name="doc-glossref",
		# Translators: The output for a dpub role, used to identify a reference to a glossary definition.
		output=pgettext("aria", "glossary reference"),
		priority=DpubRolesLevel.SOME,
		landmark=False,
	),
	"doc-index": DpubRole(
		name="doc-index",
		# Translators: The output for a dpub role, used to identify the index section of a document.
		output=pgettext("aria", "index"),
		priority=DpubRolesLevel.MOST,
		landmark=False,
	),
	"doc-introduction": DpubRole(
		name="doc-introduction",
		# Translators: The output for a dpub role, used to identify the introduction section of a document.
		output=pgettext("aria", "introduction"),
		priority=DpubRolesLevel.MOST,
		landmark=True,
	),
	"doc-noteref": DpubRole(
		name="doc-noteref",
		# Translators: The output for a dpub role, used to identify a reference to a note section of a document.
		output=pgettext("aria", "note reference"),
		priority=DpubRolesLevel.SOME,
		landmark=False,
	),
	"doc-notice": DpubRole(
		name="doc-notice",
		# Translators: The output for a dpub role, used to identify the notice section of a document.
		output=pgettext("aria", "notice"),
		priority=DpubRolesLevel.SOME,
		landmark=False,
	),
	"doc-pagebreak": DpubRole(
		name="doc-pagebreak",
		# Translators: The output for a dpub role, used to identify a page break in a document.
		output=pgettext("aria", "page break"),
		priority=DpubRolesLevel.SOME,
		landmark=False,
	),
	"doc-pagelist": DpubRole(
		name="doc-pagelist",
		# Translators: The output for a dpub role, used to identify the page list section of a document.
		output=pgettext("aria", "list of pages"),
		priority=DpubRolesLevel.SOME,
		landmark=False,
	),
	"doc-part": DpubRole(
		name="doc-part",
		# Translators: The output for a dpub role, used to identify the part section of a document.
		output=pgettext("aria", "part"),
		priority=DpubRolesLevel.MOST,
		landmark=True,
	),
	"doc-preface": DpubRole(
		name="doc-preface",
		# Translators: The output for a dpub role, used to identify the preface section of a document.
		output=pgettext("aria", "preface"),
		priority=DpubRolesLevel.MOST,
		landmark=True,
	),
	"doc-prologue": DpubRole(
		name="doc-prologue",
		# Translators: The output for a dpub role, used to identify the prologue section of a document.
		output=pgettext("aria", "prolog"),
		priority=DpubRolesLevel.MOST,
		landmark=True,
	),
	"doc-pullquote": DpubRole(
		name="doc-pullquote",
		# Translators: The output for a dpub role, used to identify the pull quote section of a document.
		output=pgettext("aria", "emphasized text"),
		priority=DpubRolesLevel.SOME,
		landmark=False,
	),
	"doc-qna": DpubRole(
		name="doc-qna",
		# Translators: The output for a dpub role, used to identify the question and answers section of a document.
		output=pgettext("aria", "questions and answers"),
		priority=DpubRolesLevel.SOME,
		landmark=False,
	),
	"doc-subtitle": DpubRole(
		name="doc-subtitle",
		# Translators: The output for a dpub role, used to identify the subtitle head of a document.
		output=pgettext("aria", "subtitle"),
		priority=DpubRolesLevel.SOME,
		landmark=False,
	),
	"doc-tip": DpubRole(
		name="doc-tip",
		# Translators: The output for a dpub role, used to identify a tip in a document.
		output=pgettext("aria", "tip"),
		priority=DpubRolesLevel.SOME,
		landmark=False,
	),
	"doc-toc": DpubRole(
		name="doc-toc",
		# Translators: The output for a dpub role, used to identify the table of contents section of a document.
		output=pgettext("aria", "table of contents"),
		priority=DpubRolesLevel.SOME,
		landmark=False,
	),
}
