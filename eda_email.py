import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
import mailbox
import csv
import re
import datetime
import pytz
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from scipy import ndimage
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import seaborn as sns
from wordcloud import WordCloud

def extract_email_ID(string):
  email = re.findall(r'<(.+?)>', string)
  if not email:
    email = list(filter(lambda y: '@' in y, string.split()))
  return email[0] if email else np.nan

def refactor_timezone(x):
  est = pytz.timezone('US/Eastern')
  return x.astimezone(est)

def plot_todo_vs_year(df, ax, color='C0', s=0.5, title=''):
  ind = np.zeros(len(df), dtype='bool')
  est = pytz.timezone('US/Eastern')
  df[~ind].plot.scatter('year', 'timeofday', s=s, alpha=0.6, ax=ax,
color=color)
  ax.set_ylim(0, 24)
  ax.yaxis.set_major_locator(MaxNLocator(8))
  ax.set_yticklabels([datetime.datetime.strptime(str(int(np.mod(ts,24))), "%H").strftime("%I %p") for ts in ax.get_yticks()])
  ax.set_xlabel('')
  ax.set_ylabel('')
  ax.set_title(title)
  ax.grid(ls=':', color='k')
  return ax


mboxfile = "C:/Users/kisho/Documents/course_file/2026-2027/AD1203/email/All_mail_Including_Spam_and_Trash.mbox"
mbox = mailbox.mbox(mboxfile)
#for key in mbox[0].keys():
#  print(key)

with open('C:/Users/kisho/Documents/course_file/2026-2027/AD1203/email/mailbox.csv', 'w') as outputfile:
 writer = csv.writer(outputfile)
 writer.writerow(['subject','from','date','to','label','thread'])
 for message in mbox:
    writer.writerow([
      message['subject'],
      message['from'],
      message['date'],
      message['to'],
      message['X-Gmail-Labels'],
      message['X-GM-THRID']
    ]
 )


outputfile.close()
# Load the dataset
dfs = pd.read_csv('C:/Users/kisho/Documents/course_file/2026-2027/AD1203/email/mailbox.csv') # Display basic information about the dataset
print(dfs.info())

# # Display the first few rows of the dataset print(df.head())
# # Descriptive statistics 
print(dfs.describe())
# # Check for missing values 
print(dfs.isnull().sum())


dfs['date'] = dfs['date'].apply(lambda x: pd.to_datetime(x,errors='coerce', utc=True))

dfs = dfs[dfs['date'].notna()]


dfs['from'] = dfs['from'].apply(lambda x: extract_email_ID(x))

myemail = 'kishorekumaraiml@dmice.ac.in'
dfs['label'] = dfs['from'].apply(lambda x: 'sent' if x==myemail else 'inbox')
dfs.drop(columns='to', inplace=True)
dfs.head(10)
dfs['date'] = dfs['date'].apply(lambda x: refactor_timezone(x))

# Visualize the distribution of numerical variables 
sns.pairplot(dfs)
plt.show()
# Visualize the distribution of categorical variables 
sns.countplot(x='label', data=dfs)
plt.show()
# Correlation matrix for numerical variables 
correlation_matrix = float(dfs.corr())
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm') 
plt.show()
# Word cloud for text data (if you have a column with text data) from wordcloud 
text_data = ' '.join(dfs['text_column'])
wordcloud = WordCloud(width=800, height=400, random_state=21, max_font_size=110).generate(text_data)
plt.figure(figsize=(10, 7)) 
plt.imshow(wordcloud, interpolation="bilinear") 
plt.axis('off')
plt.show()

