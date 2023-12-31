"""
pythoneda/sandbox/artifact/artifact/infrastructure/dbus/sandbox_artifact_dbus_signal_listener.py

This file defines the SandboxArtifactDbusSignalListener class.

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
from pythoneda.shared.artifact.artifact.infrastructure.dbus import (
    ArtifactArtifactDbusSignalListener,
)


class SandboxArtifactDbusSignalListener(ArtifactArtifactDbusSignalListener):

    """
    A class to materialize ArtifactArtifactDbusSignalListener to be used within the Sandbox (meta)artifact context.

    Class name: SandboxArtifactDbusSignalListener

    Responsibilities:
        - Connect to d-bus.
        - Listen to signals relevant to Sandbox-artifact.

    Collaborators:
        - pythoneda.application.pythoneda.PythonEDA: Receives relevant domain events.
        - pythoneda.shared.artifact.artifact.events.infrastructure.dbus.*
    """

    def __init__(self):
        """
        Creates a new SandboxArtifactDbusSignalListener instance.
        """
        super().__init__()
