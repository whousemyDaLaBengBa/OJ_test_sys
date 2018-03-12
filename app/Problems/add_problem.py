from app import app as mainapp
from flask import render_template
from flask import request, session, redirect

#检查传参是否符合要求
def Check_Problem(TimeLimit, MemoryLimit, ProblemHead, ProblemDescription, Input, Output, SampleInput, SampleOutput):
    if (TimeLimit=='' or TimeLimit==None):#如果什么都不填则传回来的是''
        return False

    if (MemoryLimit=='' or MemoryLimit==None):#如果什么都不填则传回来的是''
        return False
    
    if (ProblemHead=='' or ProblemHead==None):#如果什么都不填则传回来的是''
        return False
    
    if (ProblemDescription=='' or ProblemDescription==None):
        return False

    if (Input=='' or Input==None):
        return False

    if (Output=='' or Output==None):
        return False

    if (SampleInput=='' or SampleInput==None):
        return False

    if (SampleOutput=='' or SampleOutput==None):
        return False

    return True


@mainapp.route('/problem/addproblem',methods=['GET','POST'])
def addproblem():
    try:
        TimeLimit = request.values.get("TimeLimit")
        MemoryLimit = request.values.get("MemoryLimit")
        ProblemHead = request.values.get("ProblemHead")
        ProblemDescription = request.values.get("ProblemDescription")
        Input = request.values.get("Input")
        Output = request.values.get("Output")
        SampleInput = request.values.get("SampleInput")
        SampleOutput = request.values.get("SampleOutput")
        Hint = request.values.get("Hint")
        Author = request.values.get("Author")
        Source = request.values.get("Source")
    except:
        return render_template("addproblem.html")
    else:
        if (Check_Problem(TimeLimit, MemoryLimit, ProblemHead, ProblemDescription, Input, Output, SampleInput, SampleOutput)==False):
            return render_template("addproblem.html")
        else:
            pass
            #这里写写入题目的函数