import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(layout='wide')

refrigerantes= { 'nomes':['kuat guarana 2lts','sukita uva 2lts','sukita laranja 2lts','antarctica guarana 2lts','pepsi twist 2lts','pepsi tradicional 2lts','coca-cola 2lts','coca-cola 1,5lts'],
                'valores':[4.99,5.29,5.29,7.49,7.29,7.29,9.99,8.99],
                'quantidades':[2000.0,2000.0,2000.0,2000.0,2000.0,2000.0,2000.0,1500.0]}
df_refri = pd.DataFrame(refrigerantes)

def lino():
    st.markdown("# Apresentação pessoal")
    st.markdown(f"""
                * Me chamo Lino Mufarrej de Carvalho, tenho 44 anos,
                pai de três lindos filhos, resiliente, flexível,
                faixa marrom de jiu-jitsu, matemático em formação,
                fui educador de matemática e educação financeira no 
                Curso pré-vestibular do Centro de Estudos e Ações 
                Solidárias da Maré (CEASM), link 01 abaixo.
                
                * Ministrei o minicurso: Usar o R-Markdown para criação de Relatórios Dinâmicos 
                para graduação e pós na Unirio no ano de 2023, 
                na Mostra de Desenvolvimento Sustentável (SIA2023), link 2 abaixo.
                
                * Participei das Olimpíadas de Inovação da Unirio no ano de 2023 (inovacao), link 3 abaixo.
                
                * Meu currículo Lattes (lattes), link 4 abaixo.
                """,unsafe_allow_html=True)
    
    st.subheader("Links:")
    ceasm = st.page_link('https://www.ceasm.org.br/', label="CEASM")
    sia2023 = st.page_link('https://github.com/petunirio/minicurso_estatistica-2023', label='sia2023')
    inovacao = st.page_link('https://empreende.net.br/olimpiadaunirio/1o-olimpiada-de-inovacao/', label='inovacao')
    lattes = st.page_link('https://buscatextual.cnpq.br/buscatextual/visualizacv.do;jsessionid=514E1B731A33FBDCEA331A8F8F95FBCB.buscatextual_0', label='lattes')

def aula():
    st.markdown("# Apresentação Aula")
    st.markdown("""
                'Diante de uma nova realidade educacional, o <br>
                ensino de matemática não pode manter-se enraizado <br>
                a um processo de ensino usual voltado para uma metodologia <br>
                em que o roteiro a ser seguido começa por uma aula expositi- <br>
                va, seguida de exemplos e, por fim, a resolução de diversos <br>
                exercícios, sem nenhuma aproximação ou inserção da realidade do estudante.'<br>
                fonte: Ensino da Matemática em Debate (ISSN: 2358-4122), São Paulo, v. 6, n. 3, p. 174-206, 2019. 
                """,unsafe_allow_html=True)
    st.markdown("""
                Definições:
                * tópico: **Razão** e **Educação Financeira**,<br>
                * Sequência didática: Ensino por Atividade,<br>
                * Série: sétima série do fundamental 02.<br>
                * Faixa etária: 12-17 anos. 
                """, unsafe_allow_html=True)
    st.markdown("""
                Obs. O estudo de razão possui variadas conexões <br>
                com outras áreas, mas na própria matemática destacamos <br>
                a sua atilização dentro de razões trigonométricas <br> 
                no triângulo retângulo, proporções, juros e probabilidade. 
                """, unsafe_allow_html=True)

def aplicacao():
    import pandas as pd
    
    st.subheader("""
                Você já refletiu sobre quais situações e/ou momentos do seu dia a dia que utiliza ou utilizou conceitos matemáticos, para tomar decisões e/ou resolver as situações (problemas)?"""
                )
    st.markdown("---")
    st.markdown("#### Como você e mais três amigos escolheriam uma das opções que serão descritas abaixo")
    st.markdown("""
                a. Vocês vão jogar (futebol, volei, basquete, queimado, etc) e passam no Multimix
                para comprar um refrigerante, só que vocês querem escolher o refrigerante
                que tem mais e mais barato, como farão a escolha? E quanto Cada um vai pagar? 
                """, unsafe_allow_html=True)
    
    st.write('Imagens retiradas do site dia 20/08/2024')
    st.image('refrigerantes_multimix_f1.png',caption='promoções')
    st.image('refrigerantes_multimix_f2.png', caption='promoções')
    st.image('refrigerantes_multimix_cocacola2lts.png', caption='coca-colas 2lts')
    st.image('refrigerantes_multimix_cocacola1500.png', caption='coca-colas 1,5lts')
    st.page_link('https://www.emporiomultimix.com.br/subcategorias', label='ImporioMultimix')
    st.markdown("---")
    fig = px.bar(df_refri,x='nomes', y='valores', color='nomes')
    st.plotly_chart(fig)

def conceito():
    tab1,tab2 = st.tabs(['Conceito','Soluções'])
    with tab1:
        st.markdown("# Conceito de fração como razão e conceito de razão")
        texto = r'''
                    - Dados dois números **a** e **b**, com b $\not=$ 0, dizemos **razão de a para b**, ou 
                    apenas **razão entre a e b**, nessa ordem, o quociente (resultado) 
                    de $\frac{a}{b}$ que também pode ser indicado por a:b.

                    - O número _a_ é chamado de __antecedente__, e o número _b_ é chamado de __consequente__.
        '''
        st.write(texto)
    with tab2:
        df_refri_original = df_refri
        st.table(df_refri_original)
        st.markdown("---")
        st.write('a. análise do menor valor/quantidade pela tabela')                
        df_refri['valor/qtde'] = df_refri['valores']/df_refri['quantidades']
        st.table(df_refri)
        texto_solucao_a = r'''
        O refrigerante escolhido foi o Kuat guarana 2lts, cada amigo vai pagar $\frac{4.99}{4.0}$~ R$1.25.
        '''
        st.markdown(texto_solucao_a)

paginas = {
    'Apresentacao Lino': lino,
    'Apresentacao Aula': aula,
    'Aula Sequencia 01': aplicacao,
    'Aula Sequencia final': conceito,
}

st.sidebar.image("col-koeler.png", caption="Selecione a opção:")
with st.sidebar:
    selecao = st.selectbox("Selecione a Opção:",options=paginas, label_visibility='collapsed')

paginas[selecao]()