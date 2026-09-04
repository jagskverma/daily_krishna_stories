#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Style-normalize batch n080 (DKS_0475-0480) per docs/HOUSE_STYLE_GUIDE.md v1."""
import json, difflib, sys

BASE = "/Users/dev_env/Documents/projects/indian_apps/dailyX/daily_krishna_stories"

PATHS = {
    "DKS_0475": f"{BASE}/data/stories/DKS_0475.json",
    "DKS_0476": f"{BASE}/data/stories/DKS_0476.json",
    "DKS_0477": f"{BASE}/data/pilot_stories/DKS_0477.json",
    "DKS_0478": f"{BASE}/data/stories/DKS_0478.json",
    "DKS_0479": f"{BASE}/data/stories/DKS_0479.json",
    "DKS_0480": f"{BASE}/data/stories/DKS_0480.json",
}

NEW_STORIES = {}

NEW_STORIES["DKS_0475"] = """All through the war at Kurukshetra, Karna, the greatest archer of the Kaurava army, had carried one weapon that he never once hurled at Arjuna. It was a dart — given to him long ago by Indra, king of the gods, in exchange for the armour Karna had worn since birth and the ear-rings that belonged to it. The dart never missed. Whichever single warrior it was aimed at would fall. It was the one thing that could end the whole war in a single stroke, and from the day Indra gave it, it was meant for Arjuna.

Many times across the battles, Arjuna had come within reach. Many times Karna's hand had closed on the dart. And every time — before he could hurl it — something went wrong.

Krishna finally explained why, on a night when the two armies fought on in darkness. Speaking to Satyaki, his close friend and a warrior on the Pandava side, as the uproar of the night battle died down for a moment, he said, \"Whenever Karna reached for that dart and fixed his eyes on Arjuna, I clouded his mind. That is why the dart was never hurled at Arjuna.\"

That was the whole secret — not armour, not luck, not a vow. In the instant between drawing back the arm and letting the dart fly, Karna's thoughts would wander, the moment would slip past him, and the danger would pass before anyone on the Pandava side even knew it had come. Protection can work like that: invisible, unfelt, finished before it is ever noticed.

Then Krishna said something that had no strategy in it at all. \"I do not hold my father, my mother, my brothers — not even my own life — so worthy of protection as Arjuna in battle.\"

His father. His mother. His brothers. His own life. Arjuna stood above them all.

The words made sense of something the whole army had seen that night and not understood. When Ghatotkacha fell — Bhima's son, killed in the darkness by that very dart, spent at last on someone other than Arjuna — the Pandava host had wept. Krishna had danced. He had seemed heartless, dancing while others mourned. But he had been looking at Arjuna, alive on the field; the dart that could have taken Arjuna's life was gone forever. \"Seeing Arjuna, like one returned from the dead, still standing on the field,\" Krishna told Satyaki, \"this joy seized me.\"

The armour, the ear-rings, the dart: one by one they had been stripped from Karna, and the last of the three was spent on the night Krishna had chosen. Arjuna never learned how close the war had come to ending in a single instant, because the danger had never been allowed to arrive.

On the dark field, Krishna sat in his chariot with Arjuna alive beside him. He had protected what he valued most in the world, by means no one could see, at a cost he had already counted. And somewhere out in the night, Karna still carried his bow — not yet knowing that the weapon he trusted was gone, and that he himself, who had given away the armour of his birth, was as mortal now as any man on the field."""

