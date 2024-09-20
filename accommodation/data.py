# Mock data for accommodations availability
accommodation_data = [
    {'date': 'September 20, 2024', 'available': True},
    {'date': 'September 21, 2024', 'available': False},  # Sold out
    {'date': 'September 22, 2024', 'available': True}
]

# Mock data for ratings and updates
news_data = {
    1: {
        'title': "Dreamwave Resort",
        'content': "Reviews: Absolutely stunning views and the staff were incredibly friendly. A perfect getaway!",
        'source': "AussieStay",
        'image': "https://via.placeholder.com/800x400",
        'Ratings': 'Rating: 5/5'
    },
    2: {
        'title': "Starview Grand Hotel",
        'content': "While the hotel is lovely, I expected more from the dining options. Still a nice stay!",
        'source': "DownUnderBookings",
        'image': "https://via.placeholder.com/800x400",
        'Ratings': 'Rating: 3/5'
    }
}

updates_data = {
    1: {
        'title': "Dreamwave Resort",
        'content': "The beach access was amazing! A few minor issues with the room, but overall a great stay.",
        'source': "DownUnderBookings",
        'image': "https://via.placeholder.com/800x400",
        'Ratings': 'Rating: 4/5'
    },
    2: {
        'title': "Green Haven Lodge",
        'content': "Beautiful surroundings and cozy cabins. Just wish there were more activities available.",
        'source': "OzTravelHub",
        'image': "https://via.placeholder.com/800x400",
        'Ratings': 'Rating: 4/5'
    }
}

# Mock booking data
bookings = {
    "sl923@uowmail.edu.au": [
        {"event": "Dreamwave Resort", "date": "September 25, 2024", "people": '2'},
        {"event": "Starview Grand Hotel", "date": "October 10, 2024", "people": '1'}
    ],
    "florayhua@outlook.com": [
        {"event": "Green Haven Lodge", "date": "October 1, 2024", "people": '1'}
    ]
}

# Mock event data
events = {
    1: {
        'title': 'Dreamwave Resort',
        'date': 'September 25, 2024',
        'description': 'Escape to Dreamwave Resort, where your perfect seaside getaway begins.',
        'image': 'https://via.placeholder.com/800x400'
    },
    2: {
        'title': 'Starview Grand Hotel',
        'date': 'October 1, 2024',
        'description': 'Experience unmatched luxury at Starview Grand Hotel, where every night is a starlit celebration.',
        'image': 'https://via.placeholder.com/800x400'
    },
    3: {
        'title': 'Green Haven Lodge',
        'date': 'October 10, 2024',
        'description': 'Discover tranquility at Green Haven Lodge, your sanctuary amidst nature.',
        'image': 'https://via.placeholder.com/800x400'
    }
}