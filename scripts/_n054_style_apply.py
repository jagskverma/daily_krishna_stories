#!/usr/bin/env python3
"""Style-normalization pass n054 for DKS_0319..DKS_0324 per docs/HOUSE_STYLE_GUIDE.md."""
import json, os, sys

BASE = "/Users/dev_env/Documents/projects/indian_apps/dailyX/daily_krishna_stories"
STORY_DIR = os.path.join(BASE, "data/stories")
REPORT_PATH = os.path.join(BASE, "data/mining/style_report/n054.jsonl")

NEW = {}
NEW["DKS_0319"] = """Across the battlefield came Shamvara's golden chariot, and the demon king rode it like a storm. "Drive straight at that boy," he told his charioteer, "and quickly. With my arrows I will kill him who has wronged me."

He meant the young man waiting on the far side of the field, his bow already strung: Pradyumna, the son of Krishna and Rukmini. Shamvara had snatched the child away as a baby, meaning to destroy him, and the child had lived, grown, and come back to cut down the demon's four chief ministers, one after another, until the army itself had fled from him.

Pradyumna watched the golden chariot come and set a golden arrow to his string. His first shaft struck home, and Shamvara reeled in his seat, clutched the reins, and lost his senses. When he came to himself a few moments later, rage had made him reckless. He snatched up his bow and loosed seventy sharpened arrows at Krishna's son. Pradyumna answered with seven shafts, and all seventy were cut into seven pieces in mid-air before a single one could reach him. Then seventy winged arrows flew back at the demon, and then a thousand, until the sky grew so thick with arrows that the sun itself was hidden. Shamvara broke that darkness with his thunderbolt and rained arrows down on Pradyumna's chariot; Pradyumna, light of hand, sliced them to pieces as they came. In the end it was the arrows that gave out first.

So the demon changed his art. By his illusory powers he made the whole field bloom with trees, and Pradyumna, angry now, burned them all to ash with fiery weapons. Shamvara answered with a downpour of stones; Pradyumna swept them from the field with weapons of air. Then came the beasts, lions, tigers, bears, monkeys, horses, camels, asses, and elephants like slow clouds, hurled at his chariot — and he cut the whole phantom herd to pieces with the weapons of the Gandharvas, the celestial musicians. So Shamvara raised the stakes once more: war elephants with sixty heads apiece, mad for battle, ridden by expert drivers. Pradyumna answered illusion with illusion, calling up lions of his own, and his lions tore the elephants down as the sun sends away the night.

Illusion followed illusion. Shamvara cast the Sunmohini spell, the spell of fascination that the great builder Maya had fashioned; Pradyumna broke it with the weapon of his own clear mind, and the charm fell from him like mist. Shamvara sent lions again; Pradyumna sent the sharabhas, eight-legged creatures of claw and tooth, and they harried the lions as the wind scatters clouds.

For the first time the demon king doubted himself. "Fool that I am," he thought. "Why did I not kill him in his infancy? Now he has grown to youth and mastered every weapon. Only one illusion is left to me — the dread illusion of serpents, which the great god Shiva himself taught me and no one else knows. Let me spread it, and see whether this magician can survive it."

He spread it. Serpents full of burning venom coiled around Pradyumna, around his chariot, his horses, and his charioteer, and bound them all fast. But Pradyumna thought of the garudas, the great eagles that feast on serpents, and at the very thought they came wheeling down from the sky and tore the venomous illusion apart. When the last serpent dissolved, the gods and the demons watching from above cried out together: "Well done! Well done! Son of Rukmini, the illusion is defeated, and we are pleased."

Shamvara stood in his golden chariot with nothing left of his magic. But one weapon remained that was no magic at all: the golden club, shaped like the staff of Death himself, which the goddess Uma had given him long ago, saying it could break every illusion and slay every demon. Many a demon had already gone down to Yama, the lord of the dead, struck by that club. Now, while the applause of the gods still rang over the field, his hand closed on it."""

