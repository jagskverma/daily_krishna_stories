#!/usr/bin/env python3
"""Style-normalize batch n045 (DKS_0265-0270) per docs/HOUSE_STYLE_GUIDE.md v1."""
import json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORY_DIR = os.path.join(BASE, "data", "stories")
REPORT = os.path.join(BASE, "data", "mining", "style_report", "n045.jsonl")

NEW_STORY = {
"DKS_0265": """Heaven welcomed Krishna with honour, and lost a tree. He had come up to the bright court of Indra, king of the gods, and at first no one there could guess why.

He came first as one returning what was owed. In his hands he carried the earrings of Aditi, mother of the gods — the earrings the demon Naraka had torn from her long ago, when he robbed heaven itself. Krishna had won them back when he struck Naraka down, and now he laid them before her. Aditi, pleased beyond words, took back what was hers, and there was peace between heaven and the one who had fought heaven's battle.

But Krishna had not come to Indra's heaven alone. Satyabhama, his wife, was at his side — and she had seen the Parijata, the wish-fulfilling tree of the gods, the delight of heaven itself. She wanted it growing in her own garden in Dwaraka. And Krishna, wishing to please his beloved the way any ordinary husband pleases his wife, went and took it. He lifted the great tree whole, roots and all, and set it upon Garuda, the vast eagle who bore him through the sky.

The gods were not amused. Indra's wife Shachi protested that the tree belonged to her; it was not proper, she told Krishna — Govinda, as she called him — to carry it off. And Indra himself came raging, blind with anger, and rushed at Krishna with all his host. The thunderbolt-wielder and his armies fell upon the man who had just done heaven a kindness, as though he were no more than a husband indulging his wife's whim. They had seen him return the earrings; still they misread him. The thunderbolt came down and was turned aside like a twig. Host after host of the immortals pressed in, weapons raised, and found their arms checked by a calm they could not break, a strength that gave way nowhere. One by one they were put aside, and still the tree stayed on Garuda's back.

In the end it was the gods who gave way. Indra, who had come raging, came at last to his senses, and all of heaven understood what it should have understood from the first: this was no mortal carrying off a tree. The king of the gods let the Parijata go, and the wish-fulfilling tree of heaven was given to the earth.

Krishna rode down out of the clouds, and as he came over Dwaraka he blew his conch. The whole city rose at the sound, delighted, watching the sky for the shape of the great bird. He planted the Parijata in Satyabhama's garden, and there it stood, perfuming the earth for three furlongs around. And more than that, the old tellings say: whoever came near the tree could remember the events of their past lives, and the Yadavas who stood in its shade saw themselves as they had been long before, in their own bright heavenly forms.

So the tree of heaven came down to earth at a wife's request. The gods who had lost it could only wonder at what they had learned — heaven itself could not keep what Krishna had chosen to take for the one he loved. In Satyabhama's garden the Parijata settled into the soil of Dwaraka, and its perfume drifted over the city like a promise kept.""",

"DKS_0266": """In Dwaraka, sixteen thousand one hundred brides were waiting — and one bridegroom, Krishna, who had promised himself to all of them.

They were the maidens he had freed from the demon Naraka's palace, and they had come to the city with the demon's treasures. Daughters of kings from many lands, they had been carried off from their families and shut away in the tyrant's inner palace, and now they were free. They had made their choice with their own eyes the moment they saw Krishna standing in the demon's hall — every one of them chose him before a word was spoken.

Krishna, meanwhile, took possession of the wealth, the elephants and the horses recovered from Naraka, and the city absorbed them into its storehouses almost without noticing; its mind was elsewhere. At an auspicious season, the wedding came. In separate mansions across Dwaraka, sixteen thousand one hundred brides sat veiled and waiting — and in a single moment Krishna married them all. He multiplied himself into as many forms, one for each bride, and at the same instant took the hand of every one of them, according to the ritual, in her own house. Each bride saw only her bridegroom; each believed he was hers alone. And each of them was right.

Nor did the wonder end with the ceremony. Krishna took up his place in each of those houses, living with each wife as a householder lives with his own — present to her, and to all of them, at once. How one man could be wholly present to sixteen thousand one hundred wives, none could reckon; and the old tellings say even Brahma and the gods cannot trace the path by which he did it.

As for the brides, they did what brides do in the old stories, and their joy was plain in every small act. They rose to greet him and offered him seats; they washed his feet and worshipped him; they brought him betel leaf, rest, and cooling fans, garlands and perfumes; they tended his hair, his bed, his bath. Hundreds of maidservants served each household, and the wives gave themselves to their husband with a love that only grew — laughing, glancing, shy at each new meeting, delighted at each familiar one. It did not cool with custom or with the turning of the seasons; it kept rising, fed from within, the way the same spring feeds a hundred gardens at once. They had been prisoners, and now they were wives, and their devotion poured out in the small offices of a shared life.

What the old tellings wonder at is not the size of the wedding but its closeness. A king might marry many wives by proxy, or visit them in turn; this was different. Each marriage was complete. Each bride had her husband whole — not a share of him divided among thousands, but all of him, present to her alone, in her own house, every day.

So Dwaraka settled into an even stranger peace: a city of palaces, each with its bride and its lord, and a lord who was everywhere and never absent. The maidens Naraka had stolen were home at last, and the city that had received them as guests came to know them as queens — each with her own house, her own garden, her own claim on the same undivided heart. The one who had freed them had become, to each of them, the whole of home.""",

"DKS_0267": """The war at Kurukshetra was over, and the five Pandava brothers had won it — but victory had left Hastinapura a house of mourning, its sons fallen, its future in doubt. Krishna, who had stood by them through the long conflict, was preparing to return to his own city, Dwaraka, when the cry came: a young woman running toward him across the palace courtyard, her hands clasped, her face white with terror.

"Protect me, protect me, great lord, master of the world!" she cried. "Let this blazing iron-tipped arrow burn me — but let the child in my womb not fall."

She was Uttara, daughter of King Virata, and the child she carried was all that remained of the Pandavas' hopes. The war had given them a kingdom and cost them nearly everything else; the next generation of their house had been cut down in the terrible days after the fighting, and one unborn child now stood between the Kuru line and its end. It was to destroy that last hope that Drona's son Ashvatthama had loosed his weapon, aiming so that the Pandavas would be left without an heir.

And the arrow was already in the air, flying toward her. It was the Brahmashira, the supreme weapon of its age — unerring, they said, beyond any counter, a thing no shield could stop and no wall turn. It sought its mark like a falcon and was not known to miss, and its mark now was a few hundred yards of palace air, and the small life at the end of them.

Krishna, who dwells in all beings, understood everything in a moment. The weapon's intent was as plain to him as its flight, and the terror in the young woman's face moved him more than the fire in the sky. He reached for no bow and shouted no command. Quietly, by his own power, he entered the womb of Virata's daughter and gathered the unborn child into his protection, and the Sudarshana disc blazed up around the small life within her — a ring of fire, patient and absolute, that no weapon could pass.

In the courtyard a hush fell. Men held their breath; women turned their faces away; even the birds had stopped calling. The unerring arrow arrived — and found nothing to strike. Against that quiet ring of light, the weapon that had never failed, the weapon armies had learned to fear at terrible cost, spent itself and died, quenched as a flame is quenched. Those who watched drew a breath and called it a wonder — and so it was.

In time the child was born, whole and unharmed, and the Kuru line had its heir. He would be called Parikshit — the child of the womb that Krishna had entered and held. And Uttara, who had asked only that her child live, kept both her own life and his. The house that had been saved by a ring of light kept, in that small life, everything it had nearly lost.""",

"DKS_0268": """Word reached the city of Karavira that Krishna, lord of Dwaraka, was coming with his warriors, and King Shrigala, certain they meant to attack, decided to strike first. He rode out of his city instead of waiting behind its walls.

He was a king to make an army pause: terrible in battle, and said to be as strong as Indra, king of the gods. His chariot alone was a sight to stop a host — golden axles, its racks packed with weapons and with quivers that never ran empty, drawn by horses so swift that the whole machine flew along like Garuda, the great eagle, shining like the sun. It seemed the very chariot of Indra come down to earth. The king stood in it with a bow in his hand, his fiery eyes sweeping the field, whirling the weapon about him like a flash of lightning, blazing in the shine of his ornaments. The earth, it was said, sank beneath his weight. And he came at Krishna the way an insect comes at a flame.

Krishna watched him come, untroubled. He sat at ease while the great car thundered closer, and when Shrigala was within earshot, the king did not hesitate to speak his mind.

"I have heard of your work among the weak kings on Mount Gomanta," he called out, "and of the defeat of those useless warrior kings who had no leader. But I stand here as emperor of the world. You are not expert in the art of war — you will fly away the moment I obstruct you. You are alone, and I have my army, so I will not fight you with all of them. Come: I shall fight you alone, and one of us will meet his death in a fair fight. If you are slain, I shall be the only Vasudeva in the world. And if I am slain, you shall be the only one."

Vasudeva was one of Krishna's own names — the name that said whose son he was. Krishna, who could forgive anything, looked at the blazing king and answered simply: "Strike me as you wish." And he held up his discus.

The two came together, and for a moment the field had the look of a forest where two infuriated elephants are about to meet — the air gone still before the clash.

Shrigala lost his senses in anger. He loosed a net of arrows at Krishna; he hurled maces and every weapon that came to hand, weapons that flew trailing flame. And Krishna stood there, motionless, like a mountain taking the weather. The king of Karavira fought the way a storm fights a mountain: he emptied his quivers, flung his maces, sent weapon after weapon streaming fire at the motionless man — and the mountain did not move.

Then Krishna moved. Wrath rose in him at last, and he hurled the discus at Shrigala's breast. It struck as it always had: the king's heart was pierced, and his life and his joy went out in the same instant. Shrigala fell from his chariot, and the emperor of the world lay still upon the earth that had once seemed to sink beneath his weight.

At the sight, his soldiers lost heart and fled. Some rushed weeping into the city; some stayed beside their fallen king, performing the rites for the dead and mourning him with heavy hearts. And over the field, Krishna raised his hand.

"Do not fear," he told the people assembled there, his voice like the rumbling of clouds. "Do not fear."

The subjects and ministers of Karavira wept over their king, fallen in his pride, and then Shrigala's queens came out of the city with their sons, and when they saw their royal husband lying in that plight, they beat their breasts and wept.

The king who had wanted to be the only Vasudeva in the world was gone. And the man he had challenged stood over his body, telling his people not to fear.""",

"DKS_0269": """A battle raged at the great sacrificial ground, where the Yadavas — Krishna's own clan — and the five Pandava brothers had gathered for a great martial festival. The demons, the Asuras, were losing it; their host broke and ran — until their own commander stopped them with words sharper than any weapon.

"Why do you take to your heels?" Nikumbha roared after the routed host. "You swore to avenge the destruction of your kinsmen! Break that oath and fly, and whose face will you look upon when you reach your own house? What will your wives say? Shame on you! Shame on you!"

Shame did what fear could not. The Asuras turned and came back with double vigour into the fight — and the Yadavas, who had thought the field won, had to fight it all over again. The struggle that followed was terrible. Those who stood their ground were cut down; those who rose into the sky were slain by Indra's son Jayanta and by Pravara, the brahmin warrior; and the killing went on until, the old tellings say, the field ran red, thick as a river in flood.

Nikumbha himself fought like a man who had decided he would never retreat. He struck Pravara down with his iron club. Indra's son caught his comrade as he fell, embraced him, and ran back at the Asura. Arrows rained on Nikumbha, and he took them, until at last he thought: Why exhaust myself against Indra's son? It is Krishna who killed my kinsmen. Let me fight him.

He vanished from that spot and reappeared where Krishna stood. Above them, on Airavata his white elephant, Indra himself had come with the gods to watch the battle, and trumpets had sounded for Jayanta's victories. Nikumbha gave a lion's roar and hurled himself at Krishna — at Arjuna, Bhima, and Yudhishthira, at the brothers, the Yadava chiefs, and the kings — and so great were his powers of illusion that none of those masters of weapons could see him at all. He was a storm no eye could follow.

Krishna closed his eyes and called on Vilwodakeshwara, the lord of goblins, and the power of that lord parted the veil. Suddenly everyone could see Nikumbha, standing before them like the summit of Kailasa, the mountain where Shiva dwells, inviting Krishna to fight.

Arjuna had already strung his great bow, the Gandiva. He loosed his shafts — and they struck Nikumbha's body and shattered, falling broken to the ground. "What is this, Krishna?" Arjuna asked in astonishment. "My arrows pierce mountains. Why are they useless here?"

Krishna smiled and began to answer — and then the demon was gone, breaking away and fleeing toward the mountains, into the cave of Shatpura, the stronghold of his kin. Krishna followed him in.

There, in the darkness of the cave, a voice that no eye could see commanded him: use the discus. Saluting Mahadeva — another name for Shiva — whose presence filled that mountain stronghold, Krishna loosed his discus, the Sudarshana, bright as the disc of the sun. It flew across the gloom and took the great demon's head, with its beautiful earrings, from his body. It returned to its master's hand, and Nikumbha fell — the terror of the field ended in a single stroke.

The routed Asuras, who had come back to fight at his bidding, had no one left to rally them. And the cave of Shatpura, stronghold of his kin, fell silent.""",

"DKS_0270": """All day the Yadavas, Krishna's own people, had been at sport in the sea — swimming, laughing, racing the waves — while the whole city of Dwaraka lay at leisure, its palaces open, its gardens unwatched. And that, exactly, was what the demon Nikumbha had been waiting for.

Wicked and unapproachable, an old enemy of the gods, he had chosen this moment to settle a score. The old tellings are blunt about where his vengeance would lead: he was bent, they say, on his own destruction. Years before, Pradyumna — Krishna's son, foremost of all who knew illusion — had carried off Prabhavati, the daughter of Nikumbha's brother Vajranabha, and Vajranabha had been killed in that business. Nikumbha had not forgotten. Now, remembering that old enmity and biding his time, he turned his powers of illusion upon the women of the Yadavas and stole away Bhanumati, the beautiful daughter of Bhanu, from the very garden attached to her father's palace.

It should have been impossible. The garden was unapproachable, set apart for the women of the house, and no outsider could enter it by daylight. But the guards were gone — the Yadavas were all at their ocean sport, and no one had thought to leave a watch. In that weak, unguarded moment the demon cast his illusions so that no eye marked him, laid hold of the weeping maiden, and was gone with her before the garden knew it had been entered.

The cry went up almost at once. The women's quarters erupted in tumult; lamentations rang through the palace, for the maiden was gone and none could say where. Women ran this way and that, calling her name; servants searched the garden, then the streets, and found no trace of her anywhere. Vasudeva — Krishna's father — and Ahuka heard the uproar and rushed out, burning with anger, and found no one to strike, for the demon had already vanished. They went at once to Krishna, still in the clothes they had worn to the shore.

Krishna heard of the insult and moved like thunder. He mounted Garuda, his great eagle, the enemy of serpents, with his cousin Arjuna beside him; he commanded Pradyumna, whose banner bore the Makara, the great sea creature, to follow in his chariot; and he told Garuda to fly.

Soon the great bird was climbing over the rooftops of Dwaraka, and behind it came Pradyumna's chariot, its sea-creature banner streaming in the wind. Somewhere ahead, a demon was carrying off a king's daughter to avenge a theft of his own — and for once, the Yadavas were the ones chasing a thief.

But Nikumbha was a master of illusion, and he knew a hundred ways to vanish. Finding him would take all the speed of Garuda, all the arrows of Arjuna, and all the cunning of Pradyumna — and even then, the chase was only just beginning."""
}

