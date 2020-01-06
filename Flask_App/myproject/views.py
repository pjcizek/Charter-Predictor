from flask import render_template
from myproject import app

import pandas as pd

from flask import request

import numpy as np



@app.route('/')
#@app.route('/index')
#def index():
#    return render_template("index.html",
#       title = 'Home', user = { 'nickname': 'Miguel' },
#       )

@app.route('/input', methods=['GET', 'POST'])
def movie_input():
    return render_template("input.html")

@app.route('/output')
def movie_output():
    # First convert request.args to regular Python dictionary
    import pandas as pd
    response = request.args.get('School')
    response = int(response)
    data2 = pd.read_excel('Charter_School_Output.xlsx')
   

    #data2 = data2.set_index('School')
    school_name = data2.iloc[response][1]
    nn1_name = data2.iloc[response][2]
    nn2_name = data2.iloc[response][3]
    nn3_name = data2.iloc[response][4]
    nn4_name = data2.iloc[response][5]
    nn5_name = data2.iloc[response][6]
    
    probability = data2.iloc[response][25]
    nn1_probability = data2.iloc[response][26]
    nn2_probability = data2.iloc[response][27]
    nn3_probability = data2.iloc[response][28]
    nn4_probability = data2.iloc[response][29]
    nn5_probability = data2.iloc[response][30]
    
    risk_level = data2.iloc[response][31]
    nn1_risk_level = data2.iloc[response][32]
    nn2_risk_level = data2.iloc[response][33]
    nn3_risk_level = data2.iloc[response][34]
    nn4_risk_level = data2.iloc[response][35]
    nn5_risk_level = data2.iloc[response][36]
    
    school_enrollment = data2.iloc[response][37] 
    nn1_school_enrollment = data2.iloc[response][38]
    nn2_school_enrollment = data2.iloc[response][39]
    nn3_school_enrollment = data2.iloc[response][40]
    nn4_school_enrollment = data2.iloc[response][41]
    nn5_school_enrollment = data2.iloc[response][42]
   
    avg_enrollment = 240
    
    school_lat = data2.iloc[response][13]
    nn1_lat = data2.iloc[response][14]
    nn2_lat = data2.iloc[response][15]
    nn3_lat = data2.iloc[response][16]
    nn4_lat = data2.iloc[response][17]
    nn5_lat = data2.iloc[response][18]
    
    school_long = data2.iloc[response][19]
    nn1_long = data2.iloc[response][20]
    nn2_long = data2.iloc[response][21]
    nn3_long = data2.iloc[response][22]
    nn4_long = data2.iloc[response][23]
    nn5_long = data2.iloc[response][24]
    
    nn1_distance = data2.iloc[response][44]
    nn2_distance = data2.iloc[response][45]
    nn3_distance = data2.iloc[response][46]
    nn4_distance = data2.iloc[response][47]
    nn5_distance = data2.iloc[response][48]
   
    return render_template("output.html", the_result= risk_level, viability = probability, 
                           movie_title= school_name, se = school_enrollment, 
                           ae = avg_enrollment, lat0 = school_lat, long0 = school_long,
                           nn1name = nn1_name, nn2name = nn2_name, nn3name = nn3_name, 
                           nn4name = nn4_name, nn5name = nn5_name, nn1probability = nn1_probability,
                           nn2probability = nn2_probability, nn3probability = nn3_probability, 
                           nn4probability = nn4_probability, nn5probability = nn5_probability,
                           nn1risk_level = nn1_risk_level, nn2risk_level = nn2_risk_level,
                           nn3risk_level = nn3_risk_level, nn4risk_level = nn4_risk_level,
                           nn5risk_level = nn5_risk_level, nn1school_enrollment = nn1_school_enrollment,
                           nn2school_enrollment = nn2_school_enrollment, nn3school_enrollment = nn3_school_enrollment,
                           nn4school_enrollment = nn4_school_enrollment, nn5school_enrollment = nn5_school_enrollment,
                           nn1lat = nn1_lat, nn2lat = nn2_lat, nn3lat = nn3_lat, nn4lat = nn4_lat, nn5lat = nn5_lat,
                           nn1long = nn1_long, nn2long = nn2_long, nn3long = nn3_long, nn4long = nn4_long, nn5long = nn5_long,
                           nn1distance = nn1_distance, nn2distance = nn2_distance,  nn3distance = nn3_distance, 
                           nn4distance = nn4_distance, nn5distance = nn5_distance)
