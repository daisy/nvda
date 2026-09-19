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
	landmark: bool = True

	def __str__(self):
		return f"{self.name} ({self.output}, priority {self.priority})"

	def __repr__(self):
		return f"DpubRole(name={self.name}, output={self.output}, priority={self.priority})"


dpubRoles: dict[str, DpubRole] = {
	"doc-abstract": DpubRole(
		name="doc-abstract",
		# Translators: The output for a dpub role.
		output=pgettext("dpub role", "Abstract"),
		priority=DpubRolesLevel.SOME,
	),
}
