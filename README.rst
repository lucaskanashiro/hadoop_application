.. -*- coding: utf-8 -*-

.. highlight:: rest

.. _hadoop_application:

=================================
Hadoop aplicado 
=================================

O que é o Hadoop?
=================

Apache Hadoop é um framework open-source para armazenamento e processamento em larga escala de conjuntos de dados voltados para hardware de baixo custo. Hadoop é um projeto de nível superior Apache sendo construído e usado por uma comunidade global de colaboradores e usuários. Ele é licenciado sob a licença Apache 2.0. 
O quadro Apache Hadoop é composto por diversos módulos, entre os principais que são: 

* Hadoop Common - contém as bibliotecas e utilitários necessários para outros módulos do Hadoop 

* Hadoop Distributed File System (HDFS) - um sistema de arquivos distribuído que armazena dados em máquinas de baixo custo, proporcionando alta largura de banda entre clusters. 

* Hadoop MapReduce - um modelo de programação para o processamento de dados em larga escala.

Como instalar o Hadoop
----------------------
Segue abaixo o link utilizado para instalação do Hadoop 2.4.0

.. code-block::

  http://hadoop.apache.org/docs/r2.4.0/hadoop-project-dist/hadoop-common/SingleCluster.html


Aplicação dados abertos
===========================

Aplicação que realiza análise da similaridade de votos entre partidos a partir dos dados abertos da Câmara de São Paulo com o intuito de realizar uso de Hotspots do framework MapReduce.

Como executar a aplicação
-------------------------
Os pré-requisitos para a execução da aplicação são: PHP, Python, Java e Hadoop:


.. code-block::

  /opt/hadoop/hadoop-2.4.0/hadoop_application/html $  python main.py [ano]
  
A aplicação esta no formato Java, mas é chamada dentro de um script em Python. O script executa o Hadoop, processando os arquivos da pasta 'input' executando a tarefa de MapReduce. Por fim os dados são analisados antes que sejam escritos no arquivo HTML para geração dos gráficos.
