# CliniBraz

## Resumo do Projeto

CliniBraz é um sistema de gestão para clínicas odontológicas, desenvolvido com o objetivo de facilitar o agendamento de consultas, o cadastro de pacientes e profissionais, e o acompanhamento do histórico de atendimentos. O projeto conta com um frontend web, voltado para o uso da recepção e dos dentistas no dia a dia da clínica, e um frontend mobile, voltado para os pacientes acompanharem e agendarem suas próprias consultas.

## Funcionalidades

- **Cadastro de pacientes**: registro de informações básicas como nome, telefone e data de nascimento.

- **Cadastro de dentistas**: registro dos profissionais da clínica, incluindo nome e especialidade.

- **Agendamento de consultas**: criação de consultas vinculando paciente, dentista, data e horário. Impedindo agendamentos no mesmo horário para o mesmo dentista e agendamentos no passado

- **Histórico de atendimentos**: registro dos procedimentos realizados em cada consulta (ex: limpeza, canal, extração).

- **Validação de regras de negócio no agendamento**: o sistema impede agendamentos em horários já ocupados para o mesmo dentista, impede agendamentos em datas/horários passados, respeita o horário de funcionamento da clínica (ex: 8h–18h, seg–sex) e limita a duração mínima/máxima de uma consulta.

- **Ciclo de vida da consulta**: cada consulta passa por status ao longo do tempo (agendada → confirmada → em andamento → concluída → cancelada), em vez de ser apenas um registro estático.

- **Perfis de usuário**: o sistema diferencia o acesso e as permissões entre recepcionista, dentista e paciente. 

## Autor

João Guilherme Braz Oliveira