# -*- coding: utf-8 -*-
from TrainingSetsUtil import get_words
from TrainingSetsUtil import spam_training_set
from TrainingSetsUtil import ham_training_set

# c is an experimentally obtained value
def classify(message, training_set, prior = 0.5, c = 3.7e-4):
    
    """
    Returns the probability that the given message is of the given type of
    the training set.
    """
    
    msg_terms = get_words(message)
    
    msg_probability = 1
    
    for term in msg_terms:        
        if term in training_set:
            msg_probability *= training_set[term]
        else:
            msg_probability *= c
            
    return msg_probability * prior
  
mail_msg = input('Enter the message to be classified:')
print ('')

## 0.2 and 0.8 because the ratio of samples for spam and ham were the 0.2-0.8
spam_probability = classify(mail_msg, spam_training_set, 0.2)
ham_probability = classify(mail_msg, ham_training_set, 0.8)
if spam_probability > ham_probability:
    print ('Your mail has been classified as SPAM.')
    print (spam_probability)
else:
   print ('Your mail has been classified as Not-Spam.')
   print (ham_probability)
print ('')
