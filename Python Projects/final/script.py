#Final Programming Project
#Repository Pathway: https://github.com/KR031994/bch5884
#Regression analysis& related plots on running program and Data visualizations in html
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, make_scorer
from sklearn.model_selection import cross_validate

def write_html(image_list):
    doc = '''<html>
    <head>
    <title>Graphical Representation</title>
    </head>
    <body style="background-color:black;"></body>
	<h1 style="color:red;text-align:center;">Holistic Approach to
               Diabetes Risk Prediction</h1>
    <h3 style="color:yellow;text-align:left;">Type 2 diabetes (formerly called non-insulin-dependent, or adult-onset) results from the body’s ineffective use of insulin.In 2014, 8.5% of adults aged 18 years and older had diabetes. 
               In 2016, diabetes was the direct cause of 1.6 million deaths and in 2012 high blood glucose was the cause of another 2.2 million deaths.Between 2000 and 2016, there was a 5% increase in premature mortality from diabetes.</h3>
    <h3  style="color:yellow;text-align:left;">Adults with diabetes have a two- to three-fold increased risk of heart attacks and strokes.
               Combined with reduced blood flow, neuropathy (nerve damage) in the feet increases the chance of foot ulcers, infection and eventual need for limb amputation.
               Diabetic retinopathy is an important cause of blindness, and occurs as a result of long-term accumulated damage to the small blood vessels in the retina. Diabetes is the cause of 2.6% of global blindness.
               Diabetes is among the leading causes of kidney failure.Here's one look into the shocking statistics.<a href="https://www.who.int/news-room/fact-sheets/detail/diabetes#:~:text=Key%20facts,in%20premature%20mortality%20from%20diabetes."><em>[www.who.int]</em></a></h3> 
	'''
    for image in image_list:
        doc += '''<img src="'''+image+'''" width="623" height="610" class="center">'''
    doc += '''</body></html>'''
    with open("output.html", 'w') as f:
        f.write(doc)

# begin analysis of file "diabetesdataset1.csv"
#Dataset1- Accounting for risk factors of diabetes progression
df = pd.read_csv('diabetesdataset1.csv')
print(df.head())
print(df.describe())
print(df.info())

#Data Visualization
df.hist(bins=10, figsize=(10, 10))
plt.savefig('graph1_1.jpg')
plt.clf()

sns.set(style="whitegrid")
df.boxplot(figsize=(15,6))
plt.savefig('graph1_2.jpg')
plt.clf()

sns.countplot(y=df['Outcome'], palette='Set1')
plt.title('NIDDK Records-Outcome:0 for non-diabetic,1 for diabetic')
plt.savefig('graph1_3.jpg')
plt.clf()

#Removing Outliers
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3-Q1
df_out = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
df.shape,df_out.shape

#Extraction of target data
X = df_out.drop(columns=['Outcome'])
y = df_out['Outcome']

#Splitting train test data into 80:20 ratio
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2)
print(train_X.shape, test_X.shape, train_y.shape, test_y.shape)

#Creation of Confusion Matrix
def tn(y_true, y_pred):#tn(true negative):outcome where model correctly predicts the negative class
    return confusion_matrix(y_true, y_pred)[0, 0]

def fp(y_true, y_pred):#fp(false positive):outcome where model incorrectly predicts the positive class
    return confusion_matrix(y_true, y_pred)[0, 1]

def fn(y_true, y_pred):#fn(false negative):outcome where model incorrectly predicts the negative class
    return confusion_matrix(y_true, y_pred)[1, 0]

def tp(y_true, y_pred):#tp(true positive):outcome where model correctly predicts the positive class
    return confusion_matrix(y_true, y_pred)[1, 1]

#cross validation(no. of runs)
scoring = {'accuracy': make_scorer(accuracy_score), 'prec': 'precision'}
scoring = {'tp': make_scorer(tp), 'tn': make_scorer(tn),
           'fp': make_scorer(fp), 'fn': make_scorer(fn)}

def display_result(result):
    print("TP: ", result['test_tp'])
    print("TN: ", result['test_tn'])
    print("FN: ", result['test_fn'])
    print("FP: ", result['test_fp'])

#Building the models
acc = []
roc = []
#ROC AUC:Area under the ROC(Receiver operating characteristic)Curve

def do_predictions(stats):#to find how accurately models can predict reported hospital data
    stats.fit(train_X, train_y)
    y_pred = stats.predict(test_X)
    ac = accuracy_score(test_y, y_pred)
    acc.append(ac)
    rc = roc_auc_score(test_y, y_pred)
    roc.append(rc)
    print("\nAccuracy {0} ROC {1}".format(ac, rc))
    result = cross_validate(stats, train_X, train_y, scoring=scoring, cv=10)
    display_result(result)

