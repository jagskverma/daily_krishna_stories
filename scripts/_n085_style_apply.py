#!/usr/bin/env python3
"""Style normalization pass v1 for agent n085 (DKS_0505..DKS_0510).

Per docs/HOUSE_STYLE_GUIDE.md: rewrites ONLY the `story` field and adds
generation_metadata.style_normalization. All other fields byte-identical.
DKS_0507 lives in data/pilot_stories/ per data/mining/style_manifest.json.
"""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FILES = {
    "DKS_0505": "data/stories/DKS_0505.json",
    "DKS_0506": "data/stories/DKS_0506.json",
    "DKS_0507": "data/pilot_stories/DKS_0507.json",
    "DKS_0508": "data/stories/DKS_0508.json",
    "DKS_0509": "data/stories/DKS_0509.json",
    "DKS_0510": "data/stories/DKS_0510.json",
}

NEW_STORY = {}

NEW_STORY["DKS_0505"] = (
'"Listen," Krishna said, "and I will tell you what freedom looks like." Uddhava, '
"Krishna's close friend, had asked for teaching, and Krishna answered as he often did \u2014 with a story.\n\n"
"There was once a king named Yadu, of the line of Nahusha, who ruled a great kingdom and knew its "
"burdens: ministers who angled for favor, petitions without end, wars that had to be fought to keep "
"the peace. One day his party halted in a forest, and down the road came a wandering brahmin \u2014 an "
"avadhuta, a man who had put aside everything: home, family, ritual, even the marks of his order.\n\n"
"The king could not take his eyes off him. The man owned nothing and feared nothing. He moved without "
"hurry, laughed like a child, stood as still as a ghost \u2014 and yet there was a serenity in him that "
"Yadu had never seen at court. There every man wore his rank like armor; here was one who wore nothing "
"and needed no armor, and the difference struck the king like a blow.\n\n"
"The world around them was burning, and Yadu thought of it constantly: people consumed by the forest "
"fire of desire and greed, everyone running after what the next man had. His own ministers would have "
"cut each other's throats over a district; the neighboring kings measured friendship in brides and "
"borders; even the ascetics who came to the palace asked for something \u2014 a cow, a village, an "
"audience. This man asked for nothing and was afraid of no one, and he walked through the middle of "
"the burning world untouched.\n\n"
'Yadu dismounted and approached him. "Men spend their lives on dharma, wealth, pleasure, and the itch '
'of curiosity," he said, "and burn in that fire all the same. But you are capable, wise, skilled, '
"fortunate; your speech is like nectar; for those who ask, you are the very cause of joy. You act like "
'a child, a madman, a ghost \u2014 and yet you are a sage. How did you gain such wisdom?"\n\n'
'The brahmin smiled, the way a man smiles who has been taught by everything he ever met. "O king, I '
"have many gurus. Twenty-four of them. From each one I learn whatever I learn.\"\n\n"
"And he named them, one after another: earth, wind, sky, water, fire, the moon, the sun; the pigeon, "
"the python, the ocean; the moth, the bee, the elephant, the honey-gatherer; the deer, the fish, "
"Pingala, the osprey; the child, the maiden, the arrow-maker, the serpent, the spider, the cricket.\n\n"
"Yadu stared. Twenty-four teachers \u2014 and not one of them a scholar or a sage. Every child knew the "
"sun and the moon were holy, but a python? A fish? A maiden? And Pingala \u2014 the name sounded like a "
"woman's, and the king's curiosity sharpened at the thought that she too had taught this man "
"something. He had paid the finest brahmins in the land to instruct him and had mastered the texts and "
"the rituals; here was a penniless wanderer who had studied with rivers and birds.\n\n"
'"Then teach me," Yadu said.\n\n'
"The avadhuta looked at him for a long moment \u2014 at the king's ornaments, the armed guard, the fine "
"horse cropping the grass \u2014 and it seemed to Yadu that the man was not judging him but weighing "
"something far older: whether the question had come from the king's boredom or from his hunger. Then "
"he nodded, as if he had been waiting for it all along. And he began with the first of his teachers: "
"the earth itself."
)

