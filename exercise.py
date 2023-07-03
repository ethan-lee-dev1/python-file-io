print("opening exercise.py")
with open('origin.txt', 'r') as in_stream:
    print('Opening origin.txt')
    with open('exercise_output.txt', 'w') as out_stream:
        line_num = 0
        for line in in_stream:
            line = line.strip()
            word_list = line.split()
            line_num += 1
            for word in word_list:
                if 'inherit' in word:
                    out_stream.write(str(line_num) + '{0}\n'.format(word))
print('Done!')
print('origin.txt is closed?', in_stream.closed)
print('origin.txt is closed?', out_stream.closed)