warnings.filterwarnings("ignore", category=FutureWarning)
do_predictions(LogisticRegression(max_iter=1000))
do_predictions(GaussianNB())
do_predictions(RandomForestClassifier())
do_predictions(KNeighborsClassifier(n_neighbors=3))
do_predictions(SVC(kernel='linear'))
do_predictions(GradientBoostingClassifier(n_estimators=50, learning_rate=0.2))

#Comparison of accuracy scores of algorithms
ax = plt.figure(figsize=(12, 4))
plt.bar(['Logistic Regression', 'SVM', 'KNN', 'Random Forest',
         'Naivye Bayes', 'Gradient Boosting'], acc, label='Accuracy')
plt.ylabel('Accuracy Score')
plt.xlabel('Algorithms')
plt.title('Dataset I')
plt.savefig('graph1_ML1.jpg')
plt.show()
plt.clf()

ax = plt.figure(figsize=(12, 4))
plt.bar(['Logistic Regression', 'SVM', 'KNN', 'Random Forest',
         'Naivye Bayes', 'Gradient Boosting'], roc, label='ROC AUC')
plt.ylabel('ROC AUC')
plt.xlabel('Algorithms')
plt.title('Dataset I')
plt.savefig('graph1_ML2.jpg')
plt.show()

#begin analysis of "diabetesdataset2.csv"
#Dataset2-Typical Symptoms of early onset diabetes
df = pd.read_csv("diabetesdataset2.csv")
print(df.head())
print(df.describe())
print(df.info())

#Data Visualizations
df.hist(grid=False, figsize=(15, 15))
plt.savefig("graph2_1.jpg")
plt.clf()

corr = df.corr()
sns.heatmap(corr,annot=True)
plt.savefig("graph2_2.jpg")
plt.clf()

sns.distplot(df['class'])
plt.title('Sylhet, Bangladesh Hospital Records-Class:0 for non-diabetic,1 for diabetic')
plt.savefig("graph2_3.jpg")
plt.clf()

#Removing Outliers
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3-Q1
df_out = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
df.shape,df_out.shape

#Extraction of target data
X = df_out.drop(columns=['class', 'Gender'])
y = df_out['class']

#Splitting train test data into 80:20 ratio
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2)
print(train_X.shape, test_X.shape, train_y.shape, test_y.shape)

#Building models
acc = []
roc = []

warnings.filterwarnings("ignore", category=FutureWarning)
do_predictions(LogisticRegression(max_iter=1000))
do_predictions(RandomForestClassifier())
do_predictions(GradientBoostingClassifier(n_estimators=50, learning_rate=0.2))

ax = plt.figure(figsize=(12, 4))
plt.bar(['Logistic Regression', 'Random Forest',
         'Gradient Boosting'], acc, label='Accuracy')
plt.ylabel('Accuracy Score')
plt.xlabel('Algorithms')
plt.title('Dataset II')
plt.savefig('graph2_ML3.jpg')
plt.show()

ax = plt.figure(figsize=(12, 4))
plt.bar(['Logistic Regression', 'Random Forest',
         'Gradient Boosting'], roc, label='ROC AUC')
plt.ylabel('ROC AUC')
plt.xlabel('Algorithms')
plt.title('Dataset II')
plt.savefig('graph2_ML4.jpg')
plt.show()

#begin analysis of "diabetesdataset3.csv"(Only data visualization,no ML analysis)
#Dataset3:Visualizing possible correlation between measurement of HbA1c levels and hospital readmission rates 
df=pd.read_csv('diabetesdataset3.csv')
print(df.head())
print(df.describe())
print(df.info())

#Data Visualization
sns.countplot(x=df['readmitted'])
plt.title('10:None;20:<30 days;40:>30 days')
plt.savefig("graph3_1.jpg")
plt.clf()

sns.countplot(df['A1Cresult'])
plt.title('0:None;1:Norm;3:>6;4:>7')
plt.savefig("graph3_2.jpg")
plt.clf()

df.plot(kind ='density',subplots = True, layout =(2,2),sharex = False)
plt.savefig("graph3_3.jpg")
plt.clf()

sns.heatmap(df.corr())
plt.savefig("graph3_4.jpg")
plt.clf()

pics = ["graph"+str(i)+"_"+str(j)+".jpg"
            for i in range(1, 3) for j in range(1, 4)]
pics.extend(["graph3_1.jpg","graph3_2.jpg","graph3_3.jpg","graph3_4.jpg"])
write_html(pics) #write the images to output html file