NEW_STORIES["DKS_0476"] = """That same night, the war took its cruelest turn. Karna had carried through every battle a dart given to him by Indra — kept all those months for Krishna or for Arjuna; a weapon that could slay any single warrior it was aimed at, one that even the gods could not turn aside. In the black hour of night it was spent at last, not on Arjuna but on Ghatotkacha, the son of Bhima and of Hidimba, a princess of the rakshasas, a fierce and powerful race. Ghatotkacha fell, a loss that the blind Kaurava king Dhritarashtra would later wave away as nothing — as insignificant, he would say, as the crushing of straw.

Now the Kaurava troops — the army of the Pandavas' cousins and enemies — were wild with joy at the death of the young rakshasa prince. They raised loud shouts in the darkness and flung themselves at the Pandava ranks. King Yudhishthira, the eldest of the five Pandava brothers, watched his army begin to give way — and something in him gave way too. He turned to his brother Bhima. \"Resist the Kaurava host,\" he said. \"The slaughter of Hidimba's son has left me stunned.\" Bhima rode out to hold the enemy, and the king sat down on his chariot, his face wet with tears, sighing again and again. The man who had borne exile and loss without flinching sat staring at Karna's arrows, utterly without cheer.

Krishna saw him and came to him. \"Let not such grief be yours,\" he said. \"Despair like this does not become you, as it might an ordinary man. Rise, O king, and fight. Bear the heavy burden. If you lose heart, our victory becomes uncertain.\"

The words reached Yudhishthira through the noise of the night, and he wiped his eyes with his hands and answered. The path of duty was not unknown to him — but first he spoke of Ghatotkacha, and what he said was not a lesson; it was a reckoning of love. While the Pandavas had lived as exiles in the forests, Ghatotkacha, then little more than a child, had served them in a hundred ways. When Arjuna went away to win celestial weapons, Ghatotkacha came to them at Kamyaka forest and stayed until Arjuna returned. Through wild and trackless country he had carried the tired princess of Panchala — Draupadi, wife of the five brothers — on his own back. Skilled in every kind of warfare, he had done hard and difficult things for the king's sake, feats no one else could do.

\"My love for Ghatotkacha,\" said Yudhishthira, \"is twice the love I bear my youngest brother, Sahadeva. He was devoted to me, and I was dear to him. That is why grief scorches me. Look at our troops — afflicted, routed. Look at our great chariot-warriors broken before Karna's shafts.\"

His voice broke, and for a moment the night held its silence. All around, the battle pressed on: Karna's arrows still darkening the air, the Pandava host still reeling. But in the circle of that chariot there was only the king's grief and the friend who had come to answer it. Krishna had not asked the king to forget the boy. He had asked him to stand — to bear the burden, to keep the victory from slipping away. So he waited, letting the grief speak itself out, for he knew that the king's love for the dead youth was not something to be argued away.

The war did not stop for Yudhishthira's sorrow. The Kaurava shouts still rang across the dark field, and the Pandava line still had to hold. But the counsel had been spoken, and the king who had wiped his eyes with his own hands had answered out of love rather than out of despair. That, in the dark of that night, was the first step of bearing the burden again."""

NEW_STORIES["DKS_0477"] = """Drona, the great teacher of weapons who had trained the warriors of both armies, was cutting through the Pandava host, and nothing could stand before him. The Panchalas and the Srinjayas — allies of the Pandavas from the land of Panchala — rushed at him in waves, yelling as they came, and his arrows struck them down as fast as they arrived. Mighty warriors they were, full of courage, and even as he cut them down they did not yet fear him; still they came on, and still they fell. Steeds and men went down in such numbers that the field came to look like a battlefield of the gods in some older age. Fear crept into the hearts of the five Pandava brothers, and hope drained out of them. Drona alone seemed enough to undo them all. The day was theirs to lose, and he was taking it from them hour by hour.

\"He will swallow us all,\" they said to one another, \"like a fire swallowing a heap of dry straw in spring. No one can even look at him in battle. And Arjuna — the one man who is his match — will not fight him.\" For Drona had been Arjuna's own teacher, the man who had taught him the bow, and Arjuna, who honoured the ways of right conduct, would not raise his weapon against the man who had given him his skill.

It was Krishna who answered their despair. \"This greatest of bowmen cannot be defeated by force,\" he said, \"not even by the gods, with Indra at their head. But when he lays aside his weapons, even mortal men can slay him. Set aside the path of strict virtue for once, sons of Pandu, and find some way — before Drona destroys us all. When his son Ashvatthama falls, he will stop fighting. Let some man tell him that Ashvatthama has been slain.\"

It was not the kind of counsel the brothers had expected from him, and it landed among them like a stone dropped into still water. Arjuna would not agree to it; he heard the plan and refused. Others approved of it. And Yudhishthira — the eldest, the brother whose word was truth itself — agreed only with the greatest difficulty. To save his brothers he would have to become, for a little while, the bearer of a falsehood, and he accepted that burden with his head bowed. It was the hardest thing he had yet agreed to in the whole war.

So it was done, in a way that split the truth down the middle. Bhima, the mightiest of the brothers, took up his mace and struck down a war-elephant of their own army — a huge, terrible, foe-crushing beast named Ashvatthama, which belonged to Indravarman, chief of the Malava people. Their own elephant, felled by their own hand, not to win any fight but to make a single sentence true. Then Bhima approached Drona in the midst of the battle and, with some bashfulness in his voice, cried aloud: \"Ashvatthama has been slain.\"

The words were true of the elephant lying dead behind him. They were spoken to a father who would hear them as the name of his son. There is a difference between a lie and a truth spoken to deceive, and the whole weight of that difference sat in Bhima's voice. Drona had heard a thousand war-cries that day and never once turned from his work. But this one name, spoken low, would do what no weapon on that field could do. On the width of a name shared between a man and a beast, the whole battle was about to turn."""

