"""
Python script for creating Arabic verb conjugations; code + examples. Runs in terminal. 
See README for more details.
"""

class Conjugate(object):
    
    def __init__(self):
        self.verbTable = VerbHashTable()
        self._build()
        
    def _form1(self, rad1, rad2, rad3, stem, tense, voice):
        if tense == "perf":
            initialVowel = "a"  if voice == "active" else "u"
            stemVowel    = stem if voice == "active" else "i"
            
        if tense == "pres":
            initialVowel = ""
            stemVowel    = stem if voice == "active" else "a"
        
        form_one = rad1 + initialVowel + rad2 + stemVowel + rad3
        return(form_one)

    def _form2(self, rad1, rad2, rad3, stem, tense, voice):
        if tense == "perf":
            initialVowel = "a" if voice == "active" else "u"
            stemVowel    = "a" if voice == "active" else "i"
            
        if tense == "pres":
            initialVowel = "a"
            stemVowel    = "i" if voice == "active" else "a"
            
        form2 = rad1 + initialVowel + rad2*2 + stemVowel + rad3
        return(form2)
    
    def _form3(self, rad1, rad2, rad3, stem, tense, voice):
        if tense == "perf":
            initialVowel = "a" if voice == "active" else "u"
            stemVowel    = "a" if voice == "active" else "i"
            
        if tense == "pres":
            initialVowel = "a"
            stemVowel    = "i" if voice == "active" else "a"
            
        form3 = rad1 + initialVowel*2 + rad2 + stemVowel + rad3
        return(form3)
    
    def _form4(self, rad1, rad2, rad3, stem, tense, voice):
        if tense == "perf":
            initialVowel = "a" if voice == "active" else "u"
            stemVowel    = "a" if voice == "active" else "i"

        if tense == "pres":
            initialVowel = ""
            stemVowel    = "i" if voice == "active" else "a"
        
        form4 = initialVowel + rad1 + rad2 + stemVowel + rad3
        return(form4)
    
    def _form5(self, rad1, rad2, rad3, stem, tense, voice):
        if tense == "perf":
            initialVowel = "a" if voice == "active" else "u"
            stemVowel    = "a" if voice == "active" else "i"

        if tense == "pres":
            initialVowel = "a"
            stemVowel    = "a" if voice == "active" else "a"
            
        form5Prefix = "ta" if voice == "active" or tense =="pres" else "tu"
        form5 = form5Prefix + rad1 + initialVowel + rad2*2 + stemVowel + rad3
        return(form5)
    
    def _form6(self, rad1, rad2, rad3, stem, tense, voice):
        if tense == "perf":
            initialVowel = "a" if voice == "active" else "u"
            stemVowel    = "a" if voice == "active" else "i"

        if tense == "pres":
            initialVowel = "a"
            stemVowel    = "a" if voice == "active" else "a"
            
        form6Prefix = "t" + ("a" if voice == "active" or tense =="pres" else "u")
        form6 = form6Prefix + rad1 + initialVowel*2 + rad2 + stemVowel + rad3
        return(form6)
    
    def _form7(self, rad1, rad2, rad3, stem, tense, voice):
        if tense == "perf":
            initialVowel = "a" if voice == "active" else "u"
            stemVowel    = "a" if voice == "active" else "i"

        if tense == "pres":
            initialVowel = "a"
            stemVowel    = "i" if voice == "active" else "a"
            
        form7Prefix = "n" if tense == "pres" else "in" if voice == "active" else "un"
        form7 = form7Prefix + rad1 + initialVowel + rad2 + stemVowel + rad3
        return(form7)
    
    def _form8(self, rad1, rad2, rad3, stem, tense, voice):
        if tense == "perf":
            initialVowel = "a" if voice == "active" else "u"
            stemVowel    = "a" if voice == "active" else "i"

        if tense == "pres":
            initialVowel = "a"
            stemVowel    = "i" if voice == "active" else "a"
            
        form8Prefix = "" if tense == "pres" else "i" if voice == "active" else "u"
        form8Infix  = "t"
        form8 = form8Prefix + rad1 + form8Infix + initialVowel + rad2 + stemVowel + rad3
        return(form8)
    
    def _form10(self, rad1, rad2, rad3, stem, tense, voice):
        if tense == "perf":
            initialVowel = "a" if voice == "active" else "u"
            stemVowel    = "a" if voice == "active" else "i"

        if tense == "pres":
            initialVowel = "a"
            stemVowel    = "i" if voice == "active" else "a"
            
        form10Prefix = "st" if tense == "pres" else "ist" if voice == "active" else "ust"
        form10 = form10Prefix + stemVowel + rad1 + rad2 + stemVowel + rad3
        return(form10)
    
    def _moodMarker(self, mood, indMarker):
        if mood == "ind":
            marker = indMarker
            
        if mood == "subj":
            marker = "a" if indMarker == "u" else ""
            
        if mood == "juss":
            marker = ""
            
        return marker
    
    
    def _build(self):
        self.verbTable.add("perf", "1st", "sing", "masc", ("", "tu"))
        self.verbTable.add("perf", "2nd", "sing", "masc", ("", "ta"))
        self.verbTable.add("perf", "2nd", "sing", "fem",  ("", "ti"))
        self.verbTable.add("perf", "3rd", "sing", "masc", ("", "a"))
        self.verbTable.add("perf", "3rd", "sing", "fem",  ("", "at"))

        self.verbTable.add("perf", "2nd", "dual", "masc", ("", "tumaa"))
        self.verbTable.add("perf", "3rd", "dual", "masc", ("", "aa"))
        self.verbTable.add("perf", "3rd", "dual", "fem",  ("", "taa"))

        self.verbTable.add("perf", "1st", "plu",  "masc", ("", "naa"))
        self.verbTable.add("perf", "2nd", "plu",  "masc", ("", "tum"))
        self.verbTable.add("perf", "2nd", "plu",  "fem",  ("", "tunna"))
        self.verbTable.add("perf", "3rd", "plu",  "masc", ("", "uu"))
        self.verbTable.add("perf", "3rd", "plu",  "fem",  ("", "na"))

        self.verbTable.add("pres", "1st", "sing", "masc", ("a",  "",   "u" ))
        self.verbTable.add("pres", "2nd", "sing", "masc", ("ta", "",   "u" ))
        self.verbTable.add("pres", "2nd", "sing", "fem",  ("ta", "ee", "na"))
        self.verbTable.add("pres", "3rd", "sing", "masc", ("ya", "",   "u" ))
        self.verbTable.add("pres", "3rd", "sing", "fem",  ("ta", "",   "u" ))

        self.verbTable.add("pres", "2nd", "dual", "masc", ("ta", "aa", "ni"))
        self.verbTable.add("pres", "2nd", "dual", "fem",  ("ta", "aa", "ni"))
        self.verbTable.add("pres", "3rd", "dual", "masc", ("ya", "aa", "ni"))
        self.verbTable.add("pres", "3rd", "dual", "fem",  ("ta", "aa", "ni"))

        self.verbTable.add("pres", "1st", "plu",  "masc", ("na", "",   "u" ))
        self.verbTable.add("pres", "2nd", "plu",  "masc", ("ta", "oo", "na")) 
        self.verbTable.add("pres", "2nd", "plu",  "fem",  ("ta", "na", ""  ))
        self.verbTable.add("pres", "3rd", "plu",  "masc", ("ya", "oo", "na"))
        self.verbTable.add("pres", "3rd", "plu",  "fem",  ("ya", "na", ""  ))
    
    
    def generate(self, root, tense, person, num, gender, form="1", stem="a", mood="ind", voice="active"):
        rad1 = root.split('-')[0]
        rad2 = root.split('-')[1]
        rad3 = root.split('-')[2]
        
        get_form = {
            "1": self._form1,
            "2": self._form2,
            "3": self._form3,
            "4": self._form4,
            "5": self._form5,
            "6": self._form6,
            "7": self._form7,
            "8": self._form8,
            "10": self._form10
        }
        base = get_form[form](rad1, rad2, rad3, stem, tense, voice)
        
        affixes = self.verbTable.get(tense, person, num, gender)
        subjPrefix  = affixes[0] if voice == "active" else affixes[0].replace('a', 'u')
        subjPrefix  = subjPrefix if form == "1" or int(form) > 4 else subjPrefix.replace('a', 'u')
        subjSuffix  = affixes[1]
        
        moodSuffix = "" if tense == "perf" else self._moodMarker(mood, affixes[2])
        
        full = subjPrefix + base + subjSuffix + moodSuffix
        return full
    
    def generate_all(self, root):
        tenses = ["perf", "pres"]
        persons = ["1st", "2nd", "3rd"]
        nums    = ["sing", "dual", "plu"]
        genders = ["masc", "fem"]
        moods   = ["ind", "subj", "juss"]
        voices  = ["active", "passive"]
        allForms = {}
        
        for tense in tenses:
            for person in persons:
                for num in nums:
                    for gender in genders:
                        for mood in moods:
                            for voice in voices:
                                try:
                                    key = "-".join([tense,person,num,gender,mood,voice])
                                    allForms[key] = self.generate(root, tense, person, num, 
                                                                  gender, mood=mood, voice=voice)
                                except:
                                    break
        return allForms

    
