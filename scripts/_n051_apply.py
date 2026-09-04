#!/usr/bin/env python3
# Style normalization pass v1 — n051 (DKS_0301..DKS_0306)
import json, os, sys

BASE = '/Users/dev_env/Documents/projects/indian_apps/dailyX/daily_krishna_stories'

NEW_STORIES = {}

NEW_STORIES['DKS_0301'] = '''No enemy threw the Yadavas out of Mathura. They left of their own counsel, on a day they chose themselves, carrying the city with them in the shape of a decision.

The Yadavas were Krishna's own clan, and Mathura was their city. The decision to leave it had been forming for years. Jarasandha, the emperor of the eastern kingdom of Magadha, had marched against Mathura and been beaten back, but he could not be slain — the gods had made him deathless to his enemies — and his soldiers were so many that the Yadavas could not have destroyed them even in a hundred years of war. Now word came that Kalayavana, a foreign king of terrible strength, was marching on the city with a host beyond counting, and that his messenger had already come to the houses of the Vrishnis and the Andhakas, the two branches of the Yadava family. The clans gathered, set Krishna at their head, and held their council in fear.

Krishna spoke to the Yadus in full assembly. This city of Mathura, he said, is the home of the Yadavas. We were born here, and we grew up in Vraja, the cowherd country. Our griefs have vanished and our enemies have been defeated — but now our wars with the kings have begun, and the war with Jarasandha. Our foot soldiers and our beasts are beyond counting, and we have jewels and friends in plenty. Yet for all that wealth, Mathura is small, and an enemy can enter it easily. If a crore of princes and soldiers — ten million of them — live crowded together here, dissension will spring up among them. It seems to me better, O leading Yadavas, that we should live elsewhere. If you wish it, we shall lay out a new city. Tell me it is well before this assembly, and I shall carry it out at the proper time.

The Yadavas answered with one voice: do what you deem proper for the good of all of us.

Even then the leaving might have waited — but word came that Jarasandha and Kalayavana were now advancing together. The elders consulted among themselves and saw no end to it. Then Krishna said: today is an auspicious day. We shall go out of Mathura this very day, with our army and our followers.

They went out that same day, headed by Vasudeva, Krishna's father. The whole city poured after them — wives and children, chariots and elephants — and the noise of the march was like the waves of the ocean. They carried their wealth, their kinsmen and friends, their golden chariots and great elephants, their horses trotting under gold-decked harness, and set their faces to the west. Vasudeva and the elders rode in front, guiding the long column like men who had always known the way.

They marched until they reached the bank of the sea. The shore was green with creepers and vines, rich in coconut trees, covered with ketaki and palmyra, and the Yadavas were as delighted as if they had come to the country of the gods. Krishna went searching for the ground where he would lay out a city, and found an open tract on the ocean's edge — coppery soil mixed with gravel, firm ground for beasts of burden, marked with every good sign a city needs, as if the Goddess of Prosperity herself watched over it. The sea breeze fanned it, and the ocean watered it. Near it rose Mount Raivata, shining above the shore, where Drona, the great teacher of princes, had once lived and where the archer Ekalavya had once made his home, and beside the mountain lay the old sporting ground that already bore the name Dwaravati.

There Krishna chose his ground, and that night the Yadava commanders pitched their tents. Krishna himself, standing on the new land, thought over the names he would give to the houses of the city that would rise here, and rested without a care.

The Yadavas had secured Dwaravati, and they lived there happily with their friends, as the gods live in their own city. The city of gates — Dwaraka — had begun.'''