NEW_STORIES["DKS_0478"] = """Drona came on like a fire racing through dry straw, and no one could stand before him. Teacher to both armies, he had been enraged by the fall of Bhurishravas and Jayadratha, two great champions of the Kaurava side, and now he turned his full fury on the Panchalas and the Srinjayas, the Pandavas' allies. His shafts and darts cut them down as they charged. Again and again the finest warriors of the Pandava army rushed at him; again and again they fell, until the field grew crowded with the fallen and the ground turned dark beneath the horses' feet. Fear entered the hearts of the five Pandava brothers, and their hope of victory drained away. No one dared even look at him in battle, and Arjuna — the one man who was his match — would not fight his own teacher, for he honoured the ways of right conduct.

Seeing the brothers afflicted and afraid, Krishna, who had their welfare at heart, spoke. This greatest of bowmen, he said, could never be conquered by force — not even by the gods, with Indra at their head. But when he lays aside his weapons, even mortal men can slay him. \"Cast aside the path of strict virtue for once, sons of Pandu,\" Krishna said, \"and find some way to win, so that Drona does not slaughter us all. When his son Ashvatthama falls, he will stop fighting, I think. Let some man go and tell him that Ashvatthama has been slain.\"

To Yudhishthira — the eldest, called the son of Dharma for his justice, whose whole life had been the keeping of his word — Krishna said it even more plainly. \"If Drona fights on in rage for even half a day, I tell you truly, your army will be annihilated. Save us from Drona. In such a strait as this, falsehood is better than truth.\"

Arjuna would not approve of the plan. Others approved. But Yudhishthira accepted it only with the greatest difficulty.

Then Bhima, the mighty-armed, took up his mace and slew a war-elephant of their own army — a huge, terrible, foe-crushing beast named Ashvatthama, belonging to Indravarman, chief of the Malavas. The beast was built for the front of a charge, and its fall shook the ground. Then Bhima approached Drona in the midst of the battle and, with some bashfulness, began to shout aloud: \"Ashvatthama has been slain!\" Keeping the true fact within his own mind, he spoke the untrue words across the field.

Hearing them, Drona felt his limbs go weak, as sand dissolves in water. But he remembered the prowess of his son and soon came to regard the news as false; recovering himself, he took comfort, knowing that no foe could stand against Ashvatthama. Then, filled with rage, he rushed at Dhrishtadyumna, the young prince of Panchala, and buried him under a thousand sharp arrows. Twenty thousand Panchala chariot-warriors in turn covered Drona with their shafts, until he vanished from sight in a storm of arrows. Drona scattered their arrows, invoked the Brahma weapon, a celestial weapon of immense power, and stood blazing like a smokeless fire. He struck down the Panchala warriors where they stood, and the great ones of that army fell like trees torn up by a storm. Twenty thousand Panchala chariot-warriors were slain that day; a warrior named Vasudana was cut down by a single broad-headed arrow; and with them fell five hundred soldiers of the Matsya country, six thousand elephants, and ten thousand horses.

The lie that was meant to end him had only fed his fury. Drona stood on the field as if he meant to wipe out the warrior class itself, and the great seers — Viswamitra, Jamadagni, Bharadwaja, Gautama, Vasishtha, Kasyapa, and Atri — gathered to look upon him. Even they could not turn the great teacher from his course."""

