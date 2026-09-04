#!/usr/bin/env python3
# Style normalization pass v1 - n071 (DKS_0421..DKS_0426), peace_mission arc
import json, os

BASE = '/Users/dev_env/Documents/projects/indian_apps/dailyX/daily_krishna_stories'

NEW = {}

NEW['DKS_0421'] = '''Word of Krishna's coming had travelled ahead of him, and Hastinapura made ready as though for its greatest festival. The main streets were hung with jewels and gems, and no man, woman or child stayed indoors, so eager was everyone to see the visitor who had ridden so far on an errand of peace.

His errand touched every family in the city. Krishna had come to plead with the sons of the blind king Dhritarashtra, who held the Kuru kingdom, for his cousins, the five Pandava brothers, who had been cheated out of that kingdom and driven into the forest.

The welcome began before he reached the gates. All of Dhritarashtra's sons except Duryodhana had ridden out to meet him in their finest robes, and with them came Bhishma, the revered elder of the Kuru house, Drona and Kripa, the teachers of the princes, and the other elders of the court. Behind them the people followed by the thousand, some in chariots and fine carriages, most on foot.

Krishna had risen before dawn, said his morning prayers, and taken leave of his cousins at their camp; and all along the road the townspeople had come out to see him pass. At Vrikasthala they pressed about his chariot so thickly that only when he was gone did they turn back to their homes. Soon after, Bhishma and Drona and the sons of Dhritarashtra met him on the open road, and he entered the city in the midst of them all.

The citizens lined the streets and bent their heads to the ground, singing his praise as he passed. Ladies leaned from the windows of the great houses, crowding so thickly that the tall mansions seemed ready to bend beneath their weight. And though Krishna's horses were among the swiftest in the world, they could barely move through that dense river of people.

At last he came to the palace of the blind king and passed through three outer halls into the chamber where Dhritarashtra sat. The king, who could not see his guest, rose to his feet as Krishna entered, and with him rose Bhishma, Drona, Kripa, Somadatta and king Vahlika, for all of them stood to honour him. Krishna bowed first to the king and to Bhishma, greeted the other elders in the order of their years, and spoke warmly to Drona and his son, to Vahlika, Kripa and Somadatta.

In the centre of the chamber stood a wide golden seat set with jewels. At the king's request Krishna took it, and the priests brought the offerings of a royal welcome — a cow, honey, curds and water — and performed the rites with care. Krishna stayed a while among the Kurus, laughing and jesting with each as age and closeness allowed, while the blind king who had risen for him sat honoured and glad. When he had taken his leave, Krishna greeted the assembled court and went on to the house of Vidura — the king's younger brother, and the truest friend the exiled Pandavas had in Hastinapura.

Vidura received him with every good thing his house could offer. What use, he asked, in trying to put into words the joy he felt at this coming? Then he asked the question that had been on his heart all day: how did the Pandavas fare? And Krishna, who knew how dearly Vidura loved his nephews, told him everything — how they lived in the forest, how they bore their exile, what they hoped.

So the day that had begun with a city pouring into the streets to honour one man ended quietly, in Vidura's house, with Krishna speaking freely of his cousins. The plea for peace that had brought him to Hastinapura was still waiting to be spoken aloud.'''

