"""Further NGAT and GAT items that are not already in the other papers.

Sources: the Debre Berhan University GAT model exam, a short public GAT
sample, and NGAT statistics and coding items posted for practice.
Graph questions and items already in the bank are omitted.
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

    A(Q(v, "Synonym", "RESTIVE",
        ["restful", "restless", "crucial", "pause"], 1,
        "Restive means restless or hard to keep still."))
    A(Q(v, "Synonym", "CRAVEN",
        ["cowardly", "laziness", "politely", "arrogant"], 0,
        "Craven means cowardly."))
    A(Q(v, "Antonym", "PERFIDY",
        ["to impure", "thoroughness", "purification", "loyalty"], 3,
        "Perfidy is treachery. The opposite is loyalty."))
    A(Q(v, "Antonym", "EFFICACY",
        ["strange", "well-known", "inefficiency", "effectiveness"], 2,
        "Efficacy means effectiveness. The opposite is inefficiency."))
    A(Q(v, "Analogy", "CARPENTER : SAW",
        ["athlete : runner", "assembly : member", "mason : wall", "reaper : sickle"], 3,
        "A carpenter works with a saw. A reaper works with a sickle."))
    A(Q(v, "Analogy", "MENDACITY : HONESTY",
        ["courage : cravenness", "wickedness : lie", "money : wealth", "acclaim : truthfulness"], 0,
        "Mendacity is the opposite of honesty. Courage is the opposite of cravenness."))
    A(Q(v, "Grammar", "Anas, Umar and I ______ going.",
        ["am", "was", "are", "have been"], 2,
        "The subject is three people, so the verb is are."))
    A(Q(v, "Grammar", "If I ______ time, I would have purchased it yesterday.",
        ["had had", "would had", "would have", "had have"], 0,
        "This is a third conditional about yesterday. The if-clause needs the past perfect: had had."))

    A(Q(v, "Grammar", "Please try and do the assignment as ______ as you can.",
        ["well", "good", "possible", "soon"], 0,
        "Well is the adverb that describes how the work is done. Good is an adjective."))
    A(Q(v, "Grammar", "He should have taken more time ______ his essay.",
        ["to edit", "editing", "for edits", "to editing"], 0,
        "“Take time to edit” uses the infinitive."))
    A(Q(v, "Grammar", "“It’s good news that Rashid passed his first-year exams, ______? Let’s hope he’s ______ next year, too.”",
        ["isn’t it; succeeded", "doesn’t he; succeed", "weren’t they; succeeded", "isn’t it; successful"], 3,
        "The tag for “it’s” is “isn’t it.” After “he’s,” the word that fits is the adjective successful."))
    A(Q(v, "Grammar", "______ sure you adhere to the ethical procedures when carrying ______ your research project.",
        ["To make; off", "Making; up", "Make; out", "To make; out"], 2,
        "The sentence is an instruction, so it starts with the imperative Make. “Carry out” means perform."))
    A(Q(v, "Vocabulary", "Which word is most like “altered” in “Have you altered the introduction?”",
        ["forgotten", "selected", "composed", "amended"], 3,
        "To alter a text is to amend it."))
    A(Q(v, "Vocabulary", "Which word is most like “assume” in “I assume the tutors can help”?",
        ["suppose", "know", "doubt", "deduce"], 0,
        "To assume is to suppose something is true."))
    A(Q(v, "Vocabulary", "Which phrase uses “intense” in the usual way?",
        ["intense error", "intense formula", "intense funds", "intense pain"], 3,
        "Pain is commonly described as intense. The other pairings are not."))
    A(Q(v, "Vocabulary", "Which phrase uses “relief” in the usual way?",
        ["breath of relief", "sigh of relief", "gasp of relief", "noise of relief"], 1,
        "The set phrase is “a sigh of relief.”"))
    A(Q(v, "Grammar", "Is that ______ “8” or ______ “B”? I can’t read it.",
        ["a; an", "an; an", "an; a", "a; the"], 2,
        "“Eight” starts with a vowel sound, so it takes an. “Bee” starts with a consonant sound, so it takes a."))
    A(Q(v, "Grammar", "We huddled together for warmth ______ the blankets.",
        ["along", "besides", "into", "beneath"], 3,
        "They were under the blankets, so the preposition is beneath."))
    A(Q(v, "Grammar", "There were very ______ people on the beach, so nobody saw the child drowning.",
        ["much", "a fewer", "few", "very little"], 2,
        "People is a plural countable noun. “Very few people” is the correct phrase."))
    A(Q(v, "Grammar", "Would you like ______ bread?",
        ["a collection of", "a bunch of", "a loaf of", "a can of"], 2,
        "Bread is measured as a loaf."))
    A(Q(v, "Grammar", "There is ______ butter left. We need to buy ______ more.",
        ["few; any", "little; some", "much; many", "few; some"], 1,
        "Butter is uncountable, so the quantity word is little, and the extra amount is some."))
    A(Q(v, "Grammar", "Which sentence about glittering is correct?",
        ["All that glitters is not gold.", "All these glitters is not gold.", "All that glitters are not gold.", "All glittering is not gold."], 0,
        "“That” is singular here, so the verb is is. The proverb is “All that glitters is not gold.”"))
    A(Q(v, "Grammar", "She has been ______ to music all day.",
        ["listening", "listened", "listens", "listen"], 0,
        "“Has been” is followed by the present participle: listening."))
    A(Q(v, "Grammar", "When I came to this city, I ______ anyone.",
        ["haven’t known", "didn’t know", "wasn’t knowing", "wouldn’t knowing"], 1,
        "“When I came” is a finished past time, so the verb is the simple past didn’t know."))
    A(Q(v, "Grammar", "Which sentence about being ready is correct?",
        ["One should keep oneself ready for an emergency.", "One should kept himself or herself ready for an emergency.", "One should be keeping himself ready for an emergency.", "One should keep himself to herself ready for an emergency."], 0,
        "“One” is followed by oneself, and the verb after should is the base form keep."))
    A(Q(v, "Grammar", "Did you just ______ me a liar?",
        ["call", "called", "have called", "calling"], 0,
        "After did, the verb stays in the base form: call."))
    A(Q(v, "Grammar", "Those newspapers ______ in a big truck.",
        ["are delivering", "is deliver", "are delivered", "had delivered"], 2,
        "The newspapers receive the action, and the subject is plural, so the verb is are delivered."))

    A(Q(qn, "Algebra", "If a + 2b = x and a − 2b = y, which expression equals ab?",
        ["(x² − y²) / 8", "(x² + y²) / 8", "(x − y) / 4", "(x + y) / 2"], 0,
        "Adding the equations gives a = (x + y) / 2. Subtracting gives b = (x − y) / 4. Their product is (x² − y²) / 8."))
    A(Q(qn, "Algebra", "Two integers add to 42 and differ by 22. What is the greater integer?",
        ["25", "32", "8", "10"], 1,
        "Adding the two facts gives 2x = 64, so the greater integer is 32."))
    A(Q(qn, "Algebra", "If a² = 17, what is (a + 1)(a − 1)?",
        ["15", "12", "16", "9"], 2,
        "(a + 1)(a − 1) = a² − 1 = 16."))
    A(Q(qn, "Algebra", "Abebe, Beletu and Omar paid 490 dollars for a laptop. Abebe paid 50 dollars more than Beletu, and Beletu paid twice what Omar paid. How much did Abebe pay?",
        ["108", "176", "226", "295"], 2,
        "Let Omar pay o. Then Beletu pays 2o and Abebe pays 2o + 50. The total is 5o + 50 = 490, so o = 88 and Abebe pays 226."))
    A(Q(qn, "Averages", "An office has 30 trainees and one team lead. The average age of all 31 people is 27. Leaving out the team lead lowers the average by 1 year. How old is the team lead?",
        ["54", "55", "56", "57"], 3,
        "The whole group sums to 31 × 27 = 837. The 30 trainees average 26, so they sum to 780. The lead is 837 − 780 = 57."))
    A(Q(qn, "Averages", "Nineteen friends paid 120 dollars each for movie tickets. The twentieth friend paid 38 dollars more than the average paid by all twenty. What did the twenty friends pay altogether?",
        ["2438", "2440", "2204", "2140"], 1,
        "Let the total be T. Then T = 19 × 120 + T/20 + 38. So (19/20)T = 2318 and T = 2440."))
    A(Q(qn, "Operations", "A means ×, B means ÷, C means +, and D means −. What is 306 B 34 A 7 D 7 C 5?",
        ["32", "61", "54", "43"], 1,
        "The expression is 306 ÷ 34 × 7 − 7 + 5. Division and multiplication come first: 9 × 7 = 63, then 63 − 7 + 5 = 61."))
    A(Q(qn, "Number theory", "What is the sum of all the positive factors of 28?",
        ["56", "55", "28", "68"], 0,
        "The factors are 1, 2, 4, 7, 14 and 28. They add to 56."))
    A(Q(qn, "Percent", "In an election, 20% of 4,850 votes were invalid. One candidate received 35% of the valid votes. How many valid votes did the other candidate receive?",
        ["2502", "2512", "2522", "2436"], 2,
        "Valid votes are 80% of 4850, which is 3880. The other candidate received 65% of those: 0.65 × 3880 = 2522."))
    A(Q(qn, "Ratio", "A, B and C share 669 so that A : B = 17 : 27 and B : C = 2 : 5. What is C’s share?",
        ["135", "270", "223", "405"], 3,
        "Make B the same in both ratios: A : B : C = 34 : 54 : 135. Those parts sum to 223, and 669 / 223 = 3, so C gets 135 × 3 = 405."))
    A(Q(qn, "Work rates", "A team finishes a job in 20 days. With the team leader, the same job takes 15 days. How long would the leader take alone?",
        ["20 days", "60 days", "40 days", "80 days"], 1,
        "The leader’s rate is 1/15 − 1/20 = 1/60. Alone, the leader needs 60 days."))
    A(Q(qn, "Percent", "B is 5/2 times A. A is what percent of B?",
        ["40%", "20%", "60%", "50%"], 0,
        "A = (2/5)B, and 2/5 is 40%."))
    A(Q(qn, "Ages", "Five children were born 3 years apart. Their ages sum to 50. How old is the youngest?",
        ["16", "12", "4", "7"], 2,
        "The ages are x, x + 3, x + 6, x + 9 and x + 12. They sum to 5x + 30 = 50, so x = 4."))
    A(Q(qn, "Logarithms", "If log 2 = 0.3010, what is log₅ 512, to three decimal places?",
        ["2.870", "2.967", "3.876", "3.912"], 2,
        "512 = 2⁹, so log₅ 512 = 9 log 2 / log 5 = 9 × 0.3010 / 0.6990 ≈ 3.876."))
    A(Q(qn, "Algebra", "Sending 10 students from room A to room B makes the rooms equal. Sending 20 from B to A makes A twice B. How many students are in room A at the start?",
        ["20", "60", "80", "100"], 3,
        "Let A start with a and B with b. Then a − 10 = b + 10, and a + 20 = 2(b − 20). Solving gives a = 100 and b = 80."))
    A(Q(qn, "Algebra", "The price of 10 chairs equals the price of 4 tables. Fifteen chairs and 2 tables cost 4000 birr. What do 12 chairs and 3 tables cost?",
        ["3500", "3900", "3750", "3840"], 1,
        "Ten chairs match four tables, so one table costs the same as 2.5 chairs. Then 15 chairs + 2 tables = 20 chairs = 4000, so a chair is 200 and a table is 500. Twelve chairs and three tables cost 3900."))
    A(Q(qn, "Percent", "Each side of a rectangle is increased by 20%. By what percent does the area increase?",
        ["40%", "42%", "44%", "46%"], 2,
        "The new area is 1.2 × 1.2 = 1.44 times the old area, which is an increase of 44%."))
    A(Q(qn, "Rates", "A train at 60 km/h crosses a pole in 9 seconds. How long is the train?",
        ["180 m", "324 m", "120 m", "150 m"], 3,
        "60 km/h is 50/3 metres per second. In 9 seconds the train covers 150 metres, which is its own length."))
    A(Q(qn, "Clocks", "From 8:00 in the morning to 2:00 in the afternoon, through how many degrees does the hour hand turn?",
        ["180°", "168°", "150°", "144°"], 0,
        "That interval is 6 hours. The hour hand moves 30° per hour, so it turns 180°."))
    A(Q(qn, "Geometry", "A square of side 2 m has its corners cut off so that the result is a regular octagon. What is the side of the octagon?",
        ["√2 / (√2 + 1)", "2 / (√2 + 1)", "2 / (√2 − 1)", "√2 / (√2 − 1)"], 1,
        "If a length x is cut from each end of a side, the remaining side is 2 − 2x and each new edge is x√2. Setting them equal gives x = 2 − √2, and the octagon side is 2(√2 − 1), which equals 2 / (√2 + 1)."))
    A(Q(qn, "Geometry", "A ladder leans against a wall with its top 8 m above the ground. Moving the foot 2 m farther from the wall brings the top down to the foot of the wall. How long is the ladder?",
        ["10 m", "12 m", "15 m", "17 m"], 3,
        "Let the length be L. At first the foot is L − 2 from the wall, so (L − 2)² + 8² = L². That gives L = 17."))
    A(Q(qn, "Geometry", "A 6 m by 2 m pool is surrounded by a walkway of uniform width. The walkway has area 48 m². How wide is it?",
        ["4 m", "3 m", "2 m", "1 m"], 2,
        "If the width is w, then (6 + 2w)(2 + 2w) − 12 = 48. This simplifies to w² + 4w − 12 = 0, so w = 2."))
    A(Q(qn, "Statistics", "The mean of a distribution is 48 more than the mode, and the median is 12. What is the mean? Use mode = 3 × median − 2 × mean.",
        ["28", "38", "42", "52"], 0,
        "Mode = 3 × 12 − 2 × mean = 36 − 2 × mean. Then mean − mode = 3 × mean − 36 = 48, so the mean is 28."))

    exams = "Six exams — English, Mathematics, History, Physics, Chemistry and Biology — run on Monday through Saturday, one each day. Physics is not on Wednesday, and Mathematics is not on Wednesday. Exactly two exams come after Biology. Exactly two exams come between Biology and English. Chemistry is not on Friday, and Mathematics is not on Friday. Exactly three exams come between Physics and Mathematics, and Mathematics comes after Biology."
    A(Q(an, "Scheduling", "On which day is the History exam?",
        ["Tuesday", "Wednesday", "Thursday", "Friday"], 3,
        "Two exams after Biology puts Biology on Thursday, so English, two days before it, is on Monday. Mathematics is after Biology and not on Friday, so it is on Saturday, and Physics is on Tuesday. Friday is then History.", exams))

    A(Q(an, "Inference", "In a rain-affected match, Team A beat Team B by 50 runs under the Duckworth–Lewis rule. Which inference follows?",
        ["Only this: Duckworth–Lewis is a rule used to decide a rain-affected match.", "Only this: Team B batted first.", "Both of those follow.", "Neither follows."], 0,
        "The statement uses the rule to settle a rain-affected match, so the first inference follows. A win by runs means the winner batted first, so Team B did not bat first."))
    A(Q(an, "Logic", "Garry skipped one number while counting from 1 to 10. It was even, greater than 3 and less than 9, and upside down it looks like a different digit. Which number was it?",
        ["2", "6", "4", "8"], 1,
        "The even numbers in that range are 4, 6 and 8. Turned upside down, 6 looks like 9."))
    A(Q(an, "Odd one out", "Which of these does not belong with the others?",
        ["goggles", "spectacles", "bifocals", "optical readers"], 3,
        "Goggles, spectacles and bifocals are worn over the eyes. An optical reader is a device."))
    A(Q(an, "Sequences", "139 is related to 228, and 122 is related to 211. What is related to 2 in the same way?",
        ["189", "91", "198", "89"], 1,
        "Each second number is 89 more than the first. 2 + 89 = 91."))

    prof = "Seven professors, A through G, teach History, Geography, Physics, Chemistry, Maths, Biology and English from Monday to Friday. Each professor teaches one subject, and at most two subjects are taught on any day. Chemistry is taught by B on Tuesday. D teaches on Friday, but teaches neither Geography nor Physics. F teaches History, but not on Thursday or Friday. A teaches English on the same day as History. C teaches Maths on Monday. Geography and Chemistry are taught on the same day. G teaches on Thursday."
    A(Q(an, "Scheduling", "On which day is English taught?",
        ["Wednesday", "Monday", "Tuesday", "It cannot be determined"], 0,
        "Tuesday already has Chemistry and Geography. History cannot share Monday with Maths without making a third class, so History and English are both on Wednesday.", prof))
    A(Q(an, "Scheduling", "Which subject does professor G teach?",
        ["Biology", "Geography", "Physics", "Chemistry"], 2,
        "D teaches Biology on Friday, E teaches Geography on Tuesday, and the remaining subject on Thursday is Physics, taught by G.", prof))
    A(Q(an, "Scheduling", "On which day is Geography taught?",
        ["Monday", "Tuesday", "Wednesday", "Thursday"], 1,
        "Geography is taught on the same day as Chemistry, and Chemistry is on Tuesday.", prof))
    A(Q(an, "Scheduling", "Which subject is taught on Friday?",
        ["Physics", "History", "Geography", "Biology"], 3,
        "Friday’s teacher is D, and the only subject still open for D is Biology.", prof))
    A(Q(an, "Scheduling", "Which pair teaches on Tuesday?",
        ["B and D", "A and B", "B and F", "None of these"], 3,
        "Tuesday is Chemistry with B and Geography with E. E is not in the listed pairs.", prof))

    A(Q(an, "Direction", "Abebech walks 75 m north, turns left and walks 25 m, turns left and walks 80 m, then turns right through 45°. Which way is she facing at the end?",
        ["south-west", "north-west", "south", "north-east"], 0,
        "The second left turn faces her south. A right turn of 45° from south faces her south-west."))
    A(Q(an, "Syllogism", "Only a few designers are painters. No painter is a writer. All designers are singers. Which follows?",
        ["Only this: some painters could be writers.", "Only this: some singers are not writers.", "Both follow.", "Neither follows."], 1,
        "No painter is a writer, so the first claim is impossible. Some designers are painters, and every designer is a singer, so those people are singers who are not writers."))
    A(Q(an, "Coding", "“564” means “study very hard,” “736” means “hard work pays,” and “423” means “study and work.” What is the code for “work”?",
        ["5", "6", "3", "4"], 2,
        "“Hard” is the shared word of the first two codes, so hard is 6. “Study” is shared by the first and third, so study is 4. “Work” is the remaining shared digit of the second and third codes, which is 3."))
    A(Q(an, "Word play", "If the letters of PRODUCT are arranged in alphabetical order, which letter is farthest from the second letter of that new order?",
        ["T", "U", "P", "R"], 1,
        "Alphabetical order is C, D, O, P, R, T, U. The second letter is D. Among the choices, U is farthest from D."))
    A(Q(an, "Family", "S and K are brothers. W is S’s mother. T is K’s son, and M is T’s mother. How is W related to M?",
        ["mother-in-law", "sister", "father-in-law", "mother"], 0,
        "W is also K’s mother. M is K’s wife, so W is M’s mother-in-law."))
    A(Q(an, "Sequences", "What is the missing term: 8, 13, 21, 34, 55, ?, 144?",
        ["21", "34", "55", "89"], 3,
        "Each term is the sum of the two before it. 34 + 55 = 89, and 55 + 89 = 144."))
    A(Q(an, "Odd one out", "Which number does not belong with the others?",
        ["63", "42", "27", "7"], 2,
        "63, 42 and 7 are multiples of 7. 27 is not."))

    street = "Seven people live in a line of seven houses. A lives in a corner house. C lives between E and G. There is one house between D and F. F lives next to G. There are two houses between A and G."
    A(Q(an, "Ordering", "Who lives in the middle house?",
        ["C", "D", "E", "G"], 3,
        "Both arrangements that fit the rules put G in house 4, the middle house.", street))
    A(Q(an, "Ordering", "Who lives between B and G?",
        ["C", "D", "E", "F"], 3,
        "In both valid lines, F is the person between B and G.", street))
    A(Q(an, "Ordering", "Who is a neighbour of A?",
        ["B", "C", "E", "G"], 2,
        "A is at one end, and E is next to A in both valid lines.", street))
    A(Q(an, "Ordering", "How many houses are between B and E?",
        ["0", "1", "2", "3"], 3,
        "B and E have three houses between them in both valid lines.", street))

    A(Q(an, "Coding", "If A = 1 and PAT = 37, what is TAP?",
        ["73", "37", "36", "28"], 1,
        "The code is the sum of alphabet positions. P + A + T = 16 + 1 + 20 = 37, and T + A + P is the same sum."))
    A(Q(an, "Coding", "If D = 4 and BAD = 7, what is ANT?",
        ["8", "17", "35", "37"], 2,
        "B + A + D = 2 + 1 + 4 = 7. A + N + T = 1 + 14 + 20 = 35."))
    A(Q(an, "Coding", "If Z = 26 and NET = 39, what is NUT?",
        ["50", "53", "55", "56"], 2,
        "N + E + T = 14 + 5 + 20 = 39. N + U + T = 14 + 21 + 20 = 55."))
    A(Q(an, "Coding", "If F = 6 and MAT = 34, what is CAR?",
        ["21", "22", "25", "28"], 1,
        "M + A + T = 13 + 1 + 20 = 34. C + A + R = 3 + 1 + 18 = 22."))
    A(Q(an, "Coding", "If RAMAN is written 12325 and DINESH is written 675489, how is HAMAM written?",
        ["92233", "92323", "93322", "93232"], 1,
        "The digits give the letters: R=1, A=2, M=3, N=5, D=6, I=7, E=4, S=8, H=9. HAMAM is 9, 2, 3, 2, 3."))
    A(Q(an, "Coding", "If A = 26 and SUN = 27, what is CAT? Here A is 26, B is 25, and so on down to Z = 1.",
        ["24", "57", "58", "27"], 1,
        "Reversed positions: S = 8, U = 6, N = 13, and 8 + 6 + 13 = 27. C = 24, A = 26, T = 7, and 24 + 26 + 7 = 57."))

    A(Q(qn, "Statistics", "Which display is not appropriate for nominal data?",
        ["relative frequency table", "scatter plot", "pie chart", "bar graph"], 1,
        "A scatter plot needs two numeric variables. Nominal categories can be shown in a table, a pie chart or a bar graph."))
    A(Q(qn, "Statistics", "Which is not an advantage of a diagram compared with a table?",
        ["It can show a trend.", "It is more attractive.", "It is more accurate.", "It makes a quick impression."], 2,
        "A diagram is easier to look at, but a table keeps the exact figures. Accuracy is the table’s advantage."))
    A(Q(qn, "Statistics", "What does the vertical axis of a histogram represent?",
        ["cumulative frequency", "relative cumulative frequency", "the true upper limit", "frequency"], 3,
        "In a histogram the height of each bar is the frequency of that class."))
    A(Q(qn, "Statistics", "Which is not a feature of the mean?",
        ["It is affected by extreme values.", "Every value helps determine it.", "It is used for nominal data as well as continuous data.", "A data set has only one mean."], 2,
        "The mean needs numeric data. It is not used for nominal categories such as colours or names."))
    A(Q(qn, "Statistics", "When the mean, median and mode of a data set differ, which summary is appropriate?",
        ["median and quartiles", "mean and standard deviation", "median and standard deviation", "mean and quartiles"], 0,
        "A gap between mean, median and mode means the data are skewed. The median and the quartiles describe a skewed set without being pulled by the tail."))
    A(Q(qn, "Statistics", "Which of these is measured on a nominal scale?",
        ["height of a mountain above sea level", "height of a person", "weight of a stone", "colour of a person’s eyes"], 3,
        "Colour is a name, with no order and no numeric size. The other three are measurements."))
    A(Q(qn, "Statistics", "Which of these belongs to descriptive statistics?",
        ["generalisation", "data collection", "inference", "hypothesis testing"], 1,
        "Descriptive statistics collects, organises and summarises data. Inference, hypothesis testing and generalisation go beyond the data in hand."))
    A(Q(qn, "Statistics", "Which measure of spread depends only on the largest and smallest values?",
        ["median", "mode", "mean", "range"], 3,
        "The range is the largest value minus the smallest value."))
    A(Q(qn, "Statistics", "When the mean, median and mode are the same, which summary is appropriate?",
        ["median and quartiles", "mean and standard deviation", "median and standard deviation", "mean and quartiles"], 1,
        "Equal mean, median and mode is the symmetric case. The mean and the standard deviation are then a suitable pair."))
    A(Q(qn, "Statistics", "Which is not appropriate for ordinal data?",
        ["mode", "mean", "median", "both mean and median"], 1,
        "Ordinal data have an order but not equal gaps, so the mean is not appropriate. The mode and the median are."))
    A(Q(qn, "Statistics", "Which is not part of descriptive statistics?",
        ["generalisation", "data collection", "data presentation", "summarising"], 0,
        "Collection, presentation and summary describe the data. A generalisation goes beyond them."))
    A(Q(qn, "Statistics", "Four students have a median score of 8. The highest score then increases by 2. What is the new median?",
        ["8", "8.5", "10", "8.2"], 0,
        "The median depends on the middle positions, not on the highest score. It stays 8."))
    A(Q(qn, "Statistics", "A distribution has mode 7, median 8 and mean 9. How is it shaped?",
        ["skewed negatively", "not skewed", "skewed positively", "bimodal"], 2,
        "The mean is pulled above the median, which is the pattern of a positive skew."))
    A(Q(qn, "Statistics", "Which measure of centre is most influenced by an extreme score?",
        ["median", "mode", "mean", "range"], 2,
        "One extreme score moves the mean. The median and the mode can stay where they were. The range is a measure of spread, not of centre."))
    A(Q(qn, "Statistics", "In a class of 60, the mean biostatistics score is 70 and the median is 55. What should you expect?",
        ["Many students scored below the mean.", "Many students scored above the mean.", "Half the students scored above 70.", "Half the students scored below 70."], 0,
        "The mean is well above the median, so a few high scores are pulling it up and more of the scores sit below the mean."))
    A(Q(qn, "Statistics", "Which measure of centre is sensitive to extreme scores at either end?",
        ["median", "mean", "mode", "range"], 1,
        "The mean uses every score, so a very high or very low score changes it."))
    A(Q(qn, "Statistics", "The largest of 12 scores is increased by 36. What happens to the mean?",
        ["It increases by 12.", "It stays the same.", "It increases by 3.", "It increases by 36."], 2,
        "The total increases by 36 and there are 12 scores, so the mean increases by 36 / 12 = 3."))
    A(Q(qn, "Statistics", "Of ten students, 3 scored 4, 4 scored 5, 2 scored 9 and 1 scored 10. What is the mean?",
        ["3.8", "6", "5", "4"], 1,
        "The total is 3 × 4 + 4 × 5 + 2 × 9 + 10 = 60. The mean is 60 / 10 = 6."))
    A(Q(qn, "Statistics", "The scores are 4, 6, 8, 9, 11, 13, 16, 24, 24, 24, 26. The 16 is corrected to 19. Which index changes?",
        ["median", "mode", "range", "standard deviation"], 3,
        "The middle score stays 13, the mode stays 24, and the smallest and largest scores stay 4 and 26. Changing 16 to 19 does change the standard deviation."))
    return items
