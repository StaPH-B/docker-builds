# Bandage container

Main tool: [Bandage](https://rrwick.github.io/Bandage/)
  
Code repository: https://github.com/rrwick/Bandage

Basic information on how to use this tool:
- executable: Bandage
- help: --help
- version: --version
- description: |

> Bandage is a program for visualising de novo assembly graphs.
  
Full documentation: [https://github.com/rrwick/Bandage/wiki](https://github.com/rrwick/Bandage/wiki)

## Example Usage
### GUI ###
Example command to use Bandage GUI
```bash
docker run \
-v /my-data-dir:/data
-v /tmp/.X11-unix:/tmp/.X11-unix \
-e DISPLAY=$DISPLAY \
-e QT_QPA_PLATFORM=xcb \
staphb/bandage:0.9.0 \
Bandage
```
### CLI ###
```bash
Bandage image test.gfa test.png
```
