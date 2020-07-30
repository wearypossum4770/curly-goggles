from scrapy import Spider
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)


def build_url_list():
    profession_codes = [
        "BAR",
        "BAS",
        "BBS",
        "BIN",
        "BES",
        "BSH",
        "CAB",
        "CAP",
        "CBN",
        "CBS",
        "CES",
        "CHB",
        "CIN",
        "CIS",
        "CST",
        "TCS",
        "SOM",
        "COA",
        "COH",
        "COM",
        "SOC",
    ]
    starturls = [
        f"https://pr.mo.gov/downloadables/{pro_code}.ZIP"
        for pro_code in profession_codes
    ]
    return starturls


class COSBARSpider(Spider):
    name = "cosbar"
    # ~ starturls =build_url_list()
    file_urls = build_url_list()

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = "quotes-%s.html" % page
        with open(filename, "wb") as f:
            f.write(response.body)
            self.log("Saved file %s" % filename)
        print("\n\n\n\n\n")
        pp.pprint(self)
        print("\n\n\n\n\n")
        pp.pprint(response)
        # ~ zip_db_file
        # ~ with open (zip_db_file,'w+') as save_data:
        # ~ save_data.write()


def pro_mapper():
    profession_mapper = {
        "BAR": "Barber",
        "BAS": "Barber Shop",
        "BBS": "Barber School",
        "BIN": "Barber Instructor",
        "BES": "Beauty Shop",
        "BSH": "Beauty & Barber Shop",
        "CAB": "Hairdressing & Manicuring/Barber",
        "CAP": "Cosmetology Apprentic",
        "CBN": "Cosmetology/Barber Instructor",
        "CBS": "Cosmetology/Barber School",
        "CES": "Cosmetology Esthetics",
        "CHB": "Hairdressing/Barber",
        "CIN": "Cosmetology Instructor",
        "CIS": "Student Instructor Cosmetologist",
        "CST": "Cosmetology Student",
        "TCS": "Temporary Cosmetologist Student",
        "SOM": "School of Manicuring",
        "COA": "Cosmetologist/All",
        "COH": "Cosmetologist/Hairdressing",
        "COM": "Cosmetologist/Manicuring",
        "SOC": "School of Cosmetology",
    }