NEW_STORIES["DKS_0479"] = """From the chariot where the two of them stood, Krishna showed Arjuna the battle as only he could see it. He pointed across the field. \"There,\" he said. \"Your brother Yudhishthira is being hunted by many great bowmen of the Kaurava army, all bent on killing him. The mighty warriors of Panchala, allies of the Pandavas and hard to defeat in battle, are racing after the king to save him.\"

Arjuna looked, and Krishna read the confusion of the fight for him, piece by piece. Duryodhana himself — the Kaurava king and the Pandavas' chief enemy — was pursuing Yudhishthira with a great force of chariots, he and his brothers, warriors whose weapons stung like poisonous snakes. Elephants, horses, chariots, and foot-soldiers of the Kauravas all pressed toward the king, greedy as poor men after a precious jewel. Satyaki and Bhima had checked them for a moment, but the host was too vast; now it rolled toward Yudhishthira again like floodwater in the rainy season rushing to the sea, the warriors roaring like lions, blowing their conch-shell trumpets, shaking their bows.

\"I consider Yudhishthira as good as dead,\" Krishna said, \"caught in Duryodhana's grip — a man already poured out as an offering on the sacrificial fire.\" So mighty was that host, he said, that even Indra, king of the gods, could scarcely escape its arrows. Who could bear the fury of Duryodhana himself, who loosed his shafts in ceaseless showers and, when angry, seemed like death? The arrows of the great Kaurava bowmen — Duryodhana, Ashvatthama, Kripa, and Karna, the deadliest of them all — could break down mountains.

Then Krishna told Arjuna why the danger was graver than it looked. Not long before, Karna had forced king Yudhishthira to turn his back and flee the field. Karna fought with immense skill and speed of hand, more than a match for the eldest Pandava — especially with Duryodhana beside him. And Yudhishthira, worn thin by his fasts, strong in spirit but not in a warrior's bodily strength, had been caught by Karna's assault in terrible peril. \"I think the king has fallen,\" Krishna said. \"Bhima, who is fierce in battle, stands silent while the Kauravas roar with triumph and blow their conches. I think Pandu's son Yudhishthira is dead.\"

Then he pointed again — to Karna, urging the Kaurava chariot-warriors forward, shooting as he came, with arrows and clubs and every weapon he carried. The king's banner was no longer to be seen; Karna's shafts had likely struck it down. Before the very eyes of the two youngest Pandava brothers, the twins, and of Satyaki, Shikhandi, Dhrishtadyumna, and Bhima — before all the Panchala and Cedi troops — Karna was destroying the Pandava division with his arrows, the way an elephant destroys a bed of lotuses. Arjuna's chariot-warriors were fleeing; wounded elephants were stampeding in every direction, crying out in pain. Karna's own standard, bearing the device of the elephant's rope, moved all over the field; and there he was, rushing at Bhima himself, scattering hundreds of arrows as he came, routing the Panchala warriors as he went.

\"Set your heart rightly on the battle,\" Krishna said. \"Advance against that leader of chariot-warriors.\""""

