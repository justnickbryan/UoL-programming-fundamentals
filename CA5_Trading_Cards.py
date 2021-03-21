# Nicholas Bryan - 201531951
# COMP517 - CA5 Trading Cards

# import the openpyxl module for use in class methods
import openpyxl

class Card:
    """Card class defines characteristics of trading cards
    
    Attributes:
        _name (str): name of the card
        _cardType (str): each card is classified as one of the following types; "Magi", "Water", "Fire", "Earth", "Air", "Astral"
        _maxHP (int): maximum number of health points of the card
        _moves (:obj: 'list' of :obj: 'list' of :obj: 'str','int'): each card has between 1 and 5 moves
            the card's moves are stored in a list of lists as pairs of [moveName(str),damageFactor(int)]
        _shiny (boolean): a card can either be shiny (true), or not (false)
        _cardAverageDamage (float): average damage factor (to 1 decimal place) of the card's moves
    """ 

    def __init__(self, theName, theType, theHP, theMoves, isShiny):
        """Initialiser creates an instance of the Card class
        
        Args:
            theName (str): name of the card
            theType (str): card type
            theHP (int): max health points (HP) of the card
            theMoves (:obj: 'list' of :obj: 'list' of :obj: 'str','int'): a list of lists as pairs of [moveName(str),damageFactor(int)]
            isShiny (boolean): card is shiny (true), or not (false)
        """

        self._name = theName
        self._cardType = theType
        self._maxHP = theHP
        self._moves = theMoves
        self._shiny = isShiny
        
        # calculates the average damage of the cards moves
        cardDamageTotal = 0
        for move in self._moves:
            damageFactor = move[1]
            cardDamageTotal += damageFactor
        cardAverageDamage = cardDamageTotal / len(self._moves)
        
        self._cardAverageDamage = float("{:.1f}".format(cardAverageDamage))


    def __str__(self):
        """Returns string representation of a Card instance, giving the name, type, maxHP, shiny status, average damage and list of moves
                
        Returns:
            str: string representation of a Card instance
        """
        
        return "Card: {self._name}, Type: {self._cardType}, Max HP: {self._maxHP}, Shiny: {self._shiny}, Average Damage: {self._cardAverageDamage}, ...\n Moves: {self._moves}".format(self=self)


