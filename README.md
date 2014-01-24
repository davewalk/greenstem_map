# greenSTEM Map

Code and data for the map at [greenstemnetwork.org](http://greenstemnetwork.org/).

### Installation

1. Install [TileMill](https://www.mapbox.com/tilemill/) if you don't have it already.
2. Clone/fork this repo.
3. Create a symbolic link between your TileMill project directory and wherever you pulled down this repo with (run this within the TileMill project dir):  
    `ln -s ~/wherever/this/repo/is greenstem_map`
4. Open TileMill and you should see "greensteam_map" as one of the available projects

### Credits
- Data:  
    - Philadelphia city limits, streets centerline, parks and hydrology layers courtesy of the [City of Philadelphia](http://opendataphilly.org/opendata/search/?qs=City%20of%20Philadelphia)
- Images:  
    - City background image from [subtlepatterns.com](http://subtlepatterns.com)
    - Marker from [Maki](https://www.mapbox.com/maki/) by MapBox
- Colors:  
    - [colourco.de](http://colourco.de) was a huge help

### Geocoding

To update the markers on the map:

1. Edit the `data/schools.csv` file in this project with accurate school names, addresses and zip codes.
2. In the root of the project, install the Python requirements with (psst: you should probably use [virtualenv](http://dabapps.com/blog/introduction-to-pip-and-virtualenv-python/)):  
`pip install -r requirements.txt`
3. And now run the geocoding script:  
`python scripts/geocode_schools.py data/schools`
4. And there you have it, an updated `schools.geojson` file to import into TileMill.

### License

Copyright (c) 2014 Dave Walk   

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


