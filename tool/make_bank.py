#!/usr/bin/env python3
"""Build assets/questions/bank.json from the practice papers in assets/."""

import json
from pathlib import Path

from deep_paper import questions as deep_questions
from more_paper import questions as more_questions
from uog_paper import questions as uog_questions

ROOT = Path(__file__).resolve().parents[1]


def Q(section, topic, stem, choices, answer, explanation, passage=None, also=None):
    item = {
        "section": section,
        "topic": topic,
        "stem": stem.strip(),
        "choices": choices,
        "answer": answer,
        "explanation": explanation.strip(),
    }
    if passage:
        item["passage"] = passage.strip()
    if also:
        item["alsoAccept"] = also
    return item


def exam(eid, title, summary, source, minutes, questions):
    out = []
    for i, question in enumerate(questions, start=1):
        question = dict(question)
        question["id"] = f"{eid}-{i}"
        out.append(question)
    return {
        "id": eid,
        "title": title,
        "summary": summary,
        "source": source,
        "minutes": minutes,
        "questions": out,
    }


MAGELLAN = """
The 16th century was an age of great land exploration. Magellan lost the favour of the king of Portugal when he became involved in a political entanglement. The Pope divided New World lands between Spain and Portugal according to their location on one side or the other of an imaginary geographical line 50 degrees west of Greenwich that extends in a north and south direction.
""".strip()

CURIE = """
Marie Curie showed intelligence by leaving Poland and traveling to France to enter the Sorbonne. Her husband, Pierre Curie, was killed in a street accident involving a horse-drawn wagon. In 1911 Marie Curie received the Nobel Prize in chemistry for isolating radium.
""".strip()

EDU = """
The purpose of education is to make the student an expert in his subject. This must be clearly understood, and mere muddling through lessons, lectures and books, and passing examinations, are relegated to secondary importance as means to an end — which is excellence in the field chosen.

But there are so many fields, and no one can become an expert in all of them. It is necessary to decide which fields are the important ones that a person should know well.

It is clear that one's own work is the most important. This has been realised, and modern civilization has accordingly provided vocational education. It is now possible to acquire high professional skill in medicine, engineering, production, commerce and so on — but with good and bad mixed together, and no standard for guidance.
""".strip()

ARISTOTLE = """
According to Aristotle, the most important question in the physical world was the search for happiness. He was not an idealist preaching impossible ideals and counsels of perfection. His scientific training made him a realist who believed that happiness was the aim of life and every activity, even ethics, was subordinate to it. He tries to explore the nature of happiness and explains it by differentiating man from other animals in that he possesses the thinking faculty by which he masters the earth and surpasses all living beings, and its development will give him fulfilment and happiness.
""".strip()

DUTY = """
A duty is an obligation. It is something we owe to others as social beings when we live together. We must let others live with us. My right of living implies my duty to my fellow men to allow them the same conditions of life. In fact, rights and duties are co-related. What is a right in regard to one is a duty in regard to others. Rights and duties are two sides of the same coin. We should always observe them from the standpoint of others. Thus they are duties. Moral duty is more effective than the legal. A moral duty is that which is laid upon people on moral grounds. It is my moral duty to help the poor because I am a member of society.

I must try to create conditions which contribute to the welfare of humanity. Similarly, I owe a duty to my parents — to be obedient and respectful to them. This duty originates from the sense of responsibility which is directly related to our conscience. So this maxim is concerned with a moral duty which a person should owe without legal bondage.

Sense of duty is paramount for the proper development of civilization. Hypocrisy and diplomacy are quite reverse to the sense of duty. Hypocrisy involves wickedness; duty involves sincerity and faithfulness.
""".strip()

DANGER = """
When we are suddenly confronted with any terrible danger, the change of nature we undergo is equally great. In some cases fear paralyses us. Like animals, we stand still, powerless to move a step in fright or to lift a hand in defence of our lives, and sometimes we are seized with panic and again act more like the inferior animals than rational beings. On the other hand, frequently in cases of sudden extreme peril, which cannot be escaped by fright and must be instantly faced, even the most timid men at once, as if by miracle, become possessed of the necessary courage, sharp quick apprehension and swift decision. This is a miracle very common in nature. Man and the inferior animals alike, when confronted with almost certain death, "gather resolution from despair", but there can really be no trace of so debilitating a feeling in the person fighting, or prepared to fight, for dear life. At such times the mind is clearer than it has ever been; the nerves are steel; there is nothing felt but a wonderful strength and daring. Looking back at certain perilous moments in my own life, I remember them with a kind of joy, not that there was any joyful excitement then, but because they brought me a new experience — a new nature, as it were — and lifted me for a time above myself.
""".strip()

ACCOUNTS = """
Because of a computer malfunction, an accountant cannot directly determine the classification of certain accounts. Each account is type 1, 2, 3, 4 or 5. Exactly four operations exist: W, X, Y and Z. No operation is performed more than once on a given account, and the operations follow these rules:

• Type 1: the computer performs either W or, alternatively, X.
• Type 2: the computer performs either X alone or X together with any one of the remaining operations except W.
• Type 3: the computer performs either Y alone or Y together with any one of the remaining operations.
• Type 4: the computer performs exactly two operations, in any combination, except that X cannot be one of them.
• Type 5: the computer performs exactly three operations, in any combination drawn from the four operations.
""".strip()

DIGNITARIES = """
Seven dignitaries — F, G, H, I, N, O and P — sit in a row of seven chairs numbered 1 to 7 from front to back. One person sits in each chair.

• F must sit in the chair immediately behind O.
• G cannot sit immediately in front of N, and G cannot sit immediately behind N.
• There must be exactly two chairs between H and P.
• There must be at least one chair between I and P.
• N must sit in chair 3.
""".strip()

SCULPTURES = """
Exactly five sculptures are displayed on stands 1 through 5. They are chosen from M, N, P, Q, R, S, T and U, one sculpture on each stand.

• Either M or U, or both, must be selected.
• If M is selected, M must be on stand 1.
• Either R or S must be on stand 3.
• If T is selected, P must also be selected, and T and P must be on stands immediately next to each other.
""".strip()

SELFISH = """
Selfishness is a principal evil in our society. Every person is concerned with only himself. Personal advancement is the only motivating force in the world today. This does not mean that individuals are not willing to help one another; on the contrary, _______. However, these are only short-term occurrences, which ultimately serve our long-term goal of personal gain.
""".strip()