class Deck:
    """Deck class provides functionality for managing a deck of trading cards
    
    Attributes:
        _cardList (:obj: 'list' of :obj: 'Card'): a list of all the Card instances in the deck
        _totalCards (int): number of cards in the deck
        _totalShinys (int): number of shiny cards in the deck
        _averageDamage (float): average damage factor (to 1 decimal place) of all the cards in the deck
        _mostPowerful (:obj: 'Card'): the card in the deck with the highest average damage factor over the card's moves
        _deckNum (int): serial number assigned to the deck (counts number of deck instances)
    """

    # counts number of deck instances
    _deckCount = 0

    def __init__(self):
        """Initialiser creates an instance of the Deck class"""

        self._cardList = []
        
        self._totalCards = 0
        self._totalShinys = 0
        self._averageDamage = 0.0

        # increment _deckCount by 1 when new deck is initialised
        Deck._deckCount += 1
        self._deckNum = Deck._deckCount


    def __str__(self):
        """Returns string representation of a Deck instance, giving the number of the deck, number of cards, number of shiny cards and the average damage value over the entire deck
                
        Returns:
            str: string representation of a Deck instance
        """

        # get updated values of total cards, total shinys and the average damage of the deck
        self.getTotalCards()
        self.getTotalShinys()
        self.getAverageDamage()

        return "-- Deck {self._deckNum} --\n# of Cards: {self._totalCards}, # of Shiny's: {self._totalShinys}, Average Damage: {self._averageDamage}".format(self=self)


    def inputFromFile(self, fileName):
        """Populates initialised deck with (validated) trading card data from each row of an .xlsx file, using openpyxl module
        
        Args:
            fileName (str): name and file extension of the file containing data of trading cards, e.g. "<fileName>.xlsx"

        Raises:
            FileNotFoundError: if specified file cannot be found in directory
            TypeError: if invalid data type is given for fileName argument or for a cell value in card row
            ValueError: if incorrect number of moves have been assigned to a card (card must have between 1 and 5 moves)
            Exception: if file format or file type is incorrect, catches openpyxl error messages (may catch and print other unanticipated errors)
        """
        
        # tries to open file but raises error if file can't be found or not in correct format / file type for openpyxl module
        try:
            # opens Excel workbook and active sheet within the workbook
            deckFile = openpyxl.open(fileName)
            activeSheet = deckFile.active

            print("Deck {} data input from {}".format(self._deckNum, fileName))
            # iterates over all rows of spreadsheet, excluding row 1 (which contains the column headers), therefore rowCount starts at 1
            rowCount = 1
            for row in activeSheet.iter_rows(2):
                rowCount += 1
                 
                # movesList will be populated with all values for move name and damage factor in a single list
                movesList = []
                # theMoves will be populated with lists of [move name, damage factor]
                theMoves = []
                # instanceList will be populated with the validated card data from the row, so that a Card instance can be initialised
                instanceList = []

                # tries to add card data from row to instance list and then add to deck, but raises error and moves to next row if data is invalid
                try:    
                    # checks first cell of row in spreadsheet and raises type error if empty (because final row of sheet is always an empty row)
                    if row[0].value is None:
                        print("Empty cell in row {}, TypeError: row contains None value".format(rowCount))
                        raise TypeError
                    else:
                        # index of object in row collection is used to get cell values 
                        # name, type, HP and shiny status are all checked by method calls and assigned to variables if valid 
                        # rowCount is provided for ease of identification of errors in .xlsx file, if errors are raised during data check
                        theName = self.checkName(row[0].value, rowCount)
                        theType = self.checkCardType(row[1].value, rowCount)
                        theHP = self.checkHP(row[2].value, rowCount)
                        isShiny = self.checkShiny(row[3].value, rowCount)

                        # cellIndex is created and set to 4 as index of first object in row to contain move data
                        cellIndex = 4
                        # iterates over cells containing move data to populate movesList with move names and damage factors [moveName, damageFactor, moveName, damageFactor, ...]
                        for cellIndex in range(4,14):
                            # movesList can contain None values for now, to allow for empty cells at end of row when fewer than 5 moves
                            if row[cellIndex].value is None:
                                movesList.append(row[cellIndex].value)
                                cellIndex += 1
                            else:
                                # move names are in cells with even index number
                                if cellIndex % 2 == 0:
                                    # checks move name by method call and assigns to variable if valid 
                                    moveName = self.checkMoveName(row[cellIndex].value, rowCount)
                                    movesList.append(moveName)
                                    cellIndex += 1
                                # damage factors are in cells with odd index number
                                else:
                                    # checks damage factor by method call and assigns to variable if valid 
                                    damageFactor = self.checkDamageFactor(row[cellIndex].value, rowCount)
                                    movesList.append(damageFactor)
                                    cellIndex += 1

                        # iterates over objects in movesList to populate 'theMoves' with move names and damage factors [[moveName, damageFactor], [moveName, damageFactor], ...]
                        for i in range(0,5):
                            # creates empty list to hold each move's name and damage factor
                            move = []
                            # adds move name and damage factor pairs to move
                            move.append(movesList[2*i])
                            move.append(movesList[2*i+1])

                            # if neither the moveName nor the damageFactor are None, append the move to theMoves
                            if None not in move:
                                theMoves.append(move)
                            # if exclusively one of the moveName OR damageFactor is None, raise TypeError (row is not added a Card instance)
                            elif (move[0] is None and move[1] is not None) or (move[0] is not None and move[1] is None):
                                print("Empty cell in row {}, TypeError: row contains None value".format(rowCount))
                                raise TypeError
                            # if both moveName AND damageFactor are None then may have reached end of moves
                            # but continue through loop (in case of, for example, move 2 having been entered as move 3, leaving move 2 cells empty)
                            else:
                                continue
                    
                    # checks for correct number of moves in theMoves
                    if not 0 < len(theMoves) < 6:
                        print("'{}' moves in row {}, ValueError: number of moves must be between 1 and 5".format(len(theMoves), rowCount))
                        raise ValueError

                    # add all validated parameters to instanceList to be used as parameter in addCard function
                    instanceList.append(theName)
                    instanceList.append(theType)
                    instanceList.append(theHP)
                    instanceList.append(theMoves)
                    instanceList.append(isShiny)

                    # runs addCard method to add card for that row to the deck
                    self.addCard(instanceList)

                except TypeError:
                    continue

                except ValueError:
                    continue

                # if no errors are raised, confirms that card entry from row was valid
                else:
                    print("Row {} OK".format(rowCount))

        except FileNotFoundError:
            print("FileNotFoundError: {}".format(fileName))
        
        except TypeError:
            print("TypeError, invalid file name: {}".format(fileName))
        
        # catches and prints openpyxl filetype errors
        except Exception as exc:
            print(exc)


    def checkName(self, theName, rowCount):
        """Checks that the name entered as an argument for the instance of the Card class is of the correct data type, string
        
        Args:
            theName (str): name of the card from .xlsx sheet
            rowCount (int): row of .xlsx sheet being checked 

        Returns:
            theName (str): if the name is a string

        Throws:
            TypeError: if invalid data type is entered for an argument of the class instance
        """

        if type(theName) != str:
            print("'{}' in row {}, TypeError: Name must be a string".format(theName, rowCount))
            raise TypeError
        else:
            return theName    


    def checkCardType(self, theType, rowCount):
        """Checks that the card type entered as an argument for the instance of the Card class is one of the available types from a tuple of strings
        
        Args:
            theType (str): card type from .xlsx sheet
            rowCount (int): row of .xlsx sheet being checked 

        Returns:
            theType (str): if the type is valid

        Throws:
            TypeError: if invalid data type is entered for an argument of the class instance
        """

        # allowed Card types
        typeValidation = ("Magi", "Water", "Fire", "Earth", "Air", "Astral")

        if theType not in typeValidation:
            print("'{}' in row {}, TypeError: Type must be one of following: {}".format(theType, rowCount, typeValidation))
            raise TypeError
        else:
            return theType


    def checkHP(self, theHP, rowCount):
        """Checks that the max HP entered as an argument for the instance of the Card class is of the correct data type, integer
        
        Args:
            theHP (int): card max HP from .xlsx sheet
            rowCount (int): row of .xlsx sheet being checked 

        Returns:
            theHP (int): if the max HP is an integer

        Throws:
            TypeError: if invalid data type is entered for an argument of the class instance
        """
        
        if type(theHP) != int:
            print("'{}' in row {}, TypeError: HP must be an integer".format(theHP, rowCount))
            raise TypeError
        else:
            return theHP
            

    def checkShiny(self, isShiny, rowCount):
        """Checks that the shiny status entered as an argument for the instance of the Card class is of the correct data type, boolean
        
        Args:
            isShiny (boolean): shiny status of card from .xlsx sheet
            rowCount (int): row of .xlsx sheet being checked 
            
        Returns:
            isShiny (boolean): if the shiny status of the instance is valid

        Throws:
            TypeError: if invalid data type is entered for an argument of the class instance
        """
        
        if type(isShiny) != bool:
            if isShiny == 0:
                isShiny = False
                return isShiny
            elif isShiny == 1:
                isShiny = True
                return isShiny
            else:        
                print("'{}' in row {}, TypeError: Shiny status must be a boolean or a binary value".format(isShiny, rowCount))
                raise TypeError
        else:
            return isShiny   


    def checkMoveName(self, moveName, rowCount):
        """Checks that the move name entered for a move of the Card instance is of the correct data type, string
        
        Args:
            moveName (str): name of a move from .xlsx sheet
            rowCount (int): row of .xlsx sheet being checked 

        Returns:
            moveName (str): if name of move is a string

        Throws:
            TypeError: if invalid data type is entered
        """
        
        if type(moveName) != str:
            print("'{}' in row {}, TypeError: Move Name must be a string".format(moveName, rowCount))
            raise TypeError
        else:
            return moveName


    def checkDamageFactor(self, damageFactor, rowCount):
        """Checks that the damage factor entered for a move of the Card instance is of the correct data type, integer
        
        Args:
            damageFactor (int): damage of a move from .xlsx sheet
            rowCount (int): row of .xlsx sheet being checked 

        Returns:
            damageFactor (int): if damage of move is an int

        Throws:
            TypeError: if invalid data type is entered
        """
        
        if type(damageFactor) != int:
            print("'{}' in row {}, TypeError: Damage Factor must be an integer".format(damageFactor, rowCount))
            raise TypeError
        else:
            return damageFactor


    def addCard(self, theCard):
        """Adds the specified Card object or list of arguments (from inputFromFile) to initialise a Card instance to the Deck
        
        Args:
            theCard (:obj: 'Card', or :obj: 'list', or :obj: 'tuple')

        Raises:
            IndexError: if arguments for new card instance cannot be accessed by index
            TypeError: if theCard is not of the correct data type for creating new instance
        """

        # checks if theCard is an instance of the Card class
        if isinstance(theCard,Card):
            # if true, appends the card to the deck's cardList
            self._cardList.append(theCard)
        else:
            # if not an instance of the Card class, such as when inputting from .xlsx file, tries to initialise an instance taking arguments as collection objects
            try:
                newCard = Card(theCard[0], theCard[1], theCard[2], theCard[3], theCard[4])
                if isinstance(newCard,Card):
                    self._cardList.append(newCard)
            # raises IndexError if arguments for new card instance cannot be accessed by given indices
            except IndexError as iE:
                print("{} not added to deck {}:".format(theCard, self._deckNum), iE)
            # raises TypeError if theCard is not of the correct data type for creating new instance
            except TypeError as tE:
                print("{} not added to deck {}:".format(theCard, self._deckNum), tE)


    def rmCard(self, theCard):
        """Removes the specified Card from the Deck
        
        Args:
            theCard (:obj: 'Card')
        """
        
        # checks if theCard is an instance of the Card class
        if isinstance(theCard,Card):
            # checks if theCard instance is in the deck
            if theCard in self._cardList:
                self._cardList.remove(theCard)


    def getTotalCards(self):
        """Returns the total number of cards in the deck
        
        Returns:
            _totalCards (int): number of cards in the deck
        """
        
        # assigns the number of cards in the deck to _totalCards
        self._totalCards = len(self._cardList)
        return self._totalCards


    def getTotalShinys(self):
        """Returns the total number of shiny cards in the deck
        
        Returns:
            _totalShinys (int): number of shiny cards in the deck
        """

        # assigns number of shiny cards as 0 to _totalShinys
        self._totalShinys = 0
        
        # iterates over cards in the Deck (_cardList)
        for card in self._cardList:
            shiny = card._shiny
            # increments _totalShinys if card is shiny 
            if shiny:
                self._totalShinys += 1

        return self._totalShinys        


    def getMostPowerful(self):
        """Returns the most powerful card in the deck
        
        Returns:
            _mostPowerful (:obj: 'Card'): the card in the deck with the highest average damage factor over the card's moves
        """
        
        self._mostPowerful = None

        # if deck is not empty, iterates over cardList to find card with highest average damage
        if self._cardList != []:
            mostPowerfulAverageDamage = 0

            for card in self._cardList:
                cardAverageDamage = card._cardAverageDamage

                # compares the average damage of each card with the average damage of the most powerful card in the deck so far
                # if the current card is more powerful than the current most powerful, the current card is assigned as the most powerful  
                if cardAverageDamage > mostPowerfulAverageDamage:
                    self._mostPowerful = card
                    mostPowerfulAverageDamage = cardAverageDamage
                else:
                    continue
        
        return self._mostPowerful


    def getAverageDamage(self):
        """Returns the average damage of all of the cards in the deck
        
        Returns:
            _averageDamage (float): average damage factor (to 1 decimal place) of all the cards in the deck
        """
        
        self._averageDamage = 0.0

        # if deck is not empty, iterates over cardList to calculate the average damage of the deck
        if self._cardList != []:
            damageTotal = 0

            # adds the average damage of each card to damageTotal and divides this by the number of cards in the deck to find the average damage
            for card in self._cardList:
                cardAverageDamage = card._cardAverageDamage
                damageTotal += cardAverageDamage

            self._totalCards = len(self._cardList)
            averageDamage = damageTotal / self._totalCards
            self._averageDamage = float("{:.1f}".format(averageDamage))
        
        return self._averageDamage

    
    def viewAllCards(self):
        """Prints details of all of the cards in the deck"""
        
        print("-- Deck {} All Cards --".format(self._deckNum))
        if self._cardList != []:
            cardCount = 0
            for card in self._cardList:
                cardCount += 1
                print("{}.  {}".format(cardCount, card))
        else:
            print(None)


    def viewAllShinyCards(self):
        """Prints details of all of the shiny cards in the deck"""

        print("-- Deck {} Shiny Cards --".format(self._deckNum))
        if self._cardList != []:
            cardCount = 0
            for card in self._cardList:
                shiny = card._shiny
                if shiny:
                    cardCount += 1
                    print("{}.  {}".format(cardCount, card))
        else:
            print(None)


    def viewAllByType(self, theType):
        """Prints details of all of the cards that belong to the type specified as theType in the deck
        
        Args:
            theType (str): card type, one of the following: "Magi", "Water", "Fire", "Earth", "Air", "Astral"

        Raises:
            TypeError: if invalid type is entered as theType
        """

        # allowed Card types
        typeValidation = ("Magi", "Water", "Fire", "Earth", "Air", "Astral")

        try:
            if theType not in typeValidation:
                raise TypeError
            else:        
                print("-- Deck {} {} Cards --".format(self._deckNum, theType))
                if self._cardList != []:
                    cardCount = 0
                    for card in self._cardList:
                        cardType = card._cardType
                        if cardType == theType:
                            cardCount += 1
                            print("{}.  {}".format(cardCount, card))
                else:
                    print(None)
        except TypeError:
            print("'{}', TypeError: Type must be one of following: {}".format(theType, typeValidation))


    def getCards(self):
        """Returns a collection of all Cards in the Deck

        Returns:
            _cardList (:obj: 'list' of :obj: 'Card'): a list of all the Card instances in the deck
        """

        return self._cardList


    def saveToFile(self, fileName):
        """Populates and saves an .xlsx file with details of all cards currently in the deck, using openpyxl module
        
        Args:
            fileName (str): name and file extension of the file to be saved with data of trading cards, e.g. "<fileName>.xlsx"

        Raises:
            AttributeError: if fileName is not a datatype executable by openpyxl (should be a string in format "<fileName>.xlsx")
        """
        
        # opens new Excel workbook and active sheet
        deckFile = openpyxl.Workbook()
        activeSheet = deckFile.active

        # add column headers as first row
        headerRow = ("Name", "Type", "HP", "Shiny", "Move Name 1", "Damage 1", "Move Name 2", "Damage 2", "Move Name 3", "Damage 3", "Move Name 4", "Damage 4", "Move Name 5", "Damage 5")
        activeSheet.append(headerRow)

        # for each card in the deck: gets attributes, adds attributes to a list, appends list of attributes as a row in the sheet
        for card in self._cardList:

            name = card._name
            cardType = card._cardType
            maxHP = card._maxHP
            shiny = card._shiny
            moves = card._moves

            rowList = [name, cardType, maxHP, shiny]

            for move in moves:
                for i in move:
                    rowList.append(i)

            activeSheet.append(rowList)
        
        # tries to save file to fileName, but raises error if fileName is not executable by openpyxl
        try:
            deckFile.save(fileName)
            print("Deck {} saved as: {}".format(self._deckNum, fileName))
        except AttributeError as error:
            print("File not saved:", error)


