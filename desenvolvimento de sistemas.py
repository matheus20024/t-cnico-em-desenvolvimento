banco_de_dados_i = float(input("Digite a nota do Banco de Dados I: "))
etica_e_cidadania_organizacional = float(input("Digite a nota do Ética e Cidadania Organizacional: "))
tecnicas_programacao_e_algoritmos = float(input("Digite a nota do Técnicas de Programação e Algoritmos: "))
fundamentos_da_informatica = float(input("Digite a nota do Fundamentos da Informática: "))
design_digital = float(input("Digite a nota do Design Digital: "))
sistemas_embarcados = float(input("Digite a nota do Sistemas Embarcados: "))
programacao_web_i = float(input("Digite a nota do Programação Web I: "))
planejamento_e_desenvolvimento_do_trabalho_de_conclusao = float(input("Digite a nota do Planejamento e Desenvolvimento do Trabalho de Conclusão: "))
banco_de_dados_ii = float(input("Digite a nota do Banco de Dados II: "))
programacao_de_aplicativos_mobile = float(input("Digite a nota do Pogramação de Aplicativos Mobile: "))
qualidade_de_teste_de_software = float(input("Digite a nota do Qualidade de Teste de Software: "))
programacao_web_ii = float(input("Digite a nota do Programação Web II: "))
internet_protocolos_e_sistemas_de_informacao = float(input("Digite a nota do Internet, Protocolos e Segurança de Sistemas de Informação: "))
analise_e_projeto_de_sistemas = float(input("Digite a nota do Análise e Projeto de Sistemas: "))
desenvolvimento_de_sistemas = float(input("Digite a nota do Desenvolvimento de Sistemas: "))
soma = (banco_de_dados_i + etica_e_cidadania_organizacional + tecnicas_programacao_e_algoritmos + fundamentos_da_informatica + design_digital + sistemas_embarcados + programacao_web_i + planejamento_e_desenvolvimento_do_trabalho_de_conclusao + banco_de_dados_ii + programacao_de_aplicativos_mobile + qualidade_de_teste_de_software + programacao_web_ii + internet_protocolos_e_sistemas_de_informacao + analise_e_projeto_de_sistemas + desenvolvimento_de_sistemas) / 15
if soma > 7.0:
    print(f"Parabens você passou com {soma}")
else:
    print(f"Você foi reprovado com {soma}")