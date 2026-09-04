#!/usr/bin/env python3
# Style normalization pass v1 — n052 (DKS_0307..DKS_0312)
import json, os

BASE = '/Users/dev_env/Documents/projects/indian_apps/dailyX/daily_krishna_stories'

NEW_STORIES = {}

NEW_STORIES['DKS_0307'] = '''Beyond the seven continents of the earth stood a city so tightly sealed that even the wind could not enter without the king's leave. It was called Vajra, and its king was Vajranabha, an Asura — one of the demon race that had fought the gods since the beginning of the world.

Vajranabha had won the city the hard way. On the summit of Mount Sumeru he had stood in long austerities until Brahma, the creator of the universe, appeared and offered him any boon he asked. The demon asked for two things: that no god should ever be able to kill him, and that he should own the city of Vajra — ringed with gardens and branch towns, rich in peerless jewels, a place that granted every wish before the wish was even spoken. Brahma said yes to both.

Millions of Asuras, the old enemies of the gods, took refuge there, healthy, well fed and content under the shelter of the boon. Grown bold, Vajranabha began to think of ruling everything. He went to Indra, king of the gods, and announced that the three worlds — heaven, earth and the world below — belonged by right to all the sons of the sage Kashyapa, father of gods and demons alike. He meant to govern them himself, and if Indra would not agree, let him give battle.

Indra took counsel with Brihaspati, the wise priest of the gods. "Our father Kashyapa is in the middle of a great sacrifice," Indra said. "When it ends, he will do what is fair." Vajranabha carried the same demand to Kashyapa himself and was sent home with the same promise. He returned to Vajra to bide his time.

But Indra had not finished. He came secretly to Dwaraka, where Krishna ruled with his clan, the Yadavas, and told him everything. Krishna listened, and answered calmly. The horse-sacrifice of his father Vasudeva was at hand; once it was over, he would kill Vajranabha. He was honest about the difficulty. "Even the wind cannot enter his city," Krishna said, "if Vajranabha does not wish it. But at the right hour we will find a way in."

The way in proved to be an actor. During the horse-sacrifice, a performer named Bhadra so delighted the assembled sages that they offered him any boon he wished. Prompted by Krishna — and seeming to be urged on by the goddess of learning herself — Bhadra asked that he might roam freely over the seven continents and through the sky with nothing to stop him; that he might be strong and unharmed by any creature, moving or still; that he might take whatever form he pleased; that age might never touch him; and that the sages might always be pleased with him. "So be it," they said.

From that day the actor ranged over the whole earth, performing in the cities of the demon kings and in far-off Uttarakuru, Bhadrashva and Ketumala, and on the island of Kalamra; and on every festival day he came home to Dwaraka, where the Yadavas welcomed him like a friend.

At last Indra summoned the swans of heaven. "You are brothers to the gods," he told them, "for both gods and swans were born of the sage Kashyapa. The destruction of the enemies of the gods lies before us, and you must help. Keep this counsel secret. Go to the city of Vajra, where no one else may enter, and swim in the pools of the king's own palace. Vajranabha has a daughter, Prabhavati, fair as moonlight, the jewel of the three worlds, kept apart for her swayamvara — the day she will choose her own husband. Tell her of Pradyumna, Krishna's son — his family, his beauty, his deeds — until her heart is won; then carry her words back to him, and report to Krishna and me at Dwaraka every day. The gods cannot kill the Asuras — Brahma's boon protects them. Their ruin must come from the sons of the gods, from Pradyumna and his brothers. And the door of the sealed city will open through Bhadra's boon, for the Yadavas will enter in the guise of his troupe of actors."

So the swans rose into the sky and turned toward the city no army could approach, carrying in their breasts a message that would open it from within — a message meant not for the walls, but for the heart of the king's own daughter.'''

