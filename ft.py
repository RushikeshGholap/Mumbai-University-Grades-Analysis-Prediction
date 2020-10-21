import urllib.error


def about():
    import streamlit as st
    
    
    
    st.markdown(
        """ <p style="color:red">
         <b>Note</b> - Change the parameters on left menu and if its not present hit on arrow at top left , you will get a menubar.
        If your using mobile device then you might require to hit arrow frequently as it gets hidden due to  diplay size is small.
        For best experience use Desktop 
        </p>


        """,unsafe_allow_html=True

    )

    st.sidebar.success("Select from Menu 👆 ")

   

# Turn off black formatting for this function to present the user with more
# compact code.
# fmt: off
def prediction():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import pickle
    from sklearn.linear_model import LinearRegression
    import plotly.graph_objects as go
    import statistics 
    import plotly.express as px 





    diploma = st.sidebar.checkbox("Diploma Student/Direct 2nd year", False)

   
    
    
    
    
    st.markdown(
        """ <p style="color:red">
         <b>Note</b> - Change the parameters on left menu and if its not present hit on arrow at top left , you will get a menubar.
        If your using mobile device then you might require to hit arrow frequently as it gets hidden due to  diplay size is small.
        For best experience use Desktop 
        </p>


        """,unsafe_allow_html=True

    )
    st.sidebar.success("Enter the semwise Pointers  👇 ")
    
    if diploma:
        counter = pd.read_csv("./csv_db/counter.csv")
        mean_df = pd.read_csv('./csv_db/mean_df_dip.csv')
        max_df = pd.read_csv('./csv_db/max_df_dip.csv')
        min_df = pd.read_csv('./csv_db/min_df_dip.csv')

        dip_template = pd.read_csv('./csv_db/Diploma_template.csv')
        
        infile = open('regression_model_diploma','rb')
        regression_model_diploma = pickle.load(infile)
        infile.close()

        college_code_list = mean_df['college_code'].unique()
        sub_college = st.sidebar.selectbox(
            "Choose College Code ", list(college_code_list))
        dep_list = mean_df[mean_df['college_code']==sub_college]['department'].unique()
        sub_dep = st.sidebar.selectbox(
            "Choose Department", list(dep_list))

        diff = 0 
        sem_1 = None
        sem_2 = None
        sem_8 = None
        cgpi = None
        sem_3 = st.sidebar.number_input("Sem 3",value =  float(min(10,float((mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)]['sem_3']+diff).round(2)))),min_value=float(0),max_value=float(10))   
        diff = sem_3-float((mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)]['sem_3']).round(2))
        sem_4 = st.sidebar.number_input("Sem 4",value =  float(min(10,float((mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)]['sem_4']+diff).round(2)))),min_value=float(0),max_value=float(10))
        diff = sem_4-float((mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)]['sem_4']).round(2))
        sem_5 = st.sidebar.number_input("Sem 5",value =  float(min(10,float((mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)]['sem_5']+diff).round(2)))),min_value=float(0),max_value=float(10))
        diff = sem_5-float((mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)]['sem_5']).round(2))
        sem_6 = st.sidebar.number_input("Sem 6",value =  float(min(10,float((mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)]['sem_6']+diff).round(2)))),min_value=float(0),max_value=float(10))
        diff = sem_6-float((mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)]['sem_6']).round(2))
        sem_7 = st.sidebar.number_input("Sem 7",value =  float(min(10,float((mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)]['sem_7']+diff).round(2)))),min_value=float(0),max_value=float(10))
        
              
        college_code = 'college_code_'+str(sub_college)
        dep = 'department_'+str(sub_dep)
        df_1 = { college_code:1 ,    dep:1 , 
                               
                                'sem_3': sem_3,            'sem_4': sem_4,        'sem_5':sem_5 ,
                                'sem_6': sem_6,            'sem_7': sem_7 }
        
        
        pred = dip_template.append(df_1,ignore_index=True)
        pred.fillna(0,inplace= True )
        
        
        mean_college = [sem_1,sem_2]
        max_college = [sem_1,sem_2]
        min_college = [sem_1,sem_2]
        for x in ['sem_3','sem_4','sem_5','sem_6','sem_7','sem_8','cgpi']:

            mean_college.append(float(mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)][x]))
            max_college.append(float(max_df[(max_df['college_code']==sub_college) & (max_df['department']==sub_dep)][x]))
            min_college.append(float(min_df[(min_df['college_code']==sub_college) & (min_df['department']==sub_dep)][x]))
            
        st.write("<b> College selected : <i  style ='color:#3366ff'>%s</i> </b> " % sub_college, unsafe_allow_html=True)
        st.write(" <b> Deparment selected : <i style ='color:#3366ff'>%s</i> </b>"%sub_dep, unsafe_allow_html=True)
        st.write("<b><i>Entered Pointers 👇</i></b>",unsafe_allow_html = True)
        st.write("<b>SEM III : <i style='color:#3366ff'>%4.2f</i> | SEM IV : <i style='color:#3366ff'>%4.2f</i> | SEM V : <i style='color:#3366ff'>%4.2f</i> | SEM VI : <i style='color:#3366ff'>%4.2f</i> | SEM VII : <i style='color:#3366ff'>%4.2f</i> </b>"%(sem_3,sem_4,sem_5,sem_6,sem_7),unsafe_allow_html=True)
        if st.button('Predict'):
            sem_8 = float(regression_model_diploma.predict(pred[-1:]))
            cgpi = statistics.mean([sem_8,sem_3,sem_4,sem_5,sem_6,sem_7])
            st.write(" <b > The predicted pointers for SEM VIII : <i style ='color:#0047b3' >%4.2f</i></b> "%sem_8, unsafe_allow_html=True)
            st.write(" <b >The predicted CGPI : <i style ='color:#0047b3'>%4.2f</i> </b>"%cgpi, unsafe_allow_html=True)
            row = { 'college_code':sub_college ,    'dep':sub_dep , 
                                'sem_1':sem_1 ,        'sem_2': sem_2,
                                'sem_3': sem_3,            'sem_4': sem_4,        'sem_5':sem_5 ,
                                'sem_6': sem_6,            'sem_7': sem_7 , 'sem_8':sem_8, 'cgpi':cgpi , 'type':'Diploma'}
            counter = counter.append(row,ignore_index =True)
            counter.to_csv('counter.csv',index=False)
        
    else:
        counter = pd.read_csv("./csv_db/counter.csv")
        mean_df = pd.read_csv('./csv_db/mean_df.csv')
        max_df = pd.read_csv('./csv_db/max_df.csv')
        min_df = pd.read_csv('./csv_db/min_df.csv')
        template = pd.read_csv('./csv_db/template.csv')


        college_code_list = mean_df['college_code'].unique()
        sub_college = st.sidebar.selectbox(
            "Choose College Code ", list(college_code_list))
        dep_list = mean_df[mean_df['college_code']==sub_college]['department'].unique()
        sub_dep = st.sidebar.selectbox(
            "Choose Department", list(dep_list))


        infile = open('regression_model_regular','rb')
        regression_model_regular = pickle.load(infile)
        infile.close()
              
        sem_8 = None
        cgpi = None
        diff = 0 
        sem_1 = st.sidebar.number_input("Sem 1",value =  float(min(10,float((mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)]['sem_1']+diff).round(2)))),min_value=float(0),max_value=float(10))
        diff = sem_1-float((mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)]['sem_1']).round(2))
        sem_2 = st.sidebar.number_input("Sem 2",value =  float(min(10,float((mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)]['sem_2']+diff).round(2)))),min_value=float(0),max_value=float(10))
        diff = sem_2-float((mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)]['sem_2']).round(2))
        sem_3 = st.sidebar.number_input("Sem 3",value =  float(min(10,float((mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)]['sem_3']+diff).round(2)))),min_value=float(0),max_value=float(10))   
        diff = sem_3-float((mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)]['sem_3']).round(2))
        sem_4 = st.sidebar.number_input("Sem 4",value =  float(min(10,float((mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)]['sem_4']+diff).round(2)))),min_value=float(0),max_value=float(10))
        diff = sem_4-float((mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)]['sem_4']).round(2))
        sem_5 = st.sidebar.number_input("Sem 5",value =  float(min(10,float((mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)]['sem_5']+diff).round(2)))),min_value=float(0),max_value=float(10))
        diff = sem_5-float((mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)]['sem_5']).round(2))
        sem_6 = st.sidebar.number_input("Sem 6",value =  float(min(10,float((mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)]['sem_6']+diff).round(2)))),min_value=float(0),max_value=float(10))
        diff = sem_6-float((mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)]['sem_6']).round(2))
        sem_7 = st.sidebar.number_input("Sem 7",value =  float(min(10,float((mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)]['sem_7']+diff).round(2)))),min_value=float(0),max_value=float(10))
        mean_college = []
        max_college = []
        min_college = []
        for x in ['sem_1','sem_2','sem_3','sem_4','sem_5','sem_6','sem_7','sem_8','cgpi']:
            
            mean_college.append(float(mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)][x]))
            max_college.append(float(max_df[(max_df['college_code']==sub_college) & (max_df['department']==sub_dep)][x]))
            min_college.append(float(min_df[(min_df['college_code']==sub_college) & (min_df['department']==sub_dep)][x]))


    

        college_code = 'college_code_'+str(sub_college)
        dep = 'department_'+str(sub_dep)
        df_1 = { college_code:1 ,    dep:1 , 
                                'sem_1':sem_1 ,        'sem_2': sem_2,
                                'sem_3': sem_3,            'sem_4': sem_4,        'sem_5':sem_5 ,
                                'sem_6': sem_6,            'sem_7': sem_7 }
        
        
        pred = template.append(df_1,ignore_index=True)
        pred.fillna(0,inplace= True )
        
        st.write("<b> College selected : <i  style ='color:#3366ff'>%s</i> </b> " % sub_college, unsafe_allow_html=True)
        st.write(" <b> Deparment selected : <i style ='color:#3366ff'>%s</i> </b>"%sub_dep, unsafe_allow_html=True)
        st.write("<b><i>Entered Pointers 👇</i></b>",unsafe_allow_html = True)
        st.write("<b>SEM I : <i style='color:#3366ff'>%4.2f</i> | SEM II : <i style='color:#3366ff'>%4.2f</i> | SEM III : <i style='color:#3366ff'>%4.2f</i> | SEM IV : <i style='color:#3366ff'>%4.2f</i> | SEM V : <i style='color:#3366ff'>%4.2f</i> | SEM VI : <i style='color:#3366ff'>%4.2f</i> | SEM VII : <i style='color:#3366ff'>%4.2f</i> </b>"%(sem_1,sem_2,sem_3,sem_4,sem_5,sem_6,sem_7),unsafe_allow_html=True)
        
        if st.button('Predict'):
            sem_8 = float(regression_model_regular.predict(pred[-1:]))
            cgpi = statistics.mean([sem_8,sem_1,sem_2,sem_3,sem_4,sem_5,sem_6,sem_7])
            st.write(" <b > The predicted pointers for SEM VIII : <i style ='color:#0047b3' >%4.2f</i></b> "%sem_8, unsafe_allow_html=True)
            st.write(" <b >The predicted CGPI : <i style ='color:#0047b3'>%4.2f</i> </b>"%cgpi, unsafe_allow_html=True)
            row = { 'college_code':sub_college ,    'dep':sub_dep , 
                                'sem_1':sem_1 ,        'sem_2': sem_2,
                                'sem_3': sem_3,            'sem_4': sem_4,        'sem_5':sem_5 ,
                                'sem_6': sem_6,            'sem_7': sem_7 , 'sem_8':sem_8, 'cgpi':cgpi , 'type':'Regular'}
            counter = counter.append(row,ignore_index =True)
            counter.to_csv('counter.csv',index=False)
            
    
            

    # Add data
    sem = ["SEM I","SEM II","SEM III","SEM IV","SEM V","SEM VI","SEM VII","SEM VIII","CGPI"]            
    predicted = [sem_1,sem_2,sem_3,sem_4,sem_5,sem_6,sem_7,sem_8,cgpi]
   
    fig = go.Figure()
    # Create and style traces
    fig.add_trace(go.Scatter(x=sem, y=max_college, name='Max of College',
                            line=dict(color='firebrick', width=4)))
    fig.add_trace(go.Scatter(x=sem, y=mean_college, name='Average of College',
                            line=dict(color='royalblue', width=4)))
    fig.add_trace(go.Scatter(x=sem, y=min_college, name = 'Min of College',
                            line=dict(color='red', width=4)))
    fig.add_trace(go.Scatter(x=sem, y=predicted, name='Current/Predicted',
                            line=dict(color='green', width=4,
                                dash='dash'),connectgaps=False ))

    # Edit the layout
    fig.update_layout(title='Performance per Semisters ',
                        xaxis_title='Semisters ',
                    yaxis_title='Pointers',height=550)
    fig.update_yaxes(tickvals=[0,1,2,3,4,5,6,7,8,9,10])
    st.plotly_chart(fig)

   
    st.write(" <b >Predictions performed Counter: <i style ='color:red'>%.0f</i> </b>"%counter.shape[0], unsafe_allow_html=True)
    df = counter['type'].value_counts().rename_axis('Type').reset_index(name='Counts')


    fig_1 = px.bar(df,x='Counts',y ='Type',barmode='stack',orientation='h',height=250,text='Counts',color="Type",title='Category wise predicted counts')
    fig_1.update_traces(texttemplate='%{text}',textposition='outside')
    st.plotly_chart(fig_1)



