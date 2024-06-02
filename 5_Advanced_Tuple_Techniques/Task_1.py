# Example Catalogs
catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))

# Function to join multiple product catalogs
def join_catalogs(*catalogs):
    combined_catalog = ()
    for catalog in catalogs:
        combined_catalog += catalog
    return combined_catalog

# Join the example catalogs
combined_catalog = join_catalogs(catalog1, catalog2)

# Print the combined catalog
print("Combined Product Catalog:")
for product in combined_catalog:
    print(f"Product: {product[0]}, Price: {product[1]}")