NEW_STORIES['DKS_0308'] = '''The sealed city of Vajra, ruled by the demon king Vajranabha, had seen many traveling players, but never a troupe whose heroes looked so exactly like the heroes they pretended to be. There was a reason: the young men of the company were warriors of the Yadava clan, the family of Krishna of far-off Dwaraka, who had entered the sealed city disguised as players under the famous actor Bhadra.

Word of the players had gone ahead of them, and at Supura, a city of the demon king, Vajranabha's orders had already arrived: give the actors the finest rooms, treat them as honored guests, press jewels and fine clothes upon them. Bhadra danced for the people of Supura, and they were delighted. Then the company performed the Ramayana, the story of Vishnu taking birth as Rama to destroy the demon king Ravana. The players who took the parts of Rama and his brothers looked so much like the princes they played that even the oldest demons were startled; they rose to applaud, flinging down necklaces of gold and gems, bracelets and fine cloth, while the actors praised each demon house in verse.

The news reached the city of Vajra itself. Vajranabha, who had heard of the famous actor long before, sent for the troupe, and demons from the branch cities escorted the disguised warriors through the gates. They were lodged in a beautiful house built by the architect of the gods, and the king raised a great pavilion and turned their coming into a festival. When they had rested, he gave them jewels and called for the play. The women of his family watched from behind a screen, and the king sat among his kinsmen.

The young men of the Yadava clan dressed as players and began. First came music — drums and flutes — and then the women of the troupe sang a song of heaven, sweet to the ear, called Chhalikya. With the seven scales of music and the ragas of spring they sang the story of the sacred river Ganga's descent from heaven, and the demons rose again and again in pleasure. Pradyumna, Krishna's son, spoke the opening blessing with Gada and Shamba, his young kinsmen, and sang the hymn of the Ganga himself with graceful gestures. Then came a drama, the tale of the nymph Rambha: Pradyumna played the god Nalakuvara, who cursed the demon king Ravana for his cruelty and comforted the nymph, and the warriors' illusion raised Mount Kailasa behind them. Scene by scene the demons showered the players with costly garments, jewelled necklaces, sky-chariots, celestial elephants and cooling sandal scents — and at last the Chintamani, the gem that grants every wish. So freely did they give that they emptied their own treasuries.

But the true purpose of the festival lay elsewhere — in the chamber where Prabhavati, the king's daughter, lived. She had given her heart to a man she had never seen, Pradyumna, whose name and deeds the swans of heaven had carried to her. Now her dearest friend, a goose named Suchimukhi, came to her with news from beyond the walls. "I went to Dwaraka, the city of the Yadavas," she said. "I saw Pradyumna there in secret and told him of your love. He was glad, and he has appointed this very evening to meet you. The Yadavas never speak an untruth. Truly, tonight you will meet your love."

Prabhavati's heart leapt. "Stay in my room tonight," she said. "If you are with me, I fear nothing. With you beside me, I will see Krishna's son."

That evening a fragrant garland, thick with bees, was carried to the princess's chamber, and hidden among the bees was Pradyumna in the form of one of them. As dusk deepened, the other bees flew away one by one, until only one remained; and that one, the hero of the Yadava house, settled slowly on Prabhavati's ear.

The full moon rose over the city. Prabhavati's limbs burned and her mouth had gone dry; she confessed to the goose the strange fever of loving a man she had only heard of. "I have not seen him," she said, "and still my limbs burn." Then the bee at her ear was a bee no longer — the guest promised for the evening had come. In the lamplit room above the city, the princess who had given her heart to a name met at last the hero who had crossed the most guarded walls in the world as a bee in a flower garland.'''

