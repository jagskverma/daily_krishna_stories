#!/usr/bin/env python3
# Style normalization pass v1 — n038 (DKS_0223..DKS_0228)
import json, os

BASE = '/Users/dev_env/Documents/projects/indian_apps/dailyX/daily_krishna_stories'

NEW_STORIES = {}

NEW_STORIES['DKS_0223'] = '''Krishna, the lord of Dwaraka, had brought his queens to a festival on Mount Raivataka. The day belonged to Rukmini, his first wife: the sage Narada — a wanderer who moved freely between the worlds — had arrived with a flower from the gardens of heaven, the Parijata, and the flower had gone to Rukmini. Now Narada sat with her, praising it, and one face was missing from the circle of Krishna's wives. Satyabhama was gone — and Krishna knew, before anyone told him, where she had gone and why.

Under some pretext he rose and left the festival, walking quickly toward the mansion on the hill that Vishvakarma, the gods' master builder, had raised for Satyabhama. He had left his son Pradyumna to entertain Narada, and his charioteer Daruka waited at the gate. Krishna entered alone. His queen, he knew, was burning with jealous anger, and the knowledge made his steps slower and heavier as he climbed.

From the doorway he saw her in the room her maids called the apartment of anger, in the midst of her handmaids, sighing hot and fast. She laughed a mocking laugh at a lotus she held near her face, nipping its petals with her nails. She traced lines on the floor with one toe. She sat with her face resting on her palm. She took sandal paste from a maid's hand, touched it to her breast, and flung it aside as if it had stung her. She lay down on her bed, then sat up, then lay down again. Krishna watched the whole restless theater — a woman determined to be angry at the only man she loved — and did not announce himself.

At last she laid her head on the pillow and drew her veil over her face. This was his moment. He signed to the handmaids to keep silence, crossed the room with careful steps, took up a fan, and stood beside her, fanning her slowly and laughing a little under his breath.

The Parijata flower had left its perfume on him, and the fragrance drifted through the chamber — heavenly, rare, unmistakable. Satyabhama smelled it and wondered. She threw the veil back. "What is this?" Without a single glance at her husband she questioned her maids about the scent. They could only kneel, faces to the floor and palms pressed together. Perhaps the earth herself had breathed out one of her own precious perfumes, she thought — and then, looking about her, her eyes fell on Krishna. "Ah — you," she said, and her eyes brimmed at once, love and jealousy crowding each other. Pouting and sighing, she turned her face away. Then she frowned, and with her eyes lifted she said: "You look very beautiful." The tears she had been holding spilled down her cheeks like dew shaken from lotus petals.

Krishna went to her at once and caught the falling tears in his hands, then wiped with his own fingers the tears that reached her breast. "Why do tears fall from your eyes like dew from a pair of lotuses?" he asked gently. "Why does your face wear the look of the full moon in a morning sky, or of a lotus at noon? And why, today, are you dressed in plain white — the color a lady wears only when she worships the gods — instead of the safflower-sprinkled, gold-dusted silks you love?"

She had no answer yet, and so he gave her his own. "As flame lives in fire," he said, "so my love lives in you — and in you alone."'''

NEW_STORIES['DKS_0224'] = '''The trouble on Mount Raivataka had begun with a flower. Satyabhama, Krishna's queen, had shut herself into her rooms because of the Parijata that the sage Narada had brought — a flower from heaven that had found its way to Rukmini's hair, and not to hers. Krishna had followed her, and by gentleness had won his way past her silence. Now he sat close to her and asked her to name the grief itself. Her sorrow, he said, seemed to burn through all his limbs. If there was no harm in it, if it was fitting for a husband who loved her to hear it, he begged her on his life to reveal it.

At last she spoke, her voice choked with tears. "It was you yourself who raised me to honor and good fortune in the old days, and they grew famous through the world. Because I was the wife you loved best, I held my head higher than anyone. But my maids tell me that today I am laughed at — by your other wives, and by strangers too. The Parijata flower that Narada gave you, you gave to your dear Rukmini, and thought nothing of me. By giving her that priceless thing you have shown everyone where your heart lies. Narada praised her in your hearing, and you were pleased to hear your beloved praised. And even if the sage had his reasons — why was my name never spoken in all of it?"

"And if I am to repent of having tasted the sweetness of your love," she went on, her voice rising, "then I would rather have none of it. Grant me leave to go. I could not have believed, even in a dream, that you would honor another above me — yet it has come to pass, awake, before everyone's eyes. Perhaps the sage Narada has grown fond of her; what cuts me is that you sat there through it all. You have always told me that people live for honor. Dishonored as I am, I have no wish to live. My protector has become my terror."

"Cast off by you, I shall wither like a white lily. How could I look again on these Raivataka hills in their spring flowers? How could I breathe this breeze, ringing with cuckoo song and fragrant with blossom? How could I watch the sea below the hill, where I once rested on your lap in the water? You told me once, 'Daughter of Satrajit, there is no wife dearer to me than you.' What is left of that promise now? Who remembers it?" Her voice broke into bitter laughter. "I never knew you for a cheat before. Now I find you fickle and false, partial to my rival. I read your thoughts in your face, thief, however you try to hide them. Your tongue is honey — and your heart is guile."

Then Krishna spoke. "Say no such thing, dearest ruler of my heart. What more can I tell you, my darling? Know that I am yours entirely. To please me, the sage Narada, whose deeds are beyond reproach, gave her that flower out of generous feeling and regard — I did not give it with my own hands."

And then Krishna made the promise that answered everything. "What is a single flower?" he said. "I shall fetch the Parijata tree itself — the best of all trees, from the gardens of paradise — and keep it in your mansion. So be it. From this day, it is my first concern."

The storm in Satyabhama's eyes faltered. She had asked, in her grief, only to be remembered; he had answered by promising her a tree from heaven — not the flower that had wounded her, but the whole tree it had grown from, to be rooted in her own courtyard. Whatever she had expected from her accusation, it was not this.'''

