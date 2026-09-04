#!/usr/bin/env python3
"""n088 style normalization apply — DKS_0523..0528"""
import json, sys, copy

FILES = {
    "DKS_0523": "data/pilot_stories/DKS_0523.json",
    "DKS_0524": "data/stories/DKS_0524.json",
    "DKS_0525": "data/stories/DKS_0525.json",
    "DKS_0526": "data/stories/DKS_0526.json",
    "DKS_0527": "data/stories/DKS_0527.json",
    "DKS_0528": "data/stories/DKS_0528.json",
}

NEW_STORY = {}
NEW_REFLECTION = {}
CHANGED = {}

# ----------------------------------------------------------------------------
NEW_STORY["DKS_0523"] = """Krishna's people, the Yadavas, were one great family with many branches — Vrishnis, Andhakas, Bhojas, Satvatas — the strongest warrior clan of their age. A brahmin's curse lay on that house: the day would come, it was said, when the proud clan would turn on one another and be destroyed. Krishna had known of it for years and had accepted it. When the hour came at last, he did not stand in its way.

Evening was coming down over the shore at Prabhasa, where the Yadavas had gathered to drink, and the sea lay calm beyond them.

They drank the strong sweet wine called maireya until their minds were overthrown, and as they drank, anger kindled between men who had grown up together. Pradyumna turned on Samba, Akrura on Bhoja, Aniruddha on Satyaki; the two Gadas met, and Sumitra and Suratha, and Subhadra and Sangramajit; and after them came the rest — Nishatha, Ulmuka, Sahasrajit, Satajit, Bhanu. The branches of the family, forgetting that they were one, fought one another. Banners fell; chariots and elephants crashed into one another; fathers fought sons and sons fought fathers, brothers fought brothers, and sisters' sons and daughters' sons fell upon their uncles. Old friends who had once eaten from the same plate fought one another.

There was a strangeness over it all. These were men who had fought side by side for years, and each now saw an enemy in the other's face. Some of them, in their madness, even took Balarama for an enemy. The wine was only part of it; something older and heavier was at work, a veil drawn over their minds. And Krishna watched it without moving to stop it.

In the midst of the assembly, the drunken Satyaki laughed at Kritavarma and taunted him: what kind of warrior, he shouted, would strike down men lost in sleep — men already as good as dead? Then he rushed at Kritavarma and cut him down with a sword in the very sight of Krishna.

The quarrel spread through the whole clan. When their arrows were spent and their bows broke in their hands, they did not stop. Along the shore grew the tall reeds called eraka — green things that no one had ever looked at twice. The warriors snatched them up, and in their fists the reeds turned to bars of iron, hard as thunderbolts, and they struck one another down. Son killed father, and father killed son. Uddhava, who lived to tell of it, said afterward that as the sun went down there had been among them a crushing of one another, like a field of reeds trampled flat.

Balarama, Krishna's elder brother, took no part in any of it. He walked down to the ocean's edge, seated himself in the stillness of deep meditation, and there, quietly, he let his body go.

When the noise died away, in a short time there was almost no one left of the Yadava race — only Krishna and his charioteer, Daruka. The curse had run its course, and the sea kept its own counsel."""

