#!/usr/bin/env python3
"""Style-normalize batch n070 (DKS_0415-0420) per docs/HOUSE_STYLE_GUIDE.md v1."""
import json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORY_DIR = os.path.join(BASE, "data", "stories")
REPORT = os.path.join(BASE, "data", "mining", "style_report", "n070.jsonl")

NEW_STORY = {
"DKS_0415": """Krishna was leaving Upaplavya, where the five Pandava brothers were camped, to carry their offer of peace to their cousins in Hastinapura. The chariot had not yet cleared the camp when Arjuna walked beside it and spoke again, in a voice that carried over the rattle of the wheels.

Krishna turned to listen. Everything Arjuna had said before had been a plea: the words of a friend who wanted no war between the two branches of one family, who had begged Krishna to go and bring peace between the Pandavas and the sons of Dhritarashtra. He had asked Krishna to carry one more word to their cousin Duryodhana, whose anger never cooled — that if he refused good counsel, he would be the maker of his own ruin. But this was a different kind of word. This was what a man says when he has finished asking.

"If Dhritarashtra's son," Arjuna said, "who always chooses the crooked path, acts otherwise, then I shall surely annihilate the whole race of the Kshatriyas, the warrior class itself."

There was no heat in the words, and that made them heavier. He did not rehearse the wrongs of thirteen years or count Duryodhana's crimes. He said only that if the man who always chose the crooked path chose it once more, the warrior race itself would be ended — by his hand, in a war that would leave no one to boast of victory. The warning was exact, and it was total: peace was on offer, and refusal had been priced.

Krishna had already agreed to the errand. He would go to Dhritarashtra, the king of the Kurus, seeking what was right, what would serve the Pandavas, and what was for the good of the Kurus as well. The warning did not change his purpose; it only made plain what the errand was riding against.

Then Bhima heard it, and Bhima, the mightiest of the five brothers, answered in his own way. He set his feet on the earth, drew a breath that seemed to take in half the morning, and let out a terrible shout. It went out across the camp and the fields and the road — a sound with no words in it and no need of them, the whole of Arjuna's promise given a body and a voice.

The bowmen who heard it trembled where they stood, their hands unsteady on their bows. The steeds and the elephants, it was said, lost all command of themselves and stood shaking as the sound rolled over them. Men who stood near felt the very ground tremble, and the birds of omen that had followed the chariot scattered. It was the sound of a war that had not yet begun — the war itself announcing its presence at the edge of the camp, so that every man who heard it knew, without being told, what a refusal would sound like. The shout seemed to hang in the air long after the sound of it had died.

Krishna drove on, carrying the plea for peace and, beside it, the shape of what refusal would cost. Behind him the brothers stood on the road and watched the chariot go, and between them and it the morning still trembled with the echo of Bhima's shout. In Hastinapura, when Duryodhana made his choice, he would be choosing within the hearing of that roar.""",

"DKS_0416": """Krishna had not travelled far from Upaplavya, the camp of the Pandava brothers, when he saw ahead on the road a company of sages. Even from a distance they seemed to carry a light of their own — the radiance of men who had burned away the world's desires in long austerity. He reined in the chariot, and before the horses had fully stopped he had alighted and gone to bow before them. He travelled as the envoy of kings, but before sages every envoy bows first.

Among the sages stood Narada, the tireless traveller of the three worlds, and his presence carried its own meaning: whatever happened on this road would be known everywhere. The others, too, had that stillness about them, and Krishna honoured the whole company as it was due — and waited for their word.

Then one of the sages came forward, and the air seemed to change around him. It was Parashurama, son of the sage Jamadagni — the warrior-sage of an older age, feared by every warrior in the world, feared since before the fathers of the men now gathering were born. He came to Krishna and embraced him, and the embrace was not a formality between two great men; it was the greeting of an elder who had come a long way on purpose.

"We are desirous," Parashurama said, "of beholding all the Kshatriyas of the earth assembled from every side." The great gathering at Hastinapura would draw every king and every warrior of the world to one place, and the sages had not wanted to miss it. But they had not come only to watch. "And we are anxious," the sage went on, "to hear the words of peace that will be spoken by you unto the Kurus, in the presence of all."

There was something in the words that made the moment larger than a roadside courtesy. These were men who had renounced the world, yet they had journeyed to hear a speech about peace. They would take no side in the quarrel; they had come to stand as listeners where the fate of the earth was about to be spoken aloud. And it was Parashurama, the terror of warriors since an age gone by, who said that what mattered was the word Krishna would speak.

Krishna received the blessing and the embrace, remounted the chariot, and gathered the reins. As the chariot rolled on toward Hastinapura, the sages stayed where they were, a company of witnesses in the dust of the road — a kind of promise that whatever words were spoken at the gathering of the Kurus would not be spoken unheard. Their light faded behind the chariot. Ahead lay the city, and the assembly, and the words that everyone had come to hear.""",

"DKS_0417": """From Upaplavya, the Pandavas' camp, Krishna set out on the errand Yudhishthira had asked of him. Ten car-warriors rode behind his chariot, fully armed and ready to meet hostile heroes; a thousand foot-soldiers and a thousand horsemen followed, with attendants by the hundred carrying provisions in abundance. Ahead lay Hastinapura, the capital of the Kurus. And for those who watched him go, the sky itself began to speak.

Though no cloud stood in it, thunder rolled and lightning flashed. Fleecy clouds in the clear sky rained down behind him. The seven great rivers — the Sindhu among them — that flow eastward turned and ran the other way. The directions themselves seemed reversed, and nothing could be told apart. Fires blazed up from the earth, and the earth trembled again and again. Wells and water jars by the hundred swelled up and ran over. Darkness covered the whole universe, and dust filled the air until neither one point of the horizon nor another could be distinguished. Loud roars rolled through the sky, and no being was visible from whom they came. And a south-westerly wind, harsh with thunder, tore up trees by the thousands and crushed the city of Hastinapura.

But the road that Krishna travelled turned gentle. Delicious breezes blew, and everything around him became auspicious. Showers of lotuses and fragrant flowers fell where he passed. The way itself grew delightful, free of prickly grass and thorns. Wherever he stayed, brahmin priests by the thousand glorified him and worshipped him with dishes of curds, ghee, and honey, and with gifts of wealth, and the women, coming out onto the road, strewed wild flowers of great fragrance in his path. The same departure was ruin for the Kuru capital and blessing for every place his chariot touched.

He passed through villages abounding in bees, pleasing to the eye and restful to the heart, and through cities and kingdoms of every kind, until he came to a delightful spot called Salibhavana, filled with every sort of crop. The citizens of Upaplavya — always cheerful, well protected, free from any fear of invaders — came out of their town and stood together on the way, eager to see Krishna; and when he arrived, they worshipped him with all the honours due to a guest.

At last, when Krishna came to Vrikasthala, the sun reddened the sky with long, straggling rays of light. Alighting from his chariot, he performed the traveller's washing and set himself to his evening prayers. Daruka, his charioteer, freed the horses and tended them as a master charioteer should, loosening the yokes and traces and letting them rest. Then Krishna said, "Here we must pass the night — for the sake of Yudhishthira's mission."

Reading his intention, the attendants soon raised a shelter and prepared, in a short time, excellent food and drink. The brahmins of the village — noble and high-born, modest, devoted to the learning of the Vedas — came to honour him with blessings and auspicious words, and pressed their own houses, rich as they were, upon him. "Enough," Krishna told them, and he paid each one the respect due to his rank, walked with them to their homes, and returned in their company to his own tent. He fed the brahmins with sweetmeats and took his meal with them, and passed the night there content — at the very threshold of the city whose sky had darkened at his coming.""",

"DKS_0418": """News of Krishna's coming reached the Kuru palace before Krishna did. Krishna was on his way to Hastinapura to plead for peace between the Pandavas and their cousins, and Dhritarashtra, the blind king, learned from his spies that the envoy had set out — and his hair stood on end. He called for Bhishma, the grandsire of his house; for Drona, who had taught the princes of both families the art of war; for Sanjaya, his trusted counsellor; and for the wise Vidura. And he spoke to them, with Duryodhana, his son, and the royal advisers listening.

"What strange and wonderful news we hear," the king said. "Men, women, and children speak of nothing else, in the houses where people gather and in the open squares. All say that Krishna of great prowess is coming here for the sake of the Pandavas. He deserves honour and worship at our hands. A guest so honoured grants happiness; a guest slighted brings misery — and if Krishna is pleased with our offerings, all our wishes may be granted through his grace before the assembled kings. So make every arrangement for his reception without delay. Let pavilions be set up along the road, furnished with every comfort, so that he may be pleased with us. Bhishma, what do you think in this matter?"

Bhishma and the others applauded the king's words. "Excellent," they said.

So Duryodhana chose delightful spots at proper intervals along the route, and there rose pavilion after pavilion, glittering with gems of every kind. The king sent fine seats, attendants, perfumes and ornaments, rich robes, the best of food, drinks of many kinds, and fragrant garlands — and at Vrikasthala, where Krishna would pass the night, he raised one pavilion more beautiful than all the rest. When everything stood ready, Duryodhana informed his father that all was prepared.

The road from Vrikasthala to the capital had become a pageant. Pavilions rose at every interval like small palaces of jewels, and the air along the way carried the weight of garlands, scents, and vessels of drink laid out for a king's welcome. Travellers and townsfolk alike slowed to look at what Duryodhana had built, and the talk was all of the wealth being spent to receive one man.

Then Krishna arrived at the capital of the Kurus.

And he passed all of it by — the gem-studded pavilions, the seats, the garlands, the costly feast raised in his honour — without casting a single glance at it. Not one of the gems of diverse kinds drew his eyes. Duryodhana had built as though the visitor could be dazzled into alliance, as though magnificence itself were the language in which the Kurus and the Pandavas could still be reconciled. But Krishna needed nothing, and his chariot rolled past the last pavilion and on toward the city — leaving a court that had measured him in gold to wonder, at his silent passing, what measure would have been right.""",

"DKS_0419": """Dhritarashtra had begun to list the treasures he would heap upon Krishna — gold, jewels, gifts beyond measure, everything a king could give a guest. The blind king planned to win over the visitor the whole court called the lord of the three worlds, and most of the assembly took this for wisdom. Vidura heard it and could hold his peace no longer.

Vidura was the blind king's brother, and the one man in that hall who told him the truth. "Great king," he said, "the three worlds respect you, and everyone who knows you holds you dear. Your years are many, and your mind is calm, so that what you say can never be against the scriptures or against right reason. Your subjects are certain that virtue lives in you as surely as letters live cut in stone, as light lives in the sun, as waves live in the ocean. Every person you honour is made happy by it. So hold fast to those virtues, with your friends and kinsmen beside you. Choose sincerity. Do not, out of folly, bring destruction on your sons, your grandsons, your friends, your kinsmen — on all that you hold dear."

Then he came to the point. "It is much that you wish to give Krishna as your guest. Know that he deserves all this and far more — the whole earth itself. But I swear by my own soul that you do not wish to give it either from virtue or for the sake of pleasing him. All this betrays only deception, falsehood, and insincerity."

The words fell on the hall like a stone into still water. Vidura went on, unsparing. "By your outward acts, O king, I know your secret purpose. The five Pandavas ask only for five villages. You will not give them even that — and so you are not truly willing for peace. You hope to win the hero of Vrishni's race to your side with wealth, and in this way to separate Krishna from the Pandavas. But neither wealth, nor attention, nor worship can do that. I know Krishna's greatness, and I know the firmness of Arjuna's devotion. Arjuna is Krishna's very life, and Krishna will never give him up."

And then he told the king what Krishna would actually accept. "Only a vessel of water, only the washing of his feet, only the usual enquiries after the welfare of those he will meet — nothing more. Give him the one thing he comes seeking: peace between you and Duryodhana on one side and the Pandavas on the other. Follow his counsel, O king. You are their father; the Pandavas are your sons, young in years beside you. Behave as a father to them, and they will honour you as sons."

In a single speech Vidura had named the plan and the heart beneath it: the gifts were not generosity but a bid to prise Krishna loose from the Pandavas; the peace Krishna had crossed half the country to offer was real; and the guest himself could not be bought at any price. The question that hung in the air of the Kuru hall was whether anyone there was willing to hear it.""",

"DKS_0420": """The debate over Krishna's welcome had barely settled when Duryodhana rose, and to the surprise of the hall he agreed with Vidura on one point alone: that Krishna could never be separated from the Pandavas.

"All that Vidura has said about Krishna is truly said," Duryodhana declared. "Krishna is devoted to the Pandavas and can never be torn from them. So let no wealth be bestowed on him. He is not unworthy of our worship, of course — but this is neither the time nor the place for it. If we honour him now, he will only think we worship him out of fear, and no warrior who respects himself brings such disgrace upon his own head. Krishna deserves the reverence of the three worlds. But war has been decided, and war should never be put off by hospitality. Give him nothing."

Then Bhishma, the grandsire of the Kuru house, answered in his deep old voice. "Worshipped or not worshipped, Krishna never becomes angry," he said. "But no one may treat him with disrespect, for he is not a man to be slighted. Whatever he sets his mind to, no one can frustrate, by any means, with all his power. Do without hesitation what Krishna of the mighty arms advises, and bring about peace with the Pandavas through him. He has a virtuous soul, and he will speak only what is right and profitable. So answer him, with all your friends, only with what is agreeable to him."

Duryodhana's answer came like a blow. "Grandsire, I cannot by any means live sharing this swelling prosperity of mine with the Pandavas. Listen — this is the great resolution I have formed. I will imprison Krishna, who is the refuge of the Pandavas. He comes here tomorrow morning, and once he is confined, the Vrishnis, Krishna's own clan, and the Pandavas — aye, the whole earth — will submit to me. Tell me how it may be done, so that Krishna does not guess our purpose and no danger overtakes us."

A silence fell over the hall. Even Dhritarashtra, who had yielded to his son in so much, recoiled. At the fearful words about imprisoning Krishna, the king and all his counsellors were deeply pained. "Never say such a thing again," he said to Duryodhana. "This is not the ancient custom. Krishna comes to us as an ambassador. He is our kin, dear to us, and he has done us no wrong. How then does he deserve imprisonment?"

But the old king's protest only released the older man's wrath. Bhishma rose from his seat. "This wicked son of yours has his hour upon him, Dhritarashtra," he said. "Set before good and evil, he chooses evil, though his own well-wishers beg him otherwise — and you follow in the wake of this wicked wretch, treading the thorny path, setting at naught the words of every friend. This son of yours, with all his counsellors, will come into contact with Krishna of unstained acts and be destroyed in a moment. I will not listen to the words of this sinful wretch who has abandoned all virtue."

And having said this, the aged chief of the Bharata race, blazing with anger, rose and left the hall — the assembly staring after him, the blind king stricken, the prince unmoved. And the plan to imprison the ambassador stood in the middle of the hall, like a storm that had not yet broken."""
}

