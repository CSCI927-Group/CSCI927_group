from .objects import Hotel
from . import db
from .init import init_data

def init_data():

    price = db.Column(db.Integer)

    event1 = Hotel(
        name="Grand Plaza Hotel", 
        description="Luxurious 5-star hotel with ocean views and top-notch amenities.", 
        price="250.0", 
        image="src/grand_plaza.jpg", 
    )

    event2 = Hotel(
        name="City Central Inn", 
        description="Affordable and cozy hotel located in the heart of the city.", 
        price="85.0", 
        image="src/city_central.jpg", 
    )

    event3 = Hotel(
        name="Mountain Retreat Lodge", 
        description="Escape to the mountains with stunning views and tranquil surroundings.", 
        price="180.0", 
        image="src/mountain_retreat.jpg", 
    )

    event4 = Hotel(
        name="Beachside Resort", 
        description="Relax at a beachfront resort with private access to the white sand beach.", 
        price="220.0", 
        image="src/beachside_resort.jpg", 
    )

    event5 = Hotel(
        name="Downtown Luxury Suites", 
        description="Modern luxury suites located near top restaurants and attractions.", 
        price="320.0", 
        image="src/downtown_luxury.jpg", 
    )

    event6 = Hotel(
        name="Historic Riverside Inn", 
        description="Charming hotel with historical significance, offering scenic river views.", 
        price="150.0", 
        image="src/riverside_inn.jpg", 
    )

    event7 = Hotel(
        name="Airport Express Hotel", 
        description="Conveniently located near the airport with free shuttle service.", 
        price="110.0", 
        image="src/airport_express.jpg", 
    )

    event8 = Hotel(
        name="Lakeside Cabins", 
        description="Rustic cabins by the lake, perfect for a peaceful weekend getaway.", 
        price="95.0", 
        image="src/lakeside_cabins.jpg", 
    )

    event9 = Hotel(
        name="The Royal Palace Hotel", 
        description="Experience royalty in this grand hotel with exquisite decor and service.", 
        price="400.0", 
        image="src/royal_palace.jpg", 
    )

    event10 = Hotel(
        name="Urban Oasis Hotel", 
        description="Boutique hotel offering a blend of modern design and natural elements.", 
        price="175.0", 
        image="src/urban_oasis.jpg", 
    )


    db.session.add_all([event1, event2, event3, event4, event5, event6, event7, event8, event9, event10])
    db.session.commit()

    print("Database populated successfully!")