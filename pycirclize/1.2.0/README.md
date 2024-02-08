# pyCirclize container

Main tool: [pyCirclize](https://pypi.org/project/pyCirclize/)
  
Code repository: https://github.com/moshi4/pyCirclize

Basic information on how to use this tool:
- executable: NA
- help: NA
- version: NA
- description: pyCirclize is a python package for creating visual images of circular genomes (like those of bacteria)
 
Full documentation: https://pypi.org/project/pyCirclize/

## Example Usage

This is for running containers with a specific python package, and is not really meant to be run from the command line. Instead, a bioinformatician could create a python script that uses pycirclize.

example1.py:
```python
from pycirclize import Circos
import numpy as np
np.random.seed(0)

# Initialize Circos sectors
sectors = {"A": 10, "B": 15, "C": 12, "D": 20, "E": 15}
circos = Circos(sectors, space=5)

for sector in circos.sectors:
    # Plot sector name
    sector.text(f"Sector: {sector.name}", r=110, size=15)
    # Create x positions & random y values
    x = np.arange(sector.start, sector.end) + 0.5
    y = np.random.randint(0, 100, len(x))
    # Plot lines
    track1 = sector.add_track((80, 100), r_pad_ratio=0.1)
    track1.xticks_by_interval(interval=1)
    track1.axis()
    track1.line(x, y)
    # Plot points 
    track2 = sector.add_track((55, 75), r_pad_ratio=0.1)
    track2.axis()
    track2.scatter(x, y)
    # Plot bars
    track3 = sector.add_track((30, 50), r_pad_ratio=0.1)
    track3.axis()
    track3.bar(x, y)

# Plot links 
circos.link(("A", 0, 3), ("B", 15, 12))
circos.link(("B", 0, 3), ("C", 7, 11), color="skyblue")
circos.link(("C", 2, 5), ("E", 15, 12), color="chocolate", direction=1)
circos.link(("D", 3, 5), ("D", 18, 15), color="lime", ec="black", lw=0.5, hatch="//", direction=2)
circos.link(("D", 8, 10), ("E", 2, 8), color="violet", ec="red", lw=1.0, ls="dashed")

circos.savefig("example01.png")
```

```bash
python example1.py
```