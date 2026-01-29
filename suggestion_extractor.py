from pytrends.request import TrendReq

pytrends = TrendReq(hl='pl-PL', tz=360)
kw_list = [
#    "mieszkania",
#    "wynajem",
#    "apartment",
#    "dom",
    "kavalerka",
#    "pokoje"
]
for kw in kw_list:
    print(f'\nsuggestions for "{kw}":')
    suggestions = pytrends.suggestions(keyword=kw)
    for s in suggestions:
        print(s)