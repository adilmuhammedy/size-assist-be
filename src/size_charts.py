from src.schemas import GarmentSize

UNIFIED_SIZE_CHART = {

    # 1️⃣ Bottomwear
    "bottomwear": [
        GarmentSize(name="XS", waist=(73.7, 76.2)),
        GarmentSize(name="S", waist=(78.7, 81.3)),
        GarmentSize(name="M", waist=(83.8, 86.4)),
        GarmentSize(name="L", waist=(88.9, 91.4)),
        GarmentSize(name="XL", waist=(94, 96.5)),
        GarmentSize(name="XXL", waist=(99.1, 101.6)),
        GarmentSize(name="3XL", waist=(104.2, 106.7)),
    ],

    # 2️⃣ T-Shirts
    "tshirt": [
        GarmentSize(name="XS", chest=(84, 88), waist=(66, 71), shoulder=(37, 39)),
        GarmentSize(name="S", chest=(89, 93), waist=(72, 76), shoulder=(39, 41)),
        GarmentSize(name="M", chest=(94, 98), waist=(77, 81), shoulder=(41, 43)),
        GarmentSize(name="L", chest=(99, 103), waist=(82, 86), shoulder=(43, 45)),
        GarmentSize(name="XL", chest=(104, 108), waist=(87, 91), shoulder=(45, 47)),
        GarmentSize(name="XXL", chest=(109, 113), waist=(92, 96), shoulder=(47, 49)),
    ],

    # 3️⃣ Formal Shirts
    "formal_shirt": [
        GarmentSize(name="XS", chest=(88, 92), waist=(70, 74), shoulder=(39, 41)),
        GarmentSize(name="S", chest=(92, 96), waist=(74, 78), shoulder=(41, 42)),
        GarmentSize(name="M", chest=(96, 100), waist=(78, 82), shoulder=(42, 44)),
        GarmentSize(name="L", chest=(101, 105), waist=(83, 87), shoulder=(44, 46)),
        GarmentSize(name="XL", chest=(106, 110), waist=(88, 92), shoulder=(46, 48)),
        GarmentSize(name="XXL", chest=(111, 116), waist=(93, 98), shoulder=(48, 50)),
    ],

    # 4️⃣ Casual Outerwear
    "casual_outerwear": [
        GarmentSize(name="XS", chest=(82, 86), waist=(64, 68), shoulder=(37, 39)),
        GarmentSize(name="S", chest=(88, 92), waist=(70, 74), shoulder=(39, 41)),
        GarmentSize(name="M", chest=(94, 98), waist=(76, 80), shoulder=(41, 43)),
        GarmentSize(name="L", chest=(100, 104), waist=(82, 86), shoulder=(43, 45)),
        GarmentSize(name="XL", chest=(106, 110), waist=(88, 92), shoulder=(45, 47)),
        GarmentSize(name="XXL", chest=(112, 116), waist=(94, 98), shoulder=(47, 49)),
        GarmentSize(name="3XL", chest=(118, 122), waist=(100, 104), shoulder=(49, 51)),
    ],

    # 5️⃣ Pyjama
    "pyjama": [
        GarmentSize(name="XS", waist=(73.7, 76.2)),
        GarmentSize(name="S", waist=(78.7, 81.3)),
        GarmentSize(name="M", waist=(83.8, 86.4)),
        GarmentSize(name="L", waist=(88.9, 91.4)),
        GarmentSize(name="XL", waist=(94, 96.5)),
        GarmentSize(name="XXL", waist=(99.1, 101.6)),
    ],

    # 6️⃣ Kurta
    "kurta": [
        GarmentSize(name="XS", chest=(82, 86), waist=(64, 68), shoulder=(37, 39)),
        GarmentSize(name="S", chest=(88, 92), waist=(70, 74), shoulder=(39, 41)),
        GarmentSize(name="M", chest=(94, 98), waist=(76, 80), shoulder=(41, 43)),
        GarmentSize(name="L", chest=(100, 104), waist=(82, 86), shoulder=(43, 45)),
        GarmentSize(name="XL", chest=(106, 110), waist=(88, 92), shoulder=(45, 47)),
        GarmentSize(name="XXL", chest=(112, 116), waist=(94, 98), shoulder=(47, 49)),
        GarmentSize(name="3XL", chest=(118, 122), waist=(100, 104), shoulder=(49, 51)),
    ],

    # 7️⃣ Vest
    "vest": [
        GarmentSize(name="S", waist=(80, 85)),
        GarmentSize(name="M", waist=(85, 90)),
        GarmentSize(name="L", waist=(90, 95)),
        GarmentSize(name="XL", waist=(95, 100)),
        GarmentSize(name="XXL", waist=(100, 105)),
        GarmentSize(name="3XL", waist=(105, 110)),
    ],

    # 8️⃣ Boxer
    "boxer": [
        GarmentSize(name="S", waist=(70, 75)),
        GarmentSize(name="M", waist=(75, 80)),
        GarmentSize(name="L", waist=(80, 85)),
        GarmentSize(name="XL", waist=(85, 95)),
        GarmentSize(name="XXL", waist=(95, 100)),
        GarmentSize(name="3XL", waist=(100, 105)),
    ]
}

MEASUREMENT_WEIGHTS = {
    "tshirt": {"chest": 0.4, "waist": 0.2, "shoulder": 0.4},
    "formal_shirt": {"chest": 0.35, "waist": 0.2, "shoulder": 0.45},
    "bottomwear": {"waist": 1.0},
    # ...
}