NEW_STORY["DKS_0524"] = """One day three wandering sages — Vishvamitra, Kanwa, and Narada — came to Dwaraka, the sea-city where Krishna's family, the Yadavas, ruled, and sat down to rest at the city's edge. A band of young Vrishni heroes, Samva among them, decided to play a trick on them — the kind of trick played by men who have never once been crossed in their lives. The old accounts say the heroes were not entirely to blame: the gods had already laid a blindness on them, and the arrogance behind their joke was itself part of the doom that was coming for the whole clan.

Samva, the son of Krishna and strong as his father, was dressed in women's clothes and led before the sages. \"This is the wife of Vabhru of great strength,\" the young men said, keeping their faces straight. \"She wishes for a son. Tell us, O sages, what she will bring forth.\"

The sages were not deceived. Their eyes reddened with anger as they looked at the grinning young men, and their answer was something far heavier than a riddle. \"This is Samva, of the house of Vasudeva,\" they said. \"He will bring forth a fierce iron bolt, and through that bolt the Vrishnis and the Andhakas will be destroyed. As for you — cruel and foolish, swollen with pride — you will use it to wipe out your own race. Only Balarama and Krishna will escape it. Balarama, the hero who carries the plough, will lay down his body and enter the ocean, and a hunter named Jara will one day pierce Krishna as he lies on the ground.\"

Without another word, the three sages rose and went to see Krishna.

Krishna heard them out. He called the Vrishnis together and told them exactly what the sages had said. He did not rage; he did not deny it; he did not order the curse undone. \"That which is destined will surely happen,\" he said, and he went into his house. He would not bend the world to spare himself.

The next morning Samva brought the iron bolt into the world — a thing of iron born of a man, fierce as a messenger of death. Everyone who saw it understood what it meant: through this bolt the Vrishni and Andhaka races would one day be burned to ashes. The report was carried to the king, old Ugrasena, and he was stricken with grief. He ordered the bolt ground into the finest powder, and men were sent to scatter the powder on the sea. Let the sea keep it, the city told itself. Let it be forgotten.

Then commands went out in the name of King Ugrasena, of Krishna, of Balarama, and of the high-souled Vabhru. Throughout the city it was proclaimed that from that day no one among the Vrishnis or the Andhakas might make wine or any strong drink, and that whoever brewed it in secret would be put to death on a stake, he and all his family. Out of fear of the king — and because the word came from Balarama, whose word no one questioned — the people obeyed, and Dwaraka went dry overnight.

So the iron bolt lay in the sea, and the wine was forbidden, and for a little while it looked as though a house could sweep out a curse with the dust of its own floor. But the powder had not been recalled, only hidden, and words spoken by sages do not dissolve in salt water. Everyone in Dwaraka sensed it, even as they nodded at the king's decree and emptied their jars onto the ground. The sea kept its secret. The curse kept its own time."""

NEW_STORY["DKS_0525"] = """Krishna's people, the Yadavas, were gone. At Prabhasa, on a seashore under a curse spoken long before, they had drunk wine until they fell on one another, and in a short time almost none of them were left. Now the few survivors searched for Balarama, Krishna's elder brother, who had walked away from the slaughter without a word. Krishna left the ruin with his charioteer Daruka and with Vabhru, one of the last heroes of the clan, and followed the trail of the man who had walked away from everything.

They found him at last in a solitary spot, sitting with his back against a tree, thoughtful, his great arms folded, looking at nothing. The man who had levelled armies with his plough-arm sat as still as the tree, as though the strength had gone out of him with his clan.

Krishna stood before his brother, and there was no collapse in his voice, only care. \"Daruka,\" he said, \"go to the Kurus, to Hastinapura, and carry this news to Arjuna, whom his friends call Partha. Tell him how the Yadavas destroyed one another under a brahmin's curse, and ask him to come here quickly.\"

Daruka, nearly out of his senses with grief, climbed onto his chariot and drove toward Hastinapura without looking back, carrying the worst news a messenger had ever carried. The road was long, and the news would not keep.

Krishna turned to Vabhru. \"Go quickly,\" he said, \"and guard the women. Let no robbers harm them, tempted by the wealth that travels with them.\" Vabhru — still dazed with wine, and sick at heart over his slaughtered kinsmen — touched Krishna's hand and set out. He had gone only a little way when the iron bolt found him at last. That bolt, which Samva had brought forth and which the king had ground to powder and scattered on the sea, had kept its shape somewhere in the world, waiting for a hunter's hand; now it sprang from the mallet in a hunter's grip and struck down the solitary survivor, who had been named in the same curse.

Krishna watched it happen and did not move. He had always known the bolt would not stay buried. He turned to Balarama. \"Wait for me here,\" he said, \"while I place the women under the care of their kinsmen.\"

He entered the city of Dwaraka and went to his father, old Vasudeva. \"Guard the women of our house,\" he said, \"until Arjuna comes. Balarama is waiting for me at the edge of the forest, and I will join him there today. I have watched our people destroy one another, as once I watched the great warriors of the Kuru line destroy one another in war, and I cannot bear to look on this city without the Yadavas in it. I am going into the woods, to live a life of stillness and prayer with Balarama.\" He touched his father's feet with his head and left his presence quickly.

Behind him the wailing began — the women of the house and the children crying out together, a sound like the city tearing in two. Krishna stopped, turned back, and stood before them. \"Arjuna will come,\" he said. \"That foremost of men will lift this grief from you.\"

Then he walked out of Dwaraka toward the forest where his brother waited, and the city was left holding its breath, watching the yellow cloth of his robe grow small against the trees. No one at the gate moved until the cloth had vanished into the green, and then the wailing began again, softer this time, as if the city no longer had the heart for it."""

