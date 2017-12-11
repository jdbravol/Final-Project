
def find_occurrences(word_to_find, file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    total_words = 0
    occ = 0
    for line in lines:
        for word in line.split():
            total_words+=1
            word = word.lower()
            if word_to_find in word:
                occ += 1
            elif word_to_find + "s" in word:
                occ += 1
            elif word_to_find + "es" in word:
                occ += 1
    file.close()
    return occ, total_words
file_name = ["2chainz", "2pac", "50_cent", "asap_rocky", "big_sean", "cardi_b",
             "childish_gambino", "drake", "dram", "eminem", "future", "jaden_smith", "jay-z", "jcole",
             "kanye", "kendricklamar", "lil_uzi", "lil_wayne", "lil_yachty", "logic", "mac_miller",
             "migos", "Nas", "nicki_minaj", "notorious_big", "outkast", "playboy_carti", "post_malone",
             "pusha_t", "schoolboy_q", "snoop", "travis_scott", "tyler_the_creator", "wiz_kha", "young_thug"]
word_to_find = ["fuck", "bitch", "hoe", "slut", "cunt", "dick", "ass", "shit", "nigga", "whore", "motherfucker",
                "fag", "damn", "asshole", "crap", "cock", "pussy", "douche"]
total_cursed = []
total_words = []
for file in file_name:
    total = 0
    words = 0
    for word in word_to_find:
        occ, words = find_occurrences(word, "raw/"+file)
        total += occ
    print "In " + file + " total number of cursed words: " + str(total)
    total_cursed.append(total)
    total_words.append(words)

print file_name

print total_cursed

print total_words