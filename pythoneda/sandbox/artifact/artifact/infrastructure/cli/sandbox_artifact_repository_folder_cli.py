"""
pythoneda/sandbox/artifact/artifact/infrastructure/cli/sandbox_artifact_repository_folder_cli.py

This file defines the SandboxArtifactRepositoryFolderCli.

Copyright (C) 2023-today rydnr's https://github.com/pythoneda-sandbox-artifact/python-artifact

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
from pythoneda.shared.artifact.infrastructure.cli import RepositoryFolderCli


class SandboxArtifactRepositoryFolderCli(RepositoryFolderCli):

    """
    A class to materialize RepositoryFolderCli in the SandboxArtifact context.

    Class name: SandboxArtifactRepositoryFolderCli

    Responsibilities:
        - Parse the command-line to retrieve the information about the repository folder.

    Collaborators:
        - PythonEDA subclasses: They are notified back with the information retrieved from the command line.
    """

    def __init__(self):
        """
        Creates a new SandboxArtifactRepositoryFolderCli instance.
        """
        super().__init__()