def ngat_set_one():
    v, qn, lg = "Verbal", "Quantitative", "Logical"
    items = []
    A = items.append

    A(Q(v, "Analogy", "SEGREGATE : UNIFY :: repair :", ["approach", "outwit", "damage", "push"], 2,
        "Segregate is the opposite of unify. Repair is the opposite of damage."))
    A(Q(v, "Analogy", "monarch : ______ :: KING : COBRA", ["queen", "butterfly", "royal", "venom"], 1,
        "A king cobra is a kind of snake named with “king”. A monarch butterfly is the matching pair, so the missing word is butterfly."))
    A(Q(v, "Analogy", "EXECUTIONER : CRIMINAL", ["convict : murderer", "florist : flowers", "worker : manager", "butcher : animal"], 3,
        "An executioner performs his work on a criminal. A butcher performs his work on an animal."))
    A(Q(v, "Analogy", "LOATH : COERCION", ["reluctant : persuasion", "irate : antagonism", "contemplative : meditative", "irritate : caressing"], 0,
        "To be loath is to be unwilling, and coercion is forcing someone. Reluctant is the matching attitude toward persuasion."))
    A(Q(v, "Analogy", "MOON : SATELLITE", ["flowers : garland", "fishes : pond", "singer : chorus", "Earth : Planet"], 3,
        "The Moon is an example of a satellite. Earth is an example of a planet."))
    A(Q(v, "Analogy", "POETRY : RHYME :: philosophy :", ["imagery", "theory", "by-law", "music"], 1,
        "Rhyme is a characteristic feature of poetry. Theory is a characteristic feature of philosophy."))

    A(Q(v, "Word substitution", "His son is a ______, as he lost his life protecting the lives of people of this country.",
        ["soldier", "revolutionist", "philanthropist", "martyr"], 3,
        "A martyr is someone who dies for a cause or while protecting others. The defining detail is that he lost his life."))
    A(Q(v, "Word substitution", "Her schoolmates organised a house party for Sara’s birthday, but she does not get excited easily even if you put in a lot of effort and emotion. Sara is ______.",
        ["inclement", "gregarious", "placid", "frenzied"], 2,
        "Placid means calm and not easily excited. Gregarious means sociable, and frenzied means wildly excited."))
    A(Q(v, "Word substitution", "We bought a new machine to help mother with household chores. The machine can easily be carried anywhere. It is ______.",
        ["potable", "portable", "relatable", "cartable"], 1,
        "Portable means easy to carry. Potable means safe to drink."))
    A(Q(v, "Word substitution", "Mr Gupta has four wives and twelve children. He is a ______.",
        ["classicogamist", "bigamist", "polygamist", "monogamist"], 2,
        "A polygamist has more than one spouse. A bigamist has two; a monogamist has one."))
    A(Q(v, "Word substitution", "This is Peter’s first press conference. He is anxious because he speaks little. He is ______.",
        ["garrulous", "terse", "sullen", "reticent"], 3,
        "Reticent means reserved and reluctant to speak. Garrulous is the opposite, and terse means brief without the sense of anxiety."))
    A(Q(v, "Word substitution", "I cannot stay in the hospital for five minutes because I fear confined places. I have ______.",
        ["Onochlophobia", "Claustrophobia", "Agoraphobia", "Stasiphobia"], 1,
        "Claustrophobia is the fear of enclosed or confined spaces. Agoraphobia is the fear of open or crowded places."))
    A(Q(v, "Word substitution", "Sheren’s father won an award for a book about his own life. The book is an ______.",
        ["autobiography", "bibliography", "biography", "ownography"], 0,
        "An autobiography is the story of a person’s life written by that person. A biography is written by someone else."))
    A(Q(v, "Word substitution", "At the ancient palace we saw old manuscripts written by saints, but they were not clear enough to read. They were ______.",
        ["legible", "illegible", "decipherable", "negligible"], 1,
        "Illegible means impossible to read. Legible and decipherable mean the writing can be read."))
    A(Q(v, "Word substitution", "I don’t mind talking to him about the project, but he thinks only of himself. He is an ______.",
        ["boaster", "proud person", "eccentric", "egoist"], 3,
        "An egoist is concerned only with himself. A boaster talks about his achievements, which the sentence does not say."))

    A(Q(v, "Sentence completion", "Ancient Greek authors believed that literature should contain a perfect balance between the social and the personal, objectivity and ______, and ______ and emotion.",
        ["subjectivity … reason", "selectivity … passion", "subjection … rationality", "personality … sociability"], 0,
        "The sentence pairs opposites: social with personal, objectivity with subjectivity, and emotion with reason."))
    A(Q(v, "Sentence completion", "If you act ______ at their party, you won’t be asked back; they don’t want spiteful and irritating people at their affairs.",
        ["contrite", "frantic", "passionate", "splenetic"], 3,
        "Splenetic means bad-tempered, spiteful and irritable, which matches the people they do not want."))
    A(Q(v, "Sentence completion", "If you continue to skip classes and fail to complete homework, you will soon find that you have been ______ the university.",
        ["warned about", "trapped in", "invited to", "dismissed from"], 3,
        "Repeated absence and missed work lead to being dismissed, not invited or merely warned in the strongest reading of “soon find that you have been”."))
    A(Q(v, "Sentence completion", "Asegedech was so abrupt with clients that her supervisor put a letter in her file citing her ______.",
        ["lethargy", "enthusiasm", "rudeness", "diligence"], 2,
        "Abrupt treatment of clients is rudeness. The letter cites the fault, not a virtue such as diligence."))
    A(Q(v, "Sentence completion", "Hadas, a passionate woman, agreed to marry a rich, ______ neighbour even though she loved a ______, uneducated man.",
        ["educated … poor", "affluent … untutored", "indigent … impoverished", "opulent … unschooled"], 0,
        "The contrast is a rich, educated neighbour against a poor, uneducated man. The other options repeat the same idea twice."))
    A(Q(v, "Sentence completion", "This professor spent his entire life trying to ______ his students to appreciate the beauty of poetry.",
        ["encourage", "repeal", "alienate", "develop"], 0,
        "A teacher trying to bring students to appreciate poetry is encouraging them. Repeal and alienate work against that aim."))
    A(Q(v, "Sentence completion", "Hanan was known for her ______; no one was more ______ than she.",
        ["communism … conservative", "conservatism … leftist", "economy … profligate", "altruism … selfless"], 3,
        "The second description agrees with the first. Altruism and selfless say the same thing. The other pairs are opposites."))
    A(Q(v, "Sentence completion", "Alemu waited ______ for his turn, relaxing in an easy chair with his eyes closed.",
        ["warily", "impatiently", "calmly", "angrily"], 2,
        "Relaxing with closed eyes shows he waited calmly, not impatiently or angrily."))

    A(Q(v, "Grammar", "People pay little attention to what he says because ______.",
        ["he is a sociable person", "he is an honest person", "he is unreliable", "he is an agreeable person"], 2,
        "People ignore someone when they cannot trust what he says. Unreliability explains the lack of attention."))
    A(Q(v, "Grammar", "Our team scored one goal at the end of the match, but they lost. It was ______.",
        ["very late", "a little too late", "too little too late", "the final stage of the match"], 2,
        "One late goal was not enough. “Too little too late” means both insufficient and too late to change the result."))
    A(Q(v, "Grammar", "“If I had seen her, I would have told her the news” means ______.",
        ["he didn’t tell her the news", "he told her the news when he saw her", "he told her the news when he sees her", "he saw her but he didn’t tell her the news"], 0,
        "This is a third conditional about a past that did not happen. He did not see her, so he did not tell her the news."))
    A(Q(v, "Grammar", "Despite all his efforts, ______.",
        ["he never lost hope", "he was very lucky", "his success was predictable", "he was unsuccessful"], 3,
        "Despite introduces a contrast. Efforts would normally bring success, so the contrasting result is that he was unsuccessful."))
    A(Q(v, "Grammar", "I would have met the boss ______.",
        ["if I hadn’t arrived early", "had I been a bit early", "had I been late", "if he is in his office"], 1,
        "“Would have met” needs a past unreal condition. “Had I been a bit early” means he was not early, so he missed the boss."))

    A(Q(v, "Sentence meaning", "“Don’t forget to buy Monica a present.” The closest meaning is:",
        ["Monica must buy you a gift.", "I want you to remember Monica’s address.", "Monica forgot her birthday card.", "I want you to remember to buy Monica a gift."], 3,
        "The speaker is reminding you to buy the present. The request is about your memory, not Monica buying a gift."))
    A(Q(v, "Sentence meaning", "“Feyera speaks Afan Oromo and English.” The closest meaning is:",
        ["Feyera wants to learn English.", "Feyera speaks two languages.", "Feyera speaks to British people on the phone.", "Feyera is learning English."], 1,
        "Naming two languages he speaks means he is bilingual. The sentence does not say he is still learning."))
    A(Q(v, "Sentence meaning", "“Tinbit is sick and tired of her stepmother.” The closest meaning is:",
        ["Tinbit is fed up with her stepmother.", "Tinbit’s stepmother has an illness.", "Tinbit needs to take a nap.", "Tinbit is sick because she likes her stepmother."], 0,
        "“Sick and tired of” is an idiom meaning fed up with someone, not a physical illness."))
    A(Q(v, "Sentence meaning", "“Emebet is older than Fantu, but younger than Adanu.”",
        ["Emebet is the oldest.", "Emebet is the youngest.", "Adanu is the oldest.", "Fantu is older than Adanu."], 2,
        "The order from oldest to youngest is Adanu, Emebet, Fantu. Adanu is the oldest."))
    A(Q(v, "Sentence meaning", "“Hagos used to drink a lot of alcohol.”",
        ["He drinks less now.", "He is an alcoholic.", "He no longer drinks a lot of alcohol.", "He drinks a lot now."], 2,
        "“Used to” describes a past habit that has stopped. He drank a lot before and does not do so now."))
    A(Q(v, "Sentence meaning", "“Daniel can play the kirar and the piano.”",
        ["Daniel wants to play the violin instead.", "Daniel plays two instruments.", "Daniel plays the keyboard.", "Daniel only plays the piano."], 1,
        "The kirar and the piano are two instruments, so he plays two."))

    A(Q(v, "Reading", "The 16th century was an age of great ______ exploration.",
        ["mental", "land", "cosmic", "common man"], 1,
        "The passage opens by calling the 16th century an age of great land exploration.", MAGELLAN))
    A(Q(v, "Reading", "Magellan lost the favour of the king of Portugal when he became involved in a political ______.",
        ["discussion", "entanglement", "problem", "negotiation"], 1,
        "The passage says the loss of favour came from a political entanglement.", MAGELLAN))
    A(Q(v, "Reading", "The Pope’s imaginary line 50 degrees west of Greenwich extends in a ______ direction.",
        ["easterly", "crosswise", "south-east", "north and south"], 3,
        "A meridian of longitude runs north and south. The passage states that direction directly.", MAGELLAN))
    A(Q(v, "Reading", "By leaving Poland and travelling to France to enter the Sorbonne, Marie ______.",
        ["behaved badly", "was distressed", "showed intelligence", "challenged a tribe"], 2,
        "The passage presents that decision as evidence of her intelligence.", CURIE))
    A(Q(v, "Reading", "According to the passage, Pierre Curie was killed by ______.",
        ["a laboratory accident", "a horse-drawn wagon", "radiation exposure", "a tribal battle"], 1,
        "The passage says Pierre was killed in an accident involving a horse-drawn wagon.", CURIE))
    A(Q(v, "Reading", "In 1911 Marie Curie received the Nobel Prize in ______ for isolating radium.",
        ["physics", "chemistry", "medicine", "peace"], 1,
        "Her 1903 Nobel Prize was in physics; the 1911 prize, for isolating radium, was in chemistry. The passage states chemistry.", CURIE))

    A(Q(qn, "Geometry", "The total surface area of a cube is 24. What is the volume of the cube?",
        ["8", "24", "64", "16"], 0,
        "A cube has 6 faces, so 6a² = 24, a² = 4 and a = 2. The volume is a³ = 8."))
    A(Q(qn, "Geometry", "A rectangle has perimeter 54 metres. The length-to-width ratio is 5 to 4. What is the length, in metres?",
        ["27", "30", "15", "24"], 2,
        "Let the sides be 5k and 4k. Then 2(5k + 4k) = 54, so 18k = 54 and k = 3. The length is 15."))
    A(Q(qn, "Clocks", "On a 12-hour clock the time is 11:00. What is the acute angle between the hour and minute hands?",
        ["15°", "60°", "30°", "45°"], 2,
        "At 11:00 the minute hand is on 12 and the hour hand is on 11, which is 30° away. The acute angle is 30°."))
    A(Q(qn, "Numbers", "A is a two-digit number whose last digit is 3, and the difference of its digits is 6. What is A?",
        ["53", "23", "93", "63"], 2,
        "If the units digit is 3, the tens digit must be 9, because |9 − 3| = 6. The number is 93. A negative tens digit is impossible."))
    A(Q(qn, "Algebra", "If x² − y² = 2 and xy = 4, what is x⁴ + y⁴?",
        ["28", "16", "32", "36"], 3,
        "(x² + y²)² = (x² − y²)² + 4x²y² = 4 + 4(xy)² = 4 + 64 = 68. Then x⁴ + y⁴ = (x² + y²)² − 2x²y² = 68 − 2(16) = 36."))
    A(Q(qn, "Percent", "If 25 percent of a number is 1,600, what is 10 percent of the number?",
        ["400", "1,440", "40", "640"], 3,
        "The number is 1,600 ÷ 0.25 = 6,400. Ten percent of 6,400 is 640."))
    A(Q(qn, "Work rates", "X can finish a job in 15 days and Y in 20 days. What fraction remains if they work together for 8 days?",
        ["4/15", "1/20", "1/15", "1/4"], 2,
        "Together they complete 1/15 + 1/20 = 7/60 of the job per day. In 8 days they complete 56/60 = 14/15, so 1/15 remains."))
    A(Q(qn, "Mixtures", "A 10-litre solution is 20% salt. How many litres of an 8% salt solution must be added to make a 12% solution?",
        ["24", "18", "20", "15"], 2,
        "The original salt is 2 litres. If x litres of 8% solution are added, (2 + 0.08x) / (10 + x) = 0.12. Then 2 + 0.08x = 1.2 + 0.12x, so 0.8 = 0.04x and x = 20."))
    A(Q(qn, "Similar figures", "On level ground a building’s shadow is 12 m when a man’s shadow is 0.60 m. The man is 1.80 m tall. How tall is the building, in metres?",
        ["28", "32", "36", "24"], 2,
        "The triangles are similar, so height / shadow is constant. 1.80 / 0.60 = 3, and 3 × 12 = 36."))
    A(Q(qn, "Numbers", "The last digit of X is 9 and the last digit of Y is 8. Both are two-digit numbers. What is the last digit of X × Y?",
        ["2", "8", "9", "7"], 0,
        "Only the units digits matter: 9 × 8 = 72, which ends in 2."))
    A(Q(qn, "Factors", "If n = 9 × 28 × 26, which of the following is NOT an integer?",
        ["n / 36", "n / 21", "n / 32", "n / 18"], 2,
        "n = 9 × 28 × 26 = 2³ × 3² × 7 × 13. Dividing by 32 = 2⁵ needs two more factors of 2 than n has, so n/32 is not an integer. The other divisors all divide n."))
    A(Q(qn, "Inequalities", "If 0 < x < y < 1, which statement is true?",
        ["x/y > 1", "y − x > 1", "xy > 1", "y/x > 1"], 3,
        "Both numbers are positive and y is larger than x, so y/x is greater than 1. Their product and difference are each less than 1."))
    A(Q(qn, "Algebra", "Three times the third of three consecutive odd integers is 3 more than twice the sum of the first and the second. What is the sum of the three integers?",
        ["23", "21", "19", "25"], 1,
        "Let the integers be n, n+2 and n+4. Then 3(n+4) = 3 + 2(n + n+2), so 3n + 12 = 4n + 7 and n = 5. The integers are 5, 7 and 9, and their sum is 21."))
    A(Q(qn, "Geometry", "An equilateral triangle has perimeter 30 m. What is its area, in m²?",
        ["30√3", "20√3", "25√3", "5√3"], 2,
        "Each side is 10 m. Area = (√3 / 4) × side² = (√3 / 4) × 100 = 25√3."))
    A(Q(qn, "Ratio", "The sides of a triangle are in the ratio 3 : 5 : 6, and the perimeter is 70 m. What is the longest side, in metres?",
        ["25", "6", "30", "5"], 2,
        "The sides are 3k, 5k and 6k. Then 14k = 70, so k = 5 and the longest side is 30."))
    A(Q(qn, "Algebra", "The price of 2 ties and 3 shirts is Birr 2,800. The same amount buys 1 tie and 5 shirts. What is the price of 1 tie and 1 shirt?",
        ["1,400", "1,500", "1,250", "1,200"], 3,
        "2t + 3s = t + 5s = 2,800, so t = 2s. Then 4s + 3s = 2,800, s = 400 and t = 800. One of each costs 1,200."))
    A(Q(qn, "Algebra", "If p = 2/3 and r = 4, what is (p√3)^r − (p + 1/9)?",
        ["5/9", "1", "7/9", "16/9"], 1,
        "(2/3 × √3)⁴ = (2√3 / 3)⁴ = (4 × 3 / 9)² = (4/3)² = 16/9. Then p + 1/9 = 6/9 + 1/9 = 7/9, and 16/9 − 7/9 = 1."))
    A(Q(qn, "Comparison", "Quantity M is (526)² − (525)². Quantity N is 210. Which is true?",
        ["M is less than N", "M is greater than N", "M equals N", "The relationship cannot be determined"], 1,
        "(526)² − (525)² = (526 − 525)(526 + 525) = 1,051. That is greater than 210."))
    A(Q(qn, "Algebra", "What is the least value of x for which (2x + 1)(x − 2) = 0?",
        ["2", "−1/2", "−1", "−2"], 1,
        "The solutions are x = −1/2 and x = 2. The smaller value is −1/2."))
    A(Q(qn, "Algebra", "If a − b = p, what is a² − 2ab + b²?",
        ["p² + ap − b²", "2p", "p²", "p(a − b)"], 2,
        "a² − 2ab + b² is (a − b)², which equals p². Note that p(a − b) is also p², so D is numerically the same; the direct simplified form is p².",
        also=[3]))
    A(Q(qn, "Exponents", "If n = 3, what is 2^(2n) + 1?",
        ["65", "64", "33", "129"], 0,
        "2n = 6, so 2^6 + 1 = 64 + 1 = 65. The nearby traps are 2^6 = 64 and 2^7 + 1 = 129."))

    A(Q(lg, "Paradox", "A priest asks, “Do you speak to the devil and follow his biddings?” The parishioner says yes. The priest replies, “You must be lying. Nobody who is in league with the devil tells the truth.” Why is the priest’s behaviour paradoxical?",
        ["His behaviour followed religious law, but he accused the parishioner of violating it.", "He relied on the parishioner’s answer in order to reject that answer.", "He accused the parishioner, then later changed his story.", "He asked about the devil but does not believe the devil exists."], 1,
        "The priest uses the “yes” as evidence, then says anyone in league with the devil would lie. He depends on an answer that his own rule says cannot be trusted."))
    A(Q(lg, "Inference", "Turkey’s GDP rose 8.5% in 2011, but inflation was high and much of its banking system is part-owned by Eurozone banks. As the single currency falters, that dependency raises questions about the stability of Turkish growth. Which conclusion follows?",
        ["Turkish banks are European-owned mainly to help Turkey join the European Union.", "The Turkish economy was stagnant in 2011.", "European ownership was chosen to add variety to the market.", "There are concerns that Turkey’s development may falter after 2011."], 3,
        "The passage itself says the dependency raises questions about the stability of growth. It does not give a reason for the ownership, and it reports rapid growth rather than stagnation."))
    A(Q(lg, "Deduction", "Ahmed lives in a big apartment. Abay lives in a small apartment. There are no big apartments in Hawassa. Small apartments have one bedroom. Which must be true?",
        ["Abay’s apartment has one bedroom.", "Abay lives in Hawassa.", "Big apartments have one bedroom.", "Ahmed lives in Hawassa."], 0,
        "Abay lives in a small apartment, and every small apartment has one bedroom. Ahmed’s big apartment cannot be in Hawassa, but Abay’s home is not located."))
    A(Q(lg, "Percent", "About 55% of people in poverty in Ethiopia are government employees, and this is expected to reach 60% by 2025. Also, 25% of people in poverty are not government employees because they are unfit to work through age or disability. Which follows?",
        ["There are equal numbers of people in poverty and in government employment.", "55% of people are in poverty.", "20% of people in poverty are not government employees, but they are fit to work.", "The number of people in poverty will rise."], 2,
        "If 55% are government employees, 45% are not. Of that 45%, 25 percentage points are unfit, leaving 20% who are not government employees and are fit to work."))
    A(Q(lg, "Deduction", "Cleo is a good dog. Clona is a bull. Good dogs are fast and keep the house safe. Bulls do not make noise. Which must be true?",
        ["Cleo is a quiet dog.", "Clona can run very fast.", "Cleo is a fast dog.", "Clona moves every night."], 2,
        "Cleo is a good dog, and every good dog is fast. Nothing says bulls are fast or that Cleo is quiet."))
    A(Q(lg, "Assumption", "Technology companies that make tablets and smartphones should invest in making them more intuitive for elderly people. This group has not been reached and could benefit greatly. The argument depends on which assumption?",
        ["Elderly people would want to buy tablets and smartphones.", "Technology companies are already investing in this area.", "Apps for elderly people are already in development.", "Elderly people do not like new technology."], 0,
        "The recommendation only makes sense if elderly people would actually want the devices. If they would not buy them, the untapped market disappears."))
    A(Q(lg, "Assumption", "Good education is the lifeblood of the country. We need to keep class sizes from being too large by building new schools. Which is assumed?",
        ["Young pupils are a vital part of the country.", "Class sizes are too large and must be reduced.", "People work better in smaller classes.", "Schools are cheap to build."], 1,
        "Calling for new schools so that classes will not be too large assumes that classes are currently too large. The argument does not discuss building costs."))
    A(Q(lg, "Classification", "Kaliti Flour Factory has 180 employees. Factories with fewer than 200 employees are classified as small manufacturers. Therefore:",
        ["Kaliti Flour Factory is a small manufacturer.", "Kaliti Flour Factory has sizable employees.", "Kaliti Flour Factory is a big manufacturer.", "Kaliti Flour Factory is categorized as a small manufacturer."], 0,
        "180 is less than 200, so the factory meets the definition of a small manufacturer. D says the same thing in different words.",
        also=[3]))
    A(Q(lg, "Deduction", "Not everyone with a car has a licence, and not everyone with a licence owns a car. Everyone with a licence has taken the driving test. Everyone who drives on the road has a licence. Ahmed drives on the road. Therefore:",
        ["Ahmed has a driving licence.", "Ahmed owns a car.", "Ahmed has taken his driving test.", "Some drivers on the road have taken the driving test."], 2,
        "Ahmed drives, so he has a licence, and everyone with a licence has taken the test. A and D also follow; the direct conclusion about Ahmed is that he has taken the test. He need not own a car.",
        also=[0, 3]))
    A(Q(lg, "Syllogism", "There are no politicians who are not party members. There are no appointees who are not politicians. Which must be true?",
        ["All appointees are party members.", "Any party member is also an appointee.", "There is no party member who is not a politician.", "All politicians are appointees."], 0,
        "All appointees are politicians, and all politicians are party members, so all appointees are party members. The reverse claims do not follow."))
    A(Q(lg, "Syllogism", "All university teachers can teach in secondary schools. University teachers trained in Ethiopia can teach in Ethiopian universities, but not in Kenya. Which follows?",
        ["All secondary teachers can teach at university.", "A university teacher trained in Ethiopia can teach anywhere.", "A university teacher trained in Ethiopia can teach at a secondary school or a university in Ethiopia.", "All university teachers in Kenya can teach in Ethiopia."], 2,
        "A university teacher trained in Ethiopia is a university teacher, so he can teach in secondary school, and the second sentence allows him to teach in an Ethiopian university."))
    A(Q(lg, "Deduction", "Loft insulation saves on heating bills, but leaving the heating on with the windows open wastes energy. Wasting energy raises bills. Zeberga has loft insulation but regularly leaves the heating on with the windows open.",
        ["Zeberga is not wasting energy.", "Zeberga is wasting energy.", "Zeberga is saving on heating.", "Zeberga’s loft insulation does not work."], 1,
        "Leaving the heating on with the windows open is given as wasting energy, and Zeberga does that. The insulation does not cancel that stated waste."))
    A(Q(lg, "Deduction", "At Addis Ababa University everyone works 8 hours, but people start at different times. Tigist started at 9 AM, at least one hour after everyone else. Whoever leaves last must lock up. Which must be true?",
        ["Tigist started one hour before everyone else.", "Everyone in the office has to lock up.", "Everyone else started at 8 AM or earlier.", "Everyone must start work at 8 AM."], 2,
        "Tigist’s 9 AM start was at least one hour after every other person, so nobody else started after 8 AM. Only the last person to leave locks up."))
    A(Q(lg, "Syllogism", "All birds have beaks, and all sparrows are birds. Therefore:",
        ["Some sparrows must have beaks.", "All birds are sparrows.", "All sparrows must have beaks.", "Almost all sparrows must have beaks."], 2,
        "Sparrows are birds and every bird has a beak, so every sparrow has a beak. “Some” is weaker but also true.",
        also=[0]))
    A(Q(lg, "Assumption", "The family doctor said he would perform a blood test today. The patient concludes, “I know I will feel pain today.” The argument depends on which assumption?",
        ["The doctor will have trouble finding a vein.", "Using a needle always causes the patient pain.", "The doctor will have to try several needles.", "This patient has felt pain at this doctor’s office before."], 1,
        "A blood test leads to pain only if the needle used for the test is assumed to cause pain. Past visits and difficult veins are not required."))
    return items


