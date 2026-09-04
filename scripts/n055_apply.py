# -*- coding: utf-8 -*-
"""Style-normalize DKS_0325-0330 per docs/HOUSE_STYLE_GUIDE.md (pass v1)."""
import json, os

BASE = 'data/stories/'
REPORT = 'data/mining/style_report/n055.jsonl'

NEW_STORIES = {}

NEW_STORIES['DKS_0325'] = """The king of Sonitpura learned of his daughter's guest the way kings learn such things — late, and from other mouths.

Aniruddha — whose father was Pradyumna and whose grandfather was Krishna of Dwaraka — had come to Bana's city the way he had come to Usha's dream: without warning, and utterly. Usha, Bana's daughter, had seen him in a vision and chosen him for her husband by the gift of a goddess, and she had pined for him so sorely that her friend Chitralekha crossed the sky to Dwaraka to fetch him. There the sage Narada blessed her errand and gave her the Tamasika art, a secret learning with the power to beguile the minds of a whole world. By it she passed into Aniruddha's palace, where the prince sat among the loveliest women of his court, wine in his hand and his thoughts far away, and she knew at once that his heart was busy with the dream. She spoke to him of Usha — how the maiden wept and sighed because she could not see him, how she would live if he came to her and die if he stayed away. And when at last he slept, she carried him through the sky to Sonitpura, to the rooms where Usha was waiting.

Now the dream had a body. In the women's quarters of Sonitpura, Usha and Aniruddha lived as bride and groom, and for a little while the city of the thousand-armed king kept its secret.

But no secret survives long among the watchful. Word reached Bana that his daughter was living with a stranger of the Yadava clan — a prince of Krishna's own family — who had come unbidden into his house and into her chambers. The king did not go himself, and he asked no questions. He sent his demon soldiers with a single order: kill the intruder.

They found Aniruddha at ease, and they paid for the surprise. The young prince seized a dreadful parigha, a great iron club, and fell upon them, killing the demons who pressed closest. Then, single-handed, he drove the whole host from the field. The soldiers of Sonitpura scattered before one man, as though the city had sent its army against a single storm.

When the field lay empty, Aniruddha stood among the fallen, threw back his head, and let out the long, delighted cry of a victor who has enjoyed his fight — a lion's shout that rang across the rooftops of Sonitpura.

The shout carried into the king's palace, and Bana understood what his soldiers could not do. But the king of a thousand arms had other instruments than an army, and before long the prince who had emptied the field would find himself a prisoner in the very city he had just won."""

NEW_STORIES['DKS_0326'] = """In the dark of Bana's prison, the young man who had routed an army had nothing left but his voice.

He had come to Sonitpura in the night — Aniruddha, grandson of Krishna, stolen from Dwaraka by enchantment to marry a princess he had only ever seen in a dream. For a little while the dream had kept its promise. Usha, Bana's daughter, had chosen him by the gift of a goddess; her friend Chitralekha had carried him across the sky in secret; and for a few days the two had lived as husband and wife in the women's quarters of the city. Then Bana — king of Sonitpura, son of the great demon Bali of an older age — learned that his daughter was living with a prince of Krishna's own family. He seized Aniruddha and threw him into chains, and Usha, who would not be parted from her husband, was bound beside him. The hero of the field was now a prisoner, held by a strong noose of serpents, his strength useless and his club far away.

And it was there, in that darkness, that Aniruddha did the one thing left to him: he sought refuge with the goddess Kaumari, the maiden goddess, and sang her a hymn.

It was a careful song. First he saluted Narayana, the changeless Lord of all. Then he praised the goddess herself — Chandi, whom the wise also call Katyayani — whom gods, sages, and demons alike worship. She was the sister of Indra and of Vishnu, close kin to the family he trusted, she who grants honour and answers the prayers of her devotees. He bowed low for his own well-being, and with a cleansed mind and folded hands he asked one thing only: “Release me from my bonds, and give me life and health.”

The goddess heard him, for she loved those who called on her, and Durga herself came to the cell where Aniruddha lay in chains. She appeared before the young hero in the gloom of the prison and consoled him; he saluted her, and then — with her own fingers, as easily as a mother loosens a knot — she cut the strong noose of serpents that held him.

And then she spoke. “Wait here a few days more, Aniruddha. He who holds the discus, the slayer of demons, will cut off Bana's thousand arms, set you free from your fetters, and take you to his own city.”

She did not carry him out of the prison. She cut his bonds, gave him a promise, and left him with something stronger than freedom: the certainty of rescue. Aniruddha waited — and across the sky, already flying toward Sonitpura on the great bird Garuda, came Krishna with his brother Balarama and with Pradyumna, Aniruddha's own father, to make the goddess's words good."""

