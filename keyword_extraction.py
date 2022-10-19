""" Cho một văn bản tiếng Việt, rút trích các từ khóa (keyword) đại diện cho văn bản đó.
Gợi ý: tập tin đính kèm chứa các minh họa cho việc rút trích keyword cho một văn bản tiếng Anh.
Các bạn có thể tham khảo một trong 3 hướng tiếp cận LSA, LDA, NMF trong các minh họa để thực hiện tương tự cho tiếng Việt.

Lưu ý:
- Các bạn chỉ cần cài đặt 1 hướng tiếp cận duy nhất trong chương trình, theo thứ tự ưu tiên LSA > LDA > NMF, Phương pháp Khác (Tức là LSA là bắt buộc, các phương pháp LDA, NMF và Phương pháp khác nếu các bạn làm sẽ được cộng điểm).
- Nộp: file nén .zip chứa mã nguồn chương trình và data thực nghiệm

Quy tắc viết chương trình:
- Chương trình viết dưới dạng dòng lệnh, hỗ trợ 2 tham số bắt buộc là input_file và result, tên tập tin chạy là keyword_extraction.py.
Ví dụ:
python keyword_extraction.py --input_file text.txt --result output.txt
Trong đó: text.txt là văn bản đầu vào (cần trích từ khóa), output chứa các từ khóa kết quả """
texts =["""Tất cả là về du lịch. Tôi đi du lịch rất nhiều. Những người không đi du lịch chỉ đọc một trang." - Saint Augustine nói. Anh ấy là một người tuyệt vời về du lịch. Đi du lịch có thể dạy cho bạn nhiều điều hơn bất kỳ khóa học đại học nào. Bạn tìm hiểu về văn hóa của đất nước bạn đến thăm. Nếu bạn nói chuyện với người dân địa phương, bạn có thể sẽ tìm hiểu về suy nghĩ, thói quen, truyền thống của họ và lịch sử nữa. sẽ nhìn đất nước của bạn với đôi mắt mới. """,
        """Bạn có thể học hỏi nhiều điều về bản thân thông qua việc đi du lịch. Bạn có thể quan sát cảm giác của mình khi rời xa đất nước của mình. Bạn sẽ tìm hiểu cảm giác của mình về quê hương của mình. Bạn nên đi du lịch, bạn sẽ nhận ra cảm giác thực sự của mình đối với người nước ngoài. Bạn sẽ biết được mình biết / chưa biết bao nhiêu về thế giới, có thể quan sát cách phản ứng của bạn trong những tình huống hoàn toàn mới. Trong quá trình đi du lịch, bạn sẽ gặp những người rất khác biệt với bạn. Nếu bạn đi du lịch đủ nhiều, bạn sẽ học cách chấp nhận và đánh giá cao những khác biệt này. Đi du lịch khiến bạn cởi mở và chấp nhận hơn. """,
        """Một số kỷ niệm trân quý nhất của tôi là từ khi tôi đi du lịch. Nếu bạn đi du lịch, bạn có thể trải nghiệm những điều mà bạn không bao giờ có thể trải nghiệm ở nhà. Bạn có thể nhìn thấy những địa điểm và phong cảnh đẹp không tồn tại ở nơi bạn sống. Bạn Bạn có thể gặp những người sẽ thay đổi cuộc đời bạn và sự nghiệp của bạn. Bạn có thể thử những hoạt động mà bạn chưa từng thử bao giờ. nhận ra rằng bạn có thể tồn tại mà không cần tất cả sự trợ giúp luôn sẵn sàng dành cho bạn ở nhà. Bạn có thể sẽ nhận ra rằng bạn mạnh mẽ và dũng cảm hơn nhiều so với những gì bạn mong đợi. """,
        """Nếu bạn đi du lịch, bạn có thể học được rất nhiều điều hữu ích. Những điều này có thể là bất cứ điều gì từ một người mới tiếp nhận, một giải pháp mới, hiệu quả hơn cho một vấn đề thông thường hoặc một cách mới để tạo ra thứ gì đó. Ngay cả khi bạn đi đến một quốc gia nơi họ nói cùng một ngôn ngữ với bạn, bạn vẫn có thể học một số từ và cách diễn đạt mới chỉ được sử dụng ở đó. Nếu bạn đến một quốc gia mà họ nói một ngôn ngữ khác, bạn sẽ còn học được nhiều hơn thế. """,
        """Sau khi trở về nhà sau một chuyến đi dài, rất nhiều khách du lịch cảm thấy rằng họ có động lực hơn nhiều so với trước khi rời đi. Trong chuyến đi của mình, bạn có thể học được những điều mà bạn cũng sẽ muốn thử ở nhà. Bạn có thể muốn để kiểm tra các kỹ năng và kiến ​​thức mới của bạn. Trải nghiệm của bạn sẽ mang lại cho bạn rất nhiều năng lượng. Trong quá trình đi du lịch, bạn có thể trải nghiệm những điều điên rồ nhất, thú vị nhất, cuối cùng sẽ trở thành những câu chuyện tuyệt vời mà bạn có thể kể cho người khác. Khi bạn già đi và nhìn lại cuộc sống của bạn và tất cả những trải nghiệm du lịch của bạn, bạn sẽ nhận ra rằng bạn đã làm được bao nhiêu điều trong cuộc sống của mình và cuộc sống của bạn không phải là vô ích. Nó có thể mang lại cho bạn hạnh phúc và sự hài lòng trong suốt quãng đời còn lại. """,
        """Lợi ích của việc đi du lịch không chỉ xảy ra một lần: du lịch thay đổi bạn về thể chất và tâm lý. Có ít thời gian hoặc tiền bạc không phải là lý do chính đáng. Bạn có thể đi du lịch với giá rẻ rất dễ dàng. Nếu bạn có toàn thời gian công việc và gia đình, bạn vẫn có thể đi du lịch vào cuối tuần hoặc ngày lễ, ngay cả khi có em bé. Đi du lịch nhiều hơn có thể có tác động to lớn đến sức khỏe tinh thần của bạn, đặc biệt nếu bạn không quen với việc đi ra khỏi vùng an toàn của mình . Tin tôi đi: hãy đi du lịch nhiều hơn và bác sĩ của bạn sẽ vui vẻ. Hãy liên hệ với bác sĩ của bạn, họ có thể giới thiệu một số loại thuốc để đi cùng bạn trong chuyến du lịch, đặc biệt nếu bạn đang đến các khu vực có khả năng mắc các bệnh nguy hiểm trên thế giới . """,
        """Chắc chắn rồi, bạn có thể cảm thấy thoải mái ở nơi mình đang ở, nhưng đó chỉ là một phần nhỏ của thế giới! Nếu bạn là sinh viên, hãy tận dụng các chương trình như Erasmus để biết thêm nhiều người, trải nghiệm và hiểu văn hóa của họ. Dám đi du lịch đến những vùng mà bạn có ý kiến ​​hoài nghi. Tôi cá rằng bạn sẽ thay đổi suy nghĩ của mình và nhận ra rằng mọi thứ ở nước ngoài không quá tệ.""",
        """Vì vậy, du lịch khiến bạn trân trọng cuộc sống. Hãy đi du lịch nhiều hơn. Hãy chia sẻ nhật ký du lịch của bạn với chúng tôi"""]
def get_stopwords_list(stop_file_path):
    """load stop words """
    
    with open(stop_file_path, 'r', encoding="utf-8") as f:
        stopwords = f.readlines()
        stop_set = set(m.strip() for m in stopwords)
        return list(frozenset(stop_set))

stopwords_path = "vietnamese-stopwords.txt"
stopwords = get_stopwords_list(stopwords_path)

from sklearn.feature_extraction.text import TfidfVectorizer

# Defining the vectorizer
vectorizer = TfidfVectorizer(stop_words=stopwords, max_features= 1000,  max_df = 0.5, smooth_idf=True)

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
