#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Style-normalization pass (v1) for wave n030: DKS_0175..DKS_0180.

Rewrites ONLY the `story` field (and DKS_0176's `reflection`), and appends
generation_metadata.style_normalization. All other fields are preserved
byte-for-byte via load->mutate->dump with indent=1, ensure_ascii=False
(verified to reproduce the original files exactly).
"""
import json, os

BASE = "/Users/dev_env/Documents/projects/indian_apps/dailyX/daily_krishna_stories"

def _dash(t):
    # corpus uses spaced em dashes; the source above used ASCII " - " separators
    return t.replace(" - ", " \u2014 ")

NEW_STORIES = {}

NEW_STORIES["DKS_0175"] = '''Muchukunda, a king of the Ikshvaku line - one of the oldest royal families in the world - woke slowly, the way a man surfaces from a sleep that has lasted for ages. The cave smelled of smoke and ash, and near its mouth lay a heap of ashes where something, or someone, had been burned away. He had slept through the turning of the world, but he understood what he saw well enough: the one who had pursued Krishna into this mountain was gone now, consumed, as it seemed, by his own wickedness.

What stood before him was a young man such as he had never seen: dark as a laden rain cloud, dressed in yellow silk, four-armed, glowing as though light came from within him, a garland of forest flowers looped across his chest, and a smile of pure affection on his face. Muchukunda pressed his palms together. The long watch he had kept for the gods against the asuras - the demons who were heaven's old enemies - had worn his senses thin, but he could still ask the question that mattered. "Are you the fire that burns within all things?" he said. "I think you must be the best of the three great gods who rule the worlds. I cannot look at you steadily - your splendor is more than my eyes can bear."

The young man spoke, and his voice was easy, as if he were telling an old story. Through many births, he said, he had measured the dust of the earth and known the deeds of all three times - what is, what was, and what has not yet come. But let the king hear about today. For the relief of a world grown heavy with evil kings, Kalanemi had been slain, and Kamsa, and Pralamba, and the others who hated the good. "And for your sake," Krishna said, "I came into this cave. Ask me for a boon, best of kings - whatever you desire, I will give it."

A gift, offered freely. Muchukunda had once conquered the four directions and sat on a golden throne while lesser kings bowed before him. He had been young and drunk on kingship, and the years of that drunkenness had passed like a bad dream. He had seen what it all came to: the body a king is praised for is only a jar of clay, and in the end it is called worms and ashes and dust. "When a man is ready to leave the turning world," he said, "it is then that he meets the good. I count it your grace, Lord, that the kingdom fell away from me of its own accord, for I desire no boon but the service of your feet - the one gift even the poorest may ask. Blessings bind. They are woven of desire and fear and the dull pride of having, and they keep a man tethered to what fades. Give me none of them. Only take me as your refuge."

Krishna heard him out, and when he answered there was something like pleasure in his voice. "That you were not tempted by the boons I offered," he said, "know it to be your true wakefulness. Men who are not devoted may discipline their breath and their minds for years and still not reach me. Wander the earth as you please - only keep your mind resting in me. You lived by the warrior's law and slew creatures in the chase; that debt is settled. In your next birth, king, you will be born a brahmana - of the class of priests and teachers - a friend to all beings, and you will come to me alone."

Muchukunda had asked for nothing, and so he had received everything there was to receive. He rose from the stone floor of the cave and went out into a world that looked new to him - a wanderer now, with nothing to carry but the one thing he had chosen. Behind him the ashes in the cave settled into stillness, and the long sleep of the king of the Ikshvakus was over at last.'''

NEW_STORIES["DKS_0176"] = '''Jarasandha, the king of Magadha, had marched on Mathura before, and every time the brothers who held the city had turned him back. He could not forgive it. Krishna and Balarama had slain the tyrant Kamsa and ended the reign that had kept Mathura in fear, and Jarasandha had sworn that the city would not stay theirs. Now he came once more, with an army so vast that it covered the plain like a rising flood. There would be no more turning back, he told his generals. This time the brothers would learn what it cost to defy him.

And this time the two brothers did not wait to meet him. Krishna had already set the city's wealth moving - the herds and the treasure, carried away with the men he had chosen for the task. Then, with the enemy's vanguard in sight, he and Balarama abandoned whatever remained and ran. The two of them, who had faced every host the Magadha king could bring and never given ground, fled on foot as though terror had finally caught them. They did not look back. They did not slow down. They ran as men run when everything is lost.

The king of Magadha laughed out loud when he saw it. This was the pair who had broken his armies season after season; now they were running like startled deer, and their flight told him the long quarrel was ending at last. Jarasandha gave chase, and his soldiers chased with him, sure that nothing could save the brothers now. Krishna and Balarama ran until their breath burned and their legs would carry them no farther, and when they reached the great mountain that stood alone above the plain - Mount Pravarshana - they climbed, exhausted, and hid among its rocks and trees.

Jarasandha's men ringed the hill. They searched the slopes for footprints, for any trace of the two who had vanished into the scrub, and they found nothing at all. The king of Magadha did what besiegers do when the quarry will not come out: he set the mountain on fire. Flames raced up the grass and the dry brush, and the smoke rose in thick columns until the whole flank of Pravarshana burned like a torch. Let them burn with it, Jarasandha thought, and he turned his army toward home, certain that he had seen the last of them.

But on the burning slope, Krishna and Balarama were not waiting for the fire to reach them. They sprang from the blazing hillside and leapt eleven yojanas - an old measure of distance, and a leap so far that no eye could follow where they came down - landing beyond the ring of Jarasandha's soldiers, unseen, in the quiet darkness at the mountain's foot. While the smoke still climbed behind them, they made their way across the country and back to Dwaraka, their city by the sea, where their people had made their home behind walls of water that guarded them better than any wall of stone.

Back in Magadha, Jarasandha told the story of how he had smoked the brothers out of Pravarshana and left them ashes, and he believed every word of it. What he did not know - could not know - was that the whole pursuit had been shaped from the beginning: the flight that looked like fear, the hill that looked like a trap, the fire that looked like an ending. Krishna and Balarama had chosen to be thought dead, because a king who believes his enemy is gone will stop looking. And so the brothers walked the streets of Dwaraka, unharmed and unlooked for, while the king of Magadha celebrated a victory that had never happened.'''

NEW_STORIES["DKS_0177"] = '''One morning in the hall where Krishna held his court at Dwaraka, when the brahmanas - the priests and learned men of the city - sat at ease and the business of the day had quieted, a stranger was brought in. He was not a merchant, not a soldier, not a king's man; dust lay on his clothes from a long road and hard travel. The guards let him pass because he asked, with a stranger's urgency, to see Krishna. He crossed the hall, bowed low before him, and pressed his palms together.

He had come, he said, from the kings of the earth. When Jarasandha of Magadha had set out to conquer the world, he had demanded that every king bow to him. Those who submitted kept their thrones; those who refused were taken by force and shut away in his fortress at Girivraja, in the heart of Magadha. Twenty thousand kings, the man said, lay imprisoned there - kings who had once commanded armies of their own and now sat in darkness, waiting for something that no army could bring them.

Then he delivered their words, and the hall grew still. "This world," the captive kings said, "is a place where the strong cut short the hopes of the weak whenever it pleases them. We have learned it at last. The happiness of a king is only a dream that depends on others; we carried its burden in bodies that knew fear from dawn to dawn. Now, Lord, we have given all of that up. We take refuge in you from the terror of this world. Your feet remove the sorrow of those who bow down - free us from the bond of Magadha. Jarasandha holds us with the strength of ten thousand elephants and keeps us shut in his house like a lion penning sheep."

And they reminded Krishna who Jarasandha was. Eighteen times, they said, this king had been broken by Krishna in battle, with his discus raised, and still he swelled with pride; still he oppressed the people who looked to Krishna for protection. "You have come down into this world for the sake of the good and the restraint of the wicked," the kings said. "If a man may cross your command and nothing follows, then we do not know what this world is. Ordain an end to it, unconquered one."

The messenger fell silent. Twenty thousand kings had sent their plea in the mouth of one unknown man, and the plea lay now at Krishna's feet. The brahmanas looked at one another; the courtiers looked at the floor; no one spoke. The whole hall waited for Krishna to answer, and in that stillness twenty thousand prisoners hung on a single word.'''

NEW_STORIES["DKS_0178"] = '''Uddhava was the man Krishna trusted most - a friend who could speak plainly, and he did so now in the quiet of Dwaraka. The Rajasuya, he began, was no common rite. It was the sacrifice by which a king had himself acknowledged as emperor of the world, and the scriptures were clear about who might offer it: only a king who had conquered the circle of the directions, who had brought every quarter of the earth to bow before him. One quarter had never bowed. Magadha stood across the path of every conqueror, and at the heart of Magadha stood Jarasandha, holding twenty thousand kings in his prison at Girivraja and calling himself lord of all the earth.

For Krishna, Uddhava said, this was one deed that served two ends. Bring Jarasandha down, and the directions would lie open for the sacrifice; bring him down, and the captive kings would go free. There was no need to choose between the rite and the rescue - they were the same road, and it led to the same gate.

But how? Jarasandha was no ordinary enemy, and Uddhava did not pretend otherwise. His strength, he reminded Krishna, was the strength of ten thousand elephants. Send against him a hundred akshauhinis - the full war-host of a king, chariots and elephants and foot-soldiers together - and he would still not fall. Such a man cannot be overwhelmed; he can only be met. Only one man alive was his match, and that man was Bhima, the strongest of the five Pandava brothers, Krishna's cousins. In a duel of two chariots, on a field with no army to hide behind and no retreat to run to, Bhima could finish what no host on earth could finish. That was the only way: not war, but single combat, man against man, and the stronger man would walk away.

And here was the shape of it. Bhima would go to Girivraja dressed as a brahmana - a man of the priestly class - passing himself off as a mendicant come to beg alms of the great king. And the alms he would ask for was a duel; Jarasandha, who prided himself on his strength and had never in his life refused a challenge, would grant it. Let the two fight it out, chariot against chariot, with Krishna there to see it done.

Uddhava's voice carried no heat. He was not proposing a gamble; he was reading a map. The slaying of Jarasandha, he said, would serve a great purpose - for the kings he held in prison, for the sacrifice that waited on a conquered world, for the peace of every kingdom between the seas. The women of those captive courts already sang of the day their enemy would fall and their husbands walk free; the gopis of Vrindavan sang of Krishna, and Sita the daughter of Janaka sang of him, and the sages who had made him their refuge. All the world that looked to him was waiting on this one deed. The man who could not be broken by armies would be broken by the one thing he had never learned to fear: an equal.

Krishna listened, and the plan settled into place like a stone dropping into still water. Bhima would go in a brahmana's dress; Arjuna, his brother, would go with Krishna to see it through; and the long quarrel with Magadha would end where Jarasandha had made his strength a prison - on a field of single combat, with no one left to save him but himself.'''

NEW_STORIES["DKS_0179"] = '''The morning Krishna left Dwaraka, the conches sounded before the sun cleared the sea. They began at the palace and were answered from the gates, and by the time the first light touched the city's white towers, every street knew that its lord was going out on a journey - and that no one remembered a departure like it.

He had spoken of it the evening before, quietly, the way he did everything that mattered. Yudhishthira, the eldest of the five Pandava brothers and Krishna's cousin, was preparing the Rajasuya, the great imperial sacrifice, and had sent for Krishna to come to Indraprastha. There was more in the invitation than ceremony. The sacrifice asked that every king of the land acknowledge Yudhishthira's eminence, and one king, Jarasandha of Magadha, would never bow to any man's glory. He stood between them and the sacrifice; but that was for later. First came the road.

Krishna entrusted Dwaraka to his elder brother Balarama, who would guard the city and its people while he was gone. Then he mounted his chariot - the one that bore the banner of Garuda, the great eagle of the gods - and gave the word.

What followed was less a departure than the city turning itself inside out. The army came first - chariots by the hundred, horsemen, elephants in their ornaments, foot soldiers in ordered ranks, so many that the plain beyond the gates could not hold them. The music began: drums of every kind - the mridanga and the bheri and the deep-voiced anaka - with conches and the curved gomukha horns joining in, until the sound rolled back off the walls and out over the sea. Banners climbed the morning air, and the sun caught on weapons, armor, and the crests of the allied kings who had chosen to ride with Krishna.

Behind the army came the inner procession. The women of the palace followed - Krishna's queens, with their children and attendants - borne on gilded palanquins with silk curtains drawn against the dust, and after them the long trains of oxen, camels, mules, and she-elephants carrying the household's goods. The whole mass of it shone and moved and sounded like an ocean stirred by great fish, and at its head rode one chariot under the Garuda banner - and in that chariot sat Krishna himself, calm as the eye of the storm.

Halfway down the road, the sage Narada met them - the tireless traveler of the gods, welcome in every court. He bowed before Krishna and paid his homage, and Krishna returned the honor with words that pleased him. Then Narada rose through the sky, carrying the sight of Krishna in his heart, and the procession went on.

Krishna had also sent a royal messenger ahead, to the kings whose lands the road would cross - a courtesy, and a signal too, so that no ruler along the way would mistake an army for an invasion. The messenger carried his word from court to court, and the kings made ready to receive their guest.

The land rolled past them: Anarta, where Dwaraka stood, then the dry country of Sauvira, the wastes of Maru, and Vinashana, where an old river was said to vanish into the earth. They crossed the Drishadvati and then the Sarasvati, rivers of the older stories, and everywhere they passed, towns emptied into the streets to watch - the local kings riding out to greet Krishna and ride a stretch of the way beside him, children running alongside the elephants, women watching from the rooftops.

It took many days. But the road was the easy part; what waited at its end was not. Indraprastha lay ahead, and the Rajasuya, and the question of Jarasandha - and Krishna was going there with the whole weight of his city at his back, to settle all of it.'''

NEW_STORIES["DKS_0180"] = '''The city of Girivraja was still settling after the fall of its king when Krishna did something the court had not expected. Jarasandha was dead - Bhima, Krishna's cousin and the strongest of the five Pandava brothers, had slain him in single combat outside the city, after a duel long enough to shatter two great maces - and in the hush that followed, everyone waited to see what the victors would do with a conquered capital. Magadha had been the terror of kings for a generation: its armies had marched across the world and carried its enemies home in chains. Some braced for fire, or plunder, or a war carried into the houses of the defeated. What they got instead was a coronation.

Jarasandha's son was a young man named Sahadeva. He had not chosen his father's wars, had not dragged kings from their thrones, had not filled the dungeons beneath the city. Krishna called him forward before the assembled court and installed him as lord of the Magadhas - the house of Jarasandha set back on the seat its king had made terrible. The ministers and elders of Magadha, who had expected a reckoning, watched the crown come down on the head of the one man in the city whose hands were clean of all of it. A conquered capital does not often get its own line of kings back, and the court did not quite know what to make of the mercy.

But the crowning was only half of what Krishna had come to do. The other half lay underneath their feet.

For years Jarasandha had kept his prisoners in Girivraja - kings he had vanquished in battle and carried away from their own thrones, warrior-kings of many lands who had ruled their own courts and now sat in darkness. He had not held them for ransom. He had gathered them for one terrible purpose: he meant to offer them up, one great day, as a sacrifice to Rudra - Shiva, the great god - the kings of the world led up like animals to feed a god who had never asked for them.

Krishna went down to them himself, and the prison was opened. One by one the captive kings came out into a light they had not seen in years - blinking, leaning on one another, slow to trust that the doors were truly open and that no guard would drag them back. Some wept. Some knelt. When the last of them stood in the daylight, Jarasandha's whole design lay undone: the kings of a hundred lands walking free out of the city that had swallowed them, no condition asked, no oath extracted, no price set on their freedom.

Girivraja that day saw both halves of a victory arranged side by side: a new king crowned in the hall above, and in the courtyard below, the old king's prisoners taking their first free steps. The kingdom of Magadha did not fall - it was handed back to its own people, with a son of their own line on the throne. It was the cruelty of the old reign that ended, not the kingdom itself.

And with the kings freed, the last obstacle on the road to the Rajasuya - the great imperial sacrifice - was gone. The captives who had been meant to die for a sacrifice would instead return to their own kingdoms, and when they reached their courts they carried a story with them: that the man who had conquered their lands had been answered at last, and that the man who had freed them had asked nothing for it but their freedom - and that on the day Magadha lost its terrible king, it found a gentler one.'''

# apply em-dash normalization now that the dict is fully populated
NEW_STORIES = {k: _dash(v) for k, v in NEW_STORIES.items()}

# Reflection override for DKS_0176 only (house guide §18: no sermon-adjacent "lesson").
NEW_REFLECTIONS = {
    "DKS_0176": _dash("Jarasandha's laughter is the hinge of the episode: he believes he has won because he saw the brothers run, and Krishna lets him keep the belief. The whole escape turns on an enemy defeating himself - the fire, the ashes, the triumphant return home all belong to a story that was never true, while the brothers slip, unseen, toward a city the sea will guard better than any army."),
}

LEVELS = {
    "DKS_0175": "minor",
    "DKS_0176": "major",
    "DKS_0177": "minor",
    "DKS_0178": "minor",
    "DKS_0179": "minor",
    "DKS_0180": "minor",
}

def main():
    os.makedirs(os.path.join(BASE, "data/mining/style_report"), exist_ok=True)
    report_lines = []
    for sid in ["DKS_0175", "DKS_0176", "DKS_0177", "DKS_0178", "DKS_0179", "DKS_0180"]:
        path = os.path.join(BASE, "data/stories", sid + ".json")
        raw = open(path, "rb").read()
        data = json.loads(raw)
        before = data["story"]
        before_wc = len(before.split())
        after_wc = len(NEW_STORIES[sid].split())
        assert 450 <= after_wc <= 700, f"{sid}: after_wc={after_wc} out of 450-700"

        # snapshot every field that must NOT change
        snapshot = {k: v for k, v in data.items() if k not in ("story", "reflection")}
        snapshot["generation_metadata"] = {
            k: v for k, v in data["generation_metadata"].items() if k != "style_normalization"
        }

        data["story"] = NEW_STORIES[sid]
        if sid in NEW_REFLECTIONS:
            data["reflection"] = NEW_REFLECTIONS[sid]
        data["generation_metadata"]["style_normalization"] = {
            "pass": "v1",
            "model": "deepseek-v4-flash",
            "changed": LEVELS[sid],
        }
        out = json.dumps(data, indent=1, ensure_ascii=False).encode()
        open(path, "wb").write(out)

        # verify: reloaded file differs from original only in the allowed fields
        reloaded = json.loads(open(path, "rb").read())
        snap2 = {k: v for k, v in reloaded.items() if k not in ("story", "reflection")}
        snap2["generation_metadata"] = {
            k: v for k, v in reloaded["generation_metadata"].items() if k != "style_normalization"
        }
        assert snap2 == snapshot, f"{sid}: untouched fields changed!"
        assert reloaded["generation_metadata"]["style_normalization"] == {
            "pass": "v1", "model": "deepseek-v4-flash", "changed": LEVELS[sid]
        }, sid
        assert reloaded["story"] == NEW_STORIES[sid], sid
        if sid in NEW_REFLECTIONS:
            assert reloaded["reflection"] == NEW_REFLECTIONS[sid], sid
        print(f"{sid}: before={before_wc} after={after_wc} changed={LEVELS[sid]} verified")
    print("ALL OK")

if __name__ == "__main__":
    main()
