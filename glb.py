###VARIALBES
MOVIENAME='Mad Max Fury Road'
APIKEY='5b248f61321474b5f3e42b34ac06d315'
departments=['Sound','Camera','Costume & Make-Up','Crew','Directing','Writing','Visual Effects','Production','Art','Editing']
genres=['Action','Adventure','Animation','Comedy','Crime','Documentary','Drama','Family','Fantasy','Foreign','History','Horror','Music','Mystery','Romance','Science Fiction','TV movie','Thriller','War','Western']
productionCompaniesPopluate=[]
genreTest=[]
movieNameList=[u"Who's Your Caddy?\n", u'Son of the Mask\n', u'Troll 2\n', u'Gigli\n', u'BloodRayne\n', u'You Got Served\n', u'Barb Wire\n', u'Catwoman\n', u'Superman IV: The Quest for Peace\n', u'Batman & Robin\n', u'Police Academy 5: Assignment: Miami Beach\n', u'The Wicker Man\n', u'Dungeons & Dragons\n', u'In the Name of the King: A Dungeon Siege Tale\n', u'Bio-Dome\n', u'Basic Instinct 2\n', u'On Deadly Ground\n', u'Halloween III: Season of the Witch\n', u'The Adventures of Rocky & Bullwinkle\n', u'The Karate Kid, Part III\n', u'The Last Airbender\n', u'Skyline\n', u"Freddy's Dead: The Final Nightmare\n", u'Dr. Dolittle 2\n', u'Jonah Hex\n', u'Envy\n', u'Miss Congeniality 2: Armed & Fabulous\n', u'Flubber\n', u"Charlie's Angels: Full Throttle\n", u'The Covenant\n', u'The Haunted Mansion\n', u'Cold Creek Manor\n', u'Queen of the Damned\n', u'Elektra\n', u'The Dukes of Hazzard\n', u'Shutter\n', u'An American Haunting\n', u'An American Werewolf in Paris\n', u'The Specialist\n', u'Little Nicky\n', u'Masters of the Universe\n', u'Star Trek V: The Final Frontier\n', u'Beverly Hills Cop III\n', u'Raw Deal\n', u'The Tuxedo\n', u'Scary Movie 4\n', u'Johnny Mnemonic\n', u'The Hills Have Eyes II\n', u'Loser\n', u'Agent Cody Banks\n', u'Pathfinder\n', u'Beethoven\n', u'Collateral Damage\n', u'Urban Legend\n', u'American Pie Presents Beta House\n', u'Dracula: Dead and Loving It\n', u'The Ten\n', u'Children of the Corn\n', u'Hollywood Homicide\n', u'Bulletproof Monk\n', u'The Pacifier\n', u'Volcano\n', u'Forces of Nature\n', u'The Bonfire of the Vanities\n', u'Virtuosity\n', u'Timeline\n', u'Little Fockers\n', u'Ghost Ship\n', u'Paul Blart: Mall Cop\n', u'The Skulls\n', u'Kicking & Screaming\n', u'Drumline\n', u'AVP: Alien vs. Predator\n', u'White Noise\n', u'I Know What You Did Last Summer\n', u'Conan the Destroyer\n', u'Alvin and the Chipmunks\n', u'Bubble Boy\n', u'12 Rounds\n', u'John Tucker Must Die\n', u"Charlie's Angels\n", u'Nine 1/2 Weeks\n', u'Made of Honor\n', u'Perfect Stranger\n', u'The Art of War\n', u'Passenger 57\n', u'Turner & Hooch\n', u'Wrong Turn 2: Dead End\n', u'Analyze That\n', u'The Postman\n', u'Mr. Deeds\n', u'Men in Black II\n', u'Bridget Jones: The Edge of Reason\n', u'Space Jam\n', u'Jaws 2\n', u'Universal Soldier\n', u'The Legend of Zorro\n', u'Jurassic Park III\n', u'1941\n', u'Into the Blue\n', u'Win a Date with Tad Hamilton!\n', u'Mercury Rising\n', u'Johnny English\n', u'The Amityville Horror\n', u'The 6th Day\n', u'A Night at the Roxbury\n', u'Sweet Home Alabama\n', u'Waterworld\n', u'Chicken Little\n', u'Multiplicity\n', u'Georgia Rule\n', u'Black Sheep\n', u'Stick It\n', u'Reign of Fire\n', u'Murder by Numbers\n', u'The Replacement Killers\n', u"The Devil's Own\n", u'Addicted to Love\n', u'Bring It On\n', u'The Money Pit\n', u'Disclosure\n', u'The Cable Guy\n', u'Diary of the Dead\n', u'Dear John\n', u'Sahara\n', u'The Brothers Grimm\n', u'Thick as Thieves\n', u'Tango & Cash\n', u'Clash of the Titans\n', u'Walking Tall\n', u'Scary Movie\n', u'Green Card\n', u'The Invasion\n', u'The Ruins\n', u'Forever Young\n', u'Nine\n', u"All the King's Men\n", u'Die Another Day\n', u'The Dead Pool\n', u'Dinner for Schmucks\n', u'Piranha\n', u'Two for the Money\n', u'Cannibal Holocaust\n', u'War\n', u'Inkheart\n', u'Armageddon\n', u"One Night at McCool's\n", u'Punisher: War Zone\n', u'Big Daddy\n', u'The Nanny Diaries\n', u'Entrapment\n', u'Shrek the Third\n', u'American Wedding\n', u"Ocean's Twelve\n", u'The Adventures of Buckaroo Banzai Across the 8th Dimension\n', u'The Texas Chainsaw Massacre\n', u'Planet 51\n', u'*batteries not included\n', u'I Now Pronounce You Chuck & Larry\n', u'Starsky & Hutch\n', u'Beverly Hills Cop II\n', u'The Rocketeer\n', u'Once Upon a Time in Mexico\n', u'So I Married an Axe Murderer\n', u'Barbershop\n', u'Instinct\n', u'Kate & Leopold\n', u"Mr. Magorium's Wonder Emporium\n", u'Now and Then\n', u'Sydney White\n', u'The River Wild\n', u'The Siege\n', u'Tin Cup\n', u'Arachnophobia\n', u'The 51st State\n', u'Always\n', u'The Perfect Storm\n', u'Heartbreakers\n', u'Solomon Kane\n', u'Life as We Know It\n', u'Crash\n', u'The Ice Harvest\n', u'The Replacements\n', u'Lions for Lambs']

