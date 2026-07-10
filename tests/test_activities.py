def test_get_activities_returns_expected_structure(client):
    response = client.get("/activities")

    assert response.status_code == 200

    payload = response.json()
    assert "Chess Club" in payload

    chess_club = payload["Chess Club"]
    assert chess_club["description"] == "Learn strategies and compete in chess tournaments"
    assert chess_club["schedule"] == "Fridays, 3:30 PM - 5:00 PM"
    assert chess_club["max_participants"] == 12
    assert chess_club["participants"] == ["michael@mergington.edu", "daniel@mergington.edu"]


def test_get_activities_includes_all_seeded_activities(client):
    response = client.get("/activities")

    assert response.status_code == 200
    assert len(response.json()) == 9