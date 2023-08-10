catalog = {
    "PS5 Game": {
        "brand": "God of War",
        "price": 49.00
    },

    "XBOX One Game": {
        "brand": "Halo 5",
        "price": 33.33
    },

    "Nintendo Switch Game": {
        "brand": "Mario/Wario",
        "price": 60.00
    }
}

def cat_org(catalog):
    for game, brands in catalog.items():
        print(game)
        for brand, price in brands.items():
            print(f"{brand}: {price}")
        print()

def main():
    cat_org(catalog)

if __name__ == "__main__":
    main()