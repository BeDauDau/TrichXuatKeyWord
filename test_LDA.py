texts= ["""It's all about travel. I travel a lot.  those who do not travel read only a page.” – said Saint Augustine. He was a great travel person. Travelling can teach you more than any university course. You learn about the culture of the country you visit. If you talk to locals, you will likely learn about their thinking, habits, traditions and history as well.If you travel, you will not only learn about foreign cultures, but about your own as well. You will notice the cultural differences, and will find out what makes your culture unique. After retrurning from a long journey, you will see your country with new eyes.""",
        """ You can learn a lot about yourself through travelling. You can observe how you feel beeing far from your country. You will find out how you feel about your homeland.You should travel You will realise how you really feel about foreign people. You will find out how much you know/do not know about the world. You will be able to observe how you react in completely new situations. You will test your language, orientational and social skills. You will not be the same person after returning home.During travelling you will meet people that are very different from you. If you travel enough, you will learn to accept and appreciate these differences. Traveling makes you more open and accepting.""",
        """Some of my most cherished memories are from the times when I was travelling. If you travel, you can experience things that you could never experience at home. You may see beautiful places and landscapes that do not exist where you live. You may meet people that will change your life, and your thingking. You may try activities that you have never tried before.Travelling will inevitably make you more independent and confident. You will realise that you can cope with a lot of unexpected situations. You will realise that you can survive without all that help that is always available for you at home. You will likely find out that you are much stronger and braver than you have expected.""",
        """If you travel, you may learn a lot of useful things. These things can be anything from a new recepie, to a new, more effective solution to an ordinary problem or a new way of creating something.Even if you go to a country where they speak the same language as you, you may still learn some new words and expressions that are only used there. If you go to a country where they speak a different language, you will learn even more.""",
        """After arriving home from a long journey, a lot of travellers experience that they are much more motivated than they were before they left. During your trip you may learn things that you will want to try at home as well. You may want to test your new skills and knowledge. Your experiences will give you a lot of energy.During travelling you may experience the craziest, most exciting things, that will eventually become great stories that you can tell others. When you grow old and look back at your life and all your travel experiences, you will realise how much you have done in your life and your life was not in vain. It can provide you with happiness and satisfaction for the rest of your life.""",
        """The benefits of travel are not just a one-time thing: travel changes you physically and psychologically. Having little time or money isn't a valid excuse. You can travel for cheap very easily. If you have a full-time job and a family, you can still travel on the weekends or holidays, even with a baby. travel  more is likely to have a tremendous impact on your mental well-being, especially if you're no used to going out of your comfort zone. Trust me: travel more and your doctor will be happy. Be sure to get in touch with your physician, they might recommend some medication to accompany you in your travels, especially if you're heading to regions of the globe with potentially dangerous diseases.""",
        """Sure, you probably feel comfortable where you are, but that is just a fraction of the world! If you are a student, take advantage of programs such as Erasmus to get to know more people, experience and understand their culture. Dare traveling to regions you have a skeptical opinion about. I bet that you will change your mind and realize that everything is not so bad abroad.""",
        """ So, travel makes you cherish life. Let's travel more . Share your travel diaries with us too"""
]
texkkt = [""" Quyết định không gia hạn hợp đồng với Liên đoàn Bóng đá Việt Nam (VFF) đồng nghĩa HLV Park sẽ không còn gắn bó với tuyển Việt Nam sau ngày 31/1/2023. Ông sẽ khép lại hơn 5 năm vinh quang cùng các đội tuyển quốc gia Việt Nam. 5 năm cũng là thời gian hợp lý cho một chu kỳ thành công trong bóng đá. Lịch sử hiếm ghi nhận những chu kỳ dài hơn thế. Với HLV Park, lặp lại các thành công cũ đã khó chưa chưa nói tới vượt qua chúng. """]
# Import gensim, nltk
import gensim
from gensim import models, corpora
import nltk
from nltk.corpus import stopwords

# Before topic extraction, we remove punctuations and stopwords.
my_stopwords=set(stopwords.words('english'))
punctuations=['.','!',',',"You","I"]

# We prepare a list containing lists of tokens of each text
all_tokens=[]
for text in texts:
  tokens=[]
  raw=nltk.wordpunct_tokenize(text)
  for token in raw:
    if token not in my_stopwords:
      if token not in punctuations:
        tokens.append(token)
        all_tokens.append(tokens)

# Creating a gensim dictionary and the matrix
dictionary = corpora.Dictionary(all_tokens)
doc_term_matrix = [dictionary.doc2bow(doc) for doc in all_tokens]

# Building the model and training it with the matrix 
from gensim.models.ldamodel import LdaModel
model = LdaModel(doc_term_matrix, num_topics=5, id2word = dictionary,passes=40)

print(model.print_topics(num_topics=6,num_words=5))