NEW_STORIES['DKS_0302'] = '''Rukmi, the king of Vidarbha, had spent his life in rivalry with Krishna, the lord of Dwaraka — and everyone knew why. Years before, Krishna had carried off Rukmi's sister Rukmini to marry her, and Rukmi, who had sworn to destroy the man who took her, had been defeated instead; the defeat had never sat well with him. Yet when Rukmi announced a swayamvara for his own daughter — a gathering at which the princess herself would choose her husband — kings and princes came to his house from many lands, rich and powerful, each hoping to be chosen.

Among the princes came Pradyumna, the son of Krishna and Rukmini. The moment she saw him, Rukmi's daughter Rukmavati wanted to marry him. She was celebrated for her beauty, graceful and radiant, and Krishna's son — peerless in beauty himself — wished to marry her in return. When the kings had taken their seats in the swayamvara hall, the princess of Vidarbha walked past them all and chose Pradyumna, the slayer of enemies: a master of arms, well built like a lion, the most handsome young man in the assembly. The choice was made, and she gave him her heart utterly.

After the ceremony the kings returned to their own cities, and Pradyumna brought the princess of Vidarbha home to Dwaraka. He lived happily with her, and in time she bore him a son, Aniruddha — matchless in deeds, like the son of a god.

The years turned. Aniruddha came of age and mastered the Vedas, the ancient sacred hymns, the science of archery, and the moral laws. Then Krishna chose a wife for him — and the bride was a second Rukmavati: the granddaughter of Rukmi, gold-like in beauty, namesake of the elder Rukmavati who had married Pradyumna. The name ran through the family like a thread joining one generation to the next.

It was a strange match, for Rukmi had never stopped treating Krishna as an enemy. But the wedding had been urged by Rukmi's own son and by Rukmini, and for their sakes he set aside his old enmity. "I confer Rukmavati on Aniruddha," he said with delight, "a youth of accomplishments and a peaceful nature."

So Krishna went to Vidarbha surrounded by his own army, accompanied by Rukmini, by Balarama, his elder brother, by his sons, and by the other Yadavas; and Rukmi's kinsmen, friends, and allies came too, at his invitation. On an auspicious day, under a favorable star, the wedding of Aniruddha and Rukmavati was celebrated with great festivity. The Vidarbhas and the Yadavas rejoiced together, and the Vrishnis, honored there like the immortals, lived happily in the midst of the feast.

For those days at least, the old quarrel between the two houses was remembered by no one. Vidarbha and Dwaraka sat down together as one family.'''

NEW_STORIES['DKS_0303'] = '''Krishna had promised his queen Satyabhama a tree from the garden of heaven itself — the Parijata, whose blossoms no earthly tree could match. Indra, the king of the gods, who owned the tree, had refused to give it up, and so Krishna had set out to take it for himself.

He rode out of Dwaraka one morning under the pretext of a hunt, with Satyaki, his friend and fellow warrior, beside him. He left his charioteer Daruka with the chariot, telling him to wait, tending and grooming the horses, until his master returned on that very car. Pradyumna, his son, followed on a chariot of his own, swift enough to course over the hills. Within the twinkling of an eye they stood in Nandana, the pleasure park of the gods, where hosts of heavenly guardians kept watch — and there, before their eyes, Krishna uprooted the Parijata tree and laid it across the back of Garuda, the great bird who carried him.

Then a strange thing happened. The tree itself bowed to Krishna as a living thing bows in homage, and Krishna spoke to it gently: "Do not fear, O tree." When he was sure it was firmly placed, he circled once around the stronghold of heaven. But the keepers of the garden had already run to Indra, and the king of the gods came out at once on his white elephant Airavata, with his son Jayanta following on a chariot.

"What is this going on?" Indra called out, for Krishna had by then reached the eastern gate of heaven.

Seated on Garuda, Krishna bowed his head in salute to his elder. "I am only taking away this excellent tree," he said, "for a ceremony my queen wishes to hold."

"You shall not take away this tree without challenging me to fight," Indra answered. "Strike the first blow at me. Hurl your mace Kaumodaki at me — and keep the promise you sent me."

So the two of them fought, there in the sky over the gods' own garden. Krishna pierced the great elephant Airavata with arrows sharp and fierce as thunder; Indra loosed heavenly shafts at Garuda and cut Krishna's arrows from the air as fast as they flew. Krishna cut down Indra's shafts in turn, bowstring answering bowstring — and the twang of the two great bows, Indra's and the Sharanga, was enough, they say, to make the dwellers of heaven swoon.

In the middle of it all, Jayanta made his move: he slipped toward Garuda and tried to pull the Parijata tree from the bird's back. "Pradyumna — prevent him," Krishna called out, and at once his son barred the way, firm as a wall. Jayanta, smiling, sent sharp arrows into every part of Pradyumna's body; and Pradyumna — whom the old tales call the god of love come down to earth — answered from his own chariot with arrows that moved like serpents. A fierce combat raged between the son of Indra and the son of Krishna, each using every weapon of offense and defense he knew, while gods and sages and the wandering singers of heaven looked on, struck with wonder.

And then Pradyumna's chariot was struck by a weapon of heavenly make. The whole car burned to ashes before the eyes of heaven — but the fire could not touch Pradyumna himself. When the flames fell away, he was still standing in the open sky where his chariot had been, unharmed, as if the air itself held him up.

Above them, the duel of the fathers went on, bowstring against bowstring. But heaven was no longer watching only Krishna and Indra. It was watching the two sons — and the one who had lost his chariot and still had not fallen. The chariot was ash; the warrior was not.'''

