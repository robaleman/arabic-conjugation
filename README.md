# Arabic Verb Conjugation
This script is for producing verb conjugations for the Arabic language. 

### Background
Semitic languages feature a unique 3-consonantal root system in which abstract concepts (love, conflict, informing, etc.) are represented by a combination of 3 consontants (example, k-t-b), and then specialized words related to that concept are created systematically using various prefixes, suffixes, infixes, and vowel combinations, and where all of these modifiers often carry particular semantic shades.

Arabic is not different and uses this root system extensively. In Western pedagogy, these are usually classified using the "form system", where verbs are created systematically from these roots using Forms I through Form X, where "forms" are templates to create verbs using these roots. Each form usually represents some kind of semantic modifier, such as intensive, reflexive, causative, submission, or so on. Note that while all forms can be created from a certain root, not all of these verbs have been actualized into the Arabic lexicon, and it's up to learners to identify which constructions are actually used in the Arabic language. On the other hand, Arabic learners may be able to decipher the rough meaning of an unknown verb if they are familiar with its root and the semantic shades of its verb form.

Furthermore, once a verb root is created, this merely represents the "default" form of the verb (note that Arabic has no infinitive, and instead 
uses the 3rd person masculine singular past tense as the default as seen in dictionaries and pedagogy). Verbs are then further inflected by person (1st, 2nd, or 3rd person), number (singular, dual, or plural), gender (masculine or feminine), and aspect (perfect/past or imperfect/present), which are represented by a single set of prefix and suffix like other fusional languages. Mood (indicative, subjunctive, jussive, or imperative) are represented by their own suffix (although note that all moods other than indicative uniquely assume the imperfect aspect) and voice (active or passive) is indicated by specific changes in the verb's voweling.

A hash table was used to store all the appropriate conjugations prefixes and suffixes associated with a given set of parameters. It used the parameters themselves as keys: each parameter was mapped to a unique prime number and the hash function computed the product of all the primes to prevent collision. 

### Usage
Verbs are created by instantiating the Conjugate class and either using the "generate" function to create a specific, inflected verbs, or alternatively, you can also just use the generate_all function to generate a Python dictionary containing every possible conjugation combination. 

For the generate function, you must supply the verb root (in the form "C-C-C", where C is any consonant, and may need to take multiple letters from the Roman alphabet like for "th" or "kh"), along with its form, tense/aspect, person, gender, number, mood, and voice. Most of these carry defaults if they aren't supplied. Currently, only "sound" roots (roots without a glottal stop or the two semi-vowels) can be conjugated with these script, with others to be included in the future.

Note that all Form I verbs require a stem vowel that must be included. The stem vowel (vowel between the first and second consonants) and cannot be predicted since it's unique to each root itself. Future updates may include a dictionary lookup for each verb root, but for now, the stem vowel must be manually looked-up and manually input into the script. Stem vowels are not needed for Forms II through X where the voweling is completely dictated by the verb's form, aspect, and voice.

### Examples
Inputting the following function calls:

```
print(conj.generate("q-t-l",  "pres", "3rd", "plu",  "masc", mood="ind", form="1",  voice="active", stem="u"))
```

will yield the following inflected verb as a response:

```
qatala
````
