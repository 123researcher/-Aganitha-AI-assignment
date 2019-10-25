
# coding: utf-8

# In[2]:



def recognizing_speech(audio):
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
         print("Could not recognize speech beacuse of some error")
       
    