NEW_STORIES['DKS_0225'] = '''Narada was preparing to leave Dwaraka when Krishna, the lord of the city, stopped him with an errand to heaven. The sage who moved so freely between the worlds had come at just the right moment, for Krishna had made a promise to his queen Satyabhama — and the promise required the one thing no man could simply take: the Parijata tree itself, which grew only in Indra's paradise.

"Go to heaven," Krishna said, "and speak with the courtiers of Indra's court. Remind the king of the gods of the love between us from the old days, which you know well — and tell him this is my request, not my command. The Parijata tree was created long ago by the great sage Kashyapa for the happiness of Aditi, mother of the gods. It is the finest of all trees; it grants religious merit and boundless fortune, and it was given once as a gift to the goddesses themselves when they fulfilled their vows. My wives have heard of it, and they wish to give it away in their turn, to earn the merit of generous deeds and to please me. Ask Indra, therefore, to send the tree down to Dwaraka. It will be restored to heaven once the ceremony of giving is over."

He paused, and added: "Put all your skill into persuading the lord of the immortals to part with the tree. It will bring honor to your powers as an ambassador — and I know that everything you undertake is attended with success."

Narada smiled. "Very well," he said. "I will speak to the lord of the gods as you ask. But I am certain he will never part with the Parijata." And then, because the sage had seen more of the worlds than anyone, he told Krishna the tree's long history.

"The gods and the demons won the Parijata when they churned the ocean with the great mountain Mandara, seeking the treasures of the deep. When the tree rose from the waters, the great god Shiva wanted to carry it away to his mountain Mandara. Indra went to him in person and entreated him: 'This is Sachi's pleasure tree; let it stay in her gardens.' Shiva granted the boon — 'So be it' — and did not take the tree to the mountain. That is how Indra saved the Parijata from Shiva's own hands, by calling it his queen's."

"Nor was that all. Later, to please his wife Uma, Shiva created on the slopes of Mandara a forest of Parijata trees a full four miles across — a wood lit by its own light, into which neither the rays of the sun nor the cool beams of the moon nor even the breath of the wind could enter, and where heat and cold came and went at the pleasure of the mountain's daughter. None could enter it but the god and the goddess, their followers, and myself. There the Parijatas rained gems and jewels at a mere thought, and Shiva's own attendants took their pleasure in the wood by their lord's leave."

"Once," Narada said, "a mighty and dreadful demon named Andhaka, swollen with pride in a boon he had won, dared to force his way into that forest — and Shiva struck him down, though the demon was ten times stronger than the great demon Vritra and could not be slain by any created being. I tell you truly, Krishna: Indra, the thousand-eyed king of heaven, will never give you the Parijata, won at such cost. It grants queen Sachi every wish she makes, and it fulfils the desires of Indra himself."

Krishna heard the sage out in silence. Then he gave his answer. "If the lord of the immortals will not give up the tree at your request, I shall hurl my mace at his breast."

And so the request, it turned out, carried a warning folded inside it. Narada set out for heaven bearing both — a brother's plea, spoken out of the old friendship between the two houses, and a warrior's threat, spoken in the same breath. Which one Indra would hear first was now the only question.'''

