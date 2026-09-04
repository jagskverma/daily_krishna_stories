#!/usr/bin/env python3
"""Style-normalization pass v1 for group n064 (DKS_0379..DKS_0384)."""
import json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STORY_0379 = '''Krishna lay asleep in Dwaraka, his city by the sea, with Rukmini, his wife, resting beside him. Far away, in the Kamyaka forest where the five Pandava brothers lived in exile with their wife, Draupadi, a heart was failing. And at that very moment ten thousand ascetics were walking toward the brothers' hermitage.

At their head came the sage Durvasa — a guest any household dreaded, famous for a temper that blazed up like fire and curses that never missed. He had chosen his moment with care, making certain that the Pandavas were resting at their ease and that Draupadi had finished her meal before he set out with his followers. Yudhishthira, the eldest brother, went forward to greet him with palms joined, offered him the finest seat, and gave the whole company a respectful welcome. "Return quickly after your bath," he said, "and the meal will be waiting." Durvasa, never troubling himself to wonder how such a feast would be provided, went down to the stream with all ten thousand disciples to bathe.

But Draupadi knew what her husband had promised, and her heart sank. The vessel that fed the Pandavas was a gift of the sun: it stayed full until she had finished her meal, and empty afterward. She had eaten long ago. There was no food in it now, and no way to fill it — and a guest like Durvasa could not be turned away with apologies.

After much anxious thought she could see no way out. So she did what she had done in her darkest hour before: she prayed. Inwardly she called on Krishna — the son of Devaki, whose face was dark as the leaf of the blue lotus, whose eyes were red as the heart of a lily, who wore yellow robes and the bright Kaustubha gem at his breast. "You who saved me once from Dussasana, when the whole court sat silent," she said in her heart, "save me now from this."

The prayer was answered before it was finished. In Dwaraka, Krishna rose from Rukmini's bed — she slept on, unaware — and came to the forest. Draupadi bowed before him in joy and told him everything: the arrival of the sages, the empty vessel, her fear of Durvasa's wrath. And Krishna, who had crossed half the world at the thought of her trouble, said only: "I am very hungry. Give me something to eat, and then go about your work."

She stared at him. "The sun-given vessel stays full only until I have eaten from it," she said. "I ate long ago. There is nothing in it now."

"This is no time for jokes," said Krishna. "I am truly hungry. Bring me the vessel and show it to me."

She had it brought. He looked inside, and there, stuck to the rim, was a single grain of rice with a scrap of vegetable clinging to it. He took it and swallowed it. "Let Hari, the soul of the universe, be pleased," he said, "and let the god who receives the offerings at every sacrifice be satisfied with this."

Then he turned to Bhima, the strong second brother, who stood nearby. "Go quickly," he said, "and invite the sages to dinner."

Bhima hurried to the nearest stream — clear, cool water — where Durvasa and his ten thousand had plunged in and were rubbing themselves after their bath. And there they stopped, one after another, staring at one another: their stomachs were full to the throat, though they had eaten nothing. "We told the king to prepare our meal and came here for a bath," they said. "How can we eat now? The feast has been prepared for nothing."

Durvasa understood at last, and his face clouded. "By making the king prepare a feast we cannot touch," he said, "we have done Yudhishthira a great wrong."'''

REFL_0379 = '''The hinge of the story is timing: the prayer is answered before it is finished, Krishna leaving Rukmini's side the instant the thought forms in the forest. And the miracle is almost comically small — not a feast conjured from the sky, but one leftover grain swallowed at the rim of an empty pot. His protection here is not spectacle; it is presence, arriving exactly when there was no other help.'''