def analysis():
    import streamlit as st
    import streamlit as st
    import pandas as pd
    import numpy as np
    import pickle
    import plotly.graph_objects as go
    import plotly.express as px 

    mean_df = pd.read_csv('./csv_db/mean_df.csv')
    max_df = pd.read_csv('./csv_db/max_df.csv')
    min_df = pd.read_csv('./csv_db/min_df.csv')
    
    anl_sel = st.sidebar.radio("Select what insights you want to see and compare",('Internal Vs External Gradings','Regular Vs Diploma Students',
                                'Oral/Viva Vs Theory Exam','Best & Worst college Rankings','Consistent college Ranking','Top ellective Subjects',
                                'Ellected Subject & performance','Department Wise performance','Student Friendly college Rankings'))
                                
    if anl_sel == 'Internal Vs External Gradings':
        dip_sel = st.checkbox('Diploma Student/Direct 2nd year',False)
            
        if dip_sel:
            mean_df = pd.read_csv('./csv_db/mean_df_dip.csv')
            max_df = pd.read_csv('./csv_db/max_df_dip.csv')
            min_df = pd.read_csv('./csv_db/min_df_dip.csv')
            sem_1,sem_2 = None,None
        college_code_list = mean_df['college_code'].unique()
        mul_coll = st.multiselect("Choose Multiple Colleges / CollegeCodes to compare", list(college_code_list),default=['124:MGMCET','126:SAKEC','174:RAIT','17:BVCE'])
        lis= []
        for x in mul_coll:
            lis.append(mean_df[mean_df['college_code']==x]['department'].unique())
        if len(mul_coll)!= 0:
            com_dept = list(set.intersection(*map(set,lis )))
            sub_dep = st.selectbox("Choose Common Departments based on selected colleges to compare ", list(com_dept))
        cal_sub = st.radio("Select metric to compute",
                            ('Average',  'Max','Min'))
        fig = go.Figure()
        for sub_college in mul_coll:    
            mean_college = []
            max_college = []
            min_college = []
            if dip_sel:
                sem_list = ['sem_3','sem_4','sem_5','sem_6','sem_7','sem_8','cgpi']
                sem = ["SEM III","SEM IV","SEM V","SEM VI","SEM VII","SEM VIII","CGPI"]
            else : 
                sem_list  = ['sem_1','sem_2','sem_3','sem_4','sem_5','sem_6','sem_7','sem_8','cgpi']
                sem = ["SEM I","SEM II","SEM III","SEM IV","SEM V","SEM VI","SEM VII","SEM VIII","CGPI"]
            for x in sem_list:

                    if cal_sub == 'Average':
                        mean_college.append(float(mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)][x]))               
                    if cal_sub == 'Max':
                        max_college.append(float(max_df[(max_df['college_code']==sub_college) & (max_df['department']==sub_dep)][x]))
                    if cal_sub == 'Min':
                        min_college.append(float(min_df[(min_df['college_code']==sub_college) & (min_df['department']==sub_dep)][x]))
            
            
            # Add scatter trace for line
            fig.add_trace(go.Scatter(x=sem, y=max_college, name= sub_college +' Max',
                                    line=dict( width=4)))
            fig.add_trace(go.Scatter(x=sem, y=mean_college, name= sub_college + ' Average',
                                    line=dict( width=4)))
            fig.add_trace(go.Scatter(x=sem, y=min_college, name = sub_college + ' Min',
                                    line=dict( width=4)))

            if dip_sel == False:
                                
                fig.update_layout(
                    shapes=[
                        # 1st highlight
                        dict(
                            type="rect",
                            # x-reference is assigned to the x-values
                            xref="x",
                            # y-reference is assigned to the plot paper [0,1]
                            yref="paper",
                            x0="SEM I",
                            y0=0,
                            x1="SEM III",
                            y1=1,
                            fillcolor="mediumspringgreen",
                            opacity=0.6,
                            layer="below",
                            line_width=0,
                        ),
                        # 2nd highlight
                        dict(
                            type="rect",
                            xref="x",
                            yref="paper",
                            x0="SEM III",
                            y0=0,
                            x1="SEM VI",
                            y1=1,
                            fillcolor="LIGHTSALMON",
                            opacity=0.7,
                            layer="below",
                            line_width=0,
                        ),
                        # 3rd highlight 
                        dict(
                            type="rect",
                            xref="x",
                            yref="paper",
                            x0="SEM VI",
                            y0=0,
                            x1="SEM VIII",
                            y1=1,
                            fillcolor="mediumspringgreen",
                            opacity=0.6,
                            layer="below",
                            line_width=0,
                        )
                    ]
                )
            else : 
                 fig.update_layout(
                    shapes=[
                        # 2nd highlight
                        dict(
                            type="rect",
                            xref="x",
                            yref="paper",
                            x0="SEM III",
                            y0=0,
                            x1="SEM VI",
                            y1=1,
                            fillcolor="LIGHTSALMON",
                            opacity=0.7,
                            layer="below",
                            line_width=0,
                        ),
                        # 3rd highlight 
                        dict(
                            type="rect",
                            xref="x",
                            yref="paper",
                            x0="SEM VI",
                            y0=0,
                            x1="SEM VIII",
                            y1=1,
                            fillcolor="mediumspringgreen",
                            opacity=0.6,
                            layer="below",
                            line_width=0,
                        )
                    ]
                )
        st.write('<b>The background color determines who is incharge of your results</b>',unsafe_allow_html=True)
        st.write('<b><i style="color:mediumspringgreen"> External Checking</i></b> or <b><i style = "color:LIGHTSALMON"> Internal Checking </i></b>',unsafe_allow_html=True)
        st.plotly_chart(fig)
    if anl_sel == 'Regular Vs Diploma Students' :   
        mean_df_d = pd.read_csv('./csv_db/mean_df_dip.csv')
        max_df_d = pd.read_csv('./csv_db/max_df_dip.csv')
        min_df_d = pd.read_csv('./csv_db/min_df_dip.csv')
        mean_df_r = pd.read_csv('./csv_db/mean_df.csv')
        max_df_r = pd.read_csv('./csv_db/max_df.csv')
        min_df_r = pd.read_csv('./csv_db/min_df.csv')
        
        
        college_code_list = mean_df_d['college_code'].unique()
        sub_college = st.selectbox("Choose College / CollegeCode to compare", list(college_code_list))
        com_dept = (mean_df_d[mean_df_d['college_code']==sub_college]['department'].unique())
        sub_dep = st.selectbox("Choose Department based on selected college to compare ", list(com_dept))

        mean_college_d = [None,None]
        max_college_d = [None,None]
        min_college_d = [None,None]
        mean_college_r = []
        max_college_r = []
        min_college_r = []
        sem_list_d = ['sem_3','sem_4','sem_5','sem_6','sem_7','sem_8','cgpi']
       # sem = ["SEM III","SEM IV","SEM V","SEM VI","SEM VII","SEM VIII","CGPI"]
        sem_list_r = ['sem_1','sem_2','sem_3','sem_4','sem_5','sem_6','sem_7','sem_8','cgpi']
        sem = ["SEM I","SEM II","SEM III","SEM IV","SEM V","SEM VI","SEM VII","SEM VIII","CGPI"]

        cal_sub = st.radio("Select metric to compute",
                            ('Average',  'Max','Min'))
        for x in sem_list_r:

                if cal_sub == 'Average':
                    mean_college_r.append(float(mean_df_r[(mean_df_r['college_code']==sub_college) & (mean_df_r['department']==sub_dep)][x]))               
                if cal_sub == 'Max':
                    max_college_r.append(float(max_df_r[(max_df_r['college_code']==sub_college) & (max_df_r['department']==sub_dep)][x]))
                if cal_sub == 'Min':
                    min_college_r.append(float(min_df_r[(min_df_r['college_code']==sub_college) & (min_df_r['department']==sub_dep)][x]))
        for x in sem_list_d:

                if cal_sub == 'Average':
                    mean_college_d.append(float(mean_df_d[(mean_df_d['college_code']==sub_college) & (mean_df_d['department']==sub_dep)][x]))               
                if cal_sub == 'Max':
                    max_college_d.append(float(max_df_d[(max_df_d['college_code']==sub_college) & (max_df_d['department']==sub_dep)][x]))
                if cal_sub == 'Min':
                    min_college_d.append(float(min_df_d[(min_df_d['college_code']==sub_college) & (min_df_d['department']==sub_dep)][x]))
        
        fig = go.Figure()
        # Add scatter trace for line
        if cal_sub == 'Max':

            fig.add_trace(go.Scatter(x=sem, y=max_college_r, name= 'Regular Max',
                                line=dict( width=4)))
            fig.add_trace(go.Scatter(x=sem, y=max_college_d, name= 'Diploma Max',
                                line=dict( width=4)))
        if cal_sub == 'Average':

            fig.add_trace(go.Scatter(x=sem, y=mean_college_r, name=  'Regular Average',
                                    line=dict( width=4)))
            fig.add_trace(go.Scatter(x=sem, y=mean_college_d, name= 'Diploma Average',
                                    line=dict( width=4)))
            
        if cal_sub == 'Min':
            fig.add_trace(go.Scatter(x=sem, y=min_college_r, name =  'Regular Min',
                                line=dict( width=4)))
            fig.add_trace(go.Scatter(x=sem, y=min_college_d, name =  'Diploma Min',
                                line=dict( width=4)))


        fig.update_layout(
                shapes=[
                    # 2nd highlight
                    dict(
                        type="rect",
                        xref="x",
                        yref="paper",
                        x0="SEM III",
                        y0=0,
                        x1="SEM VI",
                        y1=1,
                        fillcolor="LIGHTSALMON",
                        opacity=0.7,
                        layer="below",
                        line_width=0,
                    ),
                    # 3rd highlight 
                    dict(
                        type="rect",
                        xref="x",
                        yref="paper",
                        x0="SEM VI",
                        y0=0,
                        x1="SEM VIII",
                        y1=1,
                        fillcolor="mediumspringgreen",
                        opacity=0.6,
                        layer="below",
                        line_width=0,
                    )
                ]
            )
        st.write('<b>The background color determines who is incharge of your results</b>',unsafe_allow_html=True)
        st.write('<b><i style="color:mediumspringgreen"> External Checking</i></b> or <b><i style = "color:LIGHTSALMON"> Internal Checking </i></b>',unsafe_allow_html=True)
        st.plotly_chart(fig)
    if anl_sel == 'Oral/Viva Vs Theory Exam':
        dip_sel = st.checkbox('Diploma Student/Direct 2nd year',False)
            
        if dip_sel:
            mean_df = pd.read_csv('./csv_db/mean_df_dip.csv')
            max_df = pd.read_csv('./csv_db/max_df_dip.csv')
            min_df = pd.read_csv('./csv_db/min_df_dip.csv')
            sem_1,sem_2 = None,None
        college_code_list = mean_df['college_code'].unique()
        mul_coll = st.multiselect("Choose Multiple Colleges / CollegeCodes to compare", list(college_code_list),default=['124:MGMCET','126:SAKEC','174:RAIT','17:BVCE'])
        lis= []
        for x in mul_coll:
            lis.append(mean_df[mean_df['college_code']==x]['department'].unique())
        if len(mul_coll)!= 0:
            com_dept = list(set.intersection(*map(set,lis )))
            sub_dep = st.selectbox("Choose Common Departments based on selected colleges to compare ", list(com_dept))
        cal_sub = st.radio("Select metric to compute",
                            ('Average',  'Max','Min'))
        sel_sub = st.radio("Select Oral/Internal to compare",
                            ('Term Work(TW)','Oral(OR)','Internal Grading(IN)'))
        fig = go.Figure()
        for sub_college in mul_coll:    # to loop through the selected colleges 
            tw_mean = []
            th_mean = []
            in_mean = []
            or_mean = []
            tw_max = []
            th_max = []
            in_max = []
            or_max = []
            tw_min= []
            th_min = []
            in_min = []
            or_min = []
            
            sem_list = ['c1_th','c1_tw','c1_or','c1_in','c2_th','c2_tw','c2_in','c3_th','c3_tw','c3_in','c3_or','c4_th','c4_tw','c4_in']
            x_label = ["Course I","Course II","Course III","Course IV"]
    
            if cal_sub == 'Average':
                for x in ['c1_th','c2_th','c3_th','c4_th']:
                    th_mean.append(float(mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)][x]))
                if sel_sub == 'Oral(OR)':
                    for x in ['c1_or' ,'c3_or' ]:
                        or_mean.append(float(mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)][x]))
                if sel_sub == 'Term Work(TW)' :
                    for x in ['c1_tw','c2_tw','c3_tw','c4_tw']:
                        tw_mean.append(float(mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)][x]))
                if sel_sub =='Internal Grading(IN)' :
                    for x in ['c1_in','c2_in','c3_in','c4_in']:
                        in_mean.append(float(mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)][x]))                   
            if cal_sub == 'Max':
                for x in ['c1_th','c2_th','c3_th','c4_th']:
                    th_max.append(float(max_df[(max_df['college_code']==sub_college) & (max_df['department']==sub_dep)][x]))
                if sel_sub == 'Oral(OR)':
                    for x in ['c1_or' ,'c3_or' ]:
                        or_max.append(float(max_df[(max_df['college_code']==sub_college) & (max_df['department']==sub_dep)][x]))
                if sel_sub == 'Term Work(TW)' :
                    for x in ['c1_tw','c2_tw','c3_tw','c4_tw']:
                        tw_max.append(float(max_df[(max_df['college_code']==sub_college) & (max_df['department']==sub_dep)][x]))
                if sel_sub =='Internal Grading(IN)' :
                    for x in ['c1_in','c2_in','c3_in','c4_in']:
                        in_max.append(float(max_df[(max_df['college_code']==sub_college) & (max_df['department']==sub_dep)][x]))   
            if cal_sub == 'Min':
                for x in ['c1_th','c2_th','c3_th','c4_th']:
                    th_min.append(float(min_df[(min_df['college_code']==sub_college) & (min_df['department']==sub_dep)][x]))
                if sel_sub == 'Oral(OR)':
                    for x in ['c1_or' ,'c3_or' ]:
                        or_min.append(float(min_df[(min_df['college_code']==sub_college) & (min_df['department']==sub_dep)][x]))
                if sel_sub == 'Term Work(TW)' :
                    for x in ['c1_tw','c2_tw','c3_tw','c4_tw']:
                        tw_min.append(float(min_df[(min_df['college_code']==sub_college) & (min_df['department']==sub_dep)][x]))
                if sel_sub =='Internal Grading(IN)' :
                    for x in ['c1_in','c2_in','c3_in','c4_in']:
                        in_min.append(float(min_df[(min_df['college_code']==sub_college) & (min_df['department']==sub_dep)][x]))   
    
            
            # Add scatter trace for line
            fig.add_trace(go.Scatter(x=x_label, y=th_max, name= 'TH'+sub_college [:3] +' Max',
                                    line=dict( width=4)))
            fig.add_trace(go.Scatter(x=x_label, y=tw_max, name= 'TW'+sub_college [:3] +' Max',
                                    line=dict( width=4)))
            fig.add_trace(go.Scatter(x=x_label, y=or_max, name= 'OR'+sub_college [:3] +' Max',
                                    line=dict( width=4)))
            fig.add_trace(go.Scatter(x=x_label, y=in_max, name= 'IN'+sub_college [:3] +' Max',
                                    line=dict( width=4)))  
            
                                    
            fig.add_trace(go.Scatter(x=x_label, y=th_mean, name= 'TH '+sub_college [:3] +' Average',
                                    line=dict( width=4)))
            fig.add_trace(go.Scatter(x=x_label, y=tw_mean, name= 'TW '+sub_college [:3] +' Average',
                                    line=dict( width=4)))
            fig.add_trace(go.Scatter(x=x_label, y=or_mean, name= 'OR '+sub_college [:3] +' Average',
                                    line=dict( width=4)))
            fig.add_trace(go.Scatter(x=x_label, y=in_mean, name= 'IN '+sub_college [:3] +' Average',
                                    line=dict( width=4)))
                                    
            fig.add_trace(go.Scatter(x=x_label, y=th_min, name= 'TH '+sub_college [:3] +' Min',
                                    line=dict( width=4)))
            fig.add_trace(go.Scatter(x=x_label, y=tw_min, name= 'TW '+sub_college [:3] +' Min',
                                    line=dict( width=4)))
            fig.add_trace(go.Scatter(x=x_label, y=or_min, name= 'OR '+sub_college [:3] +' Min',
                                    line=dict( width=4)))
            fig.add_trace(go.Scatter(x=x_label, y=in_min, name= 'IN'+sub_college [:3] +' Min',
                                    line=dict( width=4)))
            
            if dip_sel == False:
                                
                fig.update_layout(
                    shapes=[
                        # 1st highlight
                        dict(
                            type="rect",
                            # x-reference is assigned to the x-values
                            xref="x",
                            # y-reference is assigned to the plot paper [0,1]
                            yref="paper",
                            x0="SEM I",
                            y0=0,
                            x1="SEM III",
                            y1=1,
                            fillcolor="mediumspringgreen",
                            opacity=0.6,
                            layer="below",
                            line_width=0,
                        ),
                        # 2nd highlight
                        dict(
                            type="rect",
                            xref="x",
                            yref="paper",
                            x0="SEM III",
                            y0=0,
                            x1="SEM VI",
                            y1=1,
                            fillcolor="LIGHTSALMON",
                            opacity=0.7,
                            layer="below",
                            line_width=0,
                        ),
                        # 3rd highlight 
                        dict(
                            type="rect",
                            xref="x",
                            yref="paper",
                            x0="SEM VI",
                            y0=0,
                            x1="SEM VIII",
                            y1=1,
                            fillcolor="mediumspringgreen",
                            opacity=0.6,
                            layer="below",
                            line_width=0,
                        )
                    ]
                )
            else : 
                 fig.update_layout(
                    shapes=[
                        # 2nd highlight
                        dict(
                            type="rect",
                            xref="x",
                            yref="paper",
                            x0="SEM III",
                            y0=0,
                            x1="SEM VI",
                            y1=1,
                            fillcolor="LIGHTSALMON",
                            opacity=0.7,
                            layer="below",
                            line_width=0,
                        ),
                        # 3rd highlight 
                        dict(
                            type="rect",
                            xref="x",
                            yref="paper",
                            x0="SEM VI",
                            y0=0,
                            x1="SEM VIII",
                            y1=1,
                            fillcolor="mediumspringgreen",
                            opacity=0.6,
                            layer="below",
                            line_width=0,
                        )
                    ]
                )
        st.write('<b>The background color determines who is incharge of your results</b>',unsafe_allow_html=True)
        st.write('<b><i style="color:mediumspringgreen"> External Checking</i></b> or <b><i style = "color:LIGHTSALMON"> Internal Checking </i></b>',unsafe_allow_html=True)
        st.plotly_chart(fig)




def contribute():
    import streamlit as st
    import time
    import numpy as np


    st.markdown(
        """
        This is Contribute    
        """
    )
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")


# fmt: on

# Turn off black formatting for this function to present the user with more
# compact code.
# fmt: off
def suggestion():
    import streamlit as st
    st.markdown(
        """
        This is suggestion    
        """
    )
def working():
    import streamlit as st
    st.markdown(
        """
        This is how it works    
        """
    )
    st.write('done')