#movieNameList=[u'Problem Child 3: Junior in Love', u'Spice World', u'Glitter', u'Disaster Movie', u'Home Alone 4', u'Ernest Scared Stupid', u'Baby Geniuses', u'Ernest Goes to School', u'2001: A Space Travesty', u'Gulle      Minnaar', u'Ernest Goes to Camp', u'Crocodile', u'Barb Wire', u'Silenzio dei Prosciutti', u'Revenge of the Nerds IV: Nerds in Love', u'Return of the Texas Chainsaw Massacre', u'Ernest Goes to Jail', u'Son of the Mask', u'Battlefield Earth: A Saga of the Year 3000', u'Death Tunnel', u'Scary MoVie', u'Ernest Saves Christmas', u'Revenge of the Nerds III: The Next Generation', u'Beowulf', u'Police Academy: Mission to Moscow', u'Problem Child 2', u'Super Mario Bros.', u'Dumb and Dumberer: When Harry Met Lloyd', u'Vampires Suck', u"Beethoven's 3rd", u'Honey', u' We Shrunk Ourselves', u'Cop and 1/2', u'Feestje!', u'Mr. Magoo', u'Epic Movie', u'Volle Maan', u'Alone in the Dark', u'Deep Throat', u'Honneponnetje', u'Shriek If You Know What I Did Last Friday the Thirteenth', u'Meet the Spartans', u'Honey', u' I Blew Up the Kid', u'Jaws: The Revenge', u'Dance Flick', u'Gigli', u'Return to the Blue Lagoon', u'Next Karate Kid', u' The', u"Look Who's Talking Too", u'Police Academy 6: City under Siege', u'Stop! Or My Mom Will Shoot', u'Jaws 3-D', u'Avengers', u'Adventures of Pluto Nas', u'Piranha Part Two: The Spawning', u'Troop Beverly Hills', u"Look Who's Talking Now", u'Flintstones in Viva Rock VegasSpion van Oranje', u'Grease 2', u'Dragonball Evolution', u'Stan Helsing', u'Repossessed', u'Police Academy 5: Assignment: Miami Beach', u'From Dusk till Dawn 2: Texas Blood Money', u'American Psycho II: All American Girl', u'Inspector Gadget', u'3 Men and a Little Lady', u'Mortal Kombat: Annihilation', u"Who's That Girl?", u'Island of Dr. Moreau', u' The', u'Problem Child', u'Crossroads', u'Bombardement', u' Het', u'Thunderbirds', u"Porky's II: The Next Day", u"Porky's Revenge", u"I'll Always Know What You Did Last Summer", u'Home Alone 3', u'Junior', u'6Date Movie', u'RoboCop 3', u'Coneheads', u'Beverly Hillbillies', u' The', u'Street Fighter', u'Book of Shadows: Blair Witch 2', u'Dungeons & Dragons', u'Floris', u"Beethoven's 2nd", u'Revenge of the Nerds II: Nerds in Paradise', u'Foreigner', u' The', u'Suske en Wiske: De Duistere Diamant', u'Urban Legends: Final Cut', u'Hottie and the Nottie', u' The', u'Costa!', u'Highlander III: The Sorcerer', u'Jack and Jill']

