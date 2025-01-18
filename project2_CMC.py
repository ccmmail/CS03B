"""Seating Chart using arrays for Project 2."""

import numpy as np


def addStudent(name:str, seat_row:int, seat_col:int, seats:np.array) -> np.array:
    """Add student to seating chart, with the array index representing
    the assigned seat."""
    seats[seat_row][seat_col] = name
    return seats


def displaySeatingChart(seats:np.array):
    """Display seating chart in a human-readable format."""
    print("Seating chart:")
    for row in range(seats.size):
        for col in range(seats[row].size):
            print(seats[row][col], end="\t")
        print("\n")


def assignTeams(seats:np.array) -> np.array:
    """Assign students to teams based on seating assignment."""
    # initialize teams array with number of teams
    max_teams = max(row.size for row in seats)
    teams = np.empty(max_teams, dtype=object)
    for team in range(max_teams):
        teams[team] = np.array([], dtype=object)
    # transpose seat array into teams array
    for row in range(seats.size):
        for col in range(seats[row].size):
            teams[col] = np.append(teams[col], seats[row][col])
    return teams


def displayTeams(teams:np.array):
    """Display team number and members."""
    print("Team assignment:")
    for team in range(teams.size):
        print(f"Team {team}: ", end="\t")
        for member in range(teams[team].size):
            print(teams[team][member], end= "\t")
        print("\n")


def main():
    print("new run")
    seats = np.array(
        [np.array(["Alissa", "Betsy", "Charlie"], dtype=object),
                np.array(["Debbie", "Evan", "Fiona", "Gina"], dtype=object),
                np.array(["Henry", "Isabel", "Jaden"], dtype=object),
                np.array(["Kira", "Lisa", "Mack", "Nina", "Oscar", "Peter"], dtype=object),
                np.array(["Quincy", "Rita", "Sarah"], dtype=object),
                np.array(["Tom"], dtype=object)
               ], dtype=object)
    seats = addStudent("CHUNG", 0, 2, seats)
    displaySeatingChart(seats)
    teams = assignTeams(seats)
    displayTeams(teams)


if __name__ == "__main__":
    main()