NEW_STORIES['DKS_0226'] = '''In the court of heaven, the sage Narada stood before Indra, the king of the gods, and the message he carried was not the one Indra had hoped to hear. His brother Krishna, the lord of Dwaraka, wanted the Parijata — the tree he had promised his wife Satyabhama — the very tree that bloomed in Indra's pleasure garden, the Nandana forest, where its blossoms were said to scent the air of heaven.

The request had been made as one brother makes to another. Krishna expected indulgence, Narada reported, because he was Indra's younger brother, and he had sent his words with courtesy. But he had sent a warning too: neither god nor demon, neither the musicians of heaven nor the great serpents of the deep — no power in any of the worlds — would turn him from his pledge. If Indra refused the tree when it was asked in friendship, Krishna would come to heaven himself and hurl his mace at the breast of the king of the gods, the breast where queen Sachi lays her fragrant ointments.

Indra heard him out, and the grievances of a lifetime gathered behind his eyes. Had he not forgiven Krishna again and again, remembering only that the boy was his brother? When the Khandava forest burned, Krishna had driven Arjuna's chariot and kept Indra's rain clouds away, letting the great fire rage on. When Krishna lifted the Govardhana hill to shelter the cowherds of Vrindavan, he had done it by setting aside the worship that belonged to the lord of rain. When Indra had asked his help against the demon Vritra, Krishna had answered only that he was impartial and looked on all creatures equally — and so Indra had slain Vritra with his own arms. And in every war between the gods and the demons, Krishna fought as his own will pleased, never troubling himself about the authority of the king of heaven.

Narada listened, and then spoke plainly. He had tried to turn Krishna from this course, he said; he had set reason after reason before him, and the lord of Dwaraka had heeded none. To Indra he offered the counsel of a friend: it seemed better to let the Parijata be transplanted to Dwaraka than to let a quarrel split the house of heaven.

But Indra's mind was already made up. "Let the sage carry this answer to Krishna," he said. "Our father Kashyapa and our mother Aditi have gone into the waters on a sojourn, and this matter should rightly be laid before them — for what has my brother done but abuse his elder, and that at the urging of his wife? Shame on women," the king of the gods said, "and shame on the influence of pride — that even Vishnu, led by his wife, should insult me this day." He remembered what his parents and Brahma himself had taught him: that there is no friend like a brother, and that a wise, well-behaved brother is dearer to a man than thousands of sons. "The demons fight me because they are not my brothers," he said. "Only a brother could wound me so. I will not be the one to begin a rupture among kin. Let my brother's challenge be set before our parents when they return."

Narada waited until the king of the gods had said all he meant to say. When Indra fell silent, his answer stood clear and final. "Until I am conquered in battle by Krishna," he declared, "I will not part with the Parijata tree. Go, and tell him I am prepared for the quarrel."

So Narada bowed and left the court of heaven, carrying the challenge back to Dwaraka. And the king of the gods, who had once unleashed storms upon the world for the sake of his pride, sat waiting for the brother who had promised to come.'''

NEW_STORIES['DKS_0227'] = '''Krishna, the lord of Dwaraka, came to heaven the way daylight comes to a garden — openly, and before the eyes of everyone. Indra had refused to part with the Parijata tree, the heavenly tree Krishna had promised his queen Satyabhama, and so Krishna had come to take it himself.

He had left Dwaraka that morning under the pretext of a hunt, riding out to the Raivataka mountain with Satyaki, his friend and fellow warrior. There he handed his chariot to his charioteer, Daruka, told him to wait and groom the horses, and promised to re-enter the city on that very car by evening. Then, with Satyaki beside him, he mounted the great bird Garuda, king of all birds, and his son Pradyumna followed behind in a chariot swift enough to course over the hills. In the space of a breath, Krishna stood in the Nandana forest, the pleasure park of the gods, where hosts of celestial warriors kept watch with weapons in hand and the finest trees of heaven grew in long, ordered avenues.

He did not linger. Before the guards could gather themselves, Krishna tore the Parijata tree from the earth and set it on Garuda's back. And then a strange thing happened: the tree seemed to awaken, and to bow before the one who had taken it, as a living thing bows in homage. "Do not fear," Krishna said to it gently. When he was sure it was firmly placed, he circled the stronghold of the gods once, the great tree riding behind him on the king of birds, its branches still heavy with blossom.

The keepers of the garden did not wait to see more. They ran to Indra with the news, and the sound of their running reached the king's court before their words did: the finest tree in heaven was being carried away.

Indra came out mounted on Airavata, his great elephant, with his son Jayanta following on a chariot, and found Krishna at the eastern gate of heaven. "Krishna," the king of the gods called out, "what is this?"

Krishna, seated on Garuda, bowed his head in salute to his elder. "I am only taking away this excellent tree," he said, "for a ceremony your sister-in-law Satyabhama wishes to hold."

But Indra had given his answer to Narada, and he would not soften it now. "You should not take away this tree without challenging me to fight," he said. "Strike the first blow at me, Krishna — keep your promise, and hurl your mace at me."

So the brothers began. Krishna loosed arrows fierce as thunder at the great elephant; Indra loosed arrows of heavenly make at Garuda and cut Krishna's shafts from the air as they flew. Krishna, smiling, cut off Indra's in turn, and the two lords of earth and sky stood in the open sky severing each other's arrows, bowstring answering bowstring. At the twang of Sharanga, Krishna's own bow, and the thunder of Indra's together, the dwellers of heaven themselves swooned away.

While the duel raged, Jayanta slipped toward Garuda and tried to pull the Parijata from the bird's back. "Stop him," Krishna said to Pradyumna, and at once his son turned and barred the way. The two young warriors faced each other from their chariots — Jayanta piercing Pradyumna with sharp arrows, Pradyumna answering shaft for shaft — until a fierce combat blazed between the son of Indra and the son of Krishna, as though the quarrel of the fathers had passed whole into the hands of the sons. The gods and the sages, the perfected Siddhas and the singing Charanas, all looked on, struck with wonder at what they saw.

And then, from the host of heaven, a new champion began to advance — a messenger of the gods named Pravara, of great strength, making straight for the tree on Garuda's back. Krishna marked him and spoke one quiet word to Satyaki. "Oppose him, even from where you stand." And Satyaki, who had never refused his lord anything, moved to meet the champion of heaven.'''

