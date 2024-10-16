from .objects import Hotel
from . import db

def init_data():

    price = db.Column(db.Integer)

    event1 = Hotel(
        name="Grand Plaza Hotel", 
        description="Luxurious 5-star hotel with ocean views and top-notch amenities.", 
        price="250.0", 
        image="/assets/hotel_1.jpg", 
    )

    event2 = Hotel(
        name="City Central Inn", 
        description="Affordable and cozy hotel located in the heart of the city.", 
        price="85.0", 
        image="/assets/hotel_2.jpg", 
    )

    event3 = Hotel(
        name="Mountain Retreat Lodge", 
        description="Escape to the mountains with stunning views and tranquil surroundings.", 
        price="180.0", 
        image="/assets/hotel_3.jpg", 
    )

    event4 = Hotel(
        name="Beachside Resort", 
        description="Relax at a beachfront resort with private access to the white sand beach.", 
        price="220.0", 
        image="/assets/hotel_4.jpg", 
    )

    event5 = Hotel(
        name="Downtown Luxury Suites", 
        description="Modern luxury suites located near top restaurants and attractions.", 
        price="320.0", 
        image="/assets/hotel_5.jpg", 
    )

    event6 = Hotel(
        name="Historic Riverside Inn", 
        description="Charming hotel with historical significance, offering scenic river views.", 
        price="150.0", 
        image="/assets/hotel_6.jpg", 
    )




    db.session.add_all([event1, event2, event3, event4, event5, event6])
    db.session.commit()

    print("Database populated successfully!")