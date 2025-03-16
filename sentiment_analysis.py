# sentiment analysis model for collective response, intialization with sample training datas
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
class EmotionAnalyzer:
    """
    Emotion Analyzer that detects detailed emotions from comments and emoji reactions,
    and visualizes them in a pie chart.
    """
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        self.emotion_counts = {
            "Happy": 0,
            "Angry": 0,
            "Sad": 0,
            "Surprised": 0,
            "Fear/Concern": 0,
            "Neutral": 0
        }
        self.emoji_emotion_mapping = {
            "😀": "Happy", "😃": "Happy", "😄": "Happy", "😊": "Happy", "❤️": "Happy", "👍": "Happy",
            "😡": "Angry", "👎": "Angry", "😠": "Angry", "🤬": "Angry",
            "😢": "Sad", "😭": "Sad", "😞": "Sad", "😔": "Sad",
            "😮": "Surprised", "😲": "Surprised", "🤯": "Surprised",
            "😨": "Fear/Concern", "😰": "Fear/Concern", "😱": "Fear/Concern",
            "😐": "Neutral", "🤔": "Neutral", "🙄": "Neutral"
        }
    def analyze_text_emotion(self, text):
        """
        Analyze text comment and map sentiment to an emotion category.
        """
        score = self.analyzer.polarity_scores(text)
        compound = score['compound']
        if compound >= 0.5:
            emotion = "Happy"
        elif compound <= -0.5:
            if "angry" in text.lower() or "furious" in text.lower():
                emotion = "Angry"
            elif "sad" in text.lower() or "cry" in text.lower():
                emotion = "Sad"
            else:
                emotion = "Angry"
        elif -0.5 < compound < 0:
            emotion = "Fear/Concern"
        elif 0 < compound < 0.5:
            emotion = "Surprised"
        else:
            emotion = "Neutral"
        self.emotion_counts[emotion] += 1
        print(f"📝 Comment: {text}\n📊 Score: {score}\n🔍 Emotion: {emotion}\n")
        return emotion
    def analyze_emoji_emotion(self, emoji):
        """
        Analyze emoji and classify emotion.
        """
        emotion = self.emoji_emotion_mapping.get(emoji, "Neutral")
        self.emotion_counts[emotion] += 1
        print(f"😀 Emoji Reaction: {emoji} → 🔍 Emotion: {emotion}\n")
        return emotion
    def analyze_feedback(self, feedback_list):
        """
        Analyze combined feedback (comments + emojis).
        """
        for feedback in feedback_list:
            if feedback in self.emoji_emotion_mapping:
                self.analyze_emoji_emotion(feedback)
            else:
                self.analyze_text_emotion(feedback)
    def visualize_emotion_distribution(self, title="Event Emotion Analysis"):
        """
        Pie chart visualization of collected emotions.
        """
        labels = list(self.emotion_counts.keys())
        sizes = list(self.emotion_counts.values())
        colors = ['#4CAF50', '#F44336', '#2196F3', '#FF9800', '#9C27B0', '#9E9E9E']  # Happy, Angry, Sad, Surprised, Fear/Concern, Neutral
        explode = [0.05] * len(labels)  # Explode all slices slightly
        if sum(sizes) == 0:
            print("No emotions recorded yet. Add some feedback to see visualization.")
            return
        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                startangle=140, explode=explode, shadow=True, textprops={'fontsize': 14})
        plt.title(title, fontsize=16)
        plt.axis('equal')  # Make pie chart circular
        plt.show()

# ---------------- Example Usage ----------------

# Create instance of EmotionAnalyzer
ea = EmotionAnalyzer()
# Example mixed feedback (comments + emoji reactions)
feedback_data = [
    "I'm very happy with this decision, thank you!",  # Happy
    "Why is this taking so long? I'm furious!",       # Angry
    "This makes me sad and disappointed.",           # Sad
    "Wow! Didn't expect this at all.",               # Surprised
    "I'm scared this might cause issues.",          # Fear/Concern
    "Well, it is what it is.",                       # Neutral
    "😀", "😡", "😭", "😮", "😱", "🤔"                  # Emojis reflecting emotions
]
# Analyze all feedback
ea.analyze_feedback(feedback_data)
# Visualize emotion distribution
ea.visualize_emotion_distribution("Public Pulse: Event Emotional Response")
