def bin_a_dec(b):
    numero = 0
    cont = 0
    for i in b[::-1]: # Iterating through b in reverse order
      numero += int(i)*(2**cont)
      cont += 1
    return numero

print(bin_a_dec("101010")) # 42