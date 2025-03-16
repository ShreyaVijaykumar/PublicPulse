#trust scores of the community for the government posts which only government can see
import matplotlib.pyplot as plt
import pandas as pd
class CollectiveTrustEvaluator:
    def __init__(self):
        self.base_score = 50  # Base trust score
        self.users_data = []  # Store user trust data internally
    def add_user(self, participation, contributions, sentiment):
        """
        Add user details and calculate their trust score.
        (No user IDs are stored to maintain privacy.)
        """
        score = self.base_score + (participation * 5) + (contributions * 3)
        if sentiment == "Positive":
            score += 10
        elif sentiment == "Negative":
            score -= 10
        score = max(0, min(score, 100))  # Bound the score
        self.users_data.append({
            'Participation': participation,
            'Contributions': contributions,
            'Sentiment': sentiment,
            'Trust Score': score
        })
    def evaluate_collective_trust(self):
        """
        Evaluate and summarize the collective trust.
        """
        df = pd.DataFrame(self.users_data)
        total_users = len(df)
        avg_trust_score = df['Trust Score'].mean()
        avg_participation = df['Participation'].mean()
        # Trustworthy percentage (users with score >= 70)
        trustworthy_users = df[df['Trust Score'] >= 70]
        trustworthy_percentage = (len(trustworthy_users) / total_users) * 100 if total_users else 0
        # Community trust level
        if avg_trust_score >= 75:
            community_status = "Highly Trustworthy Community"
        elif avg_trust_score >= 50:
            community_status = "Moderately Trustworthy, Monitoring Suggested"
        else:
            community_status = "Low Trust, Intervention Required"
        # Summary Report
        print("\n------ Collective Trust Score Summary ------")
        print(f"👥 Total Users Evaluated: {total_users}")
        print(f"✅ Trustworthy Users (%): {trustworthy_percentage:.2f}%")
        print(f"📊 Average Trust Score: {avg_trust_score:.2f}")
        print(f"🧑‍🤝‍🧑 Collective Average Participation: {avg_participation:.2f} (out of 10)")
        print(f"📋 Community Trust Level: {community_status}")
        return {
            "total_users": total_users,
            "trustworthy_percentage": trustworthy_percentage,
            "average_trust_score": avg_trust_score,
            "average_participation": avg_participation,
            "community_status": community_status
        }
    def visualize_collective_metrics(self):
        """
        Create a pie chart showing trustworthy vs non-trustworthy users.
        """
        df = pd.DataFrame(self.users_data)
        total_users = len(df)
        trustworthy_users = len(df[df['Trust Score'] >= 70])
        non_trustworthy_users = total_users - trustworthy_users
        labels = ['Trustworthy Users', 'Non-Trustworthy Users']
        sizes = [trustworthy_users, non_trustworthy_users]
        colors = ['#4CAF50', '#FF5722']
        plt.figure(figsize=(7, 7))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors,
                wedgeprops=dict(width=0.5), explode=(0.05, 0))
        plt.title('Community Trustworthiness Overview', fontsize=14, fontweight='bold')
        plt.show()
# ------------------- ✅ Example Usage -------------------
# Instantiate the evaluator
trust_evaluator = CollectiveTrustEvaluator()
# Add anonymized user data
trust_evaluator.add_user(participation=8, contributions=6, sentiment='Positive')
trust_evaluator.add_user(participation=5, contributions=4, sentiment='Neutral')
trust_evaluator.add_user(participation=2, contributions=1, sentiment='Negative')
trust_evaluator.add_user(participation=10, contributions=9, sentiment='Positive')
trust_evaluator.add_user(participation=3, contributions=2, sentiment='Neutral')
# Evaluate collective trust
result = trust_evaluator.evaluate_collective_trust()
# Visualize trustworthiness distribution
trust_evaluator.visualize_collective_metrics()
