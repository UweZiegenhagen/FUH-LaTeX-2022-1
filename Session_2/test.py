from shutil import copyfile
from os import unlink
 
# copy file
copyfile('dtk-authoryear.bbx'  , './dtk-bibliography/dtk-authoryear.bbx')
copyfile('dtk-authoryear.dbx'  , './dtk-bibliography/dtk-authoryear.dbx')
copyfile('dtk-bibliography.pdf', './dtk-bibliography/dtk-bibliography.pdf')
copyfile('dtk-bibliography.tex', './dtk-bibliography/dtk-bibliography.tex')
 
# create the zip file
with zipfile.ZipFile('dtk-bibliography.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    z.write('./dtk-bibliography/README.md')
    z.write('./dtk-bibliography/dtk-authoryear.bbx')
    z.write('./dtk-bibliography/dtk-authoryear.dbx')
    z.write('./dtk-bibliography/dtk-bibliography.pdf')
    z.write('./dtk-bibliography/dtk-bibliography.tex')
 
# delete copied files
unlink('./dtk-bibliography/dtk-authoryear.bbx')
unlink('./dtk-bibliography/dtk-authoryear.dbx')
unlink('./dtk-bibliography/dtk-bibliography.pdf')
unlink('./dtk-bibliography/dtk-bibliography.tex')