NEW_STORY["DKS_0526"] = """Arjuna came back to Hastinapura as a different man. His face was withered with grief, his heart hollowed out, and he wiped his eyes with his hand as he stood before his elder brother, King Yudhishthira. He had gone to Dwaraka to bring the Yadava women home, and he had come back with the news that the world had changed while he was away.

He had loved Krishna as only a man who has been saved a hundred times can love his saviour. Standing there with his voice breaking, he remembered the friendship, the affection, the easy intimacy of the years when Krishna had been his charioteer, his brother-in-law, his laughter. At Draupadi's svayamvara — the gathering where a princess chooses her husband — when the kings had burned with envy, and at the burning of the Khandava forest, when he had fought the gods themselves, Krishna had been beside him. He remembered the sage Durvasa, whose terrible hunger had once threatened to burn the whole house of the Pandavas down, and how Krishna had come to them in the forest and turned the danger aside. He remembered the Gandiva, the great bow that had fallen to him, and every campaign it had won at Krishna's side. And he remembered Krishna's voice calling across the chariot — \"O Partha, O Arjuna, my friend, son of Kuru's race\" — the teasing, laughing voice that had made even the worst days bearable. The memories came like a flood he could not hold back.

Then he told the king what had happened in the city of their friends. The Yadavas, he said, had been deluded by the curse of the brahmins. They had drunk the madira wine — varuni, the old tales also call it — until their minds were churned and they were beside themselves. And in that madness the heroes of the Yadava race had slain one another, brother against brother, until the seashore of Prabhasa ran with their blood. Of the whole race, only four or five were left.

And Krishna, the one who had carried the burden of the earth, had departed it. The sages say he had taken up that body the way an actor takes up a costume, and when the burden of the earth was lightened, he cast it off the way an actor casts off a role. He left the world the same way he had entered it: at his own hour, on his own terms.

At that very moment the Kali age began — the age of quarrel, which the old books say is the root of every evil for those who are not awake to it. It set its foot upon the earth in the instant Krishna abandoned it. It was as if the world had been held upright by his presence, and the moment he withdrew, the darkness that had been waiting all along came in through the door.

Kunti heard it too. The mother of the Pandavas, who had seen her own children through war and exile and loss beyond counting, heard of the destruction of the Yadavas and of Krishna's going, and she took the measure of it in silence.

In the court of Hastinapura no one knew what to say. The sun rose over the city the next morning exactly as it had always risen, and the walls stood, and the river ran. The cowherds on the far bank drove their cattle down to the water as always, and children shouted in the lanes. Grief, it turned out, could walk beside an ordinary day. Only the wise could feel it: something that had been there since before anyone was born had gone out of the world, and the age itself had changed while everyone slept."""