NEW_STORIES['DKS_0327'] = """The city of Dwaraka had turned out to see its heroes leave. Aniruddha — Krishna's young grandson, the son of Pradyumna — had been carried off to the city of the demon king Bana and lay captive there, and Krishna meant to bring him home. Conches and war-horns sounded, bards sang the heroes' praises, and the people shouted blessings for victory. But no chariots stood ready in the streets and no army was mustering, for when the time came to go, Krishna did not call for horses or soldiers at all. He thought of Garuda, and the great bird was there at once, wings folded, waiting.

That day Krishna chose to go to war as a god goes, not as a man. Desiring to kill Bana, he took a form with eight arms, towering like a mountain, with countless heads. In his four right hands he carried the sword, the discus, the club, and arrows; in his four left hands, the shield, the great bow Sharanga, the thunderbolt, and the conch. Behind him on Garuda's back sat Balarama, white-armed and white-weaponed, shining like the rising moon over Mount Kailasa. And Pradyumna, eager to show his prowess in battle, had taken a form radiant as the sage Sanatkumara.

Then Garuda rose, and the great bird's beauty, touched by the radiance of the one who rode him, grew immense. The beating of his wings shook mountains and checked the very course of the wind. With the speed of thought he crossed the breadth of the heavens, and the sky itself seemed to part before him.

Halfway across the world, Balarama looked down at his own arms and frowned. “Krishna,” he said, “what wonder is this? We have lost our radiance, all of us — we have turned golden. What is the cause? Have we come to the side of Mount Sumeru?” Krishna smiled. “I think Bana's city is near at hand. A fire burns there to guard it, and its glow has fallen on us. The light of that sacred fire has changed our colour.” “Then if the road to Bana's city costs us the lustre of our bodies,” said Balarama, “let it. Do what seems right to you.” Krishna turned to Garuda. “Find us a way past this fire,” he said. “When you have, I will do what must be done.”

Garuda could take any form he wished, and now he took a thousand mouths at once. He flew up to the celestial Ganga — the river of heaven — drank deep of its water, and came back showering it down upon the fire. The blazing guardian of the city hissed and died out. Even Garuda was astonished. “How strong was this fire,” he said, “like the fire that ends an age. It changed the colour of Krishna himself.”

Then the servants of that fire came out against them — the fire-gods themselves, who had watched over the city's flame. They saw three dreadful men of many forms riding on a giant bird, and asked one another who they were and why they had come. They could not settle the matter, and so they attacked. A great uproar rose as the fire-gods and their armies fell upon the three heroes.

Their chief, the fire-god Angira, climbed onto a blazing chariot and lifted his mace, burning bright in the middle of the field. Krishna was angered, and he called out to them: “Fire-gods, wait patiently a few moments. The time of your destruction is drawing near. Within a moment, burnt by the strength of my weapons, you will fly away on all sides.” But Angira rushed at him with a burning trident, as if to take his life. Krishna cut down his mace with crescent-shaped arrows and struck him in the breast with an arrow like death itself. Angira fell. And the rest of the fire-gods, with their hosts, fled headlong toward Bana's city.

The sky fell quiet again. Far ahead, over the edge of the world, the towers of Sonitpura rose into view — the city where Aniruddha lay bound, waiting to be rescued. Garuda gathered his wings for the descent, and the three riders of the sky looked down upon the city of the demon king."""