CHANGED = {
    "DKS_0265": "major",
    "DKS_0266": "minor",
    "DKS_0267": "minor",
    "DKS_0268": "major",
    "DKS_0269": "major",
    "DKS_0270": "minor",
}

REPORTS = [
{"story_id": "DKS_0265", "changed": "major", "context_added": True,
 "ai_patterns_removed": [
   "'The Bhagavata Purana says it plainly, without excuse' source-citation aside removed",
   "title pile-up ('the lord of all things', 'the ruler of the universe', 'the master of all things') reduced to plain 'Krishna'",
   "lift-and-set-on-Garuda beat, which the old text told twice, told once",
   "unintroduced Uddhava narrator-frame tail ('Uddhava remembered the episode later...') removed",
   "'wishing to please his beloved like a common man' motif, said twice, kept only once (at the taking of the tree)"],
 "child_friendly_changes": [
   "Satyabhama glossed as Krishna's wife at first mention",
   "Garuda glossed as the vast eagle who bore him through the sky",
   "'Govinda' glossed as the name Shachi calls Krishna by",
   "Naraka's theft of Aditi's earrings given one context clause (Krishna won them back when he struck Naraka down) so the story stands alone",
   "'original celestial forms' rendered plainly as 'as they had been long before, in their own bright heavenly forms'",
   "counts and measures kept: the three-furlong perfume, Aditi's earrings, the single whole uprooting"],
 "risk": "Kept the tree's powers (past-life memory, the Yadavas' heavenly forms), the three-furlong perfume, Shachi's protest, the thunderbolt 'turned aside like a twig', and the gods' surrender. The double telling of the uprooting was compressed into one without losing that Krishna lifted the tree whole and that it stayed on Garuda."},

{"story_id": "DKS_0266", "changed": "minor", "context_added": False,
 "ai_patterns_removed": [
   "'The text pauses over the impossibility of it' meta-frame removed",
   "'Even Brahma and the other gods, it says, cannot trace his path' de-cited to plain narration",
   "'It is this that the storytellers cannot stop wondering at' -> 'What the old tellings wonder at'",
   "'seraglio' -> 'inner palace'",
   "'with a joy that makes the heart ache' (tells the reader what to feel) -> joy shown through the brides' acts"],
 "child_friendly_changes": [
   "Krishna named in the first line as the promised bridegroom so the story stands alone",
   "Naraka glossed 'the demon Naraka' on first mention",
   "'betel' -> 'betel leaf'",
   "all counts kept: sixteen thousand one hundred brides, one form per bride, hundreds of maidservants per household"],
 "risk": ""},

{"story_id": "DKS_0267", "changed": "minor", "context_added": False,
 "ai_patterns_removed": [
   "'The verse adds, gently: do not be astonished, for all wonders have their home in him' meta aside removed (commentary, not event)",
   "epithet stack in Uttara's cry ('great yogin, Lord of gods, master of the world') reduced to 'great lord, master of the world'",
   "theological register ('He was the indwelling soul of all beings, the lord of yoga') -> 'Krishna, who dwells in all beings'"],
 "child_friendly_changes": [
   "Pandavas glossed as 'the five Pandava brothers'; Krishna as one who 'stood by them through the long conflict'; Dwaraka as 'his own city'",
   "'embryo' -> 'child in my womb'",
   "'By his own maya' -> 'Quietly, by his own power'",
   "Brahmashira and Sudarshana kept with plain glosses ('supreme weapon of its age', 'a ring of fire')"],
 "risk": "The verse's closing reassurance was cut as commentary; the crowd's 'called it a wonder' beat remains. Parikshit's naming gloss ('the child of the womb that Krishna had entered and held') kept exactly."},

{"story_id": "DKS_0268", "changed": "major", "context_added": False,
 "ai_patterns_removed": [
   "gore line 'bleeding like a cleft mountain' removed",
   "archaic 'endued with the prowess of Indra' -> 'as strong as Indra, king of the gods'",
   "'useless Kshatriyas' -> 'useless warrior kings'",
   "mountain-simile pile-up thinned (cleft mountain + struck-by-thunderbolt -> one closing image)"],
 "child_friendly_changes": [
   "'Vasudeva' glossed as one of Krishna's own names — the name that said whose son he was (the boast 'I shall be the only Vasudeva' kept verbatim)",
   "Garuda in the chariot simile glossed 'the great eagle'",
   "Krishna anchored as 'lord of Dwaraka' in the first line",
   "king's mourning rites, queens' lament, and Krishna's 'Do not fear' kept in plain prose"],
 "risk": "'If you are slain, I shall be the only Vasudeva in the world...' kept verbatim; the name gloss sits beside it. Single-combat terms, quivers that never ran empty, the discus to the breast, and Krishna raising his hand over the fallen king's city all preserved."},

{"story_id": "DKS_0269", "changed": "major", "context_added": True,
 "ai_patterns_removed": [
   "opening that started mid-rout given one scene-setting sentence (who, where, why fighting)",
   "'such was the slaughter that the field was said to run with a river of blood, thick as a river in the rainy season' softened to 'the field ran red, thick as a river in flood'",
   "'set up a leonine shout' -> 'gave a lion's roar'",
   "unglossed 'the twice-born Pravara' -> 'the brahmin warrior Pravara'",
   "'son of Devaki' / 'son of Kunti' vocatives -> 'Krishna' / 'Arjuna' so first readers are not lost"],
 "child_friendly_changes": [
   "Asuras glossed 'the demons' at first mention",
   "'the Yadavas — Krishna's own clan — and the five Pandava brothers' spelled out",
   "Gandiva glossed 'his great bow, the Gandiva'; Airavata kept as 'his white elephant'",
   "Kailasa glossed 'the mountain where Shiva dwells'; Mahadeva glossed 'another name for Shiva'",
   "Vilwodakeshwara kept with the file's own 'lord of goblins' gloss",
   "beheading preserved with restraint ('took the great demon's head, with its beautiful earrings')"],
 "risk": "Opening sentence describes a battle at the gathering and the Asuras losing it — both implied by the file's own start mid-rout and the 'fight it all over again' beat; no event added. 'Fie on you' rendered 'Shame on you' (same rallying force). Krishna's call on Vilwodakeshwara, the unseen voice's command, the salute to Mahadeva, and the discus returning to his hand all kept."},

{"story_id": "DKS_0270", "changed": "minor", "context_added": False,
 "ai_patterns_removed": [
   "'the text is blunt about where his vengeance would lead him: he was bent, it says, on his own destruction' de-cited -> 'The old tellings are blunt... he was bent, they say, on his own destruction'",
   "redundant re-introduction of Nikumbha ('The Danava...' paragraph after he was already named) folded into one"],
 "child_friendly_changes": [
   "opening ties the Yadavas to Krishna ('Krishna's own people') so the cast is clear",
   "Nikumbha glossed 'the demon' / 'a demon lord, wicked and unapproachable, an old enemy of the gods'",
   "Garuda glossed 'his great eagle'; Arjuna glossed 'his cousin'; Pradyumna kept as 'Krishna's son'",
   "Vasudeva glossed 'Krishna's father'",
   "'the Makara, the great sea creature' gloss kept"],
 "risk": "Story ends where the file ends (the pursuit just beginning — resolved in DKS_0271); no resolution invented. Nikumbha's backstory (Prabhavati / Vajranabha) and the garden's unapproachable-by-daylight rule kept exactly."},
]

