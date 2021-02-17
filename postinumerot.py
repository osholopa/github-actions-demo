import json
import http_pyynto
import re

def formatoi(merkkijono):
    return re.sub(r'^[SMARTPOST]+$', 'SMARTPOST', re.sub(r'[\s-]*', '', merkkijono))

def etsi_postinumerot(postitmp, sanakirja):
    results = []
    
    for tmp in sanakirja.items():
        if(formatoi(tmp[1]) == formatoi(postitmp)):
            results.append(tmp[0])

    if len(results) == 0:
        return 'Ei löytynyt'
    else:
        results.sort()
        return f'Postinumerot: {", ".join(results)}'


if __name__ == '__main__':
    postinumerot = http_pyynto.hae_postinumerot()
    postitmp = input('Kirjoita postitoimipaikka: ').strip().upper()
    print(etsi_postinumerot(postitmp, postinumerot))
    