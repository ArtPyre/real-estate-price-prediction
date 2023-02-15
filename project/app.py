from flask import Flask, request, render_template
import preprocessing.cleaning_data
import predict.prediction
app = Flask(__name__)

@app.route('/')
def home():
   return "hello world"

@app.route('/predict', methods = ['POST', 'GET'])
def prediction():
   datas = dict()
   if (request.method == 'POST'):
      if request.form.get("garden") == None:
         datas["garden"] = False
         datas["garden-area"] = 0
      if request.form.get("terrace") == None:
         datas["terrace"] = False
         datas["terrace-area"] = 0
      if request.form.get("equipped-kitchen") == None:
         datas["equipped-kitchen"] = False
      if request.form.get("swimming-pool") == None:
         datas["swimming-pool"] = False
      if request.form.get("furnished") == None:
         datas["furnished"] = False
      if request.form.get("open-fire") == None:
         datas["open-fire"] = False

      datas.update(request.form.to_dict())
      df = preprocessing.cleaning_data.preprocess(datas)
      return render_template("app.html", result=predict.prediction.predict(df, 'GDR_model.pkl'))
   elif(request.method == 'GET') :
      
      pass
   
   return render_template("app.html")

if __name__ == '__main__':
   app.run()