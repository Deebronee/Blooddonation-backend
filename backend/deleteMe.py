import json

r = {'is_claimed': 'True', 'rating': 3.5}
r = json.dumps(r)
loaded_r = json.loads(r)
loaded_r['rating'] #Output 3.5type(r) #Output strtype(loaded_r) #Output dict