#movieNameList=['The Karate Kid', 'Carlitos Way', 'Gremlins', 'The Lost Boys', 'Coming to America', 'Under Siege', 'Sherlock Holmes', 'Lara Croft: Tomb Raider', 'The Deer Hunter', '1941', 'Alien: Resurrection', 'A Bridge Too Far', 'Dances with Wolves', 'From Dusk Till Dawn', 'Hancock', 'Blade', 'Back to the Future', 'Alice in Wonderland', 'Tequila Sunrise', 'Blade Runner', 'Stargate', 'Private School', '12 Years a Slave', 'Big Trouble in Little China', 'The Sixth Sense', 'Tender Cousins', 'Hercules', 'Caligula', 'Psycho', 'RoboCop', 'The Green Mile', 'Rain Man', 'First Blood', 'The Truman Show', 'The Name of the Rose', 'Ferris Buellers Day Off', 'Annie Hall', 'Rambo III', 'Total Recall', 'Suspiria', 'Die Hard 2', 'Austin Powers: The Spy Who Shagged Me', 'Ace Ventura: When Nature Calls', 'Heat', 'Star Wars: Episode V - The Empire Strikes Back', 'American Psycho', 'Twilight', ' Inc.', 'Me', 'Blue Lagoon: The Awakening', 'I Am Legend', 'One Flew Over the Cuckoos Nest', 'National Treasure', 'Contact', 'Tangled', 'Trainspotting', 'We Were Soldiers', 'The Matrix Reloaded', 'Taken 2', 'Indiana Jones and the Last Crusade', 'Apollo 13', 'Hair', 'The Incredibles', 'Ice Age', 'Lethal Weapon 3', 'Lethal Weapon 2', 'Poltergeist', 'The Reef', 'All Ladies Do It', 'Despicable Me', 'The Golden Child', 'Theres Something About Mary', 'The Fifth Element', 'The Hangover', 'Jurassic Park', 'Event Horizon', 'Batman Returns', 'The Running Man', 'The Shining', 'Terminator 3: Rise of the Machines', 'Midnight Express', 'Face/Off', 'The Many Adventures of Winnie the Pooh', 'The Enforcer', 'Blade II', 'Revenge of the Pink Panther', 'The Texas Chain Saw Massacre', 'Daybreakers', 'Evil Dead II', 'Mad Max 2: The Road Warrior', 'The Fog', 'Seventh Son', 'Crime Busters', 'Out of Africa', 'On Her Majestys Secret Service', 'Chicken Run', 'Full Metal Jacket', 'Iron Man 2', 'Iron Man 3', 'Toy Story 2', 'Toy Story 3', 'Top Gun', 'Die Hard: With a Vengeance', 'E.T. the Extra-Terrestrial', 'Pans Labyrinth', 'Octopussy', 'Home Alone 2: Lost In New York', 'Beauty and the Beast', 'Rocky IV', 'Shaolin Soccer', 'The Princess Bride', 'The Visitors', 'Star Wars: Episode III - Revenge of the Sith', 'Rocky II', 'Eternal Sunshine of the Spotless Mind', 'Memento', 'Wild Things', 'Spring Breakers', 'Sudden Impact', 'The Hunger Games: Mockingjay - Part 1', 'Kramer vs. Kramer', 'Birdman', 'The Little Mermaid', 'Elysium', 'Damien: Omen II', 'The Mask', 'Shrek', 'Spaceballs', 'Fantastic Four', 'WALLE', 'The Pianist', 'Fury', 'Childs Play 2', 'Sphere', 'Night at the Museum', 'An Officer and a Gentleman', 'Red Heat', 'Saturday Night Fever', 'Last Action Hero', 'Iron Man', 'The Great Escape', 'Life of Brian', 'Charlie and the Chocolate Factory', 'Cowboys & Aliens', 'Stand by Me', 'The Money Pit', 'Big Hero 6', 'The Da Vinci Code', 'A Nightmare on Elm Street', 'Prometheus', 'The Ring', '2012', 'The War of the Roses', 'The Wolf of Wall Street', 'The Boat That Rocked', 'City of the Living Dead', 'Friday the 13th Part 2', 'Gandhi', 'Star Trek', 'Scream', 'Sal', 'Aliens', 'National Lampoons Vacation', 'The Naked Gun 2: The Smell of Fear', 'The Lion King', 'Network', 'Slumdog Millionaire', 'The Lost World: Jurassic Park', 'Nice Dreams', 'Toy Story', 'American Pie', 'Escape from Alcatraz', 'Moonraker', 'Babe', 'Harry Potter and the Philosophers Stone', 'xXx: State of the Union', 'Ghostbusters', 'Aladdin and the King of Thieves', 'Night at the Museum: Secret of the Tomb', 'The NeverEnding Story II: The Next Chapter', 'The Maze Runner', 'Mad Max: Fury Road', 'Star Wars: Episode I - The Phantom Menace', 'Mission: Impossible III', 'An American Tail', 'Rambo: First Blood Part II', 'Mission: Impossible', 'Star Trek: The Motion Picture', 'Unbreakable', 'Whiplash', 'DragonHeart', 'The Gift', 'Brazil', 'Reservoir Dogs', 'The Breakfast Club', 'The Last Emperor', 'Shark Tale', 'The Evil Dead', 'Romeo + Juliet', 'Monsters', 'Firestarter', 'The Big Lebowski', 'Pulp Fiction', 'Mission: Impossible - Ghost Protocol', 'V for Vendetta', 'The Hobbit: An Unexpected Journey', 'The Bourne Ultimatum', 'The Great Mouse Detective', 'Step Up', 'Gravity', 'It Follows', 'Serenity', '48 Hrs.', 'The Aristocats', 'Dumb and Dumber To', 'Dantes Peak', '10', 'Charlies Angels', 'Batman Begins', 'Kickboxer', 'Harry Potter and the Chamber of Secrets', 'Gladiator', 'The Rock', 'Appleseed Saga: Ex Machina', 'Oldboy', 'The Godfather: Part II', 'Black Swan', 'Philadelphia', 'Se7en', 'Pirates of the Caribbean: On Stranger Tides', '2 Guns', 'The Lion King 2: Simbas Pride', 'Oceans Eleven', 'Twelve Monkeys', 'Rocky V', 'Showgirls', 'The Usual Suspects', 'Pirates of the Caribbean: At Worlds End', 'Stalingrad', 'Harry Potter and the Order of the Phoenix', 'Live Free or Die Hard', 'Forrest Gump', 'The Magic Of The Big Blue. Seven Continents', 'Valkyrie', 'Fight Club', 'Shooter', 'Titanic', 'The Lord of the Rings: The Fellowship of the Ring', 'Mimic', '000 BC', 'Predator 2', 'Dawn of the Dead', 'For Your Eyes Only', 'Flags of Our Fathers', 'The Departed', 'Independence Day', 'Pirates of the Caribbean: Dead Mans Chest', 'In Time', 'Edward Scissorhands', 'Finding Nemo', 'Armageddon', 'Speed', 'Jaws 2', 'Platoon', 'Animal House', 'House 2: The Second Story', 'Backdraft', 'Cheech & Chongs Next Movie', 'Meet the Parents', 'The Tin Drum', 'Fantastic 4: Rise of the Silver Surfer', 'Harry Potter and the Prisoner of Azkaban', 'Dead Poets Society', 'Being John Malkovich', 'Unforgiven', 'American Sniper', 'Donnie Darko', 'Legend', 'Ghost in the Shell', 'The Mummy Returns', 'Star Wars: Episode II - Attack of the Clones', 'Fast Times at Ridgemont High', 'Little Lips', 'American History X', 'Constantine', 'Harry Potter and the Goblet of Fire', 'The Hobbit: The Desolation of Smaug', 'The Intouchables', 'Men in Black 3', 'Shaun of the Dead', 'New Crouching Tiger', 'Rio', 'Aladdin', 'The Lord of the Rings: The Return of the King', 'Spider-Man', 'Taken', 'Grown Ups', 'Lethal Weapon', 'The Goonies', 'Man of Steel', 'The Godfather', 'The Bourne Identity', 'Tarzan', 'The Pursuit of Happyness', 'Indiana Jones and the Temple of Doom', 'Star Wars: Episode IV - A New Hope', 'Saving Private Ryan', 'The Keep', 'The Lord of the Rings: The Two Towers', 'The Matrix Revolutions', 'Oblivion', 'The Spy Who Loved Me', 'Basic Instinct', 'Demolition Man', 'Escape from New York', 'Jaws', 'Star Wars: Episode VI - Return of the Jedi', 'Airplane II: The Sequel', 'Airplane!', 'Goodfellas', 'Superman', 'The Hunt for Red October', 'Beetlejuice', 'Inside Man', 'La Femme Nikita', 'The Mexican', 'Pacific Rim', 'Braveheart', 'Groundhog Day', 'Kill Bill: Vol. 2', 'Django Unchained', 'Kick-Ass', 'Oliver & Company', 'Conan the Destroyer', 'Cars', 'Once Upon a Time in America', 'The Dark Knight', 'Skyfall', 'The Abyss', 'The Emerald Forest', 'Spider-Man 3', 'Daddy Day Care', 'Casino', 'Superman II', 'Shutter Island', 'Pirates of the Caribbean: The Curse of the Black Pearl', 'Secretary', 'Childs Play', 'Halloween', 'Interstellar', 'The Fox and the Hound', 'Hook', 'Silver Linings Playbook', 'Double Impact', 'The Imitation Game', 'The Fugitive', 'The Curious Case of Benjamin Button', ' Myself & Irene', 'The Blues Brothers', 'Yellowbeard', 'Inglourious Basterds', 'Howls Moving Castle', 'Alien', 'Raiders of the Lost Ark', 'The Devil Wears Prada', 'Dracula', ' Robot', 'Enemy of the State', 'Ace Ventura: Pet Detective', 'I', 'Crossroads', ' Hidden Dragon', 'Avatar', 'Rocky III', 'The Purple Rose of Cairo', 'Up in Smoke', 'The Outsiders', 'World War Z', 'Terminator 2: Judgment Day', 'The Lazarus Project', 'Terminator Salvation', 'The Godfather: Part III', 'Thor: The Dark World', 'Captain America: The First Avenger', 'The SpongeBob SquarePants Movie', 'The Bone Collector', 'Predator', 'Mad Max Beyond Thunderdome', 'The Rocky Horror Picture Show', 'Legends of the Fall', 'American Beauty', 'Nausica of the Valley of the Wind', 'The Incredible Hulk', 'Men in Black II', 'The Avengers', 'The Man in the Iron Mask', 'Kill Bill: Vol. 1', 'City of Angels', 'Inception', 'The Gods Must Be Crazy', 'Batman & Robin', 'Thor', 'Leon: The Professional', 'The Dark Knight Rises', 'Weekend at Bernies', 'Exodus: Gods and Kings', 'The Hobbit: The Battle of the Five Armies', 'Aliens vs Predator: Requiem', 'Carrie', 'The Final Countdown', 'Kingsman: The Secret Service', 'Sucker Punch', 'Beverly Hills Cop', 'Fear and Loathing in Las Vegas', 'Species', 'Mr. & Mrs. Smith', 'The Last American Virgin', 'Sin City', 'Cliffhanger', 'Cheeky', 'Cloverfield', 'Fargo', ' or the 120 Days of Sodom', 'Raging Bull', 'Starship Troopers', 'Snatch', 'Frozen', 'A Bugs Life', 'The Shawshank Redemption', 'The Hunger Games: Catching Fire', 'The Amazing Spider-Man 2', '300', 'John Wick', 'Up', 'Lucy', 'The Dreamers', 'Taken 3', 'Crash', 'THX 1138', 'Conan the Barbarian', 'Lara Croft Tomb Raider: The Cradle of Life', 'Man on Fire', 'The Return of Jafar', 'Schindlers List', 'Close Encounters of the Third Kind', 'Scarface', 'The Fly', 'Trading Places', 'Friday the 13th', 'No Country for Old Men', 'The Prestige', '1984', 'Grease', 'Die Hard', 'Interview with the Vampire', 'Stripes', ' the Ape Man', 'Hot Bubblegum', 'True Lies', 'Omen III: The Final Conflict', 'Superbad', 'Rocky', 'Licence to Kill', 'The Thing', 'Bad Boys', 'Olympus Has Fallen', 'Lupin the Third: The Castle of Cagliostro', 'Commando', 'Apocalypse Now', 'Ted', 'The Matrix', 'My Neighbor Totoro', 'The Expendables', 'Watership Down', 'Lolita', 'Zero Dark Thirty', 'Blow', 'Mrs. Doubtfire', 'Quantum of Solace', 'Good Will Hunting', 'Robin Hood: Prince of Thieves', 'Teenage Mutant Ninja Turtles', 'The Mummy', 'Stephen Kings It', 'Jurassic Park III', 'The Rescuers', 'Amadeus', 'Army of Darkness', 'TRON', 'Im for the Hippopotamus', 'Becoming Jane', 'Harry Potter and the Deathly Hallows: Part 2', 'Harry Potter and the Deathly Hallows: Part 1', 'Harry Potter and the Half-Blood Prince', 'Monty Python and the Holy Grail', 'Casino Royale', 'Guardians of the Galaxy', 'Red Sonja', 'The Terminator']