NEW_STORIES['DKS_0228'] = '''Among the warriors of heaven there was one whom no weapon could slay. His name was Pravara, and his story was strange for a fighter of the gods: he had been born a Brahmana — a priest and scholar — on the great island of Jambu, where mortal men live, and he had won his way to heaven through the merit of his penances. There he had earned the friendship of Indra himself, and Brahma, the creator, had granted him a boon: that he could never be killed. In the service of the king of the gods he had become a messenger of heaven, accomplished in mighty weapons, able to subdue all foes. And now, in the battle over the Parijata — the tree that Krishna, the lord of Dwaraka, had promised his queen Satyabhama and come to heaven to take — Pravara came forward to prove his worth.

He moved straight for the tree on Garuda's back, and Krishna marked him at once. "Satyaki," he said, "oppose him, even from where you stand."

Satyaki was no stranger to impossible work. He was a warrior of Krishna's own clan and had stood beside him through the wars of Mathura and Dwaraka; he had never yet refused Krishna anything. He nocked an arrow and rode to meet the champion of the gods, while the host of heaven fell back on either side to give the two warriors room.

The duel that followed was like no other in that long morning. Pravara was a master of the bow, and the boon of Brahma hung over him like a second skin. Shaft after shaft Satyaki loosed, and shaft after shaft Pravara met in mid-air, cutting the arrows down before they could reach him. When Satyaki's bow sang, Pravara's answered; and again and again the champion of heaven struck the bow from Satyaki's hand, disarming him before the eyes of the watching gods.

A lesser man would have been broken by the shame of it. Satyaki only bent, retrieved his bow from the air or the dust, and returned to the fight. His arrows flew straighter for each humiliation, and though he could not wound the immortal champion, he gave him no rest, closing the ground between them again and again so that Pravara had no moment to look past him. The gods and sages who had gathered to watch the brothers' quarrel found themselves watching this instead — a mortal warrior holding his own, by pure refusal to yield, against a man who could not lose. They saw the bows flash and the chariots turn in the narrow sky, and not one of them could say when Satyaki had last given ground.

Then Pravara tired of the game. He had not come to heaven to trade arrows with a mortal, however stubborn. Turning his mount, he made for the Parijata, reaching for the tree that rode on Garuda's back.

And the king of birds, who had borne the tree through the whole battle without moving, moved at last.

One blow of Garuda's wings — one vast, sweeping stroke — and the champion of heaven was gone. Pravara and his chariot together were hurled a full four miles back through the sky, tumbling end over end, until they struck the ground and lay still. The warrior whom no weapon could slay had been felled not by arrow or mace, but by a wing. His chariot lay where it had struck, and he lay senseless within it.

The gods stared. The duel between the brothers paused, as if heaven itself needed a moment to understand what it had seen. And Satyaki, bow still in hand, took his place beside the tree — the one guard of the Parijata that no champion of heaven, it seemed, could pass. And while heaven still stared at its fallen champion, the king of birds was already turning his eyes toward the elephant below.'''

# Apply
changed_levels = {
    'DKS_0223': 'major', 'DKS_0224': 'major', 'DKS_0225': 'major',
    'DKS_0226': 'minor', 'DKS_0227': 'minor', 'DKS_0228': 'minor',
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