STORY_0380 = '''Ten thousand guests, and nothing to set before them.

In the years when the five Pandava brothers lived in exile in the Kamyaka forest with their wife, Draupadi, the sage Durvasa arrived at their hermitage one day — and behind him came ten thousand disciples. He had not been expected, and there was no time to prepare. Ten thousand guests is a number that empties a granary and breaks a cook's heart.

Yudhishthira, the eldest brother — a king without a kingdom — went forward to receive him. He joined his palms, offered the sage an excellent seat, and spoke with perfect courtesy. Bathe in the river, he said, and return quickly; the food will be ready. It was a gracious invitation, and a desperate one. There was no food to be had, and to send such a guest away unfed was unthinkable.

Durvasa — a guest whose anger no one wished to test — suspected nothing of how the king would feed him and his host of followers. He went down to the stream to bathe, and the ten thousand went with him. Draupadi had already finished the day's meal, and the cooking vessel stood nearly empty.

Draupadi turned the problem over and over and found no way to feed ten thousand men. At last she did the only thing left to her: she prayed. Inwardly she called on Krishna, their cousin and dearest friend, who lived far away in his city of Dwaraka. She remembered his face, dark as the leaf of the blue lotus; his eyes, red as the heart of a lily; his yellow robes and the bright Kaustubha gem at his breast. And she begged him to come to her help.

And Krishna came. He brought no carts of provisions and no army of cooks. He asked simply for whatever there was to eat, and Draupadi brought him the vessel. He looked inside, and there, sticking to the rim, was a single grain of rice and a scrap of vegetable. One grain — not even a mouthful. He took it and swallowed it. "May Hari be pleased," he said, "and may the god who shares the offerings at every sacrifice be filled."

That was all. A single grain, offered and accepted, and nothing more.

Down at the river, something strange happened. Durvasa and his ten thousand disciples had plunged into the water and were rubbing themselves after their bath, when one by one they stopped. Every one of them felt, suddenly and unmistakably, that his stomach was full — completely, comfortably full, as after a rich feast. There was nothing more to ask for and nothing more to want. A guest who is already full cannot in courtesy sit down to a meal, and a guest who wants nothing cannot ask for more. To return now and claim a feast they could not eat would be absurd — almost a small shame.

So the sage and his ten thousand disciples did not return to the hermitage at all. They took the road out of the forest, full and wondering, and not one of them could say how it had come about. Behind them, in the quiet hermitage, stood a pot that had held nothing but a single grain — and it had been enough.'''

STORY_0381 = '''The ten thousand disciples of the sage Durvasa went down to the stream to bathe, and when they came out of the water they were full — not of the feast they had been promised, but full in a way none of them could explain, their stomachs heavy to the throat. The sage looked at his followers, and his followers looked at one another. Durvasa understood first. A feast had been promised them and they could not touch it; what king would forgive such an insult to his hospitality? The wrath of Yudhishthira, they feared, would fall on them like fire. And so, without a word of farewell, the whole company slipped away from the Kamyaka forest as quietly as it had come, fleeing the anger they believed they had earned.

The Pandavas were left standing in the sudden quiet. A few hours earlier the forest had been loud with the arrival of ten thousand guests, and Yudhishthira had gone forward with joined palms to welcome them, promising a meal for every man. It was a promise no host should ever have made: the sun-given vessel from which the brothers ate each day was empty, for Draupadi had already taken her food, and not a grain remained for a feast.

Draupadi, alone with her worry, had done the only thing she could. She had called on Krishna — their cousin, far away in Dwaraka — and reminded him of the day in the Kuru court when Dussasana had dragged her by the hair and the whole hall had sat silent. "As you protected me then," she had prayed, "extricate me now from this difficulty." And Krishna had come. He had looked into the empty vessel and found what a desperate eye could not: a single grain of rice and a leaf of vegetable clinging to its rim. That grain he had eaten. And in that same hour the sages bathing in the stream felt their hunger die in their stomachs.

Now Krishna stood before the brothers, and they did not know how to thank him. He spoke first, and his words were simple. Knowing their danger from that wrathful sage, he said, he had been implored by Draupadi to come, and therefore he had come speedily. There was no need for fear now; Durvasa was gone. And then he gave them the deeper assurance, the one they would carry long after the forest grew quiet again: "Virtuous men never suffer."

It was a strange comfort to hold, because their lives had been full of suffering — the poisoned feast, the lost kingdom, the exile, their wife dragged before an assembly of enemies who had shamed her. Yet the words came from someone who had crossed the whole distance from Dwaraka in the time it takes to say a name, and standing in his presence the brothers found that they could believe them.

He asked only one thing of them: their permission to return home. The Pandavas gave it freely and watched him go.

When he had disappeared among the trees, the forest seemed to breathe again. The sages were gone, the feast that could not have been made had somehow been served, and the danger that had filled the afternoon had lifted like mist off the river. Yudhishthira looked at the empty vessel, at the stream where the ascetics had bathed, at the sky gone soft with evening — and understood, at last, that they had never been as alone as they had felt.'''

