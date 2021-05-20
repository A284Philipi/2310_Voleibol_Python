casos = int(input())
cont = int(0)
saques_total = int(0)
bloqueios_total = int(0)
ataques_total = int(0)
ataques_efetuados = int(0)
bloqueios_efetuados = int(0)
saques_efetuados = int(0)
while cont < casos:
    jogador = str(input())
    a, b, c = input().split(" ")
    d, e, f = input().split(" ")
    saques_feitos = int(a)
    bloqueios_feitos = int(b)
    ataques_feitos = int(c)
    saques_concluidos = int(d)
    bloqueios_concluidos = int(e)
    ataques_concluidos = int(f)
    saques_total = saques_total + saques_feitos
    bloqueios_total = bloqueios_total + bloqueios_feitos
    ataques_total = ataques_total + ataques_feitos
    ataques_efetuados = ataques_efetuados + ataques_concluidos
    bloqueios_efetuados = bloqueios_efetuados + bloqueios_concluidos
    saques_efetuados = saques_efetuados + saques_concluidos
    cont = cont + 1
porcentagem_saques = float((saques_efetuados * 100) / saques_total)
porcentagem_bloqueios = float((bloqueios_efetuados * 100) / bloqueios_total)
porcentagem_ataques = float((ataques_efetuados * 100) / ataques_total)
print("Pontos de Saque: %.2f " %(porcentagem_saques) + "%.")
print("Pontos de Bloqueio: %.2f " %(porcentagem_bloqueios) + "%.")
print("Pontos de Ataque: %.2f " %(porcentagem_ataques) + "%.")