NEW_STORIES['DKS_0309'] = '''Vajranabha, king of the Asuras, was set on conquering the three worlds, and he began with a warning he refused to hear. When the great sacrifice of the sage Kashyapa — father of gods and demons alike — came to an end, the demon king went to him to press the claim he had already made to Indra. Kashyapa answered as a father should. "Indra is the eldest of you all and foremost in every accomplishment," he said. "Strong by nature, grateful, devoted to the wise, king of the whole world and refuge of the good, he holds his sovereignty because he works for the well-being of all creatures. You cannot vanquish him; you will be killed. He who rouses a serpent meets his own destruction."

Vajranabha heard it all, saluted his father, and went home to gather his kinsmen, his warriors and his friends for war against heaven itself.

But ruin was already living inside his city. Some months before, the gates of Vajra had opened for a troupe of actors — and while they played, love had crossed the line between the two houses. Pradyumna, the son of Krishna, had secretly married Prabhavati, the daughter of Vajranabha himself, and his kinsmen Gada and Shamba had married Chandravati and Gunavati, daughters of the demon lord Sunabha. Now all three wives were with child, near their time. When the swans Indra and Krishna had sent into the city brought word that Vajranabha's death was at hand and that Pradyumna would deal it, the young heroes asked what would become of their wives and sent the swans back to the two gods with their fear. The gods answered: "Have no fear. Your sons will be born beautiful and complete in every accomplishment; even in the womb they will master the Vedas, the sacred books of wisdom, and they will spring at once to youth, masters of every scripture."

The swans carried the answer back through the guarded air. In time Prabhavati bore a son, the image of his father and wise beyond his years; a month later Chandravati bore Chandraprabha, the very image of Gada; and Gunavati bore Gunavan, beautiful and no less gifted. The boys grew swiftly, mastering every shastra — every branch of knowledge and weapon-craft — and played along the high turrets of the palaces, where the demons keeping watch in the sky could see them. What they saw they carried straight to Vajranabha, still bent over his plans for the war against heaven. "Arrest them," said the king, "those who have trespassed into my house."

At his order soldiers closed every quarter of the city, and the cry went up on all sides: "Arrest them — kill them." The young mothers began to weep with fear for their sons. Pradyumna steadied them. "While we are alive and firm, you need not fear," he said. "The demons will not be able to touch us." Then he turned to the bewildered Prabhavati and laid the whole choice before her. "Your father, your uncles, your brothers and all your kinsmen are waiting with clubs in their hands. For your sake they deserve our respect and honor. But the time is dreadful, and the demon kings mean to kill us. If we bear it, we shall die; if we fight, we shall succeed. Consult with your two sisters and tell us what we should do — we are under your orders."

Prabhavati knelt, weeping, her hands on her forehead. "Descendant of Yadu, take up your arms and protect yourself. If you survive, you will see your wife and sons. Remember Rukmini, your mother, and Aniruddha, your son — and save yourself from this peril. A great sage, radiant as sun and fire, once gave me a boon: that I would lead a blameless life, never be a widow, and that my sons would live. I hold to the hope that his words will not fail."

She rose, rinsed her mouth, and took up a sword. Then she placed it in Pradyumna's hands. "Acquire victory," she said. Bending low, Pradyumna bowed his head to the blade and accepted it with joy. And Chandravati, delighted, gave a sword to Gada; and Gunavati gave another to the mighty Shamba.

So the daughters of the demon house armed the sons of the Yadava house — and the family that love had joined in secret turned, as one, to face the armies of its own blood.'''

