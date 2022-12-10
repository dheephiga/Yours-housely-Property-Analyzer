from flask import Flask, render_template, request
import pandas as pd
import pickle
app = Flask(__name__, template_folder="templates")
rfr = pickle.load(open('cbr.pkl','rb'))
le1 = pickle.load(open('le1.pkl','rb'))
le2 = pickle.load(open('le2.pkl','rb'))
le3 = pickle.load(open('le3.pkl','rb'))
le4 = pickle.load(open('le4.pkl','rb'))
le5 = pickle.load(open('le5.pkl','rb'))
le6 = pickle.load(open('le6.pkl','rb'))


@app.route('/')
def home():
    return render_template ('front.html')

@app.route('/predict',methods=['POST'])
def predict():
    pid = request.form['p_id']
    Property_Type = request.form['p_type']
    parea = request.form['p_area']
    pwind = request.form['p_windows'] 
    pdoor = request.form['p_doors']
    Furnishing = request.form['p_furn']
    ppcuts = request.form['p_pcuts']
    Power_Backup = request.form['p_pbackup']
    Water_Supply = request.form['p_water']
    ptraffic = request.form['p_traffic']
    Crime_Rate = request.form['p_crime']
    Dust_and_Noise = request.form['p_dustnoise']
    pair = request.form['p_air']
    pneigh = request.form['p_neigh']
    
    data = {
        # "Property_ID" : pid,
        "Property_Type" : Property_Type,
        "Property_Area" : parea,
        "No_of_windows" : pwind,
        "No_of_doors" : pdoor,
        "Furnishing" : Furnishing,
        "Powercuts" : ppcuts,
        "Power_Backup": Power_Backup,
        "Water_Supply" : Water_Supply,
        "Traffic_Density": ptraffic,
        "Crime_Rate" : Crime_Rate,
        "Dust_Noise" : Dust_and_Noise,
        "Air_Density" : pair,
        "Neighbourhood_Review" : pneigh,
    }

    ch_df = pd.DataFrame(data, index=list('Property_ID'))

    ch_df['Property_Type'] = le1.transform(ch_df['Property_Type'])
    ch_df['Furnishing'] = le2.transform(ch_df['Furnishing'])
    ch_df['Power_Backup'] = le3.transform(ch_df['Power_Backup'])
    ch_df['Water_Supply'] = le4.transform(ch_df['Water_Supply'])
    ch_df['Crime_Rate'] = le5.transform(ch_df['Crime_Rate'])
    ch_df['Dust_Noise'] = le6.transform(ch_df['Dust_Noise'])
    
    score1 = rfr.predict(ch_df)
    score = score1[0]

    return render_template('front.html',predict_text= 'Score of the property is {}'.format(score))
if __name__ == "__main__":
    app.run(debug=True)
    