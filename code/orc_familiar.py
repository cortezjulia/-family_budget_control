#FERRAMENTA PARA CONTROLE DE ORÇAMENTO FAMILIAR

import os
import unicodedata
from simple_colors import *
import time
import matplotlib.pyplot as plt
import sys
import numpy as np

#variable initialization
total_income=0
income_sum_list=[]
spending_sum_list=[]
balance_month_list=[]
categories_by_month=[]
final_total_income=0.0


#immutable standard variables
official_month=['JAN','FEV','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ']
inputs = {
    'Renda': ['Salários','13º Salário','Férias','Renda extra','Alugueis','Juros de Investimento'],
    'Habitação': ['Prestação de compra','Aluguel','Água','IPTU','Luz','Telefone','TV por assinatura','Supermercado','Empregada','Reformas'],
    'Saúde': ['Plano de saúde','Médico','Dentista','Medicamentos','Seguro de vida'],
    'Impostos':['IRFF','INSS'],
    'Auto':['Prestação','Seguro','Combustível','Lavagens','IPVA','Mecânico','Multas'],
    'Pessoal':['Higiene pessoal','Cosméticos','Cabelereiro','Vestuário','Lavanderia','Academia','Unhas','Cursos'],
    'Dependentes':['Escola/Faculdade','Cursos Extras','Material escolar','Esportes/Uniformes','Mesada','Passeios/Férias','Vestuário','Saúde'],
    'Lazer':['Restaurantes','Livraria','Streamings','Passagens','Hotéis','Passeios'],
    'Investimentos':['Previdência','Aplicações']

}
#dicts that receives user input values
expenses_months={
    'JAN': [],
    'FEV': [],
    'MAR': [],
    'ABR': [],
    'MAI': [],
    'JUN': [],
    'JUL': [],
    'AGO': [],
    'SET': [],
    'OUT': [],
    'NOV': [],
    'DEZ':[],
}
values_months={
    'JAN':[],
    'FEV':[],
    'MAR':[],
    'ABR':[],
    'MAI':[],
    'JUN':[],
    'JUL':[],
    'AGO':[],
    'SET':[],
    'OUT':[],
    'NOV':[],
    'DEZ': [],
}
#function that validates if the inserted month is present in the registered data "official months"
def month_comparation(month_comparation):

    flag3=False
    month_comparation=str_accentuation_check(month_comparation)
    month_comparation=month_comparation.lower()
    
    for m in official_month:
       
        original_m=m
        m=m.lower()
        if m==month_comparation:
            flag3=True
            break
    
    if flag3==False:
        original_m='nulo'

        
    return original_m


#receives, processes and saves the values ​​received from the user
def parameters_receive(expense_groupe,expense,value,month):
   

    expense=str(expense)
    expense_groupe=str(expense_groupe)

    
    
    final_expense,final_groupe=expenses_comparation(expense,expense_groupe)
    final_month=month_comparation(month)
    

    if (final_groupe or final_expense)=='nulo':
        print(green('***O GASTO INSERIDO NÃO CORRESPONDE A NENHUM GASTO CADASTRADO***','bold'))
        time.sleep(3)
        return 
    if (final_month)=='nulo':
        print(green('***O MÊS INSERIDO NÃO CORRESPONDE A NENHUM MÊS CADASTRADO***','bold'))
        time.sleep(3)
        return 

    expenses_months[final_month].append(final_expense)
    values_months[final_month].append(value)

#prints the menu and receives user input
def menu():
    os.system('cls')
    ind=0
    for key, value in inputs.items():
        print('\n')
        print(magenta(f'----------{key}----------','bold'))
        print('\n')
        for ind,va in enumerate(value):
            
            print(f'{ind} - {va}')
            
    print('\n')
    user_groupe=input(magenta('Insira o gasto geral: ',['bold','bright']))
    user_name=input(magenta('Insira o gasto específico: ',['bold','bright']))
    user_value=input(magenta('Insira o valor: ',['bold','bright']))
    user_month=input(magenta('Insira o mês: ',['bold','bright']))

    try:
        user_value=float(user_value)
    except:
        print(green('***INSIRA APENAS NÚMEROS PARA O VALOR***','bold'))
        time.sleep(4)
        user_value='error'
    os.system('cls')
    return user_groupe,user_name,user_value,user_month

