import os,re,time,subprocess

folder2 = os.getcwd()
folderout = os.path.join(folder2, 'output')

mkvpaths = []
mkvnames = []
subpaths = []
fontpaths = []

def replace(s):
	x=s.replace('-', '').replace(" ", "").replace("[","").replace("]","").replace("_","").replace("(","").replace(")","")
	return x.lower()

for root, dirnames, filenames in os.walk(folder2):
	for filename in filenames:

		if filename.lower().endswith('.mkv'):
			mkvpaths.append(os.path.join(root, filename))
			replaced = filename.replace('.mkv', '')
			replaced = replaced.strip()
			mkvnames.append(replaced)

		if filename.lower().endswith('ass'):
			subpaths.append(os.path.join(root, filename))

		if filename.lower().endswith('ttf') or filename.lower().endswith('otf'):
			fontpaths.append(os.path.join(root, filename))

def match(mkvnames, mkvpaths, fontpaths,subpaths):

	for i in range(len(mkvnames)):

		y=0
		pattern = re.compile(replace(mkvnames[i]))
		outpath = os.path.join(folderout, mkvnames[i]+".mkv")
		command=['mkvmerge', '--output', outpath, '--no-attachments','--no-subtitles', mkvpaths[i]]
		
		for x in range(len(subpaths)):

			matches = pattern.findall(replace(subpaths[x]))
			if matches:
				y=1
				command.extend([subpaths[x]])
		
		for x in range(len(fontpaths)):

			matches = pattern.findall(replace(fontpaths[x]))
			if matches:
				y=1
				command.extend(["--attach-file", fontpaths[x]])
			
		#print(command)
		
		if y==1:
			subprocess.call(command)
		elif y==0:
			print("No matches")
		else:
			print("Error in matching")

def match_debug(mkvnames, mkvpaths, fontpaths,subpaths):

	for i in mkvnames:
		print(replace(i))
	for i in fontpaths:
		print(replace(i))
	for i in subpaths:
		print(replace(i))

match(mkvnames, mkvpaths, fontpaths, subpaths)

print("Done")