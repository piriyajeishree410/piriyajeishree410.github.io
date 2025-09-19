import json, random

neighborhoods = [
    "Back Bay","Beacon Hill","North End","South End","Fenway",
    "Jamaica Plain","Charlestown","Seaport","Cambridge","Allston"
]
amenities_pool = [
    "Wi-Fi","Kitchen","Air Conditioning","Heating","Washer","Dryer","TV",
    "Essentials","Hot Tub","Pool","Parking","Elevator","Gym","Pet Friendly","Smoke Alarm"
]

listings = []
for i in range(1, 51):
    neigh = random.choice(neighborhoods)
    n_amen = random.randint(3, 7)
    listing_amen = random.sample(amenities_pool, n_amen)
    listings.append({
        "name": f"Charming Apt in {neigh} #{i}",
        "description": f"A comfy place in {neigh}, close to transit and cafes. Great for students and visitors.",
        "amenities": listing_amen,
        "host": {
            "host_name": f"Host_{random.randint(1,999)}",
            "host_thumbnail_url": f"https://i.pravatar.cc/40?img={random.randint(1,70)}"
        },
        "price": random.randint(70, 350),
        "thumbnail_url": f"https://picsum.photos/300/200?random={i}",
        "rating": round(4 + random.random(), 1)
    })

with open("data/airbnb_listings.json", "w", encoding="utf-8") as f:
    json.dump(listings, f, indent=2, ensure_ascii=False)

print("Created data/airbnb_listings.json with 50 items")