NEW_STORY["DKS_0527"] = """When Vidura put his question — Vidura, the wise minister of the Kuru court, who had come down to the Yamuna to hear the story of Krishna from the man who had known him best — the silence that answered it lasted a long moment. Uddhava, who had served Krishna since he was five years old and had grown old in that service, seemed for a while to have forgotten that anyone was waiting. He sat on the bank of the river with his eyes closed, lost in the sweetness of remembering Krishna's feet, his limbs trembling with love, tears slipping from beneath his lids. Then, slowly, he wiped his eyes, and when he looked up he was smiling.

\"The sun has set,\" he said. \"Krishna has set. What good news can I bring to houses stripped of their fortune? Wretched is this world, and more wretched still the Yadavas — who lived with him, ate with him, fought beside him, and never knew him.\"

This was the grief that had been gathering in Uddhava since the news of Prabhasa reached him. The Yadavas had been no ordinary clan. They were subtle men, masters at reading a glance, mature in counsel, devoted to Krishna alone. And yet his own magic had touched them; the very power by which he had walked among mortals had closed their eyes. They had lived inside the miracle and never once recognised it.

Now that the miracle was over, memory came back to Uddhava in fragments he could not stop. He remembered the Rajasuya of King Yudhishthira — the great sacrifice at which the Pandava king had been crowned — when the three worlds had looked upon Krishna and found their eyes blessed by the sight. He remembered the love that spilled from Krishna's laughing glance during the rasa, the night-dance with the cowherd women of Vrindavan, the look that had given worth to everyone it fell on. Who among the gods, he asked, could ever forget the dust of his lotus feet? At that same sacrifice, even Shishupala — who had hated Krishna all his life — had reached perfection, drawn by that hatred into a fixed gazing at his enemy. And in the great battles, the heroes of the earth had fallen looking upon the lotus of Krishna's face.

That was the strangest part of his sorrow. Enemies had won release by fixing their minds on Krishna, however unwillingly. The whole world had been given the sight of him. Only his own kinsmen — the ones who had been closest — had been struck blind.

He spoke too of how the deathless one had taken birth in Vasudeva's house and played at being a child, and of how Krishna, before setting out on some errand, had bowed at his parents' feet. The memory choked him. \"Who could ever forget the dust of his lotus feet?\" he said again. \"And we — we lived our whole lives beside him.\"

Vidura listened and asked nothing more. Uddhava, wiping his eyes once more, drew a breath and began to tell it — the long tale that Vidura would carry away with him, and that would be told again and again long after both of them were gone.

He stopped once, and said something strange: that the man seated before him on the riverbank was no ordinary minister, but a soul without equal, a master of the three worlds whose every wish had already been granted. Vidura did not answer. In the world after Krishna, Uddhava seemed to be saying, even the greatest souls went disguised, and only love could recognise them.

The river moved past them, unhurried — the same river that had flowed past the village of his boyhood, where he had grown up among the cowherds. Uddhava's voice steadied as he spoke, as if the telling itself were a kind of returning. The sun had set, but the remembering had begun."""

