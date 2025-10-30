# untuk clean and process text
import re

positif = [
    "bagus", "senang", "hebat", "baik", "suka", "gembira", "ceria", "mantap", 
    "keren", "luar biasa", "menarik", "bahagia", "puas", "ramah", "indah", "terbaik",
    "sukses", "sehat", "positif", "beruntung", "menyenangkan", "lega", "berhasil",
    "terimakasih", "terima kasih", "bersyukur", "nikmat", "wow", "mantul", "top",
    
    "good", "great", "happy", "awesome", "excellent", "wonderful", "fantastic",
    "amazing", "love", "nice", "cool", "brilliant", "positive", "enjoy", "superb",
    "best", "fun", "kind", "beautiful", "success", "glad", "pleased", "thankful",
    "grateful", "perfect", "smile", "delight", "awesome", "outstanding"
]

negatif = [
    "buruk", "sedih", "jelek", "marah", "benci", "kecewa", "persetan", "sial", 
    "menyebalkan", "tidak suka", "jahat", "gagal", "bosan", "lelah", "sakit", "malas", 
    "menakutkan", "parah", "pusing", "payah", "muram", "tertekan", "galau", "risih", 
    "malu", "kejam", "susah", "sedih banget", "menyedihkan", "menyesal", "jahat banget",
    
    "bad", "sad", "angry", "hate", "terrible", "awful", "worst", "ugly", "disappoint", 
    "annoying", "tired", "sick", "boring", "pain", "hurt", "failure", "cry", "mad", 
    "stupid", "disgusting", "horrible", "depressed", "broken", "lazy", "upset", 
    "nonsense", "idiot", "regret", "fear", "frustrated", "hopeless", "dont", "don't", "do not"
]

def analyze_sentiment(text: str):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # itung kata kata yang muncul
    pos_count = sum(word in text for word in positif)
    neg_count = sum(word in text for word in negatif)

    if pos_count > neg_count:
        label = "positif"
        score = pos_count / (pos_count + neg_count + 1)
    elif neg_count > pos_count:
        label = "negatif"
        score = neg_count / (pos_count + neg_count + 1)
    else:
        label = "netral"
        score = 0.5

    return label, round(score, 2)
