import time
import re
import json

from selenium import webdriver


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


exFile = open("examples.txt", "a", encoding="UTF-8")
driver = webdriver.Firefox()

allType = ["verb", "noun", "adjective", "adverb", "prefix", "abbreviation", "symbol", "article", "suffix",
           "conjunction", "preposition", "exclamation"]

wordList = ["Abandon", "Keen", "jealous", "tact", "oath", "vacant", "hardship", "gallant", "data", "unaccustomed",
            "bachelor", "qualify", "Corpse", "conceal", "dismal", "frigid", "inhabit", "numb", "peril", "recline",
            "shriek",
            "sinister", "tempt", "wager", "typical", "minimum", "scarce", "annual", "persuade", "essential", "blend",
            "visible", "expensive", "talent", "devise", "wholesale", "Vapor", "eliminate", "villain", "dense",
            "terminator",
            "utilize", "humid", "validation", "theory", "descend", "circulate", "enormous", "ambitions", "predict",
            "vanish", "Tradition", "Rural", "absorbance", "Burden", "campus", "majority", "assemble", "explore",
            "topic",
            "debate", "evade", "probe", "generation", "generation time", "reform", "approach", "detect",
            "mixed cropping",
            "minor groove", "pest", "Possible", "Compel", "Awkward", "Venture", "Awesome", "signaling", "Guide",
            "Quench",
            "defect", "Betray", "employee", "neglect", "deceive", "undoubtedly", "popular", "thorough", "client",
            "Collaboration", "Yet", "comprehensive", "catalysis", "catalyst", "defraud", "cascade", "Utter", "Pacify",
            "Respond", "acclaimed", "especially", "goodbye", "Postpone", "consent", "massive", "capsule", "preserve",
            "denounce", "unique", "torrent", "resent", "molest", "gloomy", "unforeseen", "Exaggerate", "amateur",
            "mediocre", "variety", "valid", "survive", "weird", "prominent", "security", "bulky", "reluctant",
            "obvious",
            "Vicinity", "Century", "rage", "document", "conclude", "undeniable", "resist", "lack", "ignore",
            "challenge",
            "miniature", "source", "Excel", "Feminine", "mount", "compete", "dread", "masculine", "menace", "tendency",
            "underestimate", "victorious", "numerous", "flexible", "evidence", "solitary", "vision", "frequent",
            "glimpse",
            "recent", "decade", "hesitate", "absurd", "conflict", "minority", "fiction", "ignite", "abolish", "urban",
            "population", "frank", "pollute", "reveal", "prohibit", "urgent", "adequate", "decrease", "audible",
            "Journalist", "famine", "revive", "commence", "observant", "identify", "migrate", "vessel", "persist",
            "hazy",
            "gleam", "editor", "Unruly", "rival", "violent", "brutal", "opponent", "brawl", "duplicate", "vicious",
            "whirling", "underdog", "thrust", "bewildered", "expand", "alter", "mature", "sacred", "revise", "pledge",
            "casual", "pursue", "unanimous", "fortunate", "pioneer", "innovative", "slender", "surpass", "vast",
            "doubt",
            "capacity", "penetrate", "pierce", "accurate", "microscope", "grateful", "cautious", "confident", "appeal",
            "addict", "wary", "aware", "misfortune", "avoid", "wretched", "keg", "nourish", "harsh", "quantity", "opt",
            "Tragedy", "pedestrian", "glance", "budget", "nimble", "manipulate", "reckless", "horrid", "rave",
            "economical",
            "lubricate", "ingenious", "harvest", "abundant", "uneasy", "calculate", "absorb", "estimate", "morsel",
            "quota",
            "threat", "ban", "panic", "appropriate", "emerge", "jagged", "linger", "ambush", "crafty", "defiant",
            "vigor",
            "perish", "fragile", "captive", "proper", "devour", "Plea", "Weary", "Collide", "Confirm", "Verify",
            "Anticipate", "Dilemma", "Detour", "Merit", "Transmit", "Relieve", "baffle", "Warden", "Acknowledge",
            "Justice",
            "Delinquent", "Reject", "Deprive", "Spouse", "Vocation", "Unstable", "Homicide", "Penalize", "beneficiary",
            "Reptile", "Rarely", "Forbid", "Logical", "Exhibit", "Proceed", "Precaution", "Extract", "Prior", "Embrace",
            "Valiant", "partial", "Fierce", "Detest", "Sneer", "Scowl", "Encourage", "Consider", "Vermin", "Wail",
            "Symbol",
            "Authority", "Neutral", "trifle", "Architect", "Matrimony", "Baggage", "Squander", "Abroad", "Fugitive",
            "Calamity", "Pauper", "Envy", "Collapse", "Prosecute", "bigamy", "beckon", "Despite", "Disrupt", "Rash",
            "Rapid", "Exhaust", "Severity", "Feeble", "Unite", "Cease", "Thrifty", "Miserly", "monarch", "Outlaw",
            "Promote", "Undernourished", "Illustrate", "Disclose", "Excessive", "Disaster", "Censor", "Culprit",
            "Juvenile",
            "Bait", "insist", "Toil", "Blunder", "Daze", "Mourn", "Subside", "Maim", "Comprehend", "Commend", "Final",
            "Exempt", "Vain", "repetition", "Depict", "Mortal", "Novel", "Occupant", "Appoint", "Quarter", "Site",
            "Quote",
            "Verse", "Morality", "Roam", "attract", "Commuter", "Confine", "Idle", "Idol", "Jest", "Patriotic",
            "Dispute",
            "Valor", "Lunatic", "Vein", "Uneventful", "fertile", "Refer", "Distress", "Diminish", "Maximum", "Flee",
            "Vulnerable", "Signify", "Mythology", "Provide", "Colleague", "Torment", "loyalty", "Volunteer",
            "Prejudice",
            "Shrill", "Jolly", "Witty", "Hinder", "Lecture", "abuse", "Mumble", "mute", "Wad", "retain", "Candidate",
            "Precede", "Adolescent", "Coeducational", "Radical", "Spontaneous", "Skim", "Vaccinate", "Untidy",
            "Utensil",
            "Sensitive", "temperate", "Vague", "Elevate", "Lottery", "Finance", "Obtain", "Cinema", "Event", "Discard",
            "Soar", "Subsequent", "Relate", "stationary", "Prompt", "Hasty", "Scorch", "Tempest", "soothe",
            "Sympathetic",
            "Redeem", "resume", "Harmony", "Refrain", "Illegal", "narcotic", "heir", "Majestic", "Dwindle", "Surplus",
            "Traitor", "Deliberate", "Vandal", "Drought", "Abide", "Unify", "Summit", "heed", "Biography", "Drench",
            "Swarm", "Wobble", "Tumult", "Kneel", "Dejected", "Obedient", "Recede", "Tyrant", "Charity", "verdict",
            "Unearth", "Depart", "Coincide", "Cancel", "Debtor", "Legible", "Placard", "Contagious", "Clergy",
            "Customary",
            "Transparent", "scald", "Epidemic", "Obesity", "Magnify", "Chiropractor", "Obstacle", "Ventilate",
            "Jeopardize",
            "Negative", "Pension", "Vital", "Municipal", "oral", "Complacent", "Wasp", "Rehabilitate", "Parole",
            "Vertical",
            "Multitude", "Nominate", "Potential", "Morgue", "Preoccupied", "Upholstery", "indifference", "Maintain",
            "Snub",
            "Endure", "Wrath", "Expose", "Legend", "Ponder", "Resign", "drastic", "Wharf", "Amend", "ballot"]

examplesDic = {}
i = 1
for w in wordList:
    driver.get("https://translate.google.com/#view=home&op=translate&sl=en&tl=fa&text=" + str.lower(w))
    time.sleep(0.4)
    mores = driver.find_elements_by_class_name("cd-expand-label")
    for more in mores:
        if "examples" in more.text:
            more.click()
            break
    time.sleep(0.05)

    # exFile.write("#w#" + w)
    exList = []
    examples = driver.find_elements_by_class_name('gt-ex-text')
    for exp in examples:
        exList.append(exp.text)
    examplesDic[w] = exList
    print(str(i))
    i += 1
    if i == 2:
        break

exFile.write(str(json.dumps(examplesDic)))
