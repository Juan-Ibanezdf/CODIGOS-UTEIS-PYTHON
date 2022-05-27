# Create and Modify PDF
# pip install fpdf
from fpdf import FPDF
pdf = FPDF()
# Add Pages to PDF
pdf.add_page()
# Add Text to PDF
pdf.set_font("Arial", size=12)
pdf.cell(100, 50, txt="Medium Article", ln=1, align="C")
# Add Image
pdf.image("img.jpg", x=10, y=10, w=50, h=50)
# Create Table with MultiCell
pdf.multi_cell(w=0, h=10, txt="Table with MultiCell", border=1, align="C")
# Color of Text
pdf.set_text_color(r=0, g=0, b=0)
# Add Line Break
pdf.ln(10)
# Save PDF
pdf.output("medium_article.pdf")