NEW_STORIES['DKS_0328'] = """The weeping began in Aniruddha's palace and did not stop. Krishna's young grandson had vanished from his own home; how he had been taken, or by whom, no one in Dwaraka could say.

His wives and their companions wept in his empty rooms like ewes crying for a lost lamb. “Even under the protection of Krishna we are grieving,” they cried. “The gods themselves live without fear in the shelter of his arms — and yet his own grandson has been carried off. Who has stolen him away? Whoever did this has no fear left in the world, but he stands before the open teeth of Death.”

Their cries rose over the palace like the noise of ospreys crying in the sky, and the whole city heard. The Yadu chiefs rushed out of their houses as lions come from their caves when roused. “Krishna protects us completely,” they said to one another. “Why this fear, then? What is this uproar in Aniruddha's house?” The great war-bugle of Krishna's court was brought and sounded, and at its call the Yadavas — the warriors of Krishna's clan — assembled. They asked one another what had happened, and each answered with the little he had heard. The eyes of those grim warriors, red with anger, filled with tears; they sat and sighed, helpless.

Only one of them spoke. Viprithu, a Yadava chief, looked at Krishna — who sat sighing again and again — and said: “Krishna, foremost of men, why are you troubled? Your people live freely under the shelter of your arms. Leave the care of success and defeat to you, and even Indra, the king of the gods, sleeps peacefully. But your kinsmen are sunk in a grief they cannot measure. Save them. What is the cause of your worry? Why do you not speak? Do not sit brooding in silence.”

Krishna sighed for a long time before he answered. “Viprithu, I have been anxiously thinking about this. Even thinking, I have not been able to settle anything — that is why I could not answer you. Hear the truth. Because of Aniruddha's captivity, every king on earth and all my friends will think me powerless. Once an enemy king named Shalwa carried off our king Ahuka himself, and we brought him back after a dreadful fight. And the demon Shamvara stole Pradyumna, Rukmini's child and my own son, while he was still a baby — but Pradyumna slew his captor and came home. Where has Aniruddha been taken? I do not remember ever feeling sorrow like this. And I will kill in battle, with all his people, the one who has set an ash-covered foot upon my head — who has dared to shame me so.”

Then Satyaki, Krishna's kinsman and a trusted warrior, spoke: “Krishna, send spies in every direction to find Aniruddha. Let them search the earth with its mountains and forests. Let open and secret messengers be sent out on this work.”

King Ahuka heard, and acted at once. He gave the messengers horses and chariots. “Search every country on the earth and under it,” he ordered. “Go soon, on horseback. Search the mountains Rikshavan and Raivataka, covered with trees and creepers. Enter the gardens and forests without hesitation; look into every creek and corner. On horses and on elephants, find Aniruddha, the joy of the Yadavas.”

They went. They searched the mountains and the forests, the cities and the hidden places, the countries above the earth and below it — and they came home empty-handed. “We saw Aniruddha nowhere,” the messengers said. The great hall of Dwaraka fell silent again, heavier than before. The search was over, and the waiting had begun."""

NEW_STORIES['DKS_0329'] = """The search parties had come home empty-handed, and the great hall of Dwaraka had settled into a gloom no one knew how to break. The messengers had combed the mountains and the forests, the cities and the hidden places, and their only report was the same weary sentence: “We saw Aniruddha nowhere.” The Yadavas asked one another the same question — where was the boy? — and had no answer. Then, without warning, an answer walked into the room.

Narada had arrived — the sage who wandered through all the worlds, carrying news from every court. The assembly fell quiet around him, for Narada always knew what other men did not.

He told them what he had seen. In the city of the demon king Bana — Sonitpura, ringed with its guardian fire — there lived a daughter named Usha. For her sake, said the sage, the apsara Chitralekha, a dancer of the celestial courts and a mistress of illusion, had carried off Aniruddha and brought him to the demon's city. That was the theft: not an enemy raid, not an ambush on the road, but a girl's longing and an enchantress's art, reaching into Dwaraka itself and taking the prince away.

And Bana? When the king of Sonitpura learned that Krishna's own grandson lay in his city, he had the young man bound in serpent-nooses, fetters strong enough to hold even a warrior, and kept him prisoner there. The Yadavas knew the king's name, and they knew his city, guarded by its fire and by the armies of the demons who served him. The prince who had vanished from the middle of Dwaraka lay in the heart of the enemy's stronghold.

But one word in Narada's report changed everything: Aniruddha still lived. Bound he was, but alive — the nooses had not taken his breath, and Bana's rage had not yet reached the point of killing him. The name of the city, the name of the demon, and the certain knowledge that the boy still breathed passed through the hall like water poured on a burning house. The wives who had wept in the palace, crying that even under Krishna's protection they were lost, heard that their lord still lived. Where there had been only helpless grief, there was now a place, a name, and a hope.

Krishna heard the sage out, and the anxiety that had weighed on the court for days at last had somewhere to go. His own messengers had searched the mountains and the forests and found nothing; Narada had walked into the palace and handed them the whole truth — where Aniruddha was, who had taken him, and that he still lived. It was enough.

Dwaraka turned its face toward Sonitpura, the far-off city of the demon king, where a bound prince still breathed in his chains and waited to be brought home."""