NEW['DKS_0422'] = '''That afternoon Krishna went to the house of his aunt Kunti — the mother of the five Pandava brothers, who were living in the forest while their cousins held the kingdom. Krishna had come straight from her sons, and she had been waiting for him since word of his arrival reached her.

When he stood at her door, she could not hold back. She threw her arms around his neck and wept, remembering her sons, and the tears she had held back for months came freely at the sight of him. Only after Krishna had received the rites of hospitality and taken his seat did she speak, her face drawn, her voice choked with tears.

Her sons, she said, had been gentle children. From their earliest years they had waited with reverence on their elders, held together in friendship, mastered both their anger and their joy, and spoken only the truth. Robbed of their kingdom by trickery, they had gone quietly into the forest, though they deserved to live among friends and servants. "They left their old mother behind," she wept, "and went into the woods. How do they live now, in that deep forest full of lions and tigers and elephants?"

They had lost their father as small children, and she had raised them alone. At home they slept in high rooms on soft blankets and deerskin, and woke each morning to the grunt of elephants and the neighing of horses, the clatter of chariot wheels, the music of conches and cymbals, the singing of women and the praise-songs of the bards, with the blessings of priests at dawn. How could sons who woke to such music sleep now in a wilderness that rang with the howls of beasts? The thought was more than she could bear.

Then, one by one, she asked after them, as though the telling might bring them nearer. How was Yudhishthira, her eldest — gentle, golden-skinned, the most learned of the Kurus, bearing without complaint the weight of a kingdom he could not use? How was Bhima, strong as ten thousand elephants and swift as the wind, who had slain the demons Hidimva and Vaka, who fed on men, and the warrior Kichaka besides — terrible in anger, yet quick to obey his elder brother? How was Arjuna, who could loose five hundred arrows in a single stretch, the finest bowman of his age, whose skill men compared to the fabled king Kartavirya's?

Krishna answered her gently. "What woman in the world is like you?" he asked. "You have borne both happiness and sorrow with a patience few can match; bear this waiting too. Your sons are well, and they send you their love through me. The time is coming — sooner than you think — when you will see them again as lords of the whole world, their foe slain and their fortunes restored."

The words were spoken softly, but Kunti knew the man who spoke them. She let her tears fall at last, a little lighter for being spent, for her sons were alive and well, and someone who loved them had come to speak for them.'''

NEW['DKS_0423'] = '''From his aunt Kunti's house, Krishna went to the palace of Duryodhana — the eldest of the blind king's hundred sons, and the prince who now held the kingdom his cousins had lost. Everyone in Hastinapura knew why Krishna had come, and Duryodhana meant to receive him as an honoured guest before a single word of peace could be spoken.

The palace was furnished with great wealth, its halls set with beautiful seats, fit, men said, for the king of the gods himself. Krishna crossed three wide courtyards, unhindered by the waiting servants, and entered the great hall — high as a hill, bright as a summer cloud. There, in the midst of a thousand kings and surrounded by the whole Kuru court, sat Duryodhana on his throne, his brother Dussasana at his side, and with them Karna, the great archer who had sworn his friendship to Duryodhana, and Sakuni, the uncle who had cheated the Pandavas out of their kingdom at dice.

At Krishna's entry, Duryodhana rose, and his counsellors rose with him. Krishna greeted the sons of Dhritarashtra, the counsellors, and every king present, each according to his age, and took the golden throne that had been set for him, its seat covered with a carpet embroidered in gold. The king offered him a cow, honey, curds and water, and placed at his service palaces, mansions and the whole kingdom. The Kauravas and the assembled kings honoured him as he sat there.

Then, the worship over, Duryodhana invited Krishna to eat at his house. Krishna did not accept.

The king pressed him, his voice gentle with something else moving behind it, his eyes on Karna as he spoke. Why would Krishna not accept the feast prepared for him — the fine foods and drinks, the robes and beds kept ready? He had promised his help to both sides and wished both parties well; he was of Dhritarashtra's own kin, and the old king loved him. "Tell me the true reason for this refusal," Duryodhana said.

Krishna raised his right arm and answered in a voice deep as thunder, calm and clear: "An envoy, O king, eats and accepts gifts only when his mission has succeeded. When my work here is done, you may feast me and my companions."

Duryodhana answered that such words ill became Krishna. Whether the mission succeeded or failed, the feast was offered out of kinship, and there was no quarrel between them, no war.

But Krishna had not finished. "Not from pride, not from anger, not from malice, nor for any gain would I turn aside from what is right," he said. "A man eats another's food when he is in need — or when love moves him to it. I am in no need, and you have shown me no love. From the day they were born, you have hated your own cousins, the gentle Pandavas, who never did you harm and who hold fast to virtue. Who can injure such men? He who hates them hates me, and he who loves them loves me. Know this: the Pandavas and I have but one soul between us. The food of a house that hates my very self could not pass my lips. I will eat at the house of Vidura, where the food is offered in love."

In a hall prepared for a thousand kings, Krishna had chosen the simple table of Vidura's house — the one table in Hastinapura where he could eat without denying his own words. The refusal was not discourtesy. The friend of the Pandavas would not sit down to the feast of the man who had spent his life hating them.'''