def main():
    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    pristine = {}
    before_words = {}
    for sid in NEW_STORY:
        old = json.load(open(os.path.join(STORY_DIR, sid + ".json"), encoding="utf-8"))
        pristine[sid] = old
        before_words[sid] = len(old["story"].split())

    for sid, new_story in NEW_STORY.items():
        path = os.path.join(STORY_DIR, sid + ".json")
        old = pristine[sid]
        wc_after = len(new_story.split())
        assert 450 <= wc_after <= 700, f"{sid} after-wordcount {wc_after} out of range"
        new = json.loads(json.dumps(old, ensure_ascii=False))  # deep copy, same key order
        new["story"] = new_story
        assert new["reflection"] == old["reflection"], "reflection must not change"
        new["generation_metadata"]["style_normalization"] = {
            "pass": "v1", "model": "deepseek-v4-flash", "changed": CHANGED[sid]}
        with open(path, "w", encoding="utf-8") as f:
            f.write(json.dumps(new, indent=1, ensure_ascii=False))
        print(f"{sid}: words {before_words[sid]} -> {wc_after} | changed={CHANGED[sid]}")

    # verify written files: every field byte-identical to pristine except story +
    # generation_metadata.style_normalization (round-trip formatting proven exact)
    for sid in NEW_STORY:
        now = json.load(open(os.path.join(STORY_DIR, sid + ".json"), encoding="utf-8"))
        old = pristine[sid]
        assert now["story"] == NEW_STORY[sid]
        assert now["generation_metadata"]["style_normalization"] == {
            "pass": "v1", "model": "deepseek-v4-flash", "changed": CHANGED[sid]}
        for k, v in old.items():
            if k in ("story", "generation_metadata"):
                continue
            assert now[k] == v, f"{sid}: field {k} changed!"
        for k, v in old["generation_metadata"].items():
            assert now["generation_metadata"][k] == v, f"{sid}: metadata field {k} changed!"
        print(f"{sid}: verified — only story + style_normalization changed")

    with open(REPORT, "w", encoding="utf-8") as f:
        for r in REPORTS:
            sid = r["story_id"]
            r["length_before"] = before_words[sid]
            r["length_after"] = len(NEW_STORY[sid].split())
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("report written:", REPORT)

if __name__ == "__main__":
    main()
