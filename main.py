from flask import Flask, render_template, redirect, url_for, send_from_directory
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, RadioField, IntegerField
from wtforms.validators import DataRequired, InputRequired, NumberRange
from utils import Configs, DataGenerator, makeConfig, ZipFiles
from utils.processText import Validate
import os
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config["SECRET_KEY"] = "ABCDFWA"


class LoginForm(FlaskForm):
    TextInput = TextAreaField("ChatMsg", validators=[DataRequired()])
    submit = SubmitField("检查数据格式")
    # submit1 = SubmitField("填写配置文件")


class CodeSubmitForm(FlaskForm):
    Code = TextAreaField("ChatMsg", validators=[InputRequired()])
    submit1 = SubmitField("提交代码")


Data = ''
res = ''


@app.route('/', methods=['GET', 'POST'])
def index():  # 主页面
    form = LoginForm()
    flag = False
    validate = True
    dataDescription = ''
    if form.validate_on_submit():  # 用户提交了文本就会触发这个
        global Data
        global res
        Data = form.TextInput.data
        res = Validate(Data)  # 对数据块进行合法性验证
        flag = True
        if res[0]:  # 如果数据格式没问题，那就跳转到config路由，也就是输入代码和造小样例的页面
            # dataDescription = "数据格式无误，原数据如下：", [str(Data)], "数据解释如下：", res[1]
            return redirect(url_for("config"))
        else:
            validate = False
            dataDescription = "数据格式有误，报错信息如下：", res[1], "原数据为：\n\n", [str(Data)]
    return render_template("index.html", Functions=Configs.configFun, form=form, flag=flag,
                           dataDescription=dataDescription, validate=validate)


@app.route('/config', methods=["GET", "POST"])
def config():  # 输入代码和造小样例的页面
    # res[2]为函数调用参数列表，res[1]为数据解释
    global Data
    global res
    X = DataGenerator.Generator()
    dataList = X.GenerateMini(res[2])  # 造一个小样例
    form = CodeSubmitForm()
    if Data == '':
        Data = "None"
        res = [[], ["None"]]
    dataDescription = "数据格式无误，原数据如下：", [str(Data)], "数据解释如下：", res[1]  # 能跳转到这里来的都是没问题的数据
    if form.validate_on_submit() or form.validate():  # 用户提交代码就会有这玩意
        z = X.GenerateDataFiles(res[2], 10, form.Code.data)  # 依据数据结果和代码造数据
        print("数据生成完毕，结果为：{}".format("Success" if z else "Fail"))
        if not z:
            form.Code.data = 'CodeERROR'  # 如果没有生成成功，那就把输入框里面的内容改成这玩意
        else:
            return redirect(url_for("final"))  # 否则跳转到最后填写problem.conf
        # dataList = [["1 2"], ['1 2 4 11 2 4 11 2 4 11 2 4 11 2 4 11 2 4 11 2 4 1 end'], ['1 4 53 2']]
    return render_template("config.html", dataDescription=dataDescription, form=form, dataList=dataList)


@app.route('/downloads/', methods=['GET', 'POST'])
def downloadsMiniData():  # 返回小样例的路由
    return send_from_directory(os.path.join(Configs.configLocationRoot(), "utils", "pythonCodeExcute"), "datain.txt", as_attachment=True)


class configForm(FlaskForm):
    builtin_checker = RadioField(u'解释器', validators=[DataRequired()])
    time_limit = IntegerField(u"时间限制（sec）", validators=[DataRequired(message=u"此字段需要输入哦"), NumberRange(min=1, max=2, message=u"时间不能设置的太离谱了哦")])
    memory_limit = IntegerField(u"空间限制（MB）", validators=[DataRequired(message=u"此字段需要输入哦"), NumberRange(min=128, max=256, message=u"空间不能设置的太离谱了哦")])
    submit = SubmitField(u"生成ZIP!")


@app.route('/configfile', methods=["GET", "POST"])
def final():  # 填写problem.conf的页面
    Form = configForm()
    Form.builtin_checker.choices = [("1", "ncmp"), ("2", "fcmp"), ("3", "wcmp")]
    if Form.validate_on_submit():
        mem_lim = Form.memory_limit.data
        tim_lim = Form.time_limit.data
        checker = "ncmp" if Form.builtin_checker.data == 1 else("fcmp" if Form.builtin_checker.data == 2 else "wcmp")
        print(mem_lim, tim_lim, checker)
        makeConfig.processConf(tim_lim, mem_lim, checker)
        return redirect(url_for("returnZIP"))
    return render_template("makeZIP.html", form=Form)


@app.route('/getZIP', methods=["GET", "POST"])
def returnZIP():  # 返回ZIP的路由
    FileList = ["w{}.in".format(K) for K in range(1, 11, 1)]
    FileList += ["w{}.out".format(K) for K in range(1, 11, 1)]
    FileList += ["problem.conf"]
    ZipFiles.Pack(Configs.configLocationDataPool(), FileList, "output.zip")
    return send_from_directory(os.path.join(Configs.configLocationDataPool()), "output.zip",
                               as_attachment=True)


if __name__ == '__main__':
    app.run(port=3690, debug=True)
