import json
#
#========================== CREATE JSON FILES (and add to them) * if ever to-production, use scraper =======================================
#
# rcp = {'Nat\'s Bolognese':{'pork mince':500, 'beef mince':500, 'red wine':300, 'onion':1, 'celery':1, 'carrot':3, 'canned tomatoes':400, 'milk':100, 'thyme':2, },\
#             'Nat\'s Chicken Curry':{'chicken breasts':3, 'rice':200, 'double cream':1, 'chicken stock':400, 'tomatoes, canned':400, 'yoghurt, plain':300, 'garlic':3, \
#             'coriander':1, 'onion':1, 'chilli':1, 'bell pepper':2,}, 'Tom\'s Chicken Pasta':{'chicken breast':3, 'tomatoes, canned':800, 'onion':1, 'carrot':2, 'turmeric':1, \
#             'coriander':1, 'cumin':1, 'chestnut mushrooms':200, 'pasta':300, 'garlic':1, 'fine beans':200}, 'Gordon\'s Chorizo Roast Chicken':{'chorizo':1, 'onion':2, 'garlic':1, \
#             'cannolini beans':400, 'thyme':1, 'tomatoes, dried':150, 'lemon':1, 'paprika':1}, 'Tom\'s Chilli':{'beef mince':800, 'onion':1, 'dark chocolate':50, \
#             'fine beans':200, 'garlic':1, 'cumin':1, 'paprika':1, 'chilli powder':1, 'coriander':1, 'carrot':2, 'pepper, green':2, 'kidney beans':400, 'chilli':2, \
#             'tomatoes, canned':400, 'beef stock':400, 'red wine':300}}

# with open ("recipes.json", "w") as outfile:
#     json.dump(rcp, outfile)

# rcp_object = json.dumps(rcp, indent=4)
# print(rcp_object)