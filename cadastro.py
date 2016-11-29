def cadastro_usuario(mail,passwd,user):
    users = open('db/user/users.bin','r')
    u = ''
    while True:
        ultimo = u
        u = users.readline()
        if not u:
            users.close()
            break
    print ultimo
    ultimo = ultimo.split(";")
    id_user = int(ultimo[0]) + 1

    users = open('db/user/users.bin','a')
    users.write(str(id_user)+";"+str(mail)+";"+str(passwd)+";"+str(user)+"\n")
    out = 1
    return out