NEW['DKS_0424'] = '''At nightfall Krishna ate at the house of Vidura, as he had promised in Duryodhana's hall. Vidura was the blind king's younger brother, and the one man in that palace whom the exiled Pandavas could call a true friend. When the meal was over and the house had grown quiet, the meaning of Krishna's choice came clear, and the man who had welcomed him with joy now spoke with dread. Krishna had come to Hastinapura to plead for his cousins, and Vidura meant to tell him, before he went to the court, exactly what waited there.

"Your coming here was not well judged, Krishna," Vidura said. "Dhritarashtra's son obeys neither the laws of kingship nor the laws of goodness. He is wicked and quick to anger; he craves honour while he insults others; he turns from the counsel of the aged. He thinks himself wise, but he is a fool — a slave to his desires, ungrateful, suspicious of his truest friends, in love with what he knows to be wrong. Were you yourself to point out his true good, he would cast it aside out of pride and rage. He believes that Bhishma, Drona and Kripa, that Karna, Drona's son and king Jayadratha can win him anything he wants — and so he has never once set his heart on peace."

Krishna listened, and Vidura went on. Duryodhana and his brothers, with Karna at their head, truly believed that the Pandavas could not even look upon Bhishma and Drona, let alone fight them. The short-sighted prince, with his great army assembled, already counted his purpose achieved; he had decided that Karna alone could defeat his enemies. So he would never make peace. Krishna might desire peace and brotherhood between the two houses, but Dhritarashtra's sons had resolved to give the Pandavas nothing that was theirs. "Among men so resolved," Vidura said, "your words will be wasted — like a song sung to the deaf."

Nor did Vidura think Krishna should enter that assembly at all. The Kauravas had gathered a mighty force and feared no one; they truly believed that Indra at the head of all the gods could not overcome them. Duryodhana sat in the midst of his elephants, his chariots and his heroes and counted the whole earth already his; what he held, he would never give back. "Alas," Vidura said, "for Duryodhana's sake the destruction of the earth is at hand." All the kings of the earth had chosen their side and were eager to fight the Pandavas; many were old enemies of Krishna, and all, fearing him, had bound themselves to Karna and the sons of Dhritarashtra. They had their suspicions of Krishna himself. "It does not seem right to me," Vidura said, "that you should walk into the midst of them."

The night was still. Krishna had heard every word — the long tale of Duryodhana's faults, the certainty of war, the plea that he turn back. He did not argue with any of it. Vidura knew this court as no one else did, and Krishna had not come to Hastinapura to be persuaded out of listening.'''

