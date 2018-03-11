from app import app as mainapp
from flask import render_template
from flask import request, session, redirect

#检查传参是否符合要求
def Check_Problem(ProblemHead, ProblemDescription, Input, Output, SampleInput, SampleOutput, Hint, Author):
    if (ProblemHead==''):#如果什么都不填则传回来的是''
        return False
    
    if (ProblemDescription==''):
        return False

    if (Input==''):
        return False

    if (Output==''):
        return False

    if (SampleInput==''):
        return False

    if (SampleOutput==''):
        return False

    return True


@mainapp.route('/problem/addproblem',methods=['GET','POST'])
def addproblem():
    try:
        ProblemHead = request.values.get("ProblemHead")
        ProblemDescription = request.values.get("ProblemDescription")
        Input = request.values.get("Input")
        Output = request.values.get("Output")
        SampleInput = request.values.get("SampleInput")
        SampleOutput = request.values.get("SampleOutput")
        Hint = request.values.get("Hint")
        Author = request.values.get("Author")
    except:
        return render_template("addproblem.html")
    else:
        if (Check_Problem(ProblemHead, ProblemDescription, Input, Output, SampleInput, SampleOutput, Hint, Author)==False):
            return render_template("addproblem.html")
        else:
            pass