def ngat_set_two():
    v, qn, lg = "Verbal", "Quantitative", "Logical"
    items = []
    A = items.append
    chess = "The title Grandmaster is awarded to chess players by the world chess organisation FIDE. Apart from World Champion, Grandmaster is the highest title a chess player can attain. Once achieved, the title is held for life."
    morris = "Six years ago, lawyer-banker-scholar Charles Morris wrote a prophetic book, Two Trillion Dollar Meltdown, that foresaw the 2008 Great Recession before it hit America and the world. Now Morris has reversed course and sees good times ahead. His forthcoming book, Comeback, predicts that growing U.S. energy independence will bring a rise in American manufacturing and jobs."

    A(Q(v, "Analogy", "THIGH : LEG", ["palm : hand", "thumb : finger", "tie : neck", "arm : shoulder"], 0,
        "The thigh is part of the leg. The palm is part of the hand. A thumb is a kind of finger, not part of a finger."))
    A(Q(v, "Analogy", "DILIGENCE : SUCCESS", ["excitement : stimulation", "victory : ecstasy", "vivacity : animation", "triumph : achievement"], 1,
        "Diligence can produce success, just as victory can produce ecstasy. The other pairs are closer to synonyms."))
    A(Q(v, "Analogy", "FISH : SARDINE", ["herd : cattle", "camel : hump", "cow : calf", "fowl : chicken"], 3,
        "A sardine is a kind of fish. A chicken is a kind of fowl."))
    A(Q(v, "Analogy", "PARENT : CHILD", ["couple : offspring", "father : mother", "brother : sister", "mother : cousin"], 0,
        "A parent produces a child. A couple produces offspring. The other pairs are family relations of a different kind."))
    A(Q(v, "Analogy", "DERMATOLOGY : SKIN", ["logic : reasoning", "histology : tissue", "chronology : crime", "etymology : society"], 1,
        "Dermatology is the study of skin. Histology is the study of tissue."))
    A(Q(v, "Vocabulary", "PERCEPTIBLE", ["noticeable", "trivial", "undetectable", "visible"], 0,
        "Perceptible means able to be noticed or seen. Noticeable is the closest meaning. Visible is also acceptable.",
        also=[3]))
    A(Q(v, "Vocabulary", "OFFENCE", ["congruence", "virtue", "immorality", "cruelty"], 2,
        "In this vocabulary set the choices contrast a fault with its opposite. Offence here is paired with immorality, the general moral wrong; cruelty is only one kind of offence."))
    A(Q(v, "Vocabulary", "SERENE", ["bright", "noisy", "sedentary", "quiet"], 3,
        "Serene means calm and quiet. Noisy is an antonym, and sedentary means sitting still."))
    A(Q(v, "Vocabulary", "PROHIBIT", ["encourage", "deter", "connect", "block"], 3,
        "To prohibit is to forbid or block something. Deter means to discourage, which is weaker than a prohibition."))
    A(Q(v, "Sentence completion", "There are several reasons why school uniforms must be ______ for all students.",
        ["worn", "sought", "mandatory", "found"], 0,
        "The natural completion is that uniforms must be worn. Mandatory repeats the idea of “must,” and sought or found does not fit a rule about uniforms."))
    A(Q(v, "Sentence completion", "Computer ______ can be defined as the excessive or compulsive use of the computer which persists despite serious negative ______.",
        ["browsing … functions", "addiction … consequences", "processing … applications", "programming … outlooks"], 1,
        "Compulsive use that continues despite harm is addiction, and the harm is described as negative consequences."))
    A(Q(v, "Sentence completion", "Almost every aspect of modern life has been ______ through the convenience provided by technology.",
        ["affirmed", "improved", "disjointed", "connected"], 1,
        "Convenience that touches almost every aspect of life is an improvement. Disjointed would be a loss of convenience."))
    A(Q(v, "Sentence completion", "Unlike human beings, the computer ______ repetitive calculations without getting tired or ______.",
        ["indicates … observed", "classifies … noticed", "demonstrates … stuck", "performs … bored"], 3,
        "Computers perform calculations, and the human failure they avoid is becoming bored or tired."))
    A(Q(v, "Sentence completion", "In order to succeed in class, students need to ______ the resources available to them throughout their studies.",
        ["distinguish", "clarify", "utilize", "produce"], 2,
        "Success comes from using the resources that are already available. Utilize means to put them to use."))
    A(Q(v, "Sentence completion", "It is certain that advertising is an everyday ______ of our lives.",
        ["feature", "demand", "forecast", "discussion"], 0,
        "Something present every day is a feature of daily life. A forecast or a demand is not what advertising itself is."))
    A(Q(v, "Sentence completion", "In the strictest sense, the ______ of a material would produce a ______ supply of the original.",
        ["discarding … smaller", "creation … larger", "extracting … limitless", "recycling … fresh"], 3,
        "Recycling returns used material as a fresh supply of the original kind. Discarding reduces supply rather than producing it."))
    A(Q(v, "Sentence completion", "Obesity is a medical condition in which excess body fat has ______ to the extent that it may harm health.",
        ["developed", "accumulated", "hardened", "risen"], 1,
        "The medical definition of obesity is excess body fat that has accumulated enough to affect health."))
    A(Q(v, "Grammar", "She always gets up early ______ be late for work.",
        ["in order not to", "in order to", "in order", "in order that she"], 0,
        "She gets up early for the purpose of avoiding lateness. “In order not to be late” is the complete infinitive of purpose."))
    A(Q(v, "Grammar", "She asked me if I ______ the film before.",
        ["had seen", "see", "have seen", "have had"], 0,
        "The reporting verb “asked” is past, so the earlier experience is past perfect: had seen."))
    A(Q(v, "Grammar", "The committee chose to postpone the meeting rather than ______ it that day.",
        ["has", "having", "to have", "not having"], 1,
        "After “rather than,” the gerund matches the structure used here: postpone the meeting rather than having it."))
    A(Q(v, "Grammar", "We all left the place ______ as soon as we heard the blast.",
        ["with hurry", "hurried", "hurriedly", "be in a hurry"], 2,
        "The blank modifies the verb “left,” so it needs the adverb hurriedly."))
    A(Q(v, "Grammar", "She didn’t want to stop and talk to me ______.",
        ["as she was very busy", "in spite of her busy schedule", "for I asked her", "irrespective of being busy"], 0,
        "Being busy explains why she would not stop. “In spite of her busy schedule” would mean she stopped despite being busy."))
    A(Q(v, "Reading", "According to the text, which statement is true?",
        ["World Champion is a title held for life.", "Grandmaster is a higher title than World Champion.", "World Champion is a higher title than Grandmaster.", "The title World Champion is awarded by FIDE."], 2,
        "The passage says Grandmaster is the highest title apart from World Champion, so World Champion ranks higher. Only the Grandmaster title is said to be held for life and awarded by FIDE.", chess))
    A(Q(v, "Reading", "The passage implies you should pay attention to Charles Morris because:",
        ["His predictions have come true once already.", "He’s a published author.", "The U.S. is becoming more energy independent.", "His first book was a best seller."], 0,
        "The reason to trust the new forecast is that his earlier warning about the 2008 recession came true. Being published, by itself, is not the point of the passage.", morris))

    A(Q(qn, "Percent", "In 2000 E.C. a jacket cost Birr p. The price rose 20% in each of the next years, but in 2003 it fell by 10%. What was the total percentage increase from 2000 to 2003?",
        ["34%", "30%", "30.6%", "29.6%"], 3,
        "The multipliers are 1.20 for 2001, 1.20 for 2002 and 0.90 for 2003. 1.2 × 1.2 × 0.9 = 1.296, which is a 29.6% increase."))
    A(Q(qn, "Averages", "A class has 29 students, 15 of them girls. The girls average 42 kg and the boys average 45 kg. A new student of 54 kg joins. What is the new average weight, in kg?",
        ["43.8", "43.5", "44", "47"], 0,
        "There are 14 boys. Total weight is 15×42 + 14×45 = 630 + 630 = 1,260. Adding 54 gives 1,314 kg for 30 students, and 1,314 / 30 = 43.8."))
    A(Q(qn, "Comparison", "Quantity M is (526)² − (525)². Quantity N is 210.",
        ["M is less than N", "M is greater than N", "M equals N", "The relationship cannot be determined"], 1,
        "The difference of squares is (526 − 525)(526 + 525) = 1,051, which is greater than 210."))
    A(Q(qn, "Quadratics", "What is the least value of x for which (2x + 1)(x − 2) = 0?",
        ["2", "−1/2", "−1", "−2"], 1,
        "Set each factor equal to zero: x = −1/2 or x = 2. The least is −1/2."))
    A(Q(qn, "Coordinate geometry", "Region R is where y ≤ x + 2 and y ≥ x². For a point (x, y) in R, what is the maximum of 2y − x?",
        ["6", "8", "9", "10"], 0,
        "Because the coefficient of y is positive, use the largest allowed y, which is x + 2. Then 2y − x = x + 4. The region also needs x + 2 ≥ x², so x is between −1 and 2. The maximum of x + 4 on that interval is 6, at x = 2, y = 4."))
    A(Q(qn, "Statistics", "Scores and frequencies: 2 (1), 5 (4), 6 (2), 8 (2), 10 (1). Which statement is true?",
        ["The median is the average of the mode and the mean.", "The mode is greater than the mean and the median.", "The mean, mode and median are equal.", "The mean is the average of the mode and the median."], 0,
        "The ten scores sum to 60, so the mean is 6. Ordered, the 5th and 6th scores are 5 and 6, so the median is 5.5. The mode is 5. The average of the mode and the mean is (5 + 6) / 2 = 5.5, which equals the median."))
    A(Q(qn, "Variation", "Two positive quantities are related by y = k/x, where k is constant. If x increases by 50%, what happens to y?",
        ["It decreases by 66.7%", "It decreases by 33.3%", "It decreases by 50%", "It increases by 50%"], 1,
        "The new x is 1.5 times the old x, so the new y is y/1.5 = (2/3)y. That is a decrease of one third, or about 33.3%."))
    A(Q(qn, "Approximation", "x = 10^0.3 + √0.017, 10^0.6 = 4 and √1.7 = 1.3. If y = √(x² + 2.7), which is the best approximation of y²?",
        ["6.5", "7.4", "6.7", "7.2"], 3,
        "10^0.3 = √(10^0.6) = √4 = 2. √0.017 = √(1.7/100) = 0.13. So x ≈ 2.13 and x² ≈ 4.54. Then x² + 2.7 ≈ 7.24, and y² is that sum, about 7.2."))
    A(Q(qn, "Inequality", "A man spent between one fifth and one fourth of his yearly net income on loan payments. He spent Birr 45,000. Which could have been his income?",
        ["170,000", "228,000", "222,000", "178,000"], 2,
        "Income I satisfies I/5 < 45,000 < I/4, so 180,000 < I < 225,000. Only 222,000 lies strictly inside that range."))
    A(Q(qn, "Sequences", "Which number does NOT belong in the pattern 2, 6, 12, 20, 30, 42, 56, … written in the paper as 2, 6, 12, 20, 32, 42, 56, …?",
        ["32", "56", "42", "72"], 0,
        "The pattern is n(n + 1): 2, 6, 12, 20, 30, 42, 56, 72. The listed 32 breaks the pattern; 30 belongs there. 72 is the next term, not an intruder."))
    A(Q(qn, "Surds", "Simplify √(539/242) ÷ √(189/66).",
        ["(1/7)√6", "(1/7)√3", "(1/3)√14", "(1/3)√7"], 3,
        "Combine the roots: √[(539 × 66) / (242 × 189)]. Cancel to 7/9. The square root is √7 / 3, or (1/3)√7."))
    A(Q(qn, "Algebra", "If a − b = p, what is a² − 2ab + b²?",
        ["p² + ap − b²", "2p", "p²", "p(a − b)"], 2,
        "(a − b)² = p². The choice p(a − b) equals p² as well, so both name the same value; p² is the simplified form.",
        also=[3]))
    A(Q(qn, "Geometry", "Circle O has triangle AOB with perimeter 12. OA and OB are radii, and the standard figure makes AOB equilateral. Which statement is NOT true?",
        ["The area of triangle AOB is 4√3 square units.", "The area of the circle is 12π square units.", "Triangle AOB is isosceles.", "The circumference of the circle is 8π units."], 1,
        "An equilateral triangle of perimeter 12 has side 4, so the radius is 4. Its area is (√3/4)×16 = 4√3, and it is isosceles. The circumference is 2π×4 = 8π, but the area is 16π, not 12π."))
    A(Q(qn, "Algebra", "If 4x − 2y = 8, what is 2x − y?",
        ["2", "4", "6", "8"], 1,
        "Divide every term of 4x − 2y = 8 by 2. The left side becomes 2x − y and the right side becomes 4."))
    A(Q(qn, "Sequences", "What is m in the sequence 1/2, 3/5, 8/11, 19/23, 42/47, m, …?",
        ["89/95", "76/91", "85/97", "65/87"], 0,
        "Each numerator is the previous numerator plus the previous denominator: 42 + 47 = 89. Denominator gaps double: +3, +6, +12, +24, so the next denominator is 47 + 48 = 95."))
    A(Q(qn, "Exponents", "If n = 3, what is 2^(2n) + 1?",
        ["65", "64", "33", "129"], 0,
        "2^(2×3) + 1 = 2^6 + 1 = 65."))
    A(Q(qn, "Statistics", "Using scores 2, 5, 5, 5, 5, 6, 6, 8, 8, 10, what is the population standard deviation?",
        ["√4.4", "√5.4", "√6", "√5"], 0,
        "The mean is 6. Squared deviations sum to 16 + 4(1) + 0 + 2(4) + 16 = 44. The population variance is 44/10 = 4.4, so the standard deviation is √4.4."))

    A(Q(lg, "Inference", "More than 95% of the people working in Ethio telecom know programming. Which follows?",
        ["More than 5% of them don’t know programming.", "Less than 5% of them don’t know programming.", "5% of them know nothing except programming.", "5% of them know something other than programming."], 1,
        "If more than 95% know programming, the rest are less than 5%. The statement says nothing about what else they know."))
    A(Q(lg, "Inference", "The government has allowed unsubsidized educational institutions to increase their fees. Which is the best inference?",
        ["Subsidized institutions need to increase their fees.", "Unsubsidized institutions have less money for infrastructure.", "Subsidized institutions are not the ones being allowed to raise fees.", "Unsubsidized institutions are established by rich people."], 2,
        "The permission is stated only for unsubsidized institutions. It does not say they lack money, or that subsidized institutions must raise fees."))
    A(Q(lg, "Assumption", "It is vital that we increase public spending on healthcare to keep the population in good health. Which is assumed?",
        ["Public spending on healthcare is too low.", "Public spending on healthcare is too high.", "The health of the population is already in decline.", "Public healthcare is this government’s only concern."], 0,
        "Calling an increase vital assumes the present spending is not enough. The sentence does not say health is already declining."))
    A(Q(lg, "Assumption", "In the Ethiopian context, the advisable age for a child to join kindergarten is 6 years. Which best supports that advice?",
        ["At this age, the child is ready to learn new things.", "Kindergartens refuse children older than 6.", "After this age, children dislike kindergarten.", "Children who skip kindergarten perform badly."], 0,
        "An advisable age is justified by readiness to learn. The other choices add rules and consequences the statement does not give."))
    A(Q(lg, "Deduction", "Before 2015, Katie’s staff did not need a driving licence, but applicants needed 3 A-levels. From 2015, applicants need a driving licence and a car, and only 2 A-levels. Angela works for Katie, has 3 A-levels and no driving licence. Which must be true?",
        ["Liam, who has 2 A-levels and a licence, started before 2015.", "Jim, who has 2 A-levels and no licence, has a car.", "Jim could have been hired before 2015, but cannot be hired now.", "Angela started working for Katie before 2015."], 3,
        "Angela has no licence, so she could not meet the rule introduced in 2015. She must already have been employed. Jim had only 2 A-levels, so he also failed the pre-2015 rule."))
    A(Q(lg, "Deduction", "In the UK, everyone who carries a firearm is a criminal, a farmer, or a police officer. An illegal weapon means the person is a criminal. A shotgun plus a licence means the person is a farmer. Being in the police force means the person is a police officer. Hannah has an illegal weapon, a shotgun and a shotgun licence. Eric is in the police force. Which follows?",
        ["Hannah is a criminal and a farmer.", "Hannah is neither a criminal nor a farmer.", "Eric possesses a firearm.", "No one is a criminal."], 0,
        "The illegal weapon makes Hannah a criminal, and the licensed shotgun makes her a farmer. Eric’s job does not by itself say he is carrying a firearm."))
    A(Q(lg, "Data", "Students in classes of fewer than 30 pupils perform better. Meti’s maths class has 20 pupils and her English class has 33. Which is the best conclusion?",
        ["Meti is more likely to perform better in history than in maths.", "Meti is more likely to perform better in maths than in English.", "Meti is more likely to perform better in English than in history.", "Meti is likely to perform better in English than in any other subject."], 1,
        "Maths is under the 30-pupil threshold and English is over it. The study therefore favours better performance in maths than in English."))
    A(Q(lg, "Inference", "MP3 players boomed in 2007 and popularised the MP3 format. By 2017 MP3 was much less popular, which some attribute to streaming services that do not need MP3 files. Ryan’s software converts audio to MP3, and he is going to have to stop developing it. Which is supported?",
        ["He must stop because the software has become more popular.", "The rise of MP3 players inevitably caused the format’s downfall.", "Demand for MP3 is increasing.", "MP3 is in decline because fewer people use MP3 files."], 3,
        "The passage links the decline to streaming, which removes the need for MP3 files. It does not say demand is rising or that the players themselves caused the later decline."))
    return items