NEW_STORIES['DKS_0310'] = '''Pradyumna, the son of Krishna, did not wait for the demon host to strike. The demon king Vajranabha had discovered that the young warriors of Dwaraka were living hidden inside his city, married in secret to princesses of his own house — and while the cries of "Arrest them — kill them!" still rang through the streets of Vajra, Pradyumna created a chariot out of nothing and set the king of serpents to drive it. The soldiers sent to seize the trespassers found a household already in arms and the princes already beyond their reach.

The swords had barely left the princesses' hands. Pradyumna told his kinsmen to hold the ground and fight the demons below while he carried the battle to the sky. By his power of illusion he created a celestial car, and for its charioteer he made Ananta, the thousand-headed serpent, foremost of his kind, his thousand hoods spread over the car like a living crown.

Like fire running over dry grass, Pradyumna swept through the midst of the demon army, gladdening Prabhavati as he rode. Crescent-shaped arrows streamed from his bow — some sharp-headed, some blunt — and the demons fell before him without number, until the field was thick with the fallen. The demons who turned upon Gada and Shamba met their destruction like boats in a mighty ocean. The ascetic power behind the king's boon was spent, and with it the seal of the city: beings that had never been able to pass the walls now came and went as they pleased, and the demons who had lived safe behind their king's protection found their walls worth nothing. High above, Indra and the gods watched the battle between the demons and the Yadavas with pleasure.

Seeing the battle, Indra and Krishna sent their aid, with the permission of Brahma, the creator. Krishna sent his own chariot to Gada, driven by the son of Matali, the charioteer of the gods; Indra sent his great white elephant Airavata to Shamba, with the heavenly warrior Pravara upon it; and Indra's son Jayanta came to stand at Pradyumna's side. Then Pradyumna and Jayanta pressed through the very palaces of the city, driving the demons before a net of arrows, until no corner of Vajra was safe from them.

In the midst of the fighting, Pradyumna called out to Gada: "Indra has sent you this chariot, and the son of Matali is its driver. This elephant, with Pravara upon it, is for Shamba. Today a great worship of the god Rudra is being held in Dwaraka; when it ends, Krishna himself will come here tomorrow, and by his orders we will kill Vajranabha together with his kinsmen. But we must take care that he does not kill us and our sons first. The destruction of one's own sons is worse than one's own death — protect your sons by every means."

Then Pradyumna multiplied himself by his power of illusion into countless forms and dispelled the darkness the demons had cast over the field. Wherever an enemy turned, there stood Krishna's son, until the demons seemed to see him in every foe. The king of the gods watched, pleased, as the destroyer of his enemies stood everywhere at once.

All through the night the battle raged. When Jayanta went down to the celestial Ganga, the sacred river that springs from the foot of Vishnu, for his evening prayers, Pradyumna held the demons alone; and when Pradyumna in his turn said his evening prayers in that same river, Jayanta alone held the host — two men who paused in the middle of slaughter to keep faith with their devotions, a strangeness the demons could not understand. By dawn, three of every four demons lay dead.

At sunrise the field was still. The army that had marched out to conquer heaven lay broken around the city, and only its king remained — untouched, at the center of the ruin, waiting.'''

NEW_STORIES['DKS_0311'] = '''The first sign of help was a sound — a long, deep blast of a conch rolling through the sky above the sealed city of Vajra and its demon king, Vajranabha, so commanding that the air itself seemed to hold still. It was Panchajanya, the conch of Krishna, lord of the Yadavas. To the demon host below it was not music but a summons: somewhere beyond the clouds, at the edge of Indra's bright realm, Krishna had come to the war.

He came riding Garuda, the king of birds and the ancient enemy of serpents, who crosses the sky swifter than wind or thought and scatters the clouds like leaves. Beneath them the battle had already lasted long. Pradyumna, Krishna's son, had driven the demon armies before him, and the fighting had climbed into the upper air, close to the realm of Indra. As Garuda swept into that bright region, Krishna raised the conch and blew; and the demons below felt the old terror of that sound, for they had heard it before and remembered what followed it.

Pradyumna heard it and knew it at once. He had been waiting for that sound the way a son waits for his father's voice in a crowd. He came swiftly to his father, and Krishna spoke in few words. "Speedily kill Vajranabha," he said. Then he added, "Go there on Garuda's back." Pradyumna saluted Indra, saluted his father, mounted the great bird, and was gone.

Garuda carried him to his rival as swiftly as a thought, the wind of his passage flattening the banners of the demon host. Seated firmly on the bird, the young warrior — well read in the use of every weapon — struck first. The club was in his hand before Vajranabha had finished turning toward the sound of wings. It crashed against the demon king's breast, and the mighty Asura reeled and lost consciousness, until he lay like one dead.

Pradyumna, irrepressible in battle, looked down at the fallen king and spoke two words: "Be consoled." It was a strange courtesy between enemies, but it found its mark. In a moment Vajranabha's eyes opened. He gathered himself and spoke, with something close to admiration in his voice. "Well done, mighty Yadava," he said. "By your prowess you have become an illustrious enemy of mine. Now is the time for me to strike you in return. Wait here firmly." He planted his feet, drew himself up to his full height, and roared — a roar like a hundred clouds colliding — and hurled a huge club adorned with bells straight at Pradyumna. The blow caught the young warrior on the forehead, and he fell senseless.

Krishna saw his son fall. He did not descend from the sky; he did not cry out. He raised Panchajanya to his lips and blew — the same conch that had spread terror through the demons, now sounding like a father's voice calling a child home. It was not a battle-cry and not a signal. It was the sound a father makes when his child is hurt, a call that has never needed words. At that sound Pradyumna stirred. Strength returned to his limbs, and he rose and stood on the field again, whole and ready. And beholding him revived, all the worlds were glad — the gods in their bright houses, the warriors on the field, Indra most of all, and Krishna.'''

