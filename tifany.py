"""
...
"""

class tifany:
    wms_adress = ""
    example_wms_adress = ""
    georeference = {}
    tif = None
    def __init__(self, adress):
        self.wms_adress = adress

    def __str__(self):
        return "TifAany: WMS " + self.wms_adress
