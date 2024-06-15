import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
data=pd.read_csv('data.csv')
data['constituency_name']=data['constituency_name'].str.replace(' (ST)','').str.replace(' (SC)','')
def election_results(y):
    x=data[data['constituency_name']==y]
    plt.bar(x['party_name'][:5],x['total_votes'][:5])
    plt.xlabel('Party Name')
    plt.ylabel('Total Votes')
    plt.title('Votes Polled by the Top 5 Parties in '+y)
    plt.show()
root=tk.Tk()
root.title("Get Election Results")
root.geometry("400x200")
input_label=tk.Label(root,text="Enter Constituency Name:")
input_label.pack()
input_field=tk.Entry(root)
input_field.pack()
submit_button=tk.Button(root,text="Submit",command=lambda:election_results(input_field.get()))
submit_button.pack()
root.mainloop()