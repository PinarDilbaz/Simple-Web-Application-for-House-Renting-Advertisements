from Database import Database


class RentDatabase(Database):
    def __init__(self):
        super().__init__()

    def addUser(self, param):
        query = ''' INSERT INTO user(username,password,fullname,email,phone,sessionId)
              VALUES(?,?,?,?,?,?) '''
        self.queryExecute(query, param)

    def addCity(self, param):
        query = ''' INSERT INTO city(cid,cname)
                      VALUES(?,?) '''
        self.queryExecute(query, param)

    def addHouse(self, param):
        query = ''' INSERT INTO house(street,noOfBedrooms,MonthlyFee,cityId)
                      VALUES(?,?,?,?) '''
        self.queryExecute(query, param)

    def addRent(self, param):
        query = ''' INSERT INTO rent(username,houseId)
                      VALUES(?,?) '''
        self.queryExecute(query, param)
