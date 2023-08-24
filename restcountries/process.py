from json import load
with open("C:\\Users\IMMANUEL\\Desktop\python\\restcountries\\rest.json",encoding="UTF-8")as f:
    data=load(f)
    # print(len(data))

    #print all country names
    # for m in data:
    #     print(m.get("name"))
# all_country_names=[m.get("names")for m in data]
# print all countrey names
all_region_names={m.get("region")for m in data}
print(all_region_names)
# print asia country names
asia=[m.get("name")for m in data if m.get ("region")=="Asia"]
print(asia)
# print population of afganistan
pop_afg=[m.get("population")for m in data if m.get("name")=="Afghanistan"]
print(pop_afg)
# print india boarders
boardes=[m.get("borders")for m in data if m.get("name")=="India"][0]
print(boardes)
country_boarders_name=[m.get("name")for m in data if m.get("alpha3Code")in boardes]
print(country_boarders_name)
# 
#print currency code
currency=[m.get("code")for m in data if m.get("name")=="India"]
print(currency)