import urllib.error


def about():
    import streamlit as st

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




    diploma = st.sidebar.checkbox("Diploma Student/Direct 2nd year", False)

   
    
    
    
    
    st.markdown(
        """ 
        Change the parameters on left menu and if its not present hit on arrow at top left you will get menubar
        """

    )
    st.sidebar.success("Enter the semwise Pointers  👇 ")
    
    if diploma:
        mean_df = pd.read_csv('./mean_df_dip.csv')
        max_df = pd.read_csv('./max_df_dip.csv')
        min_df = pd.read_csv('./min_df_dip.csv')

        dip_template = pd.read_csv('./Diploma_template.csv')
        
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
        
        sem_8 = float(regression_model_diploma.predict(pred[-1:]))
        cgpi = statistics.mean([sem_8,sem_3,sem_4,sem_5,sem_6,sem_7])
        mean_college = [sem_1,sem_2]
        max_college = [sem_1,sem_2]
        min_college = [sem_1,sem_2]
        for x in ['sem_3','sem_4','sem_5','sem_6','sem_7','sem_8','cgpi']:

            mean_college.append(float(mean_df[(mean_df['college_code']==sub_college) & (mean_df['department']==sub_dep)][x]))
            max_college.append(float(max_df[(max_df['college_code']==sub_college) & (max_df['department']==sub_dep)][x]))
            min_college.append(float(min_df[(min_df['college_code']==sub_college) & (min_df['department']==sub_dep)][x]))
            
        
        st.write("The predicted pointers for SEM VIII :",round(sem_8,2))
        st.write("The predicted CGPI :",round(cgpi,2))


    else:
        mean_df = pd.read_csv('./mean_df.csv')
        max_df = pd.read_csv('./max_df.csv')
        min_df = pd.read_csv('./min_df.csv')
        template = pd.read_csv('./template.csv')
        college_code_list = mean_df['college_code'].unique()
        sub_college = st.sidebar.selectbox(
            "Choose College Code ", list(college_code_list))
        dep_list = mean_df[mean_df['college_code']==sub_college]['department'].unique()
        sub_dep = st.sidebar.selectbox(
            "Choose Department", list(dep_list))


        infile = open('regression_model_regular','rb')
        regression_model_regular = pickle.load(infile)
        infile.close()
                
        diff = 0 
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
        sem_8 = float(regression_model_regular.predict(pred[-1:]))
        cgpi = statistics.mean([sem_8,sem_1,sem_2,sem_3,sem_4,sem_5,sem_6,sem_7])
        st.write("The predicted pointers for SEM VIII :",round(sem_8,2))
        st.write("The predicted CGPI :",round(cgpi,2))
    # Add data
    sem = ["SEM I","SEM II","SEM III","SEM IV","SEM V","SEM VI","SEM VII","SEM VIII","CGPI"]            
    predicted = [sem_1,sem_2,sem_3,sem_4,sem_5,sem_6,sem_7,sem_8,cgpi]
    fig = go.Figure()
    # Create and style traces
    fig.add_trace(go.Scatter(x=sem, y=max_college, name='Max of College',
                            line=dict(color='firebrick', width=4)))
    fig.add_trace(go.Scatter(x=sem, y=mean_college, name='Mean of College',
                            line=dict(color='royalblue', width=4)))
    fig.add_trace(go.Scatter(x=sem, y=min_college, name = 'Min of College',
                            line=dict(color='red', width=4)))
    fig.add_trace(go.Scatter(x=sem, y=predicted, name='Predicted',
                            line=dict(color='green', width=4,
                                dash='dash'),connectgaps=False ))

    # Edit the layout
    fig.update_layout(title='Performance per Semisters ',
                    xaxis_title='Semisters ',
                    yaxis_title='Pointers')
    fig.update_yaxes(tickvals=[0,1,2,3,4,5,6,7,8,9,10])
    st.plotly_chart(fig)



def analysis():
    import streamlit as st
    import numpy as np

    st.markdown(
        """
        This is analysis 
        """
    )

      
    # Interactive Streamlit elements, like these sliders, return their value.
    # This gives you an extremely simple interaction model.
    iterations = st.sidebar.slider("Level of detail", 2, 20, 10, 1)
    separation = st.sidebar.slider("Separation", 0.7, 2.0, 0.7885)

    # Non-interactive elements return a placeholder to their location
    # in the app. Here we're storing progress_bar to update it later.
    progress_bar = st.sidebar.progress(0)

    # These two elements will be filled in later, so we create a placeholder
    # for them using st.empty()
    frame_text = st.sidebar.empty()
    image = st.empty()

    m, n, s = 960, 640, 400
    x = np.linspace(-m / s, m / s, num=m).reshape((1, m))
    y = np.linspace(-n / s, n / s, num=n).reshape((n, 1))

    for frame_num, a in enumerate(np.linspace(0.0, 4 * np.pi, 100)):
        # Here were setting value for these two elements.
        progress_bar.progress(frame_num)
        frame_text.text("Frame %i/100" % (frame_num + 1))

        # Performing some fractal wizardry.
        c = separation * np.exp(1j * a)
        Z = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))
        C = np.full((n, m), c)
        M = np.full((n, m), True, dtype=bool)
        N = np.zeros((n, m))

        for i in range(iterations):
            Z[M] = Z[M] * Z[M] + C[M]
            M[np.abs(Z) > 2] = False
            N[M] = i

        # Update the image placeholder by calling the image() function on it.
        image.image(1.0 - (N / N.max()), use_column_width=True)

    # We clear elements by calling empty on them.
    progress_bar.empty()
    frame_text.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")


# fmt: on

# Turn off black formatting for this function to present the user with more
# compact code.
# fmt: off
def compare():
    import streamlit as st
    import time
    import numpy as np
    st.markdown(
        """
        This is compare    
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