NEW_STORY["DKS_0506"] = (
"A king named Yadu had halted his party on a forest road to question a wandering brahmin \u2014 an "
"avadhuta, a renunciate who owned nothing and feared nothing. Yadu had asked how such freedom was won, "
"and the brahmin answered that he kept twenty-four teachers: everything he had ever met. Now the "
"wanderer sat on the bare earth with the king before him, and began with the first of them.\n\n"
'"The earth taught me forbearance," the avadhuta said. "Every being walks upon her \u2014 beasts and '
"men, armies in their thousands, the hooves of cattle, the wheels of carts. She is trampled by all of "
"them, morning and evening, and she never once strays from her course. So the wise one, though the "
'world treads on him, does not leave his path."\n\n'
"Yadu thought of how often he had been wronged \u2014 by rivals, by fate, by his own temper \u2014 and "
"how often he had left the path in fury instead of staying on it. The first lesson had already found "
"its mark.\n\n"
'"The wind taught me detachment," the avadhuta said. "It moves everywhere \u2014 through palaces and '
"market streets, through the trees, into every corner of every house \u2014 and it clings to nothing it "
"touches. So the sage moves through the world, touching a thousand things and holding on to none.\"\n\n"
"The wind, the king realized, had taught this man what he had spent his life failing to learn: to be "
"in the middle of things and not be caught by them.\n\n"
'"The sky taught me to remain untouched. Clouds sail through it, rain falls from it, the smoke of a '
"thousand hearths rises into it, birds cross it \u2014 and none of them leaves a mark. So the wise one "
"lives among all the beings of the world \u2014 moving and still, hidden in each \u2014 and is touched by "
"none. The sky is everywhere, and nowhere is it held; and in the same way he sees the one self in all "
'things and knows himself in everything."\n\n'
'"The water taught me purity. It is clear by nature and sweet to the taste, and wherever it flows it '
"makes the place holy \u2014 a tirtha, where men come to bathe. So the sage, pure in himself, makes "
"everything around him sacred; people come to him as they come to a river, and the dirt they carry "
'falls from them in his presence."\n\n'
'"The fire taught me to take no stain. Whatever it is given \u2014 wood, refuse, offerings, filth \u2014 '
"it burns, and takes no stain from any of it. So the sage is not polluted by what he consumes. His "
'light is his own, and the world\'s dirt does not reach it."\n\n'
'"The moon taught me to wax and to wane. It swells to fullness and thins to a sliver, and both are its '
"own nature. So it is with the body: it rises and falls through birth, youth, age, and death, down to "
"the cremation ground \u2014 and all of these belong to the body, not to the self. The wise one watches "
"them as the moon watches its own phases, taking what time brings and letting it go when time takes "
'it."\n\n'
'"The sun taught me the one soul in many bodies. One sun rises on the palace and on the hut, on the '
"king and on the beggar, and gives light to them all alike. So the one self appears in every body; and "
"when a body ends, nothing of that light is lost. The wise one lives in that single sight, seeing "
'himself in every face."\n\n'
"The king sat silent. Seven lessons, and every one drawn from something that had never spoken a word "
"\u2014 each as clear as water. He had filled his court with the learned, and none of them had ever told "
"him anything so simply. The avadhuta paused, and when the king leaned forward, he went on \u2014 to the "
"eighth of his teachers, the pigeon, and to what love had cost it."
)

NEW_STORY["DKS_0507"] = (
"The avadhuta \u2014 a wandering brahmin, a renunciate who had left home and name behind \u2014 once "
"told King Yadu how he had come by his teachers. The eighth of them, he said, was a pigeon.\n\n"
"A pigeon built his nest in a forest tree and lived there with his mate. They shared one perch and "
"one nest; where one went, the other went too, and what one wanted, the other gave without being "
"asked. They were, in the way of birds, a single household, and the tree was their home. It was a "
"small life, and a complete one.\n\n"
"In time the hen laid eggs, and when the chicks hatched, the two birds loved them with a tenderness "
"that filled the nest with soft feathers and low, contented cooing. They fed them from first light "
"and kept them warm through the night; the nest was their whole world, and their world was warm. The "
"chicks grew, their feathers coming in soft as silk, their clumsy antics the parents' whole delight; "
"watching them, the two birds felt that no harm could ever reach this tree or this nest. Everything "
"they owned was in it: their young, their days, their reason for flying out and flying back.\n\n"
"One day the two flew out together to gather food. While they were gone, a hunter came through the "
"forest, saw the young birds alone in the nest, and spread his net over them.\n\n"
"The hen came home first. She saw her chicks struggling in the mesh, and love moved faster in her than "
"fear. She did not stop to think of herself, did not try to pull them free; she flew into the net and "
"settled down among her young, wanting only to be with them.\n\n"
"Then the pigeon came home and saw them all \u2014 his mate and his children caught in the hunter's "
'cords. "Alas," he cried, "what has my foolish heart brought down on us? My home is destroyed, my '
'wife and children are trapped \u2014 what use is my life now?" He could not bear to be the only one '
"left free, to sit in an empty nest while everyone he loved was taken. So he too flew into the net, "
"and the hunter, finding them all gathered there, carried them away.\n\n"
"The nest stood empty in the tree. Its soft lining stirred once in the wind, then was still.\n\n"
'"This is why the pigeon is numbered among my teachers," the avadhuta said. "Love without any distance '
"left that nest empty. A man who clings to home and family as that bird did \u2014 bound to them, never "
"at peace \u2014 comes in the end to ruin. Human birth is the one door that opens on freedom, and he "
'shut it on himself."'
)