class VerbHashTable():
    def __init__(self):
        self.table = [None]*10000
        
    def _hashFunction(self, tense, person, num, gender):
        self._verify(tense, person, num, gender)

        personPrime = int(person[0])
        tensePrime  = 5  if tense  == "perf" else 7
        genderPrime = 11 if gender == "masc" else 13
        numPrime    = 17 if num    == "sing" else 19 if num == "plu" else 23
        
        keyIndex = personPrime * tensePrime * genderPrime * numPrime
        return keyIndex
    
    def _verify(self, tense, person, num, gender):
        if int(person[0]) >= 4 or int(person[0]) <= 0:
            raise Exception("Invalid person: must be '1st', '2nd', or '3rd'.")
            
        if tense != "pres" and tense != "perf":
            raise Exception("Invalid tense: must be 'pres' or 'perf'.")
            
        if gender != "masc" and gender != "fem":
            raise Exception("Invalid gender: must be 'masc' or 'fem'.")
        
        if num != "sing" and num != "dual" and num != "plu":
            raise Exception("Invalid number: must be 'sing', 'dual', or 'plu'.")
        
    def add(self, tense, person, num, gender, value):
        index = self._hashFunction(tense, person, num, gender)
        self.table[index] = value
        
    def get(self, tense, person, num, gender):
        self._verify(tense, person, num, gender)
        index = self._hashFunction(tense, person, num, gender)
        
        return self.table[index]
        
