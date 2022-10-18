address_liste = [('Anrede', 'Vorname', 'Nachname', 'Straße', 'Hausnummer', 'PLZ', 'Ort', 'Telefonnummer', 'E-Mail'),
                 ('Herr', 'Tobias', 'Horn', 'Leipziger Str.', '50', '09111', 'Chemnitz', '0123456789',
                  'horn.tobias.teaching@gmail.com'),
                 ('Herr', 'Hans', 'Meisel', 'Berliner Str.', '76', '04123', 'Leipzig', '0987654321',
                  'hans.meisel@something.com'),
                 ('Frau', 'Maria', 'Ebert', 'Chemnitzer Str.', '26', '01217', 'Dresden', '0987651234',
                  'maria.ebert@something.com'),
                 ('Frau', 'Anna', 'Meinel', 'Kölner Str.', '33', '10243', 'Berlin', '0987612345',
                  'anna.meinel@something.com'),
                 ('Frau', 'Alexandra', 'Horn', 'Plauener Str.', '15', '08064', 'Zwickau', '0987123456',
                  'alexandra.horn@something.com'),
                 ('Herr', 'Tobias', 'Schulz', 'Dresdener Str.', '21', '08541', 'Plauen', '0567894321',
                  'tobias.schulz@something.com')
                 ]
all_dict = {}
headers = address_liste[0]
for i in range(1, len(address_liste)):
    address = address_liste[i]
    address_dict = {}
    for j in range(len(headers)):
        key = headers[j]
        value = address[j]
        address_dict[key] = value
    all_dict[i] = address_dict    
print("Complete dictionary:", all_dict)