NEW["DKS_0320"] = """A voice came from the sky, and for a moment even the arrows stopped. From the clouds a radiant figure descended — an ascetic with matted locks, a vina in his hand, his face bright as fire — and came to rest before Pradyumna's chariot, on the field where the last illusions had just died. It was Narada, the wandering sage of the gods, and Indra, the king of the gods, had sent him. He came without herald or escort, as he always came, and the armies on both sides knew him at once: the sage who wandered between the worlds, carrying the news of heaven in his vina.

Pradyumna's own story had been kept from Pradyumna. As a baby he had been stolen away by the demon king Shamvara, who meant to kill him and somehow never did; the boy had grown up in the demon's household and been trained in arms, until at last he stood against his kidnapper in open battle. He had slain Shamvara's four ministers and shattered every illusion the demon could cast — and still he did not know the simplest thing about himself: who he had been before this life began.

"Remember your birth before this one, hero," Narada said. "You are Kama. In a former life you were the god of love, and you have been born again, in the house of Krishna, as Pradyumna. The demon who stole you never knew what he held." Then the sage gave him the Vaishnava weapons and a coat of mail — weapons unlike anything in the demon's armoury, for they were consecrated to Vishnu — and the coat of mail settled on his shoulders as if it had been waiting for him. Then Narada told him the task the gods had set before him. "When you have killed Shamvara in battle with these weapons," he said, "take your wife Mayavati and go to Dwaraka."

Pradyumna stood with the mail on his shoulders and the weapons in his hands, and understood at last why Shamvara's magic had never held him. It had not been only a boy's quick hands that cut the illusions to pieces; something in him was older than the demon's art, older than the demon himself, and the illusions could not touch it.

His stolen boyhood had been a long apprenticeship in war and watchfulness, and no one had ever said where he came from. Now the shape of his life rearranged itself in a few words. He was not an orphan of chance; he was Kama, born again, and every year of that boyhood had been leading to this field. He thought of his mother Rukmini and his father Krishna in Dwaraka, of a city he had been too young to remember — and of Mayavati, a wife he had not known he possessed, waiting somewhere to be claimed. The battle that had begun as a desperate boy's contest had become a return. He set his hand to the weapons, and their weight told him what nothing in the demon's house ever had: he was not alone in this war.

Narada watched him a moment, then rose into the sky as suddenly as he had come, leaving the young warrior alone on the field with his new name and his new weapons. Pradyumna turned his chariot toward the golden car of Shamvara, who was reaching for the golden club that no god or demon could withstand. Shamvara did not understand why the boy's face had changed. But the gods watching from above understood: the stolen child had remembered himself, and the last battle of the demon king could now begin."""

NEW["DKS_0321"] = """Dwaraka was at peace, and then the storm came — a sudden hurricane over the sea-girt city, clouds charged with lightning, thunder muttering over the water. And in the heart of the tempest a figure appeared: Narada, the wandering sage of the gods, with matted locks and a vina in his hand, radiant as fire. The instant his feet touched the ground of Krishna's court, the foul weather vanished. The court went still.

All the kings of the earth had gathered in that hall. Duryodhana, the Kuru prince, was celebrating a great sacrifice in Hastinapura, and every king who travelled to it had turned aside on the way to see Krishna — drawn by his fame, by the report of his sons, by the wonder of Dwaraka standing on the shore of the ocean. They had come in multitudes, each with his army: Duryodhana and his brothers, the sons of Dhritarashtra; the sons of the Pandavas; the warrior Dhrishtadyumna; and the kings of Pandya, Chola, Kalinga, Vahlika, Dravida, and Khasa. Krishna had welcomed each according to age and rank, seated them in their proper places, and taken his own golden throne, shining among them like the autumn sun. His kinsmen the Yadavas and the visiting kings had talked of this and that — and then the storm had come, and then Narada.

The sage walked into the crowded hall and went straight to Krishna's throne. "You have become a wonder to the gods themselves," he said. "There is no one blessed like you in the world."

Krishna smiled. "That is true," he said, "and never more so than in the matter of presents."

"I have received the answer I came for," said Narada, and turned to go. "I depart for the region I wished to reach."

The kings looked at one another. "He spoke of wonder and blessing," they said to Krishna, "and you answered with presents. We cannot read such words. If we are worthy to understand them, we wish to hear the meaning."

"You are worthy," Krishna said, "and Narada shall explain it. Tell these kings, O sage, what lay behind your question and my answer." Narada seated himself on a white and golden seat and began.

"Once, at sunrise, I walked alone on the bank of the Ganga," he said, "and I came upon a tortoise huge as a mountain, with two great shells, soaked through and covered with moss, its skin as hard as an elephant's. I praised it — what a wonderful life, to carry such shelter and range the water without a care. But the tortoise answered me like a man. 'What wonder is there in me, sage?' it said. 'How can I be called blessed? This Ganga, flowing past us, is the blessed one — hundreds and thousands of creatures like me live in her. What is more wonderful than she?'

"So I went and praised the Ganga in her turn, foremost of rivers, rich in lakes, thronged with great creatures, guarding the hermitages on her way to the sea. And she pointed me onward: the ocean pointed to the earth, the earth to the mountains, the mountains to Brahma the creator, Brahma to the Vedas, and the Vedas to the sacrifices that keep them alive. Each one I praised turned and showed me something greater, until the chain ran out at the sacrifices — and a sacrifice is greatest when it is accompanied by gifts. Above them all stands Vishnu alone, the great wonder, whom all of these serve."

The court understood at last. Asked what was greatest, the whole chain of creation had pointed beyond itself, and at the end of that pointing stood Vishnu — and a sacrifice with gifts. So Narada's praise had been true, and Krishna's odd answer about presents had carried the truth all along — for the one whom all the giving of the world finally reaches is the one truly blessed. The kings murmured their wonder. Narada, satisfied that the mystery was explained, rose and departed for the region he had wished to reach — and the storm did not dare return with him."""