NEW['DKS_0425'] = '''The city of Hastinapura slept, and the lamps in Vidura's house burned low. Krishna and Vidura — the blind king's brother, the wisest man in the Kuru court — still sat talking. Krishna had come to plead for peace between Dhritarashtra's sons and his cousins the Pandavas, and Vidura had just told him plainly what waited: Duryodhana's wickedness, and the enmity of every warrior king who had chosen his side.

Krishna listened to it all without surprise. Then he answered, and his answer was not a defence of his plan but a statement of why he had come at all.

"Everything you have said is true, Vidura," he said. "You have spoken to me as a father and mother speak, and your words are worthy of you — consistent with virtue, with good sense, and with truth. But hear the reason for my coming. I know well the wickedness of Dhritarashtra's son, and the enmity of the kings who stand with him — and still I have come. Great is the merit of him who frees the whole earth from the meshes of death: this earth, with its elephants, its chariots and its horses, already overshadowed by a dreadful calamity."

He spoke of merit as a man speaks of something he has weighed. If a man strives with all his might to do a good deed and fails, Krishna said, the merit of the striving is still his. And if a man only plans an evil deed in his heart but never does it, the evil can never touch him. The scales of the world are not read by outcomes alone.

"I will strive sincerely, Vidura, to bring about peace between the Kurus and the Srinjayas — between Dhritarashtra's sons and the Pandavas with the allies who would fight beside them — who are about to slaughter one another. That calamity hangs over them all because of the Kurus' own conduct; it is the doing of Duryodhana and Karna, and the other kings only follow where those two lead. The wise call a man a wretch who will not lift a hand to save a friend sinking in misfortune. Striving with all his might — even seizing his friend by the hair, if he must — one should hold him back from a wrongful act. He who does so wins praise, not blame."

So Krishna had come: not because he expected the court to listen, but because when kinsmen fall out, a true friend speaks between them. If Duryodhana judged him wrongly, he would still have his own conscience. He had come so that no one could ever say that Krishna, though able to help, had made no attempt to stop the two houses from destroying one another; and having striven for peace, he would stand free of blame before all the kings.

"If the foolish Duryodhana will not accept my words, he will only be inviting his own fate," Krishna went on. "But if I can bring peace to the Kurus without sacrificing the interests of the Pandavas, my conduct will be highly meritorious, and the Kauravas themselves will be saved from the meshes of death. If Dhritarashtra's sons reflect coolly on what I shall say — words full of wisdom and consistent with righteousness — then peace will be made, and they will honour me as its author."

Then, with the calm of a man who had settled a long argument in his own heart, he added what Vidura was meant to carry back into the night. "But if they seek to injure me, know this: all the kings of the earth united are no match for me — like a herd of deer before an enraged lion."

There was nothing more to say. The lamps flickered, the city slept on, and Krishna lay down for the night. Whatever the morning brought, he would meet it having done the one thing within his power: he had come, and he would speak.

Vidura stayed wakeful long after, weighing the man who had come to plead for peace and, in the same breath, had told him he could not be harmed if the plea was refused. Between those two truths lay everything that was about to happen to the world.'''

NEW['DKS_0426'] = '''Before the sun was fully up, the sound of conches and cymbals drifted into Vidura's house, where Krishna had spent the night in talk. A band of singers and bards with sweet voices had gathered at the door to wake him with music; and Hastinapura, which had slept through the darkest hours, stirred with the first news that the messenger of peace was awake.

Krishna rose and performed the rites of morning — the cleansing bath, his prayers, offerings of melted butter poured on the sacred fire. He dressed and began his worship of the rising sun; and while he was still at his devotions, Duryodhana and Sakuni, the uncle who had cheated the Pandavas at dice, came to him.

"The king is seated in his court," they said, "with all the Kurus led by Bhishma, and with all the kings of the earth. They are all asking for you, as the gods in heaven ask for their king Indra."

Krishna greeted them both courteously; and when the sun had climbed a little higher, he summoned a number of learned priests and made them presents of gold, robes, cows and horses. Then his charioteer Daruka came and saluted him, and soon returned with his master's chariot — a great shining car hung with rows of tinkling bells, drawn by swift horses, its wheels rumbling like distant thunder.

Krishna walked around the sacred fire and the band of priests, put on the jewel called Kaustubha, and mounted the chariot, surrounded by the Kurus and guarded by his own Vrishni kinsmen. Vidura followed in his own chariot; Duryodhana and Sakuni shared one; and Satyaki and Kritavarman, the boldest warriors of Krishna's clan, rode behind with the rest, on chariots, on horses and on elephants.

They came out onto a broad street that had been swept and watered for the occasion. Cymbals clashed, conches were blown, and every other instrument poured out its music. Young warriors, the pride of Krishna's line, surrounded the chariot; thousands of soldiers in bright dress, bearing swords, lances and axes, marched before it; five hundred elephants followed, and chariots beyond counting. All the citizens of Hastinapura, young and old, men and women, had come into the streets to see him; terraces and balconies were crowded with ladies, and every window held a face. Honoured by the Kurus, answering the greetings of all as each deserved, Krishna moved slowly down the street, his eyes on everyone.

At last he reached the Kuru court, and his attendants blew their conches and trumpets until the sky rang with the sound. The whole assembly of kings trembled with delight at the thought of seeing him; and when they heard the rumble of his chariot, like the roll of rain-heavy clouds, the kings rose, their joy so deep that the hair of their bodies stood on end.

At the gate Krishna alighted from his chariot and entered the great hall — bright with gold, high as a bank of summer cloud. He walked in with Vidura on one side and Satyaki on the other, and beside him even the splendour of the hall seemed to dim. The kings made way for him; the sages who had come to the assembly were given their seats; and Krishna, the guest the whole city had poured into the streets to see, took his place in the midst of the court.

There he sat, the calm centre of a hall that had dressed itself in all its glory to receive him — a glory that seemed, in that moment, borrowed from his presence rather than lent to it.'''