def gat_paper():
    v, qn, an = "Verbal", "Quantitative", "Analytical"
    items = []
    A = items.append

    A(Q(v, "Sentence completion", "Viruses are invisible through the ______ microscope, but we know they are there because we can see the ______ they cause.",
        ["cheap; damage", "elementary; harm", "simple; danger", "ordinary; havoc"], 3,
        "Viruses are invisible under an ordinary microscope. “Havoc” is the strong word for the damage their presence causes."))
    A(Q(v, "Sentence completion", "The sea was coming after me as high as a great hill and ______ as a ______ enemy.",
        ["furious; charging", "dreadful; advancing", "terrible; charging", "angry; attacking"], 0,
        "The pattern is “as high as a great hill and as furious as a charging enemy.” Furious matches the violence of the sea, and charging matches an enemy rushing forward."))
    A(Q(v, "Sentence completion", "Although its publicity has been ______, the film itself is intelligent, well-acted, handsomely produced and altogether ______.",
        ["tasteless; respectable", "extensive; moderate", "sophisticated; moderate", "risqué; crude"], 0,
        "Although signals a contrast. Tasteless publicity against a respectable film is the contrast. Risqué publicity with a crude film would agree, not contrast."))
    A(Q(v, "Sentence completion", "It takes ______ character to ______ the extremities of the Arctic.",
        ["an unflappable; sustain", "a dictatorial; brook", "a Spartan; negotiate", "an inimitable; resist"], 2,
        "Spartan means hardy and austere, which fits the Arctic. Here negotiate means to make one’s way through a difficulty."))
    A(Q(v, "Sentence completion", "Griffin Nicholson works to overturn wrongful convictions. He was opposed to the court ruling ______ appeals for inmates who might be ______.",
        ["barring; culpable", "curbing; exonerated", "encouraging; innocent", "scrutinizing; eligible"], 1,
        "He would oppose a ruling that curbs appeals for people who might be cleared. He would not oppose a ruling that encourages appeals for the innocent. The printed key marks C, but that choice contradicts his work."))
    A(Q(v, "Sentence completion", "Their conversation was unsettling, because the gravity of their topic contrasted so oddly with the ______ of their tone.",
        ["uniqueness", "rapidity", "lightness", "precision"], 2,
        "Gravity contrasted with lightness. A heavy subject spoken about lightly is what makes the conversation unsettling."))
    A(Q(v, "Sentence completion", "The driver suddenly applied the brakes when he saw a ______ truck ahead of him.",
        ["stationary", "moving", "static", "immobile"], 0,
        "A driver brakes for a truck that is stopped in the road. Stationary is the idiomatic choice; static and immobile are less natural for a vehicle."))
    A(Q(v, "Sentence completion", "Salma is much too ______ to have anything to do with that obnoxious affair.",
        ["noble", "proud", "happy", "difficult"], 0,
        "Noble character keeps her away from something obnoxious. Proud or happy does not explain a moral refusal as directly."))
    A(Q(v, "Sentence completion", "Roberto Clemente was seen as ______ because of his selflessness on the baseball field and his humanitarian work in Nicaragua.",
        ["an individualist", "a grandstander", "a sybarite", "an altruist"], 3,
        "Selflessness and humanitarian work define an altruist. A grandstander seeks attention, which is the opposite of the evidence. The printed key marks grandstander; the sentence supports altruist."))

    A(Q(v, "Antonym", "ABBREVIATE", ["abridge", "expand", "achieve", "accept"], 1,
        "To abbreviate is to shorten. The opposite is to expand. Abridge is a synonym."))
    A(Q(v, "Antonym", "ABJURE", ["acknowledge", "disown", "deny", "hate"], 0,
        "To abjure is to renounce or reject. The opposite is to acknowledge. Disown and deny are close in meaning to abjure."))
    A(Q(v, "Antonym", "ABSURD", ["scarcity", "adorn", "rational", "flourish"], 2,
        "Absurd means unreasonable. The opposite is rational."))
    A(Q(v, "Antonym", "ABUNDANT", ["ample", "enough", "great", "scant"], 3,
        "Abundant means plentiful. Scant means barely enough or very little."))
    A(Q(v, "Antonym", "ACERBITY", ["sweat", "gentleness", "tasty", "account"], 1,
        "Acerbity is harshness or bitterness of temper. Gentleness is the opposite."))
    A(Q(v, "Antonym", "BLOOMING", ["fading", "flowering", "quiet", "mild"], 0,
        "Blooming means flourishing. Fading is the opposite. Flowering is a synonym."))
    A(Q(v, "Antonym", "BLISS", ["merge", "disseminate", "dull", "suffering"], 3,
        "Bliss is extreme happiness. Suffering is its opposite."))
    A(Q(v, "Antonym", "BEWITCH", ["disenchant", "rapture", "profit", "avail"], 0,
        "To bewitch is to enchant. To disenchant is to free someone from that spell."))
    A(Q(v, "Antonym", "BAUBLE", ["plaything", "valuable", "modest", "besiege"], 1,
        "A bauble is a cheap trinket. Something valuable is the opposite. A plaything is close to a synonym."))

    A(Q(v, "Analogy", "BOOK : READ", ["ointment : apply", "bat : ball", "watch : time", "marriage : home"], 0,
        "A book is meant to be read. Ointment is meant to be applied. The relationship is object and its intended use."))
    A(Q(v, "Analogy", "EDUCATION : SCHOOL", ["medicine : hospital", "production : factory", "wood : furniture", "milk : cow"], 1,
        "Education is the activity carried on in a school. Production is the activity carried on in a factory. Medicine : hospital is close, but production : factory keeps the same activity-to-workplace pattern."))
    A(Q(v, "Analogy", "RENOVATION : RENEWAL", ["fail : examination", "tumble : topple", "poor : poverty", "up : climb"], 1,
        "Renovation and renewal are synonyms. Tumble and topple are synonyms."))
    A(Q(v, "Analogy", "BUSH : FLORA", ["plant : fauna", "horse : carriage", "fish : water", "blue : colour"], 3,
        "A bush is a kind of flora. Blue is a kind of colour. A plant is not a kind of fauna."))
    A(Q(v, "Analogy", "HEAVY : LIGHT", ["loophole : fool-proof", "weight : bulb", "dark : night", "water : fire"], 0,
        "Heavy and light are opposites. A loophole is the opposite of something fool-proof, which has no loophole."))
    A(Q(v, "Analogy", "BOOK : PAGE", ["parliament : minister", "rope : fibre", "ship : wood", "star : space"], 1,
        "A book is made up of pages. A rope is made up of fibres."))
    A(Q(v, "Analogy", "EXAMINATION : DEGREE", ["doctor : Ph.D.", "music : instrument", "interview : selection", "sports : medal"], 2,
        "An examination is the process that leads to a degree. An interview is the process that leads to selection."))

    A(Q(v, "Reading", "The purpose of education is to make the student:",
        ["an expert in all fields", "an expert in his subject", "only capable of earning", "confident only"], 1,
        "The passage states the purpose directly: to make the student an expert in his subject.", EDU))
    A(Q(v, "Reading", "What, according to the writer, is the end?",
        ["Excellence in the field chosen", "Passing the examination", "Earning more and more money", "Cramming lectures and books"], 0,
        "Passing examinations is only a means. The end is excellence in the chosen field.", EDU))
    A(Q(v, "Reading", "Modern civilization has provided:",
        ["vocational education", "the art of conversation", "adult education", "higher education"], 0,
        "The passage says modern civilization has provided vocational education so people can gain professional skill.", EDU))
    A(Q(v, "Reading", "In the paragraph, Aristotle:",
        ["surpasses the earth and all living beings", "tries to explore the nature of the physical world only", "speaks about all living beings as his main subject", "tries to explore the nature of happiness"], 3,
        "The paragraph says Aristotle tries to explore the nature of happiness. It is man, through the thinking faculty, who masters the earth.", ARISTOTLE))
    A(Q(v, "Reading", "Man differs from other animals in having:",
        ["a brain", "a speaking faculty", "a thinking faculty", "an eating faculty"], 2,
        "Aristotle’s distinction in the passage is the thinking faculty, not merely eating or speaking.", ARISTOTLE))
    A(Q(v, "Reading", "According to the passage, rights and duties are:",
        ["co-related", "two sides of the same coin", "neither of these", "both co-related and two sides of the same coin"], 3,
        "The passage uses both descriptions, so the complete answer is both.", DUTY))
    A(Q(v, "Reading", "According to the author, moral duty is:",
        ["enjoined upon animals", "helping the rich", "more effective than legal duty", "secondary to legal duty"], 2,
        "The passage says moral duty is more effective than legal duty.", DUTY))
    A(Q(v, "Reading", "Where does duty originate?",
        ["From responsibility, but not from conscience", "From responsibility which is related to conscience", "From legal bondage", "From hypocrisy and diplomacy"], 1,
        "The passage says duty originates from a sense of responsibility directly related to conscience, without legal bondage.", DUTY))
    A(Q(v, "Reading", "Which statement is incorrect?",
        ["Hypocrisy and diplomacy do not support the sense of duty.", "Hypocrisy involves wickedness.", "Duty involves sincerity.", "Sense of duty is not important for the development of civilization."], 3,
        "The passage says sense of duty is paramount for civilization. Calling it unimportant contradicts the text, so that statement is the incorrect one.", DUTY))
    A(Q(v, "Reading", "The author:",
        ["has a sense of responsibility", "doesn’t have a sense of duty", "both", "neither"], 0,
        "The author writes “I must try” and “I owe a duty,” which shows a sense of responsibility.", DUTY))
    A(Q(v, "Reading", "An appropriate title for the passage would be:",
        ["The change of nature", "Courage and panic", "The will to fight", "The miracle of confronting danger"], 3,
        "The passage’s own phrase is the miracle by which timid people, facing danger that must be met, suddenly find courage.", DANGER))
    A(Q(v, "Reading", "The author names three reactions to sudden danger. What are they?",
        ["Paralysis with fear, panic, or sudden courage that faces the danger", "Paralysis with fear, running away, or fighting", "Fleeing in panic, fighting back, or standing still", "Paralysis, panic, or acting like an inferior animal"], 0,
        "The three reactions in the text are paralysis, panic, and the sudden courage that faces unavoidable danger.", DANGER))
    A(Q(v, "Reading", "The distinction between “inferior animals” and “rational beings” is that:",
        ["rational beings are stronger", "rational beings can reason things out, whereas inferior animals cannot", "inferior animals are incapable of fighting", "rational beings are clever only in school"], 1,
        "The passage uses the contrast to separate creatures that can reason from those that cannot.", DANGER))

    A(Q(qn, "Algebra", "The sum of a number and its reciprocal is three times the difference of the number and its reciprocal. The number is:",
        ["±√2", "±√3", "±2", "±1/2"], 0,
        "Let the number be x. Then x + 1/x = 3(x − 1/x). Multiplying by x gives x² + 1 = 3x² − 3, so 4 = 2x² and x² = 2. Thus x = ±√2. The original options were printed with missing symbols; these are the standard choices, and ±√2 is the solution."))
    A(Q(qn, "Remainders", "When k is divided by 17, the quotient is p and the remainder is 5. When k is divided by 23, the quotient is q and the remainder is 14. Which is true?",
        ["23p + 17q = 19", "14p + 5q = 6", "17p − 23q = 9", "5p − 14q = 6"], 2,
        "k = 17p + 5 = 23q + 14. Rearrange: 17p − 23q = 14 − 5 = 9."))
    A(Q(qn, "Geometry", "What is the area of a circle whose radius is the diagonal of a square of area 9?",
        ["8π", "18π", "3π", "9π"], 1,
        "The square’s side is 3, so its diagonal is 3√2. The circle’s area is π(3√2)² = 18π."))
    A(Q(qn, "Geometry", "The circumference of a circle is xπ units and its area is yπ square units. If x = y, the radius is:",
        ["1", "2", "3π", "2π"], 1,
        "Circumference xπ = 2πr gives x = 2r. Area yπ = πr² gives y = r². Set 2r = r², so r = 2."))
    A(Q(qn, "Geometry", "A cylindrical silo has diameter 14 inches and height 6 inches. One gallon is 231 cubic inches. Its capacity is approximately:",
        ["4 gallons", "1 gallon", "2 gallons", "2.5 gallons"], 0,
        "Radius 7 gives volume π×49×6 = 294π ≈ 924 cubic inches. 924 / 231 = 4 gallons."))
    A(Q(qn, "Geometry", "What is the volume of a cube whose surface area is 294?",
        ["125", "216", "294", "343"], 3,
        "6a² = 294, so a² = 49 and a = 7. The volume is 7³ = 343."))
    A(Q(qn, "Ratio", "Boys and girls were in the ratio 2 : 3. The number of boys was five more than one third of the class. How many people were in the class?",
        ["15", "30", "45", "75"], 3,
        "Boys are 2/5 of the class. So 2n/5 = n/3 + 5. Then 6n = 5n + 75 and n = 75. The printed choices stopped at 27 and did not include this solution."))
    A(Q(qn, "Exponents", "What is the average of 5^30, 5^60, 5^17, 5^13 and 5^90?",
        ["5^210", "5^209", "5^29 + 5^59 + 5^16 + 5^12 + 5^89", "5^205"], 2,
        "Dividing the sum by 5 subtracts 1 from each exponent. The average is exactly 5^29 + 5^59 + 5^16 + 5^12 + 5^89."))
    A(Q(qn, "Inequality", "If p + 1 < 3p + 5, then:",
        ["p < −2", "p > −2", "p = 0", "p > 2"], 1,
        "Subtract p and 5: −4 < 2p, so p > −2."))
    A(Q(qn, "Geometry", "An equilateral triangle and a square have the same perimeter. What is the ratio of the triangle’s side to the square’s side?",
        ["3 : 4", "4 : 3", "1 : 2", "1 : 3"], 1,
        "3a = 4b, so a/b = 4/3."))
    A(Q(qn, "Algebra", "The sum of two integers is 42 and their difference is 22. The greater integer is:",
        ["25", "32", "8", "10"], 1,
        "Adding the equations gives 2x = 64, so the greater integer is 32. The smaller is 10."))
    A(Q(qn, "Arithmetic", "Nazir’s buckets hold 11 gallons and Osama’s hold 8. How much more water can 7 of Nazir’s buckets hold than 7 of Osama’s?",
        ["7 gallons", "9 gallons", "21 gallons", "24 gallons"], 2,
        "Each of Nazir’s buckets holds 3 gallons more. Seven buckets hold 21 gallons more."))
    A(Q(qn, "Geometry", "Two circles touch externally at C, and AB is a common tangent touching the circles at A and B. Angle ACB is:",
        ["greater than 120°", "greater than 90°", "less than 90°", "equal to 90°"], 3,
        "The radii to the points of tangency are perpendicular to the tangent. With the circles touching externally, triangle ACB is right-angled at C."))
    A(Q(qn, "Rates", "A train is 10 minutes late at 40 miles per hour and 16 minutes late at 30 miles per hour. The distance between the towns is:",
        ["12 miles", "720 miles", "8 miles", "16 miles"], 0,
        "d/30 − d/40 = 6/60 hour. So d/120 = 0.1 and d = 12 miles."))
    A(Q(qn, "Rates", "Trains 132 m and 108 m long approach on parallel tracks at 32 km/h and 40 km/h. After they meet, how long until they are clear of each other?",
        ["20 sec", "15 sec", "12 sec", "29 sec"], 2,
        "The relative distance is 240 m. The relative speed is 72 km/h, which is 20 m/s. Time = 240/20 = 12 seconds."))
    A(Q(qn, "Exponents", "If 2^a = x and 2^b = y, then xy =",
        ["9^(a+b)", "2^(ab)", "4^(a+b)", "2^(a+b)"], 3,
        "xy = 2^a × 2^b = 2^(a+b)."))
    A(Q(qn, "Averages", "The average of three consecutive integers is M. Which must be true?\nI. One of the three numbers is M.\nII. The average of two of the three numbers is M.\nIII. M is an integer.",
        ["I only", "II only", "III only", "I, II and III"], 3,
        "If the integers are n−1, n and n+1, their average M is the middle integer n. The first and third also average to n. So all three statements hold."))
    A(Q(qn, "Algebra", "If a² = 17, then (a + 1)(a − 1) =",
        ["15", "12", "√17", "16"], 3,
        "(a + 1)(a − 1) = a² − 1 = 17 − 1 = 16."))
    A(Q(qn, "Numbers", "Which cannot be written as the sum of three consecutive integers?",
        ["27", "26", "21", "42"], 1,
        "Three consecutive integers sum to 3 times the middle integer, so the sum is a multiple of 3. 26 is not a multiple of 3."))
    A(Q(qn, "Comparison", "Column A is 7 × 7 × 7 × 7. Column B is 7⁴.",
        ["Column A is greater", "Column B is greater", "The two quantities are equal", "The relationship cannot be determined"], 2,
        "Four factors of 7 are exactly 7⁴."))
    A(Q(qn, "Comparison", "N is a positive integer. Column A is 2^N. Column B is (−2)^(N+1).",
        ["Column A is greater", "Column B is greater", "The two quantities are equal", "The relationship cannot be determined"], 3,
        "If N is even, column B is negative and A is greater. If N is odd, column B equals 2^(N+1), which is larger than 2^N. The relationship changes with N."))
    A(Q(qn, "Comparison", "Column A is 2^(5−1). Column B is 2^5 − 1.",
        ["Column A is greater", "Column B is greater", "The two quantities are equal", "The relationship cannot be determined"], 1,
        "Column A is 2^4 = 16. Column B is 32 − 1 = 31. Column B is greater."))
    A(Q(qn, "Comparison", "Column A is (3^0)(9^1). Column B is 27.",
        ["Column A is greater", "Column B is greater", "The two quantities are equal", "The relationship cannot be determined"], 1,
        "3^0 × 9 = 1 × 9 = 9, which is less than 27."))
    A(Q(qn, "Comparison", "x > 1 and x ≠ y. Column A is y^x. Column B is x^x.",
        ["Column A is greater", "Column B is greater", "The two quantities are equal", "The relationship cannot be determined"], 3,
        "y could be greater than x or smaller than x. The columns cannot be ordered from the given information."))
    A(Q(qn, "Comparison", "Five consecutive integers sum to 0. Column A is their product. Column B is their average.",
        ["Column A is greater", "Column B is greater", "The two quantities are equal", "The relationship cannot be determined"], 2,
        "The integers are −2, −1, 0, 1 and 2. Their product is 0 and their average is 0."))

    A(Q(an, "Rules", "The computer has performed exactly one operation on an account. Which must be true?",
        ["The account is type 1 or type 2.", "The account is type 1, type 2, or type 3.", "The account is type 2, type 3, or type 5.", "The account is type 2, type 4, or type 5.", "The account is type 3, type 4, or type 5."], 1,
        "A single operation can be W or X on type 1, X on type 2, or Y on type 3. Type 4 needs two operations and type 5 needs three, so the account must be type 1, 2 or 3.", ACCOUNTS))
    A(Q(an, "Rules", "Operation Z was performed, but that trace alone does not show whether any other operation was performed. The account could be any type EXCEPT:",
        ["1", "2", "3", "4", "5"], 0,
        "Type 1 allows only W or only X, never Z. Types 2, 3, 4 and 5 can include Z together with other allowed operations.", ACCOUNTS))
    A(Q(an, "Rules", "Which type, if the computer operates on it, must have operation X performed?",
        ["Type 1", "Type 2", "Type 3", "Type 4", "Type 5"], 1,
        "Every type 2 case includes X. Type 1 can use W instead, type 4 cannot use X, and types 3 and 5 only sometimes include X.", ACCOUNTS))
    A(Q(an, "Rules", "The only operations performed are X and Z. The account must be type:",
        ["1", "2", "3", "4", "5"], 1,
        "Type 2 allows X plus one other operation except W, so X and Z fit. Type 4 forbids X, type 3 requires Y, and types 1 and 5 have the wrong number of operations.", ACCOUNTS))
    A(Q(an, "Rules", "Exactly two operations were performed, and Y was not one of them. Which must be true?",
        ["The account is type 1 or type 2.", "The account is type 2 or type 3.", "The account is type 2 or type 4.", "The account is type 3 or type 4.", "The account is type 3 or type 5."], 2,
        "Without Y, the possible legal pairs are XZ, which is type 2, and WZ, which is type 4. WX is not allowed for any type.", ACCOUNTS))

    A(Q(an, "Seating", "Which seating, from chair 1 through chair 7, follows every rule?",
        ["E, I, N, P, G, O, H", "G, P, N, I, H, O, F", "I, G, N, P, O, F, H", "I, H, N, P, O, F, G", "O, F, H, N, I, P, G"], 1,
        "In G, P, N, I, H, O, F, N is in 3, O and F are together with F behind, H and P have exactly two chairs between them, G is not beside N, and I is not beside P. The other rows break at least one rule.", DIGNITARIES))
    A(Q(an, "Seating", "F sits in chair 6 and H sits in chair 7. Who must sit in chair 2?",
        ["G", "I", "N", "O", "P"], 1,
        "F in 6 forces O into 5. H in 7 forces P into 4. N is in 3. G cannot sit in 2, so G is in 1 and I must sit in 2.", DIGNITARIES))
    A(Q(an, "Seating", "The seating is G, I, N, H, O, F, P. Which pair can exchange seats without breaking the rules?",
        ["F and G", "G and H", "G and I", "H and P", "I and P"], 3,
        "Swapping H and P puts them in 7 and 4, which still leaves exactly two chairs between them, and neither move breaks the O-F block or G’s restriction. Every other swap breaks a rule.", DIGNITARIES))
    A(Q(an, "Seating", "O sits in chair 1 and H sits in chair 7. How many chairs are between F and I?",
        ["Zero", "One", "Two", "Three", "Four"], 3,
        "F must be in 2, N is in 3, and P must be in 4. I cannot sit next to P, so I is in 6 and G is in 5. Chairs 3, 4 and 5 lie between F and I.", DIGNITARIES))
    A(Q(an, "Seating", "H sits in chair 4 and F sits in chair 6. Who sits in chairs 1 and 7?",
        ["G and O", "G and P", "I and P", "O and I", "P and O"], 1,
        "F in 6 puts O in 5. H in 4 can pair with P in 1 or 7. P in 1 would put I next to P, which is forbidden, so P is in 7, G is in 1 and I is in 2.", DIGNITARIES))

    A(Q(an, "Grouping", "Which row, on stands 1 through 5, is acceptable?",
        ["M, R, T, P, Q", "N, T, S, U, Q", "P, T, S, R, U", "T, P, R, S, M", "U, N, Q, P, T"], 2,
        "P, T, S, R, U has S or R on stand 3, includes U, and places T next to P. The other rows miss a required sculpture, separate T from P, or put M off stand 1.", SCULPTURES))
    A(Q(an, "Grouping", "If S is on stand 1, which must be true?",
        ["P is on stand 4.", "R is on stand 3.", "T is on stand 2.", "T is on stand 4.", "U is on stand 5."], 1,
        "Stand 3 must be R or S. S is already on stand 1, so R must be on stand 3.", SCULPTURES))
    A(Q(an, "Grouping", "If T is on stand 5, which pair can be on immediately adjacent stands?",
        ["M and P", "Q and N", "Q and P", "R and T", "U and R"], 4,
        "T on stand 5 puts P on stand 4. One legal row is U, R, S, P, T: stand 3 is S, U is included, and U is immediately beside R. M cannot sit beside P, because M would have to be on stand 1. Q cannot sit on stand 3 beside P. R cannot sit beside T, because stand 4 is already P.", SCULPTURES))
    A(Q(an, "Grouping", "If U is on stand 4, which cannot be on stand 5?",
        ["N", "P", "Q", "R", "T"], 4,
        "If T were on 5, P would have to be next to it, on 4. Stand 4 is already U, so T cannot be on 5.", SCULPTURES))
    A(Q(an, "Grouping", "If T is on stand 2, which sculpture must be selected?",
        ["M", "N", "R", "S", "U"], 4,
        "T on 2 requires P beside it. P cannot be on 3, because stand 3 is R or S, so P is on 1. M would also need stand 1, so M is out. U must therefore be selected.", SCULPTURES))
    A(Q(an, "Grouping", "P is not selected and R is on stand 1. Which sculptures must also be selected?",
        ["M, Q, T and U", "N, Q, S and T", "N, Q, S and U", "N, S, T and U", "Q, S, T and U"], 2,
        "No P means no T. R is on 1, so S must be on 3, and M cannot take stand 1. U must be selected. The two remaining places must be N and Q.", SCULPTURES))

    A(Q(an, "Completion", "Which option best fills the blank?",
        ["We are always trying to undermine others’ endeavours.", "People always deceive one another.", "Even close friends are not trustworthy.", "People want power to control others.", "There are many occasions when we graciously offer our assistance."], 4,
        "“On the contrary” reverses the idea that people are unwilling to help. The blank has to say that people do sometimes help.", SELFISH))
    A(Q(an, "Critical reasoning", "Which statement most strongly contradicts the author’s view of society?",
        ["The greatest strength of society is altruism.", "We must all learn the art of love.", "Our short-term actions may contradict our long-term goals.", "Morality is the bedrock of a growing community.", "The forces of goodwill ultimately triumph over evil."], 4,
        "The author says selfishness is the principal force and help is only temporary. Saying goodwill ultimately triumphs denies that conclusion.", SELFISH))
    A(Q(an, "Critical reasoning", "Many people do not read the books they buy. For example, 17% of college students in the study have textbooks, but only 45% of them read more than once a year, and only 17% read more than once a week. Which, if true, casts doubt on the claim that most people read the books they purchase?",
        ["Readers often exaggerate how much they read.", "Novels sell better than other books.", "Many people buy books to look like scholars.", "Regular readers are prone to eye disease.", "Frequent reading increases reading speed."], 2,
        "If people buy books for the appearance of scholarship, that gives a reason they would own books without reading them, which counts against the claim that buyers read what they buy."))
    A(Q(an, "Critical reasoning", "“The value of a close examination of an aircraft accident lies not only in fixing blame but in learning lessons.” This statement would most logically begin which passage?",
        ["A survey of the scapegoat phenomenon in modern society.", "An argument for putting specific details in any academic essay.", "An argument against the usefulness of the National Transportation Safety Board.", "A brief history of aeronautics.", "A description of the causes of a particular aircraft accident."], 4,
        "The sentence introduces why one accident is being examined: both to assign blame and to learn what caused it."))
    A(Q(an, "Assumption", "Harry Truman said, “The responsibility of the United States is to serve and not dominate the world.” Which is a basic assumption?",
        ["The United States is capable of dominating the world.", "The United States has already chosen service over domination.", "World domination is a virtue.", "A new president must be decisive.", "The previous administration had been irresponsible."], 0,
        "Choosing not to dominate assumes domination is possible. Otherwise the contrast between serving and dominating would not be a real choice."))
    A(Q(an, "Assumption", "A researcher concludes that women are as capable as men in mathematics, but their skill is less developed because society expects them to develop other abilities. Which is assumed?",
        ["Mathematics matters more than other abilities.", "Mathematics matters less than other abilities.", "Women and men should be equally capable.", "Women might be more capable than men.", "Women tend to conform to social expectations."], 4,
        "The explanation works only if women do follow the expectations society places on them. Without that conformity, the expectation would not shape their skills."))
    A(Q(an, "Weaken", "Researchers found an inactive virus in dry bread. Inactive viruses have converted healthy cells into cancer cells in earlier experiments. It is concluded that dry bread can cause cancer. Which most seriously weakens the argument?",
        ["Many studies of the same topic agreed.", "Other ingredients in dry bread can neutralise the inactive virus.", "Many cancer patients said they ate dry bread.", "Ten percent of the rural population uses dry bread.", "No medicine can kill the inactive virus."], 1,
        "If other ingredients neutralise the virus, finding it in bread does not mean eating the bread exposes cells to an active cancer risk."))
    A(Q(an, "Inference", "Bacon said, “The sum of behaviour is to retain a man’s dignity without intruding upon the liberty of others.” The writer concludes that not intruding upon another’s liberty is impossible. The implied conclusion is:",
        ["Retaining one’s dignity is impossible without intruding upon another’s liberty.", "Retaining dignity never involves taking liberty from others.", "Dignity and liberty are unrelated.", "There is always the possibility of a dignified intrusion.", "None of these."], 0,
        "If dignified behaviour requires no intrusion, and the writer says avoiding intrusion is impossible, then dignity cannot be kept without that intrusion."))
    return items


