#credit scores given to the user based on their activity by the AI panel in Google Colab
class UserCreditSystem:
    def __init__(self, user_id):
        self.user_id = user_id
        self.credit_score = 0
        self.participation_count = 0
        self.spam_warnings = 0
    def login_verification(self, verified):
        """
        Adds credit if the user is verified properly (e.g., Aadhaar-based login)
        """
        if verified:
            self.credit_score += 50
            print(f" Verified login. Credit Score: {self.credit_score}")
        else:
            print(" Verification failed. No credit added.")
    def participate(self, valid_interaction=True):
        """
        Rewards participation if valid (non-spam, non-abusive).
        """
        if valid_interaction:
            self.credit_score += 10
            self.participation_count += 1
            print(f" Valid participation. Credit Score: {self.credit_score}")
        else:
            self.credit_score -= 30
            self.spam_warnings += 1
            print(f" Invalid interaction! Credit Score: {self.credit_score}")
    def align_with_public_opinion(self, aligned=True):
        """
        Reward if user's stance matches collective public sentiment.
        """
        if aligned:
            self.credit_score += 20
            print(f" Opinion aligned with public. Credit Score: {self.credit_score}")
        else:
            print(" Diverging opinion — no credit change (diversity respected).")
    def detect_fake_submission(self, fake=False):
        """
        Penalize if user submits fake evidence or tries manipulation.
        """
        if fake:
            self.credit_score -= 50
            print(f" Fake submission detected! Credit Score: {self.credit_score}")
    def inactivity_penalty(self, months=1):
        """
        Optional: Deduct points for inactivity.
        """
        penalty = months * 5
        self.credit_score -= penalty
        print(f" Inactivity penalty applied: -{penalty} points. Credit Score: {self.credit_score}")
    def get_user_status(self):
        """
        Return current user status and credit score.
        """
        status = "🔵 Trustworthy" if self.credit_score >= 100 else "🟡 Neutral" if self.credit_score >= 50 else "🔴 Low Trust"
        print(f"User ID: {self.user_id} | Credit Score: {self.credit_score} | Status: {status}")
        return {"User ID": self.user_id, "Credit Score": self.credit_score, "Status": status}

# ---------------- Example Usage ----------------
user1 = UserCreditSystem(user_id="User1234")
user1.login_verification(verified=True)          # Proper login
user1.participate(valid_interaction=True)       # Good participation
user1.participate(valid_interaction=False)      # Spam attempt
user1.align_with_public_opinion(aligned=True)  # Aligned opinion
user1.detect_fake_submission(fake=False)
user1.inactivity_penalty(months=1)              # 1-month inactivity
# Final Status
user1.get_user_status()