STORY_0382 = '''Krishna walked through the streets of Mathura and stopped at the house of Akrura — an elder of his own family, and one of the truest friends he had. With him came his brother Balarama and Uddhava, his trusted friend and adviser. Krishna had not sent for Akrura, nor summoned him to the palace; he came himself, on foot, to the door of a friend.

When Akrura saw them approaching, he went out to meet them and bowed low before Krishna and Balarama, and they received his reverence and returned it. With his own hands he washed their feet, held that water to his head as if it were the holiest thing he would ever touch, and then seated them and took their feet in his lap, rubbing them with the tenderness of a man who had waited a long time for this visit. "Blessed are our dwellings," he said, "that the teacher of the world has entered them."

"By good fortune," he said, "Kamsa is slain with all his followers, and this family is yours." Then his praise poured out like a river that had been dammed too long. These two, he said, were the foremost of persons, the cause and the substance of the world. Krishna creates, sustains and dissolves the universe with his own powers; whenever the ancient path of the Vedas is lost among men, he restores it for the good of all; and now he had come down into the house of Vasudeva, his father, to lighten the burden of the earth, spreading glory over his own family. Even the kings of the gods, he said, found Krishna's way hard to reach — and yet here he stood, inside the walls of a devotee's house. "What wise man," Akrura asked, "would seek refuge anywhere but in you — dear to your devotees, true in speech, a friend who remembers a kindness and grants every wish?" He spoke of the bonds that hold a man — son, wife, wealth, house, the body itself — and begged Krishna to cut them all.

Krishna heard him out, and then answered. Great souls like Akrura, he said, are the ones to be served, the most worthy of all. The holy places are not made of water, nor are the gods made of clay and stone. The true sacred presence lives in people — in a friend who wishes you well, in a heart that has bowed to the good. He might have said more, but he had come on other business, and now he spoke of it.

After their father Pandu died, Krishna told him, his five children had been left with their mother, deep in sorrow, and the blind king of Hastinapura dealt with his brother's sons out of a mean and troubled mind, guided by his wicked son Duryodhana. The boys had been brought to the capital after their father's death; they were there not by choice, and the king's house was not their home. "Go to Hastinapura," Krishna said, "and learn how the Pandavas fare — whether things go well with them or ill." Learn, and come back and tell me, was the meaning of it: not a war, not a proclamation, but a friend sent to look with his own eyes and report honestly.

Akrura bowed his head. He asked for no guard, no retinue, no letter of authority; a friend's eyes were the only credential he needed. He would go, and he would watch, and he would remember everything. Krishna, Balarama and Uddhava left him standing at his own door, and the house that had held the lord of the world felt, for a moment, like the center of the earth.'''

STORY_0383 = '''Hastinapura was full of eyes, and Kunti had learned to live under them. The palace of the Kurus was a place of whispers and rivalries, and in the years since her husband Pandu's death she had felt herself watched from every side — the widow of the dead king, the mother of five boys the court had never wanted. They were the sons of Pandu, and the kingdom their father had left was now held by his blind brother. Then word came that her brother Akrura had arrived from Mathura, and for the first time in many months, Kunti let herself hope.

Akrura did what courtesy required, and more. He greeted the elders of the house — Bahlika with his son, the sage Bharadvaja, Gautama, the old friends of the family — and then he settled in and watched. He stayed for months, asking little, seeing everything. He marked how the sons of Pandu shone: their brilliance, their strength, their courage, their humility, every good quality that had survived their father's death. And he marked, too, what the sons of Dhritarashtra had done to them — the poison mixed into their food, the cruelties that had no name in the law but were known to every whisper in the palace.

Then Kunti came to him, and she did not come composed. She was weeping. In the months of Akrura's stay she had kept her composure, as a queen of the Kurus must, but this was her brother, and with him the composure failed. Among her rivals, she told him, she was like a doe among wolves; every day she measured her children's danger by the faces that surrounded them. Then she asked the question that had pressed on her heart since the day she learned her brother was in the city. "Do they still remember us?" she said — her parents, her brothers, the home she had left behind in Mathura. "Do my father and brothers still think of me?" She did not ask for wealth or power or a return to favor; she asked only to be remembered, to know that the world she had left behind still held her name.

And then, as if the question had carried her to the edge of a deeper need, she turned from the messenger to the one he had come from. "The blessed Krishna, my brother's son," she said, "is the refuge, dear to his devotees. Krishna, Krishna," she cried, "great yogin, soul of the universe, protector of all beings! I see no refuge for us but your lotus feet." She spoke of him as her nephew, the boy of Mathura who was, she knew, more than any boy. "Salutation to Krishna, the pure one, the supreme self." If her parents had forgotten her, Krishna had not. If the wolves of Hastinapura closed in, the refuge was still there, as close as a name spoken through tears.

Akrura and Vidura stood with her, sharing her sorrow, taking it into themselves. Vidura — the wise uncle of the Kurus who had always loved the Pandavas — and Akrura, who had come straight from Krishna's side. Between the two of them they could give her what the palace never would: the assurance that she was not alone. She had spoken her grief aloud at last, and she had been heard; and being heard, the walls of the palace seemed to stand a little further off.

That night Kunti slept more peacefully than she had in months. Her words were on their way to Mathura, carried by a brother who had seen everything — toward a city where someone still remembered her name.'''

