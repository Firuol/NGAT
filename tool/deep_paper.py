"""Extra public NGAT and GAT practice that is not already in the other papers.

Verbal, number, and reasoning items posted for GAT practice, plus the
figure-free questions from a 2022/23 analytical sample. Each answer is
worked here.
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

    blanks = [
        ("Fate smiles ______ those who untiringly grapple with the realities of life.",
         ["with", "over", "on", "round"], 2, "The idiom is “fate smiles on” someone."),
        ("The miser gazed ______ at the pile of gold coins in front of him.",
         ["avidly", "admiringly", "thoughtfully", "earnestly"], 0, "Avidly means with greedy eagerness, which fits a miser and a pile of gold."),
        ("Catching the earlier train will give us the ______ to do some shopping.",
         ["chance", "luck", "possibility", "occasion"], 0, "“Give us the chance” is the natural phrase."),
        ("I saw a ______ of cows in the field.",
         ["group", "herd", "swarm", "flock"], 1, "A group of cows is a herd. A flock is for birds or sheep, and a swarm is for insects."),
        ("The grapes are now ______ enough to be picked.",
         ["ready", "mature", "ripe", "advanced"], 2, "Fruit that is ready to pick is ripe."),
        ("Success in this examination depends ______ hard work alone.",
         ["at", "over", "for", "on"], 3, "Depend is followed by on."),
        ("My uncle decided to take ______ and my sister to the market.",
         ["I", "mine", "me", "myself"], 2, "Take needs an object. Me is the object form."),
        ("If you smuggle goods into the country, they may be ______ by the customs authority.",
         ["possessed", "punished", "confiscated", "fined"], 2, "Customs confiscate smuggled goods. A fine is imposed on a person, not on the goods."),
        ("Man does not live by ______ alone.",
         ["food", "bread", "meals", "diet"], 1, "The proverb is “Man does not live by bread alone.”"),
        ("He behaves strangely, so nobody gets ______ with him.",
         ["about", "through", "along", "up"], 2, "“Get along with” means to have a good relationship."),
        ("They are twin brothers, but they do not look ______.",
         ["unique", "different", "likely", "alike"], 3, "Alike means similar to each other."),
        ("To err is ______; to forgive, divine.",
         ["beastly", "human", "inhuman", "natural"], 1, "The proverb says to err is human."),
        ("The ruling party will have to put its own house ______ order.",
         ["in", "on", "to", "into"], 0, "“Put one’s house in order” means to sort out one’s own affairs."),
        ("______ of old paintings is a job for experts.",
         ["Resurrection", "Retrieval", "Restoration", "Resumption"], 2, "Restoration means repairing something old so it can be seen again."),
        ("During the festival the shops are ______ of people.",
         ["busy", "full", "crowded", "bubbling"], 1, "“Full of people” is the phrase that fits “full of.”"),
    ]
    for stem, choices, answer, explanation in blanks:
        A(Q(v, "Sentence completion", stem, choices, answer, explanation))

    analogies = [
        ("CUP : LIP :: BIRD : ?", ["bush", "grass", "forest", "beak"], 3,
         "A cup is brought to the lips. A bird uses its beak in the same way."),
        ("FLOW : RIVER :: STAGNANT : ?", ["rain", "stream", "pool", "canal"], 2,
         "Water in a river flows. Water in a pool is stagnant."),
        ("PAW : CAT :: HOOF : ?", ["lamb", "elephant", "lion", "horse"], 3,
         "A cat’s foot is a paw. A horse’s foot is a hoof."),
        ("ORNITHOLOGIST : BIRD :: ARCHAEOLOGIST : ?", ["islands", "mediators", "archaeology", "aquatic"], 2,
         "An ornithologist studies birds. An archaeologist studies archaeology."),
        ("PEACOCK : INDIA :: BEAR : ?", ["Australia", "America", "Russia", "England"], 2,
         "The peacock is a national symbol of India, and the bear is a national symbol of Russia."),
        ("REASON : SFBTPO :: THINK : ?", ["SGHMJ", "UIJOL", "UHNKI", "UJKPM"], 1,
         "Each letter moves forward one place. THINK becomes UIJOL."),
        ("CARBON : DIAMOND :: CORUNDUM : ?", ["garnet", "ruby", "pearl", "emerald"], 1,
         "Diamond is a form of carbon. Ruby is a form of corundum."),
        ("NATION : ANTINO :: HUNGRY : ?", ["HNUGRY", "UHNGYR", "YRNGUH", "UNHGYR"], 1,
         "The first pair of letters is swapped, the middle pair stays, and the last pair is swapped. HU-NG-RY becomes UH-NG-YR."),
        ("ARCHITECT : BUILDING :: SCULPTOR : ?", ["museum", "stone", "chisel", "statue"], 3,
         "An architect makes a building. A sculptor makes a statue."),
        ("EYE : MYOPIA :: TEETH : ?", ["pyorrhoea", "cataract", "trachoma", "eczema"], 0,
         "Myopia is a disease of the eye. Pyorrhoea is a disease of the teeth."),
        ("BINDING : BOOK", ["criminal : gang", "display : museum", "artist : carpenter", "frame : picture"], 3,
         "A binding holds a book together. A frame holds a picture."),
        ("EXPLORE : DISCOVER", ["read : skim", "research : learn", "write : print", "sleep : wake"], 1,
         "Exploring can lead to discovering. Research can lead to learning."),
        ("SIAMESE : CAT", ["type : breed", "dog : puppy", "mark : spot", "romaine : lettuce"], 3,
         "A Siamese is a kind of cat. Romaine is a kind of lettuce."),
        ("FINCH : BIRD", ["frog : toad", "elephant : reptile", "Dalmatian : dog", "ant : ladybug"], 2,
         "A finch is a kind of bird. A Dalmatian is a kind of dog."),
        ("PETAL : FLOWER", ["salt : pepper", "tire : bicycle", "base : ball", "puppy : dog"], 1,
         "A petal is a part of a flower. A tire is a part of a bicycle."),
        ("COTTON : BALE", ["butter : churn", "wine : ferment", "grain : shock", "beef : steak"], 2,
         "Cotton is gathered in a bale. Grain is gathered in a shock."),
        ("ELEPHANT : PACHYDERM", ["mantis : rodent", "poodle : feline", "kangaroo : marsupial", "zebra : horse"], 2,
         "An elephant is a pachyderm. A kangaroo is a marsupial."),
        ("PSYCHOLOGIST : NEUROSIS", ["ophthalmologist : cataract", "dermatologist : fracture", "infant : pediatrician", "oncologist : measles"], 0,
         "A psychologist treats a neurosis. An ophthalmologist treats a cataract."),
        ("PASTORAL : RURAL", ["metropolitan : urban", "harvest : autumn", "agrarian : benevolent", "wild : agricultural"], 0,
         "Pastoral and rural mean the same kind of place. Metropolitan and urban do too."),
        ("PEDAL : BICYCLE", ["inch : yardstick", "walk : skip", "tire : automobile", "oar : canoe"], 3,
         "A pedal drives a bicycle. An oar drives a canoe."),
        ("DIVISION : SECTION", ["layer : tier", "tether : bundle", "chapter : verse", "riser : stage"], 0,
         "A division and a section are the same kind of part. A layer and a tier are too."),
        ("DEPRESSED : SAD", ["neat : considerate", "towering : cringing", "rapid : plodding", "exhausted : tired"], 3,
         "Depressed is a stronger degree of sad. Exhausted is a stronger degree of tired."),
        ("BRISTLE : BRUSH", ["arm : leg", "stage : curtain", "recline : chair", "key : piano"], 3,
         "Bristles are parts of a brush. Keys are parts of a piano."),
        ("RAIN : DRIZZLE", ["swim : dive", "hop : shuffle", "juggle : bounce", "run : jog"], 3,
         "A drizzle is light rain. A jog is a light run."),
        ("PULSATE : THROB", ["walk : run", "tired : sleep", "examine : scrutinize", "find : lose"], 2,
         "Pulsate and throb are close in meaning. Examine and scrutinize are too, with the second word stronger."),
        ("FISH : SHOAL", ["wolf : pack", "elephant : jungle", "beagle : clan", "cow : farm"], 0,
         "A group of fish is a shoal. A group of wolves is a pack."),
        ("ODOMETER : DISTANCE", ["scale : weight", "length : width", "inch : foot", "mileage : speed"], 0,
         "An odometer measures distance. A scale measures weight."),
        ("WAITRESS : RESTAURANT", ["doctor : diagnosis", "actor : role", "driver : truck", "teacher : school"], 3,
         "A waitress works in a restaurant. A teacher works in a school."),
        ("SKEIN : YARN", ["squeeze : lemon", "fire : coal", "ream : paper", "plow : acre"], 2,
         "A skein is a quantity of yarn. A ream is a quantity of paper."),
    ]
    for stem, choices, answer, explanation in analogies:
        A(Q(v, "Analogy", stem, choices, answer, explanation))

    synonyms = [
        ("CORPULENT", ["lean", "gaunt", "emaciated", "obese"], 3, "Corpulent means fat. Obese is the synonym."),
        ("BRIEF", ["limited", "small", "little", "short"], 3, "Brief means short in time or length."),
        ("EMBEZZLE", ["misappropriate", "balance", "remunerate", "clear"], 0, "To embezzle is to misappropriate money entrusted to you."),
        ("VENT", ["opening", "end", "past", "cover"], 0, "A vent is an opening that lets air or gas through."),
        ("AUGUST", ["common", "ridiculous", "dignified", "petty"], 2, "August, as an adjective, means dignified and impressive."),
        ("CANNY", ["obstinate", "handsome", "clever", "stout"], 2, "Canny means shrewd or clever."),
        ("ALERT", ["energetic", "observant", "intelligent", "watchful"], 3, "Alert means watchful and ready."),
        ("WARRIOR", ["soldier", "sailor", "pirate", "spy"], 0, "A warrior is a soldier."),
        ("DISTANT", ["far", "removed", "reserved", "separate"], 0, "Distant means far away."),
        ("ADVERSITY", ["failure", "helplessness", "misfortune", "crisis"], 2, "Adversity is misfortune or hardship."),
        ("FAKE", ["original", "imitation", "trustworthy", "loyal"], 1, "A fake is an imitation."),
        ("INDICT", ["condemn", "reprimand", "accuse", "allege"], 2, "To indict is to formally accuse."),
        ("STRINGENT", ["dry", "strained", "rigorous", "shrill"], 2, "Stringent means strict or rigorous."),
        ("LAMENT", ["complain", "comment", "condone", "console"], 0, "To lament is to express grief or complaint."),
        ("HESITATED", ["stopped", "paused", "slowed", "postponed"], 1, "To hesitate is to pause before acting."),
        ("RESCUE", ["command", "help", "defence", "safety"], 1, "To rescue is to help someone out of danger."),
        ("ATTEMPT", ["serve", "explore", "try", "explain"], 2, "An attempt is a try."),
        ("FORAY", ["maraud", "contest", "ranger", "intuition"], 0, "A foray is a raid, and to maraud is to raid."),
        ("RECKLESS", ["courageous", "rash", "bold", "daring"], 1, "Reckless means rash, acting without care for the risk."),
        ("CONSEQUENCES", ["results", "conclusions", "difficulties", "applications"], 0, "Consequences are results."),
    ]
    for stem, choices, answer, explanation in synonyms:
        A(Q(v, "Synonym", stem, choices, answer, explanation))

    idioms = [
        ("“To make a clean breast of” means",
         ["to gain prominence", "to praise oneself", "to confess without reserve", "to destroy something early"], 2,
         "To make a clean breast of something is to confess it fully."),
        ("“To keep one’s temper” means",
         ["to become hungry", "to stay in a good mood", "to preserve one’s energy", "to stay aloof"], 1,
         "Keeping your temper means not becoming angry."),
        ("“To catch a Tartar” means",
         ["to trap a wanted criminal", "to catch a dangerous person", "to meet with disaster", "to deal with someone stronger than yourself"], 3,
         "To catch a Tartar is to take on an opponent who turns out to be more than you can handle."),
        ("“To drive home” means",
         ["to find one’s roots", "to return to a place of rest", "to go back to the start", "to emphasise"], 3,
         "To drive a point home is to emphasise it."),
        ("“To have an axe to grind” means",
         ["to have a private purpose", "to fail to arouse interest", "to have no result", "to work for both sides"], 0,
         "Someone with an axe to grind has a personal motive."),
        ("“To cry wolf” means",
         ["to listen eagerly", "to give a false alarm", "to turn pale", "to keep off starvation"], 1,
         "To cry wolf is to raise a false alarm."),
        ("“To be above board” means",
         ["to have a good height", "to be honest in a deal", "to have no debts", "to try to look beautiful"], 1,
         "Above board means open and honest."),
        ("“To put one’s hand to the plough” means",
         ["to take up farming", "to take on a hard task", "to get into unnecessary trouble", "to take up technical work"], 1,
         "The phrase means to set about a serious task and keep at it."),
        ("“To pick holes” means",
         ["to find a reason to quarrel", "to destroy something", "to criticise", "to cut part of an item"], 2,
         "To pick holes is to look for faults."),
        ("“To leave someone in the lurch” means",
         ["to reach a compromise", "to be a constant annoyance", "to put someone at ease", "to desert someone in difficulty"], 3,
         "Leaving someone in the lurch means abandoning them when they need help."),
        ("“To play second fiddle” means",
         ["to be cheerful", "to reduce a senior’s importance", "to support someone else’s lead", "to drive from the back seat"], 2,
         "Playing second fiddle means taking the supporting role."),
        ("“To beg the question” means",
         ["to refer to something", "to take something for granted", "to raise objections", "to open a discussion"], 1,
         "In this traditional sense, begging the question means assuming the point that still needs to be proved."),
        ("“A man of straw” means",
         ["a man of no substance", "a very active person", "a worthy fellow", "an unreasonable person"], 0,
         "A man of straw is a person without real substance or means."),
    ]
    for stem, choices, answer, explanation in idioms:
        A(Q(v, "Idiom", stem, choices, answer, explanation))

    A(Q(qn, "Numbers", "One-third of one-fourth of a number is 15. What is three-tenths of that number?",
        ["35", "36", "45", "54"], 3,
        "One-twelfth of the number is 15, so the number is 180. Three-tenths of 180 is 54."))
    A(Q(qn, "Numbers", "Three times the first of three consecutive odd integers is 3 more than twice the third. What is the third integer?",
        ["9", "11", "13", "15"], 3,
        "Let the integers be n, n + 2 and n + 4. Then 3n = 2(n + 4) + 3, so n = 11 and the third integer is 15."))
    A(Q(qn, "Numbers", "A two-digit number and the number formed by reversing its digits differ by 36. What is the difference between the two digits?",
        ["3", "4", "9", "cannot be determined"], 1,
        "If the digits are a and b, the difference of the numbers is 9(a − b) = 36, so the digits differ by 4."))
    A(Q(qn, "Numbers", "A two-digit number and its reverse differ by 36, and the digits are in the ratio 1 : 2. What is the difference between the sum of the digits and the difference of the digits?",
        ["4", "8", "16", "none of these"], 1,
        "The digits differ by 4 and are in the ratio 1 : 2, so they are 4 and 8. Their sum is 12 and their difference is 4, and 12 − 4 = 8."))
    A(Q(qn, "Numbers", "The digits of a two-digit number add to 15 and differ by 3. What is the number?",
        ["69", "78", "96", "it cannot be determined"], 3,
        "The digits can be 9 and 6 in either order, so the number could be 69 or 96."))
    A(Q(qn, "Numbers", "The sum of the squares of three numbers is 138, and the sum of their products taken two at a time is 131. What is their sum?",
        ["20", "30", "40", "none of these"], 0,
        "(x + y + z)² = x² + y² + z² + 2(xy + yz + zx) = 138 + 262 = 400. The sum is 20."))
    A(Q(qn, "Numbers", "A two-digit number is added to the number formed by reversing its digits. The sum is always divisible by",
        ["3", "5", "9", "11"], 3,
        "The numbers 10a + b and 10b + a add to 11(a + b), which is divisible by 11."))
    A(Q(qn, "Numbers", "In a two-digit number the units digit is 2 more than the tens digit, and the number times the sum of its digits is 144. What is the number?",
        ["24", "26", "42", "46"], 0,
        "The number 10a + (a + 2) times the digit sum 2a + 2 equals 144. That holds for 24, because 24 × 6 = 144."))
    A(Q(qn, "Numbers", "A positive number increased by 17 equals 60 times its reciprocal. What is the number?",
        ["3", "10", "17", "20"], 0,
        "n + 17 = 60/n gives n² + 17n − 60 = 0, so (n + 20)(n − 3) = 0. The positive solution is 3."))
    A(Q(qn, "Numbers", "The product of two numbers is 9375, and the larger divided by the smaller is 15. What is their sum?",
        ["380", "395", "400", "425"], 2,
        "If the smaller is y, then 15y² = 9375, so y = 25 and the larger is 375. The sum is 400."))
    A(Q(qn, "Numbers", "The product of two numbers is 120 and the sum of their squares is 289. What is their sum?",
        ["20", "23", "169", "none of these"], 1,
        "(x + y)² = x² + y² + 2xy = 289 + 240 = 529. The sum is 23."))
    A(Q(qn, "Numbers", "A three-digit number has digits that add to 10. The middle digit equals the sum of the other two, and reversing the digits increases the number by 99. What is the number?",
        ["145", "253", "370", "352"], 1,
        "The middle digit is 5, so the other two add to 5. Reversing adds 99, so the units digit is 1 more than the hundreds digit. The number is 253."))
    A(Q(qn, "Numbers", "Two numbers add to 25 and differ by 13. What is their product?",
        ["104", "114", "315", "325"], 1,
        "The numbers are 19 and 6. Their product is 114."))

    A(Q(qn, "Number theory", "What is the greatest number that divides 43, 91 and 183 and leaves the same remainder in each case?",
        ["4", "7", "9", "13"], 0,
        "The number divides the differences 48, 92 and 140. Their highest common factor is 4."))
    A(Q(qn, "Number theory", "The HCF of two numbers is 23, and the other two factors of their LCM are 13 and 14. What is the larger number?",
        ["276", "299", "322", "345"], 2,
        "The numbers are 23 × 13 = 299 and 23 × 14 = 322. The larger is 322."))
    A(Q(qn, "Number theory", "Six bells toll together and then at intervals of 2, 4, 6, 8, 10 and 12 seconds. How many times do they toll together in 30 minutes, including the start?",
        ["4", "10", "15", "16"], 3,
        "They meet every 120 seconds, the LCM of the intervals. From 0 to 1800 seconds that happens 16 times."))
    A(Q(qn, "Number theory", "N is the greatest number that divides 1305, 4665 and 6905 and leaves the same remainder each time. What is the sum of the digits of N?",
        ["4", "5", "6", "8"], 0,
        "N is the HCF of the differences 3360, 2240 and 5600, which is 1120. The digits of 1120 add to 4."))
    A(Q(qn, "Number theory", "What is the greatest four-digit number divisible by 15, 25, 40 and 75?",
        ["9000", "9400", "9600", "9800"], 2,
        "The LCM of those divisors is 600. The greatest four-digit multiple of 600 is 9600."))
    A(Q(qn, "Number theory", "The product of two numbers is 4107 and their HCF is 37. What is the greater number?",
        ["101", "107", "111", "185"], 2,
        "One number is 37 and the other is 4107 / 37 = 111. Their HCF is 37, and the greater is 111."))
    A(Q(qn, "Number theory", "Three numbers are in the ratio 3 : 4 : 5 and their LCM is 2400. What is their HCF?",
        ["40", "80", "120", "200"], 0,
        "The numbers are 3k, 4k and 5k. Their LCM is 60k = 2400, so k = 40, which is also their HCF."))
    A(Q(qn, "Number theory", "What is the GCD of 1.08, 0.36 and 0.9?",
        ["0.03", "0.9", "0.18", "0.108"], 2,
        "In hundredths the numbers are 108, 36 and 90. Their GCD is 18, so the original GCD is 0.18."))
    A(Q(qn, "Number theory", "The product of two numbers is 2028 and their HCF is 13. How many such pairs are there?",
        ["1", "2", "3", "4"], 1,
        "The numbers are 13a and 13b with ab = 12 and a, b coprime. The pairs are (1, 12) and (3, 4), so there are two."))
    A(Q(qn, "Number theory", "What is the least multiple of 7 that leaves a remainder of 4 when divided by 6, 9, 15 and 18?",
        ["74", "94", "184", "364"], 3,
        "The number is 90k + 4, and it must be divisible by 7. The smallest such value is 364."))

    A(Q(qn, "Mixtures", "High-grade milk costs 40 birr a litre and low-grade milk costs 30. In what ratio, high to low, should they be mixed to make a mixture worth 36 birr a litre?",
        ["3 : 2", "2 : 3", "4 : 3", "1 : 1"], 0,
        "The gap from 36 up to 40 is 4, and the gap from 30 up to 36 is 6. High grade to low grade is 6 : 4, which is 3 : 2."))
    A(Q(qn, "Percent", "An item costs 150 birr. A 20% discount on the marked price leaves no profit and no loss. What is the marked price?",
        ["180 birr", "187.50 birr", "200 birr", "175 birr"], 1,
        "Eighty percent of the marked price is 150, so the marked price is 150 / 0.8 = 187.50."))
    A(Q(qn, "Number theory", "What is the last digit of 237^937?",
        ["1", "3", "7", "9"], 2,
        "Only the units digit 7 matters. Its powers end in 7, 9, 3, 1 and then repeat. 937 leaves a remainder of 1 when divided by 4, so the last digit is 7."))
    A(Q(qn, "Geometry", "A rectangle has sides in the ratio 3 : 2 and area 2400 cm². What is its perimeter?",
        ["180 cm", "200 cm", "220 cm", "240 cm"], 1,
        "If the sides are 3k and 2k, then 6k² = 2400 and k = 20. The sides are 60 and 40, so the perimeter is 200 cm."))
    A(Q(qn, "Interest", "The compound interest on a sum for 3 years at 10% per year is 14,895 birr. What was the sum?",
        ["45,000 birr", "42,000 birr", "36,000 birr", "48,000 birr"], 0,
        "The growth factor is 1.1³ = 1.331, so the interest is 0.331 of the sum. 14,895 / 0.331 = 45,000."))
    A(Q(qn, "Number theory", "What remainder is left when 10368^23 is divided by 5?",
        ["0", "1", "2", "3"], 2,
        "The units digit is 8. Powers of 8 end in 8, 4, 2, 6. The 23rd power ends in 2, and a number ending in 2 leaves remainder 2 when divided by 5."))
    A(Q(qn, "Percent", "Fifty percent of P is 12 more than sixty percent of Q, and P + Q = 156. What is 75% of P?",
        ["60", "72", "84", "96"], 1,
        "0.5(156 − Q) = 0.6Q + 12 gives Q = 60 and P = 96. Seventy-five percent of 96 is 72."))
    A(Q(qn, "Operations", "If + means ÷, − means +, ÷ means × and × means −, what is (78 × 45) + 3 − 45 ÷ 68 × 13?",
        ["32", "61", "508", "3058"], 3,
        "The expression becomes (78 − 45) ÷ 3 + 45 × 68 − 13 = 11 + 3060 − 13 = 3058."))
    A(Q(qn, "Sequences", "What is the average of the first five perfect squares that end in 6?",
        ["196", "216", "256", "426"], 1,
        "Those squares are 16, 36, 196, 256 and 576. Their sum is 1080 and their average is 216."))
    A(Q(qn, "Percent", "The cost of a glass piece is directly proportional to its length and inversely proportional to its width. If the length increases by 40%, by what percent should the width decrease so that the cost doubles?",
        ["20%", "30%", "40%", "50%"], 1,
        "Cost is kL/W. With length 1.4L, the new width must be 0.7W to double the cost. The width falls by 30%."))
    A(Q(qn, "Rates", "Rohan travels 30 km at 40 km/h and then 60 km in 1 hour 15 minutes. How long does the whole journey take?",
        ["120 minutes", "105 minutes", "155 minutes", "100 minutes"], 0,
        "The first part takes 45 minutes and the second takes 75 minutes. The total is 120 minutes."))
    A(Q(qn, "Interest", "What compound interest is earned on 40,000 birr for 2 years at 20% per year?",
        ["16,000 birr", "17,600 birr", "18,000 birr", "8,000 birr"], 1,
        "The sum grows by a factor of 1.2² = 1.44. The interest is 0.44 × 40,000 = 17,600."))
    A(Q(qn, "Work rates", "Ginny works twice as fast as Sunny. Ginny finishes a job in 3 hours. How long do they take together to finish a job twice as large?",
        ["2 hours", "4 hours", "6 hours", "3 hours"], 1,
        "Sunny needs 6 hours for one job. Together they finish one job in 2 hours, so a double job takes 4 hours."))
    A(Q(qn, "Geometry", "A square has the same perimeter as an equilateral triangle of side 24 cm. What is the area of the square?",
        ["324 cm²", "225 cm²", "289 cm²", "400 cm²"], 0,
        "The triangle’s perimeter is 72 cm, so the square’s side is 18 cm. Its area is 324 cm²."))
    A(Q(qn, "Rates", "In six 10-minute intervals Radha travels 10, 12, 14, 9, 5 and 15 km. What is her average speed in the intervals where her speed is between 50 and 80 km/h?",
        ["62 km/h", "66 km/h", "58 km/h", "64 km/h"], 0,
        "Those speeds are 60, 72, 84, 54, 30 and 90 km/h. The ones between 50 and 80 are 60, 72 and 54, covering 31 km in 30 minutes, which is 62 km/h."))
    A(Q(qn, "Rates", "A 10 cm candle burns at 2 cm/h until 20% is gone, then at 3 cm/h until 50% is gone. The rest then takes 2 hours. What is the average burning rate?",
        ["2.0 cm/h", "2.5 cm/h", "3.0 cm/h", "2.25 cm/h"], 1,
        "The first 2 cm take 1 hour and the next 3 cm take 1 hour. The last 5 cm take 2 hours. Ten centimetres in 4 hours is 2.5 cm/h."))
    A(Q(qn, "Ratio", "An alloy of iron, copper and silver in the ratio 7 : 3 : 1 weighs 660 kg. After 30 kg of copper and 30 kg of silver are added, what is the new ratio?",
        ["7 : 3 : 1", "14 : 7 : 3", "7 : 4 : 2", "42 : 21 : 9"], 1,
        "The original masses are 420, 180 and 60 kg. After the additions they are 420, 210 and 90, which simplifies to 14 : 7 : 3."))
    A(Q(qn, "Percent", "In a zoo, 40% of the animals are reptiles. Of the rest, 60% are mammals. If 456 animals are neither, how many animals are there?",
        ["1140", "1520", "1900", "2280"], 2,
        "Mammals are 60% of the non-reptiles, so 36% of the zoo. The remaining 24% is 456, and 456 / 0.24 = 1900."))
    A(Q(qn, "Percent", "A television costs 7,272 birr. The seller wants a 30% profit after successive discounts of 20% and 10%. What should the marked price be?",
        ["10,908 birr", "11,340 birr", "12,120 birr", "13,130 birr"], 3,
        "The selling price must be 7,272 × 1.3 = 9,453.60. After the discounts, 72% of the marked price remains, so the marked price is 9,453.60 / 0.72 = 13,130."))
    A(Q(qn, "Percent", "John buys an item for 200 birr and sells it at a 20% profit. The buyer sells it at a 10% profit, and the next buyer sells it for 280 birr. About what profit percent does the last seller make?",
        ["6%", "10%", "16%", "20%"], 0,
        "The prices are 200, then 240, then 264. The last sale at 280 is a profit of 16 on 264, about 6%."))
    A(Q(qn, "Geometry", "The two perpendicular sides of a right triangle are 14 cm and 48 cm, and all three vertices lie on a circle. What is the area of the circle?",
        ["2304π cm²", "576π cm²", "625π cm²", "2500π cm²"], 2,
        "The hypotenuse is the diameter. It is √(14² + 48²) = 50, so the radius is 25 and the area is 625π."))
    A(Q(qn, "Rates", "A train at 72 km/h crosses a pole in 10 seconds. How long does it take to overtake a 500 m train running the same way at 54 km/h?",
        ["130 seconds", "110 seconds", "120 seconds", "140 seconds"], 3,
        "The first train is 200 m long. The relative speed is 5 m/s, and the distance to gain is 700 m, which takes 140 seconds."))
    A(Q(qn, "Rates", "A thief is 200 m ahead. Mohan runs at 18 km/h and the thief at 9 km/h. After 20 seconds Mohan speeds up to 27 km/h. How long does the chase take in total?",
        ["50 seconds", "30 seconds", "45 seconds", "55 seconds"], 0,
        "In the first 20 seconds Mohan gains 50 m, leaving a gap of 150 m. At the new relative speed of 5 m/s he closes it in 30 seconds. The total is 50 seconds."))
    A(Q(qn, "Interest", "A sum earns compound interest for 3 years at 10%, then 15%, then 20%. The interest is 15,540 birr. What was the sum?",
        ["30,000 birr", "32,000 birr", "36,000 birr", "40,000 birr"], 0,
        "The growth factor is 1.1 × 1.15 × 1.2 = 1.518. The interest is 0.518 of the sum, so the sum is 15,540 / 0.518 = 30,000."))
    A(Q(qn, "Work rates", "Harry and Sharry dig a 5 m cube in 8 days, and Harry works twice as fast as Sharry. How long would Sharry alone take to dig a 10 m cube?",
        ["216 days", "192 days", "144 days", "208 days"], 1,
        "The larger cube has 8 times the volume, so together they would need 64 days. Sharry does one third of the joint work, so alone he needs 192 days."))
    A(Q(qn, "Operations", "If + means ×, − means + and × means −, what is (122 × 32) + 20 − 13?",
        ["90", "122", "1800", "1813"], 3,
        "The expression becomes (122 − 32) × 20 + 13 = 1800 + 13 = 1813."))
    A(Q(qn, "Work rates", "Twelve men and 6 women finish a job in 10 days. Three men and 6 women finish it in 25 days. How many men are needed to finish it in 5 days?",
        ["24", "30", "36", "40"], 1,
        "A man’s rate is twice a woman’s. The job is 300 woman-days, so 30 men finish it in 5 days."))
    A(Q(qn, "Averages", "Twelve players have an average height of 170 cm. Seven of them average 166 cm. What is the average height of the other five?",
        ["173.0 cm", "174.0 cm", "175.6 cm", "176.0 cm"], 2,
        "The twelve sum to 2040 cm and the seven sum to 1162 cm. The other five sum to 878 cm, and 878 / 5 = 175.6."))
    A(Q(qn, "Proportion", "The price of a diamond is proportional to the square of its weight. A 10 g piece costs 200,000 birr and is broken into pieces of 5 g, 3 g and 2 g. What is the loss?",
        ["no loss", "124,000 birr", "100,000 birr", "76,000 birr"], 1,
        "Value follows the square of the weight, so the pieces are worth 25, 9 and 4 parts out of the original 100. That is 76,000 birr, and the loss is 124,000."))

    A(Q(an, "Work rates", "Shazo solves 5 questions a minute from 2:00. Razo solves 6 a minute from 2:15. When have they solved the same number?",
        ["3:40 pm", "3:35 pm", "3:45 pm", "3:30 pm"], 3,
        "After t minutes past 2:15, 5(t + 15) = 6t, so t = 75. That is 3:30."))
    A(Q(an, "Mixtures", "A container is 75% milk and 25% water. Adding 2 litres of water makes the milk and water equal. How much milk is in the container?",
        ["5 litres", "3 litres", "6 litres", "4 litres"], 1,
        "If the container holds x litres, 0.75x = 0.25x + 2, so x = 4. The milk is 3 litres."))
    exams = "English, Mathematics, Physics and Biology are examined on Monday, Tuesday, Wednesday and Thursday, one each day. English is not on Thursday, and Physics is not on Thursday. Physics is not on Tuesday, and Mathematics is not on Tuesday. Exactly three exams come after Biology."
    A(Q(an, "Scheduling", "On which day is Physics examined?",
        ["Monday", "Wednesday", "Thursday", "Tuesday"], 1,
        "Three exams after Biology puts Biology on Monday. Thursday must then be Mathematics, Tuesday is English, and Wednesday is Physics.", exams))
    A(Q(an, "Sequences", "What is the next letter: B, 25, D, 23, G, 19, K, 13, ?",
        ["L", "P", "N", "Q"], 1,
        "The letters jump by 2, then 3, then 4, then 5. K plus 5 is P."))
    A(Q(an, "Counting", "A and E stand at the two ends of a straight line, with 3 people between them. How many people are in the line?",
        ["4", "7", "2", "5"], 3,
        "The two ends plus the three people between them make 5."))
    A(Q(an, "Inference", "Arun goes to the park on even dates. Does he go on the last day of February?",
        ["It is uncertain.", "False", "The statement is irrelevant.", "True"], 0,
        "The last day is the 28th in a common year and the 29th in a leap year. Only the 28th is an even date, so the claim is not always true."))
    A(Q(an, "Inference", "Of 20 students, 15 passed English and 18 passed mathematics. Which follows?",
        ["Both: some passed both subjects, and nobody failed both.", "Only this: some students passed both subjects.", "Only this: nobody failed both subjects.", "Neither follows."], 1,
        "At least 15 + 18 − 20 = 13 students passed both. The students who failed one subject might or might not overlap, so it is not certain that nobody failed both."))
    A(Q(an, "Family", "Johny introduces Selvia as the mother of his sister’s brother. How is Selvia related to Johny?",
        ["aunt", "niece", "mother", "sister"], 2,
        "His sister’s brother is Johny himself, or another son of the same parents. Selvia is his mother."))
    A(Q(an, "Ordering", "Stephen sits 3rd to the left of Robert. Robert is 10th from the left end and 6th from the right end. What is Stephen’s position from the right end?",
        ["8th", "9th", "7th", "6th"], 1,
        "The row has 10 + 6 − 1 = 15 people. Stephen is 7th from the left, so he is 9th from the right."))
    A(Q(an, "Inference", "Most students who cleared the final exam also cleared the entrance exam. Does it follow that the entrance exam is easier?",
        ["The claim is irrelevant.", "True", "Uncertain", "False"], 2,
        "The statement does not compare the difficulty of the two exams. The inference is not established."))
    A(Q(an, "Odd one out", "Which three belong together: 1 sector, 2 chord, 3 diagonal, 4 diameter?",
        ["1, 2 and 3", "1, 2 and 4", "1, 3 and 4", "2, 3 and 4"], 1,
        "A sector, a chord and a diameter are parts of a circle. A diagonal belongs to a polygon."))
    A(Q(an, "Direction", "West is to north-west as south-west is to",
        ["north", "east", "west", "south"], 2,
        "North-west is 45° clockwise from west. The same turn from south-west faces west."))
    A(Q(an, "Rates", "Max moves at 5 km/h for 120 minutes, with two 10-minute halts inside that time. About how far does he travel?",
        ["9 km", "12 km", "10 km", "8 km"], 3,
        "He is moving for 100 minutes, which is 5/3 hours. The distance is about 8.3 km, nearest to 8 km."))
    A(Q(an, "Geometry", "What is the greatest number of points in which a square and a rectangle can cross each other?",
        ["4", "6", "8", "infinitely many"], 2,
        "Each side of one shape can cross two sides of the other, and the greatest number of crossing points is 8."))
    A(Q(an, "Data sufficiency", "How many chocolates does Rohan have? I. He has 30% of Vishal’s chocolates. II. Together they have 65.",
        ["II alone is enough.", "I alone is enough.", "Neither is enough, even together.", "Both together are enough."], 3,
        "From both statements, Rohan has 0.3 of Vishal’s amount and the two amounts add to 65. That gives Rohan 15. Either statement alone leaves the number unknown."))
    A(Q(an, "Family", "Ram’s mother’s sister is the wife of Vikram’s father. How is Vikram related to Ram?",
        ["brother", "cousin", "father", "uncle"], 1,
        "Ram’s aunt is Vikram’s mother, so Ram and Vikram are cousins."))
    A(Q(an, "Sequences", "The series 77, 80, 85, 88, 93, 96, 101, … adds 3 and 5 in turn. What is the first term with four different digits?",
        ["1012", "1024", "1027", "1036"], 1,
        "Continuing the alternation of +3 and +5, 1024 is the first four-digit term whose digits are all different."))
    A(Q(an, "Inference", "Company X’s market share rose from 3% to 9%, and more mobiles were sold in the market in 2019 than in 2018. Which follows?",
        ["Neither claim follows.", "Both: X sold more mobiles, and its sales exactly tripled.", "Only this: X sold more mobiles in 2019 than in 2018.", "Only this: X’s sales exactly tripled."], 2,
        "A larger share of a larger market means X sold more. The sales rose by more than a factor of three, so they did not exactly triple."))
    A(Q(an, "Data sufficiency", "Is X even? I. X is the smallest prime number. II. X is less than 5.",
        ["Both statements together still do not answer it.", "II alone is enough.", "Both together are needed.", "I alone is enough."], 3,
        "The smallest prime is 2, which is even. Being less than 5 does not say whether X is even."))
    A(Q(an, "Inference", "A mango farm has 100 trees and the average yield is 1200 mangoes a tree. Which follows?",
        ["Neither claim follows.", "Both: no tree yields under 1200, and mango farming is the most profitable.", "Only this: mango farming is the most profitable.", "Only this: no tree yields under 1200."], 0,
        "An average of 1200 allows some trees to yield less. Nothing is said about other kinds of farming."))
    A(Q(an, "Family", "R has one sibling, a brother. That brother’s only sister’s husband is M’s father. How can M be related to R?",
        ["son", "aunt", "mother", "sister"], 2,
        "R is that only sister. Her husband is M’s father, so R is M’s mother."))
    row = "Seven people stand in a row. Andrew is at the leftmost end. Three people stand between Carry and Garry. Boom stands between Andrew and Carry."
    A(Q(an, "Ordering", "Who stands at the rightmost end?",
        ["Boom", "Carry", "Andrew", "Garry"], 3,
        "The only line that fits is Andrew, Boom, Carry, then three people, then Garry. Garry is at the right end.", row))
    A(Q(an, "Inference", "Alexa goes to the market every other day, and she went yesterday. Does she go exactly 4 times a week?",
        ["The claim is irrelevant.", "It is uncertain.", "True", "False"], 1,
        "Every other day is about three or four visits in a given week, depending on which day the week starts. Four times is not guaranteed."))
    A(Q(an, "Inference", "More than 95% of the people working in Tel Aviv know a martial art. Which follows?",
        ["Only this: less than 5% do not know a martial art.", "Only this: exactly 5% know something else instead.", "Neither follows.", "Both follow."], 0,
        "More than 95% knowing a martial art means fewer than 5% do not. It does not say that exactly 5% know something else."))
    code = "“We had fun” is coded lak mak nak. “We have brain” is coded mak chak sake. “Have some fun” is coded chak tek nak."
    A(Q(an, "Coding", "What is the code for “some”?",
        ["chak", "tek", "mak", "nak"], 1,
        "We is mak, fun is nak and have is chak. The remaining code in the third sentence is tek, which is some.", code))
    A(Q(an, "Syllogism", "Some bottles are bags, and all bags are pencils. Which follows?",
        ["Both: no bottle is a pencil, and some bottles are pencils.", "Neither follows.", "Only this: no bottle is a pencil.", "Only this: some bottles are pencils."], 3,
        "The bottles that are bags must be pencils, so some bottles are pencils. The claim that no bottle is a pencil contradicts that."))
    return items
