# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/artifact/artifact/infrastructure/dbus/sandbox_artifact_dbus_signal_emitter.py

This file defines the SandboxArtifactDbusSignalEmitter class.

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
    ArtifactArtifactDbusSignalEmitter,
)


class SandboxArtifactDbusSignalEmitter(ArtifactArtifactDbusSignalEmitter):

    """
    A class to materialize ArtifactArtifactDbusSignalEmitter to be used within the Sandbox (meta)artifact context.

    Class name: SandboxArtifactDbusSignalEmitter

    Responsibilities:
        - Connect to d-bus.
        - Emit domain events as d-bus signals.

    Collaborators:
        - pythoneda.application.PythonEDA: Requests emitting events.
        - pythoneda.shared.artifact.artifact.events.infrastructure.dbus.*
    """

    def __init__(self):
        """
        Creates a new SandboxArtifactDbusSignalEmitter instance.
        """
        super().__init__()
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
