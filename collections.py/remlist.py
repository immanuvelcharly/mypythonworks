birds=["peacok","duck","hen","kozhi"]
ch_birds=input('enter  a bird :')
for i in birds:
    if i==ch_birds:
        birds.remove(i)
print(birds)