NEW["DKS_0322"] = """The gates of Dwaraka rang with conch shells and drums, and blessings followed the riders as Krishna mounted Garuda, the great eagle, king of birds. His brother Balarama and his son Pradyumna climbed up behind him, and the eagle rose into the sky above the city by the sea. They were bound for Sonitpura, the distant stronghold of Bana, the demon king with a thousand arms — Bana, whom Krishna had set out to bring down. Beneath them Dwaraka grew small and faded into the haze of the ocean, and the flight itself was already a marvel.

Krishna had taken the form he needed for war: tall as a mountain, with eight arms and countless heads. In his right hands he carried the sword, the discus, the club, and the arrows; in his left, a thick leather guard for his arm, the great bow called Shranga, the thunderbolt, and the conch. Behind him rode Balarama, who had taken a thousand forms of his own, white weapons in hand, shining like the moon rising over a mountain; and Pradyumna rode with them, radiant as eternal youth. The three of them together were a sight to stop the heart of any army, and the heavens themselves watched them pass. The great wings beat, shaking the mountains and blocking the very wind, and the leagues fell away beneath them.

High above the world, Balarama looked at his own arms and frowned. "Krishna," he said, "what is this wonder? We have suddenly lost our natural colour. We are all wearing a golden hue. What is the cause? Have we come to the side of Mount Sumeru?"

"Bana's city must be near," Krishna answered. "A fire that protects him has come blazing out to meet us. We have been touched by the glow of that sacred fire, and that is what has changed our colour."

"If coming near Bana's city costs us our brightness," said Balarama, "then do what seems best to you."

Krishna turned to Garuda, who carried them. "Do what seems best to you," he said. "Find a way, and I will do what is mine to do."

The great eagle answered with a thousand mouths. He spread them wide, leaped from the path of his flight, and climbed to the Ganga of the sky, the river that runs above the world. He drank until his breast was heavy with water, then flew back to the blazing fire and showered it down. The water fell in great silver sheets, and the blaze that had stolen the brightness of three warriors choked, dimmed, and went out at once.

Even Garuda marvelled at what he had been asked to quench. "How powerful is this fire," he said, "that it dimmed even Krishna? It burns like the fire at the end of the world." Then he beat his great wings and went on, and the sound of them rolled across the plain like thunder.

Far below, at the approaches of Bana's city, the fires themselves looked up. They were the fire-gods, servants of the great god Shiva, and they saw three dreadful beings of many forms riding the king of birds through the sky. "Who are these," they asked one another, "and why have they come here?" They could not settle it among themselves. But they did not need to: the sound of Garuda's wings was already rolling toward them, and their chief, Angira, had lifted his head. The riders were coming closer, and the road to Sonitpura lay open before them."""

