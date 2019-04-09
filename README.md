![](https://github.com/ramonfontes/mn-wifi-book-pt/blob/master/capa.png)


## Resumo
As redes de telecomunicação estão em contínua evolução, sendo profundamente impactadas com novas tecnologias, tais quais os recentes paradigmas Software-Defined Networking (SDN), Software-Defined Wireless Networking (SDWN) e Network Functions Virtualization (NFV). Pesquisas e soluções que explorem novos conceitos, no entanto, precisam ser testados em ambientes controlados, prover resultados confiáveis e, de preferência, possuir portabilidade para infraestruturas de rede físicas. Assim, buscando preencher uma lacuna importante acerca da experimentação de projetos e pesquisas em redes sem fio, o emulador Mininet-WiFi foi desenvolvido. Também capaz de emular um meio com fio, o Mininet-WiFi pode ser utilizado como ferramenta no processo de ensino em redes para diversos níveis de escolaridade e abordando múltiplos casos práticos, incluindo mobilidade, redes mesh e adhoc, balanceamento de carga, segurança, Quality of Service (QoS), MultiPath TCP (MP-TCP), redes veiculares, Internet das coisas, entre outros. Este livro traz uma abordagem ao mundo das redes sem fio com ênfase na  experimentação e casos práticos, os quais são separados em  diferentes níveis de complexidade, mas sempre seguindo um passo-a-passo didático, com acesso ao código-fonte para reprodução das atividades práticas propostas e complementados com leituras adicionais e vídeos demonstrativos. 


## Sumário
* Prefácio
* I Introdução
* 1 Fundamentação teórica  
    * 1.1 Introdução às comunicações sem fio   
    * 1.2 WiFi: Redes locais sem fio baseadas no IEEE 802.11
    * 1.3 Redes sem fio definidas por software
    * 1.4 Mininet-WiFi
        * 1.4.1 Arquitetura
        * 1.4.2 Funcionamento 

* II Nível: iniciante
* 2 Iniciante
    * 2.1 Primeiros passos com Mininet-WiFi
    * 2.2 Customizando topologias
    * 2.3 Acessando informações dos nós
    * 2.4 OVSAP versus UserAP
    * 2.5 Utilizando interfaces gráficas
        * 2.5.1 Visual Network Descriptor
        * 2.5.2 MiniEdit
        * 2.5.3  Visualizando gráficos 2D e 3D
    * 2.6 Emulação do meio sem fio
        * 2.6.1 TC (Traffic Control)
        * 2.6.2 Wmediumd
        * 2.6.3  TC versus Wmediumd na prática
    * 2.7 Modelos de propagação 
        * 2.7.1 Provendo mais realismo
    * 2.8 Relação distância versus sinal recebido
    * 2.9 Modificando o bitrate
    * 2.10 Relação distância versus largura de banda
    * 2.11 Modelos de mobilidade

* III Nível: intermediário
* 3 Intermediário
    * 3.1 Manipulando interfaces 
        * 3.1.1 Definindo múltiplas interfaces
        * 3.1.2 Interfaces binding 
        * 3.1.3 Interfaces bonding
    * 3.2 Análise de tráfego 
        * 3.2.1 Capturando pacotes
        * 3.2.2 Capturando beacons
    * 3.3 Análise do espectro
    * 3.4 Métodos de escaneamento
        * 3.4.1 Escaneamento ativo
        * 3.4.2 Escaneamento passivO
    * 3.5 Wireless mesh e adhoc
    * 3.6 Protocolo OpenFlow
        * 3.6.1 Capturando mensagens OpenFlow
        * 3.6.2 Criando fluxos
        * 3.6.3 OpenFlow no contexto sem fio
        * 3.6.4 Iniciando um controlador remoto
        * 3.6.5 OpenFlow e handover
    * 3.7 Aplicações
        * 3.7.1 Servidor WEB
        * 3.7.2 Servidor DHCP
        * 3.7.3 Lidando com loops
        * 3.7.4 Virtual LAN (VLAN)
        * 3.7.5 Roteamento
        * 3.7.6 Firewall
        * 3.7.7 Qualidade de Serviço (QoS)
        * 3.7.8 MultiPath TCP (MP-TCP)

* IV Nível: avançado
* 4 Avançado
    * 4.1 Manipulando módulos do kernel
    * 4.2 Monitoramento de tráfego com o sFlow-RT
    * 4.3 Reprodução de comportamentos
        * 4.3.1 Atributos de rede
        * 4.3.2 Mobilidade
    * 4.4 Aplicações
        * 4.4.1 Contêineres
        * 4.4.2 Interação entre ambiente virtual e real
        * 4.4.3 Decodificando pacotes
        * 4.4.4 Controle na associação
        * 4.4.5 Encaminhamento por SSID
        * 4.4.6 Segurança
        * 4.4.7 6LoWPAN / IoT
        * 4.4.8 Redes veiculares
* FAQ (Perguntas frequentes)
* Referências

## Organização dos Capítulos?

A organização deste livro se dá da seguinte forma:

Capítulo I, que introduz fundamentos teóricos das redes sem fio, redes sem fio definidas por software e também do Mininet-WiFi. Este capítulo revisa em alto nível conceitos relevantes para os objetivos de aprendizado deste livro. Para um maior aprofundamento nos diferentes tópicos o leitor será apontado para referencias bibliográficas relevantes na área;

Capítulo II, identificado como nível iniciante, que é dedicado exclusivamente a detalhes de funcionamento do Mininet-WiFi, onde os principais aspectos funcionais são apresentados. Se você já conhece o Mininet-WiFi, poderá concentrar-se apenas nos capítulos III e IV. Não é necessário conhecer previamente o Mininet para poder trabalhar com o Mininet-WiFi, mas caso você já o conheça,  certamente terá uma ambientação mais suave em relação a forma de funcionamento do Mininet-WiFi. Os tutoriais neste capítulo podem ser usados no nível de graduação, como atividades complementares em disciplinas teóricas (ex: EA074 na FEEC/UNICAMP)  assim como em roteiros práticos de disciplinas de laboratório (ex: EA080 na FEEC/UNICAMP); 

Capítulo III, que é identificado como nível intermediário, abordará tutoriais relacionados às redes sem fio, redes sem fio definidas por software e também alguns conceitos relacionados à redes de computadores. Este capítulo também inclui a utilização de algumas aplicações de rede, como tcpdump, Wireshark, etc.  Além de atender objetivos pedagógicos de disciplinas mais avançadas na área de redes de computadores como por exemplo laboratórios, os tutoriais neste capítulo são também adequados para disciplinas no nível de pós-graduação (ex: IA369, IA376 na FEEC/UNICAMP) e cursos de especialização (ex: INF-556 no IC/UNICAMP), uma vez que  permitem pesquisas experimentais em cenários mais complexos, incluindo programabilidade de redes definidas por software com o protocolo OpenFlow; 

Por fim, no Capítulo IV, identificado como nível avançado, será possível encontrar tutoriais relacionados à manipulação do núcleo do sistema operacional, contêineres, segurança, IoT, redes veiculares etc., com valiosas informações relacionadas à adaptação do protocolo OpenFlow para as redes sem fio. Este capítulo é rotulado como avançado, pois requer conhecimentos mais aprofundados e o uso de aplicações de terceiros. Portanto, os tutoriais neste capítulo são mais adequados em cursos de especialização e pós-graduação, não só em disciplinas mas também como capacitação técnica de alunos de mestrado e doutorado para o desenvolvimento de pesquisas experimentais visando avanços no estado da arte.  Mas nada impede o leitor curioso de reproduzir esses tutoriais, os quais contam com a mesma explicação passo a passo e o suporte fornecido pelos códigos dos capítulos anteriores.

## Prévia
Os dois primeiros capítulos do livro estão abertos para que você, leitor, sinta-se confortável em adquirir o livro com a certeza de ter feito uma boa escolha. Intitulados de "Introdução" e "Nível: iniciante", esses capítulos trazem uma fundamentação teórica e apresentação do emulador Mininet-WiFi, desde a sua arquitetura de desenvolvimento até a apresentação de alguns comandos e recursos suportados.

Acesse a prévia do livro [aqui](https://github.com/ramonfontes/mn-wifi-book-pt/blob/master/preview-book.pdf).   
 
## Sobre os Autores 
 
- Ramon dos Reis Fontes é Professor Doutor no Instituto Federal de Educação, Ciência e Tecnologia da Bahia (IFBA). Possui Graduação em Bacharelado de Sistemas de Informação pela Faculdade de Tecnologia e Ciências (2009); Mestrado em Sistema e Computação pela Universidade Salvador (UNIFACS) (2014); e doutorado em Engenharia Elétrica na área de Engenharia da Computação pela Universidade Estadual de Campinas (UNICAMP) (2018).   


- Christian Rodolfo Esteve Rothenberg é Professor Doutor no Departamento de Engenharia de Computação e Automação Industrial (DCA) da  Faculdade de Engenharia Elétrica e
Computação (FEEC) pela Universidade Estadual de Campinas (UNICAMP) desde 2013. Possui graduação em Ingeniero Superior de Telecomunicación pela Universidad Politécnica de Madrid (2004), mestrado em Dipl. Ing. Elektrotechnik pela Darmstadt University of Technology (2006) e doutorado em Engenharia Elétrica pela UNICAMP (2010).  

## Onde comprar (versões impressa e e-book)

[Clube dos autores](https://www.clubedeautores.com.br/livro/emulando-redes-sem-fio-com-mininet-wifi#.XKzn1XVKgqo)
