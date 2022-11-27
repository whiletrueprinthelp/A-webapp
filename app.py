from flask import Flask, render_template, request
import csv

# create app
app = Flask(__name__)

# to convert data from csv file to store into python dictionary
with open("subject-resource.csv") as file: #close file automatically 
  reader = csv.reader(file)
  header = next(reader)
  subject_list = [row for row in reader]
  print(subject_list)

#first page
@app.route('/')
def index():
    return render_template("index.html")

# after inputting subject in first page
@app.route('/wanted-subject')
def subject():
  input = request.args.get("subject").lower()
  
  #Validate submission
  if not input: # if no input
    return render_template("error.html", message="No input")

  for subject in subject_list:
    if input in subject: # subject exists in list
      if "Not available" in subject[-1]: #if there is no link
        return render_template("no_link_subject.html", message=subject[-1])
      else: # if there is link to access resource
        return render_template("wanted-subject.html", link=subject[-1], text=subject[0].capitalize()+" Repository")

  # if input cannot be found in list or is not an actual subject 
  return render_template("error.html", message="You have input an invalid input.")

app.run(host='0.0.0.0', port=5000) # might not need ? (when using replit, this was needed to run the app and display)
