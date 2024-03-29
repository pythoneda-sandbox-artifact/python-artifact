# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/artifact/application/sandbox_artifact_app.py

This file defines the SandboxArtifactApp class.

Copyright (C) 2023-today rydnr's pythoneda-sandbox-artifact/python-artifact

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
import asyncio
from pythoneda.shared.artifact import LocalArtifact
from pythoneda.shared.artifact.application import LocalArtifactApp
from pythoneda.sandbox.artifact.artifact.infrastructure import LocalSandboxArtifact


class SandboxArtifactApp(LocalArtifactApp):
    """
    Runs the SandboxArtifact PythonEDA app.

    Class name: SandboxArtifactApp

    Responsibilities:
        - Runs the SandboxArtifact PythonEDA app.

    Collaborators:
        - Command-line handlers from pythoneda-shared-artifact/infrastructure
    """

    def __init__(self):
        """
        Creates a new SandboxArtifactApp instance.
        """
        # sandbox_artifact_banner is automatically generated by pythoneda-sandbox-def/python-artifact's flake.
        try:
            from pythoneda.sandbox.artifact.artifact.application.sandbox_artifact_banner import SandboxArtifactBanner
            banner = SandboxArtifactBanner()
        except ImportError:
            banner = None

        super().__init__(banner, __file__)

    @classmethod
    def local_artifact_class(cls) -> type[LocalArtifact]:
        """
        Retrieves the subclass of LocalArtifact.
        :return: Such class.
        :rtype: type[LocalArtifact]
        """
        return LocalSandboxArtifact


if __name__ == "__main__":
    asyncio.run(
        SandboxArtifactApp.main(
            "pythoneda.sandbox.artifact.artifact.application.SandboxArtifactApp"
        )
    )
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
