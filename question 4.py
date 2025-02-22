
def program4(file, min, max,count):
    file=open(file)
    lines=file.readlines()
    file.close()
    players=[]
    for line in lines:
        data=line.strip().split(",")
        position=data[0]
        l_name=data[2]
        age=data[3]
        points=int(data[4])
        if min<=points<=max:
            players.append(f"{position},{l_name},{age},{points}")
            count+=1
    ofile=f"{min}to{max}.txt"
    out_file=open(ofile, "w")
    out_file.write("\n".join(players))
    print(count)
    out_file.close()
min=int(input("Enter the min points:"))
max=int(input("Enter the max points:"))
program4("atp.txt",min, max,0)