#remove accents from words
def str_accentuation_check(conv_str):
    str_converter = unicodedata.normalize("NFD", conv_str)
    str_converter = str_converter.encode("ascii", "ignore")
    str_converter = str_converter.decode("utf-8")
    str_converter=str_converter.lower()

    return str_converter

#checks if the word strings are present in the files registered in "inputs" 
def expenses_comparation(expense_comparation,expense_groupe_comparation):
    flag1=False
    flag2=False

    expense_comparation=str_accentuation_check(expense_comparation)
    expense_groupe_comparation=str_accentuation_check(expense_groupe_comparation)
    expense_comparation=expense_comparation.lower()
    expense_groupe_comparation=expense_groupe_comparation.lower()

    
    for key,item in inputs.items():
       
       original_groupe=key
       key=str_accentuation_check(key)
       key=key.lower()

       if key==expense_groupe_comparation:
           flag1=True
           break

    for item in inputs[original_groupe]:
        original_expense=item
        item=str_accentuation_check(item)
        item=item.lower()

        if item==expense_comparation:
            flag2=True
            break
    
   

    if (flag1 and flag2)==False:
        original_expense='nulo'
        original_groupe='nulo'
    
   
    return original_expense,original_groupe

#print the results
def result_prints(choose_month,pr_or_not):
    os.system('cls')
    sum_values=0.0
    different_color=0
    income_sum=0
    
    spending_sum=0
    month_integer_name=print_month_name(choose_month)

    if pr_or_not==0:
        print('\n')
        print(green(f'----------{month_integer_name}----------','bold'))
        print('\n')

    for gr in inputs.keys():
        if pr_or_not==0:
            print('\n')    
            print(magenta(f'----------{gr}----------'))
            print('\n')

        for exp in inputs[gr]:
            sum_values=0.0
            for index,user in enumerate(expenses_months[choose_month]):
                
                if user==exp:
                    sum_values=sum_values+values_months[choose_month][index]
                    #print("\n",'\033[1m')
                    different_color=1
                    
                    if gr=='Renda':
                        income_sum=income_sum+sum_values
                        
                    else:
                        spending_sum=spending_sum+sum_values

                    
            if pr_or_not==0:
                if different_color==0:
                    print(f'{exp} - {sum_values}')
                else:
                    print(magenta(f'{exp} - {sum_values}','bold'))
                    different_color=0
                #print("",'\033[0m')

   
            
          
          
    return income_sum,spending_sum
    
#calculates total income, expenses and balances       
def extra_calculations(receive_income_sum,receive_spending_sum,receive_increment_month):
    global final_total_income
    total_income=0.0
    total_spending=0.0
    accumulated_balance=0.0
    os.system('cls')

    income_sum_list.append(receive_income_sum)
    try:
            if type(income_sum_list[12]) is float or int:
                del income_sum_list[12]
    except:
            print()

    spending_sum_list.append(receive_spending_sum)
    try:
            if type(spending_sum_list[12]) is float or int:
                del spending_sum_list[12]
    except:
            print()
        
   
    if receive_increment_month==11:
        print('\n')
        print(magenta('----------RENDIMENTOS MENSAIS----------','bold'))
        print('\n')
        
        for i,j in enumerate(official_month):
            try:
                print(f'{j} - {income_sum_list[i]}')
                total_income=income_sum_list[i]+total_income
            except:
                print()

        print('\n')
        print(magenta(f'Total: {total_income}','bold'))
        final_total_income=total_income


        
        print('\n')
        print(magenta('----------GASTOS MENSAIS----------','bold'))
        print('\n')
        
        for i,j in enumerate(official_month):
                
            try:
                print(f'{j} - {spending_sum_list[i]}')
                total_spending=spending_sum_list[i]+total_spending
            except:
                print()

        print('\n')
        print(magenta(f'Total: {total_spending}','bold'))

        

        print('\n')
        print(magenta('----------SALDOS MENSAIS----------','bold'))
        print('\n')
        
        for o,p in enumerate(official_month):
        
                balance_month=income_sum_list[o]-spending_sum_list[o]
                if balance_month<0:
                    print(red(f'{p} - {balance_month}'))
                elif balance_month>0:
                     print(green(f'{p} - {balance_month}'))
                else:
                     print(f'{p} - {balance_month}')

                balance_month_list.append(balance_month)
                try:
                    if type(balance_month_list[12]) is float or int:
                        del balance_month_list[12]
                except:
                    print()
                
                

        print('\n')
        print(magenta('----------SALDOS ACUMULADOS----------','bold'))
        print('\n')
        
        for l,m in enumerate(official_month):
                
            accumulated_balance=accumulated_balance+balance_month_list[l]
            
            if accumulated_balance<0:
                print(red(f'{m} - {accumulated_balance}'))
            elif accumulated_balance>0:
                print(green(f'{m} - {accumulated_balance}'))
            else:
                print(f'{m} - {accumulated_balance}')
        
