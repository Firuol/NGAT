"""Extra GAT items from the University of Gondar public model exam.

Figure-only items and the long reprinted reading passages are omitted.
Explanations are worked here rather than copied from the PDF.
"""


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


def questions():
    v, qn, an = "Verbal", "Quantitative", "Analytical"
    items = []
    A = items.append

    A(Q(v, "Analogy", "CHILD : HUMAN", ["bird : robin", "dog : pet", "cow : milk", "kitten : cat"], 3,
        "A child is a young human. A kitten is a young cat."))
    A(Q(v, "Analogy", "CONTINENT : WORLD", ["teacher : classroom", "class : school", "cogent : powerful", "apple : fruit"], 1,
        "A world is made up of continents. A school is made up of classes."))
    A(Q(v, "Analogy", "WARM : HOT :: ______ : HILARIOUS", ["humid", "raucous", "summer", "amusing"], 3,
        "Warm is a milder degree of hot. Amusing is a milder degree of hilarious."))
    A(Q(v, "Analogy", "STUDENT : DORMITORY", ["curtain : stage", "prisoner : jail", "skull : brain", "shirt : clothing"], 1,
        "A dormitory is where students are housed. A jail is where prisoners are housed."))
    A(Q(v, "Analogy", "ESSAY : SHORT STORY", ["symphony : concerto", "biography : novel", "comedy : burlesque", "monologue : drama"], 1,
        "An essay and a short story are shorter nonfiction and fiction. A biography and a novel are the longer pair of the same kinds."))
    A(Q(v, "Analogy", "KNIFE : CUT", ["winter : summer", "sword : sharp", "run : fast", "drill : hole"], 3,
        "A knife is used to cut. A drill is used to make a hole."))
    A(Q(v, "Analogy", "FISH : TROUT", ["hair : black", "bird : aviary", "tiger : carnivorous", "mammal : cow"], 3,
        "A trout is a kind of fish. A cow is a kind of mammal."))
    A(Q(v, "Analogy", "RACE : FATIGUE", ["fasting : hunger", "round : boxing", "flower : color", "hiking : gangrene"], 0,
        "A race causes fatigue. Fasting causes hunger."))
    A(Q(v, "Analogy", "INDUSTRIOUS : HARDWORKING", ["sky : blue", "muddy : unclear", "book : reading", "pond : lake"], 1,
        "Industrious and hardworking are synonyms. Muddy and unclear are synonyms."))
    A(Q(v, "Analogy", "COOL : FROZEN", ["sharp : cut", "warm : hot", "hassock : stool", "freedom : liberty"], 1,
        "Frozen is a stronger degree of cool. Hot is a stronger degree of warm."))
    A(Q(v, "Antonym", "SCHOLAR : IGNORANT", ["hardworking : lazy", "knife : sword", "courage : bold", "luxury : wealth"], 0,
        "Ignorant is the opposite of scholar. Lazy is the opposite of hardworking."))
    A(Q(v, "Antonym", "MANDATORY", ["dispassionate", "obligatory", "voluntary", "inveterate"], 2,
        "Mandatory means required. Voluntary is the opposite."))
    A(Q(v, "Antonym", "REDUNDANT", ["verbose", "irrelevant", "excessive", "insufficient"], 3,
        "Redundant means more than is needed. Insufficient means not enough."))
    A(Q(v, "Antonym", "EMPATHY", ["compassion", "lack of feeling for others", "lack of religious certainty", "lack of credit"], 1,
        "Empathy is feeling for other people. The opposite is a lack of that feeling."))
    A(Q(v, "Antonym", "UBIQUITOUS", ["obsequious", "cantankerous", "rare", "omnivorous"], 2,
        "Ubiquitous means found everywhere. Rare is the opposite."))
    A(Q(v, "Antonym", "MITIGATE", ["enhance", "ignore", "worsen", "maintain"], 2,
        "To mitigate is to make something less severe. To worsen is the opposite."))

    A(Q(v, "Grammar", "“Can Billy come out and play?” “No, he ______ his mother do the chores right now.”",
        ["is always helping", "helps", "does help", "is helping"], 3,
        "“Right now” needs the present continuous: he is helping."))
    A(Q(v, "Grammar", "I’m going to the airport to get Jane. ______ at three o’clock, so I’d better hurry.",
        ["Her plane arriving", "Her plane arrives", "Is her plane arriving", "Her plane does arrive"], 1,
        "Timetables use the simple present. Her plane arrives at three."))
    A(Q(v, "Grammar", "He’s the man ______ brother built our house.",
        ["that", "which", "whose", "who"], 2,
        "Whose shows that the brother belongs to the man."))
    A(Q(v, "Grammar", "The reason ______ you can’t go is that you haven’t done the washing-up.",
        ["which", "why", "when", "where"], 1,
        "“The reason why” introduces the explanation."))
    A(Q(v, "Grammar", "Feeding a big family a healthy meal ______ more and more expensive.",
        ["get", "is getting", "gets", "getting"], 1,
        "“More and more” describes a change in progress, so the present continuous is getting is used."))
    A(Q(v, "Grammar", "If I ______ money, I would purchase it now.",
        ["has", "have", "had", "have had"], 2,
        "This is a second conditional: if + past simple, then would + verb. The past form is had."))
    A(Q(v, "Grammar", "She is looking for accommodation ______ in a flat or a shared house.",
        ["both", "until", "neither", "either"], 3,
        "Either … or presents the two choices."))
    A(Q(v, "Grammar", "Maryam, accompanied by her brother, ______ at the party last night.",
        ["is", "are", "was", "were"], 2,
        "The subject is Maryam, which is singular, and the phrase is about last night. “Accompanied by her brother” does not make the verb plural, so the verb is was."))
    A(Q(v, "Grammar", "The newly imposed rules sound very ______.",
        ["interesting", "interestingly", "interested", "interest"], 0,
        "Sound is followed by an adjective describing the rules. Interesting is that adjective."))
    A(Q(v, "Grammar", "The passive equivalent of “We gave the police some information” is:",
        ["Some information is given to the police.", "The police were given some information.", "Some information was given to the police.", "Both “The police were given some information” and “Some information was given to the police.”"], 3,
        "The original verb is past, and gave has two objects. Either object can become the subject of a past passive, so both past forms are correct."))
    A(Q(v, "Grammar", "“Belay would have bought a new car if he had been a rich man” means:",
        ["Belay wasn’t rich, so he didn’t buy a new car.", "Belay was rich, so he bought a new car.", "Belay was rich, but he didn’t buy a new car.", "Even though Belay was poor, he bought a new car."], 0,
        "The third conditional describes a past that did not happen. He was not rich, and he did not buy the car."))
    A(Q(v, "Grammar", "We sat on the floor to eat dinner and he ______ the fresh food my mother served.",
        ["had appreciated", "appreciated", "will appreciate", "no change; “appreciate” is already correct"], 1,
        "Sat is simple past, so the joined verb should also be simple past: appreciated."))
    A(Q(v, "Grammar", "Arrange: Life is never meant to / (A) country like Ethiopia / (B) be easy, especially if you / (C) live in a developing",
        ["BAC", "ACB", "BCA", "ABC"], 2,
        "The sentence is: Life is never meant to be easy, especially if you live in a developing country like Ethiopia. That order is B, C, A."))

    A(Q(v, "Vocabulary", "I passed all my exams, so my parents are very ______ of me.",
        ["proud", "calm", "ashamed", "cheerful"], 0,
        "Passing exams makes parents proud of you."))
    A(Q(v, "Vocabulary", "I’ve got lots of ______, but I think Aunt Paula and Uncle Joe are my favourites.",
        ["enemies", "partners", "classmates", "relatives"], 3,
        "An aunt and an uncle are relatives."))
    A(Q(v, "Vocabulary", "Kindly ask her to play the piano; she is a ______ pianist.",
        ["voracious", "vacuous", "volatile", "virtuoso"], 3,
        "A virtuoso is a highly skilled performer."))
    A(Q(v, "Vocabulary", "He was ______ from all the charges levelled against him.",
        ["liberated", "exonerated", "apprehended", "judged"], 1,
        "Exonerated means cleared of blame."))
    A(Q(v, "Vocabulary", "Which best expresses “hybrid”?",
        ["homogeneous", "composite", "pure", "love"], 1,
        "A hybrid is a composite, something of mixed origin."))
    A(Q(v, "Vocabulary", "Which spelling is correct?",
        ["Commiety", "Committee", "Comittee", "Committe"], 1,
        "Committee has two m’s, two t’s, and two e’s."))
    A(Q(v, "Vocabulary", "Which word means “concerned with beauty or the appreciation of beauty”?",
        ["foul", "aesthetic", "hideous", "gross"], 1,
        "Aesthetic concerns beauty. The other words describe what is unpleasant or ugly."))

    kelvin = "When you can measure ______ you are speaking about, and express it ______ numbers, you know something ______ it; when you cannot measure it, when you cannot ______ it in numbers, your knowledge is of a meagre and unsatisfactory kind; it may be the beginning of knowledge, but you have ______, in your thoughts, advanced to the stage of science."
    A(Q(v, "Summary", "When you can measure ______ you are speaking about…",
        ["when", "what", "where", "whom"], 1,
        "The thing being measured is “what you are speaking about.”", kelvin))
    A(Q(v, "Summary", "…and express it ______ numbers…",
        ["in", "to", "from", "with"], 0,
        "The standard phrase is “express it in numbers.”", kelvin))
    A(Q(v, "Summary", "…you know something ______ it…",
        ["for", "within", "about", "nearly"], 2,
        "“Know something about it” is the natural phrase.", kelvin))
    A(Q(v, "Summary", "…when you cannot ______ it in numbers…",
        ["tell", "ask", "say", "express"], 3,
        "The sentence already used “express it in numbers,” so the repeated verb is express.", kelvin))
    A(Q(v, "Summary", "…you have ______, in your thoughts, advanced to the stage of science.",
        ["immature", "scarcely", "arrogantly", "lack"], 1,
        "Scarcely means you have barely advanced to the stage of science.", kelvin))

    A(Q(qn, "Arithmetic", "(49 ÷ 7 + 5 − 4 × 6) + 18 × 6 − 5 =",
        ["91", "81", "71", "101"], 0,
        "Division and multiplication come first: 7 + 5 − 24 + 108 − 5 = 91."))
    A(Q(qn, "Sequences", "What is the next number: 3, 8, 18, 38, 78, …?",
        ["138", "156", "148", "158"], 3,
        "The gaps double: +5, +10, +20, +40, so the next gap is +80. 78 + 80 = 158."))
    A(Q(qn, "Percent", "A school plans to increase class size from 40 to 60 students. What is the percentage increase?",
        ["20%", "40%", "50%", "60%"], 2,
        "The increase is 20 students. 20 / 40 = 50%."))
    A(Q(qn, "Ratio", "Birr 480 is shared between two children in the ratio 11 : 13. How much do they get?",
        ["110 and 130", "220 and 260", "200 and 280", "210 and 230"], 1,
        "11 + 13 = 24 shares, and 480 / 24 = 20. The shares are 220 and 260."))
    A(Q(qn, "Percent", "A store buys a shoe for 90 birr and sells it at a 50% profit. What is the selling price?",
        ["120", "115", "135", "125"], 2,
        "Profit is 45 birr, so the selling price is 135 birr."))
    A(Q(qn, "Ratio", "A bus carries 60 passengers, 40 of them female. What is the ratio of male to female passengers?",
        ["2 : 3", "3 : 2", "2 : 1", "1 : 2"], 3,
        "There are 20 males. 20 : 40 simplifies to 1 : 2."))
    A(Q(qn, "Algebra", "The sum of two integers is 36 and their difference is 14. What is the larger integer?",
        ["11", "14", "36", "25"], 3,
        "Adding the equations gives 2x = 50, so the larger integer is 25."))
    A(Q(qn, "Number theory", "The product of two natural numbers is 24 and their LCM is 12. What is their HCF?",
        ["3", "2", "1", "5"], 1,
        "For two numbers, LCM × HCF = product. 12 × HCF = 24, so the HCF is 2."))
    A(Q(qn, "Sequences", "Which number completes 2, 6, 12, 20, 30, …?",
        ["36", "40", "42", "50"], 2,
        "The gaps are +4, +6, +8, +10, so the next gap is +12. 30 + 12 = 42."))
    A(Q(qn, "Geometry", "A person walks 8 km north and then 6 km east. How far is the person from the start?",
        ["8 km", "10 km", "12 km", "14 km"], 1,
        "This is a 6-8-10 right triangle. The straight-line distance is 10 km."))
    A(Q(qn, "Algebra", "Two natural numbers add to 28 and differ by 4. What is the smaller number?",
        ["12", "14", "16", "18"], 0,
        "Adding gives 2x = 32, so the numbers are 16 and 12. The smaller is 12."))
    A(Q(qn, "Ratio", "The ratio of boys to girls is 3 : 5, and there are 24 boys. How many girls are there?",
        ["64", "40", "24", "30"], 1,
        "3 parts are 24, so 1 part is 8. Girls are 5 × 8 = 40."))
    A(Q(qn, "Ratio", "Using the same class, 24 boys and girls in the ratio 3 : 5, how many students are there in total?",
        ["64", "40", "24", "30"], 0,
        "Boys are 24 and girls are 40, so the class has 64 students."))
    A(Q(qn, "Ages", "A mother is 4 times as old as her child. In 8 years she will be twice as old as the child. How old is the mother now?",
        ["4", "8", "16", "10"], 2,
        "Let the child be c. Then 4c + 8 = 2(c + 8), so c = 4 and the mother is 16."))
    A(Q(qn, "Work rates", "Three workers finish a task in 12 days. How many days will six workers need at the same rate?",
        ["4", "6", "8", "9"], 1,
        "The job is 36 worker-days. Six workers finish it in 6 days."))
    A(Q(qn, "Percent", "What is 25% of 80?",
        ["10", "15", "20", "25"], 2,
        "A quarter of 80 is 20."))
    A(Q(qn, "Sets", "Of 30 people, 18 have an engineering degree, 12 have a management degree, and 7 have both. How many have neither?",
        ["5", "7", "8", "10"], 1,
        "People with at least one degree: 18 + 12 − 7 = 23. Neither: 30 − 23 = 7."))
    A(Q(qn, "Number theory", "What is the least common multiple of 12 and 15?",
        ["45", "30", "60", "90"], 2,
        "12 = 2² × 3 and 15 = 3 × 5, so the LCM is 2² × 3 × 5 = 60."))
    A(Q(qn, "Work rates", "A man washes a car in 12 minutes. His son takes twice as long. How long do they take together?",
        ["6", "7", "10", "8"], 3,
        "Their rates are 1/12 and 1/24, which add to 1/8. Together they need 8 minutes."))
    A(Q(qn, "Algebra", "Split 50 into two parts whose reciprocals add to 1/12.",
        ["20 and 30", "24 and 26", "28 and 22", "36 and 14"], 0,
        "If the parts are a and 50 − a, then 1/a + 1/(50 − a) = 1/12. That gives a(50 − a) = 600, so the parts are 20 and 30."))
    A(Q(qn, "Algebra", "The difference of the squares of two consecutive even numbers is 84. What is their sum?",
        ["20", "22", "30", "42"], 3,
        "If the numbers are n and n + 2, then (n + 2)² − n² = 4n + 4 = 84, so n = 20. The numbers are 20 and 22, and their sum is 42."))
    A(Q(qn, "Sequences", "The 10th term of an arithmetic progression is 84 and the common difference is 8. What is the first term?",
        ["10", "13", "12", "14"], 2,
        "The 10th term is the first term plus 9 differences: a + 72 = 84, so a = 12."))
    A(Q(qn, "Number theory", "The difference between the squares of two consecutive odd integers is always divisible by:",
        ["6", "7", "5", "8"], 3,
        "Consecutive odd integers are 2k − 1 and 2k + 1. The difference of their squares is 8k, which is always divisible by 8."))
    A(Q(qn, "Counting", "How many numbers between 100 and 200 are divisible by 3?",
        ["40", "35", "33", "30"], 2,
        "The numbers run from 102 to 198. That is (198 − 102) / 3 + 1 = 33 numbers."))
    A(Q(qn, "Algebra", "What is the sum of the roots of x² − 7x + 10 = 0?",
        ["5", "7", "10", "17"], 1,
        "For x² − sx + p = 0, the sum of the roots is s. Here that sum is 7."))
    A(Q(qn, "Surds", "Simplify √98 − √50.",
        ["4√3", "2√2", "4√2", "2√3"], 1,
        "√98 = 7√2 and √50 = 5√2. The difference is 2√2."))
    A(Q(qn, "Mixtures", "A container holds 50 litres of milk. Three times in a row, 5 litres are removed and replaced with water. How much milk is left?",
        ["35.23 L", "36.45 L", "30.34 L", "34.45 L"], 1,
        "Each replacement leaves 45/50 of the milk. After three times, 50 × (0.9)³ = 36.45 litres remain."))
    A(Q(qn, "Algebra", "The digits of a two-digit number multiply to 8. Adding 18 reverses the digits. What is the number?",
        ["24", "42", "36", "40"], 0,
        "If the number is 10a + b, then ab = 8 and 10a + b + 18 = 10b + a, so b = a + 2. Then a(a + 2) = 8, and a = 2. The number is 24. Check: 24 + 18 = 42."))
    A(Q(qn, "Algebra", "If x + y = 24, what is the maximum value of xy?",
        ["120", "124", "144", "240"], 2,
        "The product is largest when the numbers are equal. Each is 12, and 12 × 12 = 144."))
    A(Q(qn, "Geometry", "The angles of a triangle are in the ratio 9 : 7 : 4. What is the largest angle?",
        ["36°", "90°", "63°", "81°"], 3,
        "The ratio has 20 parts and the angles sum to 180°, so each part is 9°. The largest angle is 9 × 9 = 81°."))
    A(Q(qn, "Geometry", "A triangle has sides 7, 10 and 5. What type is it?",
        ["equilateral", "isosceles", "scalene", "right-angled"], 2,
        "All three sides are different, so it is scalene. It is not right-angled, because 5² + 7² is not 10²."))
    A(Q(qn, "Geometry", "What is the area of a circle with radius 6 cm?",
        ["36π cm²", "12π cm²", "72π cm²", "18π cm²"], 0,
        "Area is πr² = 36π."))
    A(Q(qn, "Geometry", "A rectangle has perimeter 48 cm and its length is twice its width. What is the width?",
        ["8 cm", "12 cm", "16 cm", "18 cm"], 0,
        "2(2w + w) = 48, so 6w = 48 and the width is 8 cm."))
    A(Q(qn, "Geometry", "What is the volume of a cube with side 4 cm?",
        ["16 cm³", "32 cm³", "64 cm³", "128 cm³"], 2,
        "Volume is 4³ = 64 cm³."))
    A(Q(qn, "Geometry", "A cone has base radius 3 cm and height 4 cm. What is its volume?",
        ["12π cm³", "16π cm³", "18π cm³", "36π cm³"], 0,
        "Volume is (1/3)πr²h = (1/3)π × 9 × 4 = 12π."))
    A(Q(qn, "Rates", "A car travels 180 miles in 3 hours. What is its average speed?",
        ["30 mph", "50 mph", "60 mph", "90 mph"], 2,
        "Speed is distance divided by time: 180 / 3 = 60 mph."))
    A(Q(qn, "Geometry", "A 5 by 12 rectangle is inscribed in a circle. What is the radius of the circle?",
        ["13", "6.5", "8.5", "7"], 1,
        "The diagonal is the diameter. √(5² + 12²) = 13, so the radius is 6.5."))
    A(Q(qn, "Number theory", "How many positive divisors does 1420 have?",
        ["12", "13", "14", "15"], 0,
        "1420 = 2² × 5 × 71. The number of divisors is (2 + 1) × (1 + 1) × (1 + 1) = 12."))
    A(Q(qn, "Logarithms", "What is the value of 16^(log₄ 5)?",
        ["24", "25", "32", "20"], 1,
        "16 = 4², so 16^(log₄ 5) = (4²)^(log₄ 5) = 4^(2 log₄ 5) = (4^(log₄ 5))² = 5² = 25."))

    family = "A family has six members: E, F, G, H, I and J. E is married to F. G is the son of E. H is the brother of G. I is the sister of G. J is the father of E."
    A(Q(an, "Coding", "If CAT is written as 3120, how is DOG written?",
        ["4156", "4175", "4167", "4157"], 3,
        "Each letter is its place in the alphabet: C=3, A=1, T=20. D=4, O=15, G=7, so DOG is 4157."))
    A(Q(an, "Sequences", "Find the missing number: 2, 6, 12, 20, ?, 42.",
        ["20", "30", "22", "32"], 1,
        "The gaps are +4, +6, +8, +10, +12. The missing term is 20 + 10 = 30, and 30 + 12 = 42."))
    A(Q(an, "Family", "How is F related to J?",
        ["son", "daughter-in-law", "sister", "wife"], 1,
        "J is E’s father, and F is married to E. F is J’s daughter-in-law.", family))
    A(Q(an, "Family", "How is I related to H?",
        ["mother", "sister", "daughter", "wife"], 1,
        "I and H are both children of E, and I is female, so I is H’s sister.", family))
    A(Q(an, "Family", "E is the brother of F, F is the sister of G, and G is the father of H. How is H related to E?",
        ["son", "daughter", "nephew or niece", "cousin"], 2,
        "E and G are siblings. H is G’s child, so H is E’s nephew or niece."))
    A(Q(an, "Odd one out", "Find the odd one out: 3, 5, 9, 13, 17.",
        ["3", "9", "13", "17"], 1,
        "3, 5, 13 and 17 are prime. 9 = 3 × 3, so it is the odd one out."))
    A(Q(an, "Syllogism", "All apples are fruits. Some fruits are sweet. Which follows?",
        ["Only “all apples are sweet” follows.", "Only “some sweet things are apples” follows.", "Both follow.", "Neither follows."], 3,
        "The sweet fruits might not be apples, so neither conclusion is forced."))
    A(Q(an, "Direction", "A man walks 10 km north, turns left and walks 5 km, then turns right and walks 10 km. Where is he from the start?",
        ["north-east", "south-east", "south-west", "north-west"], 3,
        "Left from north is west. After 5 km west he turns right, so he faces north again and walks 10 km. He is 20 km north and 5 km west, which is north-west."))
    A(Q(an, "Syllogism", "All roses are flowers, and some flowers fade quickly. Which is true?",
        ["Some roses fade quickly.", "All flowers fade quickly.", "No rose fades quickly.", "None of these must be true."], 3,
        "The flowers that fade quickly might not include any roses. None of the stronger claims must be true."))
    A(Q(an, "Sets", "In a Venn diagram, elements that belong to both set E and set F are the:",
        ["union of E and F", "intersection of E and F", "difference of E and F", "symmetric difference of E and F"], 1,
        "The overlap of two sets is their intersection."))
    A(Q(an, "Sequences", "What comes next: 1A, 2B, 3C, 4D, …?",
        ["5D", "5E", "6E", "5F"], 1,
        "The number increases by 1 and the letter moves forward one place. Next is 5E."))
    A(Q(an, "Clocks", "The minute hand is on 6 and the hour hand is between 2 and 3. What time is it?",
        ["2:30", "3:30", "2:15", "3:15"], 0,
        "The minute hand on 6 means 30 minutes. The hour hand between 2 and 3 means 2:30."))
    A(Q(an, "Word play", "Rearranging the letters of IMARONA gives the name of:",
        ["a fruit", "a colour", "a country", "a city"], 2,
        "IMARONA rearranges to ROMANIA, which is a country."))
    A(Q(an, "Sequences", "What comes next: AB, BC, CD, …?",
        ["DE", "EF", "DF", "FG"], 0,
        "Each pair starts with the second letter of the previous pair. After CD comes DE."))
    A(Q(an, "Ages", "A father is twice as old as his son. Five years ago the father was three times as old as his son. What are their ages now, son and father?",
        ["5 and 10", "15 and 30", "10 and 20", "12 and 24"], 2,
        "Let the son be s. Then 2s − 5 = 3(s − 5), so s = 10 and the father is 20."))
    A(Q(an, "Ages", "Four years ago E was twice as old as F. E is 40 now. How old is F?",
        ["25", "22", "21", "18"], 1,
        "Four years ago E was 36, so F was 18 then. F is 22 now."))
    A(Q(an, "Probability", "A box has 3 red, 2 blue and 5 green balls. What is the probability of picking a red ball?",
        ["1/5", "3/10", "1/2", "3/8"], 1,
        "There are 10 balls and 3 are red, so the probability is 3/10."))
    A(Q(an, "Coding", "If CAT is written as DBU, how is DOG written?",
        ["EPH", "EPJ", "EOH", "EPI"], 0,
        "Each letter moves forward one place. D-O-G becomes E-P-H."))
    A(Q(an, "Syllogism", "Some E is F, and all F are G. Which must be true?",
        ["Some E is G.", "All E are G.", "Some G is E.", "All G are E."], 0,
        "The F’s that are also E must be G, so some E is G. The same overlap means some G is E.",
        also=[2]))
    A(Q(an, "Direction", "A man faces east. He turns 90° clockwise, then 180° anticlockwise. Which way does he face?",
        ["north", "south", "east", "west"], 0,
        "A clockwise quarter-turn from east faces him south. A half-turn anticlockwise from south faces him north."))
    A(Q(an, "Sets", "In a class of 40, 30 study maths, 25 study science, and 20 study both. How many study only maths?",
        ["15", "25", "10", "20"], 2,
        "Only maths is 30 − 20 = 10."))
    A(Q(an, "Odd one out", "Which is the odd one out?",
        ["apple", "banana", "carrot", "cherry"], 2,
        "Apple, banana and cherry are fruits. A carrot is a vegetable."))
    A(Q(an, "Syllogism", "All cats are mammals. Some mammals are not dogs. Therefore some cats are not dogs.",
        ["The conclusion must be true.", "The conclusion must be false.", "The conclusion does not follow.", "Every cat is a dog."], 2,
        "The mammals that are not dogs might not be cats. The premises do not force the conclusion."))
    A(Q(an, "Clocks", "A clock shows 3:15. What is the angle between the hands?",
        ["30°", "7.5°", "45°", "37.5°"], 1,
        "At 3:00 the hands are 90° apart. In 15 minutes the hour hand moves 7.5°, so the angle is 90 − 7.5 = 7.5°."))
    A(Q(an, "Syllogism", "Some books are pens, and some pens are not pencils. Which must be true?",
        ["Some books are pencils.", "Some pens are books.", "All pens are books.", "Some books are not pencils."], 1,
        "“Some books are pens” is the same fact as “some pens are books.” Nothing is said that forces a link between books and pencils."))

    survey = "In a survey of 25 students, 15 had taken mathematics, 12 physics and 11 chemistry. Five had taken mathematics and chemistry, 9 had taken mathematics and physics, 4 had taken physics and chemistry, and 3 had taken all three."
    A(Q(an, "Sets", "How many students had taken only mathematics?",
        ["2", "4", "5", "3"], 1,
        "Remove the overlaps from 15. Only maths and chemistry is 2, only maths and physics is 6, and all three is 3. Only mathematics is 15 − 2 − 6 − 3 = 4.", survey))
    A(Q(an, "Sets", "How many students had taken only chemistry?",
        ["2", "4", "3", "5"], 3,
        "Only chemistry is 11 − 2 − 1 − 3 = 5.", survey))
    A(Q(an, "Sets", "How many students had taken only physics?",
        ["2", "4", "5", "3"], 0,
        "Only physics is 12 − 6 − 1 − 3 = 2.", survey))
    A(Q(an, "Sets", "How many students had taken exactly one course?",
        ["10", "23", "11", "38"], 2,
        "Only maths, physics and chemistry are 4, 2 and 5. That is 11 students.", survey))
    A(Q(an, "Sets", "How many students had taken at least one of the three courses?",
        ["23", "26", "27", "24"], 0,
        "Add the only-one regions (11), the exactly-two regions (9) and the centre (3). That is 23.", survey))
    A(Q(an, "Sets", "How many students had taken none of the courses?",
        ["6", "1", "3", "2"], 3,
        "25 students were surveyed and 23 took at least one course, so 2 took none.", survey))
    A(Q(an, "Sets", "How many students had taken exactly two of the three courses?",
        ["9", "10", "11", "12"], 0,
        "Exactly two means the pairwise overlaps without the centre: (5 − 3) + (9 − 3) + (4 − 3) = 2 + 6 + 1 = 9.", survey))

    sales = "September and October sales, in birr: Branch A 150 then 180; Branch B 200 then 250; Branch C 120 then 100."
    A(Q(an, "Data", "What was the percentage increase in Branch A’s sales from September to October?",
        ["15%", "20%", "25%", "30%"], 1,
        "The increase is 30 on a base of 150, which is 20%.", sales))
    A(Q(an, "Data", "What is the ratio of Branch A’s two-month total to Branch B’s two-month total?",
        ["10 : 7", "4 : 9", "11 : 15", "12 : 11"], 2,
        "A totals 330 and B totals 450. Divide by 30 to get 11 : 15.", sales))
    return items
