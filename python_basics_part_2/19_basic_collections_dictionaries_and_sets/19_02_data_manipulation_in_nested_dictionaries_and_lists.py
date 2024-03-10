# Data Manipulation in Nested Dictionaries and Lists
# This script demonstrates various data manipulation operations on a nested dictionary and list structure,
# including accessing, updating, and summarizing data.

# Initial complex data structure
data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

# Printing the keys and values of the data dictionary
print("Keys:", list(data.keys()))
print("Values:", list(data.values()))

# Updating the 'total_diff' in 'ETH'
data["ETH"]["total_diff"] = 100

# Changing the name of the first token to 'doge'
data["tokens"][0]["fst_token_info"]["name"] = "doge"

# Summing up 'total_out' values and removing the 'total_out' key
total_out_sum = sum(token.pop("total_out", 0) for token in data["tokens"])

# Updating 'totalOut' in 'ETH'
data["ETH"]["totalOut"] += total_out_sum

# Adding 'total_price' key in the second token info, moving the value of 'price'
data["tokens"][1]["sec_token_info"]["total_price"] = data["tokens"][1]["sec_token_info"].pop("price")

# Printing the updated data
print("\nUpdated Data:")
print(data)
