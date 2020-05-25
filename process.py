data = {
    'adelaide': [('#auspol', 1354), ('#dicksonvotes', 309), ('#warringahvotes', 287), ('#lnp', 214), ('#mayovotes', 186), ('#ausvotes', 145), ('#ausvotes2019', 118), ('#lnpfail', 95), ('#watergate2019', 63), ('#ourabcnews', 54), ('#coal', 48), ('#ausvotes19', 47), ('#liberalaus', 45), ('#murdoch', 45), ('#insiders', 37), ('#labor', 37), ('#australia', 36), ('#morrison', 36), ('#abbott', 35), ('#auslaw', 33)],
    'melbourne': [('#auspol', 3461), ('#ausvotes', 628), ('#ausvotes2019', 557), ('#ausvotes19', 245), ('#election2019', 89), ('#watergate', 71), ('#lnp', 64), ('#budget2019', 60), ('#auspol2019', 54), ('#ausvote2019', 54), ('#climateelection', 47), ('#scomo', 47), ('#insiders', 45), ('#qanda', 42), ('#springst', 42), ('#changetherules', 41), ('#climatechange', 41), ('#leadersdebate', 39), ('#kooyongvotes', 36), ('#melbourne', 36)],
    'sydney': [('#auspol', 3743), ('#ausvotes2019', 632), ('#ausvotes', 630), ('#ausvotes19', 252), ('#warringahvotes', 152), ('#nswpol', 98), ('#scomo', 96), ('#lnp', 92), ('#watergate', 90), ('#lnpfail', 83), ('#qanda', 75), ('#auspol2019', 63), ('#climatechange', 60), ('#nswvotes', 50), ('#insiders', 49), ('#ausvote2019', 46), ('#australiavotes', 43), ('#mentalhealth', 38), ('#lnpcorruption', 37), ('#msm', 37)],
    'brisbane': [('#auspol', 2736), ('#ausvotes2019', 761), ('#ausvotes', 348), ('#ausvotes19', 99), ('#election2019', 98), ('#qldpol', 87), ('#dicksonvotes', 45), ('#ilikebillshorten', 44), ('#climatechange', 44), ('#libsfail', 39), ('#fakesurplus', 37), ('#christchurch', 36), ('#qanda', 35), ('#lnp', 35), ('#nswpol', 33), ('#phon', 32), ('#insiders', 29), ('#auspol2019', 29), ('#stopadani', 27), ('#onenation', 27)],
    'perth': [('#auspol', 2245), ('#ausvotes2019', 597), ('#ausvotes', 379), ('#ausvotes19', 177), ('#nswvotes', 161), ('#climatechange', 96), ('#scomo', 93), ('#lnp', 71), ('#wapol', 63), ('#insiders', 63), ('#thedrum', 54), ('#ausvote2019', 47), ('#nswpol', 46), ('#budget2019', 43), ('#election2019', 35), ('#newzealand', 33), ('#votelabor', 32), ('#newzealandterroristattacks', 30), ('#lnpfail', 30), ('#islamophobia', 29)],
}

import json
result = {}

for key in data:
    count = 0
    print()
    # includes hashtags containing auspol, ausvotes, election
    for item in data[key]:
        if 'auspol' in item[0] or 'ausvotes' in item[0] or 'election' in item[0]:
            print(key, item) 
            count += item[1]
    
    result[key] = count

with open('result.json', 'w') as fp:
    json.dump(result, fp)