NEW_STORIES['DKS_0304'] = '''The demons came to the sacrifice with a list of demands: a share of the offerings, the right to drink the sacred Soma, the daughters of the man who was performing it, his finest jewels — and if any part was refused, the sacrifice would end.

The man who had vowed it was Brahmadatta, a learned priest of the school of the sage Yajnavalka, a scholar of the four Vedas, the ancient hymns, and the branches of learning that surround them. His rite would last a full year, and it was being held in the city of Shatpura, on the sacred bank of the river Avarta. The great sages had gathered to it — Vyasa, Yajnavalka himself, Jaimini, Devala, and many more — and so had Krishna's father Vasudeva, with Devaki, Krishna's mother, beside him, for Brahmadatta was an old friend and teacher of their house. Day after day Devaki moved among the beggars who came to the rite and gave them whatever they asked, as much as her husband's wealth allowed.

Then Nikumbha and the other demons of Shatpura, proud of a boon granted them long ago, assembled at the sacrificial ground and delivered their terms. Brahmadatta refused them to their faces. "No portion of the offerings has been laid down for you in the Vedas," he told them. "How then can I let you drink Soma here? If you doubt my words, ask these great sages, learned in the scriptures and their commentaries. My daughters I shall give in marriage to proper bridegrooms, as the Vedas ordain. If you will come to terms, I will give you my entire store of jewels. But if you use force — know that the son of Devaki is my protector."

The demons did not believe him, and force is what they used. They scattered the offerings and vessels that had made the rite famous for its generous food and gifts, and they carried off his daughters.

Vasudeva, helpless before them, thought of Krishna — and of Balarama, his elder brother, and of Gada. The moment Krishna was thought of, he knew everything that had happened, and he said to Pradyumna: "Proceed, my son, and save the maidens by your power of illusion. I myself will follow soon, with the Yadava army."

Pradyumna, ever obedient to his father, was in Shatpura within a moment. By his power of illusion he carried the maidens away, every one of them, and in their place he created counterfeit figures so like the originals that no eye could tell them apart. "Be not afraid," he said to Devaki, who had feared the worst for the girls. The demons seized the false maidens, certain they had won, and entered their city well satisfied — while the true daughters of Brahmadatta were already far beyond their reach.

And the sacrifice went on, celebrated according to the proper rites. The kings who had been invited began to arrive with their hosts and encamp near Shatpura: Jarasandha and Shishupala, the king of Chedi, Dantavakra, the five Pandava brothers, the sons of Dhritarashtra, the rulers of the Malava and Tangana lands, Rukmi, Shalya, Shakuni, and many another warrior king.

The sage Narada watched them come, and what he saw did not please him. "All the warrior kings and all the Yadavas have assembled at this sacrifice," he thought. "Surely this will lead to conflict. I shall try to bring it about." And he went to the house of Nikumbha.'''

