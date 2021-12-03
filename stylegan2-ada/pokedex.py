#%%
import pokepy
import json

start = 1
end = 898
dict = {}
client = pokepy.V2Client()
for i in range(start,end+1):
    p = client.get_pokemon(i)
    name = p[0].name
    type = [p[0].types[j].type.name for j in range(len(p[0].types))]
    # type = [pb.pokemon(i).types[j].type.name for j in range(len(pb.pokemon(i).types))]
    dict[str(i).zfill(3)] = name + ", " + ", ".join(type)
    print(list(dict)[-1])

with open('datasets/text.json', 'w') as fp:
    json.dump(dict, fp,  indent=4)

#%%
import json

# %%
