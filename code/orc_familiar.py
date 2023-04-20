#PROJETO DE TABELA PARA CONTROLE DE ORÇAMENTO FAMILIAR

import os
import unicodedata
import sys



official_month=['JAN','FEV','MAR','ABR','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ']

list_income=[0,0,0,0,0,0,0,0]
list_month_income=['-','-','-','-','-','-','-','-']

list_housing=[0,0,0,0,0,0,0,0,0,0]
list_month_housing=['-','-','-','-','-','-','-','-','-','-']

list_health=[0,0,0,0,0,0,0,0]
list_month_health=['-','-','-','-','-','-','-','-']

list_tax=[0,0,0,0,0,0,0,0]
list_month_tax=['-','-','-','-','-','-','-','-']

list_car=[0,0,0,0,0,0,0,0]
list_month_car=['-','-','-','-','-','-','-','-']

list_personal=[0,0,0,0,0,0,0,0]
list_month_personal=['-','-','-','-','-','-','-','-']

list_dependent=[0,0,0,0,0,0,0,0]
list_month_dependent=['-','-','-','-','-','-','-','-']

list_leisure=[0,0,0,0,0,0]
list_month_leisure=['-','-','-','-','-','-']

list_investment=[0,0,0]
list_month_investment=['-','-','-']





gastos = {
    'Renda': ['Salários','13º Salário','Férias','Renda extra','Alugueis','Juros de Investimento'],
    'Habitação': ['Prestação de compra','Aluguel','Água','IPTU','Luz','Telefone','TV por assinatura','Supermercado','Empregada','Reformas'],
    'Saúde': ['Plano de saúde','Médico','Dentista','Medicamentos','Seguro de vida'],
    'Imposto':['IRFF','INSS'],
    'Auto':['Prestação','Seguro','Combustível','Lavagens','IPVA','Mecânico','Multas'],
    'Pessoal':['Higiene pessoal','Cosméticos','Cabelereiro','Vestuário','Lavanderia','Academia','Unhas','Cursos'],
    'Depententes':['Escola/Faculdade','Cursos Extras','Material escolar','Esportes/Uniformes','Mesada','Passeios/Férias','Vestuário','Saúde'],
    'Lazer':['Restaurantes','Livraria','Streamings','Passagens','Hotéis','Passeios'],
    'Investimentos':['Previdência','Aplicações']

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
        print('***O GASTO INSERIDO NÃO CORRESPONDE A NENHUM GASTO CADASTRADO***')
        return 
    if (final_month)=='nulo':
        print('***O MÊS INSERIDO NÃO CORRESPONDE A NENHUM MÊS CADASTRADO***')
        return 



    test_list,test_list_month=choose_list(final_groupe)

    for index,var in enumerate(gastos[final_groupe]):
        
       
        if var== final_expense:

            stored_value=test_list[index]
            test_list.insert(index,(value+stored_value))
            test_list.pop(index+1)
            test_list_month.insert(index,final_month)
            test_list_month.pop(index+1)
       
        
    print(*test_list)
    print(*test_list_month)
   



def menu():
    ind=0
    for key, value in gastos.items():
        print(f'----------{key}----------')
        print('\n')
        print(*value,sep='\n')
        print('\n')

    user_groupe=input('Insira o gasto geral: ')
    user_name=input('Insira o gasto específico: ')
    user_value=(input('Insira o valor: '))
    user_month=input('Insira o mês: ')

    try:
        user_value=float(user_value)
    except:
        print('***INSIRA APENAS NÚMEROS PARA O VALOR***')
        user_value='error'

    return user_groupe,user_name,user_value,user_month

def choose_list(choose_groupe):

    match choose_groupe:
        case 'Renda':
            return list_income,list_month_income
        case 'Habitação':
            return list_housing,list_month_housing
        case 'Saúde':
            return list_health,list_month_health
        case  'Imposto':
            return list_tax,list_month_tax
        case  'Auto':
            return list_car,list_month_car
        case 'Pessoal':
            return list_personal,list_month_personal
        case 'Depententes':
            return list_dependent,list_month_dependent
        case 'Lazer':
            return list_leisure,list_month_leisure
        case 'Investimentos':
            return list_investment,list_month_investment

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
    
    



    



while True:
    
    return_groupe,return_name,return_value,return_month=menu()
    if return_value=='error':
        continue

    parameters_receive(return_groupe,return_name,return_value,return_month)
    #os.system('cls') 