NEW_STORIES["DKS_0480"] = """The war between the Pandavas and their cousins, the Kauravas, had come to its hardest day, and Arjuna was ready to ride against Karna — when the field put another enemy in his path. Ashvatthama, the son of Drona, the great teacher who had trained the warriors of both sides, came suddenly against him with a great force of chariots. Like a shore holding back the sea, Arjuna, with Krishna at his side, withstood that furious rush. Then Ashvatthama, mad with rage, covered both heroes with arrows, and those who watched wondered to see Krishna and Arjuna — both of them called Krishna, for both were dark as a rain cloud — standing shrouded in shafts.

Arjuna answered, smiling a little, and called up a celestial weapon. Ashvatthama, born of the priestly class yet a master of arms, turned it aside. Every weapon Arjuna sent against him, he baffled. In that terrible exchange he seemed less like a man than like death itself with open jaws; he filled every quarter of the sky with straight-flying arrows and pierced Krishna three times in the right arm.

Then Arjuna struck down all the horses of his attacker's chariot. The chariot-warriors of Ashvatthama's division fell before Arjuna's arrows, and the ground beneath the two fighters ran red. Neither showed the other any mercy; they rushed at each other again and again. Ashvatthama shook his great bow, plated with gold, pierced Arjuna from every side, and once more bending the bow, struck him hard in the chest with a winged arrow. Wounded deeply, Arjuna answered with his own great bow, Gandiva, showering the son of Drona with arrows until he cut Ashvatthama's bow in two. Ashvatthama seized a spiked mace that struck like thunder and hurled it at Arjuna. Arjuna, still smiling, cut the mace down in mid-air, and it fell to the earth like a mountain split by a thunderbolt.

Maddened now, Drona's son called up the weapon of Indra — a very storm of arrows across the sky. Arjuna strung a weapon created by Indra himself, broke the storm, and buried Ashvatthama's chariot in shafts of his own. Through that hail of arrows the son of Drona came on, and with a mighty weapon of his own he pierced Krishna with a hundred shafts and Arjuna with three hundred small arrows. Arjuna answered, piercing Ashvatthama in all his vital points, pouring arrows on his horses, his driver, and his bowstring, until a broad-headed arrow struck the driver down. Taking up the reins himself, Ashvatthama guided his horses with one hand and fought on with the other, covering Krishna with arrows as he went — a feat of skill that all the watching warriors applauded. Then Arjuna cut the traces of Ashvatthama's horses with a razor-edged arrow. The horses of Drona's son bolted, dragging the chariot away, and a great cry went up from the troops.

The duel was over. The field, which had been a storm around them, fell quiet, and Krishna and Arjuna stood together on the chariot, the charioteer's right arm still marked by Ashvatthama's arrows. Arjuna's bow still hummed in his hand, and he asked to be driven against Karna — Karna, who had wounded their army and their king, whose standard bearing the elephant's rope still moved yonder over the host. But Krishna answered: \"Your brother Yudhishthira, the king, has been deeply wounded and cut down by Karna. Go to him first and comfort him. Then, Arjuna, you shall slay Karna.\""""

LEVELS = {
    "DKS_0475": "major",
    "DKS_0476": "major",
    "DKS_0477": "major",
    "DKS_0478": "major",
    "DKS_0479": "major",
    "DKS_0480": "major",
}

results = {}
for sid, path in PATHS.items():
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    old_story = data["story"]
    old_meta = dict(data["generation_metadata"])
    old_refl = data.get("reflection")

    data["story"] = NEW_STORIES[sid]
    # reflection: kept byte-identical (all six already satisfy house style §18)
    data["generation_metadata"]["style_normalization"] = {
        "pass": "v1", "model": "deepseek-v4-flash", "changed": LEVELS[sid]
    }

    out = json.dumps(data, indent=1, ensure_ascii=False)
    with open(path, "w", encoding="utf-8") as f:
        f.write(out)

    # verify
    with open(path, "r", encoding="utf-8") as f:
        chk = json.load(f)
    assert chk["story"] == NEW_STORIES[sid]
    assert chk.get("reflection") == old_refl
    assert chk["generation_metadata"]["style_normalization"]["pass"] == "v1"
    ratio = difflib.SequenceMatcher(None, old_story, NEW_STORIES[sid]).ratio()
    before_w = len(old_story.split())
    after_w = len(NEW_STORIES[sid].split())
    results[sid] = (before_w, after_w, round(ratio, 3))
    print(f"{sid}: before={before_w}w after={after_w}w similarity={ratio:.3f} refl_kept={old_refl is not None}")

print("DONE")
