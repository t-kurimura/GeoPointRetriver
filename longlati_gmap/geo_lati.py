import csv
import googlemaps


def request_result(search_key):
    gmaps = googlemaps.Client(key="{api_key}")
    return gmaps.geocode(search_key)


def extract_geo_point(response):
    return response[0]["geometry"]["location"]


def extract_formatted_address(response):
    return response[0]["formatted_address"]


def write_csv(row):
    with open("./point_geo_info.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(row)


ct = 0
with open("longlati_gmap/results-20191223-180631.csv") as f:
    reader = csv.reader(f)

    header = next(reader)
    header.append("lat")
    header.append("lng")
    write_csv(header)

    for row in reader:
        try:
            search_key = ",".join(row)
            response = request_result(search_key)

            row.append(extract_geo_point(response)["lat"])
            row.append(extract_geo_point(response)["lng"])

            write_csv(row)
        except Exception as e:
            print(e)
        finally:
            ct += 1
            if ct % 5 == 0:
                print("prgress: {}".format(ct))