NEW_STORIES['DKS_0305'] = '''There was a cave beneath Shatpura that no map of the city showed — and by the middle of that day, it had swallowed one Yadava warrior after another.

It had begun with a sacrifice. Brahmadatta, a learned priest, had vowed a year-long rite in Shatpura, and Krishna's family had taken his side when the city's demons tried to stop it. Failing in that, the demons had turned to the kings who came to witness the rite — the sage Narada had made sure of a conflict. The kings who had sided with the demons had drawn up against the Yadavas, and the sacrificial ground had become a battlefield.

At dawn the three rode out on Garuda: Balarama, Krishna's elder brother; Krishna himself; and Satyaki, a warrior of their own clan. They bathed in the sacred river Avarta, made holy by Shiva's blessing, put on their armor and finger-guards, and worshipped Shiva with offerings of bel leaves and water. Pradyumna, Krishna's son, took his place at the head of the army; the Pandava brothers stood guard over the sacrifice itself; and the rest of the soldiers watched the mouth of the cave. Krishna thought of Jayanta, the son of Indra, and of Pravara, the great champion of heaven — and both arrived the instant they were remembered, and took their posts above with Pradyumna.

The war instruments sounded — conches, drums, and battle-bugles. Samba and Gada drew the soldiers up in the shape of a makara, the great sea creature; and Uddhava, Krishna's close friend and adviser, with Kritavarma, Charudeshna, Sanatkumar, and the rest, guarded Aniruddha, Krishna's young grandson, and protected the rear.

Out of Shatpura came the demon host, dreadful in battle, roaring like gathering clouds. They rode on asses and elephants, crocodiles and hares, horses, buffaloes, lions, and tortoises, and their chariots were drawn by such beasts. Nikumbha, the chief of the demons, came at their head, filling the earth and sky with his shouts and his lion's roars.

Behind the demons came the kings who had chosen their side. Duryodhana and his hundred brothers, the princes of Hastinapura, wheeled their chariots up among the followers of Shishupala, the king of Chedi; Rukmi and Ahvati joined them, readying their great bows; and Bhagadatta, Shalya, Shakuni, Jarasandha, Trigarta, Virata, and Uttara made ready to fight the Yadavas and win the victory.

Nikumbha struck first, pouring arrows like serpents into the Yadava ranks. Anadhristhi, the commander of the Yadu army, could not bear it. He answered shaft for shaft with bright-feathered arrows whetted on stone, and slew the demons' soldiers until Nikumbha himself — chariot, standard, and horses — vanished under the hail of shafts.

Then Nikumbha, a master of illusion, worked his magic. He bewildered Anadhristhi, carried him off to the cave beneath the city, and imprisoned him there; and, invisible to every eye, he came back and took the others one by one — Kritavarma, Charudeshna, Vaitarana of the Bhoja clan, Sanatkumar, Arksha the son of Jambavati, Nishatha, Ulmuka, and many more Yadavas — dragging them all into that dreadful cave.

The fury of the Yadavas was terrible to behold. Krishna set his great bow, the Sharanga, and moved among the demons as fire moves over dry grass. The demons hurled their weapons by the thousand — iron missiles and clubs, fiery lances and burning axes, great rocks, and whole elephants and chariots flung through the air at him. A divine flame, the fire of Narayana that answers to Krishna alone, consumed them all, and Krishna baffled the demons with the blaze of his arrows, bearing their onslaught as a bull bears the autumn rain.

And then the day's fighting turned. At the command of Nandi, Shiva's messenger, Pradyumna moved among the kings who had sided with the demons, bearing the nooses that Shiva himself had given him. He bound Bhagadatta, and Shishupala, and Rukmi, and Ahvati, and the other kings who had come to fight the Yadavas, and took them all to the illusory cave. The cave that had swallowed the Yadava captains now held the kings — bound fast by the demons' own magic.'''

