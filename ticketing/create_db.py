from app import db, app, Event, Ticketing, EventUpdate

with app.app_context():

    db.create_all()


    event1 = Event(
        title="Concert at Central Park", 
        description="Enjoy a live concert in Central Park.", 
        date="September 25, 2024", 
        image="src/concert.jpg", 
        additional_info="This year's Central Park concert features an exciting lineup of artists, including local bands and famous headliners. Food and drinks will be available at various stalls. Attendees are advised to arrive by 8:00 AM for the best spots."
    )

    event2 = Event(
        title="Food Festival", 
        description="A celebration of culinary arts.", 
        date="October 1, 2024", 
        image="src/food.jpg", 
        additional_info="Taste food from around the world at the annual food festival. Over 50 food vendors will offer exclusive dishes. Join us for live cooking demos and competitions! Family-friendly activities will also be available throughout the day."
    )

    event3 = Event(
        title="Art Exhibition", 
        description="Discover modern art.", 
        date="October 10, 2024", 
        image="src/art.jpg", 
        additional_info="The Art Exhibition will display work from renowned artists, focusing on modern and contemporary art styles. Attend talks by the artists themselves and gain insight into their creative process. Open to all art enthusiasts and collectors."
    )

    event4 = Event(
        title="Jazz Night", 
        description="Live jazz performance in the city.", 
        date="October 5, 2024", 
        image="src/jazz.jpg", 
        additional_info="Experience the smooth rhythms of Jazz Night in the heart of the city. Featuring performances by up-and-coming jazz musicians, this night will be unforgettable. The show starts at 7:00 PM, and tickets are selling fast."
    )

    event5 = Event(
        title="Theatre Play", 
        description="Watch a classic theatre performance.", 
        date="October 15, 2024", 
        image="src/theatre.jpg", 
        additional_info="Join us for an unforgettable theatre performance of a classic play. The performance will be held in the newly renovated city theatre. Doors open at 6:00 PM, and seating is first-come, first-served. Bring your family and friends!"
    )

    db.session.add_all([event1, event2, event3, event4, event5])
    db.session.commit()


    ticket1 = Ticketing(event_id=event1.id, date="September 25, 2024", time_slot="09:00 - 10:00", available_tickets=50)
    ticket2 = Ticketing(event_id=event1.id, date="September 25, 2024", time_slot="10:00 - 11:00", available_tickets=0)
    ticket3 = Ticketing(event_id=event1.id, date="September 25, 2024", time_slot="12:00 - 13:00", available_tickets=10)

    ticket4 = Ticketing(event_id=event2.id, date="October 1, 2024", time_slot="09:00 - 10:00", available_tickets=100)
    ticket5 = Ticketing(event_id=event2.id, date="October 1, 2024", time_slot="14:00 - 15:00", available_tickets=50)

    ticket6 = Ticketing(event_id=event3.id, date="October 10, 2024", time_slot="09:00 - 10:00", available_tickets=75)
    ticket7 = Ticketing(event_id=event3.id, date="October 10, 2024", time_slot="11:00 - 12:00", available_tickets=60)

    ticket8 = Ticketing(event_id=event4.id, date="October 5, 2024", time_slot="20:00 - 21:00", available_tickets=120)

    ticket9 = Ticketing(event_id=event5.id, date="October 15, 2024", time_slot="14:00 - 15:00", available_tickets=80)
    ticket10 = Ticketing(event_id=event5.id, date="October 15, 2024", time_slot="19:00 - 20:00", available_tickets=0)

    db.session.add_all([ticket1, ticket2, ticket3, ticket4, ticket5, ticket6, ticket7, ticket8, ticket9, ticket10])
    db.session.commit()

 
    news1 = EventUpdate(
        type="news", 
        event_id=event1.id, 
        title="Concert at Central Park - Pre-event notice", 
        content="The concert will begin at 9 AM. Please arrive early to avoid traffic delays. Gates will open at 8 AM, and seating is first-come, first-served.", 
        date="September 20, 2024", 
        source="BCD News", 
        image="src/concert.jpg", 
        read_time="2 min"
    )

    news2 = EventUpdate(
        type="news", 
        event_id=event2.id, 
        title="Food Festival - Vendor list announced", 
        content="The list of vendors participating in this year's food festival has been officially released. Check out the international cuisines on offer.", 
        date="September 27, 2024", 
        source="Festival Notice", 
        image="src/food.jpg", 
        read_time="3 min"
    )

    news3 = EventUpdate(
        type="news", 
        event_id=event3.id, 
        title="Art Exhibition Opening Ceremony", 
        content="The highly anticipated Art Exhibition will officially open on October 10th. The ceremony will feature keynotes from renowned artists.", 
        date="October 5, 2024", 
        source="Art Gallery", 
        image="src/art.jpg", 
        read_time="4 min"
    )
    update1 = EventUpdate(
        type="update", 
        event_id=event1.id, 
        title="Road closures for concert", 
        content="Several roads around Central Park will be closed between 6 AM and 12 PM to accommodate the large crowd expected for the concert.", 
        date="September 22, 2024", 
        source="Event Center", 
        image="src/concert.jpg", 
        read_time="3 min"
    )

    update2 = EventUpdate(
        type="update", 
        event_id=event2.id, 
        title="Food Festival entry passes", 
        content="Entry passes are required for the food festival. Please ensure you have your pass printed or available on your mobile device for scanning at the entrance.", 
        date="September 29, 2024", 
        source="Event Center", 
        image="src/food.jpg", 
        read_time="2 min"
    )

    update3 = EventUpdate(
        type="update", 
        event_id=event4.id, 
        title="Jazz Night timing update", 
        content="Due to scheduling conflicts, Jazz Night will start at 8 PM instead of 7 PM. Please plan accordingly to enjoy the full performance.", 
        date="October 3, 2024", 
        source="Music of the Night", 
        image="src/jazz.jpg", 
        read_time="1 min"
    )
    db.session.add_all([news1, news2, news3, update1, update2, update3])
    db.session.commit()

    print("Database populated successfully!")