# use main() method to test code
def main():
    print("This script has been run in the source file")
    deck1 = Deck()
    deck1.inputFromFile('sampleDeck.xlsx')
    print(deck1) #expecting __str__ of deck with total 6 cards and 2 shinys
    cardCollection = deck1.getCards() #expecting list of all card objects (only if printed)
    print(cardCollection)
    deck1.viewAllCards() #expecting details of each card to be printed
    deck1.viewAllShinyCards() #expecting details of Magius and Gogrin to be printed
    deck1.viewAllByType("Water") #expecting details of Burkax, Gogrin and Sygniwr to be printed
    mostPowerful = deck1.getMostPowerful()
    print("Most Powerful:", mostPowerful) #expecting Abnorms
    deck1.rmCard(cardCollection[2]) #expecting Magius to be removed
    deck1.saveToFile('sampleDeckNoMagius.xlsx')
    deck1.rmCard(cardCollection[1]) #expecting Abnorms to be removed
    print(deck1) #expecting __str__ of deck with total 5 cards and 1 shiny
    print("Most Powerful:", deck1.getMostPowerful()) #expecting Burkax
    deck1.saveToFile('sampleDeckNoAbnorms.xlsx')    
    deck1.inputFromFile('badDeck.xlsx')
    deck1.inputFromFile('conca.xls')
    print(deck1)

# only runs test code if file has not been imported
if __name__ == "__main__":
    main()