#menu for final user decisions: exit, restart, review and graphics
def final_menu():
        while True:
           
            print('\n')
            print(green('O que você deseja fazer?','bold'))
            print('\n')
            print(magenta('Ver Gráficos com os dados gerados: [1]','bold'))
            print(magenta('Ver a lista completa dos dados inseridos: [2]','bold'))
            print(magenta('Sair: [3]','bold'))
            print(magenta('Reiniciar: [4]','bold'))
            print('\n')
            option_final=input(green('Insira o número correspondente: ','bold'))    

            if option_final == '1':
                os.system('cls')   
                while True:
                    os.system('cls')  
                    print(magenta('Gráficos disponíveis:','bold'))
                    print('\n')
                    print(green('Rendimentos e Despesas Anuais [1] ----------- Distribuição por categorias [2]','bold'))
                    print('\n')
                    op_graph=input(magenta('Digite o número correspondente ao gráfico que deseja ver: ','bold'))
                    if op_graph == '1':
                        print('\n')
                        print(green("Você escolheu 'Rendimentos e Despesas Anuais'",'bold'))
                        print('\n')
                        plt.plot(official_month, income_sum_list, label = "Rendimentos")
                        plt.plot(official_month, spending_sum_list, label = "Gastos")
                        plt.plot(official_month, balance_month_list, label = "Saldo do Mês")
                        
                        plt.legend()
                        plt.show() 
                        break 

                      

                    elif op_graph == '2':
                        print('\n')
                        print(green("Você escolheu 'Distribuição por categorias'",'bold'))
                        print('\n')
                        expenses_names = ['Renda', 'Habitação', 'Saúde', 'Impostos', 'Auto', 'Pesssoal','Dependentes','Lazer','Investimentos'] 
                        categoric_graphic()
                        #data = [23, 17, 35, 29, 12, 41, 33, 11, 99] 
                        plt.bar(expenses_names,categories_by_month,color='green')
                        plt.xticks(expenses_names)
                        plt.ylabel('CATEGORIAS')
                        plt.xlabel('VALORES EM R$')
                        plt.title('DISTRIBUIÇÃO DE ENTRADAS E SAÍDAS FINANCEIRAS DURANTE O ANO')
                        plt.show()
                        
                        break
                    else:
                        print('\n')
                        print(green('Digite uma opção válida!','bold'))
                        time.sleep(3)

                
               
            elif option_final == '2':
                print(green('Vamos ver a lista de todos os dados inseridos...','bold')) 
                time.sleep(3)
                return 0
            elif option_final=='3':
                sys.exit()
            elif option_final=='4':
                return 2
            else:
                print(green('Insira uma opção válida!','bold')) 
                time.sleep(3)


#eliminates the data entered so that the user can make a new list
def reset_function():
    os.system('cls')
    print(green('Vamos resetar todos os dados armazenados...','bold'))
    income_sum_list.clear()
    spending_sum_list.clear()  
    balance_month_list.clear() 
    categories_by_month.clear()

    for clear_list in expenses_months.values():
       clear_list.clear()

    for clear_list in values_months.values():
       clear_list.clear()

    time.sleep(3)
    print(green('Vamos reiniciar...','bold'))
    time.sleep(3)