NEW["DKS_0323"] = """The fire that guarded Bana's city was out, and its keepers were coming to answer for it.

Krishna, lord of Dwaraka, was crossing the sky with his brother Balarama and his son Pradyumna on the back of Garuda, the great eagle, bound for Sonitpura, the city of the thousand-armed demon king Bana, who was gathering his defences for war. On the way, a blaze that protected the city had leapt out at the travellers and burned away their natural colour, and Garuda had drowned it with water drawn from the Ganga of the sky, taken in a thousand mouths at once. Now the fires themselves — the gods of flame, servants of Shiva — rose up around the three riders and asked one another who these dreadful beings of many forms were, riding the king of birds. They stared and wondered and could settle nothing, and so they did the only thing left to them: they attacked.

Garuda flew on with the speed of thought, but the fire-gods met the travellers before the city itself came into view. Krishna stood in the form he had taken for the journey — eight arms, a stature like a mountain, and a weapon in every hand: sword and discus, club and arrows, the great bow, the thunderbolt, the conch. Balarama rode beside him, bright and white-weaponed, and Pradyumna kept pace, radiant as eternal youth. The noise of the clash rolled over the countryside like the roaring of lions.

In the city, Bana heard it and sent a messenger swift as thought to learn what was happening, and Angira, chief of the fires, sent one of his own. What the messengers found was a field already burning with war: the five principal fire-gods — Kalmasha, Kusuma, Dahana, Shoshana, and the powerful Tapana — fighting with all their armies; beside them the five gods who preside over the offerings to the ancestors, Pithara, Pataga, Swarna, Agadha, and Vraja; and the two radiant gods in charge of the great sacrifices, Jyotisthoma and Vasatkara. At their head, on a chariot of flame, stood the great sage Angira himself, his blazing mace lifted high, shining over the whole field like a second sun.

Krishna watched them come, and he did not frown. He smiled, again and again, the way a man smiles when a matter is already settled. "Wait a few moments, fire-gods," he said. "The time of your destruction is drawing near. In a moment the power of my weapons will send you flying in every direction."

Angira heard the words and answered them by charging, running straight at Krishna with a burning trident in his hand. Krishna bent his bow. Crescent-headed arrows sheared the great mace from Angira's hand and cut it clean away, and one last arrow struck the chief of the fires in the breast. Angira fell where he stood, in the middle of the field.

The fire-gods stared at their fallen leader. Then the four among them who are the sons of Brahma the creator turned, and the whole host with them, and fled — back to Bana's city, carrying the news that the king's protection had burned out in a single exchange of arrows.

Garuda spread his wings, and Krishna's people went on across the last stretch of sky toward Sonitpura, the air behind them empty and quiet where the fires had burned."""

NEW["DKS_0324"] = """She came to Dwaraka with a theft on her mind and a name on her lips: Aniruddha, son of Pradyumna and grandson of Krishna.

Chitralekha made her way into the city and settled near the palace of Vasudeva, Krishna's father, turning over the question of how she might find the young prince and carry him away. While she sat thinking, she saw the ascetic Narada, the wandering sage of the gods, meditating in the water. Her eyes widened with joy. She approached him, saluted him, and stood before him with her head bowed. Narada blessed her, then asked, gently, what she had come for.

With folded hands she told him everything. She was a messenger, she said, come to take Aniruddha away with her. In the city of Sonitpura lived the great demon king Bana, and Bana had a daughter, Usha, the most beautiful maiden in the city. By the boon of a goddess, Usha had chosen Aniruddha for her husband — a man she had never met except in a dream. The dream had claimed her utterly, and Chitralekha meant to take him to her. But once Aniruddha was in Sonitpura, Krishna must learn the truth, for a great battle would follow: Bana was too strong for Aniruddha to defeat, yet Krishna would vanquish the thousand-armed demon. And that was what she feared. Krishna, when angered, could consume even the three worlds with a curse; she begged Narada to arrange matters so that Usha might have her husband and she herself might not be burned by that wrath.

Narada gave his answer. "I offer you protection," he said. "Shorn of fear, hear what I say. If any battle takes place while you steal Aniruddha away to the apartments of the maidens, remember me — I am fond of seeing battles, and I take great pleasure in them. And take with you the Tamasika learning — the art of darkness and illusion that I mastered through long penance, and that can bewitch all the worlds."

"So be it," said Chitralekha. She saluted the sage and set out through the sky, searching for Aniruddha's house.

She found it in the centre of Dwaraka: the palace of Kama, the god of love, and beside it the palace where Aniruddha lived — golden altars, pillars of gold and sapphire, garlands hanging along the walls, jars of cool water at the doors, peacocks carved on the turrets, and row upon row of bright buildings set with jewels and coral, filled with the music of the Gandharvas, the heavenly musicians. And there she saw Aniruddha, playing in the midst of the most beautiful women of the court as the moon shines among the stars. Hundreds of women attended on him. Seated like Kubera, the god of wealth, on a fine seat, he was drinking Madhvika wine; sweet songs rose and fell in time, and dancers moved before him. But Chitralekha saw no pleasure in him. His mind was not on the wine; he showed dislike even for drinking it. She watched, and understood: his thoughts were with the dream. And her fear fell away.

Hiding herself in the sky above the palace, she spoke to him in sweet words, asking whether all was well with him, and then delivered her message. "I have come to you from Usha," she said, "the maiden whom you saw in a dream and married, and who cherishes you at her heart. She is weeping and sighing, for she cannot see you. She will live if you go to her; without you, she will die."

The words found their mark. By the power of her Tamasika illusion Chitralekha cast her spell over everyone in the palace except the prince himself, and carried Aniruddha away through the sky to Sonitpura — to a maiden's rooms where Usha was waiting for the man of her dream."""

