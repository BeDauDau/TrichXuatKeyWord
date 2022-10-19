texts= ["""It's all about travel. I travel a lot.  those who do not travel read only a page.” – said Saint Augustine. He was a great travel person. Travelling can teach you more than any university course. You learn about the culture of the country you visit. If you talk to locals, you will likely learn about their thinking, habits, traditions and history as well.If you travel, you will not only learn about foreign cultures, but about your own as well. You will notice the cultural differences, and will find out what makes your culture unique. After retrurning from a long journey, you will see your country with new eyes.""",
        """ You can learn a lot about yourself through travelling. You can observe how you feel beeing far from your country. You will find out how you feel about your homeland.You should travel You will realise how you really feel about foreign people. You will find out how much you know/do not know about the world. You will be able to observe how you react in completely new situations. You will test your language, orientational and social skills. You will not be the same person after returning home.During travelling you will meet people that are very different from you. If you travel enough, you will learn to accept and appreciate these differences. Traveling makes you more open and accepting.""",
        """Some of my most cherished memories are from the times when I was travelling. If you travel, you can experience things that you could never experience at home. You may see beautiful places and landscapes that do not exist where you live. You may meet people that will change your life, and your thingking. You may try activities that you have never tried before.Travelling will inevitably make you more independent and confident. You will realise that you can cope with a lot of unexpected situations. You will realise that you can survive without all that help that is always available for you at home. You will likely find out that you are much stronger and braver than you have expected.""",
        """If you travel, you may learn a lot of useful things. These things can be anything from a new recepie, to a new, more effective solution to an ordinary problem or a new way of creating something.Even if you go to a country where they speak the same language as you, you may still learn some new words and expressions that are only used there. If you go to a country where they speak a different language, you will learn even more.""",
        """After arriving home from a long journey, a lot of travellers experience that they are much more motivated than they were before they left. During your trip you may learn things that you will want to try at home as well. You may want to test your new skills and knowledge. Your experiences will give you a lot of energy.During travelling you may experience the craziest, most exciting things, that will eventually become great stories that you can tell others. When you grow old and look back at your life and all your travel experiences, you will realise how much you have done in your life and your life was not in vain. It can provide you with happiness and satisfaction for the rest of your life.""",
        """The benefits of travel are not just a one-time thing: travel changes you physically and psychologically. Having little time or money isn't a valid excuse. You can travel for cheap very easily. If you have a full-time job and a family, you can still travel on the weekends or holidays, even with a baby. travel  more is likely to have a tremendous impact on your mental well-being, especially if you're no used to going out of your comfort zone. Trust me: travel more and your doctor will be happy. Be sure to get in touch with your physician, they might recommend some medication to accompany you in your travels, especially if you're heading to regions of the globe with potentially dangerous diseases.""",
        """Sure, you probably feel comfortable where you are, but that is just a fraction of the world! If you are a student, take advantage of programs such as Erasmus to get to know more people, experience and understand their culture. Dare traveling to regions you have a skeptical opinion about. I bet that you will change your mind and realize that everything is not so bad abroad.""",
        """ So, travel makes you cherish life. Let's travel more . Share your travel diaries with us too"""
]


# Importing the Tf-idf vectorizer from sklearn
from sklearn.feature_extraction.text import TfidfVectorizer

# Defining the vectorizer
vectorizer = TfidfVectorizer(stop_words='english', max_features= 1000,  max_df = 0.5, smooth_idf=True)

# Transforming the tokens into the matrix form through .fit_transform()
matrix= vectorizer.fit_transform(texts)

# SVD represent documents and terms in vectors
from sklearn.decomposition import TruncatedSVD
SVD_model = TruncatedSVD(n_components=10, algorithm='randomized', n_iter=100, random_state=122)
SVD_model.fit(matrix)

# Getting the terms 
terms = vectorizer.get_feature_names()

# Iterating through each topic
for i, comp in enumerate(SVD_model.components_):
    terms_comp = zip(terms, comp)
    # sorting the 7 most important terms
    sorted_terms = sorted(terms_comp, key= lambda x:x[1], reverse=True)[:7]
    print("Topic "+str(i)+": ")
    # printing the terms of a topic
    for t in sorted_terms:
        print(t[0],end=' ')
    print(' ')
