'''بسم الله الرحمن الرحيم'''               

                            #Eight SESSION (Pandas Liberary) & Project using Pandas & Numpy
#مكتبة الpandas
#وهى مكتبة قوية فى مجال تحليل البيانات
#وهيا عبارة عن شيتات مثل الexcel بالظبط
#ولذلك هيا بتعتمد على الdataframe
import pandas as pd
import numpy as np
A=np.array([[1,2,3,4,5,6,7,8,9,10],[10,20,30,40,50,60,70,80,90,100],[11,22,33,44,55,66,77,88,99,110],[11,22,33,44,55,66,77,88,99,110],[11,22,33,44,55,66,77,88,99,110],[11,22,33,44,55,66,77,88,99,110],[11,22,33,44,55,66,77,88,99,110],[11,22,33,44,55,66,77,88,99,110],[11,22,33,44,55,66,77,88,99,110],[11,22,33,44,55,66,77,88,99,110],[11,22,33,44,55,66,77,88,99,110],[11,22,33,44,55,66,77,88,99,110],[11,22,33,44,55,66,77,88,99,110],[11,22,33,44,55,66,77,88,99,110],[11,22,33,44,55,66,77,88,99,110],[11,22,33,44,55,66,77,88,99,110],[11,22,33,44,55,66,77,88,99,110],[11,22,33,44,55,66,77,88,99,110]])
print(A)
#لعمل data frame 
#بمعنى عمل جدول للarray
data=pd.DataFrame(A)
print(data)
#لتخزين list مثل بروجكت المكتبة
dic={"name":["Ahemd","Ali","bahy"],"Age":[28,29,25],"study":["linear","math","geo"]}
print(dic)
#تحويلة لdataframe
data1=pd.DataFrame(data=dic)
print(data1)
#لعمل array بعناصر عشوائية غير محددة
#ويتم تحديد حجم الraws&columns
#وهدفة هو مثلا تحديد خط عشوائي فى الlinear regression فى مجال تحليل البيانات
rand=np.random.rand(6,4)
#لعمل dataframe من بيانات عشوائية
data2=pd.DataFrame(rand)
#لعمل عمليات حسابية على الdataframe فيها ارقام
print(data.describe())
#فى الشيتات للبيانات لو عدد العناصر بالarray ضخم 
#ومحتاج تظهر للمستخدم عناصر محددة
#اول 5 عناصر مثلا
print(data.head(5))
#اَخر 5 عناصر مثلا
print(data.tail(5))
#لتغيير أسماء الcolumns
data=pd.DataFrame(A,columns=list("ABCDEFGHIJ"))
#لتغيير اسماء الindex بمعنى تغيير اسما الrows
data=pd.DataFrame(A,columns=list("ABCDEFGHIJ"),index=list("ABCDEFGHIJKLMNOPQR"))
#how to slice to get aspecific column
#لو اردت طباعة عمود معين من الdataframe ولنفترض تريد طباعة column 'A'from the table
data["A"]
#to print more than one specific cloumns
data[["E","B"]]
#to print specific more than one rows(by index)
#بمعنى انك مثلا محتاج تطبع اول 3columns واول 4rows , باستعمال طريقة الindex (ولكن دة فى حالة انك لا تعلم اسماء الvariables)
data.iloc[0:3,0:4]
#بمعنى انك مثلا محتاج تطبع أول 4columns وتطبع كل الrows, باستعمال طريقة الindex (ولكن دة فى حالة انك لا تعلم اسماء الvariables)
#to print all cloumns with aspecific rows(by index)
data.iloc[:,0:4]
#to print specific columns and rows(by th name of the variables)
data.loc["E":"I","C":"I"]
#to organize aspecific column(organizing the values it has)
#بمعنى اذا اردت ترتيب عمود معين ترتيب تنازلى للارقام اللى فية
data.sort_values("E")
#to delete aspecific rows from the dataframe(the default command is for rows)
#إذا كنت تريد مسح صف معين من الdataframe (وخصوصا لو البيانات كبيرة)-للعلم الاصل فى الكود انة بيمسح من الصف
data=data.drop("A")
#if U want to delete aspecific rows & columns from the dataframe
#{0 for 'index', 1 for 'columns'}, default 0
#اذا اردت مسح عمود وصف معين من الdataframe بنسمى الصف الاول ثم نكتب رقم الindex للعمود المراد مسحة (الاصل فى الصف)
data=data.drop("A",axis=1)
#ولكن اذا اردت ان تمسح عدد معين من وسط الاعمدة
data=data.drop(["C","E"],axis=1)