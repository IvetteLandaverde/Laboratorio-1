
#dict_test = {'key_a': 'a', 'key_b': 'b'}
import numpy as np
import pandas as pd
import json

# Opening JSON file
f= open("orderbooks_05jul21.json")

# Returns JSON object as a dictionary
orderbooks_data = json.load(f)
#ob_data = orderbooks_data["bitfinex"]