def main():
    papers = [
        exam(
            "ngat-a",
            "NGAT Set A",
            "Analogies, vocabulary, grammar, short passages, quantitative problems and logical deduction.",
            "Practice paper compiled from the NGAT PDFs in assets. Items that depended on a missing chart or diagram were left out.",
            80,
            ngat_set_one(),
        ),
        exam(
            "ngat-b",
            "NGAT Set B",
            "A second paper: analogies, sentence completion, reading, arithmetic and inference.",
            "Practice paper compiled from the NGAT PDFs in assets. The climate-change items were left out because the source passage was not in the file.",
            60,
            ngat_set_two(),
        ),
        exam(
            "gat-sample",
            "GAT Sample Paper",
            "Verbal ability, quantitative problems and analytical games, with the printed answer key checked against the working.",
            "GAT Exam Question with Answers. A few quantitative choices were blank in the PDF because the symbols did not embed; those items are omitted or restored only where the algebra is unambiguous.",
            90,
            gat_paper(),
        ),
        exam(
            "uog-gat",
            "UoG GAT Model",
            "Verbal, quantitative and analytical items from the University of Gondar graduate admission model.",
            "University of Gondar GAT model exam. Items that needed a missing diagram, a garbled formula, or a long reprinted passage were left out.",
            100,
            uog_questions(),
        ),
        exam(
            "dbu-gat",
            "DBU GAT Model",
            "Verbal, quantitative, statistics and analytical items from a second university model and public NGAT practice.",
            "Debre Berhan University GAT model exam, plus public NGAT statistics and coding practice. Graph items and questions already in the other papers were left out.",
            90,
            more_questions(),
        ),
        exam(
            "ngat-extra",
            "NGAT Practice Set",
            "A large extra set: sentence completion, analogies, synonyms, idioms, number problems and reasoning.",
            "Public NGAT and GAT practice questions. Figure items and questions already in the other papers were left out.",
            120,
            deep_questions(),
        ),
    ]
    for paper in papers:
        for question in paper["questions"]:
            n = len(question["choices"])
            if not 0 <= question["answer"] < n:
                raise SystemExit(f"bad answer {question['id']}")
            for extra in question.get("alsoAccept", []):
                if not 0 <= extra < n:
                    raise SystemExit(f"bad also {question['id']}")
            if len(question["choices"]) < 2:
                raise SystemExit(f"too few choices {question['id']}")
    payload = {"exams": papers}
    dest = ROOT / "assets" / "questions" / "bank.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(dest)
    for paper in papers:
        print(f"{paper['id']}: {len(paper['questions'])} questions")


if __name__ == "__main__":
    main()

