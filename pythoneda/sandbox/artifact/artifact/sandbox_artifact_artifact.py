"""
pythoneda/sandbox/artifact/artifact/sandbox_artifact_artifact.py

This file declares the SandboxArtifactArtifact class.

Copyright (C) 2023-today rydnr's pythoneda-sandbox/python-artifact-artifact

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.shared.artifact import PythonPackage
from pythoneda.shared.nix_flake import (
    FlakeUtilsNixFlake,
    License,
    PythonedaSharedPythonedaBannerNixFlake,
)


class SandboxArtifactArtifact(PythonPackage):
    """
    Represents the pythoneda-sandbox/python-artifact Python package.

    Class name: Domain

    Responsibilities:
        - Model the pythoneda-sandbox/python-artifact Python package and its metadata.

    Collaborators:
        - pythoneda.shared.artifact.PythonPackage
    """

    def __init__(self, repositoryFolder: str):
        """
        Creates a new PythonPackage instance.
        :param repositoryFolder: The repository folder.
        :type repositoryFolder: str
        """
        flake_utils = FlakeUtilsNixFlake.default()
        nixos = NixosNixFlake.default()
        banner = PythonedaSharedPythonedaBannerNixFlake.default()
        inputs = [flake_utils, nixos, banner]
        version = self.find_out_version(repositoryFolder)
        super().__init__(
            "rydnr",
            self.find_out_version(repositoryFolder),
            f"https://github.com/pythoneda-sandbox/python-artifact-artifact/{version}?dir=python-artifact",
            inputs,
            templateSubfolder,
            "Artifact space of https://github.com/pythoneda-sandbox/python-artifact-artifact",
            self.__class__.url,
            License.from_id(
                Gpl3.license_type(),
                "2023",
                "rydnr",
                self.__class__.url,
            ),
            ["rydnr <github@acm-sl.org>"],
            2023,
            "rydnr",
        )

    @classmethod
    @property
    def url(cls) -> str:
        """
        Retrieves the url.
        :return: Such url.
        :rtype: str
        """
        return "https://github.com/pythoneda-sandbox/python-artifact-artifact"