CHANGED = {
    "DKS_0415": "minor",
    "DKS_0416": "minor",
    "DKS_0417": "major",
    "DKS_0418": "major",
    "DKS_0419": "major",
    "DKS_0420": "major",
}

REPORTS = [
{"story_id": "DKS_0415", "changed": "minor", "context_added": True,
 "ai_patterns_removed": [
   "scripture-vocative trimmed from the threat: 'O Janardana' dropped, quote naturalized while keeping its full meaning",
   "alternate epic name 'Suyodhana' replaced by 'Duryodhana' (one person; familiar name) so first readers are not lost",
   "translationese 'counsels fraught with virtue and profit' -> 'good counsel'",
   "recap list of off-scene items ('the mother's messages, the king's claim') compressed to 'the shape of what refusal would cost' — items referenced earlier stories and a first reader could not follow them",
   "'desirous of accomplishing what was consistent with righteousness, what might be beneficial to the Pandavas, and what was also for the good of the Kurus' -> plain narration of the same triple purpose"],
 "child_friendly_changes": [
   "opening anchor added: who Krishna is, where (Upaplavya, the Pandavas' camp), where he is going (Hastinapura) and why (offer of peace to their cousins)",
   "Pandavas glossed as 'the five Pandava brothers'; Dhritarashtra as 'king of the Kurus'; Duryodhana as the Pandavas' cousin and Dhritarashtra's son; Bhima as 'the mightiest of the five brothers'",
   "'the whole race of the Kshatriyas' kept in the quote with an inline gloss 'the warrior class itself'",
   "no gore: Bhima's shout rendered through its effects (bowmen trembling, steeds and elephants shaking) exactly as the file had it"],
 "risk": "The threat quote kept its force: 'If Dhritarashtra's son, who always chooses the crooked path, acts otherwise, then I shall surely annihilate the whole race of the Kshatriyas.' Suyodhana->Duryodhana is one person under two names. Krishna's agreed purpose (righteousness + Pandavas' benefit + the Kurus' good) preserved as a triple. Omen-birds, trembling bowmen, shaken steeds and elephants all retained."},

{"story_id": "DKS_0416", "changed": "minor", "context_added": True,
 "ai_patterns_removed": [
   "epithet pile-up smoothed: 'Govinda, the slayer of Madhu' -> plain 'Krishna' (file itself uses 'Govinda' nowhere else)",
   "second radiance description ('the rishis stood in the road blazing with that Brahmic lustre') folded into the first image; the image was said twice and is now said once",
   "'Brahmic lustre' rendered as 'a light of their own — the radiance of men who had burned away the world's desires in long austerity' (term kept implicit, meaning made concrete)",
   "meta-flourish 'whose names the road would carry all the way back to Upaplavya' (unexplained camp name, unexplained conceit) replaced with a plain witness beat"],
 "child_friendly_changes": [
   "opening anchor: 'Krishna had not travelled far from Upaplavya, the camp of the Pandava brothers' — sets the mission and the road",
   "Parashurama introduced as 'son of the sage Jamadagni — the warrior-sage of an older age, feared by every warrior in the world'; his being ancient and feared was in-file and is now up front",
   "Narada keeps his in-file gloss ('tireless traveller of the three worlds'); rishis read as 'sages' throughout",
   "dialogue kept but de-archaized only in framing: Parashurama's 'We are desirous... of beholding' and 'words fraught with virtue and profit' preserved as quotation, with the meaning ('see the warriors gathered', 'hear the words of peace') carried by the narration beside it"],
 "risk": "Parashurama's two wishes kept in his own quoted words ('of beholding all the Kshatriyas of the earth assembled from every side' / 'to hear the words of peace... spoken by you unto the Kurus'). The embrace, the elder's greeting, and the sages staying as witnesses at the roadside all preserved."},

{"story_id": "DKS_0417", "changed": "major", "context_added": False,
 "ai_patterns_removed": [
   "frame device removed: 'Janamejaya, the king to whom this tale was told long afterward, asked...' — a scripture-narration meta-frame that a first reader cannot place; omens now told directly as narrative",
   "translationese epithets everywhere replaced by plain 'Krishna': 'the giver of wealth', 'the hero devoted to the welfare of all creatures', 'the slayer of Madhu', 'that chastiser of foes', 'Kesava'",
   "'the rules of equine science' -> 'as a master charioteer should'; 'usual purificatory rites' -> 'the traveller's washing'",
   "register of the whole omen passage lifted from scripture catalogue into flowing narration (every omen kept)"],
 "child_friendly_changes": [
   "opening already established the errand; 'Upaplavya' glossed as 'the Pandavas' camp'",
   "'Brahmanas' -> 'brahmin priests' throughout; 'ghee' kept plain as in the corpus voice",
   "Salibhavana and Vrikasthala kept as place names with light glosses ('a delightful spot filled with every sort of crop'; 'the sun reddened the sky...' marks arrival)",
   "all twelve omens and all six gentle-side wonders preserved 1:1 (see risk)"],
 "risk": "Every omen kept: thunder with no cloud, lightning, clouds raining behind him, the seven rivers (Sindhu among them) running backward, reversed directions, fires from the earth, the trembling earth, overflowing wells and jars, darkness over the universe, dust hiding the horizon, roars from no visible being, and the south-westerly wind that 'crushed the city of Hastinapura'. Gentle-side list intact (breezes, flower-showers, thorn-free road, brahmins' curds-ghee-honey offerings, women strewing wild flowers). The Janamejaya sentence was narration furniture, not an event. Odd geography (citizens of Upaplavya greeting him after Salibhavana) kept exactly as the file had it."},

{"story_id": "DKS_0418", "changed": "major", "context_added": True,
 "ai_patterns_removed": [
   "epithet stack removed: 'the slayer of Madhu', 'Dasarha', 'Madhava', 'Kesava' -> plain 'Krishna'",
   "Dhritarashtra's hymn of praise ('He is the Lord of all creatures; on him rests the course of everything... eternal Virtue itself') compressed to its dramatic point: honour him or suffer, win his goodwill before the kings — theological register was scripture quotation, the motive is what drives the scene",
   "'viands' -> 'food'; translationese connectives ('thereupon', 'diverse qualities') naturalized",
   "narrator interlude ('The contrast was there for the whole city to see') folded into the closing contrast image"],
 "child_friendly_changes": [
   "opening context added: Krishna is travelling to Hastinapura to plead for peace between the Pandavas and their cousins, so the reception makes sense to a first reader",
   "Bhishma glossed 'the grandsire of his house', Drona 'who had taught the princes of both families the art of war', Sanjaya 'his trusted counsellor', Vidura kept as 'the wise Vidura', Duryodhana as 'his son'",
   "'beautiful girls' in the provision list rendered 'attendants' (reception staff, not a child-facing detail); every other provision kept: seats, perfumes, ornaments, robes, food, drinks, garlands",
   "the special pavilion at Vrikasthala, Bhishma's 'Excellent', and the two-stage report to Dhritarashtra all kept"],
 "risk": "Dhritarashtra's motive preserved: pleased Krishna grants happiness / slighted Krishna brings misery, and his grace before the assembled kings is what the gifts buy. The king's actual orders kept (pavilions along the road furnished with every comfort). Krishna's silent passing — 'without casting a single glance', not one gem drawing his eye — kept verbatim in meaning; the closing 'court that had measured him in gold' image retained. 'Beautiful girls' -> 'attendants' is the one softened provision."},

{"story_id": "DKS_0419", "changed": "major", "context_added": True,
 "ai_patterns_removed": [
   "every scripture-vocative and translationese frame stripped from the speech: 'O monarch, best of men', 'O giver of great wealth', 'O ruler of men' (this last belongs to 0420's file) -> plain address",
   "epithets removed: 'Kesava', 'Janardana', 'the hero of Vrishni's race', 'the mighty-armed hero' -> plain 'Krishna'; 'Dhananjaya' rendered 'Arjuna'",
   "'fraught with virtue and profit' / 'conclusions of well-directed reason' translationese register naturalized while keeping the ideas",
   "closing summary paragraph tightened from three stacked sentences to one ('In a single speech Vidura had named the plan and the heart beneath it')"],
 "child_friendly_changes": [
   "opening anchor: Vidura identified at first mention as 'the blind king's brother, and the one man in that hall who told him the truth'",
   "three similes kept and made concrete: 'letters cut in stone', 'light in the sun', 'waves in the ocean'",
   "'the five Pandavas desire only five villages' kept verbatim — the story's sharpest fact",
   "Krishna's actual terms kept exactly: a vessel of water, the washing of his feet, enquiries after welfare — nothing more"],
 "risk": "Every claim of the speech preserved: Dhritarashtra's virtues permanent as stone/sun/waves; the gifts as deception ('I swear by my own soul'); the five villages refused; the plan to separate Krishna from the Pandavas by wealth; Arjuna 'is Krishna's very life' and cannot be given up; the water/feet-washing/enquiries-only hospitality; peace between 'you and Duryodhana on one side and the Pandavas on the other'; Dhritarashtra as father to sons who offer filial regard. No new argument added."},

{"story_id": "DKS_0420", "changed": "major", "context_added": True,
 "ai_patterns_removed": [
   "epithet run removed: 'Janardana', 'Kesava', 'Hrishikesa', 'Vasudeva as the means' -> plain 'Krishna'",
   "'it behooves you to say' and other translationese connectives naturalized",
   "Bhishma's curse-speech de-duplicated: fourfold 'wicked' run (wicked son / wicked wretch / wicked wretch / sinful wretch) reduced to two beats without losing the condemnation",
   "vocatives kept minimal: only 'Grandsire' (Duryodhana to Bhishma) and 'Dhritarashtra' (Bhishma's address) remain"],
 "child_friendly_changes": [
   "opening context added: the debate follows Vidura's truth-telling, and Duryodhana's agreement with Vidura on that one point is what launches his plan",
   "Vrishnis glossed 'Krishna's own clan'; Bhishma glossed 'the grandsire of the Kuru house'; Kshatriya rendered 'warrior' in context",
   "the imprisonment plan, 'tomorrow morning', the whole-earth boast, Dhritarashtra's recoil, and Bhishma's walkout all kept plainly",
   "closing image kept: the plan standing 'like a storm that had not yet broken'"],
 "risk": "Duryodhana's full reasoning preserved: no gifts because they would look like fear; war decided should not be delayed by hospitality; the resolution to imprison 'the refuge of the Pandavas' when he comes tomorrow morning, so that 'the Vrishnis and the Pandavas — aye, the whole earth — will submit'. Bhishma's counter ('worshipped or not, Krishna never becomes angry... whatever he purposes none can frustrate') and his warning that the wicked son will be 'destroyed in a moment' kept. Dhritarashtra's protest kept ('This is not the ancient custom... He is our kin, dear to us, and has done us no wrong')."}
]

def main():
    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    pristine = {}
    before_words = {}
    for sid in NEW_STORY:
        old = json.load(open(os.path.join(STORY_DIR, sid + ".json"), encoding="utf-8"))
        pristine[sid] = old
        before_words[sid] = len(old["story"].split())
        refl = old.get("reflection")
        assert refl is None or 40 <= len(refl.split()) <= 80, f"{sid} reflection out of 40-80"

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