#individually classifies entries according to category, as per the "inputs" dictionary
def categoric_graphic():
    
    val_1=0
    val_2=0
    val_3=0
    val_4=0
    val_5=0
    val_6=0
    val_7=0
    val_8=0
    for month in official_month:
        for gr in inputs.keys():        
          for exp in inputs[gr]:
              for index,user in enumerate(expenses_months[month]):
                if user==exp:  
                    match gr:
                        
                        case 'Habitação':
                                val_1=val_1+values_months[month][index]
                            
                        case 'Saúde':
                                val_2=val_2+values_months[month][index]
                             
                        case 'Impostos':
                                val_3=val_3+values_months[month][index]
                               
                        case 'Auto':
                                val_4=val_4+values_months[month][index]
                                
                        case 'Pessoal':
                                val_5=val_5+values_months[month][index]
                              
                        case 'Dependentes':
                                val_6=val_6+values_months[month][index]
                               
                        case 'Lazer':
                                val_7=val_7+values_months[month][index]
                               
                        case 'Investimentos':
                                val_8=val_8+values_months[month][index]
                            

    

    categories_by_month.append(final_total_income)            
    categories_by_month.append(val_1)
    categories_by_month.append(val_2)
    categories_by_month.append(val_3)
    categories_by_month.append(val_4)
    categories_by_month.append(val_5)
    categories_by_month.append(val_6)
    categories_by_month.append(val_7)
    categories_by_month.append(val_8)

    try:
        if type(categories_by_month[9]) is float or int:
            del categories_by_month[9]
    except:
        print()
                
              

    

   
   


    
    #print("The bold text is",'\033[1m' + 'Python' + '\033[0m')

#function to format the sampling of months for the user
def print_month_name(month_in):
    match month_in:
        case 'JAN':
            month_out='JANEIRO'
        case 'FEV':
            month_out='FEVEREIRO'
        case 'MAR':
             month_out='MARÇO'
        case 'ABR':
             month_out='ABRIL'
        case 'MAI':
             month_out='MAIO'
        case 'JUN':
             month_out='JUNHO'
        case 'JUL':
             month_out='JULHO'
        case 'AGO':
             month_out='AGOSTO'
        case 'SET':
             month_out='SETEMBRO'
        case 'OUT':
             month_out='OUTUBRO'
        case 'NOV':
             month_out='NOVEMBRO'
        case 'DEZ':
             month_out='DEZEMBRO'
    return month_out

#function that allows the user to insert or not more values
def user_options():
    while True:
        os.system('cls')
        print('\n')
        print(magenta('Deseja inserir mais valores?','bold'))
        more_values=input(magenta('Insira [s]im ou [n]ao: ','bold'))

        if more_values.lower().startswith('s'):
            print(green('Você escolheu inserir mais valores...','bold'))
            time.sleep(3)
            return 1
        if more_values.lower().startswith('n'):
            print(green('Você finalizou a inserção de valores...','bold'))
            time.sleep(3)
            return 0


        else:
            print(green('Insira [s]im ou [n]ao!','bold'))
            time.sleep(3)
            continue
        

#main code
while True:
    #stage for receiving values
    print_or_not=1
    return_groupe,return_name,return_value,return_month=menu()
    if return_value=='error':
        continue

    parameters_receive(return_groupe,return_name,return_value,return_month)
    
    for mo in official_month:
        if mo=='JAN':
            trasfer_increment_month=0
        else:
            trasfer_increment_month+=1
    
        transfer_income_sum,transfer_spending_sum=result_prints(mo,print_or_not)
    
    op_continue=user_options()
    
    if op_continue==1:
        
        continue

    else:
        print_or_not=1
    
    #from here the results are shown
    for mo in official_month:
        if mo=='JAN':
            trasfer_increment_month=0
        else:
            trasfer_increment_month+=1
        
        transfer_income_sum,transfer_spending_sum=result_prints(mo,print_or_not)
        extra_calculations(transfer_income_sum,transfer_spending_sum,trasfer_increment_month)
    
    #code for calling the final menu
    while True:
        print_or_not=final_menu() 

        if print_or_not==2:
            reset_function()
            
            break


        for mo in official_month:
            if mo=='JAN':
                trasfer_increment_month=0
            else:
                trasfer_increment_month+=1
            
            transfer_income_sum,transfer_spending_sum=result_prints(mo,print_or_not)
        
    

        



     
    