import pandas as pd
import numpy as np
import random
df =pd.read_excel('D:\output.xlsx')

counter_array =np.array([0]*16)

def choose_case(snr,):   # change it 

    tempCounter = np.split(counter_array,[6,12])
    counter1 =tempCounter[0]
    counter2 =tempCounter[1]
    counter3 =tempCounter[2]

    if(snr<50):
        min_index = counter1.argmin()+1
        return min_index
        

    
    if(snr >50 and snr <70):
         min_index = counter2.argmin()+1
         return min_index+6
         
    if(snr>70):
        min_index = counter3.argmin()+1
    return min_index+12



def  chose_data(caseNumber,row_number):

    counter_array[caseNumber-1]= counter_array[caseNumber-1]+1

    df.at[row_number,'opoznenie'] =random.random()*13
    df.at[row_number,'BER'] =random.random()*100
    df.at[row_number,'protokol'] = random.randint(0,1)
    df.at[row_number,'kable'] = random.randint(0,1)
    df.at[row_number,'bandwith'] = random.random()*4000
   


    match caseNumber:
        case 1:
            
            df.at[row_number,'opoznenie'] =random.random()*4
            df.at[row_number,'BER'] =random.random()*20
            df.at[row_number,'protokol'] =0
            df.at[row_number,'state'] =0

            if df.at[row_number,'protokol'] == 0 :
                df.at[row_number,'straty'] =0
            else:
                df.at[row_number,'straty'] =random.random()*100

            

        case 2:
            
            df.at[row_number,'opoznenie'] =random.random()*4
            df.at[row_number,'BER'] =random.random()*500
            df.at[row_number,'protokol'] = 1
            df.at[row_number,'state'] =1
            
            if df.at[row_number,'protokol'] == 0 :
                df.at[row_number,'straty'] =0
            else:
                df.at[row_number,'straty'] =random.random()*100


        case 3:
            df.at[row_number,'opoznenie'] =random.random()*4
            df.at[row_number,'BER'] = 20 + random.random()*80
            df.at[row_number,'state'] = 1
            
            if df.at[row_number,'protokol'] == 0 :
                df.at[row_number,'straty'] =0
            else:
                df.at[row_number,'straty'] =random.random()*100
            

        case 4:
            df.at[row_number,'opoznenie'] =4+random.random()*9
            df.at[row_number,'bandwith'] = 2000+random.random()*2000
            df.at[row_number,'state'] = 0
            
            
            if df.at[row_number,'protokol'] == 0 :
                df.at[row_number,'straty'] =0
            else:
                df.at[row_number,'straty'] =random.random()*100

        case 5:
            df.at[row_number,'opoznenie'] =4+random.random()*9
            df.at[row_number,'kable'] = 0
            df.at[row_number,'bandwith'] = random.random()*2000
            df.at[row_number,'state'] = 0

            if df.at[row_number,'protokol'] == 0 :
                df.at[row_number,'straty'] =0
            else:
                df.at[row_number,'straty'] =random.random()*100
            
            
        case 6:
            df.at[row_number,'opoznenie'] =4+random.random()*9
            df.at[row_number,'kable'] = 1
            df.at[row_number,'bandwith'] = random.random()*2000
            df.at[row_number,'state'] = 1

            if df.at[row_number,'protokol'] == 0 :
                df.at[row_number,'straty'] =0
            else:
                df.at[row_number,'straty'] =random.random()*100



        case 7:
            df.at[row_number,'bandwith'] = 1000+random.random()*3000
            df.at[row_number,'opoznenie'] =random.random()*5
            df.at[row_number,'protokol'] = 0
            df.at[row_number,'state'] =0

            if df.at[row_number,'protokol'] == 0 :
                df.at[row_number,'straty'] =0
            else:
                df.at[row_number,'straty'] =random.random()*100

        case 8:
            df.at[row_number,'bandwith'] = 1000+random.random()*3000
            df.at[row_number,'opoznenie'] =random.random()*5
            df.at[row_number,'protokol'] = 1
            df.at[row_number,'state'] =1

            if df.at[row_number,'protokol'] == 0 :
                df.at[row_number,'straty'] =0
            else:
                df.at[row_number,'straty'] =random.random()*100

        case 9:
            df.at[row_number,'bandwith'] = 1000+random.random()*3000
            df.at[row_number,'opoznenie'] = 5+random.random()*8
            df.at[row_number,'straty'] =random.random()*60
            

            if df.at[row_number,'protokol'] == 0 :
                df.at[row_number,'straty'] =0
                df.at[row_number,'state'] =1
            else:
                df.at[row_number,'straty'] =random.random()*60
                df.at[row_number,'state'] =1

        case 10:
            df.at[row_number,'bandwith'] = 1000+random.random()*3000
            df.at[row_number,'opoznenie'] =random.random()*5
            df.at[row_number,'straty'] =60+random.random()*40
            df.at[row_number,'protokol'] = 1
            df.at[row_number,'state'] =2

           

        case 11:
            df.at[row_number,'bandwith'] = random.random()*1000
            if df.at[row_number,'hopes'] <7 :
                df.at[row_number,'state'] =1
            else :   
                df.at[row_number,'state'] =2 

            if df.at[row_number,'protokol'] == 0 :
                df.at[row_number,'straty'] =0
            else:
                df.at[row_number,'straty'] =random.random()*100


        case 12:
            df.at[row_number,'bandwith'] = random.random()*1000
            if df.at[row_number,'hopes'] >6 :
                df.at[row_number,'state'] =2
            else :   
                df.at[row_number,'state'] = 1     
            
            if df.at[row_number,'protokol'] == 0 :
                df.at[row_number,'straty'] =0
            else:
                df.at[row_number,'straty'] =random.random()*100

        case 13:
            df.at[row_number,'BER'] =random.random()*500
            df.at[row_number,'opoznenie'] =random.random()*7
            df.at[row_number,'kable'] = 0
            df.at[row_number,'state'] =1

            if df.at[row_number,'protokol'] == 0 :
                df.at[row_number,'straty'] =0
            else:
                df.at[row_number,'straty'] =random.random()*100

        case 14:
            df.at[row_number,'BER'] =random.random()*500
            df.at[row_number,'opoznenie'] =random.random()*7
            df.at[row_number,'kable'] = 1
            df.at[row_number,'state'] =2
            
            if df.at[row_number,'protokol'] == 0 :
                df.at[row_number,'straty'] =0
            else:
                df.at[row_number,'straty'] =random.random()*100

        case 15:
            df.at[row_number,'BER'] =random.random()*500
            df.at[row_number,'opoznenie'] =7+random.random()*6
            df.at[row_number,'state'] =2
            
            if df.at[row_number,'protokol'] == 0 :
                df.at[row_number,'straty'] =0
            else:
                df.at[row_number,'straty'] =random.random()*100

        case 16:
            df.at[row_number,'BER'] = 500+random.random()*1000
            df.at[row_number,'opoznenie'] =7+random.random()*6
            df.at[row_number,'state'] =2
            
            if df.at[row_number,'protokol'] == 0 :
                df.at[row_number,'straty'] =0
            else:
                df.at[row_number,'straty'] =random.random()*100             


for i in range(462):
    l = choose_case(df.at[i,'snr'])
    chose_data(l,i)

df.to_excel("D:/predict100.xlsx")
##df.to_excel("predict100.xlsx")
print('git')

'''''   
k1=0
k2=0
k3=0
for i in range(462):
    if df.at[i,'snr'] <50:
        k1 =k1+1
    elif df.at[i,'snr'] <70 and df.at[i,'snr'] >50:
        k2 =k2 +1
    else :
        k3=k3 +1

print(k1)
print(k2)
print(k3)'''
