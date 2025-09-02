# ============================================
# Simulação da Troca de Chaves Diffie–Hellman
# ============================================

# Valores públicos (todo mundo pode ver)
PRIMO_GRANDE = 29   # número primo (pequeno só para o exemplo)
BASE = 5            # gerador

# Segredos privados (cada um escolhe em segredo)
SEGREDO_ALICE = 12  # segredo que só a Alice sabe
SEGREDO_BOB = 15    # segredo que só o Bob sabe

# Cada um gera sua chave pública
CHAVE_PUBLICA_ALICE = pow(BASE, SEGREDO_ALICE, PRIMO_GRANDE)
CHAVE_PUBLICA_BOB = pow(BASE, SEGREDO_BOB, PRIMO_GRANDE)

print("Chave pública da Alice:", CHAVE_PUBLICA_ALICE)
print("Chave pública do Bob:  ", CHAVE_PUBLICA_BOB)

# Agora eles trocam as chaves públicas pela internet

# Cada um calcula o segredo compartilhado usando a chave pública do outro
SEGREDO_COMPARTILHADO_ALICE = pow(CHAVE_PUBLICA_BOB, SEGREDO_ALICE, PRIMO_GRANDE)
SEGREDO_COMPARTILHADO_BOB   = pow(CHAVE_PUBLICA_ALICE, SEGREDO_BOB, PRIMO_GRANDE)

print("Segredo-CompartilhadoAlice:", SEGREDO_COMPARTILHADO_ALICE)
print("Segredo-CompartilhadoBob:  ", SEGREDO_COMPARTILHADO_BOB)

# Teste de consistência
if SEGREDO_COMPARTILHADO_ALICE == SEGREDO_COMPARTILHADO_BOB:
    print("\n✅ Alice e Bob chegaram no mesmo segredo compartilhado!")
else:
    print("\n❌ Algo deu errado, os segredos não batem.")
