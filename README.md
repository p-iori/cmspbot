# cmspbot
Bot que resolve as tarefas do CMSP Web automaticamente 

1.Instalação:
É necessária uma IDE para rodar o código, assim como o python e a Selenium 

- Baixar o python no pc
- Baixar o vs code (ou outra IDE) no pc
- Baixar a extenção python no vs code (ou outra IDE)
- pip install selenium


2.Personalização:
É necessário fazer algumas alterações no main.py para que o código rode em computadores diferentes. São elas:

- Instalar o webdriver do navegador desejado em sua versão (o webdriver do arquivo é do chrome e pode estar desatualizado)
- Alterar o valor das variáveis RA, DIGITO e SENHA no código para a conta desejada do cmsp
- Caso o computador seja muito lento, aumentar o tempo de espera dos elementos 
