-- Script para poblar la base de datos
DELETE FROM categoria_categoria;
DELETE FROM almacen_producto;
-- INSERT categoria
INSERT INTO categoria_categoria (id, nombre, descripcion, imagen, slug)
VALUES
(0, 'Costo 0', 'Descripcion Costo 0', '', 'costo-0'),
(1, 'Costo 1', 'Descripcion Costo 1', '', 'costo-1'),
(2, 'Costo 2', 'Descripcion Costo 2', '', 'costo-2'),
(3, 'Costo 3', 'Descripcion Costo 3', '', 'costo-3'),
(4, 'Costo 4', 'Descripcion Costo 4', '', 'costo-4'),
(5, 'Costo 5', 'Descripcion Costo 5', '', 'costo-5'),
(6, 'Costo 6', 'Descripcion Costo 6', '', 'costo-6'),
(7, 'Costo 7', 'Descripcion Costo 7', '', 'costo-7'),
(8, 'Costo 8', 'Descripcion Costo 8', '', 'costo-8'),
(9, 'Costo 9', 'Descripcion Costo 9', '', 'costo-9'),
(10, 'Costo 10', 'Descripcion Costo 10', '', 'costo-10');
-- INSERT producto
INSERT INTO almacen_producto (id, nombre, slug, descripcion, precio, imagen, stock, is_available, fecha_creacion, fecha_modificacion, categoria_id)
VALUES
(1,'Ravnica Allegiance: Blood Crypt','blood-crypt',"({T}: Add {B} or {R}.) As Blood Crypt enters the battlefield, you may pay 2 life. If you don't, it enters the battlefield tapped.",18000,'photos/productos/blood-crypt.png',10,1,DATE('now'),DATE('now'),0),
(2,'Legends: Chains of Mephistopheles','chains-of-mephistopheles',"If a player would draw a card except the first one they draw in each of their draw steps, that player discards a card instead. If the player discards a card this way, they draw a card. If the player doesn't discard a card this way, they mill a card.",1070150,'photos/productos/chains-of-mephistopheles.png',1,1,DATE('now'),DATE('now'),2),
(3,'Beta: Black Lotus','black-lotus',"{T}, Sacrifice Black Lotus: Add three mana of any one color.",39439150,'photos/productos/black-lotus.png',2,1,DATE('now'),DATE('now'),0),
(4,'Meren of Clan Nel Toth','meren-of-clan-nel-toth',"Flying, vigilance, indestructible Other permanents you control have indestructible.",55250,'photos/productos/meren-of-clan-nel-toth.png',3,1,DATE('now'),DATE('now'),8),
(5,"'Secret Lair: Nicol Bolas, Dragon-God'",'nicol-bolas-dragon-god-522-foil',"Nicol Bolas, Dragon-God has all loyalty abilities of all other planeswalkers on the battlefield.
+1: You draw a card. Each opponent exiles a card from their hand or a permanent they control.
-3: Destroy target creature or planeswalker.
-8: Each opponent who doesn’t control a legendary creature or planeswalker loses the game.
|4|",11900,'photos/productos/nicol-bolas-dragon-god-522-foil.png',5,1,DATE('now'),DATE('now'),5),
(6,"'Phyrexia: All Will Be One: Atraxa, Grand Unifier'",'atraxa-grand-unifier',"Flying, vigilance, deathtouch, lifelink
When Atraxa, Grand Unifier enters the battlefield, reveal the top ten cards of your library. For each card type, you may put a card of that type from among the revealed cards into your hand. Put the rest on the bottom of your library in a random order. (Artifact, battle, creature, enchantment, instant, land, planeswalker, and sorcery are card types.)",29750,'photos/productos/atraxa-grand-unifier.png',2,1,DATE('now'),DATE('now'),7),
(7,'Unlimited: Volcanic Island','sheoldred-the-apocalypse',"➡️: Add 💧 or 🔥",76500,'photos/productos/sheoldred-the-apocalypse.png',3,1,DATE('now'),DATE('now'),4),
(8,'Dominaria United: Liliana of the Veil','liliana-of-the-veil',"[+1]: Each player discards a card.
[-2]: Target player sacrifices a creature.
[-6]: Separate all permanents target player controls into two piles. That player sacrifices all permanents in the pile of their choice.
|3|",18700,'photos/productos/liliana-of-the-veil.png',2,1,DATE('now'),DATE('now'),3),
(9,'Streets of New Capenna: Xander s Lounge','xanders-lounge',"({T}: Add {U}, {B}, or {R}.)
Xander's Lounge enters the battlefield tapped.
Cycling {3} ({3}, Discard this card: Draw a card.)",10200,'photos/productos/xanders-lounge.png',1,1,DATE('now'),DATE('now'),0),
(10,'War of the Spark: Niv-Mizzet Reborn','niv-mizzet-reborn',"Flying
When Niv-Mizzet Reborn enters the battlefield, reveal the top ten cards of your library. For each color pair, choose a card that's exactly those colors from among them. Put the chosen cards into your hand and the rest on the bottom of your library in a random order.",1875,'photos/productos/niv-mizzet-reborn.png',5,1,DATE('now'),DATE('now'),5),
(11,"'Guilds of Ravnica: Guild Kits: Niv-Mizzet, the Firemind (Foil)'",'niv-mizzet-the-firemind-foil',"Flying
Whenever you draw a card, Niv-Mizzet, the Firemind deals 1 damage to any target.",2250,'photos/productos/niv-mizzet-the-firemind-foil.png',4,1,DATE('now'),DATE('now'),6),
(12,'Stronghold: Mox Diamond','mox-diamond',"If Mox Diamond would enter the battlefield, you may discard a land card instead. If you do, put Mox Diamond onto the battlefield. If you don't, put it into its owner's graveyard.
{T}: Add one mana of any color.",438000,'photos/productos/mox-diamond.png',3,1,DATE('now'),DATE('now'),0),
(13,"'Multiverse Legends: Ragavan, Nimble Pilferer'",'ragavan-nimble-pilferer',"Whenever Ragavan, Nimble Pilferer deals combat damage to a player, create a Treasure token and exile the top card of that player's library. Until end of turn, you may cast that card.
Dash {1}{R} (You may cast this spell for its dash cost. If you do, it gains haste, and it's returned from the battlefield to its owner's hand at the beginning of the next end step.)",48750,'photos/productos/ragavan-nimble-pilferer.png',5,1,DATE('now'),DATE('now'),1),
(14,'Antiquities: Mishra s Workshop','mishras-workshop',"{T}: Add {C}{C}{C}. Spend this mana only to cast artifact spells.",2430000,'photos/productos/mishras-workshop.png',6,1,DATE('now'),DATE('now'),0),
(15,'Khans of Tarkir: Polluted Delta','polluted-delta',"{T}, Pay 1 life, Sacrifice Polluted Delta: Search your library for an island or swamp card and put it into play. Then shuffle your library.",36000,'photos/productos/polluted-delta.png',2,1,DATE('now'),DATE('now'),0),
(16,'3rd Edition: Wheel of Fortune','wheel-of-fortune',"Each player discards their hand, then draws seven cards.",202500,'photos/productos/wheel-of-fortune.png',1,1,DATE('now'),DATE('now'),3),
(17,'Mystery Booster/The List: Mana Crypt','mana-crypt',"At the beginning of your upkeep, flip a coin. If you lose the flip, Mana Crypt deals 3 damage to you.
{T}: Add {C}{C}.",150000,'photos/productos/mana-crypt.png',1,1,DATE('now'),DATE('now'),0),
(18,'Commander 2020: Deflecting Swat','deflecting-swat',"If you control a commander, you may cast this spell without paying its mana cost.
You may choose new targets for target spell or ability.",45000,'photos/productos/deflecting-swat.png',2,1,DATE('now'),DATE('now'),3),
(19,'Tempest: Ancient Tomb','ancient-tomb',": Add . Ancient Tomb deals 2 damage to you.",71250,'photos/productos/ancient-tomb.png',1,1,DATE('now'),DATE('now'),0),
(20,'Alliances: Force of Will','force-of-will',"You may pay 1 life and exile a blue card from your hand rather than pay Force of Will's mana cost.
Counter target spell.",81750,'photos/productos/force-of-will.png',4,1,DATE('now'),DATE('now'),5),
(21,'Double Masters: Doubling Season','doubling-season',"If an effect would create one or more tokens under your control, it creates twice that many of those tokens instead.
If an effect would put one or more counters on a permanent that you control, it puts twice that many of those counters on that permanent instead.",75000,'photos/productos/doubling-season.png',2,1,DATE('now'),DATE('now'),5),
(22,'Core Set 2021: Heroic Intervention','heroic-intervention',"Permanents you control gain hexproof and indestructible until end of turn.",17250,'photos/productos/heroic-intervention.png',1,1,DATE('now'),DATE('now'),2),
(23,'Kamigawa: Neon Dynasty: Farewell','farewell',"Choose one or more -
Exile all artifacts.
Exile all creatures.
Exile all enchantments.
Exile all graveyards.",11250,'photos/productos/farewell.png',2,1,DATE('now'),DATE('now'),6),
(24,"'Dominaria United Variants: Sheoldred, the Apocalypse (Phyrexian)'",'sheoldred-the-apocalypse-phyrexian',"Deathtouch
Whenever you draw a card, you gain 2 life.
Whenever an opponent draws a card, they lose 2 life",63750,'photos/productos/sheoldred-the-apocalypse-phyrexian.png',2,1,DATE('now'),DATE('now'),4),
(25,'Arabian Nights: Guardian Beast','guardian-beast',"As long as Guardian Beast is untapped, noncreature artifacts you control can't be enchanted, they're indestructible, and other players can't gain control of them. This effect doesn't remove Auras already attached to those artifacts.",573750,'photos/productos/guardian-beast.png',4,1,DATE('now'),DATE('now'),1),
(26,'Commander 2017: The Ur-Dragon (Foil)','the-ur-dragon-foil',"Eminence - As long as The Ur-Dragon is in the command zone or on the battlefield, other Dragon spells you cast cost {1} less to cast.
Flying
Whenever one or more Dragons you control attack, draw that many cards, then you may put a permanent card from your hand onto the battlefield.",56250,'photos/productos/the-ur-dragon-foil.png',3,1,DATE('now'),DATE('now'),9),
(27,'Theros: Swan Song','swan-song',"Counter target enchantment, instant, or sorcery spell. Its controller puts a 2/2 blue Bird creature token with flying onto the battlefield.",12000,'photos/productos/swan-song.png',5,1,DATE('now'),DATE('now'),1),
(28,'Urza s Saga: Yawgmoth s Will','yawgmoths-will',"Until end of turn, you may play cards from your graveyard.
If a card would be put into your graveyard from anywhere this turn, exile that card instead.",120000,'photos/productos/yawgmoths-will.png',6,1,DATE('now'),DATE('now'),3),
(29,'Legends: The Abyss','the-abyss',"At the beginning of each player’s upkeep, destroy target nonartifact creature that player controls of their choice. It can’t be regenerated.",630000,'photos/productos/the-abyss.png',8,1,DATE('now'),DATE('now'),4),
(30,"'Legends: Nether Void
'",'nether-void',"Whenever a player casts a spell, counter it unless that player pays {3}.",510000,'photos/productos/nether-void.png',1,1,DATE('now'),DATE('now'),4),
(31,'Commander 2017: Edgar Markov (Foil)','edgar-markov-foil',"Eminence - Whenever you cast another Vampire spell, if Edgar Markov is in the command zone or on the battlefield, create a 1/1 black Vampire creature token.
First strike, haste
Whenever Edgar Markov attacks, put a +1/+1 counter on each Vampire you control.",60000,'photos/productos/edgar-markov-foil.png',2,1,DATE('now'),DATE('now'),6),
(32,"'Time Spiral Remastered: Urborg, Tomb of Yawgmoth'",'urborg-tomb-of-yawgmoth',"Each land is a Swamp in addition to its other land types.",33750,'photos/productos/urborg-tomb-of-yawgmoth.png',1,1,DATE('now'),DATE('now'),0),
(33,'Alliances: Lake of the Dead','lake-of-the-dead',"If Lake of the Dead would enter the battlefield, sacrifice a Swamp instead. If you do, put Lake of the Dead onto the battlefield. If you don't, put it into its owner's graveyard.
{T}: Add {B}.
{T}, Sacrifice a Swamp: Add {B}{B}{B}{B}.",90000,'photos/productos/lake-of-the-dead.png',2,1,DATE('now'),DATE('now'),0),
(34,'Commander 2020: Deadly Rollick','deadly-rollick',"If you control a commander, you may cast this spell without paying its mana cost.
Exile target creature.",36000,'photos/productos/deadly-rollick.png',3,1,DATE('now'),DATE('now'),4),
(35,'Core Set 2021: Terror of the Peaks','terror-of-the-peaks',"Flying
Spells your opponents cast that target Terror of the Peaks cost an additional 3 life to cast.
Whenever another creature enters the battlefield under your control, Terror of the Peaks deals damage equal to that creature's power to any target.",32250,'photos/productos/terror-of-the-peaks.png',4,1,DATE('now'),DATE('now'),5),
(36,"'Battle for Zendikar: Ulamog, the Ceaseless Hunger'",'ulamog-the-ceaseless-hunger',"When you cast this spell, exile two target permanents.
Indestructible
Whenever Ulamog, the Ceaseless Hunger attacks, defending player exiles the top twenty cards of their library.",37500,'photos/productos/ulamog-the-ceaseless-hunger.png',3,1,DATE('now'),DATE('now'),10),
(37,'War of the Spark: Finale of Devastation','finale-of-devastation',"Search your library and/or graveyard for a creature card with converted mana cost X or less and put it onto the battlefield. If you search your library this way, shuffle it. If X is 10 or more, creatures you control get +X/+X and gain haste until end of turn.",37500,'photos/productos/finale-of-devastation.png',2,1,DATE('now'),DATE('now'),2),
(38,'Innistrad: Parallel Lives','parallel-lives',"If an effect would put one or more tokens onto the battlefield under your control, it puts twice that many of those tokens onto the battlefield instead.",41250,'photos/productos/parallel-lives.png',2,1,DATE('now'),DATE('now'),4),
(39,'Commander Legends: Jeska s Will','jeskas-will',"Choose one. If you control a commander as you cast this spell, you may choose both.
Add {R} for each card in target opponent's hand.
Exile the top three cards of your library. You may play them this turn.",21000,'photos/productos/jeskas-will.png',2,1,DATE('now'),DATE('now'),3),
(40,'Urza s Saga: Gilded Drake','gilded-drake',"Flying
When Gilded Drake enters the battlefield, exchange control of Gilded Drake and up to one target creature an opponent controls. If you don't make an exchange, sacrifice Gilded Drake. This ability can't be countered except by spells and abilities. (This effect lasts indefinitely.)",168750,'photos/productos/gilded-drake.png',2,1,DATE('now'),DATE('now'),2),
(41,'Ikoria: Lair of Behemoths: The Ozolith','the-ozolith',"Whenever a creature you control leaves the battlefield, if it had counters on it, put those counters on the Ozolith.
At the beginning of combat on your turn, if The Ozolith has counters on it, you may move all counters from The Ozolith onto target creature.",24000,'photos/productos/the-ozolith.png',1,1,DATE('now'),DATE('now'),1),
(42,'Commander Legends: Jeweled Lotus','jeweled-lotus',"{T}, Sacrifice Jeweled Lotus: Add three mana of any one color. Spend this mana only to cast your commander.",75000,'photos/productos/jeweled-lotus.png',3,1,DATE('now'),DATE('now'),0),
(43,"'Kamigawa: Neon Dynasty: Boseiju, Who Endures'",'boseiju-who-endures',"{T}: Add {G}.
Channel - {1}{G}, Discard Boseiju, Who Endures: Destroy target artifact, enchantment, or nonbasic land an opponent controls. That player may search their library for a land card with a basic land type, put it onto the battlefield, then shuffle. This ability costs {1} less to activate for each legendary creature you control.",32250,'photos/productos/boseiju-who-endures.png',1,1,DATE('now'),DATE('now'),0),
(44,'Arabian Nights: Juzam Djinn','juzam-djinn',"At the beginning of your upkeep, Juzam Djinn deals 1 damage to you.",1950000,'photos/productos/juzam-djinn.png',3,1,DATE('now'),DATE('now'),2),
(45,'Magic 30th Anniversary Edition: Black Lotus (Not Tournament Legal)','black-lotus-not-tournament-legal',"{T}, Sacrifice Black Lotus: Add three mana of any one color.",6000000,'photos/productos/black-lotus-not-tournament-legal.png',2,1,DATE('now'),DATE('now'),0),
(46,'Unlimited: Ancestral Recall','ancestral-recall',"Target player draws three cards.",6000000,'photos/productos/ancestral-recall.png',4,1,DATE('now'),DATE('now'),1),
(47,"'Phyrexia: All Will Be One: Elesh Norn, Mother of Machines'",'elesh-norn-mother-of-machines',"Vigilance
If a permanent entering the battlefield causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.
Permanents entering the battlefield don't cause abilities of permanents your opponents control to trigger.",26250,'photos/productos/elesh-norn-mother-of-machines.png',4,1,DATE('now'),DATE('now'),5),
(48,'Arabian Nights: Library of Alexandria','library-of-alexandria',"{T}: Add {C}.
{T}: Draw a card. Activate this ability only if you have exactly seven cards in your hand.",1725000,'photos/productos/library-of-alexandria.png',2,1,DATE('now'),DATE('now'),0),
(49,'Commander 2020: Fierce Guardianship','fierce-guardianship',"If you control a commander, you may cast this spell without paying its mana cost.
Counter target noncreature spell.",48750,'photos/productos/fierce-guardianship.png',1,1,DATE('now'),DATE('now'),3),
(50,'Modern Horizons 2: Urza s Saga','urzas-saga',"(As this Saga enters and after your draw step, add a lore counter. Sacrifice after III.)
I: Urza's Saga gains ""{T}: Add {CL}.""
II: Urza's Saga gains ""{2}, {T}: Create a 0/0 colorless Construct artifact creature token with 'This creature gets +1/+1 for each artifact you control.'""
III: Search your library for an artifact card with mana cost {0} or {1}, put it onto the battlefield, then shuffle.",28500,'photos/productos/urzas-saga.png',1,1,DATE('now'),DATE('now'),0);