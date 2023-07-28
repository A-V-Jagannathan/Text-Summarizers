import contractions
import threading
#used to regex clean
def re_clean(text):
    import re
    text = re.sub(r'https?:\/\/.*[\r\n]*', ' ', text, flags=re.MULTILINE)
    text = re.sub(r'\<a href', ' ', text)
    text = re.sub(r'&amp;', ' ', text) 
    text = re.sub(r'[_\-;%()|+&=*%:#$@\[\]/]', ' ', text)
    text = re.sub(r'<br />', ' ', text)
    text = re.sub(r'\'', ' ', text)
    text=re.sub(r'\n',' ',text)
    text=re.sub(' est ',' ',text)
    text=re.sub(r'[?!]','.',text)
    return text
#used to expand contractions
def expand(text):
    import contractions
    text=text.split()
    final=[]
    for word in text:
        try:
            final.append(contractions.fix(word)+" ") 
        except:
            final.append(word+" ")
            print(word)
    return "".join(final)
#used to remove small useless sentences
def remove(texts):
    final=[]
    for text in texts:
        sents=[]
        sentences=text.split(".")
        for sentence in sentences:
            if(len(sentence.split())>=5):
                sents.append(sentence+".")
        final.append("".join(sents))
    return final
#used to remove Common news tags
def removeTag(texts):
    final=[]
    #removing cnn and est
    for text in texts:
        cnn=text.find("cnn")
        if(cnn!=-1 and cnn<len(text)//10):
            text=text[cnn+3:]
        found=False
        for i in range(2):
            est=text.find(" est,")
            if(est<len(text)//5 and est!=-1):
                text=text[est+5:]
                found=True
        fs=text.find(".")
        if(fs<20 and fs!=-1 and found):
            text=text[fs:]
        final.append(text)
    return final
# Calculate tf idf scores for sentences
def tfidf(sentences,d):
    scores=[0]*len(sentences)
    freq={}
    total=0
    for sentence in sentences:
        words=sentence.split()
        for i in words:
            total+=1
            if(i in freq):
                freq[i]+=1
            else:
                freq[i]=1
    for i in freq:
        freq[i]/=total
    wordlengths=[]
    for i in range(len(sentences)):
        words=sentences[i].split()
        n=len(words)
        wordlengths.append(n)
        score=0
        for word in words:
            if(word in d):
                score+=(freq[word]*d[word])
            else:
                score+=(freq[word]*1)
        score= score/n if n>0 else 0
        scores[i]=score
    
    l=[[scores[i],sentences[i],wordlengths[i]] for i in range(len(sentences))]
    l.sort(reverse=True)
    return l
# extract sentences
def extract(text,no_words):
    import pickle
    text=expand(re_clean(text)).lower()
    cleaned=removeTag(remove([text]))[0]
    d=0
    with open("idf.pkl", 'rb') as fp:
        d = pickle.load(fp)
    text=text.split(".")
    scores=tfidf(text,d)
    final=[]
    no_words-=scores[0][2]
    while(no_words>0 and len(scores)>1):
        sentence=scores.pop()[1]+"."
        place=-1
        for i in range(len(sentence)):
            if(sentence[i].isalpha()):
                place=i
                break
        sentence=sentence[:place]+sentence[place].upper()+sentence[place+1:] if place>-1 else sentence
        final.append("".join(sentence))
        no_words-=scores[0][2]
    
    final="".join(final)
    import re
    final=re.sub(r"you.","U.",final)
    return final
def finalfunc():
    global text_area
    global input_field
    global num_words_entry
    import tkinter as tk
    n = int(num_words_entry.get())
    s=input_field.get(1.0, "end-1c")
    s=extract(s,n)    
    text_area.delete("1.0", "end")
    text_area.insert("1.0",s)
def start_thread():
    # create and start a new thread
    thread = threading.Thread(target=finalfunc)
    thread.start()
def CreateInterface():
    import tkinter as tk
    # create the root window
    root = tk.Tk()
    root.title("Extractive Text Summarizer")
    root.configure(bg="grey")
    root.state('zoomed')
    # add three line breaks
    for i in range(3):
        tk.Label(root, text="", bg="grey").pack()
    # create the heading label
    heading = tk.Label(root, text="Extractive Text Summarizer for News Articles" , bg="grey", font=("Arial", 20))
    heading.pack()
    # add three line breaks
    for i in range(3):
        tk.Label(root, text="", bg="grey").pack()
    # create a frame to hold the input field and text area
    frame = tk.Frame(root)
    frame.pack()
    # create the input field
    global input_field,text_area
    input_field = tk.Text(frame, width=60, height=20, font=("Arial", 12))
    input_field.pack(side="left")
    # create the text area
    text_area = tk.Label(frame, width=20, height=20, bg="grey", font=("Arial", 12))
    text_area.pack(side="left")
    # create the text area
    text_area = tk.Text(frame, width=60, height=20, font=("Arial", 12))
    text_area.pack(side="right")
    # add three line breaks
    for i in range(3):
        tk.Label(root, text="", bg="grey").pack()
    # create the submit button
    # create a frame to hold the number of words input
    global num_words_entry
    num_words_frame = tk.Frame(root)
    num_words_frame.pack()

    # create a label for the number of words input
    num_words_label = tk.Label(num_words_frame, text="Enter number of words:", bg="grey", font=("Arial", 12))
    num_words_label.pack(side="left")

    # create the text box to input number of words
    num_words_entry = tk.Entry(num_words_frame, width=10, font=("Arial", 12))
    num_words_entry.pack(side="left")
    for i in range(2):
        tk.Label(root, text="", bg="grey").pack()
    global submit_button
    submit_button = tk.Button(root, text="Generate", font=("Arial", 14),command=start_thread)
    submit_button.pack()

    # add three line breaks
    for i in range(2):
        tk.Label(root, text="", bg="grey").pack()
    # create the subheading label
    subheading = tk.Label(root, text="Created with <3 by Jagannathan" , bg="grey", font=("Arial", 12))
    subheading.pack()
    # run the main loop
    root.mainloop()
CreateInterface()    
    
        
                