STORY_0384 = '''Before he left Hastinapura, Akrura asked to see the king. Krishna of Mathura had sent him to the city to learn how his cousins, the five Pandava brothers, were faring in the palace of their uncle, the blind king Dhritarashtra — and Akrura had learned it well: the poison, the cruelties, the slow grinding-down of five boys and their mother. Now, with that knowledge sitting in him like a stone, he went to the one man who could change it. Dhritarashtra sat on the throne his brother Pandu had left empty, and loved his own sons with a love that had gone crooked.

Akrura did not flatter him. He spoke as a friend of the house, plainly. "Rule the earth by righteousness," he said, "and win your subjects by good conduct. Act otherwise, and you will be blamed in every mouth and walk into darkness." Then he said the thing that kings rarely hear: no one dwells in this world forever with anyone. A being is born alone, and dies alone; no retinue follows a man out of the world, and the guards who surround a throne cannot surround a grave. The wealth a man gathers by wrong means is carried off by others of little wit; the man who nourishes his sons on unrighteousness, thinking himself clever, takes the guilt onto his own shoulders and is finally abandoned by those very sons. "Therefore this world, O king," Akrura said, "is a dream, a waking illusion, a fantasy of the mind. Do not anchor your soul to it."

Dhritarashtra heard him out. The truth of it was undeniable, and the old king admitted as much. "Even so, gentle one," he said, "your sweet words do not rest in my heart, because my heart is unsteady." He knew what was right; he loved his sons more than he could hold to what was right. His love for them sat on his mind like a weight, and the truth could not move it. And then he spoke the deeper helplessness, the one that makes counsel useless: "What man can undo the ordinance of the Lord?" The lord who, entering his own creation through his inscrutable power, sets in motion the wheel of the world — who could stand against that wheel, and who could call a man guilty for being crushed beneath it? He bowed to that power, unknowable in its play, and fell silent.

Akrura left the city as he had come, and the blind king remained on his throne, the truth ringing in his ears and no room for it in his heart. The counsel had been given; whether it would be kept was another matter, and Akrura knew better than to wait for the answer.

Back in Mathura, he went straight to Krishna and to Balarama, Krishna's elder brother, and told them everything — what he had seen of the Pandavas, what the sons of Dhritarashtra had done, and what the blind king had confessed when the truth was set before him. He told them how the king had heard every word of the counsel, and acknowledged the truth of every word, and how the acknowledgment had changed nothing in his heart. He reported it all without softening a word. Krishna listened. Balarama listened. The news did not surprise them, but it was news that had to be carried, and it had been carried by a friend's eyes and a friend's honesty.

The kingdom of the Kurus went on as it had. But from that day, nothing between Hastinapura and Mathura was quite what it had been. A message had passed between the two cities — not of war, not yet — and the road that carried it ran both ways.'''

FILES = {
    "DKS_0379": ("data/stories", STORY_0379, REFL_0379, "major"),
    "DKS_0380": ("data/pilot_stories", STORY_0380, None, "minor"),
    "DKS_0381": ("data/stories", STORY_0381, None, "major"),
    "DKS_0382": ("data/stories", STORY_0382, None, "minor"),
    "DKS_0383": ("data/stories", STORY_0383, None, "minor"),
    "DKS_0384": ("data/stories", STORY_0384, None, "minor"),
}

def wc(s):
    return len(s.split())

if __name__ == "__main__":
    for sid, (d, new_story, new_refl, changed) in FILES.items():
        path = os.path.join(BASE, d, sid + ".json")
        with open(path, encoding="utf-8") as f:
            j = json.load(f)
        before = wc(j["story"])
        j["story"] = new_story
        if new_refl is not None:
            j["reflection"] = new_refl
        meta = j.setdefault("generation_metadata", {})
        meta["style_normalization"] = {"pass": "v1", "model": "deepseek-v4-flash", "changed": changed}
        with open(path, "w", encoding="utf-8") as f:
            json.dump(j, f, indent=1, ensure_ascii=False)
            f.write("\n")
        after = wc(new_story)
        print(f"{sid}: {before} -> {after} words, changed={changed}")
