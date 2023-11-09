# sandbox-artifact-artifact

(Meta)Artifact space for <https://github.com/pythoneda-sandbox/python-artifact>

## How to run it

``` sh
nix run 'https://github.com/pythoneda-sandbox/python-artifact-artifact/[version]?dir=domain-artifact'
```

### Usage

``` sh
nix run https://github.com/pythoneda-sandbox/python-artifact-artifact/[version] [-h|--help] [-r|--repository-folder folder] [-e|--event event] [-t|--tag tag]
```
- `-h|--help`: Prints the usage.
- `-r|--repository-folder`: The folder where <https://github.com/pythoneda-sandbox/python> is cloned.
- `-e|--event`: The event to send. See <https://github.com/pythoneda-shared-artifact/events>.
- `-t|--tag`: If the event is `TagPushed`, specify the tag.

