import pytest
from reports.average_rating import generate

@pytest.fixture
def sample_data():
    return [
        {'name': 'iPhone', 'brand': 'Apple', 'price': '999', 'rating': '4.9'},
        {'name': 'Galaxy', 'brand': 'Samsung', 'price': '1199', 'rating': '4.8'},
        {'name': 'Redmi', 'brand': 'Xiaomi', 'price': '199', 'rating': '4.6'},
        {'name': 'iPad', 'brand': 'Apple', 'price': '799', 'rating': '4.7'},
    ]

def test_average_rating(sample_data):
    result = generate(sample_data)
    assert result[0]['brand'] == 'apple'
    assert result[0]['average_rating'] == 4.8
    assert len(result) == 3
