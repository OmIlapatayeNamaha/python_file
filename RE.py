import re
cricet_score="""Sachin scores 76 and \n Dravid scores 40
and Rohit scores 88 and Dhoni scores 99
"""
print(cricet_score)
name=re.findall(r"[A-Z][a-z]*",cricet_score)
print(name)
runs=re.findall(r"\d{2}",cricet_score)
print(runs)

cricet_dashboard={}
i=0
for x in name:
    cricet_dashboard[x]=runs[i]
    i=i+1
print(cricet_dashboard)
