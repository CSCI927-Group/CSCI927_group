# Mock data for ticket availability
ticket_data = [
    {'date': 'September 20, 2024', 'available': True},
    {'date': 'September 21, 2024', 'available': False},  # Sold out
    {'date': 'September 22, 2024', 'available': True}
]

# Mock data for news and updates
news_data = {
    1: {
        'title': "Amazing moment zoo sets free 49 of Australia’s rarest birds",
        'content': "There are fewer than 300 of the once common songbirds left in the wild...",
        'source': "Yahoo News Australia",
        'image': "https://via.placeholder.com/800x400",
        'read_time': '2-min read'
    },
    2: {
        'title': "Meteorite discovery upends our understanding of life on Earth",
        'content': "A mysterious crater pattern on the Earth's surface led scientists...",
        'source': "Yahoo News Australia",
        'image': "https://via.placeholder.com/800x400",
        'read_time': '2-min read'
    }
}

updates_data = {
    1: {
        'title': "Road closures in the city for maintenance",
        'content': "Key streets will be closed for repair work over the next weekend...",
        'source': "City of Sydney",
        'image': "https://via.placeholder.com/800x400",
        'read_time': '3-min read'
    },
    2: {
        'title': "Public park renovation completion delayed",
        'content': "Due to unforeseen circumstances, the public park renovation...",
        'source': "City of Sydney",
        'image': "https://via.placeholder.com/800x400",
        'read_time': '4-min read'
    }
}

# Mock booking data
bookings = {
    "xh992@uowmail.edu.au": [
        {"event": "Concert at Central Park", "date": "September 25, 2024", "tickets": 2},
        {"event": "Art Exhibition", "date": "October 10, 2024", "tickets": 1}
    ],
    "heyinwong992@gmail.com": [
        {"event": "Food Festival", "date": "October 1, 2024", "tickets": 4}
    ]
}

# Mock event data
events = {
    1: {
        'title': 'Concert at Central Park',
        'date': 'September 25, 2024',
        'description': 'Enjoy a live concert in the heart of Central Park featuring popular bands and artists.',
        'image': 'https://via.placeholder.com/800x400'
    },
    2: {
        'title': 'Food Festival',
        'date': 'October 1, 2024',
        'description': 'A celebration of culinary arts with food trucks, chefs, and a variety of delicious foods.',
        'image': 'https://via.placeholder.com/800x400'
    },
    3: {
        'title': 'Art Exhibition',
        'date': 'October 10, 2024',
        'description': 'Discover modern and contemporary art at the city\'s largest art exhibition.',
        'image': 'https://via.placeholder.com/800x400'
    }
}