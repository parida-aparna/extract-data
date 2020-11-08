import csv
import copy
import pandas as pd

with open("result.txt",'w') as openfile:
	openfile.write('')

	
rows=[]
column=[]
def binary_search(arr, x): 
	low = 0
	high = len(arr) - 1
	mid = 0
  
	while low <= high: 
  
		mid = (high + low) // 2
  
        # Check if x is present at mid 
		if arr[mid] < x: 
			low = mid + 1
  
        # If x is greater, ignore left half 
		elif arr[mid] > x: 
			high = mid - 1
  
        # If x is smaller, ignore right half 
		else: 
			return mid 
  
    # If we reach here, then the element was not present 
	return -1

with open("papers1.csv","r") as f:
	
	csv_reader = csv.reader(f, delimiter=',')
	df=pd.read_csv('papers1.csv', usecols= [0])
	
	for row in csv_reader:
		rows.append(row)
	for row in rows:
		column.append(row[0])
	
	
	line_count = 0
	count=0
	for row in rows:
		authors=[]
		references=[]
		ref_authors=[]
		
		
		row3=row[1].split(' ')
		row3.pop()
		
	
		for r in row3:
			authors.append(r)
		
		row3=row[2].split(' ')
		
		for r in row3:
			if r!=0:	
				references.append(r)
			else:
				break
		sz=len(references)
		#ele=binary_search(df[0],1091)
		
		
	
		if sz>0:
			for ref in references:
				ind=binary_search(column,ref)
				if ind!=-1:
					sz-=1
					row4=rows[ind][1].split(' ')
					row4.pop()
					for a in row4:
						ref_authors.append(a)
				if sz==0:
					break
			
			for author in authors:
				for reference in ref_authors:
					with open("result.txt",'a') as openfile:	
						openfile.write(f'{author} {reference}\n')
						count+=1
						print(count)
		line_count+=1
		print(line_count)