NEW_STORIES['DKS_0312'] = '''The duel was over, and yet nothing was settled. Above the city of Vajra the two armies had fallen back, giving the two champions room. Both had been struck down that day, and both had risen again — Vajranabha from the wound on his breast, Pradyumna from the blow on his forehead, called back by his father's conch. Now they faced each other across the empty sky, and the war could have gone on for another day, or another month.

It had not been a short war. Pradyumna had ridden against the demon host with the thousand-headed serpent Ananta yoked to his celestial car; Indra had sent his own chariot, his great white elephant Airavata, and his son Jayanta to aid the heroes of Dwaraka. Only Vajranabha himself had held his ground, trading blow for blow with the young warrior until both lay senseless — and then rising again to fight on. Now, in the pause after the conch's call, Krishna decided that the war had lasted long enough.

Then a wonder happened, the kind that old stories keep and tell to children ever after. In the stillness that followed the conch's last note, Krishna's discus — a circle of bright metal set with thousands of sharp points, the weapon that had destroyed the enemies of the gods — left its place and came through the air into his son's hand. The demons lived in fear of that discus, and every eye on the field followed its flight.

Pradyumna looked at it and understood what was being asked of him. He did not hesitate. He saluted Indra, saluted his father, and hurled the discus at Vajranabha. It did not miss. Before the very eyes of the demons, who had come to watch their king win, the great Asura fell, struck down at last. The war above the city of Vajra was over.

The rest of the host did not wait to mourn, and no one moved to avenge the king. The demon lord Sunabha, for all his care, was struck down by Gada on the field; Shamba's sharpened arrows sent the demons who remained to death; and Nikumbha, seeing what had befallen Vajranabha, fled in fear of Krishna to the far city of Shatpura, and no one followed him.

When it was done, Krishna and Indra came down from the sky into the city of Vajra itself. The city had passed through war, and its boys and its old people huddled in fear, waiting to see what conquerors do. But these conquerors had not come to take — they had come to quiet. The two lords walked among the frightened people, spoke to them gently, and established peace there; and the fear went out of the streets like a tide going out.

So the war that had begun in the upper air ended on the ground, in a city learning to be at peace again. Peace is not a loud thing. It settled over the city of Vajra like evening.'''

# Apply
changed_levels = {
    'DKS_0307': 'major', 'DKS_0308': 'major', 'DKS_0309': 'major',
    'DKS_0310': 'minor', 'DKS_0311': 'minor', 'DKS_0312': 'minor',
}

counts = {}
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
    counts[sid] = (before, after)
    print(sid, 'before:', before, 'after:', after, 'changed:', changed_levels[sid])
