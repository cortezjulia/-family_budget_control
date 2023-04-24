#PROJETO DE TABELA PARA CONTROLE DE ORÇAMENTO FAMILIAR

import os
import unicodedata
from simple_colors import *
import time
import matplotlib.pyplot
import sys
total_income=0
official_month=['JAN','FEV','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ']
income_sum_list=[]
spending_sum_list=[]
balance_month_list=[]

gastos = {
    'Renda': ['Salários','13º Salário','Férias','Renda extra','Alugueis','Juros de Investimento'],
    'Habitação': ['Prestação de compra','Aluguel','Água','IPTU','Luz','Telefone','TV por assinatura','Supermercado','Empregada','Reformas'],
    'Saúde': ['Plano de saúde','Médico','Dentista','Medicamentos','Seguro de vida'],
    'Imposto':['IRFF','INSS'],
    'Auto':['Prestação','Seguro','Combustível','Lavagens','IPVA','Mecânico','Multas'],
    'Pessoal':['Higiene pessoal','Cosméticos','Cabelereiro','Vestuário','Lavanderia','Academia','Unhas','Cursos'],
    'Dependentes':['Escola/Faculdade','Cursos Extras','Material escolar','Esportes/Uniformes','Mesada','Passeios/Férias','Vestuário','Saúde'],
    'Lazer':['Restaurantes','Livraria','Streamings','Passagens','Hotéis','Passeios'],
    'Investimentos':['Previdência','Aplicações']

}

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

    
def menu():
    os.system('cls')
    ind=0
    for key, value in gastos.items():
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


def str_accentuation_check(conv_str):
    str_converter = unicodedata.normalize("NFD", conv_str)
    str_converter = str_converter.encode("ascii", "ignore")
    str_converter = str_converter.decode("utf-8")
    str_converter=str_converter.lower()

    return str_converter
    
def expenses_comparation(expense_comparation,expense_groupe_comparation):
    flag1=False
    flag2=False

    expense_comparation=str_accentuation_check(expense_comparation)
    expense_groupe_comparation=str_accentuation_check(expense_groupe_comparation)
    expense_comparation=expense_comparation.lower()
    expense_groupe_comparation=expense_groupe_comparation.lower()

    
    for key,item in gastos.items():
       
       original_groupe=key
       key=str_accentuation_check(key)
       key=key.lower()

       if key==expense_groupe_comparation:
           flag1=True
           break

    for item in gastos[original_groupe]:
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
    
def result_prints(choose_month,pr_or_not):
    os.system('cls')
    sum_values=0.0
    different_color=0
    income_sum=0
    flag_income_sum=0
    spending_sum=0
    month_integer_name=print_month_name(choose_month)

    if pr_or_not==0:
        print('\n')
        print(green(f'----------{month_integer_name}----------','bold'))
        print('\n')

    for gr in gastos.keys():
        if pr_or_not==0:
            print('\n')    
            print(magenta(f'----------{gr}----------'))
            print('\n')

        for exp in gastos[gr]:
            sum_values=0.0
            for index,user in enumerate(expenses_months[choose_month]):
                
                if user==exp:
                    sum_values=sum_values+values_months[choose_month][index]
                    #print("\n",'\033[1m')
                    different_color=1
                    
                    if gr=='Renda':
                        income_sum=income_sum+sum_values
                        flag_income_sum=1
                    else:
                        spending_sum=spending_sum+sum_values
                        
                       
                        
            if pr_or_not==0:
                if different_color==0:
                    print(f'{exp} - {sum_values}')
                else:
                    print(magenta(f'{exp} - {sum_values}','bold'))
                    different_color=0
                #print("",'\033[0m')


      
          
    return flag_income_sum,income_sum,spending_sum
    
        
       
           
   

def extra_calculations(receive_flag_income_sum,receive_income_sum,receive_spending_sum,receive_increment_month):
    
    total_income=0.0
    total_spending=0.0
    accumulated_balance=0.0
    os.system('cls')

    #size_income_list=len(income_list)
    
    #if (receive_flag_income_sum==1):
     #   if size_income_list>1 and receive_income_sum!=income_list[size_income_list-1]:
      #     income_list.insert(receive_increment_month,receive_income_sum) 
           
           
       # elif size_income_list==1 and receive_income_sum!=income_list[0]:
        #   income_list.insert(receive_increment_month,receive_income_sum) 
           
           
      #  elif size_income_list==0:
       #    income_list.insert(receive_increment_month,receive_income_sum) 

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

def graphics_and_complete_lists():
        while True:
            
            print('\n')
            print('O que você deseja fazer?')
            print('Ver Gráficos com os dados gerados: [1]')
            print('Ver a lista completa dos dados inseridos: [2]')
            print('Sair: [3]')
            print('Reiniciar: [4]')
            option_final=input('Insira o número correspondente: ')    

            if option_final == '1':
                print('Vamos ver os gráficos obtidos...')      
                matplotlib.pyplot.plot(official_month, balance_month_list)   
                matplotlib.pyplot.show()  
                continue
            elif option_final == '2':
                print('Vamos ver a lista de todos os dados inseridos...') 
                return 0
            elif option_final=='3':
                sys.exit()
            elif option_final=='4':
                return 2
            else:
                print('Insira uma opção válida!') 

def reset_function():
    income_sum_list.clear()
    spending_sum_list.clear()  
    balance_month_list.clear() 

    for clear_list in expenses_months.values():
       clear_list.clear()

    for clear_list in values_months.values():
       clear_list.clear()
 
    print(values_months)
    print(expenses_months)

                
          

    

   
   


    
    #print("The bold text is",'\033[1m' + 'Python' + '\033[0m')

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
        


while True:
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
    
        transfer_flag_income_sum,transfer_income_sum,transfer_spending_sum=result_prints(mo,print_or_not)
    
    op_continue=user_options()
    
    if op_continue==1:
        
        continue
    else:
        print_or_not=1
    
    for mo in official_month:
        if mo=='JAN':
            trasfer_increment_month=0
        else:
            trasfer_increment_month+=1
        
        transfer_flag_income_sum,transfer_income_sum,transfer_spending_sum=result_prints(mo,print_or_not)
        extra_calculations(transfer_flag_income_sum,transfer_income_sum,transfer_spending_sum,trasfer_increment_month)
    

    while True:
        print_or_not=graphics_and_complete_lists() 

        if print_or_not==2:
            print('Vamos resetar todos os dados armazenados...')
            
            reset_function()
            time.sleep(5)
            break


        for mo in official_month:
            if mo=='JAN':
                trasfer_increment_month=0
            else:
                trasfer_increment_month+=1
            
            transfer_flag_income_sum,transfer_income_sum,transfer_spending_sum=result_prints(mo,print_or_not)
        
    

        



     
    