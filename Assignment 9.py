'''
# Import required libraries
import nltk


# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag, word_tokenize, RegexpParser

# Example text
sample_text = "The quick brown fox jumps over the lazy dog"

# Find all parts of speech in above sentence
tagged = pos_tag(word_tokenize(sample_text))
print("POS tagged tokens : ", tagged)

#Extract all parts of speech from any text
chunker = RegexpParser("""
					NP: {<DT>?<JJ>*<NN>} #To extract Noun Phrases
					P: {<IN>}			 #To extract Prepositions
					V: {<V.*>}			 #To extract Verbs
					PP: {
                    <p> <NP>}		 #To extract Prepositional Phrases
					VP: {<V> <NP|PP>*}	 #To extract Verb Phrases
					""")

# Print all parts of speech in above sentence
output = chunker.parse(tagged)
print("After Extracting\n", output)

# to draw parse tree
output.draw()





class State(object):
    def __init__(self, label, rules, dot_idx, start_idx, end_idx, idx, made_from, producer):
        self.label = label
        self.rules = rules
        self.dot_idx = dot_idx
        self.start_idx = start_idx
        self.end_idx = end_idx
        self.idx = idx
        self.made_from = made_from
        self.producer = producer

    def next(self):
        """Returns the tag after the dot"""
        return self.rules[self.dot_idx]

    def complete(self):
        return len(self.rules) == self.dot_idx

    def __eq__(self, other):
        return (self.label == other.label and
                self.rules == other.rules and
                self.dot_idx == other.dot_idx and
                self.start_idx == other.start_idx and
                self.end_idx == other.end_idx)

    def __str__(self):
        rule_string = ''
        for i, rule in enumerate(self.rules):
            if i == self.dot_idx:
                rule_string += '\\bullet '
            rule_string += rule + ' '
        if self.dot_idx == len(self.rules):
            rule_string += '\\bullet'
        return 'S%d %s -> %s [%d, %d] %s %s' % (self.idx, self.label, rule_string, self.start_idx,
                                                self.end_idx, self.made_from, self.producer)


class Earley:
    def __init__(self, words, grammar, terminals):
        self.chart = [[] for _ in range(len(words) + 1)]
        self.current_id = 0
        self.words = words
        self.grammar = grammar
        self.terminals = terminals

    def get_new_id(self):
        self.current_id += 1
        return self.current_id - 1

    def is_terminal(self, tag):
        return tag in self.terminals

    def is_complete(self, state):
        return len(state.rules) == state.dot_idx

    def enqueue(self, state, chart_entry):
        if state not in self.chart[chart_entry]:
            self.chart[chart_entry].append(state)
        else:
            self.current_id -= 1

    def predictor(self, state):
        for production in self.grammar[state.next()]:
            self.enqueue(
                State(state.next(), production, 0, state.end_idx, state.end_idx, self.get_new_id(), [], 'predictor'),
                state.end_idx)

    def scanner(self, state):
        if self.words[state.end_idx] in self.grammar[state.next()]:
            self.enqueue(
                State(state.next(), [self.words[state.end_idx]], 1, state.end_idx, state.end_idx + 1, self.get_new_id(),
                      [], 'scanner'), state.end_idx + 1)

    def completer(self, state):
        for s in self.chart[state.start_idx]:
            if not s.complete() and s.next() == state.label and s.end_idx == state.start_idx and s.label != 'gamma':
                self.enqueue(State(s.label, s.rules, s.dot_idx + 1, s.start_idx, state.end_idx, self.get_new_id(),
                                   s.made_from + [state.idx], 'completer'), state.end_idx)

    def parse(self):
        self.enqueue(State('gamma', ['S'], 0, 0, 0, self.get_new_id(), [], 'dummy start state'), 0)

        for i in range(len(self.words) + 1):
            for state in self.chart[i]:
                if not state.complete() and not self.is_terminal(state.next()):
                    self.predictor(state)
                elif i != len(self.words) and not state.complete() and self.is_terminal(state.next()):
                    self.scanner(state)
                else:
                    self.completer(state)

    def __str__(self):
        res = ''

        for i, chart in enumerate(self.chart):
            res += '\nChart[%d]\n' % i
            for state in chart:
                res += str(state) + '\n'

        return res


def test():
    grammar = {
        'S': [['NP', 'VP'], ['Aux', 'NP', 'VP'], ['VP']],
        'NP': [['Det', 'Nominal'], ['Proper-Noun']],
        'Nominal': [['Noun'], ['Noun', 'Nominal']],
        'VP': [['Verb'], ['Verb', 'NP']],
        'Det': ['that', 'this', 'a'],
        'Noun': ['book', 'flight', 'meal', 'money'],
        'Verb': ['book', 'include', 'prever'],
        'Aux': ['does'],
        'Prep': ['from', 'to', 'on'],
        'Proper-Noun': ['Houston', 'TWA']
    }
    terminals = ['Det', 'Noun', 'Verb', 'Aux', 'Prep', 'Proper-Noun']

    earley = Earley(['book', 'that', 'flight'], grammar, terminals)
    earley.parse()
    print(earley)


if __name__ == '__main__':
    test()

import nltk

sentence = [
   ('a', 'DT'),
   ('clever', 'JJ'),
   ('fox','NN'),
   ('was','VBP'),
   ('jumping','VBP'),
   ('over','IN'),
   ('the','DT'),
   ('wall','NN')
]
# print(sentence)

# sentence1 = input("Enter sentence : ")
# tagged = pos_tag(word_tokenize(sentence1))
# print("tagged", tagged)
# if tagged == sentence:
#    print("Both are equal")
# else:
#    print("Unequal")


grammar = "NP:{<DT>?<JJ>*<NN>}"
Reg_parser = nltk.RegexpParser(grammar)
print("Reg : ", Reg_parser)
# Reg_parser.parse(sentence)
Output = Reg_parser.parse(sentence)
print(Output)

Output.draw()


import nltk

your_grammar = nltk.CFG.fromstring("""
S -> NP VP
VP -> AUX V 
V -> "rising"
AUX -> "is"
NP -> N | DT NP | NP PP  
N -> "peace" | "price" 
DT -> "the"
PP -> P NP
P -> "of"
""")

parser = nltk.ChartParser(your_grammar)
print(parser)
sentence = "the price of peace is rising".split()
import time
start_time = time.time()
for tree in parser.parse(sentence):
    print(tree)
tree.draw()
# for tree in parser.parse(sentence):
#     print (list(tree))
'''


import nltk
from nltk import pos_tag, word_tokenize

s = "Bag of senses"
tagged = pos_tag(word_tokenize(s))

print(tagged)