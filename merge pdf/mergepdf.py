'''from PyPDF2 import PdfFileMerger

merger=PdfFileMerger()
merger.append("pdf1.pdf.pdf")
merger.append("pdf2.pdf.pdf")

merger.write("merged_output.pdf")
merger.close()'''

'''from PyPDF2 import PdfMerger

me'''

from reportlab.pdfgen import canvas

# Create pdf1.pdf
c = canvas.Canvas("pdf1.pdf")
c.drawString(100, 750, "This is PDF 1")
c.save()

# Create pdf2.pdf
c = canvas.Canvas("pdf2.pdf")
c.drawString(100, 750, "This is PDF 2")
c.save()

from PyPDF2 import PdfMerger

merger = PdfMerger()
merger.append("pdf1.pdf")
merger.append("pdf2.pdf")

merger.write("merged_output.pdf")
merger.close()
