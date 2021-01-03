import  pandas as pd
import itertools
#import nltk, re, pprint
pd.set_option('display.max_columns', None)
import os 
#function to check the value is integer or not 
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
def reset():
    c1=''
    c1_in=''
    c1_or=''

    c1_th=''
    c1_tw=''
    c2=''
    c2_in=''

    c2_or=''
    c2_th=''
    c2_tw=''
    c3=''

    c3_in=''
    c3_or=''
    c3_th=''
    c3_tw=''

    c4=''
    c4_in=''
    c4_or=''
    c4_th=''

    c4_tw=''
    c5=''
    c5_or=''
    c5_tw=''

    cgpi=''
    college_code=''
    department=''

    elective=''
    exam_held_on=''
    page_no=''

    result=''
    result_date=''

    seat_no=''
    sem_1=''
    sem_2=''

    sem_3=''
    sem_4=''
    sem_5=''

    sem_6=''
    sem_7=''
    sem_8=''

    university=''

    
    
#function to convert text into dataframe 
def tex_df(txt,df):
    #predifining all required variable strings
    dip = '(DIPLOMA'
    s1 = 'SEM-I:'
    s2 = 'SEM-II:'
    s3 = 'SEM-III:'
    s4 = 'SEM-IV:'
    s5 = 'SEM-V:'
    s6 = 'SEM-VI:'
    s7 = 'SEM-VII:'
    cg = 'CGPI:'
    elect = '(ELECTIVE:'           

    # input file name from parameter
    input_text = open(txt, 'r')
    line_split = [line.split(" ") for line in input_text.readlines()]
    #spliting a line in text based on spaces 
    prefixes = ('@','#','RLE','RR','RCC','RPV','ADC','ABS','*') 
    for x in line_split:
        for word in x[:]:
            if word.startswith(prefixes):
                x.remove(word)
        
            while '' in x:
                x.remove('')
    line_split = list(filter((['\n']).__ne__, line_split))
    #print(line_split)

    #looping through each line of text file 
    for i in range(len(line_split)):
        #print(line_split[i])
        #identifiying key strings in file like ('UNIVERSITY', 'OF', 'MUMBAI', '\n) is head of for each page 
        if  line_split[i]== ['UNIVERSITY', 'OF', 'MUMBAI', '\n']:
            #reset()
            #print(i)
            university = ' '.join(line_split[i])
            page_no = line_split[i+1][2]
            department = [line_split[i+2][k:j+1] for k in range(len(line_split[i+2])) 
                          if line_split[i+2][k][0] == '(' for j in range(len(line_split[i+2]))  
                          if  line_split[i+2][j][-1] == ')'][0]
            #result_sem = line_split[i+2][8]
            exam_held_on = line_split[i+2][-3]+' '+line_split[i+2][-2]
            college_code = line_split[i+3][1:-7]
            result_date = line_split[i+3][5]+' '+line_split[i+3][6]+' '+line_split[i+3][7]
            #print(result_date)
        if line_split[i] ==['------------------------------------------------------------------------------------------------------------------------------------------------------', '\n'] and line_split[i+1][0] == '1.':
                new_i = i
                #print(i)
                c1 = [line_split[new_i+1][j+1] for j  in range(len(line_split[new_i+1])) 
                      if line_split[new_i+1][j] == '1.' ]
                c2 = [line_split[new_i+1][j+1] for j  in range(len(line_split[new_i+1])) 
                      if line_split[new_i+1][j] == '2.' ]
                c3 = [line_split[new_i+1][j+1] for j  in range(len(line_split[new_i+1])) 
                      if line_split[new_i+1][j] == '3.' ]
                c4 = [line_split[new_i+2][j+1] for j  in range(len(line_split[new_i+2])) 
                      if line_split[new_i+2][j] == '4.' ]
                c5 = [line_split[new_i+2][j+1] for j  in range(len(line_split[new_i+2])) 
                      if line_split[new_i+2][j] == '5.' ]
                c6 = [line_split[new_i+2][j+1] for j  in range(len(line_split[new_i+2])) 
                      if line_split[new_i+2][j] == '6.' ]
               # print(c6)



        if line_split[i] == ['------------------------------------------------------------------------------------------------------------------------------------------------------', '\n'] and len(line_split[i+1][0]) > 5 and RepresentsInt(line_split[i+1][0]):
                new = i
                #print(line_split[new+6])
                sem_1 = (([line_split[new+6][idx][6:]+line_split[new+6][idx+1] 
                           for idx in range(len(line_split[new+6])) if line_split[new+6][idx][0:6] == s1]) or
                          (   ['Diploma' for idx in range(len(line_split[new+6])) 
                               if line_split[new+6][idx][0:9] == dip] ) ) 
                sem_2 = (([line_split[new+6][idx][7:]+line_split[new+6][idx+1] 
                           for idx in range(len(line_split[new+6])) if line_split[new+6][idx][0:7] == s2] )or
                             (['Diploma' for idx in range(len(line_split[new+6])) 
                               if line_split[new+6][idx][0:9] == dip]))
                sem_3 = [line_split[new+6][idx][8:]+line_split[new+6][idx+1] 
                         for idx in range(len(line_split[new+6])) if line_split[new+6][idx][0:8] == s3]
                sem_4 = [line_split[new+6][idx][7:]+line_split[new+6][idx+1] 
                         for idx in range(len(line_split[new+6])) if line_split[new+6][idx][0:7] == s4]
                sem_5 = [line_split[new+6][idx][6:]+line_split[new+6][idx+1] 
                         for idx in range(len(line_split[new+6])) if line_split[new+6][idx][0:6] == s5]
                sem_6 = [line_split[new+6][idx][7:]+line_split[new+6][idx+1] 
                         for idx in range(len(line_split[new+6])) if line_split[new+6][idx][0:7] == s6]
                sem_7 = [line_split[new+6][idx][8:]+line_split[new+6][idx+1] 
                         for idx in range(len(line_split[new+6])) if line_split[new+6][idx][0:8] == s7]
                cgpi = [line_split[new+6][idx][5:]+line_split[new+6][idx+1] 
                        for idx in range(len(line_split[new+6])) if line_split[new+6][idx][0:5] == cg]
                sem_8 = line_split[new+5][-2]    
                #print(sem_8)
                seat_no = line_split[new+1][0]
                elective = [line_split[new+1][idx][10:17]+line_split[new+1][idx+1] 
                            for idx in range(len(line_split[new+1])) if line_split[new+1][idx][0:10] == elect]
                result = line_split[new+3][10]

                c1_th = line_split[new+2][0]
                c1_tw = line_split[new+2][1]
                c2_th = line_split[new+2][2]
                c2_tw = line_split[new+2][3]
                c3_th = line_split[new+2][4]
                c3_tw = line_split[new+2][5]
                c4_th = line_split[new+2][6]
                c4_tw = line_split[new+2][7]
                c5_tw = line_split[new+2][8]
                c6_tw = line_split[new+2][9]

                c1_in = line_split[new+3][0]
                c1_or = line_split[new+3][1]
                c2_in = line_split[new+3][2]
                c2_or = line_split[new+3][3]
                c3_in = line_split[new+3][4]
                c3_or = line_split[new+3][5]
                c4_in = line_split[new+3][6]
                c4_or = line_split[new+3][7]
                c5_or = line_split[new+3][8]
                c6_or = line_split[new+3][9]

                df_1 = {    0:i,      'c1': c1 ,   'c1_in': c1_in,        'c1_or': c1_or,
                              'c1_th': c1_th ,     'c1_tw': c1_tw,        'c2': c2,              'c2_in':c2_in ,
                              'c2_or': c2_or ,     'c2_th': c2_th,        'c2_tw': c2_tw,        'c3': c3,
                              'c3_in': c3_in,      'c3_or': c3_or,        'c3_th':c3_th ,        'c3_tw': c3_tw ,
                              'c4':c4 ,            'c4_in':c4_in,         'c4_or':c4_or ,        'c4_th': c4_th,
                              'c4_tw': c4_tw,      'c5': c5,              'c5_or': c5_or,        'c5_tw': c5_tw,
                              'cgpi':cgpi ,        'college_code':college_code ,    'department':department ,
                              'elective': elective,'exam_held_on': exam_held_on,    'page_no': page_no ,    
                              'result': result,    'result_date': result_date,      
                              'seat_no': seat_no,        'sem_1':sem_1 ,        'sem_2': sem_2,
                              'sem_3': sem_3,            'sem_4': sem_4,        'sem_5':sem_5 ,
                              'sem_6': sem_6,            'sem_7': sem_7,        'sem_8':sem_8 , 
                              'university':university
                       }
                df = df.append(df_1,ignore_index=True)
                #print(df.tail(10))

        #df.to_csv('final.csv',mode='a', header=True,index=False)
        #print(df.tail(25)) 




                
        if line_split[i] == ['-------------------------------------------------------------------------------------------------------------------------------------------------', '\n'] and line_split[i+1][0] == '1.':
                new_i = i
                #print(i)
                c1 = [line_split[new_i+1][j+1] for j  in range(len(line_split[new_i+1])) 
                      if line_split[new_i+1][j] == '1.' ]
                c2 = [line_split[new_i+1][j+1] for j  in range(len(line_split[new_i+1])) 
                      if line_split[new_i+1][j] == '2.' ]
                c3 = [line_split[new_i+1][j+1] for j  in range(len(line_split[new_i+1])) 
                      if line_split[new_i+1][j] == '3.' ]
                c4 = [line_split[new_i+2][j+1] for j  in range(len(line_split[new_i+2])) 
                      if line_split[new_i+2][j] == '4.' ]
                c5 = [line_split[new_i+2][j+1] for j  in range(len(line_split[new_i+2])) 
                      if line_split[new_i+2][j] == '5.' ]
                
               # print(c5)



        if line_split[i] == ['-------------------------------------------------------------------------------------------------------------------------------------------------', '\n'] and len(line_split[i+1][0]) > 5 and RepresentsInt(line_split[i+1][0]):
                new = i
                #print(line_split[new+6])
                sem_1 = (([line_split[new+6][idx][6:]+line_split[new+6][idx+1] 
                           for idx in range(len(line_split[new+6])) if line_split[new+6][idx][0:6] == s1]) or
                          (   ['Diploma' for idx in range(len(line_split[new+6])) 
                               if line_split[new+6][idx][0:9] == dip] ) ) 
                sem_2 = (([line_split[new+6][idx][7:]+line_split[new+6][idx+1] 
                           for idx in range(len(line_split[new+6])) if line_split[new+6][idx][0:7] == s2] )or
                             (['Diploma' for idx in range(len(line_split[new+6])) 
                               if line_split[new+6][idx][0:9] == dip]))
                sem_3 = [line_split[new+6][idx][8:]+line_split[new+6][idx+1] 
                         for idx in range(len(line_split[new+6])) if line_split[new+6][idx][0:8] == s3]
                sem_4 = [line_split[new+6][idx][7:]+line_split[new+6][idx+1] 
                         for idx in range(len(line_split[new+6])) if line_split[new+6][idx][0:7] == s4]
                sem_5 = [line_split[new+6][idx][6:]+line_split[new+6][idx+1]
                         for idx in range(len(line_split[new+6])) if line_split[new+6][idx][0:6] == s5]
                sem_6 = [line_split[new+6][idx][7:]+line_split[new+6][idx+1] 
                         for idx in range(len(line_split[new+6])) if line_split[new+6][idx][0:7] == s6]
                sem_7 = [line_split[new+6][idx][8:]+line_split[new+6][idx+1] 
                         for idx in range(len(line_split[new+6])) if line_split[new+6][idx][0:8] == s7]
                cgpi = [line_split[new+6][idx][5:]+line_split[new+6][idx+1] 
                        for idx in range(len(line_split[new+6])) if line_split[new+6][idx][0:5] == cg]
                sem_8 = line_split[new+5][-2]    
               # print('c5')
                seat_no = line_split[new+1][0]
                elective = [line_split[new+1][idx][10:17]+line_split[new+1][idx+1] 
                            for idx in range(len(line_split[new+1])) if line_split[new+1][idx][0:10] == elect]
                result = line_split[new+3][-2]

                c1_th = line_split[new+2][0]
                c1_tw = line_split[new+2][1]
                c2_th = line_split[new+2][2]
                c2_tw = line_split[new+2][3]
                c3_th = line_split[new+2][4]
                c3_tw = line_split[new+2][5]
                c4_th = line_split[new+2][6]
                c4_tw = line_split[new+2][7]
                c5_tw = line_split[new+2][8]
                #c6_tw = line_split[new+2][9]

                c1_in = line_split[new+3][0]
                c1_or = line_split[new+3][1]
                c2_in = line_split[new+3][2]
                c2_or = line_split[new+3][3]
                c3_in = line_split[new+3][4]
                c3_or = line_split[new+3][5]
                c4_in = line_split[new+3][6]
                c4_or = line_split[new+3][7]
                c5_or = line_split[new+3][8]
                #c6_or = line_split[new+3][9]

                df_1 = {    0:i,      'c1': c1 ,   'c1_in': c1_in,        'c1_or': c1_or,
                              'c1_th': c1_th ,     'c1_tw': c1_tw,        'c2': c2,              'c2_in':c2_in ,
                              'c2_or': c2_or ,     'c2_th': c2_th,        'c2_tw': c2_tw,        'c3': c3,
                              'c3_in': c3_in,      'c3_or': c3_or,        'c3_th':c3_th ,        'c3_tw': c3_tw ,
                              'c4':c4 ,            'c4_in':c4_in,         'c4_or':c4_or ,        'c4_th': c4_th,
                              'c4_tw': c4_tw,      'c5': c5,              'c5_or': c5_or,        'c5_tw': c5_tw,
                              'cgpi':cgpi ,        'college_code':college_code ,    'department':department ,
                              'elective': elective,'exam_held_on': exam_held_on,    'page_no': page_no ,    
                              'result': result,    'result_date': result_date,      
                              'seat_no': seat_no,        'sem_1':sem_1 ,        'sem_2': sem_2,
                              'sem_3': sem_3,            'sem_4': sem_4,        'sem_5':sem_5 ,
                              'sem_6': sem_6,            'sem_7': sem_7,        'sem_8':sem_8 , 
                              'university':university
                       }
                df = df.append(df_1,ignore_index=True)
                
                #print(df['sem_1'].tail(10))
        #df.to_csv('final.csv',mode='a', header=True,index=False)
        #print(df.tail(10))
    return df        


