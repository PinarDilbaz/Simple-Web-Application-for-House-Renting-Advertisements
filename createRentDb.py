from RentDatabase import RentDatabase


def main():
    db = RentDatabase()

    userTableQuery = """ CREATE TABLE IF NOT EXISTS user (
                                    username text PRIMARY KEY,
                                    password text NOT NULL,
                                    fullname text NOT NULL,
                                    email text NOT NULL,
                                    phone text NOT NULL,
                                    sessionId text NOT NULL
                                    ); """

    cityTableQuery = """ CREATE TABLE IF NOT EXISTS city (
                                    cid integer PRIMARY KEY,
                                    cname text NOT NULL
                                    ); """

    houseTableQuery = """ CREATE TABLE IF NOT EXISTS house (
                                    houseId integer PRIMARY KEY AUTOINCREMENT,
                                    street text NOT NULL,
                                    noOfBedrooms text NOT NULL,
                                    MonthlyFee text NOT NULL,
                                    cityId integer NOT NULL,
                                    FOREIGN KEY (cityId) REFERENCES city (cid)
                                    ); """

    rentTableQuery = """ CREATE TABLE IF NOT EXISTS rent (
                                    username text NOT NULL,
                                    houseId integer NOT NULL,
                                    FOREIGN KEY (username) REFERENCES user (username),
                                    FOREIGN KEY (houseId) REFERENCES house (houseId)
                                    ); """

    result = db.queryExecute(userTableQuery)
    print("user Table Created")
    result = db.queryExecute(cityTableQuery)
    print("city Table Created")
    result = db.queryExecute(houseTableQuery)
    print("house Table Created")
    result = db.queryExecute(rentTableQuery)
    print("rent Table Created")

    db.addCity([1, "Lefkosa"])
    db.addCity([2, "Girne"])
    db.addCity([3, "Gazi Magusa"])
    db.addCity([4, "Iskele"])
    db.addCity([5, "Guzelyurt"])
    db.addCity([6, "Lefke"])

    db.addUser(["ibo", "123", "ibrahim", "i@i.com", "111222", "-1"])
    db.addUser(["a", "a", "ab", "a@a.com", "131242", "-1"])
    db.addUser(["pinnos", "p", "Pınar", "p@a.com", "222222", "-1"])
    print("ok")
    db.addHouse(["a", "a", "a", 1])
    db.addHouse(["b", "b", "b", 1])
    db.addHouse(["c", "c", "c", 4])

    db.addRent(["a", 2])
    db.addRent(["ibo", 3])
    db.addRent(["pinnos", 4])


if __name__ == '__main__':
    main()