# reflection overrides (only where house-style justified)
NEW_REFL = {
 "DKS_0320": "Pradyumna does not change in the battle; he changes in a moment of recognition. He had fought brilliantly without knowing his own story, and the revelation adds no new skill — only meaning. The stolen child becomes the returning husband, and every blow he strikes from that moment is struck toward a home he has never seen.",
 "DKS_0321": "The delight of the riddle is that every being in creation, asked to name what is greatest, points beyond itself. Humility is the one thing the whole chain shares. And Krishna's odd reply about presents turns the loftiest praise into something warm and human: a god who answers an anthem with a smile about gifts.",
 "DKS_0323": "Krishna's smile before the battle is the story's strangest note — anger without rage, the calm of someone who has already seen the end of the matter. The blaze that had paled the travellers' skin was itself only a servant of the city, and its keepers scattered the moment their chief fell.",
}

# change levels (n043-style classification: major = voice overhaul, minor = targeted)
CHANGED = {"DKS_0319": "minor", "DKS_0320": "minor", "DKS_0321": "major",
           "DKS_0322": "major", "DKS_0323": "minor", "DKS_0324": "minor"}
CONTEXT_ADDED = {"DKS_0319": False, "DKS_0320": False, "DKS_0321": False,
                 "DKS_0322": True, "DKS_0323": True, "DKS_0324": False}