# loop to go through all text files in given directory 
count = 0
done = 0
for file in os.listdir("./processed_txt/"):
    if file.endswith(".txt"):
        count = count + 1
for file in os.listdir("./processed_txt/"):
    if file.endswith(".txt"):
        print(file+' '+'Started Processing')
        #tex_df('./txt/'+file,df)
        df1 = pd.read_csv('./data/csv_db/final.csv',sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
        df = tex_df('./processed_txt/'+file,df1)
        df.to_csv('./data/csv_db/final.csv',mode='w',columns=['university','page_no','department','exam_held_on',
                                                'college_code','result_date','seat_no','elective',
                                                'result','c1','c2','c3','c4','c5','c6','c1_th','c1_tw',
                                                    'c1_or','c1_in','c2_th','c2_tw','c2_or','c2_in','c3_th',
                                                'c3_tw','c3_or','c3_in','c4_th','c4_tw','c4_or','c4_in',
                                                'c5_tw','c5_or','c6_tw','c6_or','sem_1','sem_2','sem_3',
                                                'sem_4','sem_5','sem_6','sem_7','sem_8','cgpi'], header=True,index=False)
        #tex_df('./txt/T10328.pdf.txt',df)
        #print(df.tail(40))
        print(file+' '+'Finished')
        done = done + 1
        print('Done: ' + str(done) + ' out of : ' + str(count) + ", left : " +str(count-done) )
     
      