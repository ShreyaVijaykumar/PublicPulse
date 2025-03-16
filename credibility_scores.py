# credibility score generator to submit to government which is done by the AI panelist in Google Colab
import matplotlib.pyplot as plt
from fpdf import FPDF
import os
try:
    from google.colab import files
    COLAB_ENV = True
except ImportError:
    COLAB_ENV = False
class AICredibilityScore:
    def __init__(self, biased_result, unbiased_result):
        self.biased_result = biased_result
        self.unbiased_result = unbiased_result
        self.difference = abs(biased_result - unbiased_result)
        self.credibility_score = self.calculate_credibility_score()
    def calculate_credibility_score(self):
        if self.difference <= 5:
            return 100
        elif self.difference <= 15:
            return 70
        else:
            return 40
    def recommendation(self, emoji=True):
        """
        Return recommendation message. If emoji=False, return plain text (for PDF).
        """
        if self.credibility_score == 100:
            return "✅ Recommended for government action" if emoji else "Recommended for government action"
        elif self.credibility_score >= 70:
            return "⚠️ Review advised before action" if emoji else "Review advised before action"
        else:
            return "❌ Not recommended due to high bias" if emoji else "Not recommended due to high bias"
    def visualize_pie_chart(self, filename='Credibility_Pie.png'):
        """
        Display a pie chart to visually represent credibility.
        """
        labels = ['Credible', 'Bias Gap']
        sizes = [100 - self.difference, self.difference]
        colors = ['#4CAF50', '#FF5722']  # Green and Red
        explode = (0.1, 0)
        plt.figure(figsize=(7, 7))
        wedges, texts, autotexts = plt.pie(
            sizes,
            labels=labels,
            autopct='%1.1f%%',
            startangle=140,
            colors=colors,
            explode=explode,
            wedgeprops=dict(width=0.4)
        )
        plt.title("AI Decision Credibility Representation", fontsize=14, fontweight='bold')
        plt.legend(wedges, labels, loc="upper right", fontsize=10)
        plt.figtext(0.5, 0.02, f"Credibility Score: {self.credibility_score} | {self.recommendation(emoji=False)}",
                    ha="center", fontsize=12, color='darkblue', wrap=True)
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()
        return filename
    def generate_pdf_report(self, output_pdf='Credibility_Score_Report.pdf'):
        # Generate pie chart for the report
        chart_path = self.visualize_pie_chart()
        # Create the PDF document
        pdf = FPDF()
        pdf.add_page()
        # Title
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, "AI Credibility Score Report", ln=True, align='C')
        # Summary Text
        pdf.ln(10)
        pdf.set_font("Arial", '', 12)
        summary = (
            f"Biased AI Result: {self.biased_result}%\n"
            f"Unbiased AI Result: {self.unbiased_result}%\n"
            f"Difference: {self.difference}%\n"
            f"Credibility Score: {self.credibility_score}/100\n"
            f"Recommendation: {self.recommendation(emoji=False)}"
        )
        pdf.multi_cell(0, 8, summary)
        # Add Pie Chart Image
        pdf.ln(5)
        pdf.image(chart_path, x=30, w=150)
        # Save as PDF
        pdf.output(output_pdf)
        print(f"✅ PDF report generated: {output_pdf}")
        # Optional cleanup
        if os.path.exists(chart_path):
            os.remove(chart_path)
        # Auto-download if running in Colab
        if COLAB_ENV:
            files.download(output_pdf)
# ----------------- Example Usage -----------------
# Example AI results that trigger "Review advised before action"
biased = 70
unbiased = 80  # Difference = 10 (between 6 to 15)
# Create instance and evaluate
ai_credibility = AICredibilityScore(biased, unbiased)
print(f"Credibility Score: {ai_credibility.credibility_score}")
print("Recommendation:", ai_credibility.recommendation())
# Generate PDF Report with download
ai_credibility.generate_pdf_report('Final_Credibility_Report.pdf')
