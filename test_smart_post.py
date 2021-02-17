from postinumerot import etsi_postinumerot


def test_etsi_smart_post():
    TOIMIPAIKAT = {
        "44884": "SMART POST",
        "35540": "SMART-POST",
        "08504": "SMARTPSOT",
        "12345": "SMARTPOST",
        "22222": "SMARTTIPOSTI",
    }
    tulos = etsi_postinumerot('SMARTPOST', TOIMIPAIKAT)
    assert tulos == 'Postinumerot: 08504, 12345, 35540, 44884'
