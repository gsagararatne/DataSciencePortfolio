import streamlit as st 
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from keras.utils.data_utils import get_file
import pickle
import h5py

st.set_page_config(page_title="RapLyricsGenerator")
st.header("Rap Lyrics Generator")
st.subheader("Githendra Sagararatne")

"""
##### Note:
- Avoid punctuation, capitalisation of letters/words and numbers.
    - "I've had 2 dogs before" = "ive had two dogs before"
- I've tried my level best to remove cuss words from this system. If anything ill comes up, it is simply by chance and is not a view of the creator (me).
"""
'''
-----------
'''
prompt = st.text_input("Enter lyrics:")

word_count_options = [5, 10, 15, 20, 25]
word_count = st.selectbox("Number of words to be generated: ", word_count_options)

# Loading model from aws s3 bucket
lyrical_rap = get_file("model",origin="https://raplyricsgenerator.s3.us-east-2.amazonaws.com/rnn_models/lyrical_rap_model.h5")
lyrical_rap_model = load_model(lyrical_rap, compile=False)

# Loading model locally
# lyrical_rap_model = load_model("lyrical_rap_model.h5")

# load token locally
lyrical_rap_tokenizer = pickle.load(open("lyrical_rap_tokenizer.pkl", "rb")) 

def lyrical_rap_generator(prompt, word_count, lyrical_rap_model):
    # process for the model
    # last dense layer from model
    number_of_classes_lyrical_rap = 30862
    processed_phrase = lyrical_rap_tokenizer.texts_to_sequences([prompt])[0]
    for i in range(word_count):
      network_input = np.array(processed_phrase[-(len(processed_phrase)):], dtype=np.float32)
      network_input = network_input.reshape((1, (len(processed_phrase)))) 

      # the RNN gives the probability of each word as the next one
      predict_proba = lyrical_rap_model.predict(network_input)[0] 
      
      # sample one word using these chances
      predicted_index = np.random.choice(number_of_classes_lyrical_rap, 1, p=predict_proba)[0]

      # add new index at the end of our list
      processed_phrase.append(predicted_index)
      

  # indices mapped to words - the method expects a list of lists so we need the extra bracket
      output_phrase = lyrical_rap_tokenizer.sequences_to_texts([processed_phrase])[0]

    return output_phrase

   
if st.button("Generate"):
        generated_rap_lyrics = lyrical_rap_generator(prompt, word_count, lyrical_rap_model)

        if "X" not in generated_rap_lyrics:
            try:
                    st.write(generated_rap_lyrics)
            except:
                    raise ValueError('I think you may have input a word that is not in the vocabulary. Please try again with a different prompt.')
        else:
            st.write("Please try again.")

'''
-----------
'''
""" 
###### Do reach out to me through gsagararatne@gmail.com and/or [linkedin](https://www.linkedin.com/in/gsagararatne/) for comments and/or constructive critisim.
"""
st.text("Personal project created by Githendra Sagararatne.")
