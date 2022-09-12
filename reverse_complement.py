def reverse_complement(template):
    reverse =''
    for i in template.lower():
        if i == 'a':
            reverse += 't'
        elif i == 't':
            reverse += 'a'
        elif i == 'g':
            reverse += 'c'
        elif i == 'c':
            reverse += 'g'
        elif i == 'u':
            reverse += 'a'
       

    return reverse[::-1]
