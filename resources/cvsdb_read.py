import csv
from db_engine.model import Category, Market


def get_states():
    state_set = set()
    with (open(r"..\resources\Export.csv", "r", encoding="utf-8-sig", newline="") as csvfile):
        csvreader = csv.reader(csvfile)
        csvreader.__next__()
        for row in csvreader:
            state_set.add(row[10].strip())
    return state_set


def get_countries(states):
    # вычитваем округа из Export.csv -> перезаписываем округа и IDшники штатов в ExportStateID.csv
    countries_set = set()
    with (open(r"..\resources\Export.csv", "r", encoding="utf-8-sig", newline="") as csvfile):
        csvreader = csv.reader(csvfile)
        header = csvreader.__next__()
        with open(r"..\resources\ExportStateID.csv", "w", encoding="utf-8-sig", newline="") as exportfile:
            csvwriter = csv.writer(exportfile)
            csvwriter.writerow(header)

        for row in csvreader:
            with open(r"..\resources\ExportStateID.csv", "a", encoding="utf-8-sig", newline="") as exportfile:
                csvwriter = csv.writer(exportfile)
                row_to_write = row
                statename = row[10]
                state = list(filter(lambda x: x.name.strip().lower() == statename.strip().lower(), states))[0]
                row_to_write[10] = state.id
                csvwriter.writerow(row_to_write)
                countries_set.add((row[9].strip(), state.id))
    return countries_set


def get_cities(countries):
    # вычитваем города из ExportStateID.csv -> перезаписываем города и IDшники округов в ExportCountryID.csv
    cities_set = set()
    with (open(r"..\resources\ExportStateID.csv", "r", encoding="utf-8-sig", newline="") as csvfile):
        csvreader = csv.reader(csvfile)
        header = csvreader.__next__()
        with open(r"..\resources\ExportCountryID.csv", "w", encoding="utf-8-sig", newline="") as exportfile:
            csvwriter = csv.writer(exportfile)
            csvwriter.writerow(header)

        for row in csvreader:
            with open(r"..\resources\ExportCountryID.csv", "a", encoding="utf-8-sig", newline="") as exportfile:
                csvwriter = csv.writer(exportfile)
                row_to_write = row
                city_name = row_to_write[8]
                country_name = row_to_write[9]
                state_id = row_to_write[10]
                country = list(filter(lambda x: (x.name.strip().lower() == country_name.strip().lower()
                                                 and x.state_id == int(state_id)), countries))[0]
                row_to_write[9] = country.id
                cities_set.add((city_name.strip(), country.id))
                csvwriter.writerow(row_to_write)

    return cities_set


def write_city_id(cities):
    # вычитваем города из ExportCountryID.csv -> перезаписываем города и IDшники городов в ExportCityID.csv
    with (open(r"..\resources\ExportCountryID.csv", "r", encoding="utf-8-sig", newline="") as csvfile):
        csvreader = csv.reader(csvfile)
        header = csvreader.__next__()
        with open(r"..\resources\ExportCityID.csv", "w", encoding="utf-8-sig", newline="") as exportfile:
            csvwriter = csv.writer(exportfile)
            csvwriter.writerow(header)

        for row in csvreader:
            with open(r"..\resources\ExportCityID.csv", "a", encoding="utf-8-sig", newline="") as exportfile:
                csvwriter = csv.writer(exportfile)
                row_to_write = row
                city_name = row_to_write[8]
                country_ID = int(row_to_write[9])
                city = list(filter(lambda x: (x.name.strip().lower() == city_name.strip().lower() and
                                              x.country_id == country_ID), cities))[0]
                row_to_write[8] = city.id
                csvwriter.writerow(row_to_write)


def get_categories():
    with (open(r"..\resources\ExportCityID.csv", "r", encoding="utf-8-sig", newline="") as csvfile):
        csvreader = csv.reader(csvfile)
        header = csvreader.__next__()

        categories = list(map(lambda catetory: Category(name=catetory.strip()), header[28:58]))
        return categories


def get_markets(categories):
    # вычитваем рынки из ExportCityID.csv
    markets = list()
    mark_cat = list()
    with (open(r"..\resources\ExportCityID.csv", "r", encoding="utf-8-sig", newline="") as csvfile):
        csvreader = csv.reader(csvfile)
        header = csvreader.__next__()
        cat_names = header[28:58]
        for row in csvreader:
            market = Market()
            market.id = int(row[0])
            market.city_id = int(row[8])
            market.name = row[1]
            market.website, market.facebook = row[2], row[3]
            market.twitter, market.youtube = row[4], row[5]
            market.media = row[6]
            market.street = row[7]
            market.season1date, market.season1time = row[12], row[13]
            market.season2date, market.season2time = row[14], row[15]
            market.season3date, market.season3time = row[16], row[17]
            market.season4date, market.season4time = row[18], row[19]
            market.zip = row[11]
            market.lat = float(row[20])
            market.lon = float(row[21])
            market.loc = row[22]
            market.lastupdated = row[58]

            lambda_true = lambda x : x.strip().upper() == "Y"
            market.credit = lambda_true(row[23])
            market.wic = lambda_true(row[24])
            market.wiccsah = lambda_true(row[25])
            market.sfmnp = lambda_true(row[26])
            market.snap = lambda_true(row[27])

            seed_categories(mark_cat, market.id, cat_names, row[28:58], categories)
            markets.append(market)
    return markets, mark_cat


def seed_categories(mark_cat, mark_id, cat_names, csv_row, categories):
    if len(cat_names) != len(csv_row):
        raise Exception("Bad happened")
    for i in range(0, len(cat_names)):
        if (csv_row[i]).strip().upper() == "Y":
            cat_to_append = list(filter(lambda x: x.name == cat_names[i].strip(),
                                        categories))[0]
            mark_cat.append((mark_id, cat_to_append.id))