changed_levels = {'DKS_0421': 'major', 'DKS_0422': 'major', 'DKS_0423': 'major',
                  'DKS_0424': 'major', 'DKS_0425': 'minor', 'DKS_0426': 'minor'}

report = [
 dict(story_id='DKS_0421', changed='major', context_added=True,
  ai_patterns_removed=["scripture-translation diction stripped ('endued with great speed', 'of spotless deed', 'mighty one of long arms', 'royal son of Vichitravirya', 'accosted')",
   "unglossed group names resolved: 'the Dhartarashtras' -> Dhritarashtra's sons (Duryodhana named as the missing one), 'the Bharatas' -> the Pandavas at their camp",
   "disjointed day-dawn flashback (para 2) untangled into a straight chronology: dawn rites -> farewell at the Pandavas' camp -> road towns -> meeting the court party outside the gates",
   "'worshipped him' ritual language kept once but grounded as the royal welcome offerings"],
  child_friendly_changes=["opening context added: who the Pandavas are, why Krishna has come (peace mission after the kingdom was taken by trickery)",
   "Bhishma glossed as revered elder of the Kuru house; Drona and Kripa as the princes' teachers; Vidura as the blind king's younger brother and the Pandavas' truest friend",
   "Dhritarashtra identified as the blind king whose sons hold the kingdom; the risen-to-honour beat kept human ('the king, who could not see his guest, rose')",
   "'cars' -> 'chariots and fine carriages'"],
  risk="Greeting order preserved (king and Bhishma first, then elders by years, then Drona and his son, Vahlika, Kripa, Somadatta). Cow/honey/curds/water rite kept as the royal welcome. 'Left the Bharatas' rendered as 'taken leave of his cousins at their camp' — the source's Bharatas here are the Pandavas he set out from."),
 dict(story_id='DKS_0422', changed='major', context_added=True,
  ai_patterns_removed=["ornate opener removed ('countenance beaming like the radiant sun', 'woe-begone'); Kunti's alias 'Pritha' and Krishna's epithets 'Govinda of the Vrishni race' dropped in favour of plain names",
   "per-son epic comparison piles condensed to one clear trait each (gold complexion/learning; elephant strength; five-hundred arrows)",
   "palace-waking catalogue (Runku deer, songstresses, professional reciters) simplified while keeping the music-against-beasts contrast intact",
   "'plucking the very roots of her heart' overwrought metaphor removed"],
  child_friendly_changes=["context added: Kunti is Krishna's aunt and mother of the exiled Pandavas, and Krishna has come straight from her sons",
   "each brother introduced with one memorable trait so a first reader can tell them apart",
   "Hidimva and Vaka glossed as demons who fed on men; Kichaka kept as 'the warrior Kichaka'",
   "three-worlds/monarch hyperbole trimmed to 'lords of the whole world'"],
  risk="Every deed named in Kunti's questions kept (Yudhishthira's patience and learning, Bhima's strength plus Hidimva/Vaka/Kichaka, Arjuna's five hundred arrows and the Kartavirya comparison as 'fabled king Kartavirya'). Krishna's consolation kept near-verbatim: 'What woman in the world is like you?... their foe slain and their fortunes restored.'"),
 dict(story_id='DKS_0423', changed='major', context_added=True,
  ai_patterns_removed=["scripture diction ('like unto the abode of Indra', 'viands', 'Janardana', 'O Bharata', 'resembling the sun itself in splendour') removed",
   "'in a gentle voice with deception lurking behind his words' narration compressed to 'his voice gentle with something else moving behind it'",
   "third-person summary of the refusal debate rebuilt as direct, natural dialogue with the envoy logic kept verbatim",
   "double 'blazing' palace hyperbole reduced to one image"],
  child_friendly_changes=["context added: who Duryodhana is (eldest of the blind king's hundred sons, holder of the kingdom his cousins lost) and why Krishna is in the city",
   "Dussasana named as Duryodhana's brother; Karna glossed as the great archer sworn to Duryodhana; Sakuni as the uncle who cheated the Pandavas at dice",
   "the 'common soul' doctrine kept but delivered as Krishna's own quoted words, plainly stated",
   "Kunti referred to as Krishna's aunt (source's 'Pritha' removed)"],
  risk="Krishna's refusal speech kept whole in substance and partly verbatim: envoys eat only after success; no need and no love; hatred of the Pandavas from their birth; 'He who hates them hates me, and he who loves them loves me'; 'the Pandavas and I have but one soul between us'; he will eat Vidura's food. 'He had granted aid to both sides' retained as Duryodhana's own argument."),
 dict(story_id='DKS_0424', changed='major', context_added=True,
  ai_patterns_removed=["one-paragraph vice-catalog (twenty-plus charges in a single sentence chain) split into a readable indictment and condensed to the essential charges",
   "double simile (singer before the deaf / Brahmana before Chandalas) kept once as 'a song sung to the deaf'; the caste simile dropped as redundant and child-opaque",
   "epithet runs and 'Kesava' -> Krishna",
   "'endued with these and many other vices' filler close removed"],
  child_friendly_changes=["Vidura glossed at once (blind king's younger brother, the Pandavas' true friend); Krishna's mission stated in one clause so the story stands alone",
   "the roster of champions Duryodhana trusts kept whole (Bhishma, Drona, Kripa, Karna, Drona's son, king Jayadratha) as a plain list",
   "'short-sighted prince' kept; 'fate' motif kept but spoken plainly ('the destruction of the earth is at hand')",
   "army/elements/heroes claim ('Indra and all the gods could not defeat them') kept as Vidura's report of their belief"],
  risk="Condensation is faithful: every named vice survives in some form; 'great faith in Bhishma and Drona and Kripa and Karna and Drona's son and Jayadratha' kept intact; the kings' fear-driven alliance with Karna and the suspicions of Krishna himself preserved; Vidura's counsel not to enter the assembly is the story's last word before the quiet close."),
 dict(story_id='DKS_0425', changed='minor', context_added=False,
  ai_patterns_removed=["epithet 'Krishna, the delighter of the Yadavas' removed",
   "narrator paraphrase after Krishna's first speech condensed (the 'so it was that Krishna had come' passage tightened from four sentences to three)",
   "wordiness trimmed: 781 -> in range without cutting any speech",
   "'defense' US spelling normalized to 'defence'"],
  child_friendly_changes=["'hostility of every Kshatriya' glossed in context as 'every warrior king who had chosen his side'",
   "'Kurus and the Srinjayas' glossed inline as Dhritarashtra's sons vs the Pandavas with their allies",
   "Vidura re-identified briefly (blind king's brother, wisest in the court) so the story reads alone"],
  risk="All quoted speech preserved near-verbatim: father-and-mother praise; merit of failed striving; the wretch who will not save a friend ('even seizing his friend by the hair'); Duryodhana-and-Karna as the origin of the calamity; the deer-before-the-lion warning. Only glosses and trims around the quotes."),
 dict(story_id='DKS_0426', changed='minor', context_added=False,
  ai_patterns_removed=["scattered epithets (Kesava, Sauri, Janardana) all resolved to Krishna",
   "archaic diction: 'kine' -> cows, 'car' -> chariot throughout, 'celestials desiring Indra' simile lightened",
   "unglossed walk-ons identified: Daruka (charioteer), Satyaki and Kritavarman (kinsmen/warriors), Sakuni (uncle who cheated at dice), Kaustubha (a jewel), Vrishnis (his clan)",
   "balcony-crowd image varied so it does not repeat 0421's 'mansions about to fall'",
   "'conversant with every precept of religion' -> plain 'Vidura followed in his own chariot'"],
  child_friendly_changes=["morning rites explained in plain words (bath, prayers, offerings of melted butter on the fire)",
   "Brahmanas -> 'learned priests'; Rishis -> 'the sages'; Kaustubha described as 'the jewel called Kaustubha'",
   "Kailasa/abode-of-Indra comparisons grounded to 'high as a bank of summer cloud' and 'fit for the king of the gods'",
   "chariot described concretely (tinkling bells, swift horses, rumbling wheels)"],
  risk="Procession order preserved exactly: Krishna's chariot surrounded by Kurus and guarded by Vrishnis; Vidura on his own chariot; Duryodhana and Sakuni on one; Satyaki, Kritavarman and the rest behind on chariots, horses and elephants. Five hundred elephants, chariots by thousands, swept street, gifts to the priests, Kaustubha, and the hair-standing joy of the kings all kept."),
]

