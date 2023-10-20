import tkinter as tk

from pylovepdf.tools.compress import Compress
from pylovepdf.tools.imagetopdf import ImageToPdf
from pylovepdf.tools.merge import Merge
from pylovepdf.tools.pagenumber import Pagenumber
from pylovepdf.tools.pdftojpg import PdfToJpg
from pylovepdf.tools.unlock import Unlock
from pylovepdf.tools.split import Split

public_key = 'project_public_a03d3f8b991192f15821966f651af646_CMzqa559f57d368e300b964342e47b3bb19e3'

def compress_pdf():
  t = Compress(public_key, verify_ssl=True, proxies="")
  t.add_file('sample.pdf')
  t.set_output_folder('output_directory')
  t.execute()
  t.download()
  t.delete_current_task()
# Create a function to be executed when the button is clicked

def image_to_pdf():
    t = ImageToPdf(public_key, verify_ssl=True)
    t.add_file('IMG-20231004-WA0002.jpg')
    t.debug = False
    t.orientation = 'portrait'
    t.margin = 0
    t.pagesize = 'fit'
    t.set_output_folder('output_directory')
    t.execute()
    t.download()
    t.delete_current_task()

    
def merge_pdf():
    t = Merge(public_key, verify_ssl=True, proxies='')
    # two files needed
    t.add_file('sample.pdf')
    t.add_file('dummy.pdf')
    t.debug = False
    t.set_output_folder('output_directory')

    t.execute()
    t.download()
    t.delete_current_task()

def pageNumber():
    t = Pagenumber(public_key, verify_ssl=True, proxies='')
    t.add_file('dummy.pdf')
    t.debug = False
    t.set_output_folder('output_directory')
    t.execute()
    t.download()
    t.delete_current_task()

def pdf_to_jpg():
    t = PdfToJpg(public_key, verify_ssl=True, proxies='')
    t.add_file('dummy.pdf')
    t.debug = False
    t.pdfjpg_mode = 'pages'
    t.set_output_folder('output_directory')
    t.execute()
    t.download()
    t.delete_current_task()

def unlock_pdf():
    t = Unlock(public_key, verify_ssl=True, proxies='')
    t.add_file('sample.pdf')
    t.debug = False
    t.set_output_folder('output_directory')
    t.execute()
    t.download()
    t.delete_current_task()

def split_pdf():
    t = Split(public_key, verify_ssl=True, proxies='')
    t.add_file('sample.pdf')
    t.debug = False
    t.split_mode = 'ranges'
    t.fixed_range = '2'
    t.set_output_folder('output_directory')
    t.execute()
    t.download()
    t.delete_current_task()


# Create the main window
window = tk.Tk()
window.title("Button Card UI")

# Create a label to display a message
label = tk.Label(window, text="Press the button below")
label.pack(pady=10)

# Create a button
button1 = tk.Button(window, text="Compress PDF", command=compress_pdf)

button2 = tk.Button(window, text="Image to PDF", command=image_to_pdf)

button3 = tk.Button(window, text="Merge Pdf", command=merge_pdf)

button4 = tk.Button(window, text="Page Number", command=pageNumber)

button5 = tk.Button(window, text="PDF to JPG", command=pdf_to_jpg)

button6 = tk.Button(window, text="Unlock PDF", command=unlock_pdf)

button7 = tk.Button(window, text="Split PDF", command=split_pdf)

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()




# Run the main event loop
window.mainloop()
