#!/usr/bin/env python3
import re
#  Create the MyString class and give it a value property.
# The class should verify that the value is a string before assigning it.
class MyString:
    def __init__(self, value=""):
        self.value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        if type(value) == str:
            self._value = value
        else:
            print("The value must be a string.")

    value = property(get_value, set_value)

    # Define an instance method is_sentence() that returns True if the value ends in a period and False if it does not.
    def is_sentence(self):
        return self._value.endswith(".")

    # This method should return True if the value ends with a question mark and False if it does not.
    def is_question(self):
        return self._value.endswith("?")
    
    # This method should return True if the value ends with an exclamation mark and False if it does not.
    def is_exclamation(self):
        return self._value.endswith("!")
    
# What we'd like to be able to do is call a count_sentences() method on a MyString instance, 
# and get back a, well, count of sentences in its value
    def count_sentences(self):
        if len(self._value) == 0:
          return 0
        # lookahead assertion (?= ) means that the split should happen only when the punctuation mark is followed by a space.
        sentences_list = re.split(r'[.?!](?= )', self._value)
        return len(sentences_list)


string1 = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
print(string1.count_sentences())