NEW_STORY["DKS_0528"] = """Arjuna, the great archer of the Pandavas and Krishna's dearest friend, found the bodies of Krishna and Balarama and performed the funeral rites for them, and for all the slain. The eight queens of Krishna, with Rukmini at their head, embraced the body of their lord and entered the funeral fire. Revati, holding Balarama's body in her arms, climbed the blazing pyre after him, and the fire was cool to her, glad in the touch of her lord. Ugrasena, the old king, and Vasudeva with Devaki and Rohini, gave themselves to the flames as well. When the last ceremony was done, Arjuna made all the people leave the city, took the young prince Vajra — Krishna's grandson — and led the thousands of Krishna's widowed wives out of Dwaraka, slowly, with tenderness and care, the whole city following behind him.

Behind them, as they went, the sea rose and swallowed Dwaraka whole. Only the dwelling of the clan's own deity stood above the water, and the ocean has never washed it away: Krishna's presence still abides there, and whoever visits that holy shrine, the old tales say, is freed of his sins. On the same day that he departed from the earth, the dark-bodied Kali age came down upon it. The Sudharman, the great hall of assembly, and the Parijata tree, which Krishna had brought down from heaven, went back where they had come from.

Arjuna halted the long column in the country of Panchanada, a rich and fertile spot, to rest. That halt was his undoing. The robbers of the neighbourhood saw the widowed women and the great wealth in the hands of a single man, and their desires caught fire. They gathered the villainous Abhiras, the rough herdsmen of the region, and roused them. \"Here is Arjuna,\" they said, \"immensely rich, guarded only by women whose husbands are slain, passing confidently among us. His pride is swollen from slaying Bhishma and Drona and Jayadratha and Karna in the great war. He does not know the strength of simple villagers. Up, up! Take your long thick staves!\"

They rushed upon the unprotected people with cudgels and clods of earth. Arjuna turned to meet them and called out in derision: \"Retire, wretches, ignorant of what is right, unless you are eager to die.\" They paid him no heed, and seized his treasure and his women.

Then Arjuna braced Gandiva, the great heavenly bow, irresistible in battle — and it would not tighten. The string stayed slack in his hands, and the incantations of the celestial weapons would not come back to him. He loosed his shafts anyway, and the arrows that had once overthrown kings merely scratched the skin of the herdsmen. The arrows Agni, the fire-god, had given him long ago at the burning of the Khandava forest — arrows that carried certain destruction — were themselves destroyed that day and turned against him. He tried to summon the strength of Krishna, the presence that had guided his arm through a hundred wars; it was gone, and his arrows flew wide or were brushed aside by peasants. When his quiver was empty he beat at the bandits with the horn of his bow, and they only laughed. And the robbers, before his eyes, carried off all the women of the Vrishni and Andhaka tribes and went their way.

Arjuna wept. \"Alas, alas, I am deserted by my lord!\" he cried, and in that same instant the bow, the heavenly weapons, his chariot and his horses perished entirely — like a gift given to one who cannot use it, gone to nothing. \"Resistless are the decrees of fate,\" he said, \"which have laid weakness upon me, robbed me of my illustrious friend, and given victory to the base. These arms are mine, and this fist is mine, and this is my place, and I am Arjuna — but without that righteous aid, all of it is nothing. The valour of Arjuna and the strength of my brother Bhima were his work. Without him I am overcome by peasants. It can be from no other cause.\"

He made his way to Mathura, and there he placed Vajra on the throne of the Yadava line. In a wood outside the city he found the great sage Vyasa, and saluted him, lying prostrate at his feet. Vyasa looked at him for a long time. \"How is it,\" he asked, \"that I see you thus shorn of your lustre?\"

The question hung in the air. It was the question Arjuna had been asking himself ever since the day Gandiva went slack in his hands: what is an archer, when the presence that strung his bow has left the world? The Kali age had begun, and the first thing it had taken was not a kingdom — it was the strength of the strongest man alive."""

# reflections — only 0524 quoted a phrase that no longer stands in the story
NEW_REFLECTION["DKS_0524"] = "The joke is the hinge of the whole calamity: a prank among heroes who believed nothing could touch them gives the curse its instrument, and no power in the city can recall it afterwards. Krishna's quiet refusal to change what is coming is not indifference but acceptance — he lets destiny take its course rather than bend the world to spare himself."

CHANGED["DKS_0523"] = "major"
CHANGED["DKS_0524"] = "major"
CHANGED["DKS_0525"] = "major"
CHANGED["DKS_0526"] = "minor"
CHANGED["DKS_0527"] = "minor"
CHANGED["DKS_0528"] = "major"

def wc(s):
    return len(s.split())

def main():
    for sid in ["DKS_0523", "DKS_0524", "DKS_0525", "DKS_0526", "DKS_0527", "DKS_0528"]:
        path = FILES[sid]
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        before = wc(data["story"])
        # untouched-field guard: snapshot everything except story/reflection/meta
        untouched = {k: v for k, v in data.items() if k != "story"}
        if sid in NEW_REFLECTION:
            untouched["reflection"] = data["reflection"]

        data["story"] = NEW_STORY[sid]
        if sid in NEW_REFLECTION:
            data["reflection"] = NEW_REFLECTION[sid]
        meta = data.setdefault("generation_metadata", {})
        meta["style_normalization"] = {"pass": "v1", "model": "deepseek-v4-flash", "changed": CHANGED[sid]}

        out = json.dumps(data, indent=2, ensure_ascii=False)
        with open(path, "w", encoding="utf-8") as f:
            f.write(out)
        after = wc(data["story"])
        print(f"{sid}: {before} -> {after} words, changed={CHANGED[sid]}")

if __name__ == "__main__":
    main()