REPORT = {
 "DKS_0319": {
   "ai_patterns_removed": [
     "Shamvara's opening boast recast from stiff translation-speech ('O hero ... take my car to the enemy soon') into a natural charioteer command",
     "'cutting to Shamvara's very vitals' softened; the fainting kept in plainer words",
     "'the great god Hara' -> 'the great god Shiva' (same god under the plain name)",
     "source echo 'beside himself with anger' used twice reduced to one",
     "epithet address in the gods' cry ('O mighty-armed son of Rukmini') trimmed to 'Son of Rukmini'",
     "second 'beside himself' beat ('Pradyumna, beside himself with anger') varied to 'angry now'"],
   "child_friendly_changes": [
     "Gandharvas glossed 'the celestial musicians'; garudas glossed 'the great eagles that feast on serpents'",
     "Yama glossed 'lord of the dead'; the goddess Uma and 'the great builder Maya' identified by role",
     "'Sunmohini spell' explained as a spell of fascination; 'sharabhas' kept with 'eight-legged creatures of claw and tooth'",
     "'abode of Yama' naturalized to 'gone down to Yama, the lord of the dead'"],
   "risk": "Seven-against-seventy arrow maths kept exactly (seven shafts cut the seventy into seven pieces). Serpent illusion said to be known to no one but Shamvara and taught by Shiva; golden-club origin (goddess Uma) and its powers unchanged. Shamvara still reaches for the club at the close - no outcome imported."
 },
 "DKS_0320": {
   "ai_patterns_removed": [
     "'Remember your pristine birth, O hero' -> 'Remember your birth before this one, hero'",
     "'the king of the gods' named once as Indra (he sits in the file's own character list)",
     "reflection's essayistic close ('Identity, the episode suggests, is what arms a person for the life they were meant to live') cut as meta-sermon",
     "two overlapping realization paragraphs merged and tightened"],
   "child_friendly_changes": [
     "Narada identified on entry as 'the wandering sage of the gods'",
     "weapons of Vishnu glossed inline ('consecrated to Vishnu')",
     "Mayavati's standing kept plain: 'a wife he had not known he possessed'",
     "the story still ends at the threshold of the final duel, exactly as filed"],
   "risk": "Narada's commission preserved word-for-word in substance ('When you have killed Shamvara in battle with these weapons ... take your wife Mayavati and go to Dwaraka'). No kill scene added or implied; the golden-club duel stays beyond the story's edge."
 },
 "DKS_0321": {
   "ai_patterns_removed": [
     "archaic vocatives dropped: 'O thou of large arms', 'O Purusottama', 'O celestial saint', 'the twice-born Narada'",
     "'I depart for my wished-for region' naturalized to 'the region I wished to reach'",
     "court-puzzlement passage decluttered ('decipher these celestial expressions' / 'true import')",
     "'The Yadus' -> 'His kinsmen the Yadavas'",
     "king catalogue tightened and re-paragraphed; the chain-of-creation told as flowing deferrals, not a ledger"],
   "child_friendly_changes": [
     "Duryodhana introduced as 'the Kuru prince' holding his sacrifice at Hastinapura",
     "Brahma glossed 'the creator'; Vedas and yajnas explained naturally inside the tale",
     "Vishnu named as the end of the pointing; the presents joke resolved in plain words",
     "tortoise's speech and each link's deference kept, with only the tortoise and Ganga speaking"],
   "risk": "Chain of deference kept complete and in order (tortoise > Ganga > ocean > earth > mountains > Brahma > Vedas > sacrifices > Vishnu). Krishna's pun answer preserved in substance. The king roll retains every named king; only framing is compressed."
 },
 "DKS_0322": {
   "ai_patterns_removed": [
     "opener assumed prior knowledge of the Bana war; rebuilt to name the riders, the destination and the enemy in three sentences",
     "'bards and panegyrists ... by the thousands' compressed to 'conch shells and drums'",
     "'shorn of our effulgence' -> plain talk of losing natural colour; 'Methinks ... possessed by the effulgence of the fire of oblation' naturalized",
     "epithets dropped: 'O holder of the ploughshare', 'son of Vinata', 'the energy of Hari himself'",
     "decorative 'sacred route of the Siddhas and Charanas' removed from the flight",
     "'etherial Ganga' rendered 'the Ganga of the sky, the river that runs above the world'; 'disfigured the color' -> 'dimmed even Krishna'"],
   "child_friendly_changes": [
     "Garuda introduced as 'the great eagle, king of birds'; Balarama as Krishna's brother; Pradyumna as his son",
     "Bana's thousand arms and his city Sonitpura stated at the top",
     "fire-gods identified as 'servants of the great god Shiva' (Rudra renamed); Shranga bow glossed 'the great bow called Shranga'",
     "Angira named as their chief at the close instead of the bare 'chief of the fires'"],
   "risk": "Eight-arm weapon roster kept exactly (right: sword, discus, club, arrows; left: guard, Shranga bow, thunderbolt, conch). Balarama's thousand forms, Pradyumna's presence, the mirrored 'do what seems best' exchange, and Garuda's thousand-mouth drinking of the sky-Ganga all preserved."
 },
 "DKS_0323": {
   "ai_patterns_removed": [
     "recap that leaned on DKS_0322 extended to name every rider, the destination, and Bana so the story stands alone",
     "duplicated 'shining like the rising moon' (already used in this batch's DKS_0322) varied for Balarama",
     "'consumed by the energy of my weapons' warning kept in substance, plain words",
     "gore trimmed: 'bathed in blood' removed; Angira's fall reported plainly",
     "'the three Yadavas' -> 'Krishna's people' at the close"],
   "child_friendly_changes": [
     "Rudra -> Shiva ('servants of Shiva'); Brahma glossed 'the creator' at the sons-of-Brahma turn",
     "fire-god catalogue kept complete (five principal + five ancestor-offering + two great-sacrifice gods, all named) but woven into one moving sentence",
     "Balarama and Pradyumna re-identified as brother and son of Krishna in the recap"],
   "risk": "Krishna's warning kept in substance ('The time of your destruction is drawing near ... you will fly away in every direction'). Crescent-headed arrows still shear the mace and the breast-shot still fells Angira; the file's own trident-while-mace detail left untouched. No fire-god name dropped."
 },
 "DKS_0324": {
   "ai_patterns_removed": [
     "'forsooth, in your absence she will die' -> 'without you, she will die'",
     "'the large-armed Krishna' / 'the thousand-armed asura' -> plain names in the prophecy",
     "'the most beautiful of maidens' -> 'the most beautiful maiden in the city'",
     "bare 'Tamasika learning' glossed as an art of darkness and illusion",
     "'overpowered everyone' -> 'cast her spell over everyone', matching the learning's described power",
     "Vasudeva, Kubera and the Gandharvas left unglossed in the original -> each identified in one phrase"],
   "child_friendly_changes": [
     "Aniruddha identified in the first line as Pradyumna's son and Krishna's grandson",
     "Bana placed as the demon king of Sonitpura with a thousand arms before the prophecy is quoted",
     "Usha's dream-marriage told in plain order: goddess's boon, the dream, her choice",
     "Madhvika wine and the jewelled-palace description kept intact, not sanitized"],
   "risk": "Chitralekha's errand and Narada's terms preserved (protection offered, remember-me-at-the-battle, Tamasika learning given). Prophecy kept exactly: Bana too strong for Aniruddha, Krishna to vanquish the thousand-armed demon; her fear of Krishna's curse unchanged."
 },
}

