file=os.path.join('..','Desktop','paragraph_1.txt')
lines =0
nwords =0
nsent=0
nchar=0
with open(file,'r') as f:
    for line in f:
        chars=line
        words=line.split()
        sents=line.splitlines()
        lines+=1
        nwords+=len(words)
        nsent+=len(sents)
        nchar+=len(chars)
        avg_let_ct=(nchar)/(nwords)
        avg_sent_len=(nwords)/(nsent)

print('Paragraph Analysis')
print('---------------------')
print("Approximate sentence count:",nsent)
print("Approximate Word Count:",nwords)
print("Average Letter Count:", float(avg_let_ct))
print("Average Sentence Length:", avg_sent_len)
