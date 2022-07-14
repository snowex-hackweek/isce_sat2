# isce_sat2

`isce_sat2` (a play on the InSAR processing software [ISCE2](https://github.com/isce-framework/isce2) and ICESat-2) is a project to explore the data fusion possibilities between the ICESat-2 space-based lidar, UAVSAR, and future NISAR based L-band InSAR for snow water storage measurements. 

## Collaborators

- [Hannah Besso](https://github.com/bessoh2) (University of Washington)
- [Zach Keskinen](https://github.com/ZachKeskinen) (Boise State University)
- [Jack Tarricone](https://github.com/jacktarricone) (University of Nevada, Reno)
- [Naheem Adebisi](https://github.com/Surfix) (Boise State University)
- [Young Koo](https://github.com/YoungHyunKoo) (University of Texas, San Antonio)
- [Ben Roberts Pierel](https://github.com/brobertspierel) (Oregon State University)
- [Sam Neitlich](https://github.com/samsamsam34) (Montana State University)
- [Quinn Brencher](https://github.com/gbrencher) (University of Washington)
- [Mia Vanderwilt](https://github.com/MiaVanderwilt) (University of Colorado, Boulder)
- [Karina Zikan](https://github.com/khzikan) (Boise State University)

## Research Motivations

1. How can ICESat-2 improve our ability to use UAVSAR/NISAR?
2. Can we combine these instruments to improve our ability to estimate snow water storage?
3. Learn more about our respective instruments and get to work together!

## What are UAVSAR and ICESat-2?

[UAVSAR](https://uavsar.jpl.nasa.gov/education/what-is-uavsar.html) is a low frequency plane-based synthetic aperature radar. UAVSAR stands for "Uninhabited Aerial Vehicle Synthetic Aperature Radar". It captures imagery using a L-band radar. This low frequency means it can penetrate into and through clouds, vegetation, and snow.

[ICESat-2](https://icesat-2.gsfc.nasa.gov/) or the "Ice, Cloud, and Land Elevation Satellite-2" carries ATLAS, a photon counting LiDAR instrument. The ATLAS laser operates at 532 nanometers, a bright green color, and is split into 3 main tracks each with a weak and strong beam. In this project we work with the ATL03, ATL06, and ATl08 products. ATL03 gives the origonal photon cloud, ATL06 gives land ice elevation, and ATL08 gives land water vegetation elevation.

## Specific Questions

1. Can we use ICESat-2 to constrain phase change in UAVSAR pairs?
2. How well do ICESat-2 snow depths compare to UAVSAR?
3. How often does ICESat-2 intersect with itself and UAVSAR image pairs?
4. Is this kind of comparison scaleable?
5. How does UAVSAR coherence compare with ICESat-2 confidence?


## Contents

### `contributors`
Each team member has it's own folder under contributors, where they can work on their contribution. Having a dedicated folder for each person helps to prevent conflicts when merging with the main branch.

### `notebooks`
Notebooks that are considered delivered results for the project should go in here.

### `scripts`
Helper utilities that are shared with the team