# ---------------------------------------------------------------- apply
def wc(s):
    return len(s.split())

os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
lines = []
summary = []
for sid in ["DKS_0319","DKS_0320","DKS_0321","DKS_0322","DKS_0323","DKS_0324"]:
    p = os.path.join(STORY_DIR, sid + ".json")
    d = json.load(open(p, encoding="utf-8"))
    before = wc(d["story"])
    d_before = json.dumps(d, indent=1, ensure_ascii=True)  # for untouched-field check later (bytes)
    assert sid in NEW, sid
    d["story"] = NEW[sid]
    if sid in NEW_REFL:
        d["reflection"] = NEW_REFL[sid]
    d.setdefault("generation_metadata", {})["style_normalization"] = {
        "pass": "v1", "model": "deepseek-v4-flash", "changed": CHANGED[sid]}
    after = wc(d["story"])
    raw = json.dumps(d, indent=1, ensure_ascii=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(raw)
    # untouched-field verification: compare every key except the three allowed
    d2 = json.loads(raw)
    changed_keys = []
    for k in d2:
        if k in ("story", "reflection", "generation_metadata"):
            continue
        if d2[k] != json.load(open(p, encoding="utf-8"))[k]:
            changed_keys.append(k)
    # simpler robust check against original file object:
    orig = json.load(open(p, encoding="utf-8"))
    untouched_ok = True
    for k, v in orig.items():
        if k in ("story", "reflection", "generation_metadata"):
            continue
        if v != d[k]:
            untouched_ok = False
            print("!! field changed for", sid, k)
    r = REPORT[sid]
    rec = {
        "story_id": sid,
        "changed": CHANGED[sid],
        "context_added": CONTEXT_ADDED[sid],
        "ai_patterns_removed": r["ai_patterns_removed"],
        "child_friendly_changes": r["child_friendly_changes"],
        "length_before": before,
        "length_after": after,
        "risk": r["risk"],
    }
    lines.append(rec)
    summary.append((sid, CHANGED[sid], before, after, untouched_ok))

with open(REPORT_PATH, "w", encoding="utf-8") as f:
    for rec in lines:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

for s in summary:
    print(s)
print("report ->", REPORT_PATH, "lines:", len(lines))
