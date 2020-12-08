
def about():
    import streamlit as st
    
    
    
    st.markdown(
        """ <p style="color:red">
         <b>Note</b> - Change the left menu parameters, and if it's not present, hit on the arrow at the top left, you will get a menubar.
         If you are using a mobile device, then you might require to hit the arrow frequently as it gets hidden due to the small display size.
         For the best experience,<b> use Desktop.</b> 
        </p>


        """,unsafe_allow_html=True

    )
    st.markdown(
        """ <p ><b><h3>About me ?</h3></b>
       I am an enthusiastic Data Scientist who is always looking for a solution that makes a difference. 
       I am working on independent projects that help society. 
       While doing so, I am exploring and learning the required skills and knowledge. 
       I have Graduated from Mumbai University.
        </p>


        """,unsafe_allow_html=True

    )
    
    st.markdown(
        """ <p ><b><h3> Why this Mumbai University Engineering Project ?</h3></b>
         <b> Mumbai University </b> is one of the well-known universities in India and has the most graduating students per year.
         Still, there is no well-recognized platform/website that helps students compare colleges based on grades. And this creates a major pit-fall for students.
         They won't know what their grades would be and are they good enough to compete with others during the job search.
         Good grades do not guarantee a job, but it'll certainly a ticket to an interview.
        </p>


        """,unsafe_allow_html=True

    )
    st.markdown(
        """ <p ><b><h3>Challenges Faced ?</h3></b>
        I have worked on many data science projects, but most of them are learning/simplified to understand the concepts well. 
        Here you don't have data as readily available. You need to -<br><b>
        ➸ Source data <br>
        ➸ Transform data into a structure <br>
        ➸ Preprocess data <br>
        ➸ EDA <br>
        ➸ Modeling <br>
        ➸ Deployment <br>
        ➸ Maintenance <br> </b>
        While learning from any educational platform, such key aspects may be missing. 
        This project is one of those where you are challenged and asked to push over your boundaries when you're new at it.
        </p>


        """,unsafe_allow_html=True

    )
    #st.video('abc')

    st.sidebar.success("Select from Menu above ")

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
         <b>Note</b> - Change the left menu parameters, and if it's not present, hit on the arrow at the top left, you will get a menubar.
         If you are using a mobile device, then you might require to hit the arrow frequently as it gets hidden due to the small display size.
         For the best experience,<b> use Desktop.</b> 
        </p>


        """,unsafe_allow_html=True

    )
    st.sidebar.success("Enter the semwise Pointers  👇 ")
    
    if diploma:
        counter = pd.read_csv("./csv_db/counter.csv")#file that keeps count of prediction data
        mean_df = pd.read_csv('./csv_db/mean_df_dip.csv')#file consist mean of diploma data
        max_df = pd.read_csv('./csv_db/max_df_dip.csv')#file consist max of diploma data
        min_df = pd.read_csv('./csv_db/min_df_dip.csv')#file consist min of diploma data

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
        st.write(" <b> Department selected : <i style ='color:#3366ff'>%s</i> </b>"%sub_dep, unsafe_allow_html=True)
        if diploma:
            st.write("<b> <i style ='color:#3366ff'>Diploma Selected</i> </b>", unsafe_allow_html=True)
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
            counter.to_csv('./csv_db/counter.csv',index=False)
        
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
        st.write(" <b> Department selected : <i style ='color:#3366ff'>%s</i> </b>"%sub_dep, unsafe_allow_html=True)
        st.write("<b><i>Entered Pointers 👇</i></b>",unsafe_allow_html = True)
        st.write("<b>SEM I : <i style='color:#3366ff'>%4.2f</i> | SEM II : <i style='color:#3366ff'>%4.2f</i> | SEM III : <i style='color:#3366ff'>%4.2f</i> | SEM IV : <i style='color:#3366ff'>%4.2f</i> | SEM V : <i style='color:#3366ff'>%4.2f</i> | SEM VI : <i style='color:#3366ff'>%4.2f</i> | SEM VII : <i style='color:#3366ff'>%4.2f</i> </b>"%(sem_1,sem_2,sem_3,sem_4,sem_5,sem_6,sem_7),unsafe_allow_html=True)
        counts = ''
        if st.button('Predict'):
            sem_8 = float(regression_model_regular.predict(pred[-1:]))
            counts = 'of ID : '+str(counter.shape[0]+1)
            cgpi = statistics.mean([sem_8,sem_1,sem_2,sem_3,sem_4,sem_5,sem_6,sem_7])
            st.write(" <b > The predicted pointers for SEM VIII : <i style ='color:#0047b3' >%4.2f</i></b> "%sem_8, unsafe_allow_html=True)
            st.write(" <b >The predicted CGPI : <i style ='color:#0047b3'>%4.2f</i> </b>"%cgpi, unsafe_allow_html=True)
            row = { 'college_code':sub_college ,    'dep':sub_dep , 
                                'sem_1':sem_1 ,        'sem_2': sem_2,
                                'sem_3': sem_3,            'sem_4': sem_4,        'sem_5':sem_5 ,
                                'sem_6': sem_6,            'sem_7': sem_7 , 'sem_8':sem_8, 'cgpi':cgpi , 'type':'Regular'}
            counter = counter.append(row,ignore_index =True)
            counter.to_csv('./csv_db/counter.csv',index=False)
            
    
            

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
    fig.update_layout(title='Performance per Semesters '+counts,title_x=0.425,
                        xaxis_title='Semesters ',
                    yaxis_title='Pointers',height=550)
    fig.update_yaxes(tickvals=[0,1,2,3,4,5,6,7,8,9,10])
    st.plotly_chart(fig)
    st.write("The prediction above can be within the range of ±0.5 given the conditions are ideal as before. Consider these predictions as the current rate of scoring and adjust your performance according to score desire cgpi.")
   
    st.write(" <b >Predictions performed Counter: <i style ='color:red'>%.0f</i> </b>"%counter.shape[0], unsafe_allow_html=True)
    df = counter['type'].value_counts().rename_axis('Type').reset_index(name='Counts')


    fig_1 = px.bar(df,x='Counts',y ='Type',barmode='stack',orientation='h',height=250,text='Counts',color="Type",title='Category wise predicted counts')
    fig_1.update(layout=dict(title=dict(x=0.5)))
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
    st.markdown(
        """ <p style="color:red">
         <b>Note</b> - Change the left menu parameters, and if it's not present, hit on the arrow at the top left, you will get a menubar.
         If you are using a mobile device, then you might require to hit the arrow frequently as it gets hidden due to the small display size.
         For the best experience,<b> use Desktop.</b> 
        </p>


        """,unsafe_allow_html=True

    )

    mean_df = pd.read_csv('./csv_db/mean_df.csv')
    max_df = pd.read_csv('./csv_db/max_df.csv')
    min_df = pd.read_csv('./csv_db/min_df.csv')
    
    anl_sel = st.sidebar.radio("Select what insights you want to see and compare",('Internal Vs External Gradings','Regular Vs Diploma Students',
                                'Oral/Viva Vs Theory Exam','Best college Rankings','Consistent college Ranking','Top Elective Subjects',
                                'Elected Subject & performance','Department Wise performance'))
                                
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
        cal_sub = st.radio("Select a metric to compute",
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
                            x0=0,
                            y0=0,
                            x1=1.5,
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
                            x0=1.5,
                            y0=0,
                            x1=5.5,
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
                            x0=5.5,
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
                            x1=3.5,
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
                            x0=3.5,
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
        if dip_sel:
            fig.update_layout(title='Dip. '+ cal_sub+' Performance Comparison between Internal VS. External checking ',title_x=0.425,
                        xaxis_title='Semesters ',
                    yaxis_title='Pointers',height=550)
        else:
            fig.update_layout(title=cal_sub+' Performance Comparison between Internal VS. External checking ',title_x=0.425,
                        xaxis_title='Semesters ',
                    yaxis_title='Pointers',height=550)
        st.write('<b>The background color determines where your examination papers are checked.</b>',unsafe_allow_html=True)
        st.write('<b><i style="color:mediumspringgreen"> External Checking</i></b> and <b><i style = "color:LIGHTSALMON"> Internal Checking </i></b>',unsafe_allow_html=True)
        st.plotly_chart(fig)
        st.write("Look in the orange part. If grades are dipping compared to in the green part, then select college is suppressing your grades. If the inverse is observed, then college is overvaluing the grades. If grades are consistent throughout (without any sudden dips or hikes) graph, then it's a good college.")
           
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

        cal_sub = st.radio("Select a metric to compute",
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
        fig.update_layout(title='Comparison between Regular VS. Diploma students ('+cal_sub+')',title_x=0.425,
                        xaxis_title='Semesters ',
                    yaxis_title='Pointers',height=550)
        fig.update_layout(
                    shapes=[
                        # 1st highlight
                        dict(
                            type="rect",
                            # x-reference is assigned to the x-values
                            xref="x",
                            # y-reference is assigned to the plot paper [0,1]
                            yref="paper",
                            x0=0,
                            y0=0,
                            x1=1.5,
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
                            x0=1.5,
                            y0=0,
                            x1=5.5,
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
                            x0=5.5,
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
        st.write('<b>The background color determines where your examination papers are checked.</b>',unsafe_allow_html=True)
        st.write('<b><i style="color:mediumspringgreen"> External Checking</i></b> and <b><i style = "color:LIGHTSALMON"> Internal Checking </i></b>',unsafe_allow_html=True)
        st.plotly_chart(fig)
        st.write("<p>Watch out for diploma vs. regular students;<br>if diploma students are having the upper hand, then selected college is a better choice for new admission for diploma students.</p>",unsafe_allow_html=True)

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
        cal_sub = st.radio("Select a metric to compute",
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
                                    mode='markers'))
            fig.add_trace(go.Scatter(x=x_label, y=tw_max, name= 'TW'+sub_college [:3] +' Max',
                                    mode='markers'))
            fig.add_trace(go.Scatter(x=x_label, y=or_max, name= 'OR'+sub_college [:3] +' Max',
                                    mode='markers'))
            fig.add_trace(go.Scatter(x=x_label, y=in_max, name= 'IN'+sub_college [:3] +' Max',
                                    mode='markers'))  
            
                                    
            fig.add_trace(go.Scatter(x=x_label, y=th_mean, name= 'TH '+sub_college [:3] +' Average',
                                    mode='markers')) 
            fig.add_trace(go.Scatter(x=x_label, y=tw_mean, name= 'TW '+sub_college [:3] +' Average',
                                    mode='markers')) 
            fig.add_trace(go.Scatter(x=x_label, y=or_mean, name= 'OR '+sub_college [:3] +' Average',
                                    mode='markers')) 
            fig.add_trace(go.Scatter(x=x_label, y=in_mean, name= 'IN '+sub_college [:3] +' Average',
                                    mode='markers')) 
                                    
            fig.add_trace(go.Scatter(x=x_label, y=th_min, name= 'TH '+sub_college [:3] +' Min',
                                    mode='markers')) 
            fig.add_trace(go.Scatter(x=x_label, y=tw_min, name= 'TW '+sub_college [:3] +' Min',
                                    mode='markers')) 
            fig.add_trace(go.Scatter(x=x_label, y=or_min, name= 'OR '+sub_college [:3] +' Min',
                                    mode='markers')) 
            fig.add_trace(go.Scatter(x=x_label, y=in_min, name= 'IN'+sub_college [:3] +' Min',
                                    mode='markers')) 
        if dip_sel:
                cal_sub = "Dip. " + cal_sub
        fig.update_layout(title= cal_sub + " "+sel_sub[:-4] + ' Vs '+ cal_sub +' Theory Exam',title_x=0.42,
                        xaxis_title='Courses',
                    yaxis_title='Marks Obtained',height=550)
        st.plotly_chart(fig)
        st.write('Look for students of the college with High internal grades and Low theory grades. Such colleges are gems and should be recommended for new admission. If the exact opposite is observed, then colleges are suppressing your ability to score. Such colleges should be avoided.')
    
    if anl_sel == 'Best college Rankings':
        dip_sel = st.checkbox('Diploma Student/Direct 2nd year',False)
        mean_df = pd.read_csv('./csv_db/mean_df.csv')   
        if dip_sel:
            mean_df = pd.read_csv('./csv_db/mean_df_dip.csv')
        import plotly.graph_objects as go
        import pandas as pd

        df_pre = mean_df.groupby(['college_code']).mean().round(2)
        df_pre.reset_index(inplace=True)
        df_pre.sort_values(by=['cgpi'], inplace=True, ascending=False) 
        df_pre['rank']=df_pre['cgpi'].rank(ascending = 0).astype(int)
        df_pre.set_index('rank',inplace=True)
        #st.write(df_pre[['college_code','cgpi']])
        if dip_sel:
            fig = go.Figure(data=[go.Table(
        header=dict(values=list(['Dip. Rank','College','CGPI']),
            fill_color='paleturquoise',
            align='left'),
        cells=dict(values=[df_pre.index, df_pre.college_code, df_pre.cgpi],
            fill_color='lightcyan',
            align='left'))
        ])
        else:
            fig = go.Figure(data=[go.Table(
        header=dict(values=list(['Rank','College','CGPI']),
            fill_color='paleturquoise',
            align='left'),
        cells=dict(values=[df_pre.index, df_pre.college_code, df_pre.cgpi],
            fill_color='lavender',
            align='left'))
        ])
        
        st.plotly_chart(fig)
        st.write("The rankings are based on the mean grades of student's scores. This ranking should not mislead you with the facilities, teaching, campus, staff behavior, placements, etc., of any particular college, based on rankings.")


        dep_pre = mean_df.groupby(['college_code','department']).mean().round(2)
        dep_pre.reset_index(inplace=True)
        
        




        st.write('According to departments/streams')


        department_list = mean_df['department'].unique()
       
        sub_dep = st.selectbox("Choose department/stream to see ranking ", list(department_list))
        dep_pre=dep_pre[dep_pre['department']==sub_dep][['college_code','department','cgpi']]
        dep_pre.sort_values(by=['cgpi'], inplace=True, ascending=False)
        dep_pre['rank']=dep_pre['cgpi'].rank(ascending = 0).astype(int)
        dep_pre.set_index('rank',inplace=True)
        



        
        if dip_sel:
            fig = go.Figure(data=[go.Table(
        header=dict(values=list(['Dip. Rank','College','Department','CGPI']),
            fill_color='paleturquoise',
            align='left'),
        cells=dict(values=[dep_pre.index,dep_pre.college_code, dep_pre.department , dep_pre.cgpi],
            fill_color='lightcyan',
            align='left'))  
        ])
        else:
            fig = go.Figure(data=[go.Table(
        header=dict(values=list(['Rank','College','Department','CGPI']),
            fill_color='paleturquoise',
            align='left'),
        cells=dict(values=[dep_pre.index,dep_pre.college_code, dep_pre.department , dep_pre.cgpi],
            fill_color='lavender',
            align='left'))
        ])

        st.plotly_chart(fig)
        st.write('Segregated department wise rankings follow the same caveats')

    if anl_sel == 'Consistent college Ranking':
        import statistics
        import plotly.graph_objects as go
        import pandas as pd
        
        mean_df = pd.read_csv('./csv_db/mean_df.csv')
        
        mean_df['stddev']=1
        for index,x in mean_df.iterrows():
            mean_df['stddev'][index]=statistics.mean([x.sem_1,x.sem_2,x.sem_3,x.sem_4,x.sem_5,x.sem_6,x.sem_7,x.sem_8])
        mean_df = mean_df.groupby(['college_code']).std()
        mean_df.reset_index(inplace=True)
        mean_df.sort_values(by=['stddev'], inplace=True, ascending=True) 
        mean_df['rank']=mean_df['stddev'].rank(ascending = 1)
        mean_df.reset_index(inplace = True)
        mean_df.index = np.arange(1, len(mean_df) + 1)

        fig = go.Figure(data=[go.Table(
        header=dict(values=list(['Ranks','College']),
            fill_color='paleturquoise',
            align='left'),
        cells=dict(values=[mean_df.index[:-2],mean_df.college_code],
            fill_color='lavender',
            align='left'))
        ])

        st.plotly_chart(fig)

        
        st.write("Specific's of  college")

        college_code_list = mean_df['college_code'].unique()
        mul_coll = st.multiselect("Choose Multiple Colleges / CollegeCodes to compare", list(college_code_list),default=['124:MGMCET','126:SAKEC','174:RAIT','17:BVCE'])
        sem_list=[]
        
        
        fig = go.Figure()
        for sub_college in mul_coll:    
            mean_college = []
           
            sem_list  = ['sem_1','sem_2','sem_3','sem_4','sem_5','sem_6','sem_7','sem_8','cgpi']
            sem = ["SEM I","SEM II","SEM III","SEM IV","SEM V","SEM VI","SEM VII","SEM VIII","CGPI"]
            for x in sem_list:
                mean_college.append(float(mean_df[(mean_df['college_code']==sub_college)][x]))               
             
            
            
            
            fig.add_trace(go.Scatter(x=sem, y=mean_college, name= sub_college + ' Average',
                                    line=dict( width=4)))
            
            fig.update_layout(
                    legend=dict(orientation="h"),
                    shapes=[
                        # 1st highlight
                        dict(
                            type="rect",
                            # x-reference is assigned to the x-values
                            xref="x",
                            # y-reference is assigned to the plot paper [0,1]
                            yref="paper",
                            x0=0,
                            y0=0,
                            x1=1.5,
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
                            x0=1.5,
                            y0=0,
                            x1=5.5,
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
                            x0=5.5,
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
        fig.update_layout(title='College Deviations',title_x=0.5,
                        xaxis_title='Deviation w.r.t Semesters',
                    yaxis_title='Deviation w.r.t Departments',height=550)
        st.write('<b>The background color determines where your examination papers are checked.</b>',unsafe_allow_html=True)
        st.write('<b><i style="color:mediumspringgreen"> External Checking</i></b> and <b><i style = "color:LIGHTSALMON"> Internal Checking </i></b>',unsafe_allow_html=True)
        st.plotly_chart(fig)
        st.write("<p>Look for the consistency between the green and orange part as that's most prone to colleges' inconsistency. <br>Observe the line: <br>- more flatter means more consistent w.r.t semesters and vice-versa.<br>- closer to x-axis means more consistent w.r.t departments and vice-versa.</p>",unsafe_allow_html=True)
    
    if anl_sel == 'Top Elective Subjects':
        import statistics
        import plotly.graph_objects as go
        import pandas as pd
        dip_sel = st.checkbox('Diploma Student/Direct 2nd year',False)
        data = pd.read_csv('./csv_db/regular.csv')
        if dip_sel:
            data = pd.read_csv('./csv_db/diploma.csv')
            sem_1,sem_2 = None,None
        new = data.groupby(['college_code','elective','department']).max()
        new.reset_index(inplace=True)
        max_elec = new['elective'].value_counts().rename_axis('counts').reset_index(name='elective')  #new['elective'].value_counts()
        #st.write(max_elec['elective'])

        if dip_sel:
            fig = go.Figure(data=[go.Table(
        header=dict(values=list(['Dip. Elective Subjects','Max elected Counts']),
            fill_color='paleturquoise',
            align='left'),
        cells=dict(values=[max_elec.counts, max_elec['elective']],
            fill_color='lightcyan',
            align='left'))
        ])
        else:
            fig = go.Figure(data=[go.Table(
        header=dict(values=list(['Elective Subjects','Max elected Counts']),
            fill_color='paleturquoise',
            align='left'),
        cells=dict(values=[max_elec.counts, max_elec['elective']],
            fill_color='lavender',
            align='left'))
        ])

        st.plotly_chart(fig)

        

        st.write('According to departments/streams')


        department_list = mean_df['department'].unique()
       
        sub_dep = st.selectbox("Choose department/stream to see ranking ", list(department_list))
        
        new = data[data['department']==sub_dep].groupby(['college_code','elective','department']).count()
        new.reset_index(inplace=True)
        max_elec = new['elective'].value_counts().rename_axis('counts').reset_index(name='elective')  #new['elective'].value_counts()
        #st.write(max_elec['elective'])

        if dip_sel:
            fig = go.Figure(data=[go.Table(
        header=dict(values=list(['Dip. Elective Subjects','Max elected Counts']),
            fill_color='paleturquoise',
            align='left'),
        cells=dict(values=[max_elec.counts, max_elec['elective']],
            fill_color='lightcyan',
            align='left'))
        ])
        else:
            fig = go.Figure(data=[go.Table(
        header=dict(values=list(['Elective Subjects','Max elected Counts']),
            fill_color='paleturquoise',
            align='left'),
        cells=dict(values=[max_elec.counts, max_elec['elective']],
            fill_color='lavender',
            align='left'))
        ])
        
        st.plotly_chart(fig)
        st.write("Above ranking is the count of the elective subject chosen within different colleges. <br>The only tip:<br>- choose an elective subject with good resources available to study, mostly that subject is one of the top elected subjects. Do thorough research before selecting a subject as good resources aids in good grades",unsafe_allow_html=True)

    if anl_sel == 'Elected Subject & performance':
        import plotly.express as px

        dip_sel = st.checkbox('Diploma Student/Direct 2nd year',False)
        data = pd.read_csv('./csv_db/regular.csv')
        if dip_sel:
            data = pd.read_csv('./csv_db/diploma.csv')
            sem_1,sem_2 = None,None
        department_list = mean_df['department'].unique()
       
        sub_dep = st.selectbox("Choose department/stream to see ranking ", list(department_list))
        cal_sub = st.radio("Select a metric to compute",
                            ('Average',  'Max','Min'))
        if sub_dep in ['COMPUTER ENGINEERING']:
            elec_c = 'c3_th'
        else:
            elec_c = 'c2_th'
        if cal_sub == 'Average':
            new = data.groupby(['department','elective'],as_index=False)[elec_c].mean()
        if cal_sub == 'Max':
            new = data.groupby(['department','elective'],as_index=False)[elec_c].max()
        if cal_sub == 'Min':
            new = data.groupby(['department','elective'],as_index=False)[elec_c].min()
       
        new_df = new[(new['department']==sub_dep)][['elective',elec_c]]

        if dip_sel:
            sub_dep = 'Dip. ' + sub_dep

        fig = px.bar(new_df, x='elective', y=elec_c,color=elec_c,color_continuous_scale='rdylbu')
        fig.update_layout(title=sub_dep +" Elected subject's " + cal_sub + " Performance",title_x=0.5,
                        xaxis_title='Courses',
                    yaxis_title='Marks Obtained',height=550)
        st.plotly_chart(fig)
        st.write('Here look for subjects that have high grades and your interest in it.')
    

    if anl_sel == 'Department Wise performance':
        dip_sel = st.checkbox('Diploma Student/Direct 2nd year',False)
            
        if dip_sel:
            mean_df = pd.read_csv('./csv_db/mean_df_dip.csv')
            max_df = pd.read_csv('./csv_db/max_df_dip.csv')
            min_df = pd.read_csv('./csv_db/min_df_dip.csv')
            sem_1,sem_2 = None,None
        college_code_list = mean_df['college_code'].unique()
        sub_college = st.selectbox("Choose Multiple Colleges / CollegeCodes to compare", list(college_code_list))
       
        cal_sub = st.radio("Select a metric to compute",
                            ('Average',  'Max','Min'))
        fig = go.Figure()
        mul_coll = min_df[min_df['college_code']==sub_college]['department'].unique()
        for sub_dep in mul_coll:    
            mean_college = []
            max_college = []
            min_college = []
            #st.write((mul_coll))
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
                       # st.write(min_college)
            
            
            # Add scatter trace for line
            fig.add_trace(go.Scatter(x=sem, y=max_college, name= sub_dep +' Max',
                                    line=dict( width=4)))
            fig.add_trace(go.Scatter(x=sem, y=mean_college, name= sub_dep + ' Average',
                                    line=dict( width=4)))
            fig.add_trace(go.Scatter(x=sem, y=min_college, name = sub_dep + ' Min',
                                    line=dict( width=4)))
            

            if dip_sel == False:
                                
                fig.update_layout(
                    legend=dict(orientation="h"),
                    shapes=[
                        # 1st highlight
                        dict(
                            type="rect",
                            # x-reference is assigned to the x-values
                            xref="x",
                            # y-reference is assigned to the plot paper [0,1]
                            yref="paper",
                            x0=0,
                            y0=0,
                            x1=1.5,
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
                            x0=1.5,
                            y0=0,
                            x1=5.5,
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
                            x0=5.5,
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
                     
                    legend=dict(orientation="h"),
                    shapes=[
                        # 2nd highlight
                        dict(
                            type="rect",
                            xref="x",
                            yref="paper",
                            x0="SEM III",
                            y0=0,
                            x1=3.5,
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
                            x0=3.5,
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
        if dip_sel:
                cal_sub = 'Dip. ' + cal_sub
        fig.update_layout(title=cal_sub+' Department-Wise Performance of '+sub_college,title_x=0.5,
                        xaxis_title='Semesters',
                    yaxis_title='Pointers',height=550)
        st.write('<b>The background color determines where your examination papers are checked.</b>',unsafe_allow_html=True)
        st.write('<b><i style="color:mediumspringgreen"> External Checking</i></b> and <b><i style = "color:LIGHTSALMON"> Internal Checking </i></b>',unsafe_allow_html=True)
        st.plotly_chart(fig)

def contribute():
    import streamlit as st
    from PIL import Image
    st.markdown(
        """ <p style="color:red">
         <b>Note</b> - Change the left menu parameters, and if it's not present, hit on the arrow at the top left, you will get a menubar.
         If you are using a mobile device, then you might require to hit the arrow frequently as it gets hidden due to the small display size.
         For the best experience,<b> use Desktop.</b> 
        </p>


        """,unsafe_allow_html=True

    )
    st.write('You can contribute in many ways not only to me but your friends. Those who need to choose a college, one who is in college. So that they can normalize their expectations, see the pitfalls, dips in grades of college, and perform accordingly.')
    st.write('You can share my profile and help me land a Job',unsafe_allow_html=True)
    #<a href="https://www.linkedin.com/in/rushikeshgholap/"> Rushikesh Gholap</a> 
    st.write('<a href="https://www.linkedin.com/in/rushikeshgholap/"> LinkedIn    </a> <br> <a href="https://github.com/RushikeshGholap"> Github </a> <br> <a href="mailto:rushikeshbgholap?Subject=Job" target="_top">Email</a>',unsafe_allow_html=True)
    #st.write('You can share my profile and help me land a Job',unsafe_allow_html=True)
    st.write('You can donate me via UPI- rushikesh131998@oksbi')
    st.write('Or can click here (Only works with UPI enabled device)<a href="upi://pay?pa=rushikesh131998@oksbi&pn=rushikesh gholap&aid=ugicagicansjmug"> Donate</a>',unsafe_allow_html=True)
    qr = st.button('Scan QR Code')
    
    if qr:
        image = Image.open('upi.jpg')
        st.image(image, width=300)

def suggestion():
    import streamlit as st
    import pandas as pd
    sub = True
    st.markdown(
        """ <p style="color:red">
         <b>Note</b> - Change the left menu parameters, and if it's not present, hit on the arrow at the top left, you will get a menubar.
         If you are using a mobile device, then you might require to hit the arrow frequently as it gets hidden due to the small display size.
         For the best experience,<b> use Desktop.</b> 
        </p>


        """,unsafe_allow_html=True

    )
    st.markdown(
        """
        Feel free to give your suggestions and feedback
        """
    )
    user_name = st.text_input("Enter Name * ")
    if user_name == '':
        st.write('<p style="color:red"> Name not entered! </p>',unsafe_allow_html=True)
        sub = False
    
    user_contact = st.text_input("Enter your contact (like email,number,etc) *")
    if user_contact == '':
        sub = False
        st.write('<p style="color:red"> Contact not entered! </p>',unsafe_allow_html=True)
    
    user_input = st.text_input("Enter your suggestions/feedback here *")
    if user_input == '':
        sub = False
        st.write('<p style="color:red"> Suggestion/feedback not entered! </p>',unsafe_allow_html=True)
    
    if sub:
        success = st.button('Submit')
        sugges = {'name':user_name,'contact':user_contact,'suggestion':user_input}
        if success:
            suggestion = pd.read_csv('./csv_db/suggestion.csv')
            suggestion =  suggestion.append(sugges,ignore_index =True)
            suggestion.to_csv('./csv_db/suggestion.csv',index =False)
            user_name,user_contact,user_input  = '','',''
            st.success('Thank you for suggestion/feedback.')

def working():
    import streamlit as st
    st.markdown(
        """
        
        """
    )
   