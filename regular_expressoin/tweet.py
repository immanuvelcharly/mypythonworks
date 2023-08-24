from re import*
tweets="what a game, hats off to both teams .well @benstock38 @patcumins38 @patcummins30 you have bought "
rule="[@][a-zA-Z0-9]+"
matcher=finditer(rule,tweets)
for m in matcher:
    print(m.group())
