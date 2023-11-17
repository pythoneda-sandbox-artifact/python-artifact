"""
pythoneda/sandbox/artifact/artifact/infrastructure/cli/sandbox_artifact_cli.py

This file defines the SandboxArtifactCli.

Copyright (C) 2023-today rydnr's https://github.com/pythoneda-sandbox/python-artifact-infrastructure

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
from pythoneda.shared.artifact.infrastructure.cli import ArtifactCli


class SandboxArtifactCli(ArtifactCli):

    """
    A class to materialize ArtifactCli to be used by SandboxArtifact.

    Class name: SandboxArtifactCli

    Responsibilities:
        - Parse the command-line to retrieve the information required, depending on the specific hook.

    Collaborators:
        - pythoneda.shared.artifact.infrastructure.cli.*: CLI handlers.
    """

    def __init__(self):
        """
        Creates a new SandboxArtifactCli instance.
        """
        super().__init__()
