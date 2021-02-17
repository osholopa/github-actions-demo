from postinumerot import etsi_postinumerot


def test_etsi_postinumerot():
    TOIMIPAIKAT = {
        "74701": "KIURUVESI",
        "35540": "JUUPAJOKI",
        "74700": "KIURUVESI",
        "73460": "MUURUVESI"
    }
    tulos = etsi_postinumerot('KIURUVESI', TOIMIPAIKAT)
    assert tulos == 'Postinumerot: 74700, 74701'

def test_etsi_postinumerot_rajatapaukset():
    ERIKOISTAPAUKSET = {
        "43800": "KIVIJÄRVI",
        "91150": "YLI-OLHAVA",
        "65374": "SMART POST"
    }
    for avain, arvo in ERIKOISTAPAUKSET.items():
        tulos = etsi_postinumerot(arvo, ERIKOISTAPAUKSET)
        assert tulos == f'Postinumerot: {avain}'
