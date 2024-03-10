from default_zero_dict import DefaultZeroDict

# Demonstration of using DefaultZeroDict

demo_dict = DefaultZeroDict({'a': 4, 'b': 8})

# Accessing existing key
print(f"Value for 'a': {demo_dict.get('a')}")

# Accessing non-existing key, defaulting to 0
print(f"Value for 'c' (non-existing): {demo_dict.get('c')}")