# --- apply ---
counts = {}
originals = {}
for sid, new_story in NEW.items():
    path = os.path.join(BASE, 'data/stories', sid + '.json')
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    originals[sid] = data
    before = len(data['story'].split())
    data['story'] = new_story
    data['generation_metadata']['style_normalization'] = {
        'pass': 'v1', 'model': 'deepseek-v4-flash', 'changed': changed_levels[sid]}
    out = json.dumps(data, indent=1, ensure_ascii=False) + '\n'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(out)
    after = len(new_story.split())
    counts[sid] = (before, after)
    print(sid, 'before:', before, 'after:', after, 'changed:', changed_levels[sid])

# --- verify: only story + style_normalization may differ ---
print('\n--- verification ---')
ok = True
for sid, orig in originals.items():
    path = os.path.join(BASE, 'data/stories', sid + '.json')
    new = json.load(open(path, encoding='utf-8'))
    problems = []
    for k, v in orig.items():
        if k == 'story':
            continue
        if k == 'generation_metadata':
            for mk, mv in v.items():
                if mk == 'style_normalization':
                    continue
                if new['generation_metadata'].get(mk) != mv:
                    problems.append(f'generation_metadata.{mk}')
            continue
        if new.get(k) != v:
            problems.append(k)
    if problems:
        ok = False
        print(sid, 'DIFFERS IN:', problems)
    else:
        print(sid, 'clean (story + style_normalization only)')
    assert new['reflection'] == orig['reflection'], sid + ' reflection changed!'
print('ALL CLEAN' if ok else 'PROBLEMS FOUND')

# --- report ---
rep_path = os.path.join(BASE, 'data/mining/style_report', 'n071.jsonl')
os.makedirs(os.path.dirname(rep_path), exist_ok=True)
with open(rep_path, 'w', encoding='utf-8') as f:
    for r in report:
        sid = r['story_id']
        r['length_before'], r['length_after'] = counts[sid]
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
print('\nreport written:', rep_path, 'lines:', len(report))