NEW_STORIES['DKS_0330'] = """The war to free Aniruddha had reached its strangest hour. Krishna had come to the demon city of Sonitpura with his brother Balarama and with Pradyumna — his own son, and Aniruddha's father — to take the boy back from Bana, the thousand-armed king who held him prisoner. Shiva himself had fought for Bana that day, and then withdrawn from the field. Now a second god took his place. Kartikeya, the war-god and Shiva's son, drove straight at the three of them on a chariot sent by Kumbhanda, Bana's minister, and struck them with hundreds of sharp arrows.

Bathed in blood, the three fought back like three fires against the wind. They answered with the three weapons given to them by the wind-god, the fire-god, and Indra, the king of the gods. Kartikeya met each with a weapon of his own — Shaila, Varuna, and Savitri. But by their powers of illusion the three swallowed up every missile the burning god hurled at them. Nothing he shot could touch them.

Then Kartikeya, blazing with rage and biting his lips, took up his deadliest weapon: the Brahmashira, the head of Brahma the creator — a missile like the fire that ends a world. When he loosed it, it blazed with the light of a thousand suns, and it seemed made to destroy the world. Creatures everywhere lost their senses in its heat and fled; the whole universe cried out.

But Krishna took up his discus, the weapon that answers and cancels every other weapon. As clouds in the rainy season cover the rays of the sun, so the discus covered, with its light, the light of the Brahmashira. The world-destroying missile was shorn of its glow, its power, its fury, and hung harmless in the sky.

Kartikeya's rage flamed higher, like fire into which butter is poured. He seized his golden spear, the Sakti — sure of aim, hung with bells, glowing like a burning brand — and with a shout that struck terror into his enemies he hurled it at Krishna. The spear rose into the sky, opened wide, and circled above the field, as though searching for the heart of the one it was meant to kill. The watching gods lost heart. “Perhaps Krishna will be consumed,” they said.

Then the spear came down before him. Krishna shouted, a shout like a warning, and struck it out of the air to the ground. “Well done! Well done!” rose from every side of the field, and Indra and the gods sent up a leonine roar of their own.

Krishna lifted his discus again, to end the war with the god. But at that moment, at Shiva's command, the goddess Kottavi appeared before Kartikeya and shielded him with her unclothed body, and beside her stood Lamva, an eighth part of the goddess herself, bright as a golden spear. Krishna stayed his hand. “Shame on you,” he said to the goddess. “Fly away from this place. Why do you throw yourself in the way of certain destruction?” But she would not cover herself, and she would not move. “Take Kartikeya and fly away from the battlefield,” Krishna told her. “It will be well for us today if you do this. If I hold back from the fight, he will fight me himself.” And the lord of Dwaraka put away his discus, rather than strike through her.

The goddess led the war-god from the field and brought him safely before Shiva. And then the king of the demons came forward. When Bana saw Kartikeya carried off safe from Krishna's discus and retiring from the battle, he felt the wish to fight Krishna himself. His priests chanted blessings over him, murmured the sacred mantras, and performed the rites of victory with herbs and holy words, while the great demon commanders gathered around their king. And Bana marched out to meet the lord of Dwaraka.

Krishna, who had set aside his discus rather than strike through a goddess, turned to face the demon king as he came."""

GRADES = {
    'DKS_0325': 'minor', 'DKS_0326': 'minor', 'DKS_0327': 'major',
    'DKS_0328': 'major', 'DKS_0329': 'minor', 'DKS_0330': 'minor',
}
CONTEXT = {'DKS_0325': True, 'DKS_0326': True, 'DKS_0327': False,
           'DKS_0328': True, 'DKS_0329': False, 'DKS_0330': True}
