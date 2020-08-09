seq = []
maxnum = []
end_loop =""

while end_loop != "exit":

    seqq = input ("Enter valid sequesnce: ").upper()
    print(seqq)
    length = len(seqq)

    G = seqq.count('G')
    C = seqq.count('C')

    GC = G + C

    print ("\nlength of sequence is: ",length)
    print("GC count is: ",GC)

    GC_percent = (GC / length) * 100
    print("GC% is: ","%.3f"%GC_percent)

    seq.append(seqq)
    print(seq)
    maxnum.append(GC_percent)
    print(maxnum)

    end_loop = input("\nEnter exit ti end\nOr press any key to continue")

seq_score = dict()
seq_score = seq_score.update(zip(GC_percent,seq))
seq_max = seq_score[max(seq_score.key())]
print(seq_max)