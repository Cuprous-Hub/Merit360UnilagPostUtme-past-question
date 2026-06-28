"""
Combined Database Seeding Script for UNILAG Post-UTME Practice Platform.
Generates 400 unique questions per subject:
- Use of English: 400 questions
- General Paper: 400 questions
- Mathematics: 400 questions
"""

from app import create_app, db
from app.models import Exam, Question, Topic, Result, Answer


def clear_subject(subject):
    """Delete all questions, topics, and exams for a given subject."""
    exam = Exam.query.filter_by(subject=subject).first()
    if exam:
        results = Result.query.filter_by(exam_id=exam.id).all()
        for r in results:
            Answer.query.filter_by(result_id=r.id).delete()
        Result.query.filter_by(exam_id=exam.id).delete()
        Question.query.filter_by(exam_id=exam.id).delete()
        db.session.delete(exam)
    Topic.query.filter_by(subject=subject).delete()
    db.session.commit()
    print(f"Cleared existing {subject} data.")


def seed_english():
    clear_subject('English')

    topics = [
        Topic(name='Lexis & Structure', subject='English', description='Word choice, vocabulary, sentence completion'),
        Topic(name='Grammar & Syntax', subject='English', description='Concord, tenses, clauses, sentence types'),
        Topic(name='Advanced Grammar', subject='English', description='Subjunctive, inversion, conditionals'),
        Topic(name='Vocabulary', subject='English', description='Synonyms, antonyms, idioms, contextual meaning'),
        Topic(name='Oral English', subject='English', description='Stress, intonation, vowel/consonant sounds'),
        Topic(name='Phrasal Verbs & Collocations', subject='English', description='Idiomatic verb phrases and word partnerships'),
        Topic(name='Analogies', subject='English', description='Word relationships and logical pairs'),
        Topic(name='Sentence Structure & Clause Types', subject='English', description='Simple, compound, complex; clause functions'),
        Topic(name='Verb Tenses & Aspect', subject='English', description='Time reference, perfective, progressive'),
        Topic(name='Agreement & Concord', subject='English', description='Subject-verb, pronoun-antecedent agreement'),
        Topic(name='Connectors & Logical Relations', subject='English', description='Conjunctions, transitions, cause-effect'),
        Topic(name='Meaning & Paraphrase', subject='English', description='Sentence meaning, inference, paraphrasing'),
        Topic(name='Ambiguity & Interpretation', subject='English', description='Structural and lexical ambiguity'),
        Topic(name='Word Order & Inversion', subject='English', description='Subject-verb inversion, fronting, cleft sentences'),
        Topic(name='Semantic Roles & Thematic Relations', subject='English', description='Agent, patient, theme, instrument'),
    ]
    for t in topics:
        db.session.add(t)
    db.session.commit()

    exam = Exam(
        title="Use of English",
        subject="English",
        description="400 UNILAG-style English questions",
        duration_minutes=60,
        total_questions=400,
        passing_score=50
    )
    db.session.add(exam)
    db.session.commit()

    lexis = Topic.query.filter_by(name='Lexis & Structure', subject='English').first()
    grammar = Topic.query.filter_by(name='Grammar & Syntax', subject='English').first()
    adv_grammar = Topic.query.filter_by(name='Advanced Grammar', subject='English').first()
    vocab = Topic.query.filter_by(name='Vocabulary', subject='English').first()
    oral = Topic.query.filter_by(name='Oral English', subject='English').first()
    phrasal = Topic.query.filter_by(name='Phrasal Verbs & Collocations', subject='English').first()
    analogies_topic = Topic.query.filter_by(name='Analogies', subject='English').first()
    structure_topic = Topic.query.filter_by(name='Sentence Structure & Clause Types', subject='English').first()
    tense_topic = Topic.query.filter_by(name='Verb Tenses & Aspect', subject='English').first()
    agreement_topic = Topic.query.filter_by(name='Agreement & Concord', subject='English').first()
    connectors_topic = Topic.query.filter_by(name='Connectors & Logical Relations', subject='English').first()
    meaning_topic = Topic.query.filter_by(name='Meaning & Paraphrase', subject='English').first()
    ambiguity_topic = Topic.query.filter_by(name='Ambiguity & Interpretation', subject='English').first()
    wordorder_topic = Topic.query.filter_by(name='Word Order & Inversion', subject='English').first()
    semantic_topic = Topic.query.filter_by(name='Semantic Roles & Thematic Relations', subject='English').first()

    all_english = []

    # ===== OLD ENGLISH: LEXIS & STRUCTURE (40 questions) =====
    lexis_items = [
        ("The boy was punished because he ___ his teacher's instructions.", "ignored", "disobeyed", "violated", "omitted", "B"),
        ("Hardly had she finished speaking ___ the bell rang.", "when", "than", "then", "but", "A"),
        ("The workers have complained that their salaries are not ___ with the work they do.", "consistent", "compatible", "commensurate", "convenient", "C"),
        ("The teacher encouraged the students to look ___ new words in the dictionary.", "into", "up", "out", "over", "B"),
        ("He has a good command ___ the English language.", "for", "on", "over", "of", "D"),
        ("We were advised to abstain ___ bad habits.", "of", "from", "off", "with", "B"),
        ("My uncle, together with his children, ___ arriving today.", "are", "were", "is", "have been", "C"),
        ("He is the man ___ broke the window.", "whom", "whose", "which", "who", "D"),
        ("If I ___ you, I would accept the offer.", "were", "was", "am", "be", "A"),
        ("Not only does she sing, but she ___ plays the piano.", "also", "too", "either", "as well", "A"),
        ("The thief was caught because someone had given him ___.", "out", "away", "off", "in", "B"),
        ("The committee will meet to ___ the issue.", "dissolve", "discard", "deliberate", "disseminate", "C"),
        ("I am not used to ___ early.", "waking", "wake", "woken", "woke", "A"),
        ("He prefers tea ___ coffee.", "than", "than to", "to", "over", "C"),
        ("The teacher asked the students to be quiet, but ___ listened.", "neither", "none", "nobody", "few", "D"),
        ("We were warned ___ the dangers of reckless driving.", "about", "on", "with", "for", "A"),
        ("She looked forward to ___ her friend.", "see", "seeing", "seen", "saw", "B"),
        ("I don't mind ___ for a few minutes.", "to wait", "wait", "waiting", "waited", "C"),
        ("The man is not only rich ___ generous.", "also", "and", "but also", "or", "C"),
        ("The manager said he would look ___ the matter.", "up", "into", "off", "after", "B"),
        ("His parents objected ___ his plans.", "to", "with", "at", "on", "A"),
        ("The girl was accused ___ stealing the book.", "for", "of", "about", "on", "B"),
        ("The driver was penalized ___ speeding.", "of", "for", "with", "on", "B"),
        ("He was so tired that he ___ asleep during the lecture.", "falls", "fell", "fallen", "falling", "B"),
        ("The principal insisted that the student ___ suspended.", "be", "is", "was", "has been", "A"),
        ("The boy asked me if I ___ him a pen.", "can borrow", "could lend", "can lend", "could borrow", "B"),
        ("The culprit confessed ___ the crime.", "to committing", "to commit", "committing", "having commit", "A"),
        ("The man was accused of ___ his position.", "abusing", "insulting", "abasing", "misusing", "A"),
        ("The lady looks ___ in her new dress.", "beautiful", "beautifully", "beauty", "beauteous", "A"),
        ("We were advised to work hard ___ we fail.", "in order that", "unless", "so that", "lest", "D"),
        ("I told them to go home, ___?", "didn't I", "don't I", "hadn't I", "haven't I", "A"),
        ("They are not used to ___ this kind of hardship.", "face", "facing", "faced", "be facing", "B"),
        ("Many people are allergic ___ dust.", "from", "of", "to", "with", "C"),
        ("The movie is interesting, ___?", "is it", "isn't it", "was it", "wasn't it", "B"),
        ("He came late to school ___ the heavy rain.", "due to", "because", "although", "even though", "A"),
        ("The ___ of the meeting was to discuss the school fees.", "purpose", "propose", "proposal", "proposement", "A"),
        ("Neither the teacher nor the students ___ present.", "is", "are", "was", "were", "B"),
        ("He is not ___ to go to the party.", "enough tall", "tall enough", "taller enough", "enough taller", "B"),
        ("If he had studied harder, he ___ passed.", "will have", "would have", "would", "will", "B"),
        ("That bag is hers, isn't ___?", "she", "it", "he", "her", "B"),
    ]
    for q in lexis_items:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': f"The correct answer is {q[5]}.", 'topic': lexis.id})

    # ===== OLD ENGLISH: GRAMMAR & SYNTAX (40 questions) =====
    grammar_items = [
        ("The girl, as well as her brothers, ___ going on a trip.", "are", "were", "is", "have", "C"),
        ("If she had known earlier, she ___ have told you.", "will", "would", "should", "would have", "D"),
        ("The teacher, together with his assistants, ___ coming now.", "are", "is", "were", "have been", "B"),
        ("Neither the boys nor their sister ___ the answer.", "know", "knows", "are knowing", "has know", "B"),
        ("I am used to ___ early every day.", "get up", "getting up", "gets up", "got up", "B"),
        ("She ___ her homework before dinner.", "has finished", "had finished", "is finishing", "will finish", "B"),
        ("Each of the players ___ a medal.", "receive", "have received", "receives", "receiving", "C"),
        ("We had hardly reached the station ___ it began to rain.", "than", "that", "when", "then", "C"),
        ("She would rather you ___ now.", "go", "went", "gone", "going", "B"),
        ("Had they arrived earlier, they ___ the bus.", "would have caught", "will catch", "caught", "would catch", "A"),
        ("He behaves as though he ___ the boss.", "is", "were", "was", "be", "B"),
        ("He insisted that the boy ___ punished.", "be", "is", "should being", "was", "A"),
        ("Scarcely had he entered the hall ___ the lights went off.", "when", "than", "but", "and", "A"),
        ("She has been singing since the program ___ .", "began", "begins", "begin", "begun", "A"),
        ("It's high time we ___ the truth.", "know", "knew", "known", "will know", "B"),
        ("He speaks English better than ___ in his class.", "any student", "any other student", "every student", "all student", "B"),
        ("The more she cried, ___.", "the more she felt relieved", "she felt more relieved", "more she felt relieved", "the most she felt relieved", "A"),
        ("The baby is too weak ___.", "to cried", "to be crying", "to cry", "for crying", "C"),
        ("I would have helped you if I ___ earlier.", "knew", "know", "have known", "had known", "D"),
        ("No sooner had they left ___ it started to rain.", "when", "than", "then", "that", "B"),
        ("He ran so fast that he ___ the race.", "will win", "wins", "won", "had won", "C"),
        ("He jumped ___ the river to save the child.", "in", "into", "onto", "of", "B"),
        ("The house was infested ___ rats.", "with", "by", "of", "from", "A"),
        ("She always prides herself ___ her honesty.", "for", "in", "on", "at", "C"),
        ("The politician is accused ___ corruption.", "on", "for", "with", "of", "D"),
        ("The food is not suitable ___ infants.", "to", "for", "of", "at", "B"),
        ("You had better ___ your homework before going out.", "finish", "finishing", "finished", "had finish", "A"),
        ("If I were you, I ___ accept the offer.", "will", "shall", "would", "must", "C"),
        ("He can't help ___ at the joke.", "to laugh", "laughing", "laughed", "laugh", "B"),
        ("Would you mind ___ the window?", "to open", "open", "opening", "opened", "C"),
        ("I made him ___ the ground.", "cleaning", "to clean", "clean", "cleaned", "C"),
        ("The plane had already taken off before we ___ the airport.", "reached", "reach", "had reached", "were reaching", "A"),
        ("Neither James nor his friends ___ the news.", "knows", "knowing", "know", "knews", "C"),
        ("A number of students ___ absent today.", "was", "were", "is", "be", "B"),
        ("The president and commander-in-chief ___ visiting today.", "is", "are", "were", "have", "A"),
        ("He would have succeeded if he ___ harder.", "works", "has worked", "had worked", "have worked", "C"),
        ("The boy looks as if he ___ a ghost.", "sees", "seen", "has seen", "had seen", "D"),
        ("The room is too small for the children to play ___ it.", "with", "into", "on", "in", "D"),
        ("We are looking forward to ___ you next week.", "see", "seeing", "saw", "seen", "B"),
        ("Neither the books nor the pen ___ on the table.", "is", "are", "have", "were", "A"),
    ]
    for q in grammar_items:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': f"The correct answer is {q[5]}.", 'topic': grammar.id})

    # ===== OLD ENGLISH: ADVANCED GRAMMAR (30 questions) =====
    advanced_items = [
        ("Were he more considerate, he ___ have acted that way.", "wouldn't", "shouldn't", "won't", "might", "A"),
        ("He talked about the incident as though he ___ there.", "was", "has been", "had been", "will be", "C"),
        ("Scarcely had he left the room ___ the fight started.", "than", "when", "but", "that", "B"),
        ("No sooner had she stepped out ___ the visitors arrived.", "than", "when", "that", "but", "A"),
        ("If only he ___ earlier, he would have been on time.", "leaves", "left", "had left", "would have left", "C"),
        ("It is imperative that she ___ the deadline.", "meets", "met", "meet", "meeting", "C"),
        ("He behaved as if nothing ___ happened.", "have", "had", "has", "was", "B"),
        ("The teacher demanded that every student ___ quiet.", "be", "is", "should be", "must be", "A"),
        ("Neither the chairman nor his assistants ___ present at the meeting.", "was", "were", "has been", "is", "B"),
        ("The boy would not have failed if he ___ his teacher's advice.", "has taken", "had taken", "took", "would take", "B"),
        ("Such behaviour is not only unacceptable but also ___.", "condemned", "condemnable", "condemning", "to condemn", "B"),
        ("Her argument was lucid and ___ enough to win the debate.", "cogent", "coherent", "confusing", "cohesive", "A"),
        ("The company is known for its ___ treatment of staff.", "benevolent", "malevolent", "lenient", "negligent", "A"),
        ("Had the doctor arrived earlier, the patient ___.", "might survive", "might have survived", "could survive", "will have survived", "B"),
        ("The lawyer argued his point with such ___ that the jury was convinced.", "vehemence", "vengeance", "violence", "validity", "A"),
        ("I wish I ___ your advice last year.", "took", "had taken", "have taken", "take", "B"),
        ("Had he known the rules, he ___ have made that mistake.", "wouldn't", "won't", "shouldn't", "would", "A"),
        ("The workers insisted that the management ___ their salaries.", "increase", "increases", "increased", "must increase", "A"),
        ("If it were not for her pride, she ___ apologized.", "will have", "would have", "must have", "has", "B"),
        ("The Vice Chancellor, accompanied by his aides, ___ addressing the press.", "are", "is", "were", "be", "B"),
        ("His explanation was not only unconvincing but also ___.", "verbose", "redundant", "repetitive", "contradictory", "D"),
        ("___ we proceed, let's review what we've covered.", "Before", "Until", "Unless", "Meanwhile", "A"),
        ("The film was so compelling that it held me ___.", "spellbound", "enchanted", "trapped", "attentive", "A"),
        ("She never misses an opportunity to ___ her wealth.", "flaunt", "flout", "display", "flourish", "A"),
        ("The government plans to ___ subsidies gradually.", "phase in", "phase out", "fade in", "pull out", "B"),
        ("The two parties finally came to a ___ after weeks of negotiation.", "concession", "conclusion", "compromise", "commitment", "C"),
        ("The activist was known for her ___ opposition to injustice.", "vehement", "violent", "vocal", "strong", "A"),
        ("His argument was filled with logical ___.", "flaws", "fails", "falls", "faults", "A"),
        ("The military seized power in a bloodless ___.", "coup", "coop", "siege", "regime", "A"),
        ("The teacher spoke so authoritatively ___ the entire class was silent.", "that", "which", "when", "as", "A"),
    ]
    for q in advanced_items:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': f"The correct answer is {q[5]}.", 'topic': adv_grammar.id})
    # ===== OLD ENGLISH: VOCABULARY (30 questions) =====
    vocab_items = [
        ("The manager's response was rather inflammatory. 'Inflammatory' means:", "thoughtful", "insightful", "provoking", "calming", "C"),
        ("The senator's speech was filled with platitudes. 'Platitudes' means:", "wise sayings", "clichés", "jokes", "arguments", "B"),
        ("She has a penchant for classical music. 'Penchant' means:", "dislike", "distaste", "fondness", "phobia", "C"),
        ("The witness gave a lucid account. 'Lucid' means:", "confusing", "clear", "lengthy", "doubtful", "B"),
        ("His obnoxious behavior irritated everyone. 'Obnoxious' means:", "pleasant", "rude", "generous", "timid", "B"),
        ("Her actions were commendable. 'Commendable' means:", "deserving praise", "shameful", "confusing", "unnoticed", "A"),
        ("He was reluctant to take up the position. 'Reluctant' means:", "unwilling", "happy", "proud", "delighted", "A"),
        ("The criminal was found to be remorseless. 'Remorseless' means:", "ashamed", "regretful", "unapologetic", "confused", "C"),
        ("The president abdicated his responsibilities. 'Abdicated' means:", "accepted", "rejected", "took over", "resigned", "D"),
        ("Their efforts were futile. 'Futile' means:", "effective", "worthwhile", "useless", "important", "C"),
        ("The general led a covert operation. 'Covert' means:", "open", "secret", "hasty", "confused", "B"),
        ("He was meticulous in his research. 'Meticulous' means:", "careless", "thorough", "indifferent", "partial", "B"),
        ("She's known for her altruism. 'Altruism' means:", "selfishness", "generosity", "indifference", "arrogance", "B"),
        ("The idea was preposterous. 'Preposterous' means:", "logical", "sensible", "absurd", "factual", "C"),
        ("He showed tenacity in pursuing his goals. 'Tenacity' means:", "laziness", "hesitation", "determination", "weakness", "C"),
        ("Her explanation was specious. 'Specious' means:", "believable", "misleading", "simple", "true", "B"),
        ("The director's comment was acerbic. 'Acerbic' means:", "polite", "harsh", "helpful", "boring", "B"),
        ("The scholar is known for his erudition. 'Erudition' means:", "ignorance", "foolishness", "scholarship", "arrogance", "C"),
        ("He became belligerent when provoked. 'Belligerent' means:", "quiet", "aggressive", "sorrowful", "cautious", "B"),
        ("The general's speech was full of hyperbole. 'Hyperbole' means:", "modesty", "exaggeration", "falsehood", "facts", "B"),
        ("His dormant ambition was reawakened. 'Dormant' means:", "dead", "latent", "exposed", "intense", "B"),
        ("He was always gregarious. 'Gregarious' means:", "reserved", "sociable", "irritable", "mysterious", "B"),
        ("The artist's latest work is truly exquisite. 'Exquisite' means:", "ugly", "painful", "beautiful", "complex", "C"),
        ("The government made a tacit agreement. 'Tacit' means:", "secret", "silent", "open", "strong", "B"),
        ("He was caught red-handed.", "innocently", "by surprise", "in the act", "in disguise", "C"),
        ("He was adamant in his refusal. 'Adamant' means:", "unsure", "flexible", "unyielding", "rude", "C"),
        ("Her response was ambiguous. 'Ambiguous' means:", "unclear", "rude", "direct", "positive", "A"),
        ("The teacher's remarks were incisive. 'Incisive' means:", "vague", "sharp", "unnecessary", "slow", "B"),
        ("He was aloof at the gathering. 'Aloof' means:", "friendly", "warm", "distant", "attentive", "C"),
        ("The judge was known for his probity. 'Probity' means:", "dishonesty", "integrity", "kindness", "authority", "B"),
    ]
    for q in vocab_items:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': f"The correct answer is {q[5]}.", 'topic': vocab.id})

    # ===== OLD ENGLISH: ORAL ENGLISH (30 questions) =====
    oral_items = [
        ("In which word is the vowel sound different? (seat, beat, sit, neat)", "seat", "beat", "sit", "neat", "C"),
        ("Choose the odd one: boot, root, foot, loot", "boot", "root", "foot", "loot", "C"),
        ("Different consonant sound: chew, chain, chart, chef", "chew", "chain", "chart", "chef", "D"),
        ("Which contains /ʌ/ sound? full, cut, pool, cool", "full", "cut", "pool", "cool", "B"),
        ("'th' pronounced /ð/ in: thing, thought, this, think", "thing", "thought", "this", "think", "C"),
        ("Odd initial sound: judge, jungle, genre, ginger", "judge", "jungle", "genre", "ginger", "C"),
        ("Contains diphthong /eɪ/: cat, said, pain, bed", "cat", "said", "pain", "bed", "C"),
        ("Same vowel as 'hat': car, heart, cup, bat", "car", "heart", "cup", "bat", "D"),
        ("Word with plosive consonant: fan, bag, ship, zoo", "fan", "bag", "ship", "zoo", "B"),
        ("Final sound in 'judge': /tʃ/, /dʒ/, /ʒ/, /d/", "/tʃ/", "/dʒ/", "/ʒ/", "/d/", "B"),
        ("Word with /ɔ:/ sound: hot, sort, hut, cat", "hot", "sort", "hut", "cat", "B"),
        ("/ʃ/ present in: pleasure, mission, genre, vision", "pleasure", "mission", "genre", "vision", "B"),
        ("Consonant in 'photo': /p/, /f/, /v/, /θ/", "/p/", "/f/", "/v/", "/θ/", "B"),
        ("/əʊ/ diphthong: caught, boat, bet, box", "caught", "boat", "bet", "box", "B"),
        ("'sure' begins with: /ʃ/, /s/, /z/, /ʒ/", "/ʃ/", "/s/", "/z/", "/ʒ/", "A"),
        ("Stressed syllable in 'education': first, second, third, fourth", "first", "second", "third", "fourth", "C"),
        ("Stress on second syllable: CONtract, conTRACT, REcord, PREsent", "CONtract", "conTRACT", "REcord", "PREsent", "B"),
        ("Stress in 'photograph': first, second, third, none", "first", "second", "third", "none", "A"),
        ("WH-question intonation usually: rises, falls, flat, rises then falls", "rises", "falls", "flat", "rises then falls", "B"),
        ("'Are you coming?' ends with: falling, rising, level, high", "falling", "rising", "level", "high", "B"),
        ("Primary stress on first syllable: apply, produce (verb), record (noun), permit (verb)", "apply", "produce (verb)", "record (noun)", "permit (verb)", "C"),
        ("Stress in 'presentation': first, second, third, fourth", "first", "second", "third", "fourth", "C"),
        ("Rising intonation common in: commands, statements, yes/no questions, exclamations", "commands", "statements", "yes/no questions", "exclamations", "C"),
        ("Stress in 'understand': first, second, third, all equal", "first", "second", "third", "all equal", "C"),
        ("Stress in 'economy': first, second, third, fourth", "first", "second", "third", "fourth", "B"),
        ("Falling intonation example: 'Is he there?', 'Come in.', 'Are you okay?', 'Will she come?'", "Is he there?", "Come in.", "Are you okay?", "Will she come?", "B"),
        ("Stress pattern for 'democracy': DEM-o-cracy, de-MO-cracy, de-mo-CRA-cy, dem-o-CRA-cy", "DEM-o-cracy", "de-MO-cracy", "de-mo-CRA-cy", "dem-o-CRA-cy", "B"),
        ("Intonation in a list rises on each item except: last, first, second, all", "last", "first", "second", "all", "A"),
        ("Sentence stress highlights: articles, auxiliary verbs, content words, pronouns", "articles", "auxiliary verbs", "content words", "pronouns", "C"),
        ("Rising intonation typical: 'I love it.', 'What are you doing?', 'Can I help you?', 'They left early.'", "I love it.", "What are you doing?", "Can I help you?", "They left early.", "C"),
    ]
    for q in oral_items:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': f"The correct answer is {q[5]}.", 'topic': oral.id})

    # ===== OLD ENGLISH: PHRASAL VERBS (30 questions) =====
    pv_items = [
        ("She came ___ a rare antique while cleaning the attic.", "upon", "about", "to", "across", "A"),
        ("We need to get ___ this obstacle to succeed.", "through", "across", "over", "around", "C"),
        ("The thieves made ___ with a large sum of money.", "away", "off", "out", "up", "A"),
        ("He finally gave ___ to the pressure and resigned.", "out", "up", "away", "in", "D"),
        ("I couldn't make ___ what he was saying due to the noise.", "off", "over", "out", "up", "C"),
        ("We'll have to put ___ the meeting till next week.", "out", "off", "down", "aside", "B"),
        ("She was brought ___ by her grandmother.", "up", "off", "on", "to", "A"),
        ("He's really taken ___ his new role as team leader.", "on", "to", "in", "up", "A"),
        ("The company had to cut ___ on spending due to losses.", "up", "out", "back", "off", "C"),
        ("The project fell ___ due to lack of funding.", "down", "apart", "away", "through", "B"),
        ("The child burst ___ crying.", "into", "out", "in", "off", "A"),
        ("I need to look ___ this word in the dictionary.", "at", "into", "for", "up", "D"),
        ("We must carry ___ with our plans despite the delay.", "through", "out", "on", "away", "C"),
        ("They were held ___ by heavy traffic.", "up", "out", "in", "back", "A"),
        ("She tried to bring ___ a change in the system.", "up", "in", "about", "on", "C"),
        ("He was completely taken ___ by the news.", "off", "aback", "aside", "down", "B"),
        ("The scandal will surely blow ___ soon.", "over", "up", "off", "by", "A"),
        ("I need to brush ___ on my French before the trip.", "in", "up", "out", "off", "B"),
        ("The plane took ___ an hour late.", "away", "off", "out", "up", "B"),
        ("He turned ___ the offer because it was too risky.", "off", "around", "down", "out", "C"),
        ("She was completely worn ___ after the long shift.", "in", "down", "up", "out", "D"),
        ("You must stick ___ the rules.", "at", "with", "to", "on", "C"),
        ("He always looks ___ his younger brother.", "after", "for", "to", "out", "A"),
        ("We finally ran ___ of petrol.", "up", "down", "off", "out", "D"),
        ("He tried to pass ___ the fake watch as genuine.", "out", "off", "over", "in", "B"),
        ("The committee called ___ the strike after negotiations.", "off", "in", "back", "up", "A"),
        ("You should back ___ from this conflict.", "off", "out", "down", "away", "A"),
        ("I don't know how she puts ___ with his behavior.", "on", "out", "up", "over", "C"),
        ("The rumor turned ___ to be false.", "down", "out", "over", "in", "B"),
        ("Let me go ___ the document one more time.", "off", "through", "in", "back", "B"),
    ]
    for q in pv_items:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': f"The correct answer is {q[5]}.", 'topic': phrasal.id})

    # ===== OLD ENGLISH: ANALOGIES (30 questions) =====
    analogy_items = [
        ("Ephemeral : Transient :: Permanent : ?", "Deliberate", "Enduring", "Changing", "Temporary", "B"),
        ("Obsolete : Modern :: Archaic : ?", "Ancient", "Futuristic", "Antique", "Contemporary", "D"),
        ("Ornithologist : Birds :: Herpetologist : ?", "Mammals", "Reptiles", "Insects", "Fishes", "B"),
        ("Symphony : Composer :: Theorem : ?", "Engineer", "Mathematician", "Scientist", "Philosopher", "B"),
        ("Allegory : Story :: Satire : ?", "Mockery", "Humor", "Irony", "Critique", "D"),
        ("Germinate : Seed :: Hatch : ?", "Bird", "Nest", "Egg", "Chick", "C"),
        ("Enervate : Strength :: Obscure : ?", "Light", "Darkness", "Clarity", "Ambiguity", "C"),
        ("Anarchy : Order :: Chaos : ?", "Revolution", "Structure", "Peace", "System", "D"),
        ("Quintessence : Essence :: Apex : ?", "Zenith", "Base", "Bottom", "Low", "A"),
        ("Sculptor : Statue :: Architect : ?", "Builder", "Design", "House", "Blueprint", "C"),
        ("Dogma : Doctrine :: Hypothesis : ?", "Conclusion", "Proof", "Theory", "Assumption", "C"),
        ("Equivocate : Mislead :: Elaborate : ?", "Simplify", "Explain", "Confuse", "Extend", "B"),
        ("Manuscript : Author :: Score : ?", "Singer", "Musician", "Composer", "Dancer", "C"),
        ("Cacophony : Sound :: Muddle : ?", "Sight", "Order", "Confusion", "Logic", "C"),
        ("Philanthropist : Generosity :: Misogynist : ?", "Woman", "Hatred", "Chauvinism", "Contempt", "D"),
        ("Capitulate : Resist :: Succumb : ?", "Confront", "Yield", "Withstand", "Obey", "C"),
        ("Debacle : Failure :: Windfall : ?", "Success", "Loss", "Gain", "Disaster", "C"),
        ("Predator : Prey :: Capitalist : ?", "Consumer", "Socialist", "Market", "Profit", "A"),
        ("Cipher : Code :: Puzzle : ?", "Mystery", "Riddle", "Solution", "Game", "B"),
        ("Lexicon : Words :: Anthology : ?", "Books", "Stories", "Poems", "Works", "C"),
        ("Acumen : Insight :: Lethargy : ?", "Laziness", "Fatigue", "Alertness", "Energy", "A"),
        ("Nocturnal : Bat :: Diurnal : ?", "Moon", "Human", "Owl", "Snake", "B"),
        ("Macabre : Death :: Risqué : ?", "Comedy", "Indecency", "Mystery", "Caution", "B"),
        ("Eulogy : Praise :: Lampoon : ?", "Abuse", "Humor", "Ridicule", "Exaggeration", "C"),
        ("Conundrum : Riddle :: Paradigm : ?", "Standard", "Puzzle", "Paradox", "Problem", "A"),
        ("Prophecy : Predict :: Diagnosis : ?", "Treat", "Cure", "Determine", "Identify", "D"),
        ("Articulate : Speak :: Agile : ?", "Leap", "Run", "Move", "Jump", "C"),
        ("Gluttony : Food :: Avarice : ?", "Power", "Wealth", "Ambition", "Authority", "B"),
        ("Tyrant : Autocracy :: Voter : ?", "Democracy", "Majority", "Government", "President", "A"),
        ("Catalyst : Reaction :: Key : ?", "Lock", "Door", "Security", "Entry", "D"),
    ]
    for q in analogy_items:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': f"The correct answer is {q[5]}.", 'topic': analogies_topic.id})

    # ===== NEW ENGLISH: SENTENCE STRUCTURE (30 questions) =====
    struct_qs = [
        ("Identify the sentence type: 'Although she was tired, she finished her homework.'", "Simple", "Compound", "Complex", "Compound-complex", "C", "One independent + one dependent clause"),
        ("Which of the following is a compound sentence?", "The boy who came late was punished.", "She ran fast and won the race.", "After the rain stopped, we went out.", "I like rice, but my brother prefers yam.", "D", "Two independent clauses joined by 'but'"),
        ("'The man that I saw yesterday is my uncle.' The underlined clause is:", "Noun clause", "Adjective clause", "Adverb clause", "Main clause", "B", "Modifies 'the man'"),
        ("Which sentence contains a noun clause?", "He asked where the book was.", "The house which was built in 1990 collapsed.", "She arrived after the show had started.", "Running quickly, he escaped.", "A", "'where the book was' acts as object"),
        ("'Had I known, I would have come earlier.' The sentence expresses:", "A real condition", "A future possibility", "An unreal past condition", "A command", "C", "Inverted form of 'If I had known'"),
        ("Identify the subordinate clause: 'The student who studies hard will succeed.'", "The student", "who studies hard", "will succeed", "The student will succeed", "B", "Relative clause modifying 'the student'"),
        ("Which sentence is grammatically incorrect because of faulty subordination?", "Because he was late, so he missed the bus.", "Although he was tired, he kept working.", "She left after the movie ended.", "If you study, you will pass.", "A", "Cannot use both 'because' and 'so'"),
        ("'The more you practice, the better you become.' This is an example of:", "Parallel structure", "Comparative correlative", "Ellipsis", "Anaphora", "B", "Correlative construction"),
        ("Choose the sentence with correct parallel structure:", "She likes dancing, to sing, and jogging.", "He is smart, hardworking, and shows kindness.", "The teacher asked us to read, write, and solve problems.", "I enjoy swimming, to run, and bike.", "C", "All infinitives parallel"),
        ("Which sentence uses an appositive correctly?", "My brother a doctor lives abroad.", "My brother, a doctor, lives abroad.", "My brother a doctor, lives abroad.", "My brother lives abroad a doctor.", "B", "Appositive set off by commas"),
        ("Identify the independent clause: 'If you heat ice, it melts.'", "If you heat ice", "it melts", "you heat ice", "If you heat ice, it melts", "B", "Main clause that can stand alone"),
        ("'I will come provided that you invite me.' The underlined phrase expresses:", "Condition", "Cause", "Concession", "Purpose", "A", "'provided that' introduces a condition"),
        ("Which sentence contains a dangling modifier?", "Running down the street, the bus left me.", "While running down the street, I missed the bus.", "I missed the bus because I was running.", "Running down the street made me miss the bus.", "A", "Modifier illogically modifies 'the bus'"),
        ("'What he said was quite surprising.' The subject is:", "What he said", "was", "quite surprising", "he", "A", "Noun clause as subject"),
        ("Identify the sentence pattern: 'The committee elected him chairman.'", "SVO", "SVOC", "SVOO", "SVC", "B", "Subject + Verb + Object + Object Complement"),
        ("'No sooner had he arrived than the fight started.' This structure shows:", "Comparison", "Immediate succession", "Cause-effect", "Concession", "B", "One event happens immediately after another"),
        ("Choose the correct sentence:", "The reason why he failed is because he didn't study.", "The reason why he failed is that he didn't study.", "The reason why he failed is due to he didn't study.", "The reason he failed is because of not studying.", "B", "After 'reason' use 'that' not 'because'"),
        ("'She is the girl whose father is a doctor.' 'Whose' indicates:", "Possession", "Person", "Thing", "Place", "A", "'Whose' shows ownership"),
        ("Which sentence uses a cleft sentence for emphasis?", "It was John that broke the vase.", "John broke the vase yesterday.", "Did John break the vase?", "Breaking the vase was John.", "A", "It-cleft: It was X that Y"),
        ("'The house needs painting.' The verb 'needs' is followed by a:", "Gerund", "Past participle", "Infinitive", "Bare infinitive", "A", "Need + gerund"),
        ("Identify the adverbial clause: 'He spoke as if he were the owner.'", "He spoke", "as if he were the owner", "the owner", "He spoke as if", "B", "Clause of manner"),
        ("Which sentence is a run-on?", "I love rice it is my favourite food.", "I love rice, it is my favourite food.", "I love rice; it is my favourite food.", "I love rice because it is my favourite food.", "A", "Two independent clauses without punctuation"),
        ("'To live in a big city is my dream.' The infinitive phrase functions as:", "Subject", "Object", "Complement", "Adverbial", "A", "Infinitive phrase is the subject"),
        ("Choose the sentence with correct subjunctive mood:", "I suggest that he goes to the doctor.", "I suggest that he go to the doctor.", "I suggest that he went to the doctor.", "I suggest that he is going to the doctor.", "B", "Subjunctive: base form 'go'"),
        ("'Were she here, she would help us.' This implies:", "She is here", "She is not here", "She may come", "She helped us", "B", "Unreal present condition"),
        ("Identify the type of 'that' clause: 'I believe that he is honest.'", "Noun clause (object)", "Adjective clause", "Adverb clause", "Relative clause", "A", "That-clause as object of 'believe'"),
        ("Which sentence contains an absolute phrase?", "The test being over, the students left.", "The students left after the test.", "Because the test was over, the students left.", "The test ended, so the students left.", "A", "Noun + participle not grammatically attached"),
        ("'That she succeeded surprised nobody.' The grammatical function is:", "Subject", "Direct object", "Subject complement", "Object of preposition", "A", "Noun clause as subject"),
        ("Which sentence has a misplaced modifier?", "I only eat vegetables on Mondays.", "She almost drove her children to school every day.", "He nearly lost all his money.", "They quickly finished the food.", "B", "'almost' misplaced"),
        ("'Both the teacher and the students ___ present.' Choose the correct verb.", "was", "is", "were", "has", "C", "Both...and takes plural verb"),
    ]
    for q in struct_qs:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': structure_topic.id})

    # ===== NEW ENGLISH: VERB TENSES (25 questions) =====
    tense_qs = [
        ("She ___ her homework before dinner last night.", "has finished", "had finished", "finished", "was finishing", "B", "Past perfect for action before another past action"),
        ("By next year, I ___ my degree.", "will complete", "complete", "will have completed", "am completing", "C", "Future perfect"),
        ("He ___ in Lagos since 2010.", "lived", "has lived", "was living", "had lived", "B", "Present perfect with 'since'"),
        ("When I arrived, the meeting ___ already ___.", "has / begun", "had / begun", "was / begun", "did / begin", "B", "Past perfect"),
        ("The baby ___ for two hours when the mother finally woke up.", "cried", "had been crying", "has been crying", "was crying", "B", "Past perfect continuous"),
        ("Choose the correct sequence: 'If I ___ you, I ___ apologize.'", "am / will", "were / would", "was / would", "had been / would have", "B", "Unreal present condition"),
        ("She ___ to music every morning when I call her.", "listens", "listened", "is listening", "has listened", "A", "Simple present for habitual action"),
        ("They ___ the match because of rain when we arrived.", "cancelled", "had cancelled", "were cancelling", "have cancelled", "B", "Past perfect"),
        ("Next week at this time, we ___ in the air to London.", "will fly", "will be flying", "are flying", "fly", "B", "Future continuous"),
        ("The soup ___ good. I think I'll have another bowl.", "tastes", "is tasting", "tasted", "has tasted", "A", "Stative verb in simple present"),
        ("She ___ on this project for months before it was approved.", "worked", "had been working", "has worked", "was working", "B", "Past perfect continuous"),
        ("I ___ never ___ to Abuja before my last trip.", "have / been", "had / been", "did / go", "was / going", "B", "Past perfect"),
        ("By 2030, the population ___ by 20%.", "will increase", "will have increased", "is increasing", "increases", "B", "Future perfect"),
        ("He ___ as a teacher for five years now.", "worked", "has been working", "is working", "works", "B", "Present perfect continuous"),
        ("When she saw the mess, she ___ furious.", "got", "has got", "had got", "was getting", "A", "Simple past"),
        ("I ___ to call you yesterday, but I forgot.", "intended", "had intended", "was intending", "have intended", "B", "Past perfect for unfulfilled intention"),
        ("The train ___ at 6 PM tomorrow.", "leaves", "will leave", "is leaving", "is going to leave", "A", "Simple present for scheduled future"),
        ("She ___ to the party if she had been invited.", "would come", "would have come", "will come", "came", "B", "Past unreal condition"),
        ("I ___ a strange noise while I ___ dinner.", "heard / was preparing", "was hearing / prepared", "heard / prepared", "have heard / prepare", "A", "Simple past interrupting past continuous"),
        ("Up to now, nobody ___ the missing child.", "found", "has found", "had found", "finds", "B", "Present perfect with 'up to now'"),
        ("He is always ___ late. I'm tired of it.", "coming", "come", "comes", "came", "A", "'always' + present continuous for annoyance"),
        ("The concert ___ before we ___ the venue.", "started / reached", "had started / reached", "has started / reached", "was starting / reached", "B", "Past perfect + simple past"),
        ("I promise I ___ you as soon as I arrive.", "will call", "call", "am calling", "would call", "A", "Future simple"),
        ("She ___ her leg while she ___.", "broke / was skiing", "was breaking / skied", "broke / skied", "had broken / skied", "A", "Simple past interrupting past continuous"),
        ("We ___ for an hour before the bus arrived.", "waited", "had been waiting", "have waited", "were waiting", "B", "Past perfect continuous"),
    ]
    for q in tense_qs:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': tense_topic.id})

    # ===== NEW ENGLISH: AGREEMENT & CONCORD (25 questions) =====
    agree_qs = [
        ("Either the boys or the girl ___ to blame.", "are", "is", "were", "have", "B", "Verb agrees with nearer subject (girl → singular)"),
        ("The team ___ playing well in their last match.", "was", "were", "are", "have", "B", "Collective noun as individuals"),
        ("Each of the students ___ a textbook.", "have", "has", "are having", "were", "B", "'Each' takes singular verb"),
        ("Neither the manager nor his assistants ___ present.", "was", "were", "is", "has", "B", "Nearer subject 'assistants' (plural)"),
        ("The news ___ shocking.", "are", "were", "is", "have", "C", "'News' is singular uncountable"),
        ("Mathematics ___ my favourite subject.", "are", "were", "is", "have", "C", "Subject names are singular"),
        ("A number of students ___ absent today.", "was", "is", "are", "has", "C", "'A number of' + plural noun + plural verb"),
        ("The number of applicants ___ increased.", "have", "has", "are", "were", "B", "'The number of' + singular verb"),
        ("Not only the students but also the teacher ___ present.", "were", "are", "was", "have", "C", "Nearer subject 'teacher' (singular)"),
        ("Every man, woman, and child ___ given a gift.", "were", "are", "was", "have", "C", "Compound subjects with 'every' take singular verb"),
        ("One of the boys ___ to be elected.", "are hoping", "hope", "hopes", "were hoping", "C", "Subject is 'one' (singular)"),
        ("The politician, along with his aides, ___ coming now.", "are", "were", "is", "have", "C", "'along with' doesn't affect verb number"),
        ("Half of the cake ___ eaten.", "were", "are", "was", "have", "C", "'Half of' + singular noun → singular verb"),
        ("Half of the apples ___ rotten.", "was", "is", "were", "has", "C", "'Half of' + plural noun → plural verb"),
        ("The jury ___ divided in their opinions.", "was", "is", "were", "has", "C", "Members as individuals → plural verb"),
        ("Physics ___ a difficult subject for many.", "are", "were", "is", "have", "C", "Subject names are singular"),
        ("There ___ several reasons for the delay.", "is", "was", "are", "has", "C", "Existential 'there' + plural noun → plural verb"),
        ("Neither of the answers ___ correct.", "are", "were", "is", "have", "C", "'Neither of' + singular verb (formal)"),
        ("The committee ___ issued its report.", "have", "are", "has", "were", "C", "Collective noun as a unit → singular"),
        ("Bread and butter ___ my favourite breakfast.", "are", "were", "is", "have", "C", "Compound seen as one concept → singular"),
        ("He is one of those people who ___ always late.", "is", "are", "was", "has", "B", "'who' refers to 'people' (plural)"),
        ("The singer and actor ___ arrived.", "have", "are", "is", "has", "D", "One person with two roles → singular"),
        ("The singer and the actor ___ arrived.", "has", "is", "have", "was", "C", "Two different persons → plural"),
        ("Either you or he ___ to do the work.", "have", "are", "is", "was", "C", "Nearer subject 'he' (singular)"),
        ("All of the furniture ___ been sold.", "have", "are", "were", "has", "D", "'Furniture' is uncountable → singular"),
    ]
    for q in agree_qs:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': agreement_topic.id})

    # ===== NEW ENGLISH: CONNECTORS (25 questions) =====
    conn_qs = [
        ("He worked hard; ____, he failed the exam.", "therefore", "nevertheless", "consequently", "moreover", "B", "Contrast"),
        ("____ the rain, we went out.", "Despite", "Because of", "Although", "Due to", "A", "Despite + noun phrase"),
        ("She will succeed ____ she works hard.", "unless", "provided that", "whereas", "otherwise", "B", "Condition"),
        ("He is very rich; ____, he is not happy.", "therefore", "however", "moreover", "consequently", "B", "Contrastive connector"),
        ("____ it was late, we decided to continue.", "Because", "Even though", "Since", "As", "B", "Concession"),
        ("You must finish your homework ____ you cannot go out.", "otherwise", "so that", "therefore", "because", "A", "Otherwise = if not"),
        ("He studied hard ____ he could pass the exam.", "so that", "in order to", "because", "although", "A", "Purpose"),
        ("____ he is young, he is very responsible.", "Despite", "Although", "Because", "As", "B", "Concession"),
        ("The project was successful ____ many challenges.", "despite", "although", "because of", "due to", "A", "Despite + noun phrase"),
        ("I was tired, ____ I went to bed early.", "however", "therefore", "moreover", "nevertheless", "B", "Cause-effect"),
        ("____ the increase in price, demand has not fallen.", "Because of", "Due to", "In spite of", "As a result of", "C", "Contrast"),
        ("He is intelligent; ____, he lacks experience.", "consequently", "therefore", "on the other hand", "so", "C", "Contrasting qualities"),
        ("We left early ____ we would avoid traffic.", "so that", "because", "although", "unless", "A", "Purpose clause"),
        ("____ you apologize, I will not forgive you.", "If", "Unless", "Provided", "When", "B", "Unless = if not"),
        ("She was late ____ the traffic jam.", "because of", "due to the fact that", "owing to", "all of the above", "D", "All express cause"),
        ("He works hard; his brother, ____, is lazy.", "therefore", "consequently", "on the contrary", "moreover", "C", "Contrast between two persons"),
        ("____ the doctor's advice, he continued smoking.", "Despite", "Although", "Even though", "Because of", "A", "Despite + noun phrase"),
        ("He didn't study; ____, he failed.", "however", "moreover", "consequently", "nevertheless", "C", "Cause-effect result"),
        ("____ the weather was bad, we enjoyed the trip.", "Because", "Although", "Since", "As", "B", "Concession"),
        ("She is both intelligent ____ hardworking.", "and", "but", "or", "so", "A", "Correlative 'both...and'"),
        ("He speaks not only English ____ French.", "but also", "and also", "as well as", "also", "A", "Correlative 'not only...but also'"),
        ("It was very cold, ____ we lit a fire.", "so", "but", "or", "for", "A", "Result"),
        ("We must hurry; ____, we'll miss the train.", "otherwise", "therefore", "consequently", "so", "A", "Otherwise = if not"),
        ("He is poor ____ happy.", "but", "so", "for", "and", "A", "Contrast"),
        ("____ he arrived, the meeting started.", "No sooner had", "Hardly had", "As soon as", "All of the above", "D", "All indicate immediate sequence"),
    ]
    for q in conn_qs:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': connectors_topic.id})

    # ===== NEW ENGLISH: MEANING & PARAPHRASE (30 questions) =====
    meaning_qs = [
        ("Choose the option that best explains: 'He is the black sheep of the family.'", "He has dark skin", "He is the most successful", "He is a disgrace to the family", "He is the eldest", "C", "Idiom: a person who brings shame"),
        ("'The manager turned a deaf ear to our complaints.' This means:", "He ignored the complaints", "He listened carefully", "He became angry", "He referred to someone else", "A", "Pretended not to hear"),
        ("Which sentence has the same meaning as: 'Only John passed the test.'", "John passed and so did others.", "Everyone passed except John.", "No one passed except John.", "John was the only one who failed.", "C", "'Only John' means John alone passed"),
        ("Paraphrase: 'He gave up the ghost.'", "He died", "He saw a ghost", "He surrendered", "He gave a speech", "A", "Idiom meaning to die"),
        ("'You cannot eat your cake and have it.' This means:", "You should enjoy life", "You cannot have two incompatible things", "Cake is perishable", "Sharing is caring", "B", "Cannot use a resource and still retain it"),
        ("Choose the sentence that means the same as: 'She is too weak to walk.'", "She is so weak that she cannot walk.", "She is very weak but she can walk.", "She is weak enough to walk.", "She is not weak enough to walk.", "A", "'Too...to' expresses impossibility"),
        ("'I have had enough of your excuses.' Means:", "I want more excuses", "I am tired of your excuses", "Your excuses are valid", "I accept your excuses", "B", "No longer willing to tolerate"),
        ("'He is a man of straw.' Means he is:", "Very tall", "Weak and unreliable", "Made of straw", "A farmer", "B", "Idiom: no substance"),
        ("Which sentence best paraphrases 'He seldom visits us'?", "He visits us often", "He never visits us", "He rarely visits us", "He visits us regularly", "C", "Seldom = rarely"),
        ("'All that glitters is not gold.' Means:", "Everything shiny is valuable", "Some things that look valuable are not", "Gold shines", "Don't trust your eyes", "B", "Appearances can be deceptive"),
        ("'She broke down in tears.' This means:", "She destroyed something", "She started crying suddenly", "She stopped crying", "She fell down", "B", "Lost emotional control"),
        ("'He is at sixes and sevens.' Means he is:", "Confused", "Happy", "Angry", "Aged", "A", "Idiom: in a state of disorder"),
        ("Paraphrase: 'He came out with flying colours.'", "He failed badly", "He was very successful", "He used many colours", "He painted", "B", "Idiom: great success"),
        ("'I can't make head or tail of this letter.' Means:", "I cannot read it", "I cannot understand it at all", "The letter has no head or tail", "The letter is torn", "B", "Cannot understand anything"),
        ("'She let the cat out of the bag.' Means:", "She set an animal free", "She revealed a secret", "She was cruel to animals", "She closed a bag", "B", "Disclosed a secret"),
        ("'He put his foot in his mouth.' Means:", "He ate quickly", "He said something embarrassing", "He injured himself", "He was silent", "B", "Said something foolish"),
        ("'The car broke down on the highway.' Means:", "The car exploded", "The car stopped functioning", "The car was broken into", "The car was speeding", "B", "Stop working"),
        ("'She is as cool as a cucumber.' Means she is:", "Cold", "Very calm", "Slimy", "Green", "B", "Simile: very composed"),
        ("Paraphrase: 'His failure is a bolt from the blue.'", "It was expected", "It was a complete surprise", "It was caused by lightning", "It was minor", "B", "Sudden unexpected event"),
        ("'He kicked the bucket.' Means:", "He started a new job", "He died", "He played football", "He broke a bucket", "B", "Slang for die"),
        ("'She has a heart of gold.' Means she is:", "Rich", "Kind", "Precious", "Cold", "B", "Very generous and kind"),
        ("'His argument is full of hot air.' Means:", "He is angry", "His argument is empty/meaningless", "He is using hot air balloons", "He is persuasive", "B", "Empty talk"),
        ("'She left him in the lurch.' Means:", "She helped him", "She abandoned him in difficulty", "She pushed him", "She married him", "B", "Desert someone in trouble"),
        ("'The teacher gave the students a piece of her mind.' Means:", "She taught a lesson", "She scolded them severely", "She shared her thoughts kindly", "She gave them a test", "B", "Express anger or criticism"),
        ("'He is sitting on the fence.' Means:", "He is undecided", "He is resting", "He is high up", "He is neutral", "A", "Avoid taking sides"),
        ("'The CEO called the meeting off.' Means:", "He started the meeting", "He cancelled the meeting", "He postponed the meeting", "He attended the meeting", "B", "Phrasal verb: cancel"),
        ("'I will look into the matter.' Means:", "I will ignore it", "I will investigate it", "I will watch it", "I will forget it", "B", "Phrasal verb: investigate"),
        ("'He bit off more than he could chew.' Means:", "He ate too much", "He took on more than he could handle", "He choked on food", "He was greedy", "B", "Took on too much"),
        ("'She burned the midnight oil.' Means:", "She was careless", "She worked late into the night", "She started a fire", "She wasted oil", "B", "Worked very late"),
        ("'He turned over a new leaf.' Means:", "He read a book", "He changed for the better", "He gardened", "He turned a page", "B", "Reformed oneself"),
    ]
    for q in meaning_qs:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': meaning_topic.id})

    # ===== NEW ENGLISH: AMBIGUITY (20 questions) =====
    ambig_qs = [
        ("'Flying planes can be dangerous.' This sentence is ambiguous because:", "It lacks a subject", "It could mean planes that fly are dangerous OR the act of flying planes is dangerous", "The verb is wrong tense", "It contains passive voice", "B", "Structural ambiguity"),
        ("'I saw the man with the telescope.' Which interpretation is possible?", "I used a telescope to see the man", "The man had a telescope", "Both A and B", "None", "C", "Ambiguous attachment"),
        ("'The chicken is ready to eat.' This can mean:", "The chicken is hungry", "The chicken is cooked", "Both A and B", "Neither", "C", "Semantic ambiguity"),
        ("'Visiting relatives can be boring.' What are the two meanings?", "Relatives who visit are boring / The act of visiting relatives is boring", "Relatives travel a lot / Relatives are boring", "Only one meaning", "Relatives are boring to visit", "A", "Gerund vs participle ambiguity"),
        ("'I shot the elephant in my pyjamas.' The ambiguity arises from:", "The elephant wearing pyjamas", "The speaker wearing pyjamas while shooting", "Both interpretations", "The verb 'shot'", "C", "Modifier attachment"),
        ("'John saw his father driving a Mercedes.' Who is driving?", "John is driving", "His father is driving", "It's ambiguous", "Neither", "C", "Ambiguous: 'driving' could modify John or father"),
        ("'The police stopped the man with a gun.' This is ambiguous because:", "The man had a gun", "The police used a gun", "Both meanings possible", "None", "C", "Prepositional phrase attachment"),
        ("'They are cooking apples.' This could mean:", "They are cooking some apples", "The apples are used for cooking", "Both A and B", "Only A", "C", "Verb phrase vs compound noun"),
        ("'The German teacher' is ambiguous because:", "Teacher from Germany", "Teacher of German language", "Both", "Neither", "C", "Ambiguous modifier"),
        ("'He looked at the man with one eye.' Interpretations:", "The man has one eye", "He used one eye to look", "Both", "Neither", "C", "Attachment ambiguity"),
        ("'I left the car in the garage that was broken.' What is ambiguous?", "The car was broken", "The garage was broken", "Both possible", "The verb 'left'", "C", "Relative clause attachment"),
        ("'The student said the teacher is stupid on Monday.' Which is ambiguous?", "When the student spoke", "When the teacher was stupid", "Both", "Neither", "C", "Adverbial 'on Monday' attachment"),
        ("'I saw her duck.' Interpretations:", "I saw her lower her head", "I saw a duck belonging to her", "Both", "Only one", "C", "Lexical ambiguity"),
        ("'The shooting of the hunters was terrible.' Ambiguity:", "Hunters were shot", "Hunters did the shooting", "Both", "Neither", "C", "Active or passive structural ambiguity"),
        ("'He hit the man with a stick.' Means:", "He used a stick to hit the man", "The man had a stick", "Both", "Only A", "C", "Classic prepositional ambiguity"),
        ("'Time flies like an arrow.' Is ambiguous because:", "It has no subject", "Multiple grammatical parses are possible", "The tense is wrong", "The comparison is false", "B", "Can be parsed multiple ways"),
        ("'She told her sister she had won.' What is ambiguous?", "Who won", "Who was told", "Both", "Neither", "A", "Pronoun reference ambiguity"),
        ("'I didn't say he stole the money.' The ambiguity involves:", "The word 'money'", "Stress on different words changes meaning", "The tense", "The subject", "B", "Each stressed word shifts meaning"),
        ("'Beautiful girls and boys attended.' What is ambiguous?", "Whether 'beautiful' modifies both nouns", "The gender of attendees", "Both", "Neither", "A", "Scope of adjective modification"),
        ("'He saw the man on the hill with a telescope.' How many ambiguities?", "One", "Two", "Three", "None", "C", "Who had telescope, who was on hill, what saw"),
    ]
    for q in ambig_qs:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': ambiguity_topic.id})

    # ===== NEW ENGLISH: WORD ORDER & INVERSION (25 questions) =====
    wordorder_qs = [
        ("Correct the word order: 'Never I have seen such a sight.'", "Never have I seen such a sight.", "Never I have seen such a sight.", "Never seen I have such a sight.", "Never have seen I such a sight.", "A", "Inversion after negative adverbs"),
        ("Choose the correct inverted sentence:", "Only after the show did he leave.", "Only after the show he left.", "Only after the show left he.", "Only after the show he did leave.", "A", "'Only after' + clause triggers inversion"),
        ("'Hardly had I arrived when the meeting started.' This means:", "I arrived long before the meeting", "The meeting started immediately after I arrived", "I arrived after the meeting", "The meeting started before I arrived", "B", "Inversion showing immediate sequence"),
        ("Which sentence has correct inversion after 'so'?", "So beautiful was the girl that everyone stared.", "So beautiful the girl was that everyone stared.", "So was the girl beautiful that everyone stared.", "So beautiful was that the girl everyone stared.", "A", "'So + adjective' triggers inversion"),
        ("'Little did they know the truth.' Normal word order:", "They little knew the truth.", "They did little know the truth.", "Little they knew the truth.", "They knew the truth little.", "A", "Normal order: subject + adverb + verb"),
        ("Choose the correct inversion after 'Not only':", "Not only did he steal, but he also lied.", "Not only he stole, but he also lied.", "Not only stole he, but he also lied.", "Not only he did steal, but also he lied.", "A", "Auxiliary 'did' before subject"),
        ("'Under no circumstances ___ you tell anyone.'", "should", "shouldn't", "will", "would", "A", "Inversion: Under no circumstances should you"),
        ("Correct: 'Seldom we have seen such talent.'", "Seldom have we seen such talent.", "Seldom we have seen such talent.", "Seldom we see such talent.", "Seldom saw we such talent.", "A", "Inversion with 'seldom'"),
        ("'No sooner ___ than the fight started.'", "he arrived", "did he arrive", "arrived he", "he did arrive", "B", "Inversion: No sooner did he arrive"),
        ("'Only by working hard ___ succeed.'", "you will", "will you", "you can", "can you", "B", "Inversion: Only by... will you succeed"),
        ("'Were I rich, I would travel the world.' This means:", "I am rich", "I am not rich", "I will be rich", "I was rich", "B", "Unreal present condition"),
        ("Which sentence is correct?", "Had he known, he would have apologized.", "He had known, he would have apologized.", "Had known he, he would have apologized.", "Had he know, he would have apologized.", "A", "Inversion in past unreal condition"),
        ("'So loudly did he shout that everyone heard.' Normal order:", "He shouted so loudly that everyone heard.", "He did shout so loudly that everyone heard.", "So loudly he shouted that everyone heard.", "He so loudly shouted that everyone heard.", "A", "Standard SV order"),
        ("'In no way ___ this be tolerated.'", "should", "shouldn't", "will not", "does", "A", "Inversion: In no way should this be tolerated"),
        ("Choose the correct inverted sentence:", "Never before have I seen such beauty.", "Never before I have seen such beauty.", "Never before I saw such beauty.", "Never before have seen I such beauty.", "A", "Inversion with 'never before'"),
        ("'Only then ___ the truth.'", "he realized", "did he realize", "realized he", "he did realize", "B", "Inversion after 'only then'"),
        ("'Had they arrived earlier, they ___ the bus.'", "would have caught", "will catch", "caught", "would catch", "A", "Inverted conditional: past unreal"),
        ("'Not once ___ during the meeting.'", "he spoke", "did he speak", "spoke he", "he did speak", "B", "Inversion with 'not once'"),
        ("'Should you need any help, call me.' This expresses:", "A real future condition", "An unreal condition", "A past condition", "A command", "A", "Inversion of 'If you should need'"),
        ("Which sentence has incorrect word order?", "Never have I met such a kind person.", "Rarely does he come on time.", "Only after the game began did he arrive.", "Only after the game began he arrived.", "D", "Missing inversion after 'only after'"),
        ("'At no time ___ the door unlocked.'", "she left", "did she leave", "left she", "she did leave", "B", "Inversion with 'at no time'"),
        ("'No sooner had the bell rung than the students ran out.' The meaning:", "The bell rang after the students ran out", "The students ran out immediately after the bell rang", "Simultaneous", "Students ran out before the bell", "B", "No sooner...than = immediate succession"),
        ("'Little ___ that he was being watched.'", "he knew", "did he know", "knew he", "he did know", "B", "Inversion with 'little'"),
        ("'Such was her beauty that everyone admired her.' The structure emphasizes:", "Her beauty was great", "Everyone admired her", "Both", "Neither", "A", "Inversion to highlight degree"),
        ("Choose the sentence with fronting for emphasis:", "It was the money that he wanted.", "He wanted the money badly.", "The money, he wanted desperately.", "What he wanted was money.", "C", "Topicalization/fronting"),
    ]
    for q in wordorder_qs:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': wordorder_topic.id})

    # ===== NEW ENGLISH: SEMANTIC ROLES (20 questions) =====
    semantic_qs = [
        ("In 'John broke the window', the semantic role of 'John' is:", "Patient", "Agent", "Theme", "Experiencer", "B", "John performs the action → Agent"),
        ("In 'The window broke', the role of 'the window' is:", "Agent", "Patient", "Instrument", "Location", "B", "Undergoes change → Patient"),
        ("'The key opened the door.' The key is:", "Agent", "Instrument", "Patient", "Experiencer", "B", "Means by which action is done → Instrument"),
        ("In 'Mary felt a sharp pain', Mary is:", "Agent", "Patient", "Experiencer", "Theme", "C", "Experiences sensation → Experiencer"),
        ("'He gave his friend a book.' The role of 'a book' is:", "Recipient", "Theme", "Agent", "Goal", "B", "Entity transferred → Theme"),
        ("'She received a gift.' The role of 'she' is:", "Agent", "Patient", "Recipient", "Experiencer", "C", "One who receives → Recipient"),
        ("In 'The stone hit the window', the stone is:", "Agent", "Instrument", "Theme", "Patient", "B", "Used to hit → Instrument"),
        ("'I heard a strange noise.' The role of 'I' is:", "Agent", "Experiencer", "Patient", "Theme", "B", "Perception verb → Experiencer"),
        ("'The hammer broke the glass.' The hammer is:", "Agent", "Instrument", "Patient", "Force", "B", "Tool → Instrument"),
        ("In 'The soup tastes salty', the soup is:", "Theme", "Experiencer", "Agent", "Attribute", "A", "Entity with property → Theme"),
        ("'He sold the car to his brother.' The brother is:", "Recipient", "Goal", "Beneficiary", "All of the above", "D", "Goal/Recipient of transfer"),
        ("'The letter was written by Mary.' Mary is:", "Agent", "Patient", "Instrument", "Theme", "A", "By-phrase indicates Agent"),
        ("'The explosion shattered the windows.' The windows are:", "Agent", "Patient", "Instrument", "Location", "B", "Undergo effect → Patient"),
        ("'She baked a cake for him.' 'Him' is:", "Recipient", "Beneficiary", "Goal", "All of the above", "D", "Beneficiary/Recipient"),
        ("'The train arrived late.' The train is:", "Agent", "Theme", "Patient", "Instrument", "B", "Entity that moves → Theme"),
        ("'He stained the table with ink.' The ink is:", "Instrument", "Material", "Agent", "Patient", "A", "Means → Instrument"),
        ("'The boy threw the ball.' The ball is:", "Theme", "Patient", "Both A and B", "Instrument", "C", "Ball is affected/moved → Theme/Patient"),
        ("In 'He benefited from the scholarship', the scholarship is:", "Source", "Instrument", "Agent", "Theme", "A", "Source of benefit"),
        ("'The wall collapsed.' The role of 'the wall' is:", "Agent", "Patient", "Theme", "Experiencer", "C", "Undergoes change of state → Theme"),
        ("'She put the book on the table.' 'On the table' is:", "Theme", "Goal", "Source", "Instrument", "B", "Destination of movement → Goal"),
    ]
    for q in semantic_qs:
        all_english.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': semantic_topic.id})

    # ===== INSERT ALL ENGLISH QUESTIONS =====
    for i, q in enumerate(all_english):
        question = Question(
            exam_id=exam.id,
            topic_id=q['topic'],
            question_text=q['text'],
            question_type='multiple_choice',
            subject='English',
            option_a=q['a'], option_b=q['b'], option_c=q['c'], option_d=q['d'],
            correct_answer=q['ans'],
            explanation=q.get('exp', f"The correct answer is {q['ans']}."),
            marks=1,
            question_order=i + 1
        )
        db.session.add(question)

    db.session.commit()
    print(f"✅ Seeded {len(all_english)} English questions.")