NEW_STORIES['DKS_0306'] = '''The demon came out of the cave the way a storm comes off the sea — all at once, and swinging.

The anger behind that charge had been building for days, and it had begun, strangely enough, with a stolen bride. While the Yadavas were busy with their games, Nikumbha, the demon chief and master of illusion, had slipped past the garden of the women's apartments and carried off Bhanumati, the beautiful young daughter of Bhanu, a nobleman of Krishna's own clan. He had an old score to settle: Pradyumna had once carried away Prabhavati, the daughter of Nikumbha's own brother Vajranabha, and had killed the brother besides. Remembering that enmity, the demon had taken his chance — for although that garden was said to be unapproachable, at that hour no guards stood watch, since the Yadavas were all at their games.

While the weeping maiden was being carried away, a great outcry rose through the women's apartments, and Vasudeva, Krishna's father, and the clan elder Ahuka came out in a fury. Krishna, hearing of the insult, mounted Garuda at once, with Arjuna — the Pandava prince, his dearest friend — beside him, and commanded Pradyumna, whose banner bore the makara, the great sea creature, to follow on his chariot. They overtook the demon before he could reach the city of Vajra.

Pradyumna, the greatest master of illusion among them, divided himself into three. Nikumbha, as though no blow could kill him, fought all three at once with heavy clubs — holding Bhanumati in his left hand and hurling the club with his right. And here was the cruelty of it: though any one of the three could have slain the demon, none could strike him for fear of wounding the maiden in his arms. They fought with restraint, sighing with pity for her, until Arjuna — the way a skilled archer strikes the serpent coiled around a camel and leaves the camel unhurt — began to wound the demon with his slim, cane-like arrows.

Then Nikumbha resorted to his illusion and vanished with the maiden, so completely that no one could tell where he had gone; and the three pursued him as he fled, now taking the shape of a yellow vulture against the sky. The chase ranged across the whole earth, over all seven of the great island-continents, until the demon dropped down at last with the maiden on the bank of the river Chela Ganga, high on the summit of Mount Gokarna — a mountain that neither gods, nor demons, nor the greatest of ascetics could cross, for the power of Shiva himself guarded it. There Pradyumna seized Bhanumati back from him, while Krishna and Arjuna drove the demon from the mountain's northern slope to its southern with their arrows, pursuing him on Garuda.

Broken and furious, Nikumbha fled into Shatpura, the city of his kinsmen, and Krishna and Arjuna spent the night at the mouth of the cave. With Krishna's permission, Pradyumna carried the maiden home to Dwaraka in triumph, and then returned to find his father and Arjuna waiting before the cave where he had left them.

They did not wait long. Hungry for the fight, Nikumbha came out of the cave, and Arjuna met him at the threshold with arrows from his great bow, the Gandiva, blocking the way. It made no difference. The demon came on, took up his club — a great staff covered with thorns — and struck Arjuna on the head. Blood poured from the prince's mouth, and he lost consciousness on the spot. Then the master of illusions smiled, and with a stroke no eye could see he struck the heroic son of Rukmini, himself a master of illusion, on the head. Pradyumna fell senseless beside his friend.

For a moment there was silence at the mouth of the cave. Then Krishna, king of Dwaraka, seized his great mace Kaumodaki and ran toward Nikumbha.'''

# ---- dry check first ----
ok = True
counts = {}
for sid, text in NEW_STORIES.items():
    wc = len(text.split())
    counts[sid] = wc
    if not (450 <= wc <= 700):
        ok = False
        print('OUT OF RANGE', sid, wc)
if not ok:
    print('counts:', counts)
    sys.exit(1)
print('counts ok:', counts)

# ---- apply ----
changed_levels = {
    'DKS_0301': 'major', 'DKS_0302': 'minor', 'DKS_0303': 'major',
    'DKS_0304': 'minor', 'DKS_0305': 'major', 'DKS_0306': 'minor',
}

for sid, new_story in NEW_STORIES.items():
    path = os.path.join(BASE, 'data/stories', sid + '.json')
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    before = len(data['story'].split())
    data['story'] = new_story
    data['generation_metadata']['style_normalization'] = {
        'pass': 'v1', 'model': 'deepseek-v4-flash', 'changed': changed_levels[sid]
    }
    out = json.dumps(data, indent=1, ensure_ascii=False) + '\n'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(out)
    after = len(new_story.split())
    print(sid, 'before:', before, 'after:', after, 'changed:', changed_levels[sid])
