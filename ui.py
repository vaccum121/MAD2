# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1274, 516)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label.setObjectName("label")
        self.radio_ffe = QtWidgets.QRadioButton(Form)
        self.radio_ffe.setGeometry(QtCore.QRect(20, 40, 61, 21))
        self.radio_ffe.setChecked(True)
        self.radio_ffe.setObjectName("radio_ffe")
        self.radio_ccp = QtWidgets.QRadioButton(Form)
        self.radio_ccp.setGeometry(QtCore.QRect(80, 40, 61, 21))
        self.radio_ccp.setObjectName("radio_ccp")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 121, 16))
        self.label_2.setObjectName("label_2")
        self.check_use_N = QtWidgets.QCheckBox(Form)
        self.check_use_N.setGeometry(QtCore.QRect(20, 60, 121, 21))
        self.check_use_N.setObjectName("check_use_N")
        self.function = QtWidgets.QLineEdit(Form)
        self.function.setGeometry(QtCore.QRect(20, 100, 171, 23))
        self.function.setObjectName("function")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 57, 15))
        self.label_4.setObjectName("label_4")
        self.d = QtWidgets.QLineEdit(Form)
        self.d.setGeometry(QtCore.QRect(50, 170, 31, 23))
        self.d.setObjectName("d")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 16, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 21, 16))
        self.label_6.setObjectName("label_6")
        self.m = QtWidgets.QLineEdit(Form)
        self.m.setGeometry(QtCore.QRect(50, 200, 31, 23))
        self.m.setObjectName("m")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 230, 161, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(10, 250, 57, 15))
        self.label_8.setObjectName("label_8")
        self.u1_del = QtWidgets.QLineEdit(Form)
        self.u1_del.setGeometry(QtCore.QRect(80, 250, 113, 23))
        self.u1_del.setObjectName("u1_del")
        self.u2_del = QtWidgets.QLineEdit(Form)
        self.u2_del.setGeometry(QtCore.QRect(80, 280, 113, 23))
        self.u2_del.setObjectName("u2_del")
        self.u3_del = QtWidgets.QLineEdit(Form)
        self.u3_del.setGeometry(QtCore.QRect(80, 310, 113, 23))
        self.u3_del.setObjectName("u3_del")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(10, 280, 57, 15))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(10, 310, 57, 15))
        self.label_10.setObjectName("label_10")
        self.u2_int = QtWidgets.QLineEdit(Form)
        self.u2_int.setGeometry(QtCore.QRect(80, 390, 113, 23))
        self.u2_int.setObjectName("u2_int")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(10, 340, 161, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(10, 360, 57, 15))
        self.label_12.setObjectName("label_12")
        self.u3_int = QtWidgets.QLineEdit(Form)
        self.u3_int.setGeometry(QtCore.QRect(80, 420, 113, 23))
        self.u3_int.setObjectName("u3_int")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(10, 420, 57, 15))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(10, 390, 57, 15))
        self.label_14.setObjectName("label_14")
        self.u1_int = QtWidgets.QLineEdit(Form)
        self.u1_int.setGeometry(QtCore.QRect(80, 360, 113, 23))
        self.u1_int.setObjectName("u1_int")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(260, 20, 151, 16))
        self.label_15.setObjectName("label_15")
        self.linear_model = QtWidgets.QLabel(Form)
        self.linear_model.setGeometry(QtCore.QRect(260, 40, 961, 16))
        self.linear_model.setText("")
        self.linear_model.setObjectName("linear_model")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(260, 70, 151, 16))
        self.label_17.setObjectName("label_17")
        self.quad_model = QtWidgets.QLabel(Form)
        self.quad_model.setGeometry(QtCore.QRect(260, 90, 961, 16))
        self.quad_model.setText("")
        self.quad_model.setObjectName("quad_model")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(260, 120, 161, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(260, 160, 101, 20))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(260, 140, 71, 16))
        self.label_21.setObjectName("label_21")
        self.quad_model_adeq = QtWidgets.QLabel(Form)
        self.quad_model_adeq.setGeometry(QtCore.QRect(360, 160, 57, 15))
        self.quad_model_adeq.setText("")
        self.quad_model_adeq.setObjectName("quad_model_adeq")
        self.linear_model_adeq = QtWidgets.QLabel(Form)
        self.linear_model_adeq.setGeometry(QtCore.QRect(360, 140, 57, 16))
        self.linear_model_adeq.setText("")
        self.linear_model_adeq.setObjectName("linear_model_adeq")
        self.label_24 = QtWidgets.QLabel(Form)
        self.label_24.setGeometry(QtCore.QRect(290, 240, 31, 16))
        self.label_24.setObjectName("label_24")
        self.fish_lin = QtWidgets.QLineEdit(Form)
        self.fish_lin.setGeometry(QtCore.QRect(290, 260, 31, 23))
        self.fish_lin.setObjectName("fish_lin")
        self.stud_lin = QtWidgets.QLineEdit(Form)
        self.stud_lin.setGeometry(QtCore.QRect(290, 290, 31, 23))
        self.stud_lin.setObjectName("stud_lin")
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setGeometry(QtCore.QRect(260, 220, 57, 15))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(Form)
        self.label_26.setGeometry(QtCore.QRect(220, 290, 61, 20))
        self.label_26.setObjectName("label_26")
        self.label_28 = QtWidgets.QLabel(Form)
        self.label_28.setGeometry(QtCore.QRect(225, 260, 51, 20))
        self.label_28.setObjectName("label_28")
        self.koh_lin = QtWidgets.QLineEdit(Form)
        self.koh_lin.setGeometry(QtCore.QRect(290, 320, 31, 23))
        self.koh_lin.setObjectName("koh_lin")
        self.label_27 = QtWidgets.QLabel(Form)
        self.label_27.setGeometry(QtCore.QRect(220, 320, 61, 16))
        self.label_27.setObjectName("label_27")
        self.stud_quad = QtWidgets.QLineEdit(Form)
        self.stud_quad.setGeometry(QtCore.QRect(330, 290, 31, 23))
        self.stud_quad.setObjectName("stud_quad")
        self.fish_quad = QtWidgets.QLineEdit(Form)
        self.fish_quad.setGeometry(QtCore.QRect(330, 260, 31, 23))
        self.fish_quad.setObjectName("fish_quad")
        self.koh_quad = QtWidgets.QLineEdit(Form)
        self.koh_quad.setGeometry(QtCore.QRect(330, 320, 31, 23))
        self.koh_quad.setObjectName("koh_quad")
        self.label_29 = QtWidgets.QLabel(Form)
        self.label_29.setGeometry(QtCore.QRect(330, 240, 21, 16))
        self.label_29.setObjectName("label_29")
        self.calc_btn = QtWidgets.QPushButton(Form)
        self.calc_btn.setGeometry(QtCore.QRect(220, 360, 501, 121))
        self.calc_btn.setObjectName("calc_btn")
        self.label_22 = QtWidgets.QLabel(Form)
        self.label_22.setGeometry(QtCore.QRect(420, 240, 71, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_23.setGeometry(QtCore.QRect(420, 260, 101, 20))
        self.label_23.setObjectName("label_23")
        self.linear_model_adeq_d = QtWidgets.QLabel(Form)
        self.linear_model_adeq_d.setGeometry(QtCore.QRect(520, 240, 57, 16))
        self.linear_model_adeq_d.setText("")
        self.linear_model_adeq_d.setObjectName("linear_model_adeq_d")
        self.quad_model_adeq_d = QtWidgets.QLabel(Form)
        self.quad_model_adeq_d.setGeometry(QtCore.QRect(520, 260, 57, 15))
        self.quad_model_adeq_d.setText("")
        self.quad_model_adeq_d.setObjectName("quad_model_adeq_d")
        self.label_30 = QtWidgets.QLabel(Form)
        self.label_30.setGeometry(QtCore.QRect(420, 220, 161, 16))
        self.label_30.setObjectName("label_30")
        self.exp_num = QtWidgets.QLineEdit(Form)
        self.exp_num.setGeometry(QtCore.QRect(150, 130, 31, 23))
        self.exp_num.setObjectName("exp_num")
        self.num2 = QtWidgets.QRadioButton(Form)
        self.num2.setGeometry(QtCore.QRect(90, 10, 41, 23))
        self.num2.setObjectName("num2")
        self.num3 = QtWidgets.QRadioButton(Form)
        self.num3.setGeometry(QtCore.QRect(130, 10, 41, 23))
        self.num3.setObjectName("num3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Тип плана"))
        self.radio_ffe.setText(_translate("Form", "ПФЭ"))
        self.radio_ccp.setText(_translate("Form", "ЦКП"))
        self.label_2.setText(_translate("Form", "Функция отклика"))
        self.check_use_N.setText(_translate("Form", "N в критериях"))
        self.function.setText(_translate("Form", "1+u1+u2"))
        self.label_3.setText(_translate("Form", "Кол. экспериментов"))
        self.label_4.setText(_translate("Form", "Помехи"))
        self.d.setText(_translate("Form", "1"))
        self.label_5.setText(_translate("Form", "D"))
        self.label_6.setText(_translate("Form", "M"))
        self.m.setText(_translate("Form", "0"))
        self.label_7.setText(_translate("Form", "Базовые точки"))
        self.label_8.setText(_translate("Form", "u1"))
        self.u1_del.setText(_translate("Form", "0"))
        self.u2_del.setText(_translate("Form", "0"))
        self.u3_del.setText(_translate("Form", "0"))
        self.label_9.setText(_translate("Form", "u2"))
        self.label_10.setText(_translate("Form", "u3"))
        self.u2_int.setText(_translate("Form", "5"))
        self.label_11.setText(_translate("Form", "Интервалы покачивания"))
        self.label_12.setText(_translate("Form", "u1"))
        self.u3_int.setText(_translate("Form", "5"))
        self.label_13.setText(_translate("Form", "u3"))
        self.label_14.setText(_translate("Form", "u2"))
        self.u1_int.setText(_translate("Form", "5"))
        self.label_15.setText(_translate("Form", "Линейная модель"))
        self.label_17.setText(_translate("Form", "Квадратичная модель"))
        self.label_19.setText(_translate("Form", "Адекватность модели"))
        self.label_20.setText(_translate("Form", "Квадратичная"))
        self.label_21.setText(_translate("Form", "Линейная"))
        self.label_24.setText(_translate("Form", "Лин"))
        self.fish_lin.setText(_translate("Form", "1.43"))
        self.stud_lin.setText(_translate("Form", "0.68"))
        self.label_25.setText(_translate("Form", "Помехи"))
        self.label_26.setText(_translate("Form", "Стьюдент"))
        self.label_28.setText(_translate("Form", "Фишер"))
        self.koh_lin.setText(_translate("Form", "6.2"))
        self.label_27.setText(_translate("Form", "Кохрена"))
        self.stud_quad.setText(_translate("Form", "0.68"))
        self.fish_quad.setText(_translate("Form", "1.43"))
        self.koh_quad.setText(_translate("Form", "6.2"))
        self.label_29.setText(_translate("Form", "Кв"))
        self.calc_btn.setText(_translate("Form", "Вычислить"))
        self.label_22.setText(_translate("Form", "Лин"))
        self.label_23.setText(_translate("Form", "Квад"))
        self.label_30.setText(_translate("Form", "Дисперсия адекватности"))
        self.exp_num.setText(_translate("Form", "15"))
        self.num2.setText(_translate("Form", "&2"))
        self.num3.setText(_translate("Form", "&3"))