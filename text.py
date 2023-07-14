with open('transcript.txt', 'r') as fr:
    lines = fr.readlines()

    with open('transcript.txt', 'w') as fr:
        for line in lines:
            if line[0] != "2":
                fr.write(line)