NEW_STORY["DKS_0508"] = (
"King Yadu sat on the forest road before the wandering brahmin \u2014 the avadhuta, the renunciate who "
"owned nothing and feared nothing \u2014 and listened while the man spoke, one by one, of the teachers "
"he had met. The ninth and the tenth, he said, were a python and the ocean.\n\n"
'"The python taught me contentment," the avadhuta said. "He lies where he happens to be, and whatever '
"comes within reach \u2014 fine food or foul, much or little \u2014 he takes. If nothing comes, he lies "
"still for days on end, without effort, without complaint. He does not hunt, he does not plan, he "
"does not grieve the meal that passes him by; hunger comes and goes, and he is still the python "
"either way. He carries strength and vigor, yet he does not spend them on striving; what his hands "
"do, they do without desire, and it leaves no mark on him. So the sage accepts what chance brings "
'and does not run after more."\n\n'
"The king, whose days were a long argument with appetite \u2014 the next campaign, the next pleasure, "
"the next proof of his greatness \u2014 heard this and felt a strange lightness, as if a knot had "
"loosened inside him.\n\n"
'"The ocean taught me depth," the avadhuta said. "The rivers pour into it and it does not swell; they '
"may rage in flood or fail in drought, and it does not sink. It receives both without preference, "
"because its fullness is its own. Whatever pours in, whatever is withheld, the sea stays deep and " 
"still \u2014 too deep to be fathomed, too still to be stirred. So the sage stays the same whether the "
"world pours gifts on him or leaves him empty-handed: he is fixed on Narayana alone \u2014 on God \u2014 "
'and that fullness does not rise or fall with fortune."\n\n'
"Yadu looked at the wanderer \u2014 a man who owned nothing and had just described the ocean as if it "
"lived inside him \u2014 and slowly understood that the python's stillness and the ocean's depth were "
"one teaching: freedom does not come from having enough; it comes from needing nothing. The sage is "
"not the man who has everything; he is the man who is complete without anything, like the sea that no "
"river can fill and no drought can empty.\n\n"
"A wind moved through the forest, and the avadhuta sat in the middle of it, unmoved, like his "
"teachers. The king had come to the forest to escape his court for a day, and found he had wandered "
"into a school greater than any he had built. Seeing that the lesson had landed, the sage spoke again "
"\u2014 of the moth, and of the flame it cannot resist."
)

NEW_STORY["DKS_0509"] = (
"A lamp flame is a small thing, and yet the moth flies straight into it. It circles the light once, "
"twice, drawn by a brightness that promises nothing but itself, and in a moment it is gone \u2014 a "
"scorched thread of a body dropping onto the ledge below the flame. The light did not hunt it; the "
"moth did all the hunting itself. The flame burned on as if nothing had happened.\n\n"
"It was by a lamp in a wayside rest-house, at night, that the wandering teacher watched this happen, "
"and he counted the moth among his teachers. He was an avadhuta \u2014 a brahmin who had put aside "
"home, name, and belongings \u2014 and he walked the forest roads taking lessons from everything he "
"met. He had no guru but the world, and the world never ran out of lessons. Nothing was too small to "
"teach him, and nothing, he said, was too small to destroy a man.\n\n"
"The moth's lesson was desire. The flame asks nothing of the moth; it is the moth that gives "
"everything \u2014 and for what? A little brightness. So it is, he said, with a man who is not master "
"of his senses. Bewitched by a woman's beauty \u2014 the gold of her ornaments, the fine weave of her "
"clothes, the thousand small enchantments the world spins around itself \u2014 he follows the "
"brightness wherever it leads and falls into blinding darkness, exactly as the moth falls into the "
"flame. He had seen it happen: sensible men, undone by a face. It is not that beauty is false; it is "
"that desire cannot stop at looking. It must draw nearer, and then nearer, until the light that "
"seemed so lovely is the fire that burns it.\n\n"
"The bee taught him the other way. In the mornings he sat where the bees worked, among the wild "
"flowers at the road's edge, and watched them go about their business: nothing in haste, nothing in "
"excess, each blossom left able to bloom again. The bee visits many flowers and takes from each only "
"a little \u2014 a sip of nectar, a dusting of pollen \u2014 and carries nothing away to hoard. So the "
"wise man, said the avadhuta, gathers the essence of every teaching, great and small, from the "
"longest scripture to the humblest creature's way of living, the way the bee gathers from every "
"flower: he takes what is good from each and clings to none. He eats a little at a time, just enough "
"to keep the body alive; what is begged for the day is used that same day, and nothing is laid up for "
"the evening or the morning. The flower is not the enemy. The hoard is.\n\n"
"Two small creatures, two ways of being alive. One dies of wanting everything; the other lives by "
"taking a little and letting the rest go. The avadhuta said he had made himself the bee: he tasted the "
"world's sweetness without needing to own it, listened to great teachings and small ones without "
"becoming the servant of any, and slept each night with empty hands, having kept nothing for a day "
"that had not yet come. He was not cold, he said; he was only free of the need that makes men hold "
"on.\n\n"
"He used to say that the two insects together were one complete teaching. The moth shows what appetite "
"costs; the bee shows what appetite is for. Between the two, a man may choose how to want. It is a "
"quiet discipline \u2014 and a hard one. The flame is so bright, and the flowers are so many."
)

