import sys, csv, json
from geopy import geocoders
from geojson import Point, Feature, FeatureCollection

def geocode(input_file):
    """
    Geocodes a CSV file of schools. The data has to be in the format:
    Column A: name of the school
    Column B: address of the school
    Column C: zip code of the school

    There shouldn't be a header row
    """
    output = open(input_file + '.geojson', 'w')
    writer = csv.writer(output, delimiter=',')

    features = []

    with open(input_file + '.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            g = geocoders.GoogleV3()
            print 'Geocoding %s' % row[0]
            place, (lat, lng) = g.geocode(row[1] +
                                          ' Philadelphia, PA ' +
                                          row[2])
            p = Point((lng, lat))
            feature = Feature(geometry=p,
                              properties={'name':row[0],
                                          'address': row[1]})
            features.append(feature)
        collection = FeatureCollection(features)
        collection = json.dumps(collection, sort_keys=False, indent=2)
        output.write(collection)
        output.close()
        print 'Done!'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Pass the name of the CSV file of schools that you want to geocode'
    else:
        geocode(sys.argv[1])