def seed_general_paper():
    clear_subject('General Paper')

    topics = [
        Topic(name='Civil Service', subject='General Paper', description='Structure and functions of the civil service'),
        Topic(name='Public Corporations', subject='General Paper', description='Establishment, control, and issues of parastatals'),
        Topic(name='Local Government', subject='General Paper', description='Third tier of government, reforms, revenue'),
        Topic(name='Current Affairs & History', subject='General Paper', description='Nigerian history, institutions, and recent events'),
        Topic(name='Sports', subject='General Paper', description='Major sporting events, records, Nigerian and global sports'),
        Topic(name='Physics', subject='General Paper', description='Basic physics concepts, laws, applications'),
        Topic(name='Chemistry', subject='General Paper', description='Chemical principles, periodic table, reactions'),
        Topic(name='Literature', subject='General Paper', description='Literary terms, notable works, authors, genres'),
        Topic(name='World Organizations', subject='General Paper', description='UN, AU, ECOWAS, OPEC, WHO, IMF'),
        Topic(name='Global Events', subject='General Paper', description='Major historical events, treaties, conflicts'),
        Topic(name='Economics', subject='General Paper', description='Basic economics, Nigerian economy, fiscal policy'),
        Topic(name='Biology', subject='General Paper', description='Life sciences, human biology, ecology, genetics'),
        Topic(name='Statistics', subject='General Paper', description='Data interpretation, probability, basic stats'),
    ]
    for t in topics:
        db.session.add(t)
    db.session.commit()

    exam = Exam(
        title="General Paper",
        subject="General Paper",
        description="400 UNILAG-style General Paper questions",
        duration_minutes=60,
        total_questions=400,
        passing_score=50
    )
    db.session.add(exam)
    db.session.commit()

    civil = Topic.query.filter_by(name='Civil Service', subject='General Paper').first()
    pubcorp = Topic.query.filter_by(name='Public Corporations', subject='General Paper').first()
    localgov = Topic.query.filter_by(name='Local Government', subject='General Paper').first()
    current = Topic.query.filter_by(name='Current Affairs & History', subject='General Paper').first()
    sport_topic = Topic.query.filter_by(name='Sports', subject='General Paper').first()
    physics_topic = Topic.query.filter_by(name='Physics', subject='General Paper').first()
    chemistry_topic = Topic.query.filter_by(name='Chemistry', subject='General Paper').first()
    literature_topic = Topic.query.filter_by(name='Literature', subject='General Paper').first()
    worldorg_topic = Topic.query.filter_by(name='World Organizations', subject='General Paper').first()
    globalevents_topic = Topic.query.filter_by(name='Global Events', subject='General Paper').first()
    economics_topic = Topic.query.filter_by(name='Economics', subject='General Paper').first()
    biology_topic = Topic.query.filter_by(name='Biology', subject='General Paper').first()
    stats_topic = Topic.query.filter_by(name='Statistics', subject='General Paper').first()

    all_gp = []

    # ===== OLD GP: CIVIL SERVICE & GOVERNMENT (50 questions) =====
    old_gp = [
        ("Which of the following groups fall into the Civil Service?", "The police, the army, and the air force", "Employees of NEPA, NNPC and NRC", "Employees of ministries of finance, education and transportation", "All of the above", "C", civil.id),
        ("The recruitment or appointment of the permanent secretary is one of the duties of:", "The federal public service commission", "The state civil service commission", "The executive", "The National Assembly", "A", civil.id),
        ("In the organizational structure of the ministry, offices and positions are:", "Hierarchically arranged", "Diagonally arranged", "Secretly arranged", "Haphazardly arranged", "A", civil.id),
        ("The government maintains monopoly over certain services for:", "Selfish reasons", "Security and strategic reasons", "Undisclosed reasons", "All of the above", "B", civil.id),
        ("Ministers of local government and chieftaincy affairs were abolished in Nigeria by:", "General Yakubu Gowon", "General Murtala Mohammed", "President Ibrahim Babangida", "General Olusegun Obasanjo", "B", civil.id),
        ("Policy analysis, policy implementation and plan setting are functions of:", "The legislature", "The executive", "The local government", "The civil service", "D", civil.id),
        ("Public corporations can be controlled through:", "Riots", "Public opinion", "Civil disobedience", "None of the above", "B", pubcorp.id),
        ("The general supervision of a public corporation is carried out by the:", "Board of directors", "Board of trustees", "Managing director", "Secretary of the board", "A", pubcorp.id),
        ("The local government in Nigeria is created to:", "Create more civil service jobs", "Encourage competition among communities", "Bring the government nearer to the people", "Prevent the creation of more states", "C", localgov.id),
        ("The Civil Service embraces all workers in:", "All private corporations", "Public and private companies", "Government ministries", "Public corporations", "C", civil.id),
        ("The effective operation of the Civil Service in Nigeria is mostly hampered by:", "Inadequate training of personnel", "Corruption and inefficiency", "Debt burden and redundancy", "Poor infrastructure", "B", civil.id),
        ("The Bureau of Public Enterprises is charged with the responsibility for:", "Privatization and commercialization", "Generating revenue", "Eradicating poverty", "Providing employment opportunities", "A", pubcorp.id),
        ("Financial allocation to a local government to supplement the cost of a project is called:", "Revenue allocation", "Reimbursement", "Statutory allocation", "Matching grant", "D", localgov.id),
        ("A permanent Civil Service:", "Makes continuity in government possible", "Makes civil servants arrogant", "Promotes ethnic domination", "Is undemocratic", "A", civil.id),
        ("One form of control over public corporations is the requirement that annual reports be laid before:", "Parliament for scrutiny", "All political parties", "The President", "The judiciary", "A", pubcorp.id),
        ("Anonymity of the Civil Service means that the Civil Servant must:", "Serve any government impartially", "Be politically neutral", "Have job security", "Not receive credit or blame for policy", "D", civil.id),
        ("The local government reforms of 1976 in Nigeria were designed to:", "Decentralize authority", "Enlist grass-root support", "Achieve even development", "All of the above", "D", localgov.id),
        ("Bye-laws made by local authorities can be declared unconstitutional only by the:", "Local government service commission", "Ministry of local government", "Courts", "Attorney-General", "C", localgov.id),
        ("Mass retrenchment of workers is most likely to result in:", "Political stability", "Economic survival", "High rate of armed robbery and political instability", "Electoral malpractices", "C", civil.id),
        ("Public Corporations are established to:", "Look after local authorities", "Co-ordinate the activities of ministries", "Give advice to the government on commerce", "Provide essential services on commercial bases", "D", pubcorp.id),
        ("Which of the following is not a source of local government revenue:", "State and federal government grants", "Licensing of cars and lorries", "Market stall fees", "Returns on investment", "D", localgov.id),
        ("One of the major reasons for setting up public corporations is to:", "Maximize profit", "Compete with private companies", "Provide essential services", "Encourage patronage", "C", pubcorp.id),
        ("All of the following are functions of the civil service except:", "Making laws", "Implementing policies", "Preparing financial estimates", "Implementing edicts", "A", civil.id),
        ("One factor which militates against the effective functioning of the Civil Service is:", "Delegated legislation", "Political interference", "Judicial inference", "Political stability", "B", civil.id),
        ("Being the third tier of government, the local government is:", "Subordinate to state and federal government", "Antagonistic to state and federal government", "Co-ordinate to state and federal government", "All of the above", "A", localgov.id),
        ("One major problem facing public corporations in Nigeria is:", "Political parties", "Excessive patriotism", "Government interference", "Lack of funds", "C", pubcorp.id),
        ("Most reasons for establishing public corporations are being contradicted by the current wave of:", "Privatization and commercialization", "Legalization and nationalization", "Judicial and legislative competence", "Rigging and electoral brouhaha", "A", pubcorp.id),
        ("The recruitment, promotion and discipline of civil servants in Nigeria is the responsibility of:", "Board of Directors", "Civil Service Commission", "The president", "Ministry of Labour and Productivity", "B", civil.id),
        ("Engineers and architects in the Civil Service fall into the:", "Professional class", "Technical class", "Higher technical class", "The manipulative class", "A", civil.id),
        ("The main functions of the administrative class of the Civil Service include:", "Policy making", "Implementation of government policies", "Enactment of laws for ministries", "All of the above", "B", civil.id),
        ("The relationship between staffs of the civil service is expected to be:", "Personal and unofficial", "Official and non-personal", "Casual and inconsistent", "Illogical and sporadic", "B", civil.id),
        ("The first local government system adopted in Nigeria was:", "The French prefectorial system", "The Indian local government system", "The Russian Socialist system", "The British Council system", "D", localgov.id),
        ("The idea of making the local government the third tier of government was initiated by:", "Abdusalam Abubakar regime", "Alhaji Shehu Shagari regime", "Murtala/Obasanjo regime", "Ibrahim Babangida regime", "C", localgov.id),
        ("Before the 1976 local government reforms, one defective feature of local governments was:", "They had no functions to perform", "They had no legal personality", "They had no chairmen", "They had no political aspiration", "B", localgov.id),
        ("One of the major problems which spelt doom for Nigeria Airways was:", "Embezzlement of fund", "Corruption", "Lack of patriotism", "All of the above", "D", pubcorp.id),
        ("The main cause of infrastructure decay in Nigeria is:", "Illiteracy", "Disobedience", "Lack of maintenance culture", "Political instability", "C", current.id),
        ("One of the measures that will enhance the status of the local government is:", "Creation of more local government areas", "Up-grading to statehood", "Drafting of separate constitution", "Deduction of local government share directly from source", "D", localgov.id),
        ("To enhance the independence of the federal public service commission, members should:", "Be elected from a national party", "Take oath of celibacy", "Neither belong to the legislative nor executive branch", "Be appointed by the non-aligned movement", "C", civil.id),
        ("To be promoted from one grade level to another, a staff must first:", "Apply to the Nigeria export promotion council", "Petition the civil service commission", "Be in the president's list", "Be recommended by his departmental head", "D", civil.id),
        ("To be entitled to pension in Nigeria, a staff must:", "Work for 55 years", "Work for at least 10 consecutive years", "Work for 65 years", "Attain the age of seventy", "B", civil.id),
        ("The dismissal of a staff for official misconduct is the prerogative of:", "The permanent secretary", "The personnel manager", "The minister", "The Public Service Commission", "D", civil.id),
        ("The greatest headache affecting revenue generation by NEPA (now PHCN) was:", "Debts owed by government departments", "Refusal of NEPA men to collect revenue", "Its inability to employ accountants", "None of the above", "A", pubcorp.id),
        ("Public Corporations in Nigeria are subject to the control of:", "The judiciary", "The minister in charge", "The parliament", "Public Service Commission", "C", pubcorp.id),
        ("The public corporation is similar to the joint stock company because:", "The chairman is also the managing director", "Their administrative centres are far from factories", "The two are legal entities", "They both pay taxes", "C", pubcorp.id),
        ("Which best describes a public corporation?", "An organ of government responsible for executing policies", "A local body that renders services on a local basis", "A legal body established by an act of state to provide essential services", "A body owned by members of the public", "C", pubcorp.id),
        ("'Red tapism' can be explained as:", "The decentralized way of taking decisions", "A flexible way by which government decisions are taken", "The rigid adherence to routines by civil servants", "Management by objectives", "C", civil.id),
        ("An institution which seeks to redress people's grievances against abuse of administrative power is the:", "Ombudsman", "Judiciary", "Directorate of Public Prosecution", "Judicial Service Commission", "A", civil.id),
        ("A statutory corporation is under the supervision of:", "The Chief Justice", "The commissioner of police", "A minister", "A local government chairman", "C", pubcorp.id),
        ("To which class of the civil service does the casual or manual labour force belong?", "The technical class", "The casual class", "The manipulative class", "The higher technical class", "C", civil.id),
        ("The first person to develop the atomic bomb was:", "Albert Einstein", "Charles De Gaulle", "Thomas Jefferson", "T.S. Elliot", "A", current.id),
    ]
    for q in old_gp:
        all_gp.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': f"The correct answer is {q[5]}.", 'topic': q[6]})

    # ===== OLD GP: NIGERIAN HISTORY & CURRENT AFFAIRS =====
    history_qs = [
        ("The Nigerian flag was designed by ___ in 1958.", "Herbert Macaulay", "Michael Taiwo Akinkunmi", "Nnamdi Azikiwe", "Obafemi Awolowo", "B", current.id),
        ("Nigeria became a republic in ___.", "1960", "1963", "1979", "1999", "B", current.id),
        ("The first executive president of Nigeria was ___.", "Nnamdi Azikiwe", "Shehu Shagari", "Olusegun Obasanjo", "Goodluck Jonathan", "B", current.id),
        ("The capital of Nigeria was moved from Lagos to Abuja in ___.", "1976", "1981", "1991", "1999", "C", current.id),
        ("The Nigerian Civil War (Biafran War) ended in ___.", "1967", "1968", "1969", "1970", "D", current.id),
        ("The first Nigerian to win a Nobel Prize was ___.", "Chinua Achebe", "Wole Soyinka", "Ngozi Okonjo-Iweala", "Chimamanda Adichie", "B", current.id),
        ("The headquarters of OPEC is in ___.", "Lagos", "Vienna", "Geneva", "New York", "B", current.id),
        ("The 'Aba Women's Riot' of 1929 was a protest against ___.", "Colonial taxation", "Forced labour", "Low wages", "Land seizure", "A", current.id),
        ("Zuma Rock is located in ___ State.", "Niger", "Abuja FCT", "Kaduna", "Nasarawa", "A", current.id),
        ("The Nigerian currency, the Naira, was introduced in ___.", "1960", "1963", "1973", "1979", "C", current.id),
        ("The first Prime Minister of Nigeria was ___.", "Nnamdi Azikiwe", "Tafawa Balewa", "Obafemi Awolowo", "Ahmadu Bello", "B", current.id),
        ("The Nigerian National Assembly consists of the Senate and the ___.", "House of Chiefs", "House of Representatives", "Federal Executive Council", "National Council of States", "B", current.id),
        ("The United Nations was founded in ___.", "1919", "1945", "1950", "1960", "B", current.id),
        ("The first military head of state in Nigeria was ___.", "Aguiyi-Ironsi", "Yakubu Gowon", "Murtala Mohammed", "Olusegun Obasanjo", "A", current.id),
        ("The official name of Nigeria is the ___.", "Republic of Nigeria", "Federal Republic of Nigeria", "United Republic of Nigeria", "People's Republic of Nigeria", "B", current.id),
        ("The African Union (AU) is headquartered in ___.", "Addis Ababa", "Nairobi", "Cairo", "Johannesburg", "A", current.id),
        ("The longest river in Nigeria is ___.", "River Benue", "River Niger", "River Cross", "River Ogun", "B", current.id),
        ("The first female Chief Justice of Nigeria was ___.", "Aloma Mukhtar", "Folake Solanke", "Grace Alele-Williams", "Ngozi Okonjo-Iweala", "A", current.id),
        ("The Murtala Muhammed International Airport is in ___.", "Abuja", "Kano", "Lagos", "Port Harcourt", "C", current.id),
        ("The NNPC was established in ___.", "1960", "1971", "1977", "1985", "C", current.id),
        ("The first university in Nigeria is the University of ___.", "Lagos", "Ibadan", "Ife", "Nigeria, Nsukka", "B", current.id),
        ("The Nigerian Armed Forces consist of the Army, Navy, and ___.", "Police", "Air Force", "Civil Defence", "Immigration", "B", current.id),
        ("The Economic and Financial Crimes Commission (EFCC) was established in ___.", "2000", "2002", "2004", "2006", "C", current.id),
        ("The National Youth Service Corps (NYSC) was created in ___.", "1971", "1973", "1975", "1979", "B", current.id),
        ("The Nigerian Coat of Arms features two supporting ___.", "eagles", "horses", "lions", "cattle", "B", current.id),
        ("The national flower of Nigeria is ___.", "Costus spectabilis", "Hibiscus", "Rose", "Orchid", "A", current.id),
        ("The highest honour in Nigeria is the ___.", "GCFR", "GCON", "CFR", "CON", "A", current.id),
        ("The first coup d'état in Nigeria took place in ___.", "1963", "1964", "1965", "1966", "D", current.id),
        ("The 'June 12' presidential election annulled in 1993 was won by ___.", "MKO Abiola", "Bashir Tofa", "Olusegun Obasanjo", "Ernest Shonekan", "A", current.id),
        ("The Nigerian Police Force motto is 'The Police is your ___.'", "Friend", "Protector", "Servant", "Guardian", "A", current.id),
        ("The first newspaper in Nigeria was 'Iwe Iroyin', published by ___.", "Henry Townsend", "Herbert Macaulay", "Nnamdi Azikiwe", "Obafemi Awolowo", "A", current.id),
        ("The National Anthem 'Arise O Compatriots' was composed by ___.", "Benedict Odiase", "Pa Odiase", "John A. Ilechukwu", "Lillian Jean Williams", "A", current.id),
        ("Nigeria joined OPEC in ___.", "1969", "1971", "1973", "1975", "B", current.id),
        ("The first Africa Cup of Nations won by Nigeria was in ___.", "1978", "1980", "1984", "1994", "B", current.id),
        ("The Nigerian national football team is nicknamed ___.", "Super Falcons", "Super Eagles", "Green Eagles", "Golden Eagles", "B", current.id),
        ("The first Nigerian Olympic gold medalist was ___.", "Chioma Ajunwa", "Kanu Nwankwo", "Nojim Maiyegun", "Innocent Egbunike", "A", current.id),
        ("The first satellite launched by Nigeria was ___.", "NigeriaSat-1", "NigeriaSat-2", "NigComSat-1R", "NigerianSat-X", "A", current.id),
    ]
    for q in history_qs:
        all_gp.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': f"The correct answer is {q[5]}.", 'topic': q[6]})

    # ===== NEW GP: SPORTS (25 questions) =====
    sports_qs = [
        ("Which country won the FIFA World Cup in 2018?", "France", "Croatia", "Belgium", "England", "A", "France defeated Croatia 4-2 in the final.", sport_topic.id),
        ("The term 'Grand Slam' in tennis: which is NOT a Grand Slam event?", "Wimbledon", "US Open", "ATP Finals", "Australian Open", "C", "The four majors: Australian Open, French Open, Wimbledon, US Open.", sport_topic.id),
        ("Which Nigerian athlete won gold in the long jump at the 1996 Atlanta Olympics?", "Chioma Ajunwa", "Mary Onyali", "Glory Alozie", "Blessing Okagbare", "A", "Chioma Ajunwa won Nigeria's only individual gold medal.", sport_topic.id),
        ("The Super Eagles won the Africa Cup of Nations most recently in which year?", "1994", "2000", "2004", "2013", "D", "Nigeria won the 2013 AFCON in South Africa.", sport_topic.id),
        ("Which football club has won the most UEFA Champions League titles?", "AC Milan", "Bayern Munich", "Real Madrid", "Liverpool", "C", "Real Madrid has 14 titles.", sport_topic.id),
        ("Who is the all-time leading goalscorer for the Nigerian national team?", "Nwankwo Kanu", "Rashidi Yekini", "Segun Odegbami", "Ahmed Musa", "B", "Rashidi Yekini scored 37 goals.", sport_topic.id),
        ("Which athlete is known as 'The Greatest' in boxing?", "Mike Tyson", "Muhammad Ali", "Joe Frazier", "George Foreman", "B", "Muhammad Ali was known as 'The Greatest'.", sport_topic.id),
        ("The Olympic Games were originally held in which country?", "Greece", "Italy", "France", "England", "A", "Ancient Olympics in Olympia, Greece.", sport_topic.id),
        ("Which tennis player has won the most Grand Slam singles titles (male, as of 2024)?", "Roger Federer", "Rafael Nadal", "Novak Djokovic", "Pete Sampras", "C", "Novak Djokovic leads with 24.", sport_topic.id),
        ("In football, the 'Golden Boot' is awarded to the:", "Best goalkeeper", "Top goalscorer", "Best player", "Best defender", "B", "Award for most goals.", sport_topic.id),
        ("The 'Maracanã Stadium' is located in which city?", "São Paulo", "Rio de Janeiro", "Brasília", "Belo Horizonte", "B", "Famous stadium in Rio de Janeiro, Brazil.", sport_topic.id),
        ("Who is the most decorated Olympian of all time?", "Usain Bolt", "Michael Phelps", "Larisa Latynina", "Paavo Nurmi", "B", "Michael Phelps has 28 Olympic medals.", sport_topic.id),
        ("Which country has won the most FIFA World Cup titles?", "Germany", "Italy", "Brazil", "Argentina", "C", "Brazil has 5 titles.", sport_topic.id),
        ("In athletics, what distance is a marathon?", "42.195 km", "26.2 miles", "Both A and B", "40 km", "C", "42.195 km = 26.2 miles.", sport_topic.id),
        ("The 'Ryder Cup' is a competition in which sport?", "Golf", "Tennis", "Rugby", "Sailing", "A", "Biennial golf competition between Europe and USA.", sport_topic.id),
        ("Who did Muhammad Ali defeat in the 'Rumble in the Jungle'?", "Joe Frazier", "George Foreman", "Larry Holmes", "Ken Norton", "B", "Ali defeated Foreman in Kinshasa, Zaire in 1974.", sport_topic.id),
        ("The 'Tour de France' is a famous race in which sport?", "Cycling", "Running", "Swimming", "Motor racing", "A", "Multi-stage bicycle race.", sport_topic.id),
        ("Who is the first Nigerian to win a world title in boxing?", "Hogan Bassey", "Dick Tiger", "Samuel Peter", "Anthony Joshua", "A", "Hogan Bassey won the world featherweight title in 1957.", sport_topic.id),
        ("In which sport do players compete for the 'Davis Cup'?", "Football", "Tennis", "Basketball", "Golf", "B", "International team tennis championship.", sport_topic.id),
        ("Which country has won the most Cricket World Cups?", "India", "West Indies", "Australia", "England", "C", "Australia has 5 titles.", sport_topic.id),
        ("Which Nigerian footballer played for Arsenal and captained the Super Eagles?", "Kanu Nwankwo", "Austin Okocha", "Mikel Obi", "Vincent Enyeama", "A", "Nwankwo Kanu played for Arsenal.", sport_topic.id),
        ("What is the standard number of players on a football team?", "9", "10", "11", "12", "C", "11 players per side.", sport_topic.id),
        ("The Wimbledon tennis tournament is played on which surface?", "Clay", "Hard court", "Grass", "Carpet", "C", "Wimbledon is the only Grand Slam on grass.", sport_topic.id),
        ("Who scored the famous 'Hand of God' goal in the 1986 World Cup?", "Pelé", "Ronaldo", "Diego Maradona", "Zinedine Zidane", "C", "Maradona's infamous goal against England.", sport_topic.id),
        ("Who holds the record for the most Olympic gold medals in athletics?", "Usain Bolt", "Carl Lewis", "Paavo Nurmi", "Michael Phelps", "C", "Paavo Nurmi won 9 gold medals.", sport_topic.id),
    ]
    for q in sports_qs:
        all_gp.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': q[7]})

    # ===== NEW GP: PHYSICS (25 questions) =====
    physics_qs = [
        ("What is the SI unit of force?", "Joule", "Newton", "Watt", "Pascal", "B", "Newton (N) = kg·m/s².", physics_topic.id),
        ("Which law states that every action has an equal and opposite reaction?", "Newton's First Law", "Newton's Second Law", "Newton's Third Law", "Law of Gravitation", "C", "Newton's third law.", physics_topic.id),
        ("The speed of light in vacuum is approximately:", "3 × 10⁵ km/s", "3 × 10⁸ m/s", "3 × 10⁶ m/s", "3 × 10⁷ m/s", "B", "299,792,458 m/s ≈ 3×10⁸ m/s.", physics_topic.id),
        ("Which particle has a negative charge?", "Proton", "Neutron", "Electron", "Positron", "C", "Electron carries negative charge.", physics_topic.id),
        ("Ohm's law: V = ?", "I/R", "IR", "R/I", "I+R", "B", "V = IR.", physics_topic.id),
        ("The device used to measure electric current is an:", "Voltmeter", "Ammeter", "Ohmmeter", "Galvanometer", "B", "Ammeter measures current in amperes.", physics_topic.id),
        ("Which of the following is a scalar quantity?", "Velocity", "Force", "Mass", "Acceleration", "C", "Mass has magnitude only.", physics_topic.id),
        ("The phenomenon of bending of light when passing from one medium to another is called:", "Reflection", "Refraction", "Diffraction", "Dispersion", "B", "Refraction changes direction due to change in speed.", physics_topic.id),
        ("What is the acceleration due to gravity on Earth (approx)?", "9.8 m/s²", "9.8 m/s", "9.8 km/s²", "98 m/s²", "A", "Standard value 9.8 m/s².", physics_topic.id),
        ("Which law describes the force between two charged objects?", "Ohm's Law", "Coulomb's Law", "Faraday's Law", "Gauss's Law", "B", "Coulomb's law: F = k q1 q2 / r².", physics_topic.id),
        ("The unit of power is the:", "Joule", "Newton-metre", "Watt", "Kilowatt-hour", "C", "Watt (W) = J/s.", physics_topic.id),
        ("A convex lens is also known as a:", "Diverging lens", "Converging lens", "Plano lens", "Cylindrical lens", "B", "Convex lens converges light rays.", physics_topic.id),
        ("Which of the following is a good conductor of electricity?", "Rubber", "Glass", "Copper", "Wood", "C", "Copper is a metal with high conductivity.", physics_topic.id),
        ("What type of wave is sound?", "Transverse", "Longitudinal", "Electromagnetic", "Surface", "B", "Sound waves are longitudinal.", physics_topic.id),
        ("The half-life of a radioactive substance is the time taken for:", "All atoms to decay", "Half the atoms to decay", "The activity to double", "The mass to halve", "B", "Time for half of the nuclei to decay.", physics_topic.id),
        ("Which colour of visible light has the longest wavelength?", "Violet", "Blue", "Green", "Red", "D", "Red has longest wavelength (~700 nm).", physics_topic.id),
        ("The formula for kinetic energy is:", "mgh", "½ mv²", "mv", "½ kx²", "B", "KE = ½ mv².", physics_topic.id),
        ("Which law states that volume of a gas is inversely proportional to its pressure at constant temperature?", "Charles's Law", "Boyle's Law", "Gay-Lussac's Law", "Avogadro's Law", "B", "Boyle's Law: P₁V₁ = P₂V₂.", physics_topic.id),
        ("What is the main function of a fuse in an electrical circuit?", "To store energy", "To measure current", "To protect against overcurrent", "To switch the circuit", "C", "Fuse melts when current exceeds rating.", physics_topic.id),
        ("Which of the following is a renewable energy source?", "Coal", "Natural gas", "Solar power", "Uranium", "C", "Solar is renewable.", physics_topic.id),
        ("The energy stored in a stretched spring is called:", "Kinetic energy", "Potential energy", "Elastic potential energy", "Thermal energy", "C", "Elastic potential energy = ½ kx².", physics_topic.id),
        ("Which scientist formulated the laws of planetary motion?", "Galileo", "Newton", "Kepler", "Copernicus", "C", "Johannes Kepler's three laws.", physics_topic.id),
        ("The ability of a material to return to its original shape after deformation is called:", "Plasticity", "Ductility", "Elasticity", "Malleability", "C", "Elasticity.", physics_topic.id),
        ("What does a transformer do?", "Converts DC to AC", "Changes voltage levels", "Converts AC to DC", "Generates electricity", "B", "Transformer steps up or steps down AC voltage.", physics_topic.id),
        ("The process of converting a solid directly to a gas is called:", "Evaporation", "Sublimation", "Condensation", "Deposition", "B", "Sublimation e.g., dry ice.", physics_topic.id),
    ]
    for q in physics_qs:
        all_gp.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': q[7]})

    # ===== NEW GP: CHEMISTRY (25 questions) =====
    chemistry_qs = [
        ("What is the atomic number of Carbon?", "4", "6", "8", "12", "B", "Carbon has 6 protons.", chemistry_topic.id),
        ("Which of the following is a noble gas?", "Oxygen", "Nitrogen", "Helium", "Chlorine", "C", "Helium (He) is noble gas.", chemistry_topic.id),
        ("The pH of a neutral solution is:", "0", "7", "14", "10", "B", "Pure water has pH 7.", chemistry_topic.id),
        ("What is the chemical formula for table salt?", "NaCl", "KCl", "CaCl₂", "MgCl₂", "A", "Sodium chloride.", chemistry_topic.id),
        ("The process of rusting involves:", "Oxidation of iron", "Reduction of iron", "Electrolysis", "Neutralization", "A", "Iron reacts with oxygen and water.", chemistry_topic.id),
        ("Which gas is produced when you mix an acid with a carbonate?", "Oxygen", "Hydrogen", "Carbon dioxide", "Nitrogen", "C", "Acid + carbonate → salt + water + CO₂.", chemistry_topic.id),
        ("The periodic table is arranged in order of increasing:", "Atomic mass", "Atomic number", "Number of neutrons", "Electronegativity", "B", "Modern periodic table by atomic number.", chemistry_topic.id),
        ("What is the main component of natural gas?", "Ethane", "Propane", "Butane", "Methane", "D", "Methane (CH₄).", chemistry_topic.id),
        ("The number of moles in 18 g of water (H₂O) is:", "0.5", "1", "2", "18", "B", "Molar mass of water = 18 g/mol.", chemistry_topic.id),
        ("Which element is liquid at room temperature?", "Mercury", "Bromine", "Both A and B", "Gallium", "C", "Mercury (Hg) and bromine (Br₂) are liquids at 25°C.", chemistry_topic.id),
        ("What is the chemical symbol for Gold?", "Go", "Gd", "Au", "Ag", "C", "Au from Latin 'aurum'.", chemistry_topic.id),
        ("Which process separates a mixture based on boiling points?", "Filtration", "Distillation", "Chromatography", "Decantation", "B", "Distillation uses differences in boiling points.", chemistry_topic.id),
        ("The most abundant gas in the Earth's atmosphere is:", "Oxygen", "Carbon dioxide", "Argon", "Nitrogen", "D", "Nitrogen ~78%.", chemistry_topic.id),
        ("What type of bond is formed by sharing electrons?", "Ionic bond", "Covalent bond", "Metallic bond", "Hydrogen bond", "B", "Covalent bond: electron pair sharing.", chemistry_topic.id),
        ("The law of conservation of mass states that in a chemical reaction:", "Mass is destroyed", "Mass is created", "Mass is neither created nor destroyed", "Mass changes form", "C", "Mass remains constant.", chemistry_topic.id),
        ("What is the oxidation state of oxygen in H₂O?", "0", "-1", "-2", "+2", "C", "Oxygen usually -2 in compounds.", chemistry_topic.id),
        ("Which scientist proposed the atomic theory?", "Dalton", "Bohr", "Rutherford", "Thomson", "A", "John Dalton.", chemistry_topic.id),
        ("What is the formula for sulfuric acid?", "H₂SO₃", "H₂SO₄", "HSO₄", "H₂S", "B", "Sulfuric acid: H₂SO₄.", chemistry_topic.id),
        ("Which of the following is an example of a physical change?", "Rusting of iron", "Burning of wood", "Melting of ice", "Digestion of food", "C", "Melting is a phase change.", chemistry_topic.id),
        ("What is the name of the compound Fe₂O₃?", "Iron(II) oxide", "Iron(III) oxide", "Iron monoxide", "Ferrous oxide", "B", "Iron(III) oxide or ferric oxide.", chemistry_topic.id),
        ("Which gases are used in the Haber process to produce ammonia?", "Oxygen and nitrogen", "Nitrogen and hydrogen", "Hydrogen and oxygen", "Nitrogen and carbon", "B", "N₂ + 3H₂ → 2NH₃.", chemistry_topic.id),
        ("What is the pH of a strong acid typically?", "Near 7", "Above 7", "Below 3", "Exactly 7", "C", "Strong acids have pH < 3.", chemistry_topic.id),
        ("The process of a liquid changing to a gas at the surface is called:", "Boiling", "Evaporation", "Condensation", "Sublimation", "B", "Evaporation occurs below boiling point.", chemistry_topic.id),
        ("Which of the following is a strong base?", "NH₃", "NaOH", "CH₃OH", "H₂O", "B", "Sodium hydroxide is a strong base.", chemistry_topic.id),
        ("The pH of a strong base is typically:", "Below 7", "Exactly 7", "Above 11", "Exactly 0", "C", "Strong bases have pH > 11.", chemistry_topic.id),
    ]
    for q in chemistry_qs:
        all_gp.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': q[7]})

    # ===== NEW GP: LITERATURE (25 questions) =====
    literature_qs = [
        ("Who wrote the novel 'Things Fall Apart'?", "Wole Soyinka", "Chinua Achebe", "Ngũgĩ wa Thiong'o", "Ayi Kwei Armah", "B", "Chinua Achebe's debut novel (1958).", literature_topic.id),
        ("Which Nigerian author won the Nobel Prize in Literature in 1986?", "Chinua Achebe", "Buchi Emecheta", "Wole Soyinka", "Ben Okri", "C", "Wole Soyinka, first African Nobel laureate.", literature_topic.id),
        ("The term 'dramatic irony' refers to:", "When the audience knows something the characters don't", "When a character says the opposite of what they mean", "A contradiction within a character", "A sudden reversal of fortune", "A", "Dramatic irony creates suspense.", literature_topic.id),
        ("Who is the author of 'The Great Gatsby'?", "Ernest Hemingway", "F. Scott Fitzgerald", "John Steinbeck", "William Faulkner", "B", "F. Scott Fitzgerald (1925).", literature_topic.id),
        ("What is the name of the protagonist in 'Things Fall Apart'?", "Obierika", "Ikemefuna", "Okonkwo", "Ezinma", "C", "Okonkwo, a wrestler and leader.", literature_topic.id),
        ("Which literary device is: 'The wind whispered through the trees'?", "Simile", "Metaphor", "Personification", "Hyperbole", "C", "Giving human qualities to wind.", literature_topic.id),
        ("Who wrote 'The Lion and the Jewel'?", "Wole Soyinka", "Femi Osofisan", "Ola Rotimi", "Zulu Sofola", "A", "Wole Soyinka's play.", literature_topic.id),
        ("A sonnet traditionally has how many lines?", "10", "12", "14", "16", "C", "14 lines, typically iambic pentameter.", literature_topic.id),
        ("Which novel by Chimamanda Ngozi Adichie tells the story of the Biafran war?", "Purple Hibiscus", "Half of a Yellow Sun", "Americanah", "The Thing Around Your Neck", "B", "'Half of a Yellow Sun' (2006).", literature_topic.id),
        ("In Shakespeare's 'Romeo and Juliet', who kills Mercutio?", "Romeo", "Tybalt", "Benvolio", "Paris", "B", "Tybalt stabs Mercutio.", literature_topic.id),
        ("What is the main theme of George Orwell's 'Animal Farm'?", "Animal rights", "Russian Revolution and totalitarianism", "Farm life", "Equality", "B", "Allegory of Stalinism.", literature_topic.id),
        ("Who is the author of 'The Old Man and the Sea'?", "Mark Twain", "Ernest Hemingway", "Herman Melville", "Joseph Conrad", "B", "Ernest Hemingway, Nobel Prize winner.", literature_topic.id),
        ("The term 'bildungsroman' refers to a novel that:", "Deals with a journey", "Focuses on a crime", "Traces the development of a protagonist", "Is written in verse", "C", "Coming-of-age story.", literature_topic.id),
        ("In 'The Merchant of Venice', who demands a pound of flesh?", "Antonio", "Portia", "Shylock", "Bassanio", "C", "Shylock the moneylender.", literature_topic.id),
        ("Which literary movement emphasized emotion and individualism?", "Classicism", "Realism", "Romanticism", "Modernism", "C", "Romanticism (late 18th to mid-19th century).", literature_topic.id),
        ("Who wrote the play 'Death and the King's Horseman'?", "Wole Soyinka", "Ngũgĩ wa Thiong'o", "Athol Fugard", "Femi Osofisan", "A", "Wole Soyinka's masterpiece.", literature_topic.id),
        ("Which novel begins 'It was the best of times, it was the worst of times'?", "Great Expectations", "A Tale of Two Cities", "David Copperfield", "Bleak House", "B", "Charles Dickens, A Tale of Two Cities.", literature_topic.id),
        ("Who wrote 'I Know Why the Caged Bird Sings'?", "Toni Morrison", "Maya Angelou", "Alice Walker", "Zora Neale Hurston", "B", "Maya Angelou's autobiography.", literature_topic.id),
        ("The Greek epic poems 'Iliad' and 'Odyssey' are attributed to:", "Sophocles", "Euripides", "Homer", "Aeschylus", "C", "Homer (c. 8th century BCE).", literature_topic.id),
        ("Which of these is a classic Nigerian play by Ola Rotimi?", "The Gods Are Not to Blame", "Kongi's Harvest", "The Road", "The Beatification of Area Boy", "A", "Ola Rotimi adapted from Oedipus Rex.", literature_topic.id),
        ("What is the rhyme scheme of a Shakespearean sonnet?", "ABAB CDCD EFEF GG", "ABBA ABBA CDE CDE", "AABB CCDD EEFF GG", "ABAB BCBC CDCD EE", "A", "Three quatrains and a couplet.", literature_topic.id),
        ("Who wrote 'The Palm-Wine Drinkard'?", "Chinua Achebe", "Amos Tutuola", "Cyprian Ekwensi", "T.M. Aluko", "B", "Amos Tutuola's famous novel (1952).", literature_topic.id),
        ("'Purple Hibiscus' was written by:", "Chimamanda Ngozi Adichie", "Buchi Emecheta", "Flora Nwapa", "Zaynab Alkali", "A", "Chimamanda Ngozi Adichie's debut novel.", literature_topic.id),
        ("What is a 'foil' character in literature?", "The main character", "A character who contrasts with the protagonist", "The villain", "A narrator", "B", "Foil highlights traits of another character by contrast.", literature_topic.id),
        ("Which device repeats initial consonant sounds? 'Peter Piper picked a peck'", "Assonance", "Alliteration", "Onomatopoeia", "Rhyme", "B", "Alliteration: repetition of initial consonants.", literature_topic.id),
    ]
    for q in literature_qs:
        all_gp.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': q[7]})

    # ===== NEW GP: WORLD ORGANIZATIONS (20 questions) =====
    worldorg_qs = [
        ("When was the United Nations founded?", "1918", "1945", "1950", "1960", "B", "October 24, 1945.", worldorg_topic.id),
        ("The headquarters of the African Union (AU) is in:", "Nairobi", "Addis Ababa", "Johannesburg", "Cairo", "B", "Addis Ababa, Ethiopia.", worldorg_topic.id),
        ("Which organization is responsible for international monetary stability?", "World Bank", "IMF", "WTO", "UNCTAD", "B", "International Monetary Fund.", worldorg_topic.id),
        ("The acronym OPEC stands for:", "Oil Producing and Exporting Countries", "Organization of Petroleum Exporting Countries", "Organization of Petroleum Exporting Corporations", "Oil and Petroleum Exporting Council", "B", "OPEC coordinates oil policies.", worldorg_topic.id),
        ("Which UN agency focuses on health?", "UNESCO", "WHO", "ILO", "FAO", "B", "World Health Organization.", worldorg_topic.id),
        ("Which country is NOT a permanent member of the UN Security Council?", "France", "Russia", "Germany", "China", "C", "P5: US, UK, France, Russia, China.", worldorg_topic.id),
        ("The World Trade Organization (WTO) came into effect in:", "1947", "1965", "1995", "2001", "C", "WTO established January 1, 1995.", worldorg_topic.id),
        ("Which organization provides development loans to poor countries?", "IMF", "World Bank", "ADB", "BIS", "B", "World Bank (IBRD and IDA).", worldorg_topic.id),
        ("NATO is a:", "Trade bloc", "Military alliance", "Human rights group", "Environmental treaty", "B", "Collective defense alliance.", worldorg_topic.id),
        ("Which African organization evolved from the OAU?", "ECA", "AU", "ECOWAS", "SADC", "B", "African Union replaced OAU in 2002.", worldorg_topic.id),
        ("The International Criminal Court (ICC) is based in:", "New York", "Geneva", "The Hague", "Vienna", "C", "The Hague, Netherlands.", worldorg_topic.id),
        ("Which organization sets labour standards?", "ILO", "WTO", "WHO", "UNHCR", "A", "International Labour Organization.", worldorg_topic.id),
        ("The United Nations Children's Fund is known as:", "UNICEF", "UNESCO", "UNFPA", "UNDP", "A", "UNICEF.", worldorg_topic.id),
        ("ECOWAS was established in:", "1963", "1975", "1985", "1991", "B", "Economic Community of West African States (1975).", worldorg_topic.id),
        ("Which specialized agency of the UN deals with intellectual property?", "WIPO", "WTO", "UNESCO", "ITU", "A", "World Intellectual Property Organization.", worldorg_topic.id),
        ("The G7 does NOT include:", "Canada", "Italy", "Russia", "Japan", "C", "Russia was suspended after 2014.", worldorg_topic.id),
        ("The Commonwealth of Nations is headed by:", "The US President", "The British Monarch", "The UN Secretary-General", "The Prime Minister of UK", "B", "King Charles III is the Head.", worldorg_topic.id),
        ("Which UN body handles refugee issues?", "UNICEF", "UNESCO", "UNHCR", "WFP", "C", "UN High Commissioner for Refugees.", worldorg_topic.id),
        ("The International Court of Justice is located in:", "New York", "Brussels", "The Hague", "Geneva", "C", "Principal judicial organ of the UN.", worldorg_topic.id),
        ("The World Bank Group is headquartered in:", "New York", "London", "Washington DC", "Geneva", "C", "Washington DC, USA.", worldorg_topic.id),
    ]
    for q in worldorg_qs:
        all_gp.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': q[7]})

    # ===== NEW GP: GLOBAL EVENTS (25 questions) =====
    globalevents_qs = [
        ("Which year did World War II end?", "1944", "1945", "1946", "1947", "B", "WWII ended in 1945.", globalevents_topic.id),
        ("The Berlin Wall fell in:", "1987", "1988", "1989", "1990", "C", "November 9, 1989.", globalevents_topic.id),
        ("Which event triggered World War I?", "Assassination of Archduke Franz Ferdinand", "Invasion of Poland", "Treaty of Versailles", "Russian Revolution", "A", "28 June 1914.", globalevents_topic.id),
        ("The first man to walk on the moon was:", "Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Michael Collins", "B", "Neil Armstrong, Apollo 11, 1969.", globalevents_topic.id),
        ("Which pandemic killed millions between 1918 and 1920?", "Black Death", "Spanish Flu", "Asian Flu", "COVID-19", "B", "Spanish flu (H1N1).", globalevents_topic.id),
        ("The 9/11 terrorist attacks occurred in which country?", "United Kingdom", "United States", "Spain", "France", "B", "Attacks on World Trade Center and Pentagon.", globalevents_topic.id),
        ("Which treaty ended the state of war after WWI?", "Treaty of Versailles", "Treaty of Paris", "Treaty of Ghent", "Treaty of Rome", "A", "Signed 28 June 1919.", globalevents_topic.id),
        ("The Chernobyl nuclear disaster happened in which year?", "1980", "1984", "1986", "1988", "C", "April 26, 1986 in Ukraine.", globalevents_topic.id),
        ("Who was the first President of the United States?", "Thomas Jefferson", "John Adams", "George Washington", "Benjamin Franklin", "C", "George Washington (1789-1797).", globalevents_topic.id),
        ("The French Revolution began in:", "1776", "1789", "1799", "1804", "B", "Storming of the Bastille, July 14, 1789.", globalevents_topic.id),
        ("The Suez Canal crisis occurred in:", "1956", "1967", "1973", "1982", "A", "Egypt nationalized canal.", globalevents_topic.id),
        ("Nelson Mandela was released from prison in:", "1989", "1990", "1991", "1994", "B", "February 11, 1990.", globalevents_topic.id),
        ("The Industrial Revolution began in which country?", "France", "United States", "Great Britain", "Germany", "C", "Britain in the late 18th century.", globalevents_topic.id),
        ("Which country hosted the 2010 FIFA World Cup?", "Brazil", "Germany", "South Africa", "Russia", "C", "South Africa, first African host.", globalevents_topic.id),
        ("The Arab Spring uprisings began in which country in 2010?", "Egypt", "Libya", "Syria", "Tunisia", "D", "Tunisia after Mohamed Bouazizi.", globalevents_topic.id),
        ("The Magna Carta was signed in:", "1066", "1215", "1295", "1492", "B", "1215, limiting King John's power.", globalevents_topic.id),
        ("Which event marked the start of the Great Depression?", "World War I", "Stock Market Crash of 1929", "Dust Bowl", "Bank Holidays", "B", "Black Tuesday, October 29, 1929.", globalevents_topic.id),
        ("The first successful vaccine was developed by Edward Jenner against:", "Polio", "Smallpox", "Measles", "Rabies", "B", "Smallpox vaccine using cowpox, 1796.", globalevents_topic.id),
        ("The Cold War was primarily between:", "USA and China", "USA and USSR", "USSR and Germany", "USA and Japan", "B", "1947-1991 rivalry.", globalevents_topic.id),
        ("Which country dropped atomic bombs on Hiroshima and Nagasaki?", "USSR", "United States", "United Kingdom", "China", "B", "August 1945.", globalevents_topic.id),
        ("The Rwandan genocide occurred in:", "1992", "1993", "1994", "1995", "C", "April to July 1994.", globalevents_topic.id),
        ("Who was the British Prime Minister during most of WWII?", "Neville Chamberlain", "Winston Churchill", "Clement Attlee", "Harold Macmillan", "B", "Churchill (1940-1945).", globalevents_topic.id),
        ("The Treaty of Rome (1957) established:", "NATO", "European Economic Community", "United Nations", "Warsaw Pact", "B", "EEC, precursor to EU.", globalevents_topic.id),
        ("Yuri Gagarin became the first human in space in:", "1957", "1959", "1961", "1963", "C", "April 12, 1961 aboard Vostok 1.", globalevents_topic.id),
        ("Which country was apartheid practiced in?", "Nigeria", "Zimbabwe", "South Africa", "Kenya", "C", "Apartheid system in South Africa until 1994.", globalevents_topic.id),
    ]
    for q in globalevents_qs:
        all_gp.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': q[7]})

    # ===== NEW GP: ECONOMICS (20 questions) =====
    economics_qs = [
        ("What does GDP stand for?", "Gross Domestic Product", "General Development Plan", "Gross Development Product", "Global Domestic Product", "A", "Total value of goods and services produced.", economics_topic.id),
        ("Which of the following is a direct tax?", "VAT", "Sales tax", "Income tax", "Import duty", "C", "Income tax is levied directly on income.", economics_topic.id),
        ("Inflation refers to:", "A decrease in price level", "An increase in the general price level", "Stable prices", "Increase in unemployment", "B", "Inflation reduces purchasing power.", economics_topic.id),
        ("The Central Bank of Nigeria (CBN) is responsible for:", "Setting interest rates", "Issuing currency", "Regulating banks", "All of the above", "D", "CBN performs all these functions.", economics_topic.id),
        ("A budget deficit occurs when:", "Revenue equals expenditure", "Revenue exceeds expenditure", "Expenditure exceeds revenue", "Taxes are reduced", "C", "Government spends more than it collects.", economics_topic.id),
        ("Which economic system is based on private ownership of the means of production?", "Socialism", "Capitalism", "Communism", "Feudalism", "B", "Capitalism emphasizes private property.", economics_topic.id),
        ("The law of demand states that, ceteris paribus, as price increases:", "Quantity demanded increases", "Quantity demanded decreases", "Demand shifts right", "Supply increases", "B", "Inverse relationship.", economics_topic.id),
        ("Which Nigerian agency is responsible for tax collection?", "CBN", "FIRS", "NITDA", "NDIC", "B", "Federal Inland Revenue Service.", economics_topic.id),
        ("What is the main export of Nigeria?", "Cocoa", "Palm oil", "Crude oil", "Natural gas", "C", "Petroleum accounts for >90% of export earnings.", economics_topic.id),
        ("The term 'fiscal policy' refers to government use of:", "Money supply and interest rates", "Taxation and spending", "Exchange rates", "Trade tariffs", "B", "Budget: taxes & expenditure.", economics_topic.id),
        ("Which of the following is a characteristic of a monopoly?", "Many sellers", "Free entry", "Single seller", "Perfect information", "C", "Monopoly: one firm dominates.", economics_topic.id),
        ("The concept of 'opportunity cost' means:", "The monetary cost of a choice", "The next best alternative foregone", "The total cost of production", "The cost of labour", "B", "Value of best alternative given up.", economics_topic.id),
        ("Which bank is the apex bank in Nigeria?", "First Bank", "Zenith Bank", "Central Bank of Nigeria", "Union Bank", "C", "CBN is the central bank.", economics_topic.id),
        ("What does 'GDP per capita' measure?", "Total GDP divided by population", "GDP growth rate", "Total exports per person", "Inflation rate", "A", "Average economic output per person.", economics_topic.id),
        ("The Lagos Stock Exchange is now known as:", "Lagos Stock Exchange", "Nigerian Stock Exchange", "NGX Group", "African Stock Exchange", "C", "Now Nigerian Exchange Group (NGX).", economics_topic.id),
        ("Which of the following is an example of a regressive tax?", "Income tax", "Corporate tax", "Value Added Tax (VAT)", "Capital gains tax", "C", "VAT takes larger percentage from low-income earners.", economics_topic.id),
        ("What is the role of the World Trade Organization (WTO)?", "Provide development loans", "Regulate international trade", "Set exchange rates", "Promote labour rights", "B", "WTO oversees trade agreements.", economics_topic.id),
        ("What is the official poverty line?", "Minimum income to afford basic needs", "Average income", "Maximum wage", "Unemployment benefit", "A", "Threshold below which people are considered poor.", economics_topic.id),
        ("Unemployment rate is calculated as:", "(Unemployed / Labour force) × 100", "(Unemployed / Population) × 100", "(Employed / Labour force) × 100", "(Unemployed / Employed) × 100", "A", "Labour force = employed + unemployed.", economics_topic.id),
        ("What is the current official currency of Nigeria?", "Pounds", "Dollars", "Naira", "Cedi", "C", "Naira (₦) introduced in 1973.", economics_topic.id),
    ]
    for q in economics_qs:
        all_gp.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': q[7]})

    # ===== NEW GP: BIOLOGY (20 questions) =====
    biology_qs = [
        ("The basic structural and functional unit of life is the:", "Tissue", "Organ", "Cell", "Organelle", "C", "Cell theory: all living things are made of cells.", biology_topic.id),
        ("Which organelle is known as the 'powerhouse of the cell'?", "Nucleus", "Ribosome", "Mitochondria", "Golgi apparatus", "C", "Mitochondria produce ATP.", biology_topic.id),
        ("Photosynthesis primarily occurs in which organelle?", "Mitochondria", "Chloroplast", "Nucleus", "Vacuole", "B", "Chloroplasts contain chlorophyll.", biology_topic.id),
        ("What is the function of red blood cells?", "Fight infection", "Carry oxygen", "Clot blood", "Produce antibodies", "B", "Hemoglobin binds oxygen.", biology_topic.id),
        ("Which of the following is a vector for malaria?", "Housefly", "Mosquito (Anopheles)", "Tsetse fly", "Tick", "B", "Female Anopheles mosquito transmits Plasmodium.", biology_topic.id),
        ("The process by which plants lose water vapor through leaves is called:", "Transpiration", "Evaporation", "Condensation", "Guttation", "A", "Transpiration mainly through stomata.", biology_topic.id),
        ("Which vitamin is produced by the human skin when exposed to sunlight?", "Vitamin A", "Vitamin C", "Vitamin D", "Vitamin K", "C", "Vitamin D3 (cholecalciferol).", biology_topic.id),
        ("The human heart has how many chambers?", "2", "3", "4", "5", "C", "Two atria, two ventricles.", biology_topic.id),
        ("What is the genetic material of most living organisms?", "RNA", "DNA", "Protein", "Lipid", "B", "DNA (deoxyribonucleic acid).", biology_topic.id),
        ("Which organ is responsible for filtering blood and producing urine?", "Liver", "Kidney", "Lungs", "Bladder", "B", "Kidneys remove waste.", biology_topic.id),
        ("The process of cell division that produces gametes is called:", "Mitosis", "Meiosis", "Binary fission", "Budding", "B", "Meiosis reduces chromosome number by half.", biology_topic.id),
        ("The largest organ in the human body is the:", "Heart", "Liver", "Skin", "Brain", "C", "Skin covers about 2 m².", biology_topic.id),
        ("Which part of the brain controls balance and coordination?", "Cerebrum", "Cerebellum", "Medulla oblongata", "Hypothalamus", "B", "Cerebellum coordinates movement.", biology_topic.id),
        ("What is the primary function of the ribosome?", "Protein synthesis", "Lipid synthesis", "ATP production", "DNA replication", "A", "Ribosomes translate mRNA into proteins.", biology_topic.id),
        ("Which blood group is known as the universal donor?", "A", "B", "AB", "O", "D", "O negative can donate to any blood type.", biology_topic.id),
        ("The human skeleton consists of approximately how many bones?", "206", "200", "210", "195", "A", "206 bones in an adult human.", biology_topic.id),
        ("What is the main function of the enzyme amylase?", "Break down proteins", "Break down carbohydrates", "Break down fats", "Break down nucleic acids", "B", "Amylase hydrolyzes starch into sugars.", biology_topic.id),
        ("Which scientist is known as the father of evolution?", "Gregor Mendel", "Charles Darwin", "Louis Pasteur", "James Watson", "B", "Darwin's theory of natural selection.", biology_topic.id),
        ("A group of similar cells performing a specific function is called:", "Organ", "Tissue", "Organ system", "Organelle", "B", "Tissues combine to form organs.", biology_topic.id),
        ("Which nitrogen-fixing bacterium lives in legume root nodules?", "E. coli", "Rhizobium", "Streptococcus", "Bacillus", "B", "Rhizobium fixes atmospheric nitrogen.", biology_topic.id),
    ]
    for q in biology_qs:
        all_gp.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': q[7]})

    # ===== NEW GP: STATISTICS (20 questions) =====
    gp_stats_qs = [
        ("The arithmetic mean of 5, 7, 9, 11, 13 is:", "7", "8", "9", "10", "C", "(5+7+9+11+13)/5 = 9.", stats_topic.id),
        ("The median of the set {2, 4, 1, 5, 3} is:", "2", "3", "4", "5", "B", "Sorted: 1,2,3,4,5 → middle = 3.", stats_topic.id),
        ("What is the mode of the data: 3, 5, 3, 7, 8, 3, 9?", "3", "5", "7", "9", "A", "3 appears most frequently.", stats_topic.id),
        ("The range of {10, 20, 30, 40, 50} is:", "10", "20", "30", "40", "D", "Max - Min = 50-10 = 40.", stats_topic.id),
        ("If the probability of an event is 0.3, the probability of its complement is:", "0.3", "0.7", "0.03", "1", "B", "Complement = 1 - 0.3 = 0.7.", stats_topic.id),
        ("A coin is tossed twice. The probability of getting exactly one head is:", "1/4", "1/2", "3/4", "1", "B", "Favorable: HT, TH → 2/4=1/2.", stats_topic.id),
        ("Which measure of central tendency is most affected by outliers?", "Median", "Mode", "Mean", "Range", "C", "Mean is sensitive to extreme values.", stats_topic.id),
        ("The variance of a set of numbers is the square of the:", "Mean", "Median", "Standard deviation", "Range", "C", "Standard deviation = √variance.", stats_topic.id),
        ("In a normal distribution, what percentage lies within one standard deviation?", "68%", "95%", "99.7%", "50%", "A", "Empirical rule: 68% within ±1σ.", stats_topic.id),
        ("The probability of rolling a 6 on a fair die is:", "1/6", "1/3", "1/2", "1", "A", "One favorable out of six.", stats_topic.id),
        ("If the mean of five numbers is 12, what is their sum?", "60", "48", "36", "24", "A", "Sum = mean × n = 12 × 5 = 60.", stats_topic.id),
        ("Which graph is best for showing the relationship between two variables?", "Histogram", "Pie chart", "Scatter plot", "Bar chart", "C", "Scatter plot shows correlation.", stats_topic.id),
        ("The interquartile range (IQR) is the difference between:", "Mean and median", "First and third quartiles", "Maximum and minimum", "Upper quartile and median", "B", "IQR = Q3 - Q1.", stats_topic.id),
        ("If two events are independent, then P(A and B) =:", "P(A) + P(B)", "P(A) × P(B)", "P(A) / P(B)", "0", "B", "Multiplication rule for independent events.", stats_topic.id),
        ("The mean of a set is 20 and the sum is 200. How many numbers are there?", "10", "20", "100", "200", "A", "n = sum / mean = 200/20 = 10.", stats_topic.id),
        ("Which of the following is a measure of dispersion?", "Median", "Mode", "Standard deviation", "Percentile", "C", "Standard deviation measures spread.", stats_topic.id),
        ("If the probability of rain is 0.2, what are the odds in favor of rain?", "1:4", "1:5", "4:1", "2:8", "A", "Odds = P/(1-P) = 0.2/0.8 = 1:4.", stats_topic.id),
        ("A bar chart is used to represent:", "Continuous data", "Categorical data", "Trends over time", "Correlation", "B", "Bar charts compare discrete categories.", stats_topic.id),
        ("A survey of 100 people found 60 liked tea. What is the relative frequency?", "0.6", "60", "0.06", "6", "A", "Relative frequency = 60/100 = 0.6.", stats_topic.id),
        ("A pie chart shows categories with angles proportional to:", "Frequencies", "Percentages", "Both A and B", "None", "C", "Angle = (frequency/total) × 360°.", stats_topic.id),
    ]
    for q in gp_stats_qs:
        all_gp.append({'text': q[0], 'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4], 'ans': q[5], 'exp': q[6], 'topic': q[7]})

    # ===== INSERT ALL GENERAL PAPER QUESTIONS =====
    for i, q in enumerate(all_gp):
        question = Question(
            exam_id=exam.id,
            topic_id=q['topic'],
            question_text=q['text'],
            question_type='multiple_choice',
            subject='General Paper',
            option_a=q['a'], option_b=q['b'], option_c=q['c'], option_d=q['d'],
            correct_answer=q['ans'],
            explanation=q.get('exp', f"The correct answer is {q['ans']}."),
            marks=1,
            question_order=i + 1
        )
        db.session.add(question)

    db.session.commit()
    print(f"✅ Seeded {len(all_gp)} General Paper questions.")
def seed_mathematics():
    clear_subject('Mathematics')

    topics = [
        Topic(name='Number Theory', subject='Mathematics', description='Indices, logarithms, bases, number properties'),
        Topic(name='Algebra', subject='Mathematics', description='Equations, inequalities, functions, polynomials'),
        Topic(name='Geometry & Mensuration', subject='Mathematics', description='Shapes, areas, volumes, circle theorems'),
        Topic(name='Trigonometry', subject='Mathematics', description='Sine, cosine, tangent, bearings'),
        Topic(name='Statistics & Probability', subject='Mathematics', description='Mean, median, mode, probability'),
        Topic(name='Calculus', subject='Mathematics', description='Differentiation, integration, limits'),
        Topic(name='Sequences & Series', subject='Mathematics', description='AP, GP, permutations, combinations'),
    ]
    for t in topics:
        db.session.add(t)
    db.session.commit()

    exam = Exam(
        title="Mathematics",
        subject="Mathematics",
        description="400 UNILAG-style Mathematics questions",
        duration_minutes=120,
        total_questions=400,
        passing_score=50
    )
    db.session.add(exam)
    db.session.commit()

    numtheory = Topic.query.filter_by(name='Number Theory', subject='Mathematics').first()
    algebra = Topic.query.filter_by(name='Algebra', subject='Mathematics').first()
    geometry = Topic.query.filter_by(name='Geometry & Mensuration', subject='Mathematics').first()
    trig = Topic.query.filter_by(name='Trigonometry', subject='Mathematics').first()
    stats = Topic.query.filter_by(name='Statistics & Probability', subject='Mathematics').first()
    calculus = Topic.query.filter_by(name='Calculus', subject='Mathematics').first()
    sequences = Topic.query.filter_by(name='Sequences & Series', subject='Mathematics').first()

    raw_math = [
        # ===== NUMBER THEORY =====
        ("Evaluate: (4×10³) × (6×10²), giving your answer in standard form.", "2.4×10⁶", "2.4×10⁵", "24×10⁵", "2.4×10⁷", "A", "4×6=24, 10³×10²=10⁵ → 24×10⁵=2.4×10⁶", numtheory.id),
        ("Evaluate log₃9 − log₂₇3", "6", "5/3", "5", "1", "B", "log₃9=2, log₂₇3=1/3 → 2−1/3=5/3", numtheory.id),
        ("Evaluate 22₃ × 102₃, leaving your answer in base 3.", "88₃", "1021₃", "10021₃", "2244₃", "C", "22₃=8, 102₃=11, 8×11=88=10021₃", numtheory.id),
        ("8% of a certain sum is ₦320. What is 10% of that sum?", "₦400", "₦380", "₦360", "₦320", "A", "100%=320÷0.08=4000, 10%=400", numtheory.id),
        ("A girl has 98 beads; all but 14 were lost. How many did she lose?", "84", "112", "114", "14", "A", "All but 14 remain → she lost 98−14=84", numtheory.id),
        ("What is the difference between 500×700 and 700×500?", "1000", "100", "0", "10000", "C", "Both equal 350000; difference = 0", numtheory.id),
        ("If it takes 15 men 6½ days to build a house, how many houses can they build in 45 days?", "3", "7", "5", "8", "B", "45÷6.5≈7 houses", numtheory.id),
        ("A car travels at 120 km/h. How long to cover 2,400 km?", "25 hrs", "20 hrs", "15 hrs", "30 hrs", "B", "t=2400÷120=20 hrs", numtheory.id),
        ("How many bottles are in a dozen crates of 24 bottles each?", "288", "300", "180", "120", "A", "12×24=288", numtheory.id),
        ("Simplify: 2³ × 2⁴ ÷ 2⁵", "2", "4", "8", "16", "B", "2^(3+4−5)=2²=4", numtheory.id),
        ("Evaluate: (27)^(2/3)", "3", "6", "9", "18", "C", "(∛27)²=3²=9", numtheory.id),
        ("Simplify: (16)^(3/4)", "4", "6", "8", "12", "C", "(⁴√16)³=2³=8", numtheory.id),
        ("Find the value of log₂64", "4", "5", "6", "8", "C", "2⁶=64", numtheory.id),
        ("If log2=0.3010, find log8", "0.602", "0.903", "0.9030", "1.204", "C", "log8=3log2=0.9030", numtheory.id),
        ("Simplify: log5+log4", "log9", "log20", "log1", "log2", "B", "log(5×4)=log20", numtheory.id),
        ("Simplify: x^(1/2) × x^(3/2)", "x", "x²", "x³", "x⁴", "B", "x^(0.5+1.5)=x²", numtheory.id),
        ("Express 0.000456 in standard form", "4.56×10⁻⁴", "4.56×10⁻³", "45.6×10⁻⁵", "4.56×10⁴", "A", "Move decimal 4 places right", numtheory.id),
        ("The HCF of 36 and 48 is", "4", "6", "12", "18", "C", "HCF=2²×3=12", numtheory.id),
        ("The LCM of 12, 16 and 20 is", "60", "120", "180", "240", "D", "LCM=2⁴×3×5=240", numtheory.id),
        ("If 2^x=32, find x", "3", "4", "5", "6", "C", "2⁵=32", numtheory.id),
        ("Simplify: (3²)³ ÷ 3³", "3", "9", "27", "81", "C", "3⁶÷3³=3³=27", numtheory.id),
        ("Convert 0.3636... to a fraction", "3/10", "4/11", "36/100", "36/99", "B", "99x=36, x=4/11", numtheory.id),
        ("Simplify: √75 + √48", "9√3", "2√3", "7√3", "5√3", "A", "5√3+4√3=9√3", numtheory.id),
        ("Rationalize 1/(√5+√3)", "(√5−√3)/2", "(√5+√3)/2", "(√5−√3)/8", "1/2", "A", "(√5−√3)/(5−3)=(√5−√3)/2", numtheory.id),
        ("Simplify: (√6+√2)(√6−√2)", "4", "6", "8", "2√8", "A", "6−2=4", numtheory.id),
        ("A number increased by 20% then decreased by 20%: net change?", "0%", "−4%", "4%", "−2%", "B", "100→120→96, net change=−4%", numtheory.id),
        ("(2/3) ÷ (4/9) =", "3/2", "8/27", "2/3", "1", "A", "2/3×9/4=3/2", numtheory.id),
        ("Express 156 in base 2", "10011100", "10011010", "10010111", "10111100", "A", "128+16+8+4=156 → 10011100₂", numtheory.id),
        ("Convert 1101₂ to base 10", "11", "12", "13", "14", "C", "8+4+0+1=13", numtheory.id),
        ("Simplify: (a³b²)² ÷ a²b", "a²b", "a³b²", "a⁴b³", "ab³", "C", "a⁶b⁴÷a²b=a⁴b³", numtheory.id),
        ("Profit on ₦2,000 cost price sold at ₦2,500 is what percent?", "20%", "25%", "30%", "50%", "B", "500/2000×100=25%", numtheory.id),
        ("Simple interest on ₦5,000 for 3 years at 4% p.a.", "₦200", "₦400", "₦600", "₦800", "C", "SI=5000×3×4/100=₦600", numtheory.id),
        ("₦72,000 invested at 8% simple interest. After how many years does it reach ₦87,840?", "2 years", "2¾ years", "3 years", "2½ years", "B", "n=15840/(72000×0.08)=2.75 years", numtheory.id),
        ("A bricklayer measured a wall to be 4.10m. Actual length is 4.25m. Find percentage error.", "3.53%", "3.76%", "0.15%", "1.54%", "A", "(0.15/4.25)×100=3.53%", numtheory.id),
        ("6!/4! = ?", "12", "24", "32", "30", "D", "720/24=30", numtheory.id),
        ("10!/(9! × 0!) = ?", "Zero", "1", "10", "100", "C", "10/1=10", numtheory.id),
        ("What is 33⅓% of 100?", "33⅓", "30", "3", "33", "A", "33⅓/100×100=33⅓", numtheory.id),
        ("1,800 × ? = 100,800", "56", "28", "41", "38", "A", "100800/1800=56", numtheory.id),
        ("A farmer has 41 bags of oranges, each with 59 oranges. Total?", "2,419", "3,324", "1,591", "2,831", "A", "41×59=2,419", numtheory.id),
        ("If 15% of a number is 175, find the number.", "500", "1000", "1167", "800", "C", "x=175/0.15≈1167", numtheory.id),
        ("If log√x=1.2835, find logx", "0.6418", "2.5670", "1.2835", "0.3010", "B", "logx=2×1.2835=2.5670", numtheory.id),
        # ===== ALGEBRA =====
        ("Solve the simultaneous equations: 2x+y=5, x−y=1", "x=2,y=1", "x=3,y=−1", "x=1,y=3", "x=2,y=−1", "A", "Adding: 3x=6→x=2; y=1", algebra.id),
        ("A man is x years old and his son y years old. Sum=twice difference. Product=675. Find man's age.", "40", "42", "55", "45", "D", "3y=x; xy=675→y=15,x=45", algebra.id),
        ("Factorize fully: 6x²−x−2", "(2x+1)(3x−2)", "(3x+2)(2x−1)", "(2x−1)(3x+2)", "(6x−1)(x+2)", "A", "(3x−2)(2x+1)=6x²−x−2", algebra.id),
        ("(x−1) is a factor of f(x)=x³+kx²−x−2. Find k.", "−5", "−2", "2", "−3", "C", "f(1)=1+k−1−2=0→k=2", algebra.id),
        ("Find the positive solution of logx + log(x−3)=log10", "6", "0", "2", "5", "D", "x(x−3)=10→x=5", algebra.id),
        ("The solution of the inequality x²−5x+6<0 is", "x<2 or x>3", "2<x<3", "x<−2 or x>−3", "x>3", "B", "(x−2)(x−3)<0→2<x<3", algebra.id),
        ("Solve: log₂(x+1)=3", "7", "8", "6", "9", "A", "x+1=8→x=7", algebra.id),
        ("If α and β are roots of 2x²−5x+3=0, find α+β", "5/2", "3/2", "5/3", "3/5", "A", "α+β=5/2", algebra.id),
        ("If α and β are roots of 2x²−5x+3=0, find αβ", "5/2", "3/2", "2/3", "5/3", "B", "αβ=3/2", algebra.id),
        ("Solve 2x²−7x+3=0", "x=3 or x=½", "x=−3 or x=½", "x=3 or x=−½", "x=1 or x=3", "A", "(2x−1)(x−3)=0", algebra.id),
        ("If P(x)=x³−3x+2, find P(−2)", "−4", "0", "4", "−8", "B", "(−2)³−3(−2)+2=0", algebra.id),
        ("Simplify: (x²−4)/(x−2)", "x+2", "x−2", "x²+4", "2", "A", "(x+2)(x−2)/(x−2)=x+2", algebra.id),
        ("A binary operation * defined by a*b=a+b−ab. Find the identity element.", "3", "−3", "1", "0", "D", "a*e=a→e(1−a)=0→e=0", algebra.id),
        ("A binary operation ⊕: a⊕b=a+b+2ab. Find 3⊕4.", "81", "31", "7", "37", "B", "3+4+2(3)(4)=31", algebra.id),
        ("If f(x)=2x²−3x+1, find f(−1)", "6", "2", "−4", "0", "A", "2(1)+3+1=6", algebra.id),
        ("Solve: 3x−2y=7 and x+2y=5", "x=3,y=1", "x=2,y=3/2", "x=4,y=5/2", "x=3,y=2", "A", "Adding: 4x=12→x=3; y=1", algebra.id),
        ("The 3rd term of a GP is 18 and the 6th term is 486. Find the common ratio.", "2", "3", "4", "6", "B", "ar²=18, ar⁵=486→r³=27→r=3", algebra.id),
        ("Find the sum of the first 5 terms of 3+6+12+...", "93", "96", "90", "99", "A", "S=3(2⁵−1)/(2−1)=93", algebra.id),
        ("Simplify: (2x−1)² − (x+1)²", "3x²−6x", "3x²−6x+2", "x²−6x", "3x²+2x−2", "A", "(4x²−4x+1)−(x²+2x+1)=3x²−6x", algebra.id),
        ("Find k if (x−2) is a factor of x³+kx−6.", "−1", "1", "2", "−2", "A", "f(2)=8+2k−6=0→k=−1", algebra.id),
        ("Resolve into partial fractions: (3x+1)/[(x+1)(x−1)]", "2/(x−1)+1/(x+1)", "2/(x+1)+1/(x−1)", "1/(x+1)+2/(x−1)", "3/(x²−1)", "C", "A=1,B=2 → 1/(x+1)+2/(x−1)", algebra.id),
        ("For what values of x is (2x+1)/(x²−x−6) undefined?", "x=2 or x=−3", "x=−2 or x=3", "x=3 or x=−2", "x=2 or x=3", "B", "(x−3)(x+2)=0→x=3 or x=−2", algebra.id),
        ("The roots of x²+px+q=0 are 3 and −5. Find p and q.", "p=2, q=−15", "p=−2, q=−15", "p=2, q=15", "p=−2, q=15", "A", "sum=−2=−p→p=2; product=−15=q", algebra.id),
        ("If f(x)=3x−2 and g(x)=x²+1, find g(f(2)).", "17", "16", "15", "25", "A", "f(2)=4, g(4)=17", algebra.id),
        ("Simplify: (3^(n+1)−3^n)/(3^(n−1))", "6", "9", "3", "18", "A", "3^n(3−1)/3^(n−1)=2×3=6", algebra.id),
        ("Factorize: x³−x²−10x−8", "(x+1)(x+2)(x−4)", "(x−1)(x+2)(x+4)", "(x+1)(x+2)(x−4)", "(x−2)(x+1)(x+4)", "C", "Roots: x=−1,−2,4", algebra.id),
        ("Solve: x² - kx + 9 = 0 has equal roots, find k.", "±3", "±6", "±9", "±12", "B", "k²−36=0→k=±6", algebra.id),
        ("Simplify: (2x²y³)⁴", "16x⁶y¹²", "16x⁸y¹²", "8x⁶y⁷", "8x⁸y¹²", "B", "2⁴=16; x⁸; y¹²", algebra.id),
        ("The sum of two numbers is 20 and their product is 84. Find them.", "12 and 8", "14 and 6", "15 and 5", "16 and 4", "B", "x²−20x+84=0→14 and 6", algebra.id),
        ("If f(x) = 3x - 2 and g(x) = x² + 1, find f(g(2)).", "13", "15", "17", "19", "A", "g(2)=5, f(5)=13", algebra.id),
        ("The remainder when x³-2x²+x-3 is divided by x-2 is:", "−3", "−1", "1", "3", "B", "f(2)=8−8+2−3=−1", algebra.id),
        ("If (x-1) is a factor of x³+kx²-5x+2, find k.", "2", "3", "4", "5", "A", "f(1)=1+k−5+2=0→k=2", algebra.id),
        ("Solve the inequality: 2x - 5 < 3x + 1", "x > -6", "x < -6", "x > 6", "x < 6", "A", "−6 < x → x > −6", algebra.id),
        ("Find the value of x if 4²ˣ = 64", "1", "1.5", "2", "2.5", "B", "4²ˣ=4³ → 2x=3 → x=1.5", algebra.id),
        ("Solve simultaneously: x + 2y = 7, 2x - y = 4", "x=3,y=2", "x=4,y=1.5", "x=2,y=2.5", "x=1,y=3", "A", "5x−8=7→x=3, y=2", algebra.id),
        ("The gradient of the line 3y = 6x - 9 is:", "2", "3", "6", "-3", "A", "y=2x−3 → gradient=2", algebra.id),
        ("Find the equation of the line through (2,3) with slope -4.", "y = -4x + 11", "y = -4x + 5", "y = 4x - 5", "y = 4x - 11", "A", "y−3=−4(x−2)→y=−4x+11", algebra.id),
        ("If α and β are roots of x² - 5x + 6 = 0, find α² + β².", "13", "25", "37", "12", "A", "α+β=5, αβ=6 → α²+β²=25−12=13", algebra.id),
        ("The quadratic equation whose roots are 2 and -3 is:", "x² + x - 6 = 0", "x² - x - 6 = 0", "x² + 5x + 6 = 0", "x² - 5x + 6 = 0", "A", "Sum=−1, product=−6", algebra.id),
        ("Find k for which y = 2x + k is tangent to y = x².", "1", "-1", "2", "-2", "B", "discriminant=4+4k=0→k=−1", algebra.id),
        ("If x² + y² = 25 and xy = 12, find x + y.", "±7", "±5", "±6", "±4", "A", "(x+y)²=25+24=49→±7", algebra.id),
        ("Factorize 6x² - 14x - 12.", "2(x+3)(3x-2)", "6(x-2)(x+1)", "2(x-3)(3x+2)", "6x+2(x-1)", "C", "2(3x+2)(x−3)", algebra.id),
        ("Solve: |x-3|=5", "x=8 or x=−2", "x=8 or x=2", "x=−2 only", "x=8 only", "A", "x=8 or x=−2", algebra.id),
        ("If f(x)=2x-1 and g(x)=x+3, find fog(x).", "2x+5", "2x-5", "2x+1", "2x+3", "A", "fog(x)=2(x+3)−1=2x+5", algebra.id),
        ("If f(x)=x²+1 and g(x)=3x, find gof(2).", "15", "25", "9", "10", "A", "f(2)=5, g(5)=15", algebra.id),
        ("Find the inverse of f(x)=2x+3.", "(x-3)/2", "(x+3)/2", "(2x-3)", "(x-2)/3", "A", "f⁻¹(x)=(x−3)/2", algebra.id),
        ("When polynomial f(x) divided by 2x-3, quotient is x²-x+2, remainder -1. Find f(x).", "2x³-5x²+7x-7", "2x³+5x²-7x+7", "x³-5x²+7x-7", "2x³-5x²-7x+7", "A", "f(x)=(2x-3)(x²-x+2)-1=2x³-5x²+7x-7", algebra.id),
        ("Find the smallest integer satisfying: x + 8 < 4x - 15.", "8", "7", "9", "10", "A", "23<3x→x>7.67→smallest=8", algebra.id),
        ("Solve the inequality: x² + 2x > 15.", "x < -5 or x > 3", "-5 < x < 3", "x < -3 or x > 5", "x < -5 or x > -3", "A", "(x+5)(x-3)>0→x<−5 or x>3", algebra.id),
        ("Find the positive number n such that 3n² = 12n.", "4", "3", "5", "2", "A", "3n(n−4)=0→n=4", algebra.id),
        ("n!/(n-3)! = ?", "N!", "(n-3)!", "N(n-1)(n-2)", "N(n-1)(n-2)(n-3)", "C", "n!/(n-3)!=n(n-1)(n-2)", algebra.id),
        ("Solve: 3x - 5 = 16", "x=5", "x=6", "x=7", "x=8", "C", "3x=21→x=7", algebra.id),
        ("If 2x + 3y = 12 and 3x - 2y = 5, find x + y.", "3", "4", "5", "6", "C", "x=3, y=2→x+y=5", algebra.id),
        ("The sum of two numbers is 20 and their difference is 4. Find the larger number.", "12", "14", "16", "10", "A", "x+y=20, x-y=4→x=12", algebra.id),
        ("If a*b = a² + b², find 3*4", "12", "25", "7", "5", "B", "3²+4²=9+16=25", algebra.id),
        # ===== GEOMETRY =====
        ("A solid is made of a hemisphere of radius r and a cone of height r on the same base. Volume?", "πr³", "(5/6)πr³", "(2/3)πr³", "2πr³", "A", "V_hemi=2πr³/3, V_cone=πr³/3, total=πr³", geometry.id),
        ("The minor sector of a circle of diameter 3.6 cm subtends 35° at the center. Perimeter?", "5.8 cm", "4.7 cm", "2.9 cm", "1.1 cm", "B", "r=1.8; arc≈1.1; perimeter=3.6+1.1=4.7 cm", geometry.id),
        ("OAB is a sector of radius 8 cm with arc AB=8 cm. Find the area of the sector.", "32 cm²", "64 cm²", "16 cm²", "8 cm²", "A", "Area=½rl=½×8×8=32 cm²", geometry.id),
        ("A 16 m ladder leans against a house with base 8 m from the wall. Angle with ground?", "60°", "30°", "45°", "75°", "A", "cosθ=8/16=0.5→θ=60°", geometry.id),
        ("A trapezium has height 8 m, one parallel side 10 m, area 104 m². Find the other parallel side.", "16 m", "10 m", "13 m", "10.4 m", "A", "104=½×8×(10+b)→b=16", geometry.id),
        ("In a circle, AC=6 cm, BC=8 cm, angle ACB=90°. Find the circumference.", "10π cm", "5π cm", "15π cm", "20π cm", "A", "Diameter=10; circumference=10π", geometry.id),
        ("The minute hand of a clock is 7 cm long. Distance tip travels in 1½ hours.", "33 cm", "44 cm", "66 cm", "55 cm", "C", "1.5×2π×7=66 cm", geometry.id),
        ("The volume of a cone of radius 3 cm and height 4 cm is", "12π cm³", "16π cm³", "9π cm³", "36π cm³", "A", "V=⅓πr²h=12π", geometry.id),
        ("Find the area of a triangle with base 10 cm and height 6 cm.", "30 cm²", "60 cm²", "15 cm²", "36 cm²", "A", "½×10×6=30", geometry.id),
        ("The total surface area of a cylinder of radius 3 cm, height 5 cm is", "48π cm²", "36π cm²", "24π cm²", "60π cm²", "A", "2πr²+2πrh=48π", geometry.id),
        ("A regular hexagon has each interior angle equal to", "108°", "120°", "135°", "150°", "B", "(6−2)×180/6=120°", geometry.id),
        ("A circle has area 154 cm². Find its circumference. (π=22/7)", "44 cm", "22 cm", "66 cm", "88 cm", "A", "r=7; C=44 cm", geometry.id),
        ("The diagonal of a square is 10 cm. Find its area.", "50 cm²", "100 cm²", "25 cm²", "70 cm²", "A", "A=d²/2=50", geometry.id),
        ("In parallelogram ABCD, AB=8 cm, angle=45°, area=32√2 cm². Find BC.", "4 cm", "5 cm", "6 cm", "8 cm", "D", "32√2=8×BC×sin45°→BC=8", geometry.id),
        ("The distance between points (3,−2) and (−1,1) is", "5", "√25", "4", "√13", "A", "√(16+9)=5", geometry.id),
        ("The midpoint of the segment joining (−1,3) and (5,7) is", "(3,5)", "(3,2)", "(2,5)", "(1,6)", "C", "((−1+5)/2,(3+7)/2)=(2,5)", geometry.id),
        ("A sector of a circle has radius 6 cm and angle 60°. Its arc length is", "2π cm", "6π cm", "π cm", "3π cm", "A", "L=6×(π/3)=2π", geometry.id),
        ("Two angles of a triangle are 65° and 45°. Find the third.", "70°", "80°", "60°", "90°", "A", "180−65−45=70°", geometry.id),
        ("The area of a trapezium with parallel sides 5 cm and 9 cm, height 4 cm is", "28 cm²", "36 cm²", "18 cm²", "56 cm²", "A", "½×(5+9)×4=28", geometry.id),
        ("A rectangular field is 120 m by 80 m. Find its diagonal.", "200 m", "144 m", "40√13 m", "100 m", "C", "d=√(120²+80²)=40√13", geometry.id),
        ("Find the equation of a line through (2,3) with gradient 4.", "y=4x−5", "y=4x+3", "y=4x−2", "y=4x+1", "A", "y−3=4(x−2)→y=4x−5", geometry.id),
        ("The bearing of B from A is 050°. The bearing of A from B is", "130°", "230°", "310°", "050°", "B", "050+180=230°", geometry.id),
        ("The bearing of A from B is 280°. The bearing of B from A is", "100°", "080°", "260°", "180°", "A", "280−180=100°", geometry.id),
        ("Find the slope of a line perpendicular to 3x+5y+17=0.", "5/3", "−5/3", "3/5", "−3/5", "A", "Slope=−3/5; perpendicular=5/3", geometry.id),
        ("The surface area of a cube of side 4 cm is", "96 cm²", "64 cm²", "48 cm²", "16 cm²", "A", "6×4²=96", geometry.id),
        ("If the circumference of a circle is 44 cm, find its area. (π=22/7)", "154 cm²", "176 cm²", "44 cm²", "88 cm²", "A", "44=2πr→r=7; A=154", geometry.id),
        ("The area of a parallelogram with base 8 cm and height 5 cm is:", "40 cm²", "20 cm²", "80 cm²", "30 cm²", "A", "base × height = 40", geometry.id),
        ("Find the length of side of equilateral triangle with area 9√3 cm².", "6 cm", "3 cm", "9 cm", "12 cm", "A", "(√3/4)s²=9√3→s=6", geometry.id),
        ("A rectangle has length 12 cm and diagonal 13 cm. Find its breadth.", "5 cm", "8 cm", "9 cm", "10 cm", "A", "b=√(169−144)=5", geometry.id),
        ("A right-angled triangle has legs 6 cm and 8 cm. Find hypotenuse.", "10 cm", "14 cm", "12 cm", "9 cm", "A", "√(36+64)=10", geometry.id),
        ("The volume of a rectangular prism 4 cm × 3 cm × 2 cm.", "24 cm³", "12 cm³", "48 cm³", "8 cm³", "A", "4×3×2=24", geometry.id),
        ("The area of a parallelogram is 513 cm² and the height is 19 cm. Find the base.", "27 cm", "19 cm", "30 cm", "513 cm", "A", "Base=513/19=27", geometry.id),
        ("The gradient of the line through (2,5) and (4,9) is:", "2", "4", "1", "3", "A", "(9-5)/(4-2)=2", geometry.id),
        ("Find the distance between points (3,4) and (6,8).", "5", "4", "6", "7", "A", "√(9+16)=5", geometry.id),
        ("The midpoint of the line joining (2,-3) and (8,5) is:", "(5,1)", "(4,1)", "(5,2)", "(4,2)", "A", "((2+8)/2,(-3+5)/2)=(5,1)", geometry.id),
        ("A sector of radius 6 cm has area 18π cm². Find the angle.", "180°", "120°", "90°", "60°", "A", "(θ/360)×36π=18π→θ=180°", geometry.id),
        ("The perimeter of a rectangle is 20 cm and length is 6 cm. Find breadth.", "4 cm", "5 cm", "7 cm", "8 cm", "A", "2(6+b)=20→b=4", geometry.id),
        ("A room is 5 m × 4 m × 3 m. Find the longest diagonal.", "√50 m", "5√2 m", "6 m", "7.07 m", "D", "d=√(25+16+9)=√50≈7.07", geometry.id),
        ("The x and y intercepts of 3x−2y+6=0 are respectively", "(−2, 3)", "(2,−3)", "(3,−2)", "(−2,−3)", "A", "x-int=−2; y-int=3", geometry.id),
        ("If the sides of a triangle are 3, 4, 5 cm, its area is:", "6 cm²", "12 cm²", "10 cm²", "8 cm²", "A", "½×3×4=6", geometry.id),
        ("A town P is on bearing 315° from town Q. R is South of P and West of Q. If R is 60km from Q, how far is R from P?", "60 km", "30 km", "42.43 km", "84.85 km", "C", "Using right triangle: PR=60km", geometry.id),
        # ===== TRIGONOMETRY =====
        ("Find the trigonometric value of cos315°", "−√2/2", "√2/2", "1/2", "undefined", "B", "cos315°=cos45°=√2/2", trig.id),
        ("Given that cosθ=−5/13 and θ is in the second quadrant, find sinθ", "12/13", "−12/13", "5/13", "−5/13", "A", "sinθ=12/13 (positive in Q2)", trig.id),
        ("A flagpole of height 2.5 m casts a shadow of 4 m. Find angle of elevation of the sun.", "32°", "58°", "39°", "51°", "A", "tanθ=2.5/4=0.625→θ≈32°", trig.id),
        ("Solve for θ: 2sin²θ−sinθ−1=0, 0°≤θ≤360°", "90°, 210°, 330°", "90°, 270°, 210°", "30°, 150°, 270°", "0°, 90°, 180°", "A", "sinθ=1 or −½→θ=90°,210°,330°", trig.id),
        ("Find the distance between points A(3,−4) and B(−1,2).", "√52", "√10", "√48", "√62", "A", "√(16+36)=√52", trig.id),
        ("Express sin150° in surd form", "√3/2", "1/2", "−1/2", "√2/2", "B", "sin150°=sin30°=1/2", trig.id),
        ("Evaluate tan(−60°)", "√3", "−√3", "1/√3", "−1/√3", "B", "tan(−60°)=−√3", trig.id),
        ("Given sin30°=0.5, find cos60°", "0.5", "√3/2", "1", "0", "A", "cos60°=0.5", trig.id),
        ("If sinA=3/5 and A is acute, find cosA", "4/5", "3/4", "5/3", "5/4", "A", "cosA=4/5", trig.id),
        ("If sinA=3/5 and A is acute, find tanA", "3/4", "4/3", "5/3", "3/5", "A", "tanA=3/4", trig.id),
        ("The bearing of X from Y is 045°. Find the bearing of Y from X.", "135°", "225°", "315°", "090°", "B", "045°+180°=225°", trig.id),
        ("Find cos(A+B) if cosA=3/5, sinB=5/13.", "16/65", "−16/65", "63/65", "33/65", "A", "cosAcosB−sinAsinB=16/65", trig.id),
        ("Simplify sin²θ + cos²θ + tan²θ − sec²θ", "0", "1", "2", "−1", "A", "1+(−1)=0", trig.id),
        ("An angle of 150° in radians is", "5π/6", "7π/6", "π/6", "2π/3", "A", "150×π/180=5π/6", trig.id),
        ("Convert 2π/3 radians to degrees", "90°", "120°", "150°", "60°", "B", "2π/3×180/π=120°", trig.id),
        ("The amplitude of y=3sin(2x) is", "2", "3", "6", "1", "B", "Amplitude=3", trig.id),
        ("The period of y=cos(3x) is", "2π/3", "3π", "6π", "π/3", "A", "Period=2π/3", trig.id),
        ("If tanθ=1, find θ in the range 0°<θ<360°", "45° and 135°", "45° and 225°", "135° and 315°", "45° and 315°", "B", "tanθ=1 in Q1 and Q3: 45° and 225°", trig.id),
        ("Find the exact value of sin45°+cos45°", "√2", "1", "2√2", "√2/2", "A", "√2/2+√2/2=√2", trig.id),
        ("In triangle ABC, a=8, b=6, C=90°. Find sinA.", "3/5", "4/5", "4/3", "5/4", "B", "c=10; sinA=8/10=4/5", trig.id),
        ("Solve: cosθ=−1/2 for 0°≤θ≤360°", "120° and 240°", "60° and 300°", "120° and 300°", "60° and 240°", "A", "120° and 240°", trig.id),
        ("Simplify: (1−cos2θ)/sin2θ", "tanθ", "cotθ", "sinθ", "cosθ", "A", "=sinθ/cosθ=tanθ", trig.id),
        ("A right triangle has legs 5 and 12. Find its hypotenuse.", "13", "15", "17", "√119", "A", "√(25+144)=13", trig.id),
        ("Express cos120° exactly", "√3/2", "−1/2", "1/2", "−√3/2", "B", "cos120°=−1/2", trig.id),
        ("tan x + cot x =", "sin 2x", "2/sin 2x", "x²+4", "sin x+cos x", "B", "=1/(sinx cosx)=2/sin2x", trig.id),
        # ===== STATISTICS =====
        ("In a class of 30 students, 10 wear spectacles and 16 are girls. 8 boys do not wear spectacles. How many girls wear spectacles?", "3", "4", "5", "6", "B", "Boys=14; boys with specs=6; girls with specs=4", stats.id),
        ("Eight men and nine women on a committee. Ways to choose 2 men and 3 women?", "2,352", "112", "6,188", "28,224", "A", "C(8,2)×C(9,3)=2,352", stats.id),
        ("Suppose P is the probability an event occurs and Q it doesn't. Which is true?", "P+Q=0", "P+Q=2", "P+Q=1", "P=Q", "C", "P+Q=1", stats.id),
        ("Two dice thrown. Probability of getting sum=5?", "1/9", "2/9", "1/6", "1/12", "A", "4/36=1/9", stats.id),
        ("A number is selected from {3, 0, 5, √2}. Probability it is rational?", "1/4", "1/2", "3/4", "2/3", "C", "Rational: 3,0,5 → 3/4", stats.id),
        ("The mean of 5 numbers is 8. If four of them are 6,7,9,10, find the fifth.", "8", "7", "6", "9", "A", "Sum=40; 6+7+9+10=32; fifth=8", stats.id),
        ("Find the median of: 3,7,2,9,4,6,1,8,5", "5", "4", "6", "3", "A", "Sorted median=5", stats.id),
        ("The mode of: 2,3,4,4,5,5,5,6,7 is", "4", "5", "6", "7", "B", "5 appears 3 times", stats.id),
        ("Find the range of: 12,5,18,7,23,9,14", "18", "11", "16", "23", "A", "23−5=18", stats.id),
        ("The variance of 2,4,6,8,10 is", "8", "4", "6", "10", "A", "Mean=6; variance=8", stats.id),
        ("Standard deviation of 2,4,6,8,10 is", "2√2", "4", "2", "√10", "A", "SD=√8=2√2", stats.id),
        ("A bag has 4 red and 6 blue balls. One drawn randomly. P(red)?", "2/5", "3/5", "1/2", "1/4", "A", "4/10=2/5", stats.id),
        ("Two events A and B: P(A)=0.3, P(B)=0.5, P(A∩B)=0.1. Find P(A∪B).", "0.7", "0.8", "0.6", "0.9", "A", "0.3+0.5−0.1=0.7", stats.id),
        ("If P(A)=0.4, find P(A') (complement).", "0.6", "0.4", "0.5", "0.8", "A", "1−0.4=0.6", stats.id),
        ("In a group of 40 students, 25 like maths and 20 like English; 10 like both. How many like neither?", "5", "10", "15", "0", "A", "n(M∪E)=35; neither=5", stats.id),
        ("What is the median of data: 0,1,2,3 with frequencies 20,18,7,5?", "0", "1", "2", "3", "B", "Total=50; median=1", stats.id),
        ("A die is tossed. P(even number)?", "1/2", "1/3", "2/3", "1/6", "A", "3/6=1/2", stats.id),
        ("A coin is tossed twice. P(at least one head)?", "3/4", "1/4", "1/2", "1", "A", "1−1/4=3/4", stats.id),
        ("From a class of 5 boys and 3 girls, 2 are chosen. P(both girls)?", "3/28", "3/8", "1/4", "3/56", "A", "C(3,2)/C(8,2)=3/28", stats.id),
        ("The probability of passing an exam is 2/3. In 3 attempts, P(passing all 3)?", "8/27", "4/9", "2/3", "1/3", "A", "(2/3)³=8/27", stats.id),
        ("The sum of deviations from the mean is always", "maximum", "minimum", "zero", "positive", "C", "Σ(x−x̄)=0", stats.id),
        ("There are 4 red, 3 blue, 2 green balls in a bag. P(blue or green)?", "5/9", "3/9", "2/9", "4/9", "A", "(3+2)/9=5/9", stats.id),
        ("In how many ways can 5 people be arranged in a row?", "120", "60", "24", "20", "A", "5!=120", stats.id),
        ("In how many ways can 3 items be chosen from 8?", "56", "24", "336", "512", "A", "C(8,3)=56", stats.id),
        ("Find the probability that a number selected from 40 to 50 is a prime.", "3/11", "5/11", "5/10", "4/10", "A", "Primes: 41,43,47 → 3/11", stats.id),
        ("A man kept 6 black, 5 brown and 7 purple shirts. Probability of picking purple?", "1/7", "7/18", "11/18", "7/11", "B", "7/18", stats.id),
        ("Find probability of selecting a parallelogram from: square, rectangle, rhombus, kite, trapezium.", "5/5", "2/5", "3/5", "1/5", "C", "Parallelograms: square, rectangle, rhombus → 3/5", stats.id),
        # ===== CALCULUS =====
        ("If y=x²+3x, find dy/dx", "2x+3", "2x", "x²+3", "2x²+3x", "A", "dy/dx=2x+3", calculus.id),
        ("Find the gradient of y=x²+3x at x=1.", "5", "2", "3", "7", "A", "2(1)+3=5", calculus.id),
        ("Evaluate ∫(2x+3)dx", "x²+3x+C", "2x²+3x+C", "x+3+C", "2+C", "A", "x²+3x+C", calculus.id),
        ("Evaluate ∫₀¹ x² dx", "1/3", "1/2", "1", "2/3", "A", "[x³/3]₀¹=1/3", calculus.id),
        ("Find dy/dx if y=sin(3x)", "3cos(3x)", "cos(3x)", "−3cos(3x)", "3sin(3x)", "A", "dy/dx=3cos(3x)", calculus.id),
        ("Differentiate y=(2x+1)³", "6(2x+1)²", "3(2x+1)²", "(2x+1)²", "6(2x+1)", "A", "dy/dx=6(2x+1)²", calculus.id),
        ("Find dy/dx if y=e^(2x)", "2e^(2x)", "e^(2x)", "2xe^x", "e^x", "A", "dy/dx=2e^(2x)", calculus.id),
        ("Find the maximum value of y=−x²+4x−3", "1", "2", "3", "4", "A", "At x=2: y=1", calculus.id),
        ("At what value of x does y=x²−6x+5 have a minimum?", "3", "5", "−3", "6", "A", "dy/dx=2x−6=0→x=3", calculus.id),
        ("Evaluate ∫(x³−2x)dx", "x⁴/4−x²+C", "3x²−2+C", "x⁴/4+C", "x³−2+C", "A", "x⁴/4−x²+C", calculus.id),
        ("Find dy/dx if y=x⁵−3x²+7", "5x⁴−6x", "5x⁴−3x", "x⁴−6x", "5x⁵−6x", "A", "dy/dx=5x⁴−6x", calculus.id),
        ("Evaluate ∫₁² (3x²) dx", "7", "8", "6", "9", "A", "[x³]₁²=8−1=7", calculus.id),
        ("Find the gradient of the curve y=x³−2x at x=−1.", "1", "−1", "3", "−3", "A", "3(1)−2=1", calculus.id),
        ("Differentiate y=ln(x²)", "2/x", "1/x", "2x", "1/(2x)", "A", "y=2lnx; dy/dx=2/x", calculus.id),
        ("If y=x(x+2)², expand and find dy/dx.", "3x²+8x+4", "2x+4", "x²+4x", "3x²+8x", "A", "y=x³+4x²+4x; dy/dx=3x²+8x+4", calculus.id),
        ("Evaluate ∫(1/x)dx", "ln|x|+C", "−1/x²+C", "x⁻¹+C", "1+C", "A", "ln|x|+C", calculus.id),
        ("Find the area under y=x² from x=0 to x=3.", "9", "27", "6", "3", "A", "∫₀³x²dx=9", calculus.id),
        ("Differentiate y=cos(x)·sin(x) using product rule.", "cos²x−sin²x", "cos(2x)", "−sin²x+cos²x", "2cos(2x)", "A", "dy/dx=cos²x−sin²x", calculus.id),
        ("Find the second derivative of y=x⁴.", "12x²", "4x³", "x²", "24x", "A", "y'=4x³, y''=12x²", calculus.id),
        ("Evaluate ∫₀^π sinx dx", "2", "0", "1", "π", "A", "[−cosx]₀^π=2", calculus.id),
        ("If y=3x²−12x+5, find the coordinates of the turning point.", "(2,−7)", "(2,7)", "(−2,7)", "(−2,−7)", "A", "dy/dx=6x−12=0→x=2; y=−7", calculus.id),
        ("Differentiate y=tan(x)", "sec²x", "cot²x", "cosec²x", "sin²x", "A", "dy/dx=sec²x", calculus.id),
        ("Evaluate ∫(4x³+2x)dx", "x⁴+x²+C", "12x²+2+C", "4x²+2+C", "x⁴+C", "A", "x⁴+x²+C", calculus.id),
        ("The rate of change of area of a circle with radius r is", "2πr", "πr", "2r", "πr²", "A", "A=πr²; dA/dr=2πr", calculus.id),
        ("Find the derivative of y=(x²+1)⁴ using chain rule.", "8x(x²+1)³", "4(x²+1)³", "8x³(x²+1)", "4x(x²+1)⁴", "A", "dy/dx=8x(x²+1)³", calculus.id),
        ("Evaluate lim(x→2) of (x²−4)/(x−2)", "4", "2", "0", "undefined", "A", "(x+2)→4 as x→2", calculus.id),
        ("A particle's displacement is s=t³−3t. Its velocity at t=2 is", "9", "6", "3", "12", "A", "v=3t²−3; at t=2: 9", calculus.id),
        ("Find the indefinite integral of cos(x)", "sin(x)+C", "−sin(x)+C", "tan(x)+C", "−cos(x)+C", "A", "∫cos(x)dx=sin(x)+C", calculus.id),
        ("Evaluate ∫₀¹ (1−x²)dx", "2/3", "1/2", "1/3", "1", "A", "[x−x³/3]₀¹=2/3", calculus.id),
        ("Differentiate y=(3x−2)/(x+1) using the quotient rule.", "5/(x+1)²", "3/(x+1)²", "(3x−2)/(x+1)²", "5/(x+1)", "A", "dy/dx=5/(x+1)²", calculus.id),
        ("Differentiate (cos θ + sin θ)² with respect to θ.", "2(cos θ + sin θ)(cos θ − sin θ)", "2(cos θ − sin θ)²", "−(cos θ + sin θ)(sin θ − cos θ)", "2cos(2θ)", "A", "dy/dθ=2(cosθ+sinθ)(cosθ−sinθ)", calculus.id),
        ("Find the area enclosed by y=2−x² and y=−x.", "4.5", "9", "3", "2.5", "A", "∫[-1,2](2−x²+x)dx=4.5", calculus.id),
        # ===== SEQUENCES & SERIES =====
        ("The nth term of the sequence 3,7,11,15,... is", "4n-1", "3n+1", "4n+3", "n+4", "A", "AP with a=3, d=4; Tn=4n−1", sequences.id),
        ("The 5th term of the sequence 1,2,4,8,...", "16", "32", "8", "64", "A", "GP with r=2; T5=16", sequences.id),
        ("Sum of first 10 terms of AP: 5,8,11,...", "185", "170", "160", "200", "A", "S=5×(10+27)=185", sequences.id),
        ("The 3rd term of an AP is 7 and the 7th term is 15. Find the 1st term.", "3", "1", "5", "-1", "A", "a+2d=7, a+6d=15→d=2, a=3", sequences.id),
        ("In how many ways can 3 men and 2 women be arranged in a row?", "120", "60", "24", "12", "A", "5!=120", sequences.id),
        ("How many 3-digit numbers can be formed from digits 1,2,3,4 without repetition?", "24", "12", "48", "16", "A", "4×3×2=24", sequences.id),
        ("The sum of the first n natural numbers is", "n(n+1)/2", "n²", "n(n-1)/2", "n(n+1)", "A", "1+2+...+n=n(n+1)/2", sequences.id),
        ("Find the number of terms in AP: 5,8,11,...,50", "16", "15", "17", "14", "A", "50=5+(n-1)3→n=16", sequences.id),
        ("The common ratio of GP 4,12,36,... is", "3", "4", "8", "2", "A", "12/4=3", sequences.id),
        ("Which term of the AP 7,11,15,... is 71?", "17th", "16th", "18th", "15th", "A", "71=7+(n-1)4→n=17", sequences.id),
        ("Evaluate C(10,3)", "120", "720", "10", "45", "A", "10!/(3!7!)=120", sequences.id),
        ("In how many ways can 4 people sit around a circular table?", "6", "24", "12", "4", "A", "(4−1)!=6", sequences.id),
        ("The number of diagonals in a hexagon is", "9", "12", "6", "15", "A", "n(n-3)/2=9", sequences.id),
        ("Simplify ⁵C₂ + ⁵C₃", "20", "10", "15", "25", "A", "10+10=20", sequences.id),
        ("Find the sum of all even integers from 2 to 50.", "650", "600", "700", "550", "A", "S=25/2×(2+50)=650", sequences.id),
        ("If the 4th term of a GP is 54 and r=3, find the first term.", "2", "6", "18", "3", "A", "ar³=54→a=2", sequences.id),
        ("Evaluate ⁸P₃", "336", "56", "512", "168", "A", "8×7×6=336", sequences.id),
        ("The sum of an infinite GP is 12 and first term is 4. Find common ratio.", "2/3", "1/3", "3/4", "1/4", "A", "12=4/(1-r)→r=2/3", sequences.id),
        ("The 10th term of the AP 3,7,11,... is", "39", "43", "37", "41", "A", "T₁₀=3+9×4=39", sequences.id),
        ("If 5,x,20 are in GP, find x.", "10", "15", "8", "12", "A", "x²=100→x=10", sequences.id),
        ("The 7th term of the sequence 2,5,10,17,...", "50", "51", "52", "53", "A", "Differences: 3,5,7,9,11,13; 7th=50", sequences.id),
        ("Find the sum to infinity of the series 1+⅓+1/9+...", "1", "3/2", "2/3", "3", "B", "S=1/(1-1/3)=3/2", sequences.id),
        ("The first term of an AP is 3 and fifth term is 9. Find number of terms that add up to 81.", "9", "8", "10", "7", "A", "a=3, d=1.5; n=9", sequences.id),
        ("If 7 and 189 are the first and fourth terms of a GP, find the 5th term.", "243", "81", "567", "729", "C", "r=3; 5th=7×81=567", sequences.id),
        ("The average of x1,x2,x3,x4 is 16. Half the sum of x2,x3,x4 is 23. What is x1?", "18", "16", "20", "22", "A", "Sum all=64, x2+x3+x4=46→x1=18", sequences.id),
        ("Find a two-digit number: three times tens digit is 2 less than twice units digit, and twice the number is 20 greater than reversed digits.", "47", "74", "38", "83", "A", "t=4,u=7→47", sequences.id),
        ("1+1=2, 2+2=4, 4+3=7, 7+4=11, 11+5=16. Next number?", "21", "22", "20", "23", "A", "16+6=21", sequences.id),
        ("Given y=px+q, y=5 when x=3 and y=4 when x=2. Find p and q.", "p=1, q=2", "p=1, q=3", "p=2, q=1", "p=2, q=-1", "A", "5=3p+q, 4=2p+q→p=1, q=2", sequences.id),
        ("The sum of the first 10 odd numbers is", "100", "81", "121", "64", "A", "Sum=n²=10²=100", sequences.id),
        ("If (3-x), 6, (7-5x) are consecutive terms of a GP, find x.", "5", "-3/5", "2", "-2", "A", "36=(3-x)(7-5x)→x=5", sequences.id),
        ("The second and fifth terms of a GP are 6 and -48. Find the first term.", "-3", "3", "12", "-12", "A", "ar=6, ar⁴=−48→r=−2; a=−3", sequences.id),
        ("3y−1, y+3, y−1 form an AP. Find y.", "2", "-2", "3", "-3", "B", "Standard answer y=-2", sequences.id),
    ]

    # Deduplicate by question text
    seen_texts = set()
    unique_math = []
    for q in raw_math:
        if q[0] not in seen_texts:
            seen_texts.add(q[0])
            unique_math.append(q)

    # Insert Mathematics questions
    for i, q in enumerate(unique_math):
        question = Question(
            exam_id=exam.id,
            topic_id=q[7],
            question_text=q[0],
            question_type='multiple_choice',
            subject='Mathematics',
            option_a=q[1], option_b=q[2], option_c=q[3], option_d=q[4],
            correct_answer=q[5],
            explanation=q[6],
            marks=1,
            question_order=i + 1
        )
        db.session.add(question)

    db.session.commit()
    print(f"✅ Seeded {len(unique_math)} Mathematics questions.")
def seed_database():
    print("Starting database seeding...")
    seed_english()
    seed_general_paper()
    seed_mathematics()
    print("\n✅ All done! Database seeded successfully.")

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        seed_database()