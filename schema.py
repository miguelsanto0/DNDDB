sql_create_players_table = """
CREATE TABLE IF NOT EXISTS Players (
    PlayerID INT AUTO_INCREMENT PRIMARY KEY,
    PlayerName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL
);
"""

sql_create_races_table = """
CREATE TABLE IF NOT EXISTS Races (
    RaceID INT AUTO_INCREMENT PRIMARY KEY,
    RaceName VARCHAR(255) NOT NULL,
    Speed INT,
    Size VARCHAR(50),
    AbilityScoreImprovements VARCHAR(255),
    Traits TEXT
);
"""

sql_create_classes_table = """
CREATE TABLE IF NOT EXISTS Classes (
    ClassID INT AUTO_INCREMENT PRIMARY KEY,
    ClassName VARCHAR(255) NOT NULL,
    HitDie VARCHAR(50),
    PrimaryAbility VARCHAR(255),
    Saves VARCHAR(255)
);
"""

sql_create_characters_table = """
CREATE TABLE IF NOT EXISTS Characters (
    CharacterID INT AUTO_INCREMENT PRIMARY KEY,
    PlayerID INT,
    Name VARCHAR(255) NOT NULL,
    RaceID INT,
    ClassID INT,
    Level INT,
    Background VARCHAR(255),
    Alignment VARCHAR(50),
    ExperiencePoints INT,
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID),
    FOREIGN KEY (RaceID) REFERENCES Races(RaceID),
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID)
);
"""

sql_create_spells_table = """
CREATE TABLE IF NOT EXISTS Spells (
    SpellID INT AUTO_INCREMENT PRIMARY KEY,
    SpellName VARCHAR(255) NOT NULL,
    Level INT,
    CastingTime VARCHAR(100),
    Range VARCHAR(100),
    Components VARCHAR(255),
    Duration VARCHAR(100),
    Description TEXT
);
"""

sql_create_character_spells_table = """
CREATE TABLE IF NOT EXISTS CharacterSpells (
    CharacterID INT,
    SpellID INT,
    FOREIGN KEY (CharacterID) REFERENCES Characters(CharacterID),
    FOREIGN KEY (SpellID) REFERENCES Spells(SpellID),
    PRIMARY KEY (CharacterID, SpellID)
);
"""

sql_create_inventory_table = """
CREATE TABLE IF NOT EXISTS Inventory (
    InventoryID INT AUTO_INCREMENT PRIMARY KEY,
    CharacterID INT,
    ItemName VARCHAR(255) NOT NULL,
    Quantity INT,
    Weight DECIMAL(10,2),
    Description TEXT,
    FOREIGN KEY (CharacterID) REFERENCES Characters(CharacterID)
);
"""

sql_create_classes_spells_table = """
CREATE TABLE IF NOT EXISTS ClassesSpells (
    ClassID INT,
    SpellID INT,
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID),
    FOREIGN KEY (SpellID) REFERENCES Spells(SpellID),
    PRIMARY KEY (ClassID, SpellID)
);
"""

def get_dnd_schema():
    schema = (
        sql_create_players_table +
        sql_create_races_table +
        sql_create_classes_table +
        sql_create_characters_table +
        sql_create_spells_table +
        sql_create_character_spells_table +
        sql_create_inventory_table +
        sql_create_classes_spells_table
    )
    return schema
