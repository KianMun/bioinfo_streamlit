def oligocounter(oligo):
    atgc_counter = 0
    a_counter = 0
    t_counter = 0
    g_counter = 0
    c_counter = 0
    u_counter = 0
    counter = len(oligo)
    gc_counter = g_counter + c_counter
    gc_content = 0

    for i in oligo.lower():
        if i == 'a':
            a_counter += 1
        elif i == 't':
            t_counter += 1
        elif i == 'u':
            u_counter += 1
        elif i == 'g':
            g_counter += 1
        elif i == 'c':
            c_counter += 1
        else:
            atgc_counter += 0

    gc_counter = g_counter + c_counter
    
    if gc_counter > 0:
        gc_content = "{:.2f}".format(gc_counter/counter * 100)

    non_atgc = counter - atgc_counter


    return a_counter, t_counter, g_counter, c_counter, u_counter, counter,  gc_counter, gc_content