AI_PATTERNS = {
 'DKS_0325': [
  "contradictory pairing removed: 'stolen the sleeping prince out of his own palace' sat beside an awake scene with 'wine in his hand'; resequenced to found-at-ease, then carried off 'when at last he slept'",
  "opaque epithet 'found him where the moon sits among stars' dropped from the palace scene",
  "unexplained 'his Tamasika learning' glossed in place: 'a secret learning with the power to beguile the minds of a whole world'",
  "translation trio 'wept, and yawned, and sighed' trimmed to 'wept and sighed'",
 ],
 'DKS_0326': [
  "scripture-register hymn de-listed: stacked epithets ('endless, undecaying, eternal prime deity') collapsed to 'the changeless Lord of all'; 'whom all the gods and all the worlds worship' folded into one plain clause",
  "unexplained goddess-name chain (Kaumari, Chandi, Katyayani, Durga) now reads as one address: 'the goddess herself — Chandi, whom the wise also call Katyayani'",
  "trailing recap 'came Krishna, Balarama and Pradyumna' now identifies Balarama as Krishna's brother and Pradyumna as Aniruddha's father instead of leaving them as bare names",
 ],
 'DKS_0327': [
  "send-off scene de-contradicted: 'The city sent its warriors to war with music' plus 'Krishna did not call for chariots or mustering armies' rewritten so the city turns out to see the heroes leave by sky — no army is ever implied or cancelled",
  "stilted source-dialogue echo 'do what you think proper' (twice) recast once, as 'Find us a way past this fire… I will do what must be done'",
  "route catalogue 'the sacred path of the Siddhas and Charanas' simplified to 'the breadth of the heavens'",
  "'holding a thousand forms' dropped from Balarama's description; 'innumerable heads/mountains' → 'countless'",
  "repeated Krishna-smiling before the fight removed ('Krishna, angered, smiled again and again')",
 ],
 'DKS_0328': [
  "three long translation-register speeches (wives' lament, Viprithu's plea, Ahuka's search order) condensed from full quotation into narration with brief natural quotes",
  "stacked translation similes kept but separated into narration (ewes; ospreys) instead of one quotation block",
  "translation image 'their eyes appeared to have been bathed in blood' dropped",
  "'ash-covered foot upon my head' kept but made readable by the adjoining gloss '— who has dared to shame me so'",
 ],
 'DKS_0329': [
  "aphoristic close removed: 'Grief, when it knows where to point, becomes resolve.' now ends on the quiet image of Dwaraka turning toward Sonitpura",
  "duplicated 'searched the mountains and the forests, the cities and the hidden places' (opening and near-close) reduced to one full occurrence",
 ],
 'DKS_0330': [
  "trailer-flavoured open 'The war for Aniruddha had reached its strangest hour' recast into who/why/where context before the charge of Kartikeya",
  "closing 'the sky over Sonitpura darkened with the gathering of armies' trimmed to a quiet line ('turned to face the demon king as he came')",
  "unexplained epithet 'Madhava' replaced with 'Krishna'",
  "'devoured every weapon' → 'swallowed up every missile'",
 ],
}
CHILD_FRIENDLY = {
 'DKS_0325': [
  "Aniruddha identified up front: father Pradyumna, grandfather Krishna of Dwaraka (first-reader anchor)",
  "Usha named as Bana's daughter, tying her to the king of Sonitpura",
  "Yadava explained in place: 'a prince of Krishna's own family'",
  "Daityas/Danavas rendered 'demons'/'demon soldiers'",
  "'parigha' and 'Tamasika art' each glossed in the same sentence",
 ],
 'DKS_0326': [
  "opener ties the nameless 'young man who had routed an army' to his name and family: 'Aniruddha, grandson of Krishna'",
  "Bana glossed as 'son of the great demon Bali of an older age'",
  "'votaries' → 'those who called on her'; 'rishis and rakshasas' → 'sages and demons'",
  "Garuda glossed as 'the great bird'",
 ],
 'DKS_0327': [
  "Garuda introduced and glossed as a great bird before he acts",
  "Balarama = Krishna's brother, Pradyumna = Aniruddha's father (both named in the opening)",
  "'the effulgence of that fire of oblation' → 'the light of that sacred fire'",
  "violence restrained: 'Angira fell, bathed in blood' → 'Angira fell'",
  "weapon catalogue kept but each item plain (sword, discus, club, arrows / shield, bow Sharanga, thunderbolt, conch)",
 ],
 'DKS_0328': [
  "opener states who vanished and from where: Aniruddha, Krishna's young grandson, gone from his own home (standalone anchor)",
  "Viprithu identified as a Yadava chief; Satyaki as Krishna's kinsman and trusted warrior",
  "Ahuka identified as 'our king'; Shalwa as 'an enemy king'; Shamvara as 'the demon'; Pradyumna as 'Rukmini's child and my own son'",
  "Indra glossed as 'the king of the gods'",
  "'countries lying on and under the earth' kept plain and concrete",
 ],
 'DKS_0329': [
  "'the apsara Chitralekha — the enchantress of the celestial dancers' → 'a dancer of the celestial courts and a mistress of illusion'",
  "'fettered with serpent-shafts' → 'bound in serpent-nooses, fetters strong enough to hold even a warrior'",
  "'Aniruddha is not deprived of life' → 'Aniruddha still lived… the nooses had not taken his breath'",
 ],
 'DKS_0330': [
  "standalone opener: Aniruddha = Krishna's grandson, held prisoner by Bana, thousand-armed king of Sonitpura; Balarama and Pradyumna identified",
  "Kartikeya identified as the war-god and Shiva's son; Kumbhanda as Bana's minister; Indra as king of the gods",
  "Brahmashira glossed as 'the head of Brahma the creator'",
  "Kottavi's nudity handled with restraint: 'shielded him with her unclothed body' — the reason Krishna stays his hand stays intact",
  "'the slayer of Keshi' epithet removed from Krishna's first mention",
 ],
}
RISK = {
 'DKS_0325': "Harmonizing the sleeping/awake contradiction touched the abduction mechanics; kept the draft's own elements — 'stolen… sleeping prince' becomes 'when at last he slept, she carried him through the sky to Sonitpura' — with no new plot.",
 'DKS_0326': "Hymn condensed but every item kept: salute to Narayana, Chandi/Katyayani worshipped by gods, sages and demons, sister of Indra and of Vishnu, and the request held verbatim — \u201cRelease me from my bonds, and give me life and health.\u201d",
 'DKS_0327': "Full eight-arm weapon catalogue and the golden-stain exchange preserved while smoothing wording; Angira still falls to crescent arrows and an arrow like death itself.",
 'DKS_0328': "Krishna's speech keeps both precedents (Ahuka\u2013Shalwa, Pradyumna\u2013Shamvara) and the ash-foot vow; the wives still weep, the bugle still sounds, the search still fails with \u201cWe saw Aniruddha nowhere.\u201d",
 'DKS_0329': "Narada's report unchanged in substance — Usha, Chitralekha's abduction, serpent-nooses, and the fact that Aniruddha lives all preserved.",
 'DKS_0330': "Kottavi/Lamva scene kept whole: the goddess still shields Kartikeya unclothed and Krishna still lays down the discus rather than strike through her; only the wording was made chaste.",
}

# ---------- apply ----------
os.makedirs(os.path.dirname(REPORT), exist_ok=True)
reports = []
for sid, new_story in NEW_STORIES.items():
    path = BASE + sid + '.json'
    raw = open(path, encoding='utf-8').read()
    d = json.loads(raw)
    old_story = d['story']
    d['story'] = new_story
    d['generation_metadata']['style_normalization'] = {
        "pass": "v1", "model": "deepseek-v4-flash", "changed": GRADES[sid]
    }
    out = json.dumps(d, indent=1, ensure_ascii=False)
    open(path, 'w', encoding='utf-8').write(out)
    lb = len(old_story.split()); la = len(new_story.split())
    print(f"{sid}: words {lb} -> {la} | grade {GRADES[sid]}")
    reports.append({
        "story_id": sid,
        "changed": GRADES[sid],
        "context_added": CONTEXT[sid],
        "ai_patterns_removed": AI_PATTERNS[sid],
        "child_friendly_changes": CHILD_FRIENDLY[sid],
        "length_before": lb,
        "length_after": la,
        "risk": RISK[sid],
    })

with open(REPORT, 'w', encoding='utf-8') as f:
    for r in reports:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
print('report written:', REPORT, len(reports), 'lines')
