#Import Packages
import re
import pygsheets

# ID of the Source Sheet (MAPPING SHEET)
READ_SHEET_ID = '---Insert Sheet ID Here---'
# COL NUMBER USED TO MATCH CATEGORY
COLUMN_NUMBER_FOR_DICT_KEY = 2
# COL NUMBER USED TO MATCH SUB-CAT
COLUMN_NUMBER_FOR_DICT_VAL = 1

# ID OF WRITE (TARGET) SHEET
WRITE_SHEET_ID = '---Insert Sheet ID Here---'
# COL NUMBER USED TO MATCH CATEGORY
COLUMN_NUMBER_READ_VALUE = 1
# COL NUMBER OF WRITE COLUMN
COLUMN_NUMBER_WRITE_VALUE = 2


# FOLLOW STEPS HERE - https://pygsheets.readthedocs.io/en/stable/authorization.html#oauth-credentials
#Rename the downloaded JSON key to below
gs = pygsheets.authorize(client_secret='./credentials.json')



# Cleaning text to remove special characters, numbers, white spaces, etc.
def clean_text(raw_text):
	text = raw_text.lower()
	text = re.sub(r'[0-9]', ' ', text)
	text = re.sub(r'_', ' ', text)
	#remove anything else in the text that isn't a word character or a space (e.g., punctuation, special symbols, etc.)
	text = re.sub(r'[^\w\s]', ' ', text)
	text = text.replace(' ', '')
	text = text.strip()
	return text



"""
READ PART OF CODE TO CREATE DICTIONARY FROM SOURCE FILE IN GOOGLE SHEETS
"""
sh = gs.open_by_key(READ_SHEET_ID)
wk1 = sh[0]
# Read and store data for processing
read_val_col1 = wk1.get_col(COLUMN_NUMBER_FOR_DICT_VAL, include_tailing_empty=False)
read_val_col1 = read_val_col1[1:]
read_val_col2 = wk1.get_col(COLUMN_NUMBER_FOR_DICT_KEY, include_tailing_empty=False)
read_val_col2 = read_val_col2[1:]
"""value_dict = wk1.get_all_records()"""
value_list = map(list, zip(read_val_col1, read_val_col2))
"""for i in value_dict:
	value_list.append(list(i.values()))"""
# Init Category Dictionary
category_dict = {}
# Populate Category dictionary
for a, b in value_list:
	if b in category_dict.keys():
		category_dict[b].append(clean_text(a))
	else:
		category_dict[b] = [clean_text(a)]


"""
WRITE PART OF CODE TO WRITE MAPPED CATEGORY TO TAGRET DOCUMENT IN GOOGLE SHEETS
"""
sh2 = gs.open_by_key(WRITE_SHEET_ID)
wk2 = sh2[0]
read_val_col = wk2.get_col(COLUMN_NUMBER_READ_VALUE, include_tailing_empty=False)
read_val_col = read_val_col[1:]
print(read_val_col)
#result col values
result_map_col = []
for i in read_val_col:
	not_found = True
	for j in category_dict:
		if clean_text(i) in category_dict[j]:
			result_map_col.append(j)
			not_found = False
			break
	if not_found == True:
		result_map_col.append('')
print(result_map_col)
wk2.update_col(COLUMN_NUMBER_WRITE_VALUE, result_map_col, row_offset=1)