NEW_STORY["DKS_0510"] = (
"The elephant is the strongest thing in the forest. It can uproot a tree and scatter a hunting party "
"like dry leaves, and yet it is caught by something soft \u2014 a she-elephant. The hunters know this "
"well. They send the cow out as a decoy, and the great male, all his strength forgotten, follows her "
"step by step into the clearing where the rope and the stake wait. He is not conquered; he is led. "
"And he goes willingly.\n\n"
"The avadhuta, the wandering brahmin who took the world itself as his guru, watched this and learned "
"from it. If desire can bind an elephant, he said, what will it do to a man? The senses are not weak, "
"but they are hungry, and hunger does not bargain. Strength counts for nothing against desire: the "
"elephant could have broken every rope in the forest, and instead it stood quietly while the rope was "
"tied. So the wise keep away from what wakes desire \u2014 a renunciate, he said, should not touch a "
"woman, not even one made of wood \u2014 for the wise never go near what destroys a man. The only "
"safety from a snare is not to follow the decoy, however sweet she seems.\n\n"
"The honey-gatherer taught him about hoarding. A man climbs to the wild hive in the rocks, and the "
"bees swarm and sting him for every comb he takes; he comes down aching and half-blinded, carrying "
"the honey \u2014 and who eats it? Others. The sweetness is enjoyed by hands that never felt the "
"stings, while the gatherer keeps the scars. Still he climbs again the next season, because the honey "
"is sweet and the memory of pain is short. So it is with wealth hoarded in hardship, said the "
"avadhuta: a man gathers it in sleeplessness and worry, and in the end others enjoy what he spent his "
"life clutching. The sage does not pile up what was gathered in suffering.\n\n"
"The deer taught him about the ear. The deer is swift and watchful, and no hunter can run it down; "
"but it is caught by song. He had seen the hunters lure the deer with a flute, the animal stopping "
"mid-step, ears turned to the music, forgetting everything that had kept it safe. The ear, said the "
"avadhuta, is a door that cannot see. A wandering renunciate should not listen to the music and "
"dancing of the village, the songs that please the senses; the sweetest sound can be the snare.\n\n"
"The fish taught him about the tongue. The fish is caught by the mouth and hooked through the tongue, "
"and it is the taste of the bait that undoes it. Of all the senses, said the avadhuta, the tongue is "
"the hardest to master. A man may close his eyes and stop his ears, but the craving for taste follows "
"him everywhere, and it is the craving that pulls the hook. A man may refuse the cup and the plate, "
"he said, and still be undone by the memory of a taste.\n\n"
"So the avadhuta walked his road with his senses held in check, like a man fasting. The senses are "
"conquered quickly when they are not fed \u2014 the whole secret is to stop feeding them, he said. And "
"it must be all of them together: a man who has mastered one sense while another rules him is not yet "
"master of anything. When the village music drifted out to the road at dusk, he walked on past it; "
"when the markets offered their sweets, he did not turn. He had seen where each road ended \u2014 in "
"the rope, in the stings, in the bow, in the hook. The elephant was stronger than the rope that held "
"it, and it was led anyway."
)

CHANGED = {
    "DKS_0505": "minor",
    "DKS_0506": "major",
    "DKS_0507": "major",
    "DKS_0508": "minor",
    "DKS_0509": "minor",
    "DKS_0510": "minor",
}

def main():
    results = {}
    for sid, rel in FILES.items():
        path = os.path.join(BASE, rel)
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        assert "style_normalization" not in data["generation_metadata"], sid
        before = data["story"]
        n_before = len(before.split())
        data["story"] = NEW_STORY[sid]
        data["generation_metadata"]["style_normalization"] = {
            "pass": "v1",
            "model": "deepseek-v4-flash",
            "changed": CHANGED[sid],
        }
        n_after = len(data["story"].split())
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=1)
        results[sid] = (n_before, n_after)
        print(f"{sid}: {n_before} -> {n_after} words  changed={CHANGED[sid]}")
    return results

if __name__ == "__main__":
    main()