# Examples.
# Excluding a field will resort to some default. Note that all first-form verbs require a stem. 
conj= Conjugate()
print(conj.generate("q-t-l",  "pres", "1st", "sing", "masc", mood="ind", form="1",  voice="active", stem="u"))
print(conj.generate("q-t-l",  "pres", "3rd", "plu",  "fem",  mood="ind", form="1",  voice="active", stem="u"))
print(conj.generate("q-t-l",  "pres", "1st", "sing", "masc", mood="ind", form="10", voice="active"))
print(conj.generate("q-t-l",  "pres", "3rd", "plu",  "fem",  mood="ind", form="10", voice="active"))
print(conj.generate("q-t-l",  "pres", "3rd", "plu",  "fem",  mood="ind", form="10", voice="passive"))
print(conj.generate("q-t-l",  "perf", "3rd", "plu",  "fem",  form="2", voice="active"))
print(conj.generate("kh-b-r", "pres", "1st", "sing", "masc", mood="ind", form="1",  voice="active", stem="u"))
print(conj.generate("kh-b-r", "perf", "3rd", "plu",  "fem",  mood="ind", form="1",  voice="active", stem="a"))
print(conj.generate("kh-b-r", "pres", "1st", "sing", "masc", mood="ind", form="10", voice="active"))
print(conj.generate("kh-b-r", "pres", "3rd", "plu",  "fem",  mood="ind", form="5",  voice="active"))
print(conj.generate("kh-b-r", "pres", "3rd", "plu",  "fem",  mood="ind", form="8",  voice="passive"))
print(conj.generate("kh-b-r", "perf", "3rd", "plu",  "fem",  form="4", voice="active"))

print(conj.generate_all("k-t-b"))
print(